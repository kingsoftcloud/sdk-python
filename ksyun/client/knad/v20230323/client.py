import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KnadClient(AbstractClient):
    _apiVersion = '2023-03-23'
    _endpoint = 'knad.api.ksyun.com'
    _service = 'knad'
    def CreateKnad(self, request):
        """创建原生高防
        :param request: Request instance for CreateKnad.
        :type request: :class:`ksyun.client.knad.v20230323.models.CreateKnadRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateKnad", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyKnad(self, request):
        """调整防护能力
        :param request: Request instance for ModifyKnad.
        :type request: :class:`ksyun.client.knad.v20230323.models.ModifyKnadRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyKnad", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UnbindIpList(self, request):
        """设置防护对象-可选eip列表
        :param request: Request instance for UnbindIpList.
        :type request: :class:`ksyun.client.knad.v20230323.models.UnbindIpListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnbindIpList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AssociateIp(self, request):
        """绑定eip
        :param request: Request instance for AssociateIp.
        :type request: :class:`ksyun.client.knad.v20230323.models.AssociateIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateIp", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DisassociateIp(self, request):
        """解绑eip
        :param request: Request instance for DisassociateIp.
        :type request: :class:`ksyun.client.knad.v20230323.models.DisassociateIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisassociateIp", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeKnadIp(self, request):
        """已绑定eip列表
        :param request: Request instance for DescribeKnadIp.
        :type request: :class:`ksyun.client.knad.v20230323.models.DescribeKnadIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKnadIp", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteKnad(self, request):
        """退订高防实例(已绑弹性IP的高防实例无法退订)
        :param request: Request instance for DeleteKnad.
        :type request: :class:`ksyun.client.knad.v20230323.models.DeleteKnadRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteKnad", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DescribeKnad(self, request):
        """高防包列表
        :param request: Request instance for DescribeKnad.
        :type request: :class:`ksyun.client.knad.v20230323.models.DescribeKnadRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKnad", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetBWIpList(self, request):
        """获取实例的黑白名单列表
        :param request: Request instance for GetBWIpList.
        :type request: :class:`ksyun.client.knad.v20230323.models.GetBWIpListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetBWIpList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DeleteBW(self, request):
        """删除黑白名单
        :param request: Request instance for DeleteBW.
        :type request: :class:`ksyun.client.knad.v20230323.models.DeleteBWRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteBW", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def AddBWIpList(self, request):
        """添加黑白名单
        :param request: Request instance for AddBWIpList.
        :type request: :class:`ksyun.client.knad.v20230323.models.AddBWIpListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddBWIpList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetZoneList(self, request):
        """获取地理位置列表
        :param request: Request instance for GetZoneList.
        :type request: :class:`ksyun.client.knad.v20230323.models.GetZoneListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetZoneList", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyPolicy(self, request):
        """修改防护策略
        :param request: Request instance for ModifyPolicy.
        :type request: :class:`ksyun.client.knad.v20230323.models.ModifyPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyPolicy", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def ModifyBlockLocation(self, request):
        """设置封禁地域
        :param request: Request instance for ModifyBlockLocation.
        :type request: :class:`ksyun.client.knad.v20230323.models.ModifyBlockLocationRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyBlockLocation", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetBlockLocations(self, request):
        """获取封禁区域
        :param request: Request instance for GetBlockLocations.
        :type request: :class:`ksyun.client.knad.v20230323.models.GetBlockLocationsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetBlockLocations", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetKnadPolicy(self, request):
        """获取实例的防护模板信息
        :param request: Request instance for GetKnadPolicy.
        :type request: :class:`ksyun.client.knad.v20230323.models.GetKnadPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetKnadPolicy", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def InsertEips(self, request):
        """增量绑定eip
        :param request: Request instance for InsertEips.
        :type request: :class:`ksyun.client.knad.v20230323.models.InsertEipsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("InsertEips", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


