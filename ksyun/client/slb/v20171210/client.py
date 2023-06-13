import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class SlbClient(AbstractClient):
    _apiVersion = '2017-12-10'
    _endpoint = 'slb.api.ksyun.com'
    _service = 'slb'
    def DescribeLoadBalancers(self, request):
        """获取应用型负载均衡
        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`ksyun.client.slb.v20171210.models.DescribeLoadBalancersRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(e.message, e.message)


