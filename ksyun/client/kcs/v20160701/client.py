import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KcsClient(AbstractClient):
    _apiVersion = '2016-07-01'
    _endpoint = 'kcs.api.ksyun.com'
    _service = 'kcs'
    def CreateCacheCluster(self, request):
        """创建实例
        :param request: Request instance for CreateCacheCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.CreateCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCacheCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteCacheCluster(self, request):
        """删除实例
        :param request: Request instance for DeleteCacheCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeleteCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCacheCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCacheCluster(self, request):
        """查询实例详情
        :param request: Request instance for DescribeCacheCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCacheClusters(self, request):
        """查看实例列表
        :param request: Request instance for DescribeCacheClusters.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeCacheClustersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheClusters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def FlushCacheCluster(self, request):
        """清空缓存
        :param request: Request instance for FlushCacheCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.FlushCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("FlushCacheCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RenameCacheCluster(self, request):
        """修改实例名称
        :param request: Request instance for RenameCacheCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.RenameCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenameCacheCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ResizeCacheCluster(self, request):
        """更配实例
        :param request: Request instance for ResizeCacheCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.ResizeCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResizeCacheCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCacheParameters(self, request):
        """查询缓存服务参数
        :param request: Request instance for DescribeCacheParameters.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeCacheParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheParameters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def SetCacheParameters(self, request):
        """设置缓存服务参数
        :param request: Request instance for SetCacheParameters.
        :type request: :class:`ksyun.client.kcs.v20160701.models.SetCacheParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetCacheParameters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCacheDefaultParameters(self, request):
        """DescribeCacheDefaultParameters
        :param request: Request instance for DescribeCacheDefaultParameters.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeCacheDefaultParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheDefaultParameters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def SetCacheParameterGroup(self, request):
        """应用参数组，将参数组中所有的参数的当前值应用到指定的缓存服务对应参数上
        :param request: Request instance for SetCacheParameterGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.SetCacheParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetCacheParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateCacheParameterGroup(self, request):
        """创建参数组
        :param request: Request instance for CreateCacheParameterGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.CreateCacheParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCacheParameterGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteCacheParameterGroup(self, request):
        """删除参数组
        :param request: Request instance for DeleteCacheParameterGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeleteCacheParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCacheParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyCacheParameterGroup(self, request):
        """修改参数组
        :param request: Request instance for ModifyCacheParameterGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.ModifyCacheParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCacheParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCacheParameterGroups(self, request):
        """根据参数组的名称以及ID进行参数组查询
        :param request: Request instance for DescribeCacheParameterGroups.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeCacheParameterGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheParameterGroups", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCacheParameterGroup(self, request):
        """查询参数组详情
        :param request: Request instance for DescribeCacheParameterGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeCacheParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def SetTimingSnapshot(self, request):
        """设置备份时间
        :param request: Request instance for SetTimingSnapshot.
        :type request: :class:`ksyun.client.kcs.v20160701.models.SetTimingSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetTimingSnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteSnapshot(self, request):
        """删除备份
        :param request: Request instance for DeleteSnapshot.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeleteSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RenameSnapshot(self, request):
        """重命名备份
        :param request: Request instance for RenameSnapshot.
        :type request: :class:`ksyun.client.kcs.v20160701.models.RenameSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenameSnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RestoreSnapshot(self, request):
        """恢复备份
        :param request: Request instance for RestoreSnapshot.
        :type request: :class:`ksyun.client.kcs.v20160701.models.RestoreSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreSnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeSnapshots(self, request):
        """获取备份列表
        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeSnapshotsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSnapshots", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DownloadSnapshot(self, request):
        """下载备份
        :param request: Request instance for DownloadSnapshot.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DownloadSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DownloadSnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ExportSnapshot(self, request):
        """ExportSnapshot
        :param request: Request instance for ExportSnapshot.
        :type request: :class:`ksyun.client.kcs.v20160701.models.ExportSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ExportSnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeRegions(self, request):
        """查询机房
        :param request: Request instance for DescribeRegions.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeRegionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRegions", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeAvailabilityZones(self, request):
        """查询可用区
        :param request: Request instance for DescribeAvailabilityZones.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeAvailabilityZonesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAvailabilityZones", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCacheByRole(self, request):
        """通过角色查询缓存服务列表接口
        :param request: Request instance for DescribeCacheByRole.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeCacheByRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCacheByRole", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def StatisticDBInstances(self, request):
        """概览页统计查询
        :param request: Request instance for StatisticDBInstances.
        :type request: :class:`ksyun.client.kcs.v20160701.models.StatisticDBInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StatisticDBInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UpdatePassword(self, request):
        """修改缓存服务密码
        :param request: Request instance for UpdatePassword.
        :type request: :class:`ksyun.client.kcs.v20160701.models.UpdatePasswordRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdatePassword", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RestartCacheCluster(self, request):
        """实例重启
        :param request: Request instance for RestartCacheCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.RestartCacheClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestartCacheCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AllocateEip(self, request):
        """申请EIP
        :param request: Request instance for AllocateEip.
        :type request: :class:`ksyun.client.kcs.v20160701.models.AllocateEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AllocateEip", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeallocateEip(self, request):
        """释放EIP
        :param request: Request instance for DeallocateEip.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeallocateEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeallocateEip", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeInstances(self, request):
        """安全组-查询实例信息
        :param request: Request instance for DescribeInstances.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteSecurityGroupRule(self, request):
        """删除安全组规则
        :param request: Request instance for DeleteSecurityGroupRule.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeleteSecurityGroupRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityGroupRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateSecurityGroupRule(self, request):
        """创建安全组规则
        :param request: Request instance for CreateSecurityGroupRule.
        :type request: :class:`ksyun.client.kcs.v20160701.models.CreateSecurityGroupRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityGroupRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeallocateSecurityGroup(self, request):
        """解绑安全组
        :param request: Request instance for DeallocateSecurityGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeallocateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeallocateSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AllocateSecurityGroup(self, request):
        """绑定安全组
        :param request: Request instance for AllocateSecurityGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.AllocateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AllocateSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询安全组明细
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeSecurityGroupRequest`
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


    def DescribeSecurityGroups(self, request):
        """查询安全组列表
        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeSecurityGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSecurityGroups", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.kcs.v20160701.models.ModifySecurityGroupRequest`
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


    def DeleteSecurityGroup(self, request):
        """删除安全组
        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeleteSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """克隆安全组
        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.CloneSecurityGroupRequest`
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


    def CreateSecurityGroup(self, request):
        """创建安全组
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.kcs.v20160701.models.CreateSecurityGroupRequest`
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


    def DescribeHotKeys(self, request):
        """查询热key列表
        :param request: Request instance for DescribeHotKeys.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeHotKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeHotKeys", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AnalyzeHotKeys(self, request):
        """热key分析按钮
        :param request: Request instance for AnalyzeHotKeys.
        :type request: :class:`ksyun.client.kcs.v20160701.models.AnalyzeHotKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AnalyzeHotKeys", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CloseDirectAccessToCluster(self, request):
        """cluster关闭直连
        :param request: Request instance for CloseDirectAccessToCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.CloseDirectAccessToClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloseDirectAccessToCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def OpenDirectAccessToCluster(self, request):
        """cluster开启直连
        :param request: Request instance for OpenDirectAccessToCluster.
        :type request: :class:`ksyun.client.kcs.v20160701.models.OpenDirectAccessToClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OpenDirectAccessToCluster", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeParentBackUpsSnapshots(self, request):
        """redis集群备份数据父列表数据
        :param request: Request instance for DescribeParentBackUpsSnapshots.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeParentBackUpsSnapshotsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeParentBackUpsSnapshots", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeBackUpsSnapshotsDetail(self, request):
        """redis集群备份数据子列表数据
        :param request: Request instance for DescribeBackUpsSnapshotsDetail.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeBackUpsSnapshotsDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBackUpsSnapshotsDetail", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteLevelSnapshots(self, request):
        """redis集群层级备份数据删除
        :param request: Request instance for DeleteLevelSnapshots.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeleteLevelSnapshotsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteLevelSnapshots", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DownloadLevelSnapshot(self, request):
        """redis集群层次备份数据下载
        :param request: Request instance for DownloadLevelSnapshot.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DownloadLevelSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DownloadLevelSnapshot", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeBigKeys(self, request):
        """获取大key分析的任务结果列表
        :param request: Request instance for DescribeBigKeys.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeBigKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBigKeys", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteBigKeysAnalyseResult(self, request):
        """删除大key分析任务列表数据
        :param request: Request instance for DeleteBigKeysAnalyseResult.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DeleteBigKeysAnalyseResultRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBigKeysAnalyseResult", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AnalyzeBigKeys(self, request):
        """获取大key分析的结果
        :param request: Request instance for AnalyzeBigKeys.
        :type request: :class:`ksyun.client.kcs.v20160701.models.AnalyzeBigKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AnalyzeBigKeys", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCreateSnapshotStatus(self, request):
        """创建备份前的备份状态和大key分析状态查询
        :param request: Request instance for DescribeCreateSnapshotStatus.
        :type request: :class:`ksyun.client.kcs.v20160701.models.DescribeCreateSnapshotStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCreateSnapshotStatus", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetDailyAnalyzeSwitchState(self, request):
        """慢日志和运行日志分析开关
        :param request: Request instance for GetDailyAnalyzeSwitchState.
        :type request: :class:`ksyun.client.kcs.v20160701.models.GetDailyAnalyzeSwitchStateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDailyAnalyzeSwitchState", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AnalyzeDaily(self, request):
        """运行日志分析
        :param request: Request instance for AnalyzeDaily.
        :type request: :class:`ksyun.client.kcs.v20160701.models.AnalyzeDailyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AnalyzeDaily", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AnalyzeSlowDaily(self, request):
        """慢日志分析
        :param request: Request instance for AnalyzeSlowDaily.
        :type request: :class:`ksyun.client.kcs.v20160701.models.AnalyzeSlowDailyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AnalyzeSlowDaily", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AnalyzeDailySwitch(self, request):
        """AnalyzeDailySwitch
        :param request: Request instance for AnalyzeDailySwitch.
        :type request: :class:`ksyun.client.kcs.v20160701.models.AnalyzeDailySwitchRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AnalyzeDailySwitch", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


