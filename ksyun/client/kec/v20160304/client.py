import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KecClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'kec.api.ksyun.com'
    _service = 'kec'
    def DescribeInstances(self, request):
        """描述实例信息
        :param request: Request instance for DescribeInstances.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RunInstances(self, request):
        """创建实例
        :param request: Request instance for RunInstances.
        :type request: :class:`ksyun.client.kec.v20160304.models.RunInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RunInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def StartInstances(self, request):
        """启动实例
        :param request: Request instance for StartInstances.
        :type request: :class:`ksyun.client.kec.v20160304.models.StartInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def StopInstances(self, request):
        """关闭实例
        :param request: Request instance for StopInstances.
        :type request: :class:`ksyun.client.kec.v20160304.models.StopInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RebootInstances(self, request):
        """重启实例
        :param request: Request instance for RebootInstances.
        :type request: :class:`ksyun.client.kec.v20160304.models.RebootInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RebootInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyInstanceAttribute(self, request):
        """修改实例属性信息
        :param request: Request instance for ModifyInstanceAttribute.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyInstanceAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAttribute", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyInstanceType(self, request):
        """升级实例套餐类型
        :param request: Request instance for ModifyInstanceType.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyInstanceTypeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceType", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def TerminateInstances(self, request):
        """销毁实例
        :param request: Request instance for TerminateInstances.
        :type request: :class:`ksyun.client.kec.v20160304.models.TerminateInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("TerminateInstances", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeImages(self, request):
        """描述镜像信息
        :param request: Request instance for DescribeImages.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeImagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImages", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyImageAttribute(self, request):
        """修改镜像属性信息
        :param request: Request instance for ModifyImageAttribute.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyImageAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyImageAttribute", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyInstanceImage(self, request):
        """更换或者重新安装实例操作系统
        :param request: Request instance for ModifyInstanceImage.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyInstanceImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceImage", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateImage(self, request):
        """创建镜像
        :param request: Request instance for CreateImage.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateImage", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RemoveImages(self, request):
        """删除镜像
        :param request: Request instance for RemoveImages.
        :type request: :class:`ksyun.client.kec.v20160304.models.RemoveImagesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RemoveImages", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyNetworkInterfaceAttribute(self, request):
        """修改网络接口
        :param request: Request instance for ModifyNetworkInterfaceAttribute.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyNetworkInterfaceAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNetworkInterfaceAttribute", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AttachNetworkInterface(self, request):
        """实例添加弹性网卡
        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`ksyun.client.kec.v20160304.models.AttachNetworkInterfaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachNetworkInterface", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DetachNetworkInterface(self, request):
        """实例卸载弹性网卡
        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`ksyun.client.kec.v20160304.models.DetachNetworkInterfaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachNetworkInterface", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeLocalVolumes(self, request):
        """查询本地盘信息
        :param request: Request instance for DescribeLocalVolumes.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeLocalVolumesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeLocalVolumes", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateLocalVolumeSnapshot(self, request):
        """创建本地盘快照
        :param request: Request instance for CreateLocalVolumeSnapshot.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateLocalVolumeSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateLocalVolumeSnapshot", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeLocalVolumeSnapshots(self, request):
        """描述本地盘快照信息
        :param request: Request instance for DescribeLocalVolumeSnapshots.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeLocalVolumeSnapshotsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeLocalVolumeSnapshots", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RollbackLocalVolume(self, request):
        """快照回滚本地盘
        :param request: Request instance for RollbackLocalVolume.
        :type request: :class:`ksyun.client.kec.v20160304.models.RollbackLocalVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RollbackLocalVolume", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteLocalVolumeSnapshot(self, request):
        """删除本地盘快照
        :param request: Request instance for DeleteLocalVolumeSnapshot.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteLocalVolumeSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteLocalVolumeSnapshot", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyDataGuardGroups(self, request):
        """修改容灾分组信息
        :param request: Request instance for ModifyDataGuardGroups.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyDataGuardGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDataGuardGroups", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeDataGuardCapacity(self, request):
        """查询用户区域容灾分组容量
        :param request: Request instance for DescribeDataGuardCapacity.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeDataGuardCapacityRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataGuardCapacity", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateDataGuardGroup(self, request):
        """创建容灾分组
        :param request: Request instance for CreateDataGuardGroup.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateDataGuardGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDataGuardGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteDataGuardGroups(self, request):
        """删除容灾分组
        :param request: Request instance for DeleteDataGuardGroups.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteDataGuardGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDataGuardGroups", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeDataGuardGroup(self, request):
        """描述容灾分组信息
        :param request: Request instance for DescribeDataGuardGroup.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeDataGuardGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataGuardGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def RemoveVmFromDataGuard(self, request):
        """容灾分组中移除实例
        :param request: Request instance for RemoveVmFromDataGuard.
        :type request: :class:`ksyun.client.kec.v20160304.models.RemoveVmFromDataGuardRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RemoveVmFromDataGuard", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateDedicatedHosts(self, request):
        """创建专属宿主机
        :param request: Request instance for CreateDedicatedHosts.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateDedicatedHostsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDedicatedHosts", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteDedicatedHost(self, request):
        """删除专属宿主机
        :param request: Request instance for DeleteDedicatedHost.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteDedicatedHostRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDedicatedHost", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeDedicatedHosts(self, request):
        """描述专属宿主机信息
        :param request: Request instance for DescribeDedicatedHosts.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeDedicatedHostsRequest`
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeScalingConfiguration(self, request):
        """查询启动配置
        :param request: Request instance for DescribeScalingConfiguration.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeScalingConfigurationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeScalingConfiguration", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateScalingConfiguration(self, request):
        """创建启动配置
        :param request: Request instance for CreateScalingConfiguration.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateScalingConfigurationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateScalingConfiguration", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteScalingConfiguration(self, request):
        """删除启动配置
        :param request: Request instance for DeleteScalingConfiguration.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteScalingConfigurationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteScalingConfiguration", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateScalingGroup(self, request):
        """创建伸缩组接口
        :param request: Request instance for CreateScalingGroup.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateScalingGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateScalingGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeScalingGroup(self, request):
        """查询伸缩组列表接口
        :param request: Request instance for DescribeScalingGroup.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeScalingGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeScalingGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyScalingGroup(self, request):
        """修改伸缩组接口
        :param request: Request instance for ModifyScalingGroup.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyScalingGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyScalingGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def SetKvmProtectedDetach(self, request):
        """设置子机移除保护
        :param request: Request instance for SetKvmProtectedDetach.
        :type request: :class:`ksyun.client.kec.v20160304.models.SetKvmProtectedDetachRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetKvmProtectedDetach", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeScalingInstance(self, request):
        """查询伸缩组绑定的云服务器
        :param request: Request instance for DescribeScalingInstance.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeScalingInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeScalingInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AttachInstance(self, request):
        """绑定伸缩组云服务器
        :param request: Request instance for AttachInstance.
        :type request: :class:`ksyun.client.kec.v20160304.models.AttachInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DetachInstance(self, request):
        """解绑伸缩组云服务器
        :param request: Request instance for DetachInstance.
        :type request: :class:`ksyun.client.kec.v20160304.models.DetachInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeScalingActivity(self, request):
        """查询伸缩活动
        :param request: Request instance for DescribeScalingActivity.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeScalingActivityRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeScalingActivity", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteScalingGroup(self, request):
        """删除伸缩组
        :param request: Request instance for DeleteScalingGroup.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteScalingGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteScalingGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DisableScalingGroup(self, request):
        """停用伸缩组
        :param request: Request instance for DisableScalingGroup.
        :type request: :class:`ksyun.client.kec.v20160304.models.DisableScalingGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisableScalingGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def EnableScalingGroup(self, request):
        """启用伸缩组
        :param request: Request instance for EnableScalingGroup.
        :type request: :class:`ksyun.client.kec.v20160304.models.EnableScalingGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableScalingGroup", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeScalingNotification(self, request):
        """查询通知
        :param request: Request instance for DescribeScalingNotification.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeScalingNotificationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeScalingNotification", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateScalingNotification(self, request):
        """创建通知
        :param request: Request instance for CreateScalingNotification.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateScalingNotificationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateScalingNotification", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyScalingNotification(self, request):
        """修改通知
        :param request: Request instance for ModifyScalingNotification.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyScalingNotificationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyScalingNotification", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateScheduledTask(self, request):
        """创建定时任务
        :param request: Request instance for CreateScheduledTask.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateScheduledTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateScheduledTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeScheduledTask(self, request):
        """查询定时任务
        :param request: Request instance for DescribeScheduledTask.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeScheduledTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeScheduledTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyScheduledTask(self, request):
        """修改定时任务
        :param request: Request instance for ModifyScheduledTask.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyScheduledTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyScheduledTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteScheduledTask(self, request):
        """删除定时任务
        :param request: Request instance for DeleteScheduledTask.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteScheduledTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteScheduledTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateScalingPolicy(self, request):
        """创建告警触发策略
        :param request: Request instance for CreateScalingPolicy.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateScalingPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateScalingPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeScalingPolicy(self, request):
        """查询告警触发策略
        :param request: Request instance for DescribeScalingPolicy.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeScalingPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeScalingPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyScalingPolicy(self, request):
        """修改告警触发策略
        :param request: Request instance for ModifyScalingPolicy.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyScalingPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyScalingPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteScalingPolicy(self, request):
        """删除告警触发策略
        :param request: Request instance for DeleteScalingPolicy.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteScalingPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteScalingPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ImportImage(self, request):
        """镜像导入
        :param request: Request instance for ImportImage.
        :type request: :class:`ksyun.client.kec.v20160304.models.ImportImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ImportImage", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CopyImage(self, request):
        """镜像复制
        :param request: Request instance for CopyImage.
        :type request: :class:`ksyun.client.kec.v20160304.models.CopyImageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CopyImage", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyImageSharePermission(self, request):
        """镜像共享，取消共享接口
        :param request: Request instance for ModifyImageSharePermission.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyImageSharePermissionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyImageSharePermission", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeImageSharePermission(self, request):
        """镜像共享的账户列表
        :param request: Request instance for DescribeImageSharePermission.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeImageSharePermissionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeImageSharePermission", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """用户有权限机房
        :param request: Request instance for DescribeRegions.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeRegionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRegions", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AttachKey(self, request):
        """主机绑定密钥
        :param request: Request instance for AttachKey.
        :type request: :class:`ksyun.client.kec.v20160304.models.AttachKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachKey", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DetachKey(self, request):
        """主机解绑密钥
        :param request: Request instance for DetachKey.
        :type request: :class:`ksyun.client.kec.v20160304.models.DetachKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachKey", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """查询可用区列表
        :param request: Request instance for DescribeAvailabilityZones.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeAvailabilityZonesRequest`
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


    def DescribeInstanceTypeConfigs(self, request):
        """查询机型套餐配置信息
        :param request: Request instance for DescribeInstanceTypeConfigs.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeInstanceTypeConfigsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceTypeConfigs", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeInstanceFamilys(self, request):
        """查询机型配置信息
        :param request: Request instance for DescribeInstanceFamilys.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeInstanceFamilysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceFamilys", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddVmIntoDataGuard(self, request):
        """存量虚机迁入容灾分组
        :param request: Request instance for AddVmIntoDataGuard.
        :type request: :class:`ksyun.client.kec.v20160304.models.AddVmIntoDataGuardRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddVmIntoDataGuard", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateFileSystem(self, request):
        """创建一个新的文件系统
        :param request: Request instance for CreateFileSystem.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateFileSystemRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateFileSystem", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteFileSystem(self, request):
        """删除文件系统信息
        :param request: Request instance for DeleteFileSystem.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteFileSystemRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteFileSystem", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeFileSystems(self, request):
        """查询文件系统信息
        :param request: Request instance for DescribeFileSystems.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeFileSystemsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFileSystems", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyFileSystem(self, request):
        """修改文件系统（名称）
        :param request: Request instance for ModifyFileSystem.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyFileSystemRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyFileSystem", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateMountTarget(self, request):
        """创建文件系统挂载点
        :param request: Request instance for CreateMountTarget.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateMountTargetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateMountTarget", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteMountTarget(self, request):
        """删除文件系统挂载点
        :param request: Request instance for DeleteMountTarget.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteMountTargetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteMountTarget", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeMountTargets(self, request):
        """查询挂载点信息
        :param request: Request instance for DescribeMountTargets.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeMountTargetsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMountTargets", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateModel(self, request):
        """创建实例启动模版
        :param request: Request instance for CreateModel.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateModelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateModel", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def TerminateModels(self, request):
        """删除实例启动模版
        :param request: Request instance for TerminateModels.
        :type request: :class:`ksyun.client.kec.v20160304.models.TerminateModelsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("TerminateModels", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeModels(self, request):
        """查询实例启动模版
        :param request: Request instance for DescribeModels.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeModelsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeModels", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeDedicatedCluster(self, request):
        """描述专属集群信息
        :param request: Request instance for DescribeDedicatedCluster.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeDedicatedClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDedicatedCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CreateDedicatedCluster(self, request):
        """创建集群
        :param request: Request instance for CreateDedicatedCluster.
        :type request: :class:`ksyun.client.kec.v20160304.models.CreateDedicatedClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDedicatedCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteDedicatedCluster(self, request):
        """删除集群
        :param request: Request instance for DeleteDedicatedCluster.
        :type request: :class:`ksyun.client.kec.v20160304.models.DeleteDedicatedClusterRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDedicatedCluster", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def SetvCPU(self, request):
        """专属宿主机设置虚拟核数
        :param request: Request instance for SetvCPU.
        :type request: :class:`ksyun.client.kec.v20160304.models.SetvCPURequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetvCPU", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DedicatedHostMigrate(self, request):
        """宿主机迁移集群
        :param request: Request instance for DedicatedHostMigrate.
        :type request: :class:`ksyun.client.kec.v20160304.models.DedicatedHostMigrateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DedicatedHostMigrate", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyDedicatedClusterName(self, request):
        """修改专属集群名称
        :param request: Request instance for ModifyDedicatedClusterName.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyDedicatedClusterNameRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDedicatedClusterName", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def InstanceMigrate(self, request):
        """专属虚机迁移
        :param request: Request instance for InstanceMigrate.
        :type request: :class:`ksyun.client.kec.v20160304.models.InstanceMigrateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("InstanceMigrate", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyInstanceAutoDeleteTime(self, request):
        """实例定时删除
        :param request: Request instance for ModifyInstanceAutoDeleteTime.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyInstanceAutoDeleteTimeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyInstanceAutoDeleteTime", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyScalingConfiguration(self, request):
        """修改启动配置
        :param request: Request instance for ModifyScalingConfiguration.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyScalingConfigurationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyScalingConfiguration", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeSpotPriceHistory(self, request):
        """DescribeSpotPriceHistory
        :param request: Request instance for DescribeSpotPriceHistory.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribeSpotPriceHistoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSpotPriceHistory", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribePrice(self, request):
        """查询价格
        :param request: Request instance for DescribePrice.
        :type request: :class:`ksyun.client.kec.v20160304.models.DescribePriceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePrice", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def EnableImageCaching(self, request):
        """自定义镜像预热
        :param request: Request instance for EnableImageCaching.
        :type request: :class:`ksyun.client.kec.v20160304.models.EnableImageCachingRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableImageCaching", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DisableImageCaching(self, request):
        """取消自定义镜像预热
        :param request: Request instance for DisableImageCaching.
        :type request: :class:`ksyun.client.kec.v20160304.models.DisableImageCachingRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisableImageCaching", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyLoadBalancers(self, request):
        """ModifyLoadBalancers
        :param request: Request instance for ModifyLoadBalancers.
        :type request: :class:`ksyun.client.kec.v20160304.models.ModifyLoadBalancersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyLoadBalancers", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AttachInstancesIamRole(self, request):
        """实例绑定IAM角色
        :param request: Request instance for AttachInstancesIamRole.
        :type request: :class:`ksyun.client.kec.v20160304.models.AttachInstancesIamRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachInstancesIamRole", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DetachInstancesIamRole(self, request):
        """实例解除绑定IAM角色
        :param request: Request instance for DetachInstancesIamRole.
        :type request: :class:`ksyun.client.kec.v20160304.models.DetachInstancesIamRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachInstancesIamRole", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CopySnapshot(self, request):
        """本地盘快照跨region复制
        :param request: Request instance for CopySnapshot.
        :type request: :class:`ksyun.client.kec.v20160304.models.CopySnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CopySnapshot", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def PreMigrateInstance(self, request):
        """创建预迁移
        :param request: Request instance for PreMigrateInstance.
        :type request: :class:`ksyun.client.kec.v20160304.models.PreMigrateInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("PreMigrateInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def CancelPreMigrateInstance(self, request):
        """取消预迁移
        :param request: Request instance for CancelPreMigrateInstance.
        :type request: :class:`ksyun.client.kec.v20160304.models.CancelPreMigrateInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CancelPreMigrateInstance", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetVNCAddress(self, request):
        """OpenAPI获取浏览器可用的VNC地址
        :param request: Request instance for GetVNCAddress.
        :type request: :class:`ksyun.client.kec.v20160304.models.GetVNCAddressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetVNCAddress", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


