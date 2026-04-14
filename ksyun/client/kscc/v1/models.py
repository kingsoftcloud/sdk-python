from ksyun.common.abstract_model import AbstractModel

class UpdateUserQuotaRequest(AbstractModel):
    """UpdateUserQuota请求参数结构体
    """

    def __init__(self):
        r"""更新用户月度配额，如不存在则新增现在，如果存在则更新。当quotaAmount为null代表不限制。
        :param UserName: 用户邮箱前缀，比如： zhangsan3
        :type PathPrefix: String
        :param QuotaAmount: 用户月度的限额
        :type PathPrefix: Double
        """
        self.UserName = None
        self.QuotaAmount = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("QuotaAmount"):
            self.QuotaAmount = params.get("QuotaAmount")


class DescribeUserCostSummaryRequest(AbstractModel):
    """DescribeUserCostSummary请求参数结构体
    """

    def __init__(self):
        r"""用户本月配额数据统计
        :param UserName: 邮箱前缀，比如：zhangsan3
        :type PathPrefix: String
        """
        self.UserName = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")


