import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class CenClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'cen.api.ksyun.com'
    _service = 'cen'
    def CreateCen(self, request):
        """CreateCen
        :param request: Request instance for CreateCen.
        :type request: :class:`ksyun.client.cen.v20160304.models.CreateCenRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCen", params, "application/x-www-form-urlencoded")
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


    def ModifyCen(self, request):
        """ModifyCen
        :param request: Request instance for ModifyCen.
        :type request: :class:`ksyun.client.cen.v20160304.models.ModifyCenRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCen", params, "application/x-www-form-urlencoded")
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


    def DeleteCen(self, request):
        """DeleteCen
        :param request: Request instance for DeleteCen.
        :type request: :class:`ksyun.client.cen.v20160304.models.DeleteCenRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCen", params, "application/x-www-form-urlencoded")
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


    def DescribeCens(self, request):
        """查询云企业网信息
        :param request: Request instance for DescribeCens.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeCensRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCens", params, "application/x-www-form-urlencoded")
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


    def DeleteCenGrant(self, request):
        """DeleteCenGrant
        :param request: Request instance for DeleteCenGrant.
        :type request: :class:`ksyun.client.cen.v20160304.models.DeleteCenGrantRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCenGrant", params, "application/x-www-form-urlencoded")
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


    def DescribeCenGrants(self, request):
        """DescribeCenGrants
        :param request: Request instance for DescribeCenGrants.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeCenGrantsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCenGrants", params, "application/x-www-form-urlencoded")
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


    def CreateCenBandWidthPackage(self, request):
        """CreateCenBandWidthPackage
        :param request: Request instance for CreateCenBandWidthPackage.
        :type request: :class:`ksyun.client.cen.v20160304.models.CreateCenBandWidthPackageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCenBandWidthPackage", params, "application/x-www-form-urlencoded")
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


    def ModifyCenBandWidthPackage(self, request):
        """ModifyCenBandWidthPackage
        :param request: Request instance for ModifyCenBandWidthPackage.
        :type request: :class:`ksyun.client.cen.v20160304.models.ModifyCenBandWidthPackageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCenBandWidthPackage", params, "application/x-www-form-urlencoded")
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


    def DeleteCenBandWidthPackage(self, request):
        """DeleteCenBandWidthPackage
        :param request: Request instance for DeleteCenBandWidthPackage.
        :type request: :class:`ksyun.client.cen.v20160304.models.DeleteCenBandWidthPackageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCenBandWidthPackage", params, "application/x-www-form-urlencoded")
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


    def AttachCenBandWidthPackage(self, request):
        """AttachCenBandWidthPackage
        :param request: Request instance for AttachCenBandWidthPackage.
        :type request: :class:`ksyun.client.cen.v20160304.models.AttachCenBandWidthPackageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachCenBandWidthPackage", params, "application/x-www-form-urlencoded")
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


    def DetachCenBandWidthPackage(self, request):
        """DetachCenBandWidthPackage
        :param request: Request instance for DetachCenBandWidthPackage.
        :type request: :class:`ksyun.client.cen.v20160304.models.DetachCenBandWidthPackageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachCenBandWidthPackage", params, "application/x-www-form-urlencoded")
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


    def DescribeCenBandWidthPackages(self, request):
        """DescribeCenBandWidthPackages
        :param request: Request instance for DescribeCenBandWidthPackages.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeCenBandWidthPackagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCenBandWidthPackages", params, "application/json")
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


    def CreateCenRegionBandwidth(self, request):
        """CreateCenRegionBandwidth
        :param request: Request instance for CreateCenRegionBandwidth.
        :type request: :class:`ksyun.client.cen.v20160304.models.CreateCenRegionBandwidthRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCenRegionBandwidth", params, "application/x-www-form-urlencoded")
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


    def DeleteCenRegionBandwidth(self, request):
        """DeleteCenRegionBandwidth
        :param request: Request instance for DeleteCenRegionBandwidth.
        :type request: :class:`ksyun.client.cen.v20160304.models.DeleteCenRegionBandwidthRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCenRegionBandwidth", params, "application/x-www-form-urlencoded")
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


    def ModifyCenRegionBandwidth(self, request):
        """ModifyCenRegionBandwidth
        :param request: Request instance for ModifyCenRegionBandwidth.
        :type request: :class:`ksyun.client.cen.v20160304.models.ModifyCenRegionBandwidthRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCenRegionBandwidth", params, "application/x-www-form-urlencoded")
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


    def DescribeCenRegionBandwidths(self, request):
        """DescribeCenRegionBandwidths
        :param request: Request instance for DescribeCenRegionBandwidths.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeCenRegionBandwidthsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCenRegionBandwidths", params, "application/json")
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


    def DescribeCenRoutes(self, request):
        """DescribeCenRoutes
        :param request: Request instance for DescribeCenRoutes.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeCenRoutesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCenRoutes", params, "application/x-www-form-urlencoded")
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


    def DescribeCenBandWidthPackageUsage(self, request):
        """DescribeCenBandWidthPackageUsage
        :param request: Request instance for DescribeCenBandWidthPackageUsage.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeCenBandWidthPackageUsageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCenBandWidthPackageUsage", params, "application/json")
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


    def DescribeNetworkInstances(self, request):
        """DescribeNetworkInstances
        :param request: Request instance for DescribeNetworkInstances.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeNetworkInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNetworkInstances", params, "application/json")
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


    def CreateCenGrant(self, request):
        """CreateCenGrant
        :param request: Request instance for CreateCenGrant.
        :type request: :class:`ksyun.client.cen.v20160304.models.CreateCenGrantRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCenGrant", params, "application/x-www-form-urlencoded")
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


    def DescribeInterAreas(self, request):
        """DescribeInterAreas
        :param request: Request instance for DescribeInterAreas.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeInterAreasRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInterAreas", params, "application/json")
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


    def DescribeInterRegions(self, request):
        """DescribeInterRegions
        :param request: Request instance for DescribeInterRegions.
        :type request: :class:`ksyun.client.cen.v20160304.models.DescribeInterRegionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInterRegions", params, "application/json")
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


    def AttachNetworkInstance(self, request):
        """AttachNetworkInstance
        :param request: Request instance for AttachNetworkInstance.
        :type request: :class:`ksyun.client.cen.v20160304.models.AttachNetworkInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachNetworkInstance", params, "application/x-www-form-urlencoded")
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


    def DetachNetworkInstance(self, request):
        """DetachNetworkInstance
        :param request: Request instance for DetachNetworkInstance.
        :type request: :class:`ksyun.client.cen.v20160304.models.DetachNetworkInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachNetworkInstance", params, "application/x-www-form-urlencoded")
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


    def CenCidrPublish(self, request):
        """发布云企业网网络实例的路由
        :param request: Request instance for CenCidrPublish.
        :type request: :class:`ksyun.client.cen.v20160304.models.CenCidrPublishRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CenCidrPublish", params, "application/x-www-form-urlencoded")
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


    def CenCidrDelete(self, request):
        """撤销云企业网网络实例的路由
        :param request: Request instance for CenCidrDelete.
        :type request: :class:`ksyun.client.cen.v20160304.models.CenCidrDeleteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CenCidrDelete", params, "application/x-www-form-urlencoded")
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


