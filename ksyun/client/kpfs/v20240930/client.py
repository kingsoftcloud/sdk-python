import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KpfsClient(AbstractClient):
    _apiVersion = '2024-09-30'
    _endpoint = 'kpfs.api.ksyun.com'
    _service = 'kpfs'
    def DescribeFileSystemList(self, request):
        """文件系统列表查询
        :param request: Request instance for DescribeFileSystemList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeFileSystemListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFileSystemList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeDirQuotaList(self, request):
        """查询目录配额列表
        :param request: Request instance for DescribeDirQuotaList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDirQuotaListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDirQuotaList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DeleteDirQuota(self, request):
        """删除目录配额
        :param request: Request instance for DeleteDirQuota.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteDirQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDirQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def UpdateDirQuota(self, request):
        """修改目录配额
        :param request: Request instance for UpdateDirQuota.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdateDirQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDirQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def CreateDirQuota(self, request):
        """新建目录配额
        :param request: Request instance for CreateDirQuota.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateDirQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDirQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeSubDirList(self, request):
        """查询文件系统或特定目录的子目录列表
        :param request: Request instance for DescribeSubDirList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeSubDirListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSubDirList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DeleteDir(self, request):
        """删除文件系统目录
        :param request: Request instance for DeleteDir.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteDirRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDir", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def UpdateDir(self, request):
        """修改文件系统目录
        :param request: Request instance for UpdateDir.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdateDirRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDir", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def CreateDir(self, request):
        """新建文件系统目录
        :param request: Request instance for CreateDir.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateDirRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDir", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeDirQuota(self, request):
        """查询指定目录配额
        :param request: Request instance for DescribeDirQuota.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDirQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDirQuota", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


