import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KrdsClient(AbstractClient):
    _apiVersion = '2020-08-25'
    _endpoint = 'krds.api.ksyun.com'
    _service = 'krds'

    def CreateSecurityGroup(self, request):
        """创建安全组
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.krds.v20200825.models.CreateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescribeSecurityGroup(self, request):
        """查看安全组
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.krds.v20200825.models.DescribeSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DeleteSecurityGroup(self, request):
        """删除安全组
        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`ksyun.client.krds.v20200825.models.DeleteSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """修改参数组
        :param request: Request instance for ModifySecurityGroup.
        :type request: :class:`ksyun.client.krds.v20200825.models.ModifySecurityGroupRequest`
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

    def CloneSecurityGroup(self, request):
        """复制安全组
        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`ksyun.client.krds.v20200825.models.CloneSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloneSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifySecurityGroupRule(self, request):
        """修改安全组规则
        :param request: Request instance for ModifySecurityGroupRule.
        :type request: :class:`ksyun.client.krds.v20200825.models.ModifySecurityGroupRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroupRule", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def SecurityGroupRelation(self, request):
        """修改安全组实例绑定关系
        :param request: Request instance for SecurityGroupRelation.
        :type request: :class:`ksyun.client.krds.v20200825.models.SecurityGroupRelationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SecurityGroupRelation", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ModifySecurityGroupRuleName(self, request):
        """修改安全组规则名称
        :param request: Request instance for ModifySecurityGroupRuleName.
        :type request: :class:`ksyun.client.krds.v20200825.models.ModifySecurityGroupRuleNameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroupRuleName", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)
