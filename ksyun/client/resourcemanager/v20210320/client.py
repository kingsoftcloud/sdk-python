import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class ResourcemanagerClient(AbstractClient):
    _apiVersion = '2021-03-20'
    _endpoint = 'resourcemanager.api.ksyun.com'
    _service = 'resourcemanager'
    def CreateFolder(self, request):
        """创建资源夹
        :param request: Request instance for CreateFolder.
        :type request: :class:`ksyun.client.resourcemanager.v20210320.models.CreateFolderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateFolder", params, "application/x-www-form-urlencoded")
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


    def DeleteFolder(self, request):
        """删除资源夹
        :param request: Request instance for DeleteFolder.
        :type request: :class:`ksyun.client.resourcemanager.v20210320.models.DeleteFolderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteFolder", params, "application/x-www-form-urlencoded")
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


    def UpdateFolder(self, request):
        """更新资源夹
        :param request: Request instance for UpdateFolder.
        :type request: :class:`ksyun.client.resourcemanager.v20210320.models.UpdateFolderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateFolder", params, "application/x-www-form-urlencoded")
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


    def ListAccountsForParent(self, request):
        """某资源夹下所有用户
        :param request: Request instance for ListAccountsForParent.
        :type request: :class:`ksyun.client.resourcemanager.v20210320.models.ListAccountsForParentRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListAccountsForParent", params, "application/x-www-form-urlencoded")
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


    def MoveAccount(self, request):
        """移动成员到其他资源夹
        :param request: Request instance for MoveAccount.
        :type request: :class:`ksyun.client.resourcemanager.v20210320.models.MoveAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("MoveAccount", params, "application/x-www-form-urlencoded")
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


    def UpdateAccount(self, request):
        """更新成员
        :param request: Request instance for UpdateAccount.
        :type request: :class:`ksyun.client.resourcemanager.v20210320.models.UpdateAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateAccount", params, "application/x-www-form-urlencoded")
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


    def ListAccounts(self, request):
        """查看整个资源目录下的所有成员信息
        :param request: Request instance for ListAccounts.
        :type request: :class:`ksyun.client.resourcemanager.v20210320.models.ListAccountsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListAccounts", params, "application/x-www-form-urlencoded")
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


    def ListFolders(self, request):
        """资源夹列表
        :param request: Request instance for ListFolders.
        :type request: :class:`ksyun.client.resourcemanager.v20210320.models.ListFoldersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListFolders", params, "application/x-www-form-urlencoded")
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


