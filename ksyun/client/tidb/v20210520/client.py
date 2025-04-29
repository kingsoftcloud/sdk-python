import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class TidbClient(AbstractClient):
    _apiVersion = '2021-05-20'
    _endpoint = 'tidb.api.ksyun.com'
    _service = 'tidb'

    def CreateInstance(self, request):
        """CreateInstance
        :param request: Request instance for CreateInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateInstanceRequest`
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

    def ListInstance(self, request):
        """ListInstance
        :param request: Request instance for ListInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DescribeInstance
        :param request: Request instance for DescribeInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescribeInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def RenameInstance(self, request):
        """RenameInstance
        :param request: Request instance for RenameInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.RenameInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenameInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ListRegion(self, request):
        """ListRegion
        :param request: Request instance for ListRegion.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListRegion", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def DescRegion(self, request):
        """DescRegion
        :param request: Request instance for DescRegion.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescRegion", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def CreateSecurityGroup(self, request):
        """CreateSecurityGroup
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ListSecurityGroup(self, request):
        """ListSecurityGroup
        :param request: Request instance for ListSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSecurityGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DescribeSecurityGroup
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.DescribeSecurityGroupRequest`
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

    def UpdateSecurityGroup(self, request):
        """UpdateSecurityGroup
        :param request: Request instance for UpdateSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.UpdateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """CloneSecurityGroup
        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CloneSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloneSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def BindSecurityGroup(self, request):
        """BindSecurityGroup
        :param request: Request instance for BindSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.BindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BindSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def UnbindSecurityGroup(self, request):
        """UnbindSecurityGroup
        :param request: Request instance for UnbindSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.UnbindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnbindSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def RebindSecurityGroup(self, request):
        """RebindSecurityGroup
        :param request: Request instance for RebindSecurityGroup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.RebindSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebindSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def CreateSecurityRule(self, request):
        """CreateSecurityRule
        :param request: Request instance for CreateSecurityRule.
        :type request: :class:`ksyun.client.tidb.v20210520.models.CreateSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def UpdateSecurityRule(self, request):
        """UpdateSecurityRule
        :param request: Request instance for UpdateSecurityRule.
        :type request: :class:`ksyun.client.tidb.v20210520.models.UpdateSecurityRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateSecurityRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ListUnsecuredInstance(self, request):
        """ListUnsecuredInstance
        :param request: Request instance for ListUnsecuredInstance.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListUnsecuredInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListUnsecuredInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)

    def ListBackup(self, request):
        """ListBackup
        :param request: Request instance for ListBackup.
        :type request: :class:`ksyun.client.tidb.v20210520.models.ListBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)
