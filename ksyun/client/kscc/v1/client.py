import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KsccClient(AbstractClient):
    _apiVersion = 'V1'
    _endpoint = 'kscc.api.ksyun.com'
    _service = 'kscc'
    def UpdateUserQuota(self, request):
        """更新用户月度配额；QuotaAmount不传或为空时清除该用户单独配额。
        :param request: Request instance for UpdateUserQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.UpdateUserQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateUserQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeUserCostSummary(self, request):
        """查询指定用户在某月份的配额和已使用金额。
        :param request: Request instance for DescribeUserCostSummary.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeUserCostSummaryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeUserCostSummary", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeAiLogDetailByIds(self, request):
        """根据消息ID查询消息详情。
        :param request: Request instance for DescribeAiLogDetailByIds.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeAiLogDetailByIdsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAiLogDetailByIds", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeAiLogDetail(self, request):
        """根据时间、用户、模型等条件分页查询日志记录。
        :param request: Request instance for DescribeAiLogDetail.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeAiLogDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAiLogDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeOrganizationTree(self, request):
        """查询企业部门组织树，包含父子部门关系和AI启用状态。
        :param request: Request instance for DescribeOrganizationTree.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeOrganizationTreeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeOrganizationTree", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeModelMetrics(self, request):
        """查询模型维度的请求量、Token量、TPM和RPM监控数据。
        :param request: Request instance for DescribeModelMetrics.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeModelMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeModelMetrics", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeUserTokenUsage(self, request):
        """按时间范围查询用户Token和配额金额消耗，可按用户或部门过滤。
        :param request: Request instance for DescribeUserTokenUsage.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeUserTokenUsageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeUserTokenUsage", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeUserQuotaList(self, request):
        """分页查询用户月度配额、已用金额和使用比例。
        :param request: Request instance for DescribeUserQuotaList.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeUserQuotaListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeUserQuotaList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeQuotaGlobalConfig(self, request):
        """查询账号、部门、成员配额开关和通用配置。
        :param request: Request instance for DescribeQuotaGlobalConfig.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeQuotaGlobalConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeQuotaGlobalConfig", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateQuotaGlobalConfig(self, request):
        """更新配额预警、折扣、联系人和各级配额开关。
        :param request: Request instance for UpdateQuotaGlobalConfig.
        :type request: :class:`ksyun.client.kscc.v1.models.UpdateQuotaGlobalConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateQuotaGlobalConfig", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeAccountQuota(self, request):
        """查询账号级月度配额、已用金额和使用比例。
        :param request: Request instance for DescribeAccountQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeAccountQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAccountQuota", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateAccountQuota(self, request):
        """设置账号级月度配额，并可同步设置默认成员配额。
        :param request: Request instance for UpdateAccountQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.UpdateAccountQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateAccountQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteAccountQuota(self, request):
        """删除账号级月度配额限制。
        :param request: Request instance for DeleteAccountQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.DeleteAccountQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteAccountQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateDefaultMemberQuota(self, request):
        """设置全员默认成员月度配额。
        :param request: Request instance for UpdateDefaultMemberQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.UpdateDefaultMemberQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDefaultMemberQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteDefaultMemberQuota(self, request):
        """清空全员默认成员月度配额，返回值为0。
        :param request: Request instance for DeleteDefaultMemberQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.DeleteDefaultMemberQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDefaultMemberQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDeptQuotaList(self, request):
        """分页查询部门月度配额、已用金额和使用比例。
        :param request: Request instance for DescribeDeptQuotaList.
        :type request: :class:`ksyun.client.kscc.v1.models.DescribeDeptQuotaListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDeptQuotaList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateDeptQuota(self, request):
        """设置指定部门的月度配额。
        :param request: Request instance for UpdateDeptQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.UpdateDeptQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDeptQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteDeptQuota(self, request):
        """删除指定部门的月度配额限制。
        :param request: Request instance for DeleteDeptQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.DeleteDeptQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDeptQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteUserQuota(self, request):
        """删除指定用户的月度配额限制。
        :param request: Request instance for DeleteUserQuota.
        :type request: :class:`ksyun.client.kscc.v1.models.DeleteUserQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteUserQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


