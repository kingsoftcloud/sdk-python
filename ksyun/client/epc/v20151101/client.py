import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class EpcClient(AbstractClient):
    _apiVersion = '2015-11-01'
    _endpoint = 'epc.api.ksyun.com'
    _service = 'epc'
    def CreateEpc(self, request):
        """CreateEpc
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
            body = self.call_judge("StartEpc", params, "application/json")
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
            body = self.call_judge("RebootEpc", params, "application/json")
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
            body = self.call_judge("DeleteEpc", params, "application/json")
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
        """ReinstallEpc
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
        """ModifySecurityGroup
        :param request: Request instance for ModifySecurityGroup.
        :type request: :class:`ksyun.client.epc.v20151101.models.ModifySecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroup", params, "application/json")
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
        """DescribeEpcs
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
        """DescribeImages
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
        """ModifyNetworkInterfaceAttribute
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
        """DescribeEpcDeviceAttributes
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
        """DescribeProcesses
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
        """CreateProcess
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
            body = self.call_judge("DescribeShareImageAccountList", params, "application/json")
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


