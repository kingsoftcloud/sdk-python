import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class EbsClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'ebs.api.ksyun.com'
    _service = 'ebs'
    def CreateVolume(self, request):
        """CreateVolume
        :param request: Request instance for CreateVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.CreateVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateVolume", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """AttachVolume
        :param request: Request instance for AttachVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.AttachVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachVolume", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DetachVolume
        :param request: Request instance for DetachVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DetachVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachVolume", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DeleteVolume
        :param request: Request instance for DeleteVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DeleteVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteVolume", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """ResizeVolume
        :param request: Request instance for ResizeVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ResizeVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ResizeVolume", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DescribeVolumes
        :param request: Request instance for DescribeVolumes.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeVolumesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVolumes", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """ModifyVolume
        :param request: Request instance for ModifyVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ModifyVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyVolume", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DescribeEbsInstances
        :param request: Request instance for DescribeEbsInstances.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeEbsInstancesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeEbsInstances", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DescribeInstanceVolumes
        :param request: Request instance for DescribeInstanceVolumes.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeInstanceVolumesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInstanceVolumes", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """RenewVolume
        :param request: Request instance for RenewVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.RenewVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenewVolume", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """UpdateVolumeProject
        :param request: Request instance for UpdateVolumeProject.
        :type request: :class:`ksyun.client.ebs.v20160304.models.UpdateVolumeProjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateVolumeProject", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DescribeSnapshots
        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DescribeSnapshotsRequest`
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


    def CreateSnapshot(self, request):
        """CreateSnapshot
        :param request: Request instance for CreateSnapshot.
        :type request: :class:`ksyun.client.ebs.v20160304.models.CreateSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """DeleteSnapshot
        :param request: Request instance for DeleteSnapshot.
        :type request: :class:`ksyun.client.ebs.v20160304.models.DeleteSnapshotRequest`
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


    def RollbackSnapshot(self, request):
        """RollbackSnapshot
        :param request: Request instance for RollbackSnapshot.
        :type request: :class:`ksyun.client.ebs.v20160304.models.RollbackSnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RollbackSnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """ModifySnapshot
        :param request: Request instance for ModifySnapshot.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ModifySnapshotRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySnapshot", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """RecoveryVolume
        :param request: Request instance for RecoveryVolume.
        :type request: :class:`ksyun.client.ebs.v20160304.models.RecoveryVolumeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RecoveryVolume", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
        """ValidateAttachInstance
        :param request: Request instance for ValidateAttachInstance.
        :type request: :class:`ksyun.client.ebs.v20160304.models.ValidateAttachInstanceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ValidateAttachInstance", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
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
            body = self.call_judge("DescribeCreateVolumePrice", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


