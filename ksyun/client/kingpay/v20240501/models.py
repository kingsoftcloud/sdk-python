from ksyun.common.abstract_model import AbstractModel


class QueryCashWalletActionRequest(AbstractModel):
    """QueryCashWalletAction请求参数结构体
    """

    def __init__(self):
        r"""获取用户账户余额
        :param subject: 1:金山云，2：边缘云
        :type PathPrefix: Int
        """
        self.subject = None

    def _deserialize(self, params):
        if params.get("subject"):
            self.subject = params.get("subject")
