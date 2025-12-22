from ksyun.common.abstract_model import AbstractModel

class DescribeCfwAvRequest(AbstractModel):
    """DescribeCfwAv请求参数结构体
    """

    def __init__(self):
        r"""查询防病毒
        """

    def _deserialize(self, params):
        return


class DeleteBatchCfwAddrbookRequest(AbstractModel):
    """DeleteBatchCfwAddrbook请求参数结构体
    """

    def __init__(self):
        r"""批量删除地址簿
        :param AddrbookIds: 要删除的地址簿ID列表，单次删除数量不能超过1000条
        :type PathPrefix: Array
        :param CfwInstanceId: 防火墙实例ID
        :type PathPrefix: String
        """
        self.AddrbookIds = None
        self.CfwInstanceId = None

    def _deserialize(self, params):
        if params.get("AddrbookIds"):
            self.AddrbookIds = params.get("AddrbookIds")
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")


