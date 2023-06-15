import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class MongodbClient(AbstractClient):
    _apiVersion = '2017-01-01'
    _endpoint = 'mongodb.api.ksyun.com'
    _service = 'mongodb'
    def CreateMongoDBInstance(self, request):
        """创建副本集实例
        :param request: Request instance for CreateMongoDBInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.CreateMongoDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateMongoDBInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteMongoDBInstance(self, request):
        """删除实例
        :param request: Request instance for DeleteMongoDBInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DeleteMongoDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteMongoDBInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeMongoDBInstance(self, request):
        """查询实例详情
        :param request: Request instance for DescribeMongoDBInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeMongoDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeMongoDBInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeMongoDBInstances(self, request):
        """查询账号下实例列表
        :param request: Request instance for DescribeMongoDBInstances.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeMongoDBInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeMongoDBInstances", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeMongoDBInstanceNode(self, request):
        """查询副本集实例节点信息
        :param request: Request instance for DescribeMongoDBInstanceNode.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeMongoDBInstanceNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeMongoDBInstanceNode", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RenameMongoDBInstance(self, request):
        """实例重命名
        :param request: Request instance for RenameMongoDBInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.RenameMongoDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("RenameMongoDBInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ResetPasswordMongoDBInstance(self, request):
        """修改密码
        :param request: Request instance for ResetPasswordMongoDBInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.ResetPasswordMongoDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ResetPasswordMongoDBInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RestartMongoDBInstance(self, request):
        """重启实例
        :param request: Request instance for RestartMongoDBInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.RestartMongoDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("RestartMongoDBInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateMongoDBSnapshot(self, request):
        """创建手动备份
        :param request: Request instance for CreateMongoDBSnapshot.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.CreateMongoDBSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateMongoDBSnapshot", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def SetMongoDBTimingSnapshot(self, request):
        """自动备份设置
        :param request: Request instance for SetMongoDBTimingSnapshot.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.SetMongoDBTimingSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call("SetMongoDBTimingSnapshot", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeMongoDBSnapshot(self, request):
        """查询实例备份记录列表
        :param request: Request instance for DescribeMongoDBSnapshot.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeMongoDBSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeMongoDBSnapshot", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteMongoDBSnapshot(self, request):
        """删除备份
        :param request: Request instance for DeleteMongoDBSnapshot.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DeleteMongoDBSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteMongoDBSnapshot", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RenameMongoDBSnapshot(self, request):
        """备份重命名
        :param request: Request instance for RenameMongoDBSnapshot.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.RenameMongoDBSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call("RenameMongoDBSnapshot", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddSecurityGroupRule(self, request):
        """添加安全组规则
        :param request: Request instance for AddSecurityGroupRule.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.AddSecurityGroupRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AddSecurityGroupRule", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ListSecurityGroupRules(self, request):
        """查询安全组列表
        :param request: Request instance for ListSecurityGroupRules.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.ListSecurityGroupRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListSecurityGroupRules", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UpdateMongoDBInstance(self, request):
        """副本集实例更配
        :param request: Request instance for UpdateMongoDBInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.UpdateMongoDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdateMongoDBInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddSecondaryInstance(self, request):
        """副本集实例添加secondary节点
        :param request: Request instance for AddSecondaryInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.AddSecondaryInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AddSecondaryInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeMongoDBShardNode(self, request):
        """分片集群实例shard节点查询
        :param request: Request instance for DescribeMongoDBShardNode.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeMongoDBShardNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeMongoDBShardNode", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeValidRegion(self, request):
        """查询用户可用机房详情
        :param request: Request instance for DescribeValidRegion.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeValidRegionRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeValidRegion", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """实例绑定外网eip
        :param request: Request instance for AllocateEip.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.AllocateEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AllocateEip", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """实例解绑外网eip
        :param request: Request instance for DeallocateEip.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DeallocateEipRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeallocateEip", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询机房可用区
        :param request: Request instance for DescribeRegions.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeRegionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateMongoDBShardInstance(self, request):
        """创建分片集群实例
        :param request: Request instance for CreateMongoDBShardInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.CreateMongoDBShardInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateMongoDBShardInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DownloadSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DownloadSnapshot", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CloneInstance(self, request):
        """基于备份文件恢复至新实例
        :param request: Request instance for CloneInstance.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.CloneInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CloneInstance", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeShardNode(self, request):
        """查询分片集群shard节点列表
        :param request: Request instance for DescribeShardNode.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeShardNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeShardNode", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeInstanceStatistic(self, request):
        """概览页统计接口
        :param request: Request instance for DescribeInstanceStatistic.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeInstanceStatisticRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceStatistic", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddClusterNode(self, request):
        """添加分片集群的节点。支持mongos和shard节点。
        :param request: Request instance for AddClusterNode.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.AddClusterNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AddClusterNode", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteClusterNode(self, request):
        """删除分片集群节点，只支持mongos节点。
        :param request: Request instance for DeleteClusterNode.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DeleteClusterNodeRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteClusterNode", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeSlowLogDetail(self, request):
        """DescribeSlowLogDetail
        :param request: Request instance for DescribeSlowLogDetail.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeSlowLogDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogDetail", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeSlowLogStatistics(self, request):
        """DescribeSlowLogStatistics
        :param request: Request instance for DescribeSlowLogStatistics.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeSlowLogStatisticsRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogStatistics", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeSlowLogDatabase(self, request):
        """DescribeSlowLogDatabase
        :param request: Request instance for DescribeSlowLogDatabase.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeSlowLogDatabaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogDatabase", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeSlowLogLineChart(self, request):
        """慢查询产生趋势折线图，反映慢查询趋势。
        :param request: Request instance for DescribeSlowLogLineChart.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.DescribeSlowLogLineChartRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogLineChart", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UpdateMongoDBInstanceCluster(self, request):
        """分片集群节点更配
        :param request: Request instance for UpdateMongoDBInstanceCluster.
        :type request: :class:`ksyun.client.mongodb.v20170101.models.UpdateMongoDBInstanceClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdateMongoDBInstanceCluster", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


