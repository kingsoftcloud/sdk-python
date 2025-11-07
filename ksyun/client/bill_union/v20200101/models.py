from ksyun.common.abstract_model import AbstractModel

class DescribeBillSummaryByPayModeRequest(AbstractModel):
    """DescribeBillSummaryByPayMode请求参数结构体
    """

    def __init__(self):
        r"""获取计费类别汇总账单（费用账单接口，推荐使用，包含预付费、实时付费、后付费）
        :param BillBeginMonth: 账单开始时间
        :type PathPrefix: String
        :param BillEndMonth: 账单结束时间
        :type PathPrefix: String
        :param SubAccount: 成员账账号Id，非必填
        :type PathPrefix: Int
        :param FetchAllFinanceRelationData: 非必传，默认值为 False。
是否吐出全部财务关系数据。
值为true时，同时吐出财务管理和财务托管账号数据。
值为false时或不传该参数，仅吐出财务托管账号数据。
        :type PathPrefix: Boolean
        """
        self.BillBeginMonth = None
        self.BillEndMonth = None
        self.SubAccount = None
        self.FetchAllFinanceRelationData = None

    def _deserialize(self, params):
        if params.get("BillBeginMonth"):
            self.BillBeginMonth = params.get("BillBeginMonth")
        if params.get("BillEndMonth"):
            self.BillEndMonth = params.get("BillEndMonth")
        if params.get("SubAccount"):
            self.SubAccount = params.get("SubAccount")
        if params.get("FetchAllFinanceRelationData"):
            self.FetchAllFinanceRelationData = params.get("FetchAllFinanceRelationData")


class DescribeBillSummaryByProductRequest(AbstractModel):
    """DescribeBillSummaryByProduct请求参数结构体
    """

    def __init__(self):
        r"""按产品线获取账单汇总金额
        :param BillBeginMonth: 账单开始时间
        :type PathPrefix: String
        :param BillEndMonth: 账单结束时间
        :type PathPrefix: String
        :param SubAccount: 成员账号Id
        :type PathPrefix: Int
        :param FetchAllFinanceRelationData: 非必传，默认值为 False。
是否吐出全部财务关系数据。
值为true时，同时吐出财务管理和财务托管账号数据。
值为false时或不传该参数，仅吐出财务托管账号数据。
        :type PathPrefix: Boolean
        """
        self.BillBeginMonth = None
        self.BillEndMonth = None
        self.SubAccount = None
        self.FetchAllFinanceRelationData = None

    def _deserialize(self, params):
        if params.get("BillBeginMonth"):
            self.BillBeginMonth = params.get("BillBeginMonth")
        if params.get("BillEndMonth"):
            self.BillEndMonth = params.get("BillEndMonth")
        if params.get("SubAccount"):
            self.SubAccount = params.get("SubAccount")
        if params.get("FetchAllFinanceRelationData"):
            self.FetchAllFinanceRelationData = params.get("FetchAllFinanceRelationData")


class DescribeBillSummaryByProjectRequest(AbstractModel):
    """DescribeBillSummaryByProject请求参数结构体
    """

    def __init__(self):
        r"""按项目制获取账单汇总金额（费用账单接口，推荐使用，包含预付费、实时付费、后付费）
        :param BillBeginMonth: 账单开始月份
        :type PathPrefix: String
        :param BillEndMonth: 账单结束月份
        :type PathPrefix: String
        :param SubAccount: 成员账号Id
        :type PathPrefix: Int
        :param FetchAllFinanceRelationData: 非必传，默认值为 False。
是否吐出全部财务关系数据。
值为true时，同时吐出财务管理和财务托管账号数据。
值为false时或不传该参数，仅吐出财务托管账号数据。
        :type PathPrefix: Boolean
        """
        self.BillBeginMonth = None
        self.BillEndMonth = None
        self.SubAccount = None
        self.FetchAllFinanceRelationData = None

    def _deserialize(self, params):
        if params.get("BillBeginMonth"):
            self.BillBeginMonth = params.get("BillBeginMonth")
        if params.get("BillEndMonth"):
            self.BillEndMonth = params.get("BillEndMonth")
        if params.get("SubAccount"):
            self.SubAccount = params.get("SubAccount")
        if params.get("FetchAllFinanceRelationData"):
            self.FetchAllFinanceRelationData = params.get("FetchAllFinanceRelationData")


