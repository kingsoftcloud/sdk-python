from ksyun.common.abstract_model import AbstractModel

class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体
    """

    def __init__(self):
        r"""创建新工程
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param Description: 工程描述
        :type PathPrefix: String
        :param IamProjectId: 项目制ID，缺省时为默认项目
        :type PathPrefix: Int
        """
        self.ProjectName = None
        self.Description = None
        self.IamProjectId = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体
    """

    def __init__(self):
        r"""展示工程详情
        :param ProjectName: 工程名称
        :type PathPrefix: String
        """
        self.ProjectName = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")


class UpdateProjectRequest(AbstractModel):
    """UpdateProject请求参数结构体
    """

    def __init__(self):
        r"""更新工程信息
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param Description: 工程描述
        :type PathPrefix: String
        :param IamProjectId: 项目制id，缺省时为默认项目
        :type PathPrefix: Int
        """
        self.ProjectName = None
        self.Description = None
        self.IamProjectId = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体
    """

    def __init__(self):
        r"""删除该工程
        :param ProjectName: 工程名称
        :type PathPrefix: String
        """
        self.ProjectName = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")


class ListProjectsRequest(AbstractModel):
    """ListProjects请求参数结构体
    """

    def __init__(self):
        r"""查看工程列表
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param Description: 工程描述
        :type PathPrefix: String
        :param Page: 返回记录的页码，从0开始
        :type PathPrefix: Int
        :param Size: 每页返回最大条目，最大值500
        :type PathPrefix: Int
        """
        self.ProjectName = None
        self.Description = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class CreateLogPoolRequest(AbstractModel):
    """CreateLogPool请求参数结构体
    """

    def __init__(self):
        r"""创建日志池
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param RetentionDays: 数据保存时间，单位为天，范围1~3600
        :type PathPrefix: Int
        :param Partitions: 分区个数，2-64
        :type PathPrefix: Int
        :param Description: 日志池描述
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.RetentionDays = None
        self.Partitions = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("RetentionDays"):
            self.RetentionDays = params.get("RetentionDays")
        if params.get("Partitions"):
            self.Partitions = params.get("Partitions")
        if params.get("Description"):
            self.Description = params.get("Description")


class DescribeLogPoolRequest(AbstractModel):
    """DescribeLogPool请求参数结构体
    """

    def __init__(self):
        r"""日志池详情
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.LogPoolName = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")


class UpdateLogPoolRequest(AbstractModel):
    """UpdateLogPool请求参数结构体
    """

    def __init__(self):
        r"""修改日志池
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param LogPoolId: 日志池ID
        :type PathPrefix: String
        :param RetentionDays: 数据保存时间，单位为天，范围1~3600
        :type PathPrefix: Int
        :param Partitions: 分区数量
        :type PathPrefix: Int
        :param Description: 日志池描述
        :type PathPrefix: String
        :param Config: 
        :type PathPrefix: Object
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.LogPoolId = None
        self.RetentionDays = None
        self.Partitions = None
        self.Description = None
        self.Config = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("LogPoolId"):
            self.LogPoolId = params.get("LogPoolId")
        if params.get("RetentionDays"):
            self.RetentionDays = params.get("RetentionDays")
        if params.get("Partitions"):
            self.Partitions = params.get("Partitions")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Config"):
            self.Config = params.get("Config")


class DeleteLogPoolRequest(AbstractModel):
    """DeleteLogPool请求参数结构体
    """

    def __init__(self):
        r"""删除日志池
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolId: 日志池ID
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.LogPoolId = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolId"):
            self.LogPoolId = params.get("LogPoolId")


class ListLogPoolsRequest(AbstractModel):
    """ListLogPools请求参数结构体
    """

    def __init__(self):
        r"""获取日志池列表
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 根据日志池名称筛选日志池，支持模糊搜索
        :type PathPrefix: String
        :param Page: 页码，从0开始
        :type PathPrefix: Int
        :param Size: 每页返回最大条目，最大值500
        :type PathPrefix: Int
        :param Tags: 需要筛选的标签
        :type PathPrefix: Object
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.Page = None
        self.Size = None
        self.Tags = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")
        if params.get("Tags"):
            self.Tags = params.get("Tags")


