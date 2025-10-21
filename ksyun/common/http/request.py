#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
import requests
import certifi

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException

logger = logging.getLogger("ksyun_sdk_common")


def _get_proxy_from_env(host, varname="HTTPS_PROXY"):
    no_proxy = os.environ.get("NO_PROXY") or os.environ.get("no_proxy")
    if no_proxy and host in no_proxy:
        return None
    return os.environ.get(varname.lower()) or os.environ.get(varname.upper())


class ProxyConnection(object):
    def __init__(self, host, timeout=60, proxy=None, certification=None, is_http=False):
        self.request_host = host
        self.certification = certification
        if not certification:
            self.certification = certifi.where()
        self.timeout = timeout
        self.proxy = None
        if is_http:
            proxy = proxy or _get_proxy_from_env(host, varname="HTTP_PROXY")
        else:
            proxy = proxy or _get_proxy_from_env(host, varname="HTTPS_PROXY")
        if proxy:
            if is_http:
                self.proxy = {"http": proxy}
            else:
                self.proxy = {"https": proxy}
        self.request_length = 0

    def request(self, method, url, body=None, headers={}, auth=None):
        self.request_length = 0
        headers.setdefault("Host", self.request_host)
        return requests.request(method=method,
                                url=url,
                                data=body,
                                headers=headers,
                                proxies=self.proxy,
                                verify=self.certification,
                                timeout=self.timeout,
                                auth=auth)


class ApiRequest(object):
    def __init__(self, host, req_timeout=60, debug=False, proxy=None, is_http=False, certification=None):
        self.conn = ProxyConnection(host, timeout=req_timeout, proxy=proxy, certification=certification,
                                    is_http=is_http)
        url = urlparse(host)
        if not url.hostname:
            if is_http:
                host = "http://" + host
            else:
                host = "https://" + host
        self.host = host
        self.req_timeout = req_timeout
        self.keep_alive = False
        self.debug = debug
        self.request_size = 0
        self.response_size = 0

    def _build_url(self, base_url, path=None, query_params=None):
        """Build complete URL from base_url, path and query parameters.

        Ensures no double slashes between domain and path.

        :param base_url: Base URL (scheme + domain)
        :type base_url: str
        :param path: URL path
        :type path: str
        :param query_params: Query parameters
        :type query_params: str
        :return: Complete URL
        :rtype: str
        """
        # Start with base URL, remove trailing slash if present
        url = base_url.rstrip('/')

        # Add path if provided
        if path:
            # Ensure path starts with /
            if not path.startswith('/'):
                path = '/' + path
            url += path

        # Add query parameters if provided
        if query_params:
            url += '?' + query_params

        return url

    def set_req_timeout(self, req_timeout):
        self.req_timeout = req_timeout

    def is_keep_alive(self):
        return self.keep_alive

    def set_keep_alive(self, flag=True):
        self.keep_alive = flag

    def set_debug(self, debug):
        self.debug = debug

    def _request(self, req_inter):
        if self.keep_alive:
            req_inter.header["Connection"] = "Keep-Alive"
        if self.debug:
            logger.debug("SendRequest %s" % req_inter)

        if req_inter.method == 'GET':
            # For GET requests, parameters are in the query string (req_inter.data)
            req_inter_url = self._build_url(self.host, req_inter.uri, req_inter.data)
            return self.conn.request(req_inter.method, req_inter_url, None, req_inter.header, req_inter.auth)
        elif req_inter.method == 'POST' or req_inter.method == 'PUT' or req_inter.method == 'DELETE':
            # For POST/PUT/DELETE, use uri_params for query string if present
            req_inter_url = self._build_url(self.host, req_inter.uri, req_inter.uri_params if req_inter.uri_params else None)
            return self.conn.request(req_inter.method, req_inter_url, req_inter.data, req_inter.header, req_inter.auth)
        else:
            raise KsyunSDKException("ClientParamsError", 'Method only support (GET, POST, PUT, DELETE)')

    def send_request(self, req_inter):
        try:
            http_resp = self._request(req_inter)
            headers = dict(http_resp.headers)
            resp_inter = ResponseInternal(status=http_resp.status_code, header=headers, data=http_resp.text)
            self.request_size = self.conn.request_length
            self.response_size = len(resp_inter.data)
            logger.debug("GetResponse %s" % resp_inter)
            return resp_inter
        except Exception as e:
            raise KsyunSDKException("ClientNetworkError", str(e))


class RequestInternal(object):
    def __init__(self, host="", method="", uri="", header=None, data="", auth=None):
        if header is None:
            header = {}
        self.host = host
        self.method = method
        self.uri = uri
        self.header = header
        self.data = data
        self.auth = auth
        self.uri_params = None  # Query parameters for POST/PUT/DELETE requests

    def __str__(self):
        headers = "\n".join("%s: %s" % (k, v) for k, v in self.header.items())
        return ("Host: %s\nMethod: %s\nUri: %s\nHeader: %s\nData: %s\n"
                % (self.host, self.method, self.uri, headers, self.data))


class ResponseInternal(object):
    def __init__(self, status=0, header=None, data=""):
        if header is None:
            header = {}
        self.status = status
        self.header = header
        self.data = data

    def __str__(self):
        headers = "\n".join("%s: %s" % (k, v) for k, v in self.header.items())
        return ("Status: %s\nHeader: %s\nData: %s\n"
                % (self.status, headers, self.data))