class DescribeInstanceSummaryBillsRequest(AbstractModel):
    """DescribeInstanceSummaryBills请求参数结构体
    """

    def __init__(self):
        r"""按实例ID获取账单汇总金额
        :param BillMonth: 客户账单月份，YYYY-MM。不支持跨月查询
        :type PathPrefix: String
        :param ProductCode: 产品线对应的Code
        :type PathPrefix: String
        :param Page: 页码
        :type PathPrefix: Int
        :param Size: 每页数量
        :type PathPrefix: Int
        """
        self.BillMonth = None
        self.ProductCode = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("BillMonth"):
            self.BillMonth = params.get("BillMonth")
        if params.get("ProductCode"):
            self.ProductCode = params.get("ProductCode")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


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
        :param CustomerBillMonth: 账期，格式：yyyyMM。如：202111
        :type PathPrefix: Int
        :param ProductGroupCode: 产品线 code
        :type PathPrefix: String
        :param StatisticType: 统计周期
        :type PathPrefix: Int
        :param PayType: 计费类别
        :type PathPrefix: Int
        :param SubAccountId: 主账号所托管的账号Id
        :type PathPrefix: Int
        :param Page: 第几页
        :type PathPrefix: Int
        :param Size: 每页条数
        :type PathPrefix: String
        """
        self.CustomerBillMonth = None
        self.ProductGroupCode = None
        self.StatisticType = None
        self.PayType = None
        self.SubAccountId = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("CustomerBillMonth"):
            self.CustomerBillMonth = params.get("CustomerBillMonth")
        if params.get("ProductGroupCode"):
            self.ProductGroupCode = params.get("ProductGroupCode")
        if params.get("StatisticType"):
            self.StatisticType = params.get("StatisticType")
        if params.get("PayType"):
            self.PayType = params.get("PayType")
        if params.get("SubAccountId"):
            self.SubAccountId = params.get("SubAccountId")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class DescribeMiItemBillsRequest(AbstractModel):
    """DescribeMiItemBills请求参数结构体
    """

    def __init__(self):
        r"""小米计费项账单
        :param BillMonth: 
        :type PathPrefix: String
        """
        self.BillMonth = None

    def _deserialize(self, params):
        if params.get("BillMonth"):
            self.BillMonth = params.get("BillMonth")


class DescribeSplitItemDayBillDetailsRequest(AbstractModel):
    """DescribeSplitItemDayBillDetails请求参数结构体
    """

    def __init__(self):
        r"""分页查询分拆项账单明细
        :param CustomerBillMonth: 账期，格式：yyyyMM。如：202211

        :type PathPrefix: Int
        :param ProductGroupCode: 产品线 code，目前仅支持KS3_GROUP
        :type PathPrefix: String
        :param StatisticType: 统计周期，固化传 3（代表明细）
        :type PathPrefix: Int
        :param PayType: 计费类别，0（预付费），1（实时付费），2（后付费）；该接口仅支持后付费
        :type PathPrefix: Int
        :param SubAccountId: 主账号所托管的账号Id

        :type PathPrefix: Int
        :param Page: 第几页
        :type PathPrefix: Int
        :param Size: 每页条数

        :type PathPrefix: Int
        """
        self.CustomerBillMonth = None
        self.ProductGroupCode = None
        self.StatisticType = None
        self.PayType = None
        self.SubAccountId = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("CustomerBillMonth"):
            self.CustomerBillMonth = params.get("CustomerBillMonth")
        if params.get("ProductGroupCode"):
            self.ProductGroupCode = params.get("ProductGroupCode")
        if params.get("StatisticType"):
            self.StatisticType = params.get("StatisticType")
        if params.get("PayType"):
            self.PayType = params.get("PayType")
        if params.get("SubAccountId"):
            self.SubAccountId = params.get("SubAccountId")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class ListProductGroupsRequest(AbstractModel):
    """ListProductGroups请求参数结构体
    """

    def __init__(self):
        r"""获取产品线详情列表
        """

    def _deserialize(self, params):
        return


