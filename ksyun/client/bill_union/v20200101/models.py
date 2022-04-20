from ksyun.common.abstract_model import AbstractModel

class DescribeBillSummaryByPayModeRequest(AbstractModel):
    """DescribeBillSummaryByPayMode请求参数结构体
    """

    def __init__(self):
        r"""获取计费类别汇总账单
        """

    def _deserialize(self, params):
        return


class DescribeBillSummaryByProductRequest(AbstractModel):
    """DescribeBillSummaryByProduct请求参数结构体
    """

    def __init__(self):
        r"""按产品线获取账单汇总金额
        """

    def _deserialize(self, params):
        return


class DescribeBillSummaryByProjectRequest(AbstractModel):
    """DescribeBillSummaryByProject请求参数结构体
    """

    def __init__(self):
        r"""按项目制获取账单汇总金额
        :param BillBeginMonth: 账单开始月份
        :type PathPrefix: String
        :param BillEndMonth: 账单结束月份
        :type PathPrefix: String
        """
        self.BillBeginMonth = None
        self.BillEndMonth = None

    def _deserialize(self, params):
        if params.get("BillBeginMonth"):
            self.BillBeginMonth = params.get("BillBeginMonth")
        if params.get("BillEndMonth"):
            self.BillEndMonth = params.get("BillEndMonth")


class DescribeInstanceSummaryBillsRequest(AbstractModel):
    """DescribeInstanceSummaryBills请求参数结构体
    """

    def __init__(self):
        r"""按实例ID获取账单汇总金额
        """

    def _deserialize(self, params):
        return


class DescribeProductCodeRequest(AbstractModel):
    """DescribeProductCode请求参数结构体
    """

    def __init__(self):
        r"""获取产品线列表
        """

    def _deserialize(self, params):
        return


class DescribeSplitItemBillDetailsRequest(AbstractModel):
    """DescribeSplitItemBillDetails请求参数结构体
    """

    def __init__(self):
        r"""分页查询分拆项账单明细
        """

    def _deserialize(self, params):
        return


