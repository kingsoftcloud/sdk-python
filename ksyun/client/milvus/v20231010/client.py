import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MilvusClient(AbstractClient):
    _apiVersion = '2023-10-10'
    _endpoint = 'milvus.api.ksyun.com'
    _service = 'milvus'
    def DeleteSecurityRules(self, request):
        """删除安全组规则
        :param request: Request instance for DeleteSecurityRules.
        :type request: :class:`ksyun.client.milvus.v20231010.models.DeleteSecurityRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityRules", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateSecurityRules(self, request):
        """创建安全组规则
        :param request: Request instance for CreateSecurityRules.
        :type request: :class:`ksyun.client.milvus.v20231010.models.CreateSecurityRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityRules", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UnbindSecurityGroupInstances(self, request):
        """解绑安全组已绑定实例
        :param request: Request instance for UnbindSecurityGroupInstances.
        :type request: :class:`ksyun.client.milvus.v20231010.models.UnbindSecurityGroupInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnbindSecurityGroupInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def BindSecurityGroupInstances(self, request):
        """绑定实例至安全组
        :param request: Request instance for BindSecurityGroupInstances.
        :type request: :class:`ksyun.client.milvus.v20231010.models.BindSecurityGroupInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BindSecurityGroupInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.milvus.v20231010.models.DeleteSecurityGroupRequest`
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


    def DescribeSecurityGroup(self, request):
        """查询安全组详情
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.milvus.v20231010.models.DescribeSecurityGroupRequest`
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


    def CreateSecurityGroup(self, request):
        """创建安全组
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.milvus.v20231010.models.CreateSecurityGroupRequest`
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


    def ListSecurityGroup(self, request):
        """查询安全组列表
        :param request: Request instance for ListSecurityGroup.
        :type request: :class:`ksyun.client.milvus.v20231010.models.ListSecurityGroupRequest`
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


    def DeleteInstance(self, request):
        """删除milvus实例
        :param request: Request instance for DeleteInstance.
        :type request: :class:`ksyun.client.milvus.v20231010.models.DeleteInstanceRequest`
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


    def DescribeInstance(self, request):
        """查询milvus实例详情
        :param request: Request instance for DescribeInstance.
        :type request: :class:`ksyun.client.milvus.v20231010.models.DescribeInstanceRequest`
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


    def ListInstance(self, request):
        """查询milvus实例列表
        :param request: Request instance for ListInstance.
        :type request: :class:`ksyun.client.milvus.v20231010.models.ListInstanceRequest`
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


    def CreateInstance(self, request):
        """创建milvus实例
        :param request: Request instance for CreateInstance.
        :type request: :class:`ksyun.client.milvus.v20231010.models.CreateInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ReleaseDBInstanceEip(self, request):
        """实例-释放EIP
        :param request: Request instance for ReleaseDBInstanceEip.
        :type request: :class:`ksyun.client.milvus.v20231010.models.ReleaseDBInstanceEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReleaseDBInstanceEip", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AllocateDBInstanceEip(self, request):
        """实例-申请EIP
        :param request: Request instance for AllocateDBInstanceEip.
        :type request: :class:`ksyun.client.milvus.v20231010.models.AllocateDBInstanceEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AllocateDBInstanceEip", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询指定实例备份列表
        :param request: Request instance for ListBackup.
        :type request: :class:`ksyun.client.milvus.v20231010.models.ListBackupRequest`
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


    def CreateBackup(self, request):
        """指定备份维度手动创建备份
        :param request: Request instance for CreateBackup.
        :type request: :class:`ksyun.client.milvus.v20231010.models.CreateBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteBackup(self, request):
        """删除指定手动备份
        :param request: Request instance for DeleteBackup.
        :type request: :class:`ksyun.client.milvus.v20231010.models.DeleteBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBackup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListCollections(self, request):
        """备份-查询实例库表详情
        :param request: Request instance for ListCollections.
        :type request: :class:`ksyun.client.milvus.v20231010.models.ListCollectionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListCollections", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UpdateInstanceTrialOrder(self, request):
        """适用类型订单实例转正/延期
        :param request: Request instance for UpdateInstanceTrialOrder.
        :type request: :class:`ksyun.client.milvus.v20231010.models.UpdateInstanceTrialOrderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateInstanceTrialOrder", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


