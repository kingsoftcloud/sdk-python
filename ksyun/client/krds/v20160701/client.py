import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KrdsClient(AbstractClient):
    _apiVersion = '2016-07-01'
    _endpoint = 'krds.api.ksyun.com'
    _service = 'krds'

    def RebootDBInstance(self, request):
        """reboot db instance
        :param request: Request instance for RebootDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.RebootDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebootDBInstance", params, "application/json")
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

    def ModifyDBParameterGroup(self, request):
        """modify db parameter group
        :param request: Request instance for ModifyDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBParameterGroup", params, "application/json")
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

    def ResetDBParameterGroup(self, request):
        """reset db parameter group
        :param request: Request instance for ResetDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.ResetDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetDBParameterGroup", params, "application/json")
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

    def DescribeDBParameterGroup(self, request):
        """describe db parameter group
        :param request: Request instance for DescribeDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBParameterGroup", params, "application/json")
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

    def DescribeEngineDefaultParameters(self, request):
        """describe engine default parameters
        :param request: Request instance for DescribeEngineDefaultParameters.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeEngineDefaultParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEngineDefaultParameters", params, "application/json")
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

    def CreateDBParameterGroup(self, request):
        """create db parameter group
        :param request: Request instance for CreateDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBParameterGroup", params, "application/json")
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

    def DeleteDBParameterGroup(self, request):
        """delete db parameter group
        :param request: Request instance for DeleteDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBParameterGroup", params, "application/json")
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

    def CreateDBInstance(self, request):
        """create db instance
        :param request: Request instance for CreateDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBInstance", params, "application/json")
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

    def RestoreDBInstanceFromDBBackup(self, request):
        """restore db instance from db backup
        :param request: Request instance for RestoreDBInstanceFromDBBackup.
        :type request: :class:`ksyun.client.krds.v20160701.models.RestoreDBInstanceFromDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreDBInstanceFromDBBackup", params, "application/json")
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

    def DeleteDBInstance(self, request):
        """delete db instance
        :param request: Request instance for DeleteDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBInstance", params, "application/json")
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

    def CreateDBInstanceReadReplica(self, request):
        """create db instance read replica
        :param request: Request instance for CreateDBInstanceReadReplica.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateDBInstanceReadReplicaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBInstanceReadReplica", params, "application/json")
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

    def RestoreDBInstanceToPointInTime(self, request):
        """restore db instance to point in time
        :param request: Request instance for RestoreDBInstanceToPointInTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.RestoreDBInstanceToPointInTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreDBInstanceToPointInTime", params, "application/json")
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

    def DescribeDBInstanceRestorableTime(self, request):
        """describe db instance restorable time
        :param request: Request instance for DescribeDBInstanceRestorableTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstanceRestorableTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceRestorableTime", params, "application/json")
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

    def ModifyDBInstance(self, request):
        """modify db instance
        :param request: Request instance for ModifyDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstance", params, "application/json")
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

    def DescribeDBLogFiles(self, request):
        """describe db log files
        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBLogFilesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBLogFiles", params, "application/json")
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

    def DescribeDBBackups(self, request):
        """describe db backups
        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBBackupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBBackups", params, "application/json")
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

    def ModifyDBInstanceSpec(self, request):
        """modify db instance spec
        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceSpecRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceSpec", params, "application/json")
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

    def DescribeDBInstances(self, request):
        """describe db instances
        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstances", params, "application/json")
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

    def OverrideDBInstance(self, request):
        """基于备份恢复到本实例
        :param request: Request instance for OverrideDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.OverrideDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OverrideDBInstance", params, "application/json")
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

    def DescribeDBEngineVersions(self, request):
        """describe db engine versions
        :param request: Request instance for DescribeDBEngineVersions.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBEngineVersionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBEngineVersions", params, "application/json")
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

    def UpgradeDBInstanceEngineVersion(self, request):
        """upgrade db instance engine version
        :param request: Request instance for UpgradeDBInstanceEngineVersion.
        :type request: :class:`ksyun.client.krds.v20160701.models.UpgradeDBInstanceEngineVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpgradeDBInstanceEngineVersion", params, "application/json")
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

    def ModifyDBInstanceType(self, request):
        """modify db instance type
        :param request: Request instance for ModifyDBInstanceType.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceTypeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceType", params, "application/json")
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

    def DescribeDBInstanceParameters(self, request):
        """查看当前实例数据库参数运行值列表
        :param request: Request instance for DescribeDBInstanceParameters.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstanceParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceParameters", params, "application/json")
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

    def DeleteDBBackup(self, request):
        """delete db backup
        :param request: Request instance for DeleteDBBackup.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBBackup", params, "application/json")
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

    def CreateDBBackup(self, request):
        """create db backup
        :param request: Request instance for CreateDBBackup.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBBackup", params, "application/json")
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

    def RenewDBInstance(self, request):
        """renew db instance
        :param request: Request instance for RenewDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.RenewDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenewDBInstance", params, "application/json")
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

    def SwitchDBInstanceHA(self, request):
        """switch db instance h a
        :param request: Request instance for SwitchDBInstanceHA.
        :type request: :class:`ksyun.client.krds.v20160701.models.SwitchDBInstanceHARequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SwitchDBInstanceHA", params, "application/json")
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

    def GenerateDBAdminURL(self, request):
        """generate db admin u r l
        :param request: Request instance for GenerateDBAdminURL.
        :type request: :class:`ksyun.client.krds.v20160701.models.GenerateDBAdminURLRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GenerateDBAdminURL", params, "application/json")
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
        """statistic db instances
        :param request: Request instance for StatisticDBInstances.
        :type request: :class:`ksyun.client.krds.v20160701.models.StatisticDBInstancesRequest`
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

    def AllocateDBInstanceEip(self, request):
        """申请外网访问IP地址
        :param request: Request instance for AllocateDBInstanceEip.
        :type request: :class:`ksyun.client.krds.v20160701.models.AllocateDBInstanceEipRequest`
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

    def ReleaseDBInstanceEip(self, request):
        """释放外网访问IP地址
        :param request: Request instance for ReleaseDBInstanceEip.
        :type request: :class:`ksyun.client.krds.v20160701.models.ReleaseDBInstanceEipRequest`
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

    def ModifyDBInstanceAvailabilityZone(self, request):
        """修改实例备库可用区
        :param request: Request instance for ModifyDBInstanceAvailabilityZone.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceAvailabilityZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceAvailabilityZone", params, "application/json")
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

    def DescribeDBInstanceRegions(self, request):
        """查看机房列表
        :param request: Request instance for DescribeDBInstanceRegions.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstanceRegionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceRegions", params, "application/json")
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

    def DescribeDBInstancePackages(self, request):
        """查看购买套餐
        :param request: Request instance for DescribeDBInstancePackages.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstancePackagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstancePackages", params, "application/json")
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

    def DescribeLastLog(self, request):
        """DescribeLastLog
        :param request: Request instance for DescribeLastLog.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeLastLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeLastLog", params, "application/json")
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

    def StartAudit(self, request):
        """开启审计
        :param request: Request instance for StartAudit.
        :type request: :class:`ksyun.client.krds.v20160701.models.StartAuditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartAudit", params, "application/json")
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

    def StopAudit(self, request):
        """关闭审计
        :param request: Request instance for StopAudit.
        :type request: :class:`ksyun.client.krds.v20160701.models.StopAuditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopAudit", params, "application/json")
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

    def ListAudit(self, request):
        """获取审计结果
        :param request: Request instance for ListAudit.
        :type request: :class:`ksyun.client.krds.v20160701.models.ListAuditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListAudit", params, "application/json")
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

    def AuditStatistic(self, request):
        """获取审计统计数据
        :param request: Request instance for AuditStatistic.
        :type request: :class:`ksyun.client.krds.v20160701.models.AuditStatisticRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AuditStatistic", params, "application/json")
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

    def GetTableRestorableTime(self, request):
        """获取数据库可恢复时间
        :param request: Request instance for GetTableRestorableTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.GetTableRestorableTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetTableRestorableTime", params, "application/json")
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

    def GetHistoryDatabaseInfo(self, request):
        """获取指定时间点附近或者备份集的库表信息
        :param request: Request instance for GetHistoryDatabaseInfo.
        :type request: :class:`ksyun.client.krds.v20160701.models.GetHistoryDatabaseInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetHistoryDatabaseInfo", params, "application/json")
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

    def OverrideDBInstanceByPointInTime(self, request):
        """恢复实例到当前时间点
        :param request: Request instance for OverrideDBInstanceByPointInTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.OverrideDBInstanceByPointInTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OverrideDBInstanceByPointInTime", params, "application/json")
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

    def RestoreToCurInstance(self, request):
        """库表级恢复到当前实例
        :param request: Request instance for RestoreToCurInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.RestoreToCurInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreToCurInstance", params, "application/json")
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

    def RestoreToSgInstance(self, request):
        """库表级恢复到临时实例
        :param request: Request instance for RestoreToSgInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.RestoreToSgInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreToSgInstance", params, "application/json")
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

    def DescribeAuditHotCount(self, request):
        """某时间段SQL执行次数TOP10查询接口
        :param request: Request instance for DescribeAuditHotCount.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeAuditHotCountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAuditHotCount", params, "application/json")
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

    def DescribeAuditHotDuration(self, request):
        """某时间段SQL执行耗时TOP10查询接口
        :param request: Request instance for DescribeAuditHotDuration.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeAuditHotDurationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAuditHotDuration", params, "application/json")
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

    def SqlAuditReport(self, request):
        """某时间段全量SQL统计查询接口
        :param request: Request instance for SqlAuditReport.
        :type request: :class:`ksyun.client.krds.v20160701.models.SqlAuditReportRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SqlAuditReport", params, "application/json")
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

    def SqlAuditLineChart(self, request):
        """某时间段全量SQL折线图查询接口
        :param request: Request instance for SqlAuditLineChart.
        :type request: :class:`ksyun.client.krds.v20160701.models.SqlAuditLineChartRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SqlAuditLineChart", params, "application/json")
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

    def SlowLogReport(self, request):
        """某时间段慢SQL统计查询接口
        :param request: Request instance for SlowLogReport.
        :type request: :class:`ksyun.client.krds.v20160701.models.SlowLogReportRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SlowLogReport", params, "application/json")
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

    def SlowLogLineChart(self, request):
        """某时间段慢SQL折线图查询接口
        :param request: Request instance for SlowLogLineChart.
        :type request: :class:`ksyun.client.krds.v20160701.models.SlowLogLineChartRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SlowLogLineChart", params, "application/json")
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

    def SlowLogDetail(self, request):
        """某时间段慢SQL查询接口
        :param request: Request instance for SlowLogDetail.
        :type request: :class:`ksyun.client.krds.v20160701.models.SlowLogDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SlowLogDetail", params, "application/json")
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

    def StartAuditDetailExportTask(self, request):
        """创建导出任务
        :param request: Request instance for StartAuditDetailExportTask.
        :type request: :class:`ksyun.client.krds.v20160701.models.StartAuditDetailExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartAuditDetailExportTask", params, "application/json")
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

    def ListAuditDetailExportTask(self, request):
        """列出历史导出任务
        :param request: Request instance for ListAuditDetailExportTask.
        :type request: :class:`ksyun.client.krds.v20160701.models.ListAuditDetailExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListAuditDetailExportTask", params, "application/json")
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

    def DescribeInstanceAccounts(self, request):
        """DescribeInstanceAccounts
        :param request: Request instance for DescribeInstanceAccounts.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeInstanceAccountsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceAccounts", params, "application/json")
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

    def ModifyInstanceAccountInfo(self, request):
        """ModifyInstanceAccountInfo
        :param request: Request instance for ModifyInstanceAccountInfo.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceAccountInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAccountInfo", params, "application/json")
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

    def DescribeCollations(self, request):
        """DescribeCollations
        :param request: Request instance for DescribeCollations.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeCollationsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCollations", params, "application/json")
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

    def CreateInstanceDatabase(self, request):
        """CreateInstanceDatabase
        :param request: Request instance for CreateInstanceDatabase.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateInstanceDatabaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstanceDatabase", params, "application/json")
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

    def ModifyInstanceDatabasePrivileges(self, request):
        """ModifyInstanceDatabasePrivileges
        :param request: Request instance for ModifyInstanceDatabasePrivileges.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceDatabasePrivilegesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabasePrivileges", params, "application/json")
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

    def DescribeInstanceDatabases(self, request):
        """DescribeInstanceDatabases
        :param request: Request instance for DescribeInstanceDatabases.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeInstanceDatabasesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceDatabases", params, "application/json")
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

    def ModifyInstanceDatabaseInfo(self, request):
        """ModifyInstanceDatabaseInfo
        :param request: Request instance for ModifyInstanceDatabaseInfo.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceDatabaseInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabaseInfo", params, "application/json")
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

    def StartSlowLogDetailExportTask(self, request):
        """StartSlowLogDetailExportTask
        :param request: Request instance for StartSlowLogDetailExportTask.
        :type request: :class:`ksyun.client.krds.v20160701.models.StartSlowLogDetailExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartSlowLogDetailExportTask", params, "application/json")
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

    def ListSlowLogDetailExportTask(self, request):
        """ListSlowLogDetailExportTask
        :param request: Request instance for ListSlowLogDetailExportTask.
        :type request: :class:`ksyun.client.krds.v20160701.models.ListSlowLogDetailExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSlowLogDetailExportTask", params, "application/json")
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

    def CreateInstanceAccountAction(self, request):
        """CreateInstanceAccountAction
        :param request: Request instance for CreateInstanceAccountAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateInstanceAccountActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstanceAccountAction", params, "application/x-www-form-urlencoded")
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

    def ModifyInstanceAccountPrivilegesAction(self, request):
        """ModifyInstanceAccountPrivilegesAction
        :param request: Request instance for ModifyInstanceAccountPrivilegesAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceAccountPrivilegesActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAccountPrivilegesAction", params, "application/x-www-form-urlencoded")
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

    def DeleteInstanceAccountAction(self, request):
        """DeleteInstanceAccountAction
        :param request: Request instance for DeleteInstanceAccountAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteInstanceAccountActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstanceAccountAction", params, "application/x-www-form-urlencoded")
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

    def DeleteInstanceDatabaseAction(self, request):
        """DeleteInstanceDatabaseAction
        :param request: Request instance for DeleteInstanceDatabaseAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteInstanceDatabaseActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstanceDatabaseAction", params, "application/x-www-form-urlencoded")
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

    def ModifyDBNetwork(self, request):
        """修改ip/vpc
        :param request: Request instance for ModifyDBNetwork.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBNetworkRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBNetwork", params, "application/x-www-form-urlencoded")
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

    def DescribeEngineParametersModifyHistory(self, request):
        """参数组历史修改信息查询
        :param request: Request instance for DescribeEngineParametersModifyHistory.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeEngineParametersModifyHistoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEngineParametersModifyHistory", params, "application/json")
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
