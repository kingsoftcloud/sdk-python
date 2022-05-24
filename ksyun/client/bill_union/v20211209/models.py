from ksyun.common.abstract_model import AbstractModel

class DescribeCostBillRequest(AbstractModel):
    """DescribeCostBill请求参数结构体
    """

    def __init__(self):
        r"""获取预付费成本账单
        :param billMonth: 账单月
        :type PathPrefix: Int
        :param statisticalItem: 统计项，0：按实例；1：按产品
        :type PathPrefix: Int
        :param instanceIds: 实例id列表，仅当statisticalItem=0时有效
        :type PathPrefix: String
        :param pageNo: 分页page no
        :type PathPrefix: Int
        :param pageSize: 分页page size
        :type PathPrefix: Int
        """
        self.billMonth = None
        self.statisticalItem = None
        self.instanceIds = None
        self.pageNo = None
        self.pageSize = None

    def _deserialize(self, params):
        if params.get("billMonth"):
            self.billMonth = params.get("billMonth")
        if params.get("statisticalItem"):
            self.statisticalItem = params.get("statisticalItem")
        if params.get("instanceIds"):
            self.instanceIds = params.get("instanceIds")
        if params.get("pageNo"):
            self.pageNo = params.get("pageNo")
        if params.get("pageSize"):
            self.pageSize = params.get("pageSize")


