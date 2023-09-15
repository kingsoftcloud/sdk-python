import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KetClient(AbstractClient):
    _apiVersion = '2017-01-01'
    _endpoint = 'ket.api.ksyun.com'
    _service = 'ket'
    def Preset(self, request):
        """add preset
        :param request: Request instance for Preset.
        :type request: :class:`ksyun.client.ket.v20170101.models.PresetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Preset", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def UpdatePreset(self, request):
        """update preset
        :param request: Request instance for UpdatePreset.
        :type request: :class:`ksyun.client.ket.v20170101.models.UpdatePresetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdatePreset", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def DelPreset(self, request):
        """delete preset
        :param request: Request instance for DelPreset.
        :type request: :class:`ksyun.client.ket.v20170101.models.DelPresetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DelPreset", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetPresetList(self, request):
        """get preset list
        :param request: Request instance for GetPresetList.
        :type request: :class:`ksyun.client.ket.v20170101.models.GetPresetListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetPresetList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetPresetDetail(self, request):
        """get preset detail
        :param request: Request instance for GetPresetDetail.
        :type request: :class:`ksyun.client.ket.v20170101.models.GetPresetDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetPresetDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


    def GetStreamTranList(self, request):
        """get stream tran list
        :param request: Request instance for GetStreamTranList.
        :type request: :class:`ksyun.client.ket.v20170101.models.GetStreamTranListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetStreamTranList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


