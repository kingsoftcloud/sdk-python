import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class Bill_unionClient(AbstractClient):
    _apiVersion = '2020-01-01'
    _endpoint = 'bill-union.api.ksyun.com'
    _service = 'bill-union'
    def DescribeBillSummaryByPayMode(self, request):
        """获取计费类别汇总账单（费用账单接口，推荐使用，包含预付费、实时付费、后付费）
        :param request: Request instance for DescribeBillSummaryByPayMode.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.DescribeBillSummaryByPayModeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBillSummaryByPayMode", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeBillSummaryByProduct(self, request):
        """按产品线获取账单汇总金额
        :param request: Request instance for DescribeBillSummaryByProduct.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.DescribeBillSummaryByProductRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBillSummaryByProduct", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeBillSummaryByProject(self, request):
        """按项目制获取账单汇总金额（费用账单接口，推荐使用，包含预付费、实时付费、后付费）
        :param request: Request instance for DescribeBillSummaryByProject.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.DescribeBillSummaryByProjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBillSummaryByProject", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeInstanceSummaryBills(self, request):
        """按实例ID获取账单汇总金额
        :param request: Request instance for DescribeInstanceSummaryBills.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.DescribeInstanceSummaryBillsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceSummaryBills", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeProductCode(self, request):
        """获取产品线列表
        :param request: Request instance for DescribeProductCode.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.DescribeProductCodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeProductCode", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeSplitItemBillDetails(self, request):
        """分页查询分拆项账单明细
        :param request: Request instance for DescribeSplitItemBillDetails.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.DescribeSplitItemBillDetailsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSplitItemBillDetails", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeMiItemBills(self, request):
        """小米计费项账单
        :param request: Request instance for DescribeMiItemBills.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.DescribeMiItemBillsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMiItemBills", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeSplitItemDayBillDetails(self, request):
        """分页查询分拆项账单明细
        :param request: Request instance for DescribeSplitItemDayBillDetails.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.DescribeSplitItemDayBillDetailsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSplitItemDayBillDetails", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ListProductGroups(self, request):
        """获取产品线详情列表
        :param request: Request instance for ListProductGroups.
        :type request: :class:`ksyun.client.bill_union.v20200101.models.ListProductGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListProductGroups", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


