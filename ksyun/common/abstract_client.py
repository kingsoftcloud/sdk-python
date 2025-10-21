# -*- coding: utf-8 -*-
#
# Copyright 2022 Ksyun Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
import json
import sys
import uuid
import warnings
import logging
import logging.handlers

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import ksyun
from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.exception import KsyunSDKException as SDKError
from ksyun.common.http.request import ApiRequest
from ksyun.common.http.request import RequestInternal
from ksyun.common.profile.client_profile import ClientProfile
from requests_aws4auth import AWS4Auth

warnings.filterwarnings("ignore")

_json_content = 'application/json'
_multipart_content = 'multipart/form-data'
_form_urlencoded_content = 'application/x-www-form-urlencoded'
_octet_stream = "application/octet-stream"
_x_protobuf = "application/x-protobuf"


class EmptyHandler(logging.Handler):
    def emit(self, message):
        pass


LOGGER_NAME = "ksyun_sdk_common"
logger = logging.getLogger(LOGGER_NAME)
logger.addHandler(EmptyHandler())


class AbstractClient(object):
    _requestPath = '/'
    _params = {}
    _apiVersion = ''
    _endpoint = ''
    _service = ''
    _sdkVersion = 'SDK_PYTHON_%s' % ksyun.__version__
    _default_content_type = _form_urlencoded_content
    paramsFormat = True
    FMT = '%(asctime)s %(process)d %(filename)s L%(lineno)s %(levelname)s %(message)s'

    def __init__(self, credential, region, profile=None):
        if credential is None:
            raise KsyunSDKException(
                "InvalidCredential", "Credential is None or invalid")
        self.credential = credential
        self.region = region
        self.profile = ClientProfile() if profile is None else profile
        is_http = True if self.profile.httpProfile.scheme == "http" else False
        self.request = ApiRequest(
            self._get_endpoint(),
            req_timeout=self.profile.httpProfile.reqTimeout,
            proxy=self.profile.httpProfile.proxy,
            is_http=is_http,
            certification=self.profile.httpProfile.certification
        )
        if self.profile.httpProfile.keepAlive:
            self.request.set_keep_alive()

    def _fix_params(self, params):
        if not isinstance(params, (dict,)):
            return params
        if not self.paramsFormat:
            return params

        return self._format_params(None, params)

    def _format_params(self, prefix, params):
        d = {}
        if params is None:
            return d

        if not isinstance(params, (tuple, list, dict)):
            d[prefix] = params
            return d

        if isinstance(params, (list, tuple)):
            for idx, item in enumerate(params):
                if prefix:
                    key = "{0}.{1}".format(prefix, idx)
                else:
                    key = "{0}".format(idx)
                d.update(self._format_params(key, item))
            return d

        if isinstance(params, dict):
            for k, v in params.items():
                if prefix:
                    key = '{0}.{1}'.format(prefix, k)
                else:
                    key = '{0}'.format(k)
                d.update(self._format_params(key, v))
            return d

        raise KsyunSDKException("ClientParamsError", "some params type error")

    def _build_req_inter(self, action, params, req_inter, options=None):
        if self.profile.signMethod in ("HMAC-SHA1", "HMAC-SHA256", "AWS4-HMAC-SHA256"):
            self._build_req_with_signature(action, params, req_inter, options)
        else:
            raise KsyunSDKException("ClientError", "Invalid signature method.")

    def _build_req_with_signature(self, action, params, req, options=None):
        uri_params = dict()
        if not (options and options.get("IsPostJson")):
            params = copy.deepcopy(self._fix_params(params))
        else:
            uri_params['Action'] = action[0].upper() + action[1:]
            uri_params['Version'] = self._apiVersion


        params['Service'] = self._service
        params['Action'] = action[0].upper() + action[1:]
        params['Version'] = self._apiVersion
        params['SdkVersion'] = self._sdkVersion

        if self.region:
            params['Region'] = self.region
        if self.credential.secret_id:
            params['Accesskey'] = self.credential.secret_id
        if self.profile.language:
            params['Language'] = self.profile.language

        # 请求头
        req.header["Accept"] = _json_content
        content_type = self._default_content_type

        # 支持上传文件和json传参
        options = options or {}
        if options.get("IsPostJson"):
            content_type = _json_content
        if options.get("IsMultipart"):
            content_type = _multipart_content
        if options.get("IsOctetStream"):
            content_type = _octet_stream
        if options.get("IsXProtobuf"):
            content_type = _x_protobuf
        req.header["Content-Type"] = content_type

        # GET上传文件报错
        if req.method == "GET" and content_type == _multipart_content:
            raise SDKError("ClientError", "Invalid request method GET for multipart.")
        # 非get请求在url添加 Action、Version
        if req.method != "GET":
            params

        # 请求数据转换
        if content_type == _form_urlencoded_content:
            params = copy.deepcopy(self._fix_params(params))
            req.data = urlencode(params)
        elif content_type == _json_content:
            req.data = json.dumps(params)
        elif content_type == _multipart_content:
            boundary = uuid.uuid4().hex
            req.header["Content-Type"] = content_type + "; boundary=" + boundary
            req.data = self._get_multipart_body(params, boundary, options)

        req.uri_params = urlencode(uri_params)

        # 组装签名
        auth = AWS4Auth(str(self.credential.secret_id), str(self.credential.secret_key), self.region, self._service)
        req.auth = auth

    # it must return bytes instead of string
    def _get_multipart_body(self, params, boundary, options=None):
        if options is None:
            options = {}
        # boundary and params key will never contain unicode characters
        boundary = boundary.encode()
        binparas = options.get("BinaryParams", [])
        body = b''
        for k, v in params.items():
            kbytes = k.encode()
            body += b'--%s\r\n' % boundary
            body += b'Content-Disposition: form-data; name="%s"' % kbytes
            if k in binparas:
                body += b'; filename="%s"\r\n' % kbytes
            else:
                body += b"\r\n"
                if isinstance(v, list) or isinstance(v, dict):
                    v = json.dumps(v)
                    body += b'Content-Type: application/json\r\n'
            if sys.version_info[0] == 3 and isinstance(v, type("")):
                v = v.encode()
            body += b'\r\n%s\r\n' % v
        if body != b'':
            body += b'--%s--\r\n' % boundary
        return body

    def _check_status(self, resp_inter):
        if resp_inter.status != 200:
            raise KsyunSDKException("ServerNetworkError", resp_inter.data)

    def _get_service_domain(self):
        rootDomain = self.profile.httpProfile.rootDomain
        return self._service + "." + rootDomain

    def _get_endpoint(self):
        endpoint = self.profile.httpProfile.endpoint
        if endpoint is None:
            endpoint = self._get_service_domain()
        return endpoint


    def call(self, action, params, options=None):
        # Use custom path from HttpProfile if available, otherwise use default _requestPath
        request_path = self.profile.httpProfile.path if self.profile.httpProfile.path else self._requestPath
        req = RequestInternal(self._get_endpoint(), self.profile.httpProfile.reqMethod, request_path)
        self._build_req_inter(action, params, req, options)
        resp_inter = self.request.send_request(req)
        self._check_status(resp_inter)
        data = resp_inter.data
        return data

    def call_octet_stream(self, action, headers, body):
        """
        Invoke API with application/ocet-stream content-type.

        :type action: str
        :param action: Specific API action name.
        :type headers: dict
        :param headers: Header parameters for this API.
        :type body: bytes
        :param body: Bytes of requested body
        """
        if self.profile.signMethod != "HMAC-SHA256":
            raise SDKError("ClientError", "Invalid signature method.")
        if self.profile.httpProfile.reqMethod != "POST":
            raise SDKError("ClientError", "Invalid request method.")

        # Use custom path from HttpProfile if available, otherwise use default _requestPath
        request_path = self.profile.httpProfile.path if self.profile.httpProfile.path else self._requestPath
        req = RequestInternal(self._get_endpoint(),
                              self.profile.httpProfile.reqMethod,
                              request_path)
        for key in headers:
            req.header[key] = headers[key]
        req.data = body
        options = {"IsOctetStream": True}
        self._build_req_inter(action, None, req, options)

        resp = self.request.send_request(req)
        self._check_status(resp)
        data = resp.data
        json_rsp = json.loads(data)
        if "Error" in json_rsp:
            code = json_rsp["Error"]["Code"]
            message = json_rsp["Error"]["Message"]
            reqid = json_rsp["RequestId"]
            raise KsyunSDKException(code, message, reqid)
        return data

    def call_json(self, action, params):
        """
        Call api with json object and return with json object.

        :type action: str
        :param action: api name
        :type params: dict
        :param params: params with this action
        """
        options = {'IsPostJson': True}
        body = self.call(action, params, options)
        response = json.loads(body)
        if "Error" not in response:
            return body
        else:
            code = response["Error"]["Code"]
            message = response["Error"]["Message"]
            reqid = response["RequestId"]
            raise KsyunSDKException(code, message, reqid)
    def call_judge(self, action, params, content_type,options=None):
        method = self.profile.httpProfile.reqMethod
        if method and method == "POST" and 'application/json' in content_type:
            return self.call_json(action, params)
        else:
            return self.call(action, params, options)

    def set_stream_logger(self, stream=None, level=logging.DEBUG, log_format=None):
        """
        Add a stream handler

        :type stream: IO[str]
        :param stream: e.g. ``sys.stdout`` ``sys.stdin`` ``sys.stderr``
        :type level: int
        :param level: Logging level, e.g. ``logging.INFO``
        :type log_format: str
        :param log_format: Log message format
        """
        log = logging.getLogger(LOGGER_NAME)
        log.setLevel(level)
        sh = logging.StreamHandler(stream)
        sh.setLevel(level)
        if log_format is None:
            log_format = self.FMT
        formatter = logging.Formatter(log_format)
        sh.setFormatter(formatter)
        log.addHandler(sh)

    def set_file_logger(self, file_path, level=logging.DEBUG, log_format=None):
        """
        Add a file handler

        :type file_path: str
        :param file_path: path of log file
        :type level: int
        :param level: Logging level, e.g. ``logging.INFO``
        :type log_format: str
        :param log_format: Log message format
        """
        log = logging.getLogger(LOGGER_NAME)
        log.setLevel(level)
        mb = 1024 * 1024
        fh = logging.handlers.RotatingFileHandler(file_path, maxBytes=512 * mb, backupCount=10)
        fh.setLevel(level)
        if log_format is None:
            log_format = self.FMT
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        log.addHandler(fh)

    def set_default_logger(self):
        """
        Set default log handler
        """
        log = logging.getLogger(LOGGER_NAME)
        log.handlers = []
        logger.addHandler(EmptyHandler())
