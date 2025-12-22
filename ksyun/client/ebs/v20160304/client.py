import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class EbsClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'ebs.api.ksyun.com'
    _service = 'ebs'
    def CreateVolume(self, request):
        """创建硬盘资源
        :param request: Request instance for CreateVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.CreateVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AttachVolume(self, request):
        """挂载云硬盘
        :param request: Request instance for AttachVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.AttachVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DetachVolume(self, request):
        """卸载云硬盘
        :param request: Request instance for DetachVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DetachVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteVolume(self, request):
        """删除云硬盘
        :param request: Request instance for DeleteVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DeleteVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ResizeVolume(self, request):
        """云盘扩容大小
        :param request: Request instance for ResizeVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ResizeVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResizeVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeVolumes(self, request):
        """DescribeVolumes查询硬盘列表
        :param request: Request instance for DescribeVolumes.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeVolumesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVolumes", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyVolume(self, request):
        """更新云硬盘属性
        :param request: Request instance for ModifyVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ModifyVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeEbsInstances(self, request):
        """查询可挂载云主机
        :param request: Request instance for DescribeEbsInstances.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeEbsInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEbsInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeInstanceVolumes(self, request):
        """查询云主机所挂载云硬盘
        :param request: Request instance for DescribeInstanceVolumes.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeInstanceVolumesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceVolumes", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RenewVolume(self, request):
        """续费云硬盘
        :param request: Request instance for RenewVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.RenewVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenewVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UpdateVolumeProject(self, request):
        """更新云硬盘项目组
        :param request: Request instance for UpdateVolumeProject.
        :type request: :class:`ksyun.client.ebs.v20160304.models.UpdateVolumeProjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateVolumeProject", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询快照信息
        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeSnapshotsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSnapshots", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateSnapshot(self, request):
        """基于云盘创建快照
        :param request: Request instance for CreateSnapshot.
        :type request: :class:`ksyun.client.ebs.v20160304.models.CreateSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSnapshot", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """删除快照数据
        :param request: Request instance for DeleteSnapshot.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DeleteSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSnapshot", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RollbackSnapshot(self, request):
        """RollbackSnapshot
        :param request: Request instance for RollbackSnapshot.
        :type request: :class:`ksyun.client.ebs.v20160304.models.RollbackSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RollbackSnapshot", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifySnapshot(self, request):
        """修改快照名称描述
        :param request: Request instance for ModifySnapshot.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ModifySnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySnapshot", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RecoveryVolume(self, request):
        """恢复云硬盘
        :param request: Request instance for RecoveryVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.RecoveryVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RecoveryVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ValidateAttachInstance(self, request):
        """校验挂载云主机可用性
        :param request: Request instance for ValidateAttachInstance.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ValidateAttachInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ValidateAttachInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询云硬盘可用区
        :param request: Request instance for DescribeAvailabilityZones.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeAvailabilityZonesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAvailabilityZones", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeCreateVolumePrice(self, request):
        """查询云盘新建时的价格
        :param request: Request instance for DescribeCreateVolumePrice.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeCreateVolumePriceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCreateVolumePrice", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifySnapshotType(self, request):
        """3.0快照类型转化成4.0快照
        :param request: Request instance for ModifySnapshotType.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ModifySnapshotTypeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySnapshotType", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyVolumeType(self, request):
        """SSD3.0/EHDD云盘变配ESSD云盘
        :param request: Request instance for ModifyVolumeType.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ModifyVolumeTypeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyVolumeType", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyDedicatedBlockStorageClusterAttribute(self, request):
        """修改专属块存储集群属性
        :param request: Request instance for ModifyDedicatedBlockStorageClusterAttribute.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ModifyDedicatedBlockStorageClusterAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDedicatedBlockStorageClusterAttribute", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ResizeDedicatedBlockStorageClusters(self, request):
        """专属集群扩容
        :param request: Request instance for ResizeDedicatedBlockStorageClusters.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ResizeDedicatedBlockStorageClustersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResizeDedicatedBlockStorageClusters", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeDedicatedBlockStorageClusters(self, request):
        """查询专属集群列表
        :param request: Request instance for DescribeDedicatedBlockStorageClusters.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeDedicatedBlockStorageClustersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDedicatedBlockStorageClusters", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateDedicatedBlockStorageCluster(self, request):
        """创建专属块存储集群
        :param request: Request instance for CreateDedicatedBlockStorageCluster.
        :type request: :class:`ksyun.client.ebs.v20160304.models.CreateDedicatedBlockStorageClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDedicatedBlockStorageCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyVolumePreset(self, request):
        """修改云盘预配置
        :param request: Request instance for ModifyVolumePreset.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ModifyVolumePresetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyVolumePreset", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetUpgradeVolumeTypeProcessInfo(self, request):
        """获取云盘转化进度
        :param request: Request instance for GetUpgradeVolumeTypeProcessInfo.
        :type request: :class:`ksyun.client.ebs.v20160304.models.GetUpgradeVolumeTypeProcessInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetUpgradeVolumeTypeProcessInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


