import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KpfsClient(AbstractClient):
    _apiVersion = '2024-09-30'
    _endpoint = 'kpfs.api.ksyun.com'
    _service = 'kpfs'
    def DescribeFileSystemList(self, request):
        """查询文件系统列表
        :param request: Request instance for DescribeFileSystemList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeFileSystemListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFileSystemList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetTotalSize(self, request):
        """当前文件系统中的容量使用数量
        :param request: Request instance for GetTotalSize.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetTotalSizeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetTotalSize", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetInodeCount(self, request):
        """当前文件系统中的inode数量
        :param request: Request instance for GetInodeCount.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetInodeCountRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetInodeCount", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeFileSystemClientInfo(self, request):
        """查询文件系统POSIX客户端信息
        :param request: Request instance for DescribeFileSystemClientInfo.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeFileSystemClientInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFileSystemClientInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeFileSystemFileList(self, request):
        """查询文件系统文件列表
        :param request: Request instance for DescribeFileSystemFileList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeFileSystemFileListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFileSystemFileList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RenewFileSystem(self, request):
        """文件系统续费
        :param request: Request instance for RenewFileSystem.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.RenewFileSystemRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RenewFileSystem", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpgradeFileSystem(self, request):
        """文件系统扩容
        :param request: Request instance for UpgradeFileSystem.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpgradeFileSystemRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpgradeFileSystem", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateFileSystem(self, request):
        """文件系统创建
        :param request: Request instance for CreateFileSystem.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateFileSystemRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateFileSystem", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetCapacityAvailable(self, request):
        """文件系统可用容量
        :param request: Request instance for GetCapacityAvailable.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetCapacityAvailableRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetCapacityAvailable", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetCapacityTotal(self, request):
        """文件系统总容量
        :param request: Request instance for GetCapacityTotal.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetCapacityTotalRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetCapacityTotal", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetLatencyWrite(self, request):
        """客户端级写延迟
        :param request: Request instance for GetLatencyWrite.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetLatencyWriteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetLatencyWrite", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetLatencyRead(self, request):
        """性能型客户端级读延迟
        :param request: Request instance for GetLatencyRead.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetLatencyReadRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetLatencyRead", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetIopsWrite(self, request):
        """写IOPS
        :param request: Request instance for GetIopsWrite.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetIopsWriteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetIopsWrite", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetIopsRead(self, request):
        """读IOPS
        :param request: Request instance for GetIopsRead.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetIopsReadRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetIopsRead", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetBandwidthWrite(self, request):
        """文件系统统计查询_性能型写带宽
        :param request: Request instance for GetBandwidthWrite.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetBandwidthWriteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetBandwidthWrite", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetBandwidthRead(self, request):
        """文件系统统计查询_性能型读带宽
        :param request: Request instance for GetBandwidthRead.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetBandwidthReadRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetBandwidthRead", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeletePerformanceOnePosixAcl(self, request):
        """删除POSIX协议访问授权
        :param request: Request instance for DeletePerformanceOnePosixAcl.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeletePerformanceOnePosixAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeletePerformanceOnePosixAcl", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdatePerformanceOnePosixAcl(self, request):
        """修改POSIX协议访问授权
        :param request: Request instance for UpdatePerformanceOnePosixAcl.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdatePerformanceOnePosixAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdatePerformanceOnePosixAcl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribePerformanceOnePosixAclList(self, request):
        """查询POSIX协议访问授权列表
        :param request: Request instance for DescribePerformanceOnePosixAclList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribePerformanceOnePosixAclListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePerformanceOnePosixAclList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def SetPerformanceOnePosixAcl(self, request):
        """新建POSIX协议访问授权
        :param request: Request instance for SetPerformanceOnePosixAcl.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.SetPerformanceOnePosixAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetPerformanceOnePosixAcl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDirQuotaList(self, request):
        """查询目录配额列表
        :param request: Request instance for DescribeDirQuotaList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDirQuotaListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDirQuotaList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteDirQuota(self, request):
        """删除目录配额
        :param request: Request instance for DeleteDirQuota.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteDirQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDirQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateDirQuota(self, request):
        """修改目录配额
        :param request: Request instance for UpdateDirQuota.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdateDirQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDirQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateDirQuota(self, request):
        """新建目录配额
        :param request: Request instance for CreateDirQuota.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateDirQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDirQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeSubDirList(self, request):
        """查询文件系统目录列表
        :param request: Request instance for DescribeSubDirList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeSubDirListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSubDirList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteDir(self, request):
        """删除文件系统目录
        :param request: Request instance for DeleteDir.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteDirRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDir", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateDir(self, request):
        """修改文件系统目录
        :param request: Request instance for UpdateDir.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdateDirRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDir", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateDir(self, request):
        """新建文件系统目录
        :param request: Request instance for CreateDir.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateDirRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDir", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDirQuota(self, request):
        """查询指定目录配额
        :param request: Request instance for DescribeDirQuota.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDirQuotaRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDirQuota", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteFileSystem(self, request):
        """删除文件系统
        :param request: Request instance for DeleteFileSystem.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteFileSystemRequest`
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
                raise KsyunSDKException(message=str(e))


    def AddPerformanceOnePosixAclIp(self, request):
        """添加POSIX协议访问授权IP
        :param request: Request instance for AddPerformanceOnePosixAclIp.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.AddPerformanceOnePosixAclIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddPerformanceOnePosixAclIp", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RemovePerformanceOnePosixAclIp(self, request):
        """移除POSIX协议访问授权IP
        :param request: Request instance for RemovePerformanceOnePosixAclIp.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.RemovePerformanceOnePosixAclIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RemovePerformanceOnePosixAclIp", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetDataMigrateTaskProgress(self, request):
        """获取数据流转任务进度
        :param request: Request instance for GetDataMigrateTaskProgress.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetDataMigrateTaskProgressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDataMigrateTaskProgress", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDataMigrateTaskList(self, request):
        """获取数据流转任务列表
        :param request: Request instance for DescribeDataMigrateTaskList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDataMigrateTaskListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataMigrateTaskList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def StartDataMigrateTask(self, request):
        """启动数据流转任务
        :param request: Request instance for StartDataMigrateTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.StartDataMigrateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StartDataMigrateTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def StopDataMigrateTask(self, request):
        """停止数据流转任务
        :param request: Request instance for StopDataMigrateTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.StopDataMigrateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StopDataMigrateTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteDataMigrateTask(self, request):
        """删除数据流转任务
        :param request: Request instance for DeleteDataMigrateTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteDataMigrateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDataMigrateTask", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateDataMigrateTask(self, request):
        """修改数据流转任务
        :param request: Request instance for UpdateDataMigrateTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdateDataMigrateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateDataMigrateTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateDataMigrateTask(self, request):
        """创建数据流转任务
        :param request: Request instance for CreateDataMigrateTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateDataMigrateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDataMigrateTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeClientInstallInfo(self, request):
        """查询文件系统POSIX客户端安装包信息
        :param request: Request instance for DescribeClientInstallInfo.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeClientInstallInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeClientInstallInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ManageDataFlowTask(self, request):
        """变更数据流动任务
        :param request: Request instance for ManageDataFlowTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.ManageDataFlowTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ManageDataFlowTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateDataFlowStrategy(self, request):
        """创建数据流动策略
        :param request: Request instance for CreateDataFlowStrategy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateDataFlowStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDataFlowStrategy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDataFlowTaskList(self, request):
        """查看数据流动任务
        :param request: Request instance for DescribeDataFlowTaskList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDataFlowTaskListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataFlowTaskList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ActivateDataFlowTask(self, request):
        """启动数据流动导入任务
        :param request: Request instance for ActivateDataFlowTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.ActivateDataFlowTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ActivateDataFlowTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteDataFlowStrategy(self, request):
        """删除数据流动策略
        :param request: Request instance for DeleteDataFlowStrategy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteDataFlowStrategyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDataFlowStrategy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDataFlowStrategyList(self, request):
        """创建数据流动列表
        :param request: Request instance for DescribeDataFlowStrategyList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDataFlowStrategyListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataFlowStrategyList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CleanRecycledFiles(self, request):
        """清空回收站数据
        :param request: Request instance for CleanRecycledFiles.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CleanRecycledFilesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CleanRecycledFiles", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteCleanRecycledFiles(self, request):
        """清空回收站文件
        :param request: Request instance for DeleteCleanRecycledFiles.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteCleanRecycledFilesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCleanRecycledFiles", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteRecycleBinConfig(self, request):
        """删除回收站配置
        :param request: Request instance for DeleteRecycleBinConfig.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteRecycleBinConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRecycleBinConfig", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteRecycledFileList(self, request):
        """删除回收站配置
        :param request: Request instance for DeleteRecycledFileList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteRecycledFileListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRecycledFileList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetRecycleBinConfig(self, request):
        """获取回收站配置
        :param request: Request instance for GetRecycleBinConfig.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetRecycleBinConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRecycleBinConfig", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def SetRecycleBinConfig(self, request):
        """设置回收站配置
        :param request: Request instance for SetRecycleBinConfig.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.SetRecycleBinConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetRecycleBinConfig", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeRecycledFileList(self, request):
        """查看回收站中文件
        :param request: Request instance for DescribeRecycledFileList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeRecycledFileListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRecycledFileList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteRecycledFiles(self, request):
        """删除回收站中文件
        :param request: Request instance for DeleteRecycledFiles.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteRecycledFilesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRecycledFiles", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RestoreRecycledFiles(self, request):
        """恢复回收站中文件
        :param request: Request instance for RestoreRecycledFiles.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.RestoreRecycledFilesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RestoreRecycledFiles", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeClusterInfo(self, request):
        """查询可用存储集群信息
        :param request: Request instance for DescribeClusterInfo.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeClusterInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeClusterInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdatePerformanceNfsAclIp(self, request):
        """编辑NFS访问授权客户端
        :param request: Request instance for UpdatePerformanceNfsAclIp.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdatePerformanceNfsAclIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdatePerformanceNfsAclIp", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def RemovePerformanceNfsAclClient(self, request):
        """删除NFS访问授权客户端
        :param request: Request instance for RemovePerformanceNfsAclClient.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.RemovePerformanceNfsAclClientRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RemovePerformanceNfsAclClient", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def AddPerformanceNfsAclClient(self, request):
        """添加NFS访问授权客户端
        :param request: Request instance for AddPerformanceNfsAclClient.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.AddPerformanceNfsAclClientRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddPerformanceNfsAclClient", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeletePerformanceOneNfsAcl(self, request):
        """删除NFS协议访问授权
        :param request: Request instance for DeletePerformanceOneNfsAcl.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeletePerformanceOneNfsAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeletePerformanceOneNfsAcl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def SetPerformanceOneNfsAcl(self, request):
        """新建NFS协议访问授权
        :param request: Request instance for SetPerformanceOneNfsAcl.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.SetPerformanceOneNfsAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetPerformanceOneNfsAcl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribePerformanceOneNfsAclList(self, request):
        """查询NFS协议访问授权
        :param request: Request instance for DescribePerformanceOneNfsAclList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribePerformanceOneNfsAclListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribePerformanceOneNfsAclList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeFileSystemNfsClientInfo(self, request):
        """查询特定文件系统的NFS客户端信息
        :param request: Request instance for DescribeFileSystemNfsClientInfo.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeFileSystemNfsClientInfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFileSystemNfsClientInfo", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def SetFileSystemResourceProtect(self, request):
        """设置文件系统删除保护
        :param request: Request instance for SetFileSystemResourceProtect.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.SetFileSystemResourceProtectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetFileSystemResourceProtect", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeFileDeletePolicyList(self, request):
        """查看列表-删除策略
        :param request: Request instance for DescribeFileDeletePolicyList.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeFileDeletePolicyListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFileDeletePolicyList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def EnableFileDeletePolicy(self, request):
        """启用-删除策略
        :param request: Request instance for EnableFileDeletePolicy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.EnableFileDeletePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("EnableFileDeletePolicy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DisableFileDeletePolicy(self, request):
        """禁用-删除策略
        :param request: Request instance for DisableFileDeletePolicy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DisableFileDeletePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisableFileDeletePolicy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeFileDeletePolicy(self, request):
        """查看-删除策略详情
        :param request: Request instance for DescribeFileDeletePolicy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeFileDeletePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeFileDeletePolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteFileDeletePolicy(self, request):
        """删除-删除策略
        :param request: Request instance for DeleteFileDeletePolicy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteFileDeletePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteFileDeletePolicy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def UpdateFileDeletePolicy(self, request):
        """修改删除策略
        :param request: Request instance for UpdateFileDeletePolicy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.UpdateFileDeletePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateFileDeletePolicy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateFileDeletePolicy(self, request):
        """新建-删除策略
        :param request: Request instance for CreateFileDeletePolicy.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateFileDeletePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateFileDeletePolicy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDataFlowStrategySubscribe(self, request):
        """查看数据流动订阅记录
        :param request: Request instance for DescribeDataFlowStrategySubscribe.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDataFlowStrategySubscribeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataFlowStrategySubscribe", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ManageDataFlowStrategySubscribe(self, request):
        """管理数据流动订阅
        :param request: Request instance for ManageDataFlowStrategySubscribe.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.ManageDataFlowStrategySubscribeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ManageDataFlowStrategySubscribe", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetRemoteCachePutLatency(self, request):
        """分布式缓存组的分布式缓存发送数据延迟
        :param request: Request instance for GetRemoteCachePutLatency.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetRemoteCachePutLatencyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRemoteCachePutLatency", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetRemoteCacheGetLatency(self, request):
        """分布式缓存组的分布式缓存读数据延迟
        :param request: Request instance for GetRemoteCacheGetLatency.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetRemoteCacheGetLatencyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRemoteCacheGetLatency", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetRemoteCachePutThroughput(self, request):
        """分布式缓存组的分布式缓存发送数据吞吐
        :param request: Request instance for GetRemoteCachePutThroughput.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetRemoteCachePutThroughputRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRemoteCachePutThroughput", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetRemoteCacheGetThroughput(self, request):
        """分布式缓存组的分布式缓存读数据吞吐量
        :param request: Request instance for GetRemoteCacheGetThroughput.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetRemoteCacheGetThroughputRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRemoteCacheGetThroughput", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetRemoteCacheIOPSSend(self, request):
        """分布式缓存组的分布式缓存发送数据请求数
        :param request: Request instance for GetRemoteCacheIOPSSend.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetRemoteCacheIOPSSendRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRemoteCacheIOPSSend", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def GetRemoteCacheIOPSGet(self, request):
        """分布式缓存组的分布式缓存读数据请求数
        :param request: Request instance for GetRemoteCacheIOPSGet.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.GetRemoteCacheIOPSGetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetRemoteCacheIOPSGet", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeDataFlowStrategySubscribeFailed(self, request):
        """查看数据流动订阅失败事件
        :param request: Request instance for DescribeDataFlowStrategySubscribeFailed.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeDataFlowStrategySubscribeFailedRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDataFlowStrategySubscribeFailed", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def ManageMigrateTask(self, request):
        """管理迁移任务
        :param request: Request instance for ManageMigrateTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.ManageMigrateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ManageMigrateTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeMigrateTasks(self, request):
        """查询迁移任务列表
        :param request: Request instance for DescribeMigrateTasks.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeMigrateTasksRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMigrateTasks", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateMigrateTask(self, request):
        """创建迁移任务
        :param request: Request instance for CreateMigrateTask.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateMigrateTaskRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateMigrateTask", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DeleteMigrateRule(self, request):
        """删除迁移规则
        :param request: Request instance for DeleteMigrateRule.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DeleteMigrateRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteMigrateRule", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def DescribeMigrateRules(self, request):
        """查询迁移规则列表
        :param request: Request instance for DescribeMigrateRules.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.DescribeMigrateRulesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMigrateRules", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CreateMigrateRule(self, request):
        """创建迁移规则
        :param request: Request instance for CreateMigrateRule.
        :type request: :class:`ksyun.client.kpfs.v20240930.models.CreateMigrateRuleRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateMigrateRule", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


