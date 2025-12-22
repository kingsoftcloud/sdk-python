import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KrdsClient(AbstractClient):
    _apiVersion = '2016-07-01'
    _endpoint = 'krds.api.ksyun.com'
    _service = 'krds'
    def RebootDBInstance(self, request):
        """重启指定实例
        :param request: Request instance for RebootDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.RebootDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebootDBInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """修改参数组
        :param request: Request instance for ModifyDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBParameterGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """重置参数组
        :param request: Request instance for ResetDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.ResetDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResetDBParameterGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """参数组列表/详情
        :param request: Request instance for DescribeDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBParameterGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询默认参数模版(指定引擎及版本号)
        :param request: Request instance for DescribeEngineDefaultParameters.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeEngineDefaultParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEngineDefaultParameters", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建参数组
        :param request: Request instance for CreateDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBParameterGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """删除参数组
        :param request: Request instance for DeleteDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBParameterGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建实例(不含只读类型)
        :param request: Request instance for CreateDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """基于备份创建实例(临时/高可用)
        :param request: Request instance for RestoreDBInstanceFromDBBackup.
        :type request: :class:`ksyun.client.krds.v20160701.models.RestoreDBInstanceFromDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreDBInstanceFromDBBackup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """删除实例(不支持批量)
        :param request: Request instance for DeleteDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建只读实例(基于高可用实例)
        :param request: Request instance for CreateDBInstanceReadReplica.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateDBInstanceReadReplicaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBInstanceReadReplica", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """恢复数据到指定时间点(本实例/临时实例)
        :param request: Request instance for RestoreDBInstanceToPointInTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.RestoreDBInstanceToPointInTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreDBInstanceToPointInTime", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询可恢复到的时间点区间
        :param request: Request instance for DescribeDBInstanceRestorableTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstanceRestorableTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceRestorableTime", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """修改实例配置
        :param request: Request instance for ModifyDBInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询日志文件列表
        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBLogFilesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBLogFiles", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询备份列表
        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBBackupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBBackups", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """实例更配(修改内存磁盘配置)
        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceSpecRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceSpec", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询实例列表(详情)
        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
            body = self.call_judge("OverrideDBInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询数据库引擎版本(全量)
        :param request: Request instance for DescribeDBEngineVersions.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBEngineVersionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBEngineVersions", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """大版本升级(5.x)
        :param request: Request instance for UpgradeDBInstanceEngineVersion.
        :type request: :class:`ksyun.client.krds.v20160701.models.UpgradeDBInstanceEngineVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpgradeDBInstanceEngineVersion", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """实例类型转换
        :param request: Request instance for ModifyDBInstanceType.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceTypeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceType", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查看运行中参数
        :param request: Request instance for DescribeDBInstanceParameters.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstanceParametersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceParameters", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyDBBackupPolicy(self, request):
        """修改备份策略
        :param request: Request instance for ModifyDBBackupPolicy.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBBackupPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBBackupPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDBBackupPolicy(self, request):
        """查询备份策略
        :param request: Request instance for DescribeDBBackupPolicy.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBBackupPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBBackupPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """删除快照备份
        :param request: Request instance for DeleteDBBackup.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDBBackup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建快照备份
        :param request: Request instance for CreateDBBackup.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateDBBackupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDBBackup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """主备库切换
        :param request: Request instance for SwitchDBInstanceHA.
        :type request: :class:`ksyun.client.krds.v20160701.models.SwitchDBInstanceHARequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SwitchDBInstanceHA", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """获取登录链接
        :param request: Request instance for GenerateDBAdminURL.
        :type request: :class:`ksyun.client.krds.v20160701.models.GenerateDBAdminURLRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GenerateDBAdminURL", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
            body = self.call_judge("AllocateDBInstanceEip", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
            body = self.call_judge("ReleaseDBInstanceEip", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """迁移可用区
        :param request: Request instance for ModifyDBInstanceAvailabilityZone.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceAvailabilityZoneRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceAvailabilityZone", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建安全组(GET)
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateSecurityGroupRequest`
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


    def DescribeSecurityGroup(self, request):
        """查询安全组列表/详情
        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSecurityGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteSecurityGroupRequest`
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


    def ModifySecurityGroup(self, request):
        """修改安全组(描述/名称)
        :param request: Request instance for ModifySecurityGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifySecurityGroupRequest`
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


    def CloneSecurityGroup(self, request):
        """克隆安全组(仅含CIDR规则)
        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.CloneSecurityGroupRequest`
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


    def ModifySecurityGroupRule(self, request):
        """修改安全组规则
        :param request: Request instance for ModifySecurityGroupRule.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifySecurityGroupRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroupRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """修改安全组绑定关系
        :param request: Request instance for SecurityGroupRelation.
        :type request: :class:`ksyun.client.krds.v20160701.models.SecurityGroupRelationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SecurityGroupRelation", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifySecurityGroupRuleNameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroupRuleName", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """获取实时日志
        :param request: Request instance for DescribeLastLog.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeLastLogRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeLastLog", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询审计列表
        :param request: Request instance for ListAudit.
        :type request: :class:`ksyun.client.krds.v20160701.models.ListAuditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListAudit", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询审计统计数据列表
        :param request: Request instance for AuditStatistic.
        :type request: :class:`ksyun.client.krds.v20160701.models.AuditStatisticRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AuditStatistic", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetCurrentDatabaseInfo(self, request):
        """查询当前库表信息(前置)
        :param request: Request instance for GetCurrentDatabaseInfo.
        :type request: :class:`ksyun.client.krds.v20160701.models.GetCurrentDatabaseInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetCurrentDatabaseInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """获取可恢复时间段(前置)
        :param request: Request instance for GetTableRestorableTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.GetTableRestorableTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetTableRestorableTime", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """获取指定时间点/备份集附近的库表信息
        :param request: Request instance for GetHistoryDatabaseInfo.
        :type request: :class:`ksyun.client.krds.v20160701.models.GetHistoryDatabaseInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetHistoryDatabaseInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """恢复到原实例(指定时间点/备份集)
        :param request: Request instance for OverrideDBInstanceByPointInTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.OverrideDBInstanceByPointInTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("OverrideDBInstanceByPointInTime", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """恢复到原实例(指定库表)
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
        """恢复到临时实例
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
        """某时段SQL执行次数TOP10查询
        :param request: Request instance for DescribeAuditHotCount.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeAuditHotCountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAuditHotCount", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """某时段SQL执行耗时TOP10查询
        :param request: Request instance for DescribeAuditHotDuration.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeAuditHotDurationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAuditHotDuration", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """某时段全量SQL统计
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
        """某时段全量SQL折线图
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
        """慢日志统计
        :param request: Request instance for SlowLogReport.
        :type request: :class:`ksyun.client.krds.v20160701.models.SlowLogReportRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SlowLogReport", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """慢日志趋势图(折线图展示)
        :param request: Request instance for SlowLogLineChart.
        :type request: :class:`ksyun.client.krds.v20160701.models.SlowLogLineChartRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SlowLogLineChart", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """慢日志详情
        :param request: Request instance for SlowLogDetail.
        :type request: :class:`ksyun.client.krds.v20160701.models.SlowLogDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SlowLogDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
            body = self.call_judge("StartAuditDetailExportTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """导出任务列表(任务详情可下载)
        :param request: Request instance for ListAuditDetailExportTask.
        :type request: :class:`ksyun.client.krds.v20160701.models.ListAuditDetailExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListAuditDetailExportTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateInstanceAccount(self, request):
        """创建数据库账户(GET)
        :param request: Request instance for CreateInstanceAccount.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateInstanceAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstanceAccount", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询数据库账户列表
        :param request: Request instance for DescribeInstanceAccounts.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeInstanceAccountsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceAccounts", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """修改数据库账户信息
        :param request: Request instance for ModifyInstanceAccountInfo.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceAccountInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAccountInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyInstanceAccountPrivileges(self, request):
        """数据库账户赋权(GET)
        :param request: Request instance for ModifyInstanceAccountPrivileges.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceAccountPrivilegesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAccountPrivileges", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteInstanceAccount(self, request):
        """删除数据库账户(GET)
        :param request: Request instance for DeleteInstanceAccount.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteInstanceAccountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstanceAccount", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询字符集列表(指定实例)
        :param request: Request instance for DescribeCollations.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeCollationsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCollations", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建实例数据库
        :param request: Request instance for CreateInstanceDatabase.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateInstanceDatabaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstanceDatabase", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """数据库授权(GET)
        :param request: Request instance for ModifyInstanceDatabasePrivileges.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceDatabasePrivilegesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabasePrivileges", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询实例库列表
        :param request: Request instance for DescribeInstanceDatabases.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeInstanceDatabasesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceDatabases", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """修改数据库信息
        :param request: Request instance for ModifyInstanceDatabaseInfo.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceDatabaseInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabaseInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建慢日志导出任务
        :param request: Request instance for StartSlowLogDetailExportTask.
        :type request: :class:`ksyun.client.krds.v20160701.models.StartSlowLogDetailExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartSlowLogDetailExportTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """查询导出任务列表
        :param request: Request instance for ListSlowLogDetailExportTask.
        :type request: :class:`ksyun.client.krds.v20160701.models.ListSlowLogDetailExportTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSlowLogDetailExportTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """创建数据库账户(POST)
        :param request: Request instance for CreateInstanceAccountAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.CreateInstanceAccountActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateInstanceAccountAction", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """数据库账户赋权(POST)
        :param request: Request instance for ModifyInstanceAccountPrivilegesAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceAccountPrivilegesActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAccountPrivilegesAction", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """删除数据库账户(POST)
        :param request: Request instance for DeleteInstanceAccountAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteInstanceAccountActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstanceAccountAction", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """删除实例数据库(POST)
        :param request: Request instance for DeleteInstanceDatabaseAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.DeleteInstanceDatabaseActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteInstanceDatabaseAction", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """修改实例IP/VPC (POST)
        :param request: Request instance for ModifyDBNetwork.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBNetworkRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBNetwork", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDBInstanceMonitorPeriod(self, request):
        """查询实例监控周期
        :param request: Request instance for DescribeDBInstanceMonitorPeriod.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeDBInstanceMonitorPeriodRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDBInstanceMonitorPeriod", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyDBInstanceMonitorPeriod(self, request):
        """修改实例监控周期
        :param request: Request instance for ModifyDBInstanceMonitorPeriod.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyDBInstanceMonitorPeriodRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDBInstanceMonitorPeriod", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def BatchApplyDBParameterGroup(self, request):
        """批量应用参数组
        :param request: Request instance for BatchApplyDBParameterGroup.
        :type request: :class:`ksyun.client.krds.v20160701.models.BatchApplyDBParameterGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BatchApplyDBParameterGroup", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpgradeDBInstanceLatesVersion(self, request):
        """小版本升级(5.7.x)
        :param request: Request instance for UpgradeDBInstanceLatesVersion.
        :type request: :class:`ksyun.client.krds.v20160701.models.UpgradeDBInstanceLatesVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpgradeDBInstanceLatesVersion", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeProxyInstance(self, request):
        """查询代理实例详情
        :param request: Request instance for DescribeProxyInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeProxyInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeProxyInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def SetUpProxyInstance(self, request):
        """修改代理实例(只读权重/连接池设定)
        :param request: Request instance for SetUpProxyInstance.
        :type request: :class:`ksyun.client.krds.v20160701.models.SetUpProxyInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetUpProxyInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def TemporaryCloseSwitchover(self, request):
        """关闭主备切换(临时)
        :param request: Request instance for TemporaryCloseSwitchover.
        :type request: :class:`ksyun.client.krds.v20160701.models.TemporaryCloseSwitchoverRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("TemporaryCloseSwitchover", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeBackupOverview(self, request):
        """查询备份总概览(单地域)
        :param request: Request instance for DescribeBackupOverview.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeBackupOverviewRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeBackupOverview", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeStatisticBackupDetails(self, request):
        """查询备份总列表(单地域)
        :param request: Request instance for DescribeStatisticBackupDetails.
        :type request: :class:`ksyun.client.krds.v20160701.models.DescribeStatisticBackupDetailsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeStatisticBackupDetails", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyMaintenanceTime(self, request):
        """修改操作时间窗口
        :param request: Request instance for ModifyMaintenanceTime.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyMaintenanceTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyMaintenanceTime", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ModifyInstanceDatabasePrivilegesAction(self, request):
        """数据库授权(POST)
        :param request: Request instance for ModifyInstanceDatabasePrivilegesAction.
        :type request: :class:`ksyun.client.krds.v20160701.models.ModifyInstanceDatabasePrivilegesActionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceDatabasePrivilegesAction", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateDBInstanceOrder(self, request):
        """试用订单更新
        :param request: Request instance for UpdateDBInstanceOrder.
        :type request: :class:`ksyun.client.krds.v20160701.models.UpdateDBInstanceOrderRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDBInstanceOrder", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateResourceProtection(self, request):
        """删除保护设置
        :param request: Request instance for UpdateResourceProtection.
        :type request: :class:`ksyun.client.krds.v20160701.models.UpdateResourceProtectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateResourceProtection", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


