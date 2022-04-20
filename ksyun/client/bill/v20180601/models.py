from ksyun.common.abstract_model import AbstractModel

class GetMonthBillRequest(AbstractModel):
    """GetMonthBill请求参数结构体
    """

    def __init__(self):
        r"""获取月账单
        :param Action: GetMonthBill
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class GetPostpayDetailBillRequest(AbstractModel):
    """GetPostpayDetailBill请求参数结构体
    """

    def __init__(self):
        r"""获取账单明细
        """

    def _deserialize(self, params):
        return


class GetPostpayDetailBillCSVRequest(AbstractModel):
    """GetPostpayDetailBillCSV请求参数结构体
    """

    def __init__(self):
        r"""导出账单明细
        """

    def _deserialize(self, params):
        return


class GetProductCodeRequest(AbstractModel):
    """GetProductCode请求参数结构体
    """

    def __init__(self):
        r"""获取产品线映射
        """

    def _deserialize(self, params):
        return


class GetMonthConsumeRequest(AbstractModel):
    """GetMonthConsume请求参数结构体
    """

    def __init__(self):
        r"""获取日耗月账单
        """

    def _deserialize(self, params):
        return


class GetPostpayDetailConsumeRequest(AbstractModel):
    """GetPostpayDetailConsume请求参数结构体
    """

    def __init__(self):
        r"""获取日耗账单明细
        """

    def _deserialize(self, params):
        return


