from ksyun.common.abstract_model import AbstractModel

class GetMonthBillRequest(AbstractModel):
    """GetMonthBill请求参数结构体
    """

    def __init__(self):
        r"""获取月账单
        :param BillStartMonth: 必选参数，账单开始月份
        :type PathPrefix: String
        :param BillEndMonth: 必选参数，账单结束月份
        :type PathPrefix: String
        """
        self.BillStartMonth = None
        self.BillEndMonth = None

    def _deserialize(self, params):
        if params.get("BillStartMonth"):
            self.BillStartMonth = params.get("BillStartMonth")
        if params.get("BillEndMonth"):
            self.BillEndMonth = params.get("BillEndMonth")


class GetPostpayDetailBillRequest(AbstractModel):
    """GetPostpayDetailBill请求参数结构体
    """

    def __init__(self):
        r"""获取账单明细
        :param BillStartMonth: 必选参数，账单开始月份，eg. 2018-06
        :type PathPrefix: String
        :param BillEndMonth: 必选参数，账单结束月份
        :type PathPrefix: String
        :param ProductCode: 可选参数，产品类型对应的Code。eg. KEC，不传获取所有产品类型的账单,取值可以参考产品线映射关系
        :type PathPrefix: String
        :param ProjectId: 可选参数，项目组Id，不传获取所有项目Id
        :type PathPrefix: String
        """
        self.BillStartMonth = None
        self.BillEndMonth = None
        self.ProductCode = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("BillStartMonth"):
            self.BillStartMonth = params.get("BillStartMonth")
        if params.get("BillEndMonth"):
            self.BillEndMonth = params.get("BillEndMonth")
        if params.get("ProductCode"):
            self.ProductCode = params.get("ProductCode")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class GetProductCodeRequest(AbstractModel):
    """GetProductCode请求参数结构体
    """

    def __init__(self):
        r"""获取产品线映射
        """

    def _deserialize(self, params):
        return