class GetLogsRequest(AbstractModel):
    """GetLogs请求参数结构体
    """

    def __init__(self):
        r"""查询日志池
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param LogPoolId: 日志池ID
        :type PathPrefix: String
        :param From: 查询开始时间，unix时间戳
        :type PathPrefix: Int
        :param To: 查询结束时间，unix时间戳
        :type PathPrefix: Int
        :param Query: 查询分析语法。关于查询分析的详细语法，详见查询语法，不填的情况下 返回原始日志
        :type PathPrefix: String
        :param Offset: 偏移页数，从0开始
仅支持运算符语法
        :type PathPrefix: Int
        :param Size: 查询结果条数
仅支持运算符语法
        :type PathPrefix: Int
        :param HitsOpen: 是否按时间间隔统计数据行数，当该值为true时，interval参数为必填
        :type PathPrefix: Boolean
        :param Interval: 数据统计时间间隔
示例：10s、5m、1h
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.LogPoolId = None
        self.From = None
        self.To = None
        self.Query = None
        self.Offset = None
        self.Size = None
        self.HitsOpen = None
        self.Interval = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("LogPoolId"):
            self.LogPoolId = params.get("LogPoolId")
        if params.get("From"):
            self.From = params.get("From")
        if params.get("To"):
            self.To = params.get("To")
        if params.get("Query"):
            self.Query = params.get("Query")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Size"):
            self.Size = params.get("Size")
        if params.get("HitsOpen"):
            self.HitsOpen = params.get("HitsOpen")
        if params.get("Interval"):
            self.Interval = params.get("Interval")


class CreateQuickSearchRequest(AbstractModel):
    """CreateQuickSearch请求参数结构体
    """

    def __init__(self):
        r"""存为快速查询
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param QuickSearchName: 快速查询名称
        :type PathPrefix: String
        :param Query: 查询语句
        :type PathPrefix: String
        :param Description: 快速查询的备注
        :type PathPrefix: String
        :param TimeRange: 查询数据的时间范围
{
    "from": 1737388800000,
    "to": 1737444861000,
    "key": "h",
    "value": -24,
    "start": 21,
    "startKey": "m",
    "end": 2,
    "endKey": "s",
    "tab": "Absolute|Relative",
    "label": "近15分钟"
}
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.QuickSearchName = None
        self.Query = None
        self.Description = None
        self.TimeRange = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("QuickSearchName"):
            self.QuickSearchName = params.get("QuickSearchName")
        if params.get("Query"):
            self.Query = params.get("Query")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("TimeRange"):
            self.TimeRange = params.get("TimeRange")


class ListQuickSearchsRequest(AbstractModel):
    """ListQuickSearchs请求参数结构体
    """

    def __init__(self):
        r"""获取快速查询列表
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param Filter: 根据快速查询名称过滤列表，支持模糊搜索
        :type PathPrefix: String
        :param Page: 页码，从0开始
        :type PathPrefix: Int
        :param Size: 每页返回最大条目，默认 500（最大值）
        :type PathPrefix: Int
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.Filter = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class DeleteQuickSearchsRequest(AbstractModel):
    """DeleteQuickSearchs请求参数结构体
    """

    def __init__(self):
        r"""删除快速查询
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param QuickSearchName: 快速查询名称
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.QuickSearchName = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("QuickSearchName"):
            self.QuickSearchName = params.get("QuickSearchName")


class CreateDownloadTaskRequest(AbstractModel):
    """CreateDownloadTask请求参数结构体
    """

    def __init__(self):
        r"""创建日志下载任务
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolNames: 日志池名称
        :type PathPrefix: String
        :param Config: 下载参数
        :type PathPrefix: Object
        """
        self.ProjectName = None
        self.LogPoolNames = None
        self.Config = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolNames"):
            self.LogPoolNames = params.get("LogPoolNames")
        if params.get("Config"):
            self.Config = params.get("Config")


class ListDownloadTasksRequest(AbstractModel):
    """ListDownloadTasks请求参数结构体
    """

    def __init__(self):
        r"""查看日志下载任务
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param Page: 返回记录的页码，从0开始
        :type PathPrefix: String
        :param Size: 每页返回最大条目，最大值500
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


