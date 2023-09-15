from ksyun.common.abstract_model import AbstractModel

class GetMonthConsumeRequest(AbstractModel):
    """GetMonthConsume请求参数结构体
    """

    def __init__(self):
        r"""获取日耗月账单
        :param BillMonth: 必选参数，账单月份必选参数，账单月份YYYY-MM 
        :type PathPrefix: String
        """
        self.BillMonth = None

    def _deserialize(self, params):
        if params.get("BillMonth"):
            self.BillMonth = params.get("BillMonth")


class GetPostpayDetailConsumeRequest(AbstractModel):
    """GetPostpayDetailConsume请求参数结构体
    """

    def __init__(self):
        r"""获取日耗账单明细
        :param BillMonth: 必选参数，账单月份，eg. 2018-06 
        :type PathPrefix: String
        :param ProductCode: 	可选参数，产品类型对应的Code。eg. KEC，不传获取所有产品类型的账单,取值可以参考产品线映射关系
        :type PathPrefix: String
        :param ProjectId: 可选参数，项目组Id，不传获取所有项目Id 
        :type PathPrefix: String
        :param PageNo: 可选参数，页码，不传默认为0 
        :type PathPrefix: Int
        :param PageSize: 可选参数，每页数量，不传默认为1，最大只允许传5000 
        :type PathPrefix: Int
        """
        self.BillMonth = None
        self.ProductCode = None
        self.ProjectId = None
        self.PageNo = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("BillMonth"):
            self.BillMonth = params.get("BillMonth")
        if params.get("ProductCode"):
            self.ProductCode = params.get("ProductCode")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("PageNo"):
            self.PageNo = params.get("PageNo")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


