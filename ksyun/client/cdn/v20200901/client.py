import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class CdnClient(AbstractClient):
    _apiVersion = '2020-09-01'
    _endpoint = 'cdn.api.ksyun.com'
    _service = 'cdn'
    def CreateUserUsageDataExportTask(self, request):
        """创建用量导表任务
        :param request: Request instance for CreateUserUsageDataExportTask.
        :type request: :class:`ksyun.client.cdn.v20200901.models.CreateUserUsageDataExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateUserUsageDataExportTask", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def GetUserUsageDataExportTask(self, request):
        """获取用量导表任务
        :param request: Request instance for GetUserUsageDataExportTask.
        :type request: :class:`ksyun.client.cdn.v20200901.models.GetUserUsageDataExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetUserUsageDataExportTask", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteUserUsageDataExportTask(self, request):
        """删除用量导表任务
        :param request: Request instance for DeleteUserUsageDataExportTask.
        :type request: :class:`ksyun.client.cdn.v20200901.models.DeleteUserUsageDataExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteUserUsageDataExportTask", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def GetDomainUsageData(self, request):
        """用量查询接口
        :param request: Request instance for GetDomainUsageData.
        :type request: :class:`ksyun.client.cdn.v20200901.models.GetDomainUsageDataRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDomainUsageData", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateUsageDetailDataExportTask(self, request):
        """创建明细导表任务
        :param request: Request instance for CreateUsageDetailDataExportTask.
        :type request: :class:`ksyun.client.cdn.v20200901.models.CreateUsageDetailDataExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateUsageDetailDataExportTask", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def GetUsageDetailDataExportTask(self, request):
        """获取明细导出任务
        :param request: Request instance for GetUsageDetailDataExportTask.
        :type request: :class:`ksyun.client.cdn.v20200901.models.GetUsageDetailDataExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetUsageDetailDataExportTask", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteUsageDetailDataExportTask(self, request):
        """删除明细导表任务
        :param request: Request instance for DeleteUsageDetailDataExportTask.
        :type request: :class:`ksyun.client.cdn.v20200901.models.DeleteUsageDetailDataExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteUsageDetailDataExportTask", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


