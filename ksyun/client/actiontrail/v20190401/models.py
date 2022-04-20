from ksyun.common.abstract_model import AbstractModel

class ListOperateLogsRequest(AbstractModel):
    """ListOperateLogs请求参数结构体
    """

    def __init__(self):
        r"""获取历史事件记录
        :param EventName: 事件名称，为操作的接口Action名称
        :type PathPrefix: String
        :param EventRw: 事件类型：read(读操作)，write(写操作)；不传则查询所有类型操作
        :type PathPrefix: String
        :param ServiceName: 服务名称
        :type PathPrefix: String
        :param UserName: 调用者的名称。
- 如果是主账号，显示为root。
- 如果为子用户未IAM子用户名称。
        :type PathPrefix: String
        :param AccessKey: 支持使用AccessKeyID查询对应调用事件记录。
        :type PathPrefix: String
        :param EventBeginDate: 事件开始日期，格式为YYYY-MM-DD
        :type PathPrefix: String
        :param EventEndDate: 事件结束日期，格式为YYYY-MM-DD
        :type PathPrefix: String
        :param ResourceType: 资源类型
        :type PathPrefix: String
        :param ResourceName: 资源名称
        :type PathPrefix: String
        :param Page: 页码，默认1
        :type PathPrefix: String
        :param PageSize: 每页查询个数，默认10
        :type PathPrefix: String
        :param SearchAfter: 上次请求返回的最后一条数据的游标
        :type PathPrefix: String
        """
        self.EventName = None
        self.EventRw = None
        self.ServiceName = None
        self.UserName = None
        self.AccessKey = None
        self.EventBeginDate = None
        self.EventEndDate = None
        self.ResourceType = None
        self.ResourceName = None
        self.Page = None
        self.PageSize = None
        self.SearchAfter = None

    def _deserialize(self, params):
        if params.get("EventName"):
            self.EventName = params.get("EventName")
        if params.get("EventRw"):
            self.EventRw = params.get("EventRw")
        if params.get("ServiceName"):
            self.ServiceName = params.get("ServiceName")
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("AccessKey"):
            self.AccessKey = params.get("AccessKey")
        if params.get("EventBeginDate"):
            self.EventBeginDate = params.get("EventBeginDate")
        if params.get("EventEndDate"):
            self.EventEndDate = params.get("EventEndDate")
        if params.get("ResourceType"):
            self.ResourceType = params.get("ResourceType")
        if params.get("ResourceName"):
            self.ResourceName = params.get("ResourceName")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("SearchAfter"):
            self.SearchAfter = params.get("SearchAfter")


