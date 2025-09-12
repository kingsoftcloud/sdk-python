import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class EpcClient(AbstractClient):
    _apiVersion = '2015-11-01'
    _endpoint = 'epc.api.ksyun.com'
    _service = 'epc'
    def CreateEpc(self, request):
        """创建云物理主机
        :param request: Request instance for CreateEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateEpc", params, "application/x-www-form-urlencoded")
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


    def StartEpc(self, request):
        """StartEpc
        :param request: Request instance for StartEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.StartEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartEpc", params, "application/x-www-form-urlencoded")
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


    def RebootEpc(self, request):
        """RebootEpc
        :param request: Request instance for RebootEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.RebootEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebootEpc", params, "application/x-www-form-urlencoded")
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


    def DeleteEpc(self, request):
        """DeleteEpc
        :param request: Request instance for DeleteEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteEpc", params, "application/x-www-form-urlencoded")
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


    def ReinstallEpc(self, request):
        """物理机重装系统
        :param request: Request instance for ReinstallEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.ReinstallEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReinstallEpc", params, "application/x-www-form-urlencoded")
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


    def ModifySecurityGroup(self, request):
        """修改安全组
        :param request: Request instance for ModifySecurityGroup.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifySecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroup", params, "application/x-www-form-urlencoded")
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


    def CreateKey(self, request):
        """CreateKey
        :param request: Request instance for CreateKey.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateKey", params, "application/x-www-form-urlencoded")
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


    def DescribeEpcs(self, request):
        """查看云物理主机列表信息
        :param request: Request instance for DescribeEpcs.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeEpcsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEpcs", params, "application/x-www-form-urlencoded")
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


    def GetDynamicCode(self, request):
        """GetDynamicCode
        :param request: Request instance for GetDynamicCode.
        :type request: :class:`ksyun.client.epc.v20151101.models.GetDynamicCodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDynamicCode", params, "application/x-www-form-urlencoded")
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


    def DescribeVpns(self, request):
        """DescribeVpns
        :param request: Request instance for DescribeVpns.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeVpnsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVpns", params, "application/x-www-form-urlencoded")
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


    def CreateImage(self, request):
        """CreateImage
        :param request: Request instance for CreateImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateImage", params, "application/x-www-form-urlencoded")
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


    def ModifyImage(self, request):
        """ModifyImage
        :param request: Request instance for ModifyImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifyImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyImage", params, "application/x-www-form-urlencoded")
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


    def DeleteImage(self, request):
        """DeleteImage
        :param request: Request instance for DeleteImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteImage", params, "application/x-www-form-urlencoded")
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
        """查询镜像列表
        :param request: Request instance for DescribeImages.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeImagesRequest`
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


    def ModifyDns(self, request):
        """ModifyDns
        :param request: Request instance for ModifyDns.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifyDnsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDns", params, "application/x-www-form-urlencoded")
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


    def ModifyNetworkInterfaceAttribute(self, request):
        """修改网卡信息
        :param request: Request instance for ModifyNetworkInterfaceAttribute.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifyNetworkInterfaceAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNetworkInterfaceAttribute", params, "application/x-www-form-urlencoded")
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


    def DescribePhysicalMonitor(self, request):
        """DescribePhysicalMonitor
        :param request: Request instance for DescribePhysicalMonitor.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribePhysicalMonitorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePhysicalMonitor", params, "application/x-www-form-urlencoded")
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


    def DescribeEpcManagements(self, request):
        """DescribeEpcManagements
        :param request: Request instance for DescribeEpcManagements.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeEpcManagementsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEpcManagements", params, "application/x-www-form-urlencoded")
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


    def DescribeRemoteManagements(self, request):
        """DescribeRemoteManagements
        :param request: Request instance for DescribeRemoteManagements.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeRemoteManagementsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRemoteManagements", params, "application/x-www-form-urlencoded")
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


    def StopEpc(self, request):
        """StopEpc
        :param request: Request instance for StopEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.StopEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopEpc", params, "application/x-www-form-urlencoded")
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


    def ModifyEpc(self, request):
        """ModifyEpc
        :param request: Request instance for ModifyEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifyEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyEpc", params, "application/x-www-form-urlencoded")
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


    def ModifyRemoteManagement(self, request):
        """ModifyRemoteManagement
        :param request: Request instance for ModifyRemoteManagement.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifyRemoteManagementRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyRemoteManagement", params, "application/x-www-form-urlencoded")
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


    def CreateRemoteManagement(self, request):
        """CreateRemoteManagement
        :param request: Request instance for CreateRemoteManagement.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateRemoteManagementRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRemoteManagement", params, "application/x-www-form-urlencoded")
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


    def ReinstallCustomerEpc(self, request):
        """ReinstallCustomerEpc
        :param request: Request instance for ReinstallCustomerEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.ReinstallCustomerEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReinstallCustomerEpc", params, "application/x-www-form-urlencoded")
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


    def DeleteRemoteManagement(self, request):
        """DeleteRemoteManagement
        :param request: Request instance for DeleteRemoteManagement.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteRemoteManagementRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRemoteManagement", params, "application/x-www-form-urlencoded")
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


    def ResetPassword(self, request):
        """重置密码
        :param request: Request instance for ResetPassword.
        :type request: :class:`ksyun.client.epc.v20151101.models.ResetPasswordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetPassword", params, "application/x-www-form-urlencoded")
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


    def ModifyHyperThreading(self, request):
        """修改超线程
        :param request: Request instance for ModifyHyperThreading.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifyHyperThreadingRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyHyperThreading", params, "application/x-www-form-urlencoded")
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


    def AssociateCluster(self, request):
        """AssociateCluster
        :param request: Request instance for AssociateCluster.
        :type request: :class:`ksyun.client.epc.v20151101.models.AssociateClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateCluster", params, "application/x-www-form-urlencoded")
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


    def DisassociateCluster(self, request):
        """DisassociateCluster
        :param request: Request instance for DisassociateCluster.
        :type request: :class:`ksyun.client.epc.v20151101.models.DisassociateClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisassociateCluster", params, "application/x-www-form-urlencoded")
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


    def DescribeInspections(self, request):
        """DescribeInspections
        :param request: Request instance for DescribeInspections.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeInspectionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInspections", params, "application/x-www-form-urlencoded")
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


    def DescribeEpcStocks(self, request):
        """DescribeEpcStocks
        :param request: Request instance for DescribeEpcStocks.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeEpcStocksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEpcStocks", params, "application/x-www-form-urlencoded")
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


    def DescribeEpcDeviceAttributes(self, request):
        """查询云物理机型配置信息
        :param request: Request instance for DescribeEpcDeviceAttributes.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeEpcDeviceAttributesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEpcDeviceAttributes", params, "application/x-www-form-urlencoded")
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


    def DescribeProcesses(self, request):
        """查询工单信息
        :param request: Request instance for DescribeProcesses.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeProcessesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeProcesses", params, "application/x-www-form-urlencoded")
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


    def CreateProcess(self, request):
        """创建工单信息
        :param request: Request instance for CreateProcess.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateProcessRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateProcess", params, "application/x-www-form-urlencoded")
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


    def DeleteProcess(self, request):
        """DeleteProcess
        :param request: Request instance for DeleteProcess.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteProcessRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteProcess", params, "application/x-www-form-urlencoded")
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


    def ReplyProcess(self, request):
        """ReplyProcess
        :param request: Request instance for ReplyProcess.
        :type request: :class:`ksyun.client.epc.v20151101.models.ReplyProcessRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReplyProcess", params, "application/x-www-form-urlencoded")
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


    def DescribeEpcTrashes(self, request):
        """DescribeEpcTrashes
        :param request: Request instance for DescribeEpcTrashes.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeEpcTrashesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEpcTrashes", params, "application/x-www-form-urlencoded")
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


    def ReturnEpc(self, request):
        """ReturnEpc
        :param request: Request instance for ReturnEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.ReturnEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReturnEpc", params, "application/x-www-form-urlencoded")
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


    def CreateResourceRequirement(self, request):
        """创建资源需求工单
        :param request: Request instance for CreateResourceRequirement.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateResourceRequirementRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateResourceRequirement", params, "application/x-www-form-urlencoded")
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


    def AttachVolume(self, request):
        """EPC挂载EBS
        :param request: Request instance for AttachVolume.
        :type request: :class:`ksyun.client.epc.v20151101.models.AttachVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachVolume", params, "application/x-www-form-urlencoded")
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


    def DetachVolume(self, request):
        """EPC卸载EBS
        :param request: Request instance for DetachVolume.
        :type request: :class:`ksyun.client.epc.v20151101.models.DetachVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachVolume", params, "application/x-www-form-urlencoded")
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


    def DescribePrice(self, request):
        """查询价格信息
        :param request: Request instance for DescribePrice.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribePriceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePrice", params, "application/x-www-form-urlencoded")
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


    def UpdateConfirm(self, request):
        """更新工单重启状态
        :param request: Request instance for UpdateConfirm.
        :type request: :class:`ksyun.client.epc.v20151101.models.UpdateConfirmRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateConfirm", params, "application/x-www-form-urlencoded")
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


    def ModifyOverclockingAttribute(self, request):
        """修改超频
        :param request: Request instance for ModifyOverclockingAttribute.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifyOverclockingAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyOverclockingAttribute", params, "application/x-www-form-urlencoded")
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


    def CopyImage(self, request):
        """复制镜像
        :param request: Request instance for CopyImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.CopyImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CopyImage", params, "application/x-www-form-urlencoded")
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


    def DescribeEpcRaidAttributes(self, request):
        """查询多raid信息
        :param request: Request instance for DescribeEpcRaidAttributes.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeEpcRaidAttributesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEpcRaidAttributes", params, "application/x-www-form-urlencoded")
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


    def DescribeGpuImageDriver(self, request):
        """查询GPU镜像驱动
        :param request: Request instance for DescribeGpuImageDriver.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeGpuImageDriverRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeGpuImageDriver", params, "application/x-www-form-urlencoded")
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


    def CreateShareImage(self, request):
        """星曜共享镜像
        :param request: Request instance for CreateShareImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateShareImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateShareImage", params, "application/x-www-form-urlencoded")
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


    def DeleteShareImage(self, request):
        """星曜取消共享镜像
        :param request: Request instance for DeleteShareImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteShareImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteShareImage", params, "application/x-www-form-urlencoded")
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


    def DescribeShareImageAccountList(self, request):
        """星曜获取已共享镜像的账户列表信息
        :param request: Request instance for DescribeShareImageAccountList.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeShareImageAccountListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeShareImageAccountList", params, "application/x-www-form-urlencoded")
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


    def DescribeShareImage(self, request):
        """星曜获取共享镜像列表信息
        :param request: Request instance for DescribeShareImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeShareImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeShareImage", params, "application/x-www-form-urlencoded")
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


    def AcceptShareImage(self, request):
        """星曜接收共享镜像
        :param request: Request instance for AcceptShareImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.AcceptShareImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AcceptShareImage", params, "application/x-www-form-urlencoded")
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


    def RejectShareImage(self, request):
        """星曜拒绝共享镜像
        :param request: Request instance for RejectShareImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.RejectShareImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RejectShareImage", params, "application/x-www-form-urlencoded")
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


    def DescribeManagedAccessory(self, request):
        """托管备件信息查询
        :param request: Request instance for DescribeManagedAccessory.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeManagedAccessoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeManagedAccessory", params, "application/x-www-form-urlencoded")
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


    def AutoDeleteEpc(self, request):
        """AutoDeleteEpc
        :param request: Request instance for AutoDeleteEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.AutoDeleteEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AutoDeleteEpc", params, "application/x-www-form-urlencoded")
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


    def ExportImage(self, request):
        """自定义镜像导出
        :param request: Request instance for ExportImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.ExportImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ExportImage", params, "application/x-www-form-urlencoded")
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


    def QueryBuckets(self, request):
        """查询ks3对象存储bucket桶列表
        :param request: Request instance for QueryBuckets.
        :type request: :class:`ksyun.client.epc.v20151101.models.QueryBucketsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryBuckets", params, "application/x-www-form-urlencoded")
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


    def CancelImageExport(self, request):
        """取消镜像导出
        :param request: Request instance for CancelImageExport.
        :type request: :class:`ksyun.client.epc.v20151101.models.CancelImageExportRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CancelImageExport", params, "application/x-www-form-urlencoded")
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


    def UseHotStandByEpc(self, request):
        """热备机替换
        :param request: Request instance for UseHotStandByEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.UseHotStandByEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UseHotStandByEpc", params, "application/x-www-form-urlencoded")
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


    def ActivateHotStandbyEpc(self, request):
        """激活热备机
        :param request: Request instance for ActivateHotStandbyEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.ActivateHotStandbyEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ActivateHotStandbyEpc", params, "application/x-www-form-urlencoded")
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


    def BatchCreateEpc(self, request):
        """批量创建云物理主机
        :param request: Request instance for BatchCreateEpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.BatchCreateEpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BatchCreateEpc", params, "application/x-www-form-urlencoded")
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


    def DescribeUseHotStandbyRecords(self, request):
        """DescribeUseHotStandbyRecords
        :param request: Request instance for DescribeUseHotStandbyRecords.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeUseHotStandbyRecordsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeUseHotStandbyRecords", params, "application/x-www-form-urlencoded")
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


    def DescribeGpuRoceTopology(self, request):
        """查询拓扑结构接口
        :param request: Request instance for DescribeGpuRoceTopology.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeGpuRoceTopologyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeGpuRoceTopology", params, "application/x-www-form-urlencoded")
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


    def ModifyProcess(self, request):
        """修改工单信息
        :param request: Request instance for ModifyProcess.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifyProcessRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyProcess", params, "application/x-www-form-urlencoded")
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


    def ConfirmProcess(self, request):
        """客户评价工单
        :param request: Request instance for ConfirmProcess.
        :type request: :class:`ksyun.client.epc.v20151101.models.ConfirmProcessRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ConfirmProcess", params, "application/x-www-form-urlencoded")
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


    def DescribeModelConfig(self, request):
        """查询AI模型配置
        :param request: Request instance for DescribeModelConfig.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeModelConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeModelConfig", params, "application/x-www-form-urlencoded")
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


    def DescribeRoceEvent(self, request):
        """查询Roce事件告警
        :param request: Request instance for DescribeRoceEvent.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeRoceEventRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRoceEvent", params, "application/x-www-form-urlencoded")
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


    def DescribeRoceEventDetails(self, request):
        """查询Roce事件告警历史
        :param request: Request instance for DescribeRoceEventDetails.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeRoceEventDetailsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRoceEventDetails", params, "application/x-www-form-urlencoded")
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


    def BatchCreateProcess(self, request):
        """批量创建工单
        :param request: Request instance for BatchCreateProcess.
        :type request: :class:`ksyun.client.epc.v20151101.models.BatchCreateProcessRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BatchCreateProcess", params, "application/x-www-form-urlencoded")
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


    def CreateInspectHost(self, request):
        """发起故障检测
        :param request: Request instance for CreateInspectHost.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateInspectHostRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInspectHost", params, "application/x-www-form-urlencoded")
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


    def DescribeInspectHostResults(self, request):
        """查询故障检测结果
        :param request: Request instance for DescribeInspectHostResults.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeInspectHostResultsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInspectHostResults", params, "application/x-www-form-urlencoded")
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


    def DescribeXidDetails(self, request):
        """查询Xid事件详情
        :param request: Request instance for DescribeXidDetails.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeXidDetailsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeXidDetails", params, "application/x-www-form-urlencoded")
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


    def RunSoInstances(self, request):
        """创建星海实例
        :param request: Request instance for RunSoInstances.
        :type request: :class:`ksyun.client.epc.v20151101.models.RunSoInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RunSoInstances", params, "application/x-www-form-urlencoded")
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


    def DescribeSoImages(self, request):
        """查询星海镜像
        :param request: Request instance for DescribeSoImages.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeSoImagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSoImages", params, "application/x-www-form-urlencoded")
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


    def RebootSoInstance(self, request):
        """重启星海实例
        :param request: Request instance for RebootSoInstance.
        :type request: :class:`ksyun.client.epc.v20151101.models.RebootSoInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebootSoInstance", params, "application/x-www-form-urlencoded")
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


    def DeleteSoImages(self, request):
        """删除星海自定义镜像
        :param request: Request instance for DeleteSoImages.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteSoImagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSoImages", params, "application/x-www-form-urlencoded")
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


    def DeleteSoVpc(self, request):
        """删除星海私有网络
        :param request: Request instance for DeleteSoVpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteSoVpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSoVpc", params, "application/x-www-form-urlencoded")
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


    def DescribeSoAvailableResource(self, request):
        """查询可用区资源的库存信息
        :param request: Request instance for DescribeSoAvailableResource.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeSoAvailableResourceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSoAvailableResource", params, "application/x-www-form-urlencoded")
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


    def DescribeSoInstances(self, request):
        """获取星海实例信息
        :param request: Request instance for DescribeSoInstances.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeSoInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSoInstances", params, "application/x-www-form-urlencoded")
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


    def DeleteSoInstance(self, request):
        """删除星海实例
        :param request: Request instance for DeleteSoInstance.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteSoInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSoInstance", params, "application/x-www-form-urlencoded")
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


    def DescribeSoSecurityGroups(self, request):
        """查询星海安全组信息
        :param request: Request instance for DescribeSoSecurityGroups.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeSoSecurityGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSoSecurityGroups", params, "application/x-www-form-urlencoded")
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


    def CreateSoVpc(self, request):
        """创建星海私有网络
        :param request: Request instance for CreateSoVpc.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateSoVpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSoVpc", params, "application/x-www-form-urlencoded")
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


    def DeleteSoSubnet(self, request):
        """删除星海子网信息
        :param request: Request instance for DeleteSoSubnet.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteSoSubnetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSoSubnet", params, "application/x-www-form-urlencoded")
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


    def DescribeSoKeyPairs(self, request):
        """查询星海密钥对
        :param request: Request instance for DescribeSoKeyPairs.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeSoKeyPairsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSoKeyPairs", params, "application/x-www-form-urlencoded")
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


    def StartSoInstance(self, request):
        """启动星海实例
        :param request: Request instance for StartSoInstance.
        :type request: :class:`ksyun.client.epc.v20151101.models.StartSoInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartSoInstance", params, "application/x-www-form-urlencoded")
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


    def DescribeSoInstanceTypes(self, request):
        """获取实例规格信息
        :param request: Request instance for DescribeSoInstanceTypes.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeSoInstanceTypesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSoInstanceTypes", params, "application/x-www-form-urlencoded")
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


    def ModifySoSubnetAttributes(self, request):
        """修改星海指定子网信息
        :param request: Request instance for ModifySoSubnetAttributes.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifySoSubnetAttributesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySoSubnetAttributes", params, "application/x-www-form-urlencoded")
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


    def DescribeSoSubnet(self, request):
        """查询星海子网信息
        :param request: Request instance for DescribeSoSubnet.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeSoSubnetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSoSubnet", params, "application/x-www-form-urlencoded")
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


    def ModifySoKeyPairAttribute(self, request):
        """修改星海密钥对信息
        :param request: Request instance for ModifySoKeyPairAttribute.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifySoKeyPairAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySoKeyPairAttribute", params, "application/x-www-form-urlencoded")
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


    def ModifySoImageAttribute(self, request):
        """修改星海镜像信息
        :param request: Request instance for ModifySoImageAttribute.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifySoImageAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySoImageAttribute", params, "application/x-www-form-urlencoded")
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


    def ModifySoVpcAttributes(self, request):
        """修改星海私有网络
        :param request: Request instance for ModifySoVpcAttributes.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifySoVpcAttributesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySoVpcAttributes", params, "application/x-www-form-urlencoded")
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


    def ReplaceSoSystemVolume(self, request):
        """星海更换操作系统
        :param request: Request instance for ReplaceSoSystemVolume.
        :type request: :class:`ksyun.client.epc.v20151101.models.ReplaceSoSystemVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReplaceSoSystemVolume", params, "application/x-www-form-urlencoded")
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


    def CreateSoSubnet(self, request):
        """创建星海子网
        :param request: Request instance for CreateSoSubnet.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateSoSubnetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSoSubnet", params, "application/x-www-form-urlencoded")
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


    def DescribeSoVpcs(self, request):
        """查询星海私有网络
        :param request: Request instance for DescribeSoVpcs.
        :type request: :class:`ksyun.client.epc.v20151101.models.DescribeSoVpcsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSoVpcs", params, "application/x-www-form-urlencoded")
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


    def StopSoInstance(self, request):
        """停止星海实例
        :param request: Request instance for StopSoInstance.
        :type request: :class:`ksyun.client.epc.v20151101.models.StopSoInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopSoInstance", params, "application/x-www-form-urlencoded")
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


    def DeleteSoKeyPairs(self, request):
        """删除星海密钥对
        :param request: Request instance for DeleteSoKeyPairs.
        :type request: :class:`ksyun.client.epc.v20151101.models.DeleteSoKeyPairsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSoKeyPairs", params, "application/x-www-form-urlencoded")
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


    def CreateSoImage(self, request):
        """创建星海自定义镜像
        :param request: Request instance for CreateSoImage.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateSoImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSoImage", params, "application/x-www-form-urlencoded")
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


    def ModifySoInstanceAttribute(self, request):
        """修改指定实例的信息
        :param request: Request instance for ModifySoInstanceAttribute.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifySoInstanceAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySoInstanceAttribute", params, "application/x-www-form-urlencoded")
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


    def CreateSoKeyPair(self, request):
        """创建星海密钥对
        :param request: Request instance for CreateSoKeyPair.
        :type request: :class:`ksyun.client.epc.v20151101.models.CreateSoKeyPairRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSoKeyPair", params, "application/x-www-form-urlencoded")
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


