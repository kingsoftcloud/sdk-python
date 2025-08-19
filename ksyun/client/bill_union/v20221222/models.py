from ksyun.common.abstract_model import AbstractModel

class QueryInstanceConsumeRequest(AbstractModel):
    """QueryInstanceConsume请求参数结构体
    """

    def __init__(self):
        r"""查询实例按日汇总账单
        :param StartDay: 账单开始时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param EndDay: 账单结束时间，YYYY－MM-DD，支持当前月，不支持跨月。


        :type PathPrefix: String
        :param ProductCode: 可选参数，产品线对应的Code。eg. KEC，默认获取所有产品线的账单，取值可以参考 获取产品线列表  金山云-文档中心-获取产品线列表 (ksyun.com)

        :type PathPrefix: String
        :param Page: 第几页,默认值为1

        :type PathPrefix: Int
        :param Size: 每页条数,默认值20，最大值200

        :type PathPrefix: Int
        """
        self.StartDay = None
        self.EndDay = None
        self.ProductCode = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("StartDay"):
            self.StartDay = params.get("StartDay")
        if params.get("EndDay"):
            self.EndDay = params.get("EndDay")
        if params.get("ProductCode"):
            self.ProductCode = params.get("ProductCode")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class QueryProjectConsumeRequest(AbstractModel):
    """QueryProjectConsume请求参数结构体
    """

    def __init__(self):
        r"""项目制按日汇总账单
        :param StartDay: 账单开始时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param EndDay: 账单结束时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param Page: 第几页,默认值为1
        :type PathPrefix: Int
        :param Size: 每页条数,默认值20，最大值200
        :type PathPrefix: Int
        """
        self.StartDay = None
        self.EndDay = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("StartDay"):
            self.StartDay = params.get("StartDay")
        if params.get("EndDay"):
            self.EndDay = params.get("EndDay")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class QueryProductConsumeRequest(AbstractModel):
    """QueryProductConsume请求参数结构体
    """

    def __init__(self):
        r"""产品线按日汇总账单
        :param StartDay: 账单开始时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param EndDay: 账单结束时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param Page: 第几页,默认值为1
        :type PathPrefix: Int
        :param Size: 每页条数,默认值20，最大值200
        :type PathPrefix: Int
        """
        self.StartDay = None
        self.EndDay = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("StartDay"):
            self.StartDay = params.get("StartDay")
        if params.get("EndDay"):
            self.EndDay = params.get("EndDay")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class QueryFinanceUnitConsumeRequest(AbstractModel):
    """QueryFinanceUnitConsume请求参数结构体
    """

    def __init__(self):
        r"""财务单元按日汇总账单
        :param StartDay: 账单开始时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param EndDay: 账单结束时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param Page: 第几页,默认值为1
        :type PathPrefix: Int
        :param Size: 每页条数,默认值20，最大值200
        :type PathPrefix: Int
        """
        self.StartDay = None
        self.EndDay = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("StartDay"):
            self.StartDay = params.get("StartDay")
        if params.get("EndDay"):
            self.EndDay = params.get("EndDay")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class QueryFinanceUnitConsumeOfMonthRequest(AbstractModel):
    """QueryFinanceUnitConsumeOfMonth请求参数结构体
    """

    def __init__(self):
        r"""财务单元按月汇总账单
        :param CustomerBillMonth: 账期(执行月) yyyyMM
        :type PathPrefix: String
        :param Page: 第几页,默认值为1
        :type PathPrefix: Int
        :param Size: 每页条数,默认值20，最大值200
        :type PathPrefix: Int
        """
        self.CustomerBillMonth = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("CustomerBillMonth"):
            self.CustomerBillMonth = params.get("CustomerBillMonth")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class QueryUserConsumeRequest(AbstractModel):
    """QueryUserConsume请求参数结构体
    """

    def __init__(self):
        r"""计费类别按日汇总账单
        :param StartDay: 账单开始时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param EndDay: 账单结束时间，YYYY－MM-DD，支持当前月，不支持跨月。
        :type PathPrefix: String
        :param Page: 第几页,默认值为1
        :type PathPrefix: Int
        :param Size: 每页条数,默认值20，最大值200
        :type PathPrefix: Int
        """
        self.StartDay = None
        self.EndDay = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("StartDay"):
            self.StartDay = params.get("StartDay")
        if params.get("EndDay"):
            self.EndDay = params.get("EndDay")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


