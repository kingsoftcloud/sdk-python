from ksyun.common.abstract_model import AbstractModel

class QueryItemBillsRequest(AbstractModel):
    """QueryItemBills请求参数结构体
    """

    def __init__(self):
        r"""查询计费项账单
        :param CustomerBillMonth: 账期
        :type PathPrefix: Int
        :param ProductGroupCode: 产品线CODE
        :type PathPrefix: String
        :param PayType: 计费方式：0预付费、1实时付费、2后付费
        :type PathPrefix: Int
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param SubAccountId: 托管子账号ID
        :type PathPrefix: Int
        :param Size: 查询条数，最大值1000
        :type PathPrefix: Int
        :param LastSortValue: 上次查询排序值LastSortValue，基于es search_after; 
        :type PathPrefix: String
        """
        self.CustomerBillMonth = None
        self.ProductGroupCode = None
        self.PayType = None
        self.InstanceId = None
        self.SubAccountId = None
        self.Size = None
        self.LastSortValue = None

    def _deserialize(self, params):
        if params.get("CustomerBillMonth"):
            self.CustomerBillMonth = params.get("CustomerBillMonth")
        if params.get("ProductGroupCode"):
            self.ProductGroupCode = params.get("ProductGroupCode")
        if params.get("PayType"):
            self.PayType = params.get("PayType")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("SubAccountId"):
            self.SubAccountId = params.get("SubAccountId")
        if params.get("Size"):
            self.Size = params.get("Size")
        if params.get("LastSortValue"):
            self.LastSortValue = params.get("LastSortValue")


class QueryProductTypesRequest(AbstractModel):
    """QueryProductTypes请求参数结构体
    """

    def __init__(self):
        r"""产品子类型查询
        :param ProductGroupCode: 产品线code
        :type PathPrefix: String
        """
        self.ProductGroupCode = None

    def _deserialize(self, params):
        if params.get("ProductGroupCode"):
            self.ProductGroupCode = params.get("ProductGroupCode")


