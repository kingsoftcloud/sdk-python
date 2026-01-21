import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class DmpClient(AbstractClient):
    _apiVersion = '2024-01-01'
    _endpoint = 'dmp.api.ksyun.com'
    _service = 'dmp'
    def DescribeDefaultMonitorItems(self, request):
        """查询支持的监控项
        :param request: Request instance for DescribeDefaultMonitorItems.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeDefaultMonitorItemsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDefaultMonitorItems", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteMonitorPanel(self, request):
        """删除监控大盘
        :param request: Request instance for DeleteMonitorPanel.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DeleteMonitorPanelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteMonitorPanel", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def OperateMonitorPanel(self, request):
        """更新监控大盘
        :param request: Request instance for OperateMonitorPanel.
        :type request: :class:`ksyun.client.dmp.v20240101.models.OperateMonitorPanelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OperateMonitorPanel", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeMonitorPanel(self, request):
        """查询监控大盘详情
        :param request: Request instance for DescribeMonitorPanel.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeMonitorPanelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMonitorPanel", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyMonitorPanelInfo(self, request):
        """修改监控大盘信息
        :param request: Request instance for ModifyMonitorPanelInfo.
        :type request: :class:`ksyun.client.dmp.v20240101.models.ModifyMonitorPanelInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyMonitorPanelInfo", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateMonitorPanel(self, request):
        """创建监控大盘
        :param request: Request instance for CreateMonitorPanel.
        :type request: :class:`ksyun.client.dmp.v20240101.models.CreateMonitorPanelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateMonitorPanel", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteBatchInstances(self, request):
        """批量删除实例
        :param request: Request instance for DeleteBatchInstances.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DeleteBatchInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBatchInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def InstanceStatistics(self, request):
        """实例资产统计
        :param request: Request instance for InstanceStatistics.
        :type request: :class:`ksyun.client.dmp.v20240101.models.InstanceStatisticsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("InstanceStatistics", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeMonitorPanelList(self, request):
        """查询监控大盘列表
        :param request: Request instance for DescribeMonitorPanelList.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeMonitorPanelListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMonitorPanelList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeInstanceList(self, request):
        """查询实例列表
        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeInstanceListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ImportInstanceToDmp(self, request):
        """导入实例至KDMP
        :param request: Request instance for ImportInstanceToDmp.
        :type request: :class:`ksyun.client.dmp.v20240101.models.ImportInstanceToDmpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ImportInstanceToDmp", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDedicatedClusters(self, request):
        """查询专属集群列表
        :param request: Request instance for DescribeDedicatedClusters.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeDedicatedClustersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDedicatedClusters", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDedicatedHosts(self, request):
        """查询专属集群主机列表
        :param request: Request instance for DescribeDedicatedHosts.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeDedicatedHostsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDedicatedHosts", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDatabaseSchema(self, request):
        """查询数据库模式
        :param request: Request instance for DescribeDatabaseSchema.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeDatabaseSchemaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDatabaseSchema", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDatabaseList(self, request):
        """查询数据库列表
        :param request: Request instance for DescribeDatabaseList.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeDatabaseListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDatabaseList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeHistorySQL(self, request):
        """查询执行历史SQL
        :param request: Request instance for DescribeHistorySQL.
        :type request: :class:`ksyun.client.dmp.v20240101.models.DescribeHistorySQLRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeHistorySQL", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def StartExecuteSQL(self, request):
        """开始执行sql
        :param request: Request instance for StartExecuteSQL.
        :type request: :class:`ksyun.client.dmp.v20240101.models.StartExecuteSQLRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartExecuteSQL", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateInstanceDatabase(self, request):
        """刷新实例数据库信息
        :param request: Request instance for UpdateInstanceDatabase.
        :type request: :class:`ksyun.client.dmp.v20240101.models.UpdateInstanceDatabaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateInstanceDatabase", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateDatabaseTable(self, request):
        """更新数据库表信息
        :param request: Request instance for UpdateDatabaseTable.
        :type request: :class:`ksyun.client.dmp.v20240101.models.UpdateDatabaseTableRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDatabaseTable", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def TestInstanceConnection(self, request):
        """测试实例连通性
        :param request: Request instance for TestInstanceConnection.
        :type request: :class:`ksyun.client.dmp.v20240101.models.TestInstanceConnectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("TestInstanceConnection", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
