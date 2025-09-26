from ksyun.common.abstract_model import AbstractModel


class QueryInstancesRequest(AbstractModel):
    """QueryInstances请求参数结构体
    """

    def __init__(self):
        r"""根据搜索条件查询实例列表
        :param associatedUserId: 企业账号中心关联用户ID。如果空，则会返回企业账号中心有查看权限的用户ID下的实例。
        :type PathPrefix: Int
        :param instanceIds: 实例ID列表
        :type PathPrefix: Array
        :param status: 实例状态，默认值为2.
枚举值如下：1-创建中,2-已开通,3-开通失败,4-已过期,5-已回收,6-已退订,7-已删除,8-已欠费,9-欠费回收,10-一键关停,11-一键回收,12-退订中
        :type PathPrefix: Int
        :param productGroup: 产品线ID，ID可以通过“价格体系”的QueryProductTypes接口查询
        :type PathPrefix: Int
        :param renewStrategy: 续费策略：0 手动续费，1 自动续费
        :type PathPrefix: Int
        :param billingBeginTimeFrom: 计费开始时间起始，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param billingBeginTimeTo: 计费开始时间结束，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param billingEndTimeFrom: 计费结束时间起始，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param billingEndTimeTo: 计费结束时间结束，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param serviceBeginTimeFrom: 服务开始时间起始，格式：yyyy-MM-dd HH:mm:ss
和计费开始时间的区别是因为有试用，所以服务时间不等于计费时间。
        :type PathPrefix: String
        :param serviceBeginTimeTo: 服务开始时间结束，格式：yyyy-MM-dd HH:mm:ss
和计费开始时间的区别是因为有试用，所以服务时间不等于计费时间。
        :type PathPrefix: String
        :param page: 页数，从1开始，默认1
        :type PathPrefix: Int
        :param size: 页大小，默认10
        :type PathPrefix: Int
        """
        self.associatedUserId = None
        self.instanceIds = None
        self.status = None
        self.productGroup = None
        self.renewStrategy = None
        self.billingBeginTimeFrom = None
        self.billingBeginTimeTo = None
        self.billingEndTimeFrom = None
        self.billingEndTimeTo = None
        self.serviceBeginTimeFrom = None
        self.serviceBeginTimeTo = None
        self.page = None
        self.size = None

    def _deserialize(self, params):
        if params.get("associatedUserId"):
            self.associatedUserId = params.get("associatedUserId")
        if params.get("instanceIds"):
            self.instanceIds = params.get("instanceIds")
        if params.get("status"):
            self.status = params.get("status")
        if params.get("productGroup"):
            self.productGroup = params.get("productGroup")
        if params.get("renewStrategy"):
            self.renewStrategy = params.get("renewStrategy")
        if params.get("billingBeginTimeFrom"):
            self.billingBeginTimeFrom = params.get("billingBeginTimeFrom")
        if params.get("billingBeginTimeTo"):
            self.billingBeginTimeTo = params.get("billingBeginTimeTo")
        if params.get("billingEndTimeFrom"):
            self.billingEndTimeFrom = params.get("billingEndTimeFrom")
        if params.get("billingEndTimeTo"):
            self.billingEndTimeTo = params.get("billingEndTimeTo")
        if params.get("serviceBeginTimeFrom"):
            self.serviceBeginTimeFrom = params.get("serviceBeginTimeFrom")
        if params.get("serviceBeginTimeTo"):
            self.serviceBeginTimeTo = params.get("serviceBeginTimeTo")
        if params.get("page"):
            self.page = params.get("page")
        if params.get("size"):
            self.size = params.get("size")
