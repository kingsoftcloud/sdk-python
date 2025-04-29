import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KcrsClient(AbstractClient):
    _apiVersion = '2021-11-09'
    _endpoint = 'kcrs.api.ksyun.com'
    _service = 'kcrs'

    def CreateNamespace(self, request):
        """创建命名空间
        :param request: Request instance for CreateNamespace.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.CreateNamespaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateNamespace", params, "application/x-www-form-urlencoded")
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

    def DescribeNamespace(self, request):
        """查询命名空间
        :param request: Request instance for DescribeNamespace.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeNamespaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNamespace", params, "application/x-www-form-urlencoded")
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

    def ModifyNamespaceType(self, request):
        """修改命名空间类型
        :param request: Request instance for ModifyNamespaceType.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.ModifyNamespaceTypeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNamespaceType", params, "application/x-www-form-urlencoded")
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

    def DescribeNamespaceExist(self, request):
        """查询命名空间是否存在
        :param request: Request instance for DescribeNamespaceExist.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeNamespaceExistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNamespaceExist", params, "application/json")
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

    def DeleteNamespace(self, request):
        """删除命名空间
        :param request: Request instance for DeleteNamespace.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteNamespaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteNamespace", params, "application/x-www-form-urlencoded")
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

    def DescribeImages(self, request):
        """查询镜像
        :param request: Request instance for DescribeImages.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeImagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImages", params, "application/x-www-form-urlencoded")
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

    def DeleteImages(self, request):
        """删除镜像
        :param request: Request instance for DeleteImages.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteImagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteImages", params, "application/x-www-form-urlencoded")
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

    def DeleteRepoTag(self, request):
        """删除tag
        :param request: Request instance for DeleteRepoTag.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteRepoTagRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRepoTag", params, "application/x-www-form-urlencoded")
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
        """查询仓库
        :param request: Request instance for DescribeRepository.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeRepositoryRequest`
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

    def ModifyRepoDesc(self, request):
        """修改仓库描述
        :param request: Request instance for ModifyRepoDesc.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.ModifyRepoDescRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyRepoDesc", params, "application/x-www-form-urlencoded")
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
        """删除仓库
        :param request: Request instance for DeleteRepository.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteRepositoryRequest`
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

    def StartImageScan(self, request):
        """扫描镜像
        :param request: Request instance for StartImageScan.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.StartImageScanRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartImageScan", params, "application/x-www-form-urlencoded")
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

    def DescribeImageScan(self, request):
        """查询镜像扫描
        :param request: Request instance for DescribeImageScan.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeImageScanRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImageScan", params, "application/x-www-form-urlencoded")
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

    def CreateInstanceToken(self, request):
        """创建凭证
        :param request: Request instance for CreateInstanceToken.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.CreateInstanceTokenRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstanceToken", params, "application/x-www-form-urlencoded")
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

    def DescribeInternalEndpoint(self, request):
        """DescribeInternalEndpoint
        :param request: Request instance for DescribeInternalEndpoint.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeInternalEndpointRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInternalEndpoint", params, "application/x-www-form-urlencoded")
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

    def DescribeInstanceToken(self, request):
        """查询凭证
        :param request: Request instance for DescribeInstanceToken.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeInstanceTokenRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceToken", params, "application/x-www-form-urlencoded")
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

    def CreateInternalEndpoint(self, request):
        """CreateInternalEndpoint
        :param request: Request instance for CreateInternalEndpoint.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.CreateInternalEndpointRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInternalEndpoint", params, "application/x-www-form-urlencoded")
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

    def ModifyInstanceTokenStatus(self, request):
        """开启/禁用凭证
        :param request: Request instance for ModifyInstanceTokenStatus.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.ModifyInstanceTokenStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceTokenStatus", params, "application/x-www-form-urlencoded")
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

    def DeleteInternalEndpoint(self, request):
        """DeleteInternalEndpoint
        :param request: Request instance for DeleteInternalEndpoint.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteInternalEndpointRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInternalEndpoint", params, "application/x-www-form-urlencoded")
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

    def ModifyInstanceTokenInformation(self, request):
        """修改凭证信息
        :param request: Request instance for ModifyInstanceTokenInformation.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.ModifyInstanceTokenInformationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceTokenInformation", params, "application/x-www-form-urlencoded")
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

    def DescribeInternalEndpointDns(self, request):
        """DescribeInternalEndpointDns
        :param request: Request instance for DescribeInternalEndpointDns.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeInternalEndpointDnsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInternalEndpointDns", params, "application/x-www-form-urlencoded")
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

    def DeleteInstanceToken(self, request):
        """删除凭证
        :param request: Request instance for DeleteInstanceToken.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteInstanceTokenRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstanceToken", params, "application/x-www-form-urlencoded")
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

    def CreateInternalEndpointDns(self, request):
        """CreateInternalEndpointDns
        :param request: Request instance for CreateInternalEndpointDns.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.CreateInternalEndpointDnsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInternalEndpointDns", params, "application/x-www-form-urlencoded")
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

    def DeleteInternalEndpointDns(self, request):
        """DeleteInternalEndpointDns
        :param request: Request instance for DeleteInternalEndpointDns.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteInternalEndpointDnsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInternalEndpointDns", params, "application/x-www-form-urlencoded")
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

    def CreateInstance(self, request):
        """创建仓库实例
        :param request: Request instance for CreateInstance.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.CreateInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstance", params, "application/x-www-form-urlencoded")
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

    def DeleteInstance(self, request):
        """删除实例
        :param request: Request instance for DeleteInstance.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstance", params, "application/json")
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

    def DescribeInstanceUsage(self, request):
        """查询实例配额
        :param request: Request instance for DescribeInstanceUsage.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeInstanceUsageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceUsage", params, "application/json")
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

    def DescribeInstance(self, request):
        """查询镜像实例信息
        :param request: Request instance for DescribeInstance.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstance", params, "application/x-www-form-urlencoded")
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

    def CreateWebhookTrigger(self, request):
        """创建触发器
        :param request: Request instance for CreateWebhookTrigger.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.CreateWebhookTriggerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateWebhookTrigger", params, "application/json")
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

    def DescribeWebhookTrigger(self, request):
        """查询触发器
        :param request: Request instance for DescribeWebhookTrigger.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeWebhookTriggerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeWebhookTrigger", params, "application/x-www-form-urlencoded")
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

    def ModifyWebhookTrigger(self, request):
        """修改触发器
        :param request: Request instance for ModifyWebhookTrigger.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.ModifyWebhookTriggerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyWebhookTrigger", params, "application/x-www-form-urlencoded")
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

    def DescribeWebhookTriggerLog(self, request):
        """查询触发器日志
        :param request: Request instance for DescribeWebhookTriggerLog.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeWebhookTriggerLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeWebhookTriggerLog", params, "application/x-www-form-urlencoded")
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

    def DeleteWebhookTrigger(self, request):
        """删除触发器
        :param request: Request instance for DeleteWebhookTrigger.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteWebhookTriggerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteWebhookTrigger", params, "application/x-www-form-urlencoded")
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

    def CreateRetentionRule(self, request):
        """创建镜像清理规则
        :param request: Request instance for CreateRetentionRule.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.CreateRetentionRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRetentionRule", params, "application/x-www-form-urlencoded")
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

    def UpdateRetentionRule(self, request):
        """更新镜像清理规则
        :param request: Request instance for UpdateRetentionRule.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.UpdateRetentionRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateRetentionRule", params, "application/x-www-form-urlencoded")
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

    def DeleteRetentionRule(self, request):
        """删除镜像清理规则
        :param request: Request instance for DeleteRetentionRule.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DeleteRetentionRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRetentionRule", params, "application/x-www-form-urlencoded")
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

    def DescribeRetentionRule(self, request):
        """描述镜像清理规则
        :param request: Request instance for DescribeRetentionRule.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.DescribeRetentionRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRetentionRule", params, "application/x-www-form-urlencoded")
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

    def RunRetentionPolicy(self, request):
        """运行清理保留规则
        :param request: Request instance for RunRetentionPolicy.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.RunRetentionPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RunRetentionPolicy", params, "application/x-www-form-urlencoded")
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

    def GetRetentionPolicyLogs(self, request):
        """获取运行日志列表
        :param request: Request instance for GetRetentionPolicyLogs.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.GetRetentionPolicyLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRetentionPolicyLogs", params, "application/x-www-form-urlencoded")
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

    def GetRetentionPolicyLogDetail(self, request):
        """获取日志运行详情
        :param request: Request instance for GetRetentionPolicyLogDetail.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.GetRetentionPolicyLogDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRetentionPolicyLogDetail", params, "application/x-www-form-urlencoded")
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

    def GetRetentionPolicyLog(self, request):
        """获取日志保留结果
        :param request: Request instance for GetRetentionPolicyLog.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.GetRetentionPolicyLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRetentionPolicyLog", params, "application/x-www-form-urlencoded")
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

    def GetRetentionTrigger(self, request):
        """获取触发器
        :param request: Request instance for GetRetentionTrigger.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.GetRetentionTriggerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRetentionTrigger", params, "application/x-www-form-urlencoded")
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

    def UpdateRetentionTrigger(self, request):
        """修改触发器
        :param request: Request instance for UpdateRetentionTrigger.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.UpdateRetentionTriggerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateRetentionTrigger", params, "application/x-www-form-urlencoded")
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

    def Schedule(self, request):
        """ks3清理
        :param request: Request instance for Schedule.
        :type request: :class:`ksyun.client.kcrs.v20211109.models.ScheduleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Schedule", params, "application/x-www-form-urlencoded")
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
