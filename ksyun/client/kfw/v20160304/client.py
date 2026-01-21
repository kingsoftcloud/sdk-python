import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KfwClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'kfw.api.ksyun.com'
    _service = 'kfw'

    def DeleteBatchCfwAddrbook(self, request):
        """批量删除地址簿
        :param request: Request instance for DeleteBatchCfwAddrbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DeleteBatchCfwAddrbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBatchCfwAddrbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DeleteServiceGroupBatch(self, request):
        """批量删除服务组
        :param request: Request instance for DeleteServiceGroupBatch.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DeleteServiceGroupBatchRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteServiceGroupBatch", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DeleteBatchHostbook(self, request):
        """批量删除域名簿
        :param request: Request instance for DeleteBatchHostbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DeleteBatchHostbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBatchHostbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def ModifyHostbook(self, request):
        """修改已存在的域名簿信息，包括名称、域名列表和描述
        :param request: Request instance for ModifyHostbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.ModifyHostbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyHostbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def CreateHostbook(self, request):
        """创建域名簿，用于管理防火墙的域名白名单
        :param request: Request instance for CreateHostbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.CreateHostbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateHostbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeHostbook(self, request):
        """查询域名簿
        :param request: Request instance for DescribeHostbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeHostbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeHostbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def QueryCfwInstanceDetail(self, request):
        """查询防火墙详情
        :param request: Request instance for QueryCfwInstanceDetail.
        :type request: :class:`ksyun.client.kfw.v20160304.models.QueryCfwInstanceDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryCfwInstanceDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DeleteCloudFireWallInstance(self, request):
        """退订云防火墙
        :param request: Request instance for DeleteCloudFireWallInstance.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DeleteCloudFireWallInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCloudFireWallInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def QueryOverviewDetail(self, request):
        """查询指定防火墙实例在指定时间段内的总览统计数据，包括ACL拒绝次数、IPS检测次数、入站和出站流量峰值等信息
        :param request: Request instance for QueryOverviewDetail.
        :type request: :class:`ksyun.client.kfw.v20160304.models.QueryOverviewDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryOverviewDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeTrafficLog(self, request):
        """流量日志查询
        :param request: Request instance for DescribeTrafficLog.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeTrafficLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeTrafficLog", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeAttackLog(self, request):
        """根据指定的时间范围和条件查询防火墙攻击日志，支持关键字搜索和分页查询
        :param request: Request instance for DescribeAttackLog.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeAttackLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAttackLog", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeAclLog(self, request):
        """访问控制日志查询
        :param request: Request instance for DescribeAclLog.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeAclLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAclLog", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def ModifyCloudFireWallFeature(self, request):
        """修改云防火墙名称
        :param request: Request instance for ModifyCloudFireWallFeature.
        :type request: :class:`ksyun.client.kfw.v20160304.models.ModifyCloudFireWallFeatureRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCloudFireWallFeature", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeCfwAddrbook(self, request):
        """查询地址簿
        :param request: Request instance for DescribeCfwAddrbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeCfwAddrbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCfwAddrbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DeleteCfwAddrbook(self, request):
        """删除地址簿
        :param request: Request instance for DeleteCfwAddrbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DeleteCfwAddrbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCfwAddrbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def ModifyCfwAddrbook(self, request):
        """修改云防火墙地址簿的配置信息，包括地址簿名称、IP地址列表、描述信息等。支持批量更新多个IP地址，最多支持640个IP地址成员。
        :param request: Request instance for ModifyCfwAddrbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.ModifyCfwAddrbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCfwAddrbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def CreateCfwAddrbook(self, request):
        """创建地址簿
        :param request: Request instance for CreateCfwAddrbook.
        :type request: :class:`ksyun.client.kfw.v20160304.models.CreateCfwAddrbookRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCfwAddrbook", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def AlterCfwAclStatus(self, request):
        """用于批量修改云防火墙ACL规则的启用状态，支持同时开启或关闭多个ACL规则，操作后规则状态将立即生效
        :param request: Request instance for AlterCfwAclStatus.
        :type request: :class:`ksyun.client.kfw.v20160304.models.AlterCfwAclStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AlterCfwAclStatus", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def ResetCfwAclHitCount(self, request):
        """ACL重置命中数
        :param request: Request instance for ResetCfwAclHitCount.
        :type request: :class:`ksyun.client.kfw.v20160304.models.ResetCfwAclHitCountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetCfwAclHitCount", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def AlterAclPriority(self, request):
        """改acl优先级
        :param request: Request instance for AlterAclPriority.
        :type request: :class:`ksyun.client.kfw.v20160304.models.AlterAclPriorityRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AlterAclPriority", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DeleteCfwAcl(self, request):
        """删除ACL
        :param request: Request instance for DeleteCfwAcl.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DeleteCfwAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCfwAcl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def ModifyCfwAcl(self, request):
        """修改ACL
        :param request: Request instance for ModifyCfwAcl.
        :type request: :class:`ksyun.client.kfw.v20160304.models.ModifyCfwAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCfwAcl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeCfwAcl(self, request):
        """查询ACL
        :param request: Request instance for DescribeCfwAcl.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeCfwAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCfwAcl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def CreateCfwAcl(self, request):
        """创建ACL
        :param request: Request instance for CreateCfwAcl.
        :type request: :class:`ksyun.client.kfw.v20160304.models.CreateCfwAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCfwAcl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def ModifyCfwEipProtect(self, request):
        """Eip开启/关闭防护
        :param request: Request instance for ModifyCfwEipProtect.
        :type request: :class:`ksyun.client.kfw.v20160304.models.ModifyCfwEipProtectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCfwEipProtect", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeCfwEips(self, request):
        """查询EIP
        :param request: Request instance for DescribeCfwEips.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeCfwEipsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCfwEips", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeServiceGroup(self, request):
        """查询服务组
        :param request: Request instance for DescribeServiceGroup.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeServiceGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeServiceGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def ModifyCfwServiceGroup(self, request):
        """修改服务组
        :param request: Request instance for ModifyCfwServiceGroup.
        :type request: :class:`ksyun.client.kfw.v20160304.models.ModifyCfwServiceGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCfwServiceGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DeleteCfwServiceGroup(self, request):
        """删除服务组
        :param request: Request instance for DeleteCfwServiceGroup.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DeleteCfwServiceGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCfwServiceGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def CreateCfwServiceGroup(self, request):
        """创建服务组
        :param request: Request instance for CreateCfwServiceGroup.
        :type request: :class:`ksyun.client.kfw.v20160304.models.CreateCfwServiceGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCfwServiceGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DescribeCloudFireWallInstance(self, request):
        """查询防火墙
        :param request: Request instance for DescribeCloudFireWallInstance.
        :type request: :class:`ksyun.client.kfw.v20160304.models.DescribeCloudFireWallInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCloudFireWallInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
