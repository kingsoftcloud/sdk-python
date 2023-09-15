import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KceClient(AbstractClient):
    _apiVersion = '2018-03-14'
    _endpoint = 'kce.api.ksyun.com'
    _service = 'kce'
    def CreateRepoNamespace(self, request):
        """创建命名空间
        :param request: Request instance for CreateRepoNamespace.
        :type request: :class:`ksyun.client.kce.v20180314.models.CreateRepoNamespaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRepoNamespace", params, "application/x-www-form-urlencoded")
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


    def DescribeRepoNamespace(self, request):
        """查询命名空间
        :param request: Request instance for DescribeRepoNamespace.
        :type request: :class:`ksyun.client.kce.v20180314.models.DescribeRepoNamespaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRepoNamespace", params, "application/x-www-form-urlencoded")
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


    def ModifyRepoNamespaceType(self, request):
        """修改命名空间属性
        :param request: Request instance for ModifyRepoNamespaceType.
        :type request: :class:`ksyun.client.kce.v20180314.models.ModifyRepoNamespaceTypeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyRepoNamespaceType", params, "application/x-www-form-urlencoded")
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


    def RepoNamespaceExist(self, request):
        """查询命名空间是否存在
        :param request: Request instance for RepoNamespaceExist.
        :type request: :class:`ksyun.client.kce.v20180314.models.RepoNamespaceExistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RepoNamespaceExist", params, "application/x-www-form-urlencoded")
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


    def CreateRepository(self, request):
        """创建镜像仓库
        :param request: Request instance for CreateRepository.
        :type request: :class:`ksyun.client.kce.v20180314.models.CreateRepositoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRepository", params, "application/x-www-form-urlencoded")
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


    def DeleteRepository(self, request):
        """删除镜像仓库
        :param request: Request instance for DeleteRepository.
        :type request: :class:`ksyun.client.kce.v20180314.models.DeleteRepositoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRepository", params, "application/x-www-form-urlencoded")
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


    def DescribeRepository(self, request):
        """查询镜像仓库
        :param request: Request instance for DescribeRepository.
        :type request: :class:`ksyun.client.kce.v20180314.models.DescribeRepositoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRepository", params, "application/x-www-form-urlencoded")
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


    def DescribePublicRepository(self, request):
        """查询ksyun hub镜像仓库
        :param request: Request instance for DescribePublicRepository.
        :type request: :class:`ksyun.client.kce.v20180314.models.DescribePublicRepositoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePublicRepository", params, "application/x-www-form-urlencoded")
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


    def UpdateRepoDesc(self, request):
        """更新仓库描述信息
        :param request: Request instance for UpdateRepoDesc.
        :type request: :class:`ksyun.client.kce.v20180314.models.UpdateRepoDescRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateRepoDesc", params, "application/x-www-form-urlencoded")
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


    def DescribeTag(self, request):
        """查询镜像列表
        :param request: Request instance for DescribeTag.
        :type request: :class:`ksyun.client.kce.v20180314.models.DescribeTagRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTag", params, "application/x-www-form-urlencoded")
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


    def DeleteTags(self, request):
        """删除镜像
        :param request: Request instance for DeleteTags.
        :type request: :class:`ksyun.client.kce.v20180314.models.DeleteTagsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteTags", params, "application/x-www-form-urlencoded")
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


    def AddFavor(self, request):
        """收藏镜像
        :param request: Request instance for AddFavor.
        :type request: :class:`ksyun.client.kce.v20180314.models.AddFavorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddFavor", params, "application/x-www-form-urlencoded")
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


    def DeleteFavor(self, request):
        """取消收藏镜像
        :param request: Request instance for DeleteFavor.
        :type request: :class:`ksyun.client.kce.v20180314.models.DeleteFavorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteFavor", params, "application/x-www-form-urlencoded")
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


    def GetFavor(self, request):
        """查询收藏镜像
        :param request: Request instance for GetFavor.
        :type request: :class:`ksyun.client.kce.v20180314.models.GetFavorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetFavor", params, "application/x-www-form-urlencoded")
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


    def RegisterRepositoryAccount(self, request):
        """用户注册镜像仓库
        :param request: Request instance for RegisterRepositoryAccount.
        :type request: :class:`ksyun.client.kce.v20180314.models.RegisterRepositoryAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RegisterRepositoryAccount", params, "application/x-www-form-urlencoded")
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


    def ModifyPassword(self, request):
        """修改仓库密码
        :param request: Request instance for ModifyPassword.
        :type request: :class:`ksyun.client.kce.v20180314.models.ModifyPasswordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyPassword", params, "application/x-www-form-urlencoded")
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


    def DeleteRepoNamespace(self, request):
        """删除命名空间
        :param request: Request instance for DeleteRepoNamespace.
        :type request: :class:`ksyun.client.kce.v20180314.models.DeleteRepoNamespaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRepoNamespace", params, "application/x-www-form-urlencoded")
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


