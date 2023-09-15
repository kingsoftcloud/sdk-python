from ksyun.common.abstract_model import AbstractModel

class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体
    """

    def __init__(self):
        r"""创建项目
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param Description: 工程描述
        :type PathPrefix: String
        :param Region: 所属地域
        :type PathPrefix: String
        :param IamProjectId: 项目id，不填则默认为默认项目id
        :type PathPrefix: Int
        :param IamProjectName: 项目名称，不填则为默认项目名称，以IamProjectId为准
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.Description = None
        self.Region = None
        self.IamProjectId = None
        self.IamProjectName = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Region"):
            self.Region = params.get("Region")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")
        if params.get("IamProjectName"):
            self.IamProjectName = params.get("IamProjectName")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体
    """

    def __init__(self):
        r"""项目详情
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
        r"""更新项目
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param Description: 工程描述
        :type PathPrefix: String
        :param IamProjectId: 项目id，不填写则不会改变绑定项目
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
        r"""删除项目
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
        r"""查看项目列表
        :param Page: 返回记录的页码，从0开始
        :type PathPrefix: Int
        :param Size: 每页返回最大条目，默认 500（最大值）
        :type PathPrefix: Int
        """
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
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
        r"""修个日志池
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param RetentionDays: 数据保存时间，单位为天，范围1~3600
        :type PathPrefix: Int
        :param Partitions: 分区数量
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


class DeleteLogPoolRequest(AbstractModel):
    """DeleteLogPool请求参数结构体
    """

    def __init__(self):
        r"""删除日志池
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


class ListLogPoolsRequest(AbstractModel):
    """ListLogPools请求参数结构体
    """

    def __init__(self):
        r"""获取日志池列表
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param Page: 页码，从0开始
        :type PathPrefix: Int
        :param Size: 每页返回最大条目，默认 500（最大值）
        :type PathPrefix: Int
        :param LogPoolName: 如果想要根据名称搜索某个日志池，该字段必须填写
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.Page = None
        self.Size = None
        self.LogPoolName = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")


class PutLogsRequest(AbstractModel):
    """PutLogs请求参数结构体
    """

    def __init__(self):
        r"""上传日志
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param Time: 日志时间
        :type PathPrefix: String
        :param Contents: 每个元素为一个content，详见Content字段说明
        :type PathPrefix: String
        :param Key: 自定义key名称
        :type PathPrefix: String
        :param Value: 自定义key对应的值
        :type PathPrefix: String
        :param Logs: Log的列表，详见Log
        :type PathPrefix: String
        :param Filename: 日志的文件名
        :type PathPrefix: String
        :param Source: 日志来源，可以填写机器的ip
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.Time = None
        self.Contents = None
        self.Key = None
        self.Value = None
        self.Logs = None
        self.Filename = None
        self.Source = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("Time"):
            self.Time = params.get("Time")
        if params.get("Contents"):
            self.Contents = params.get("Contents")
        if params.get("Key"):
            self.Key = params.get("Key")
        if params.get("Value"):
            self.Value = params.get("Value")
        if params.get("Logs"):
            self.Logs = params.get("Logs")
        if params.get("Filename"):
            self.Filename = params.get("Filename")
        if params.get("Source"):
            self.Source = params.get("Source")


class GetLogsRequest(AbstractModel):
    """GetLogs请求参数结构体
    """

    def __init__(self):
        r"""查询日志
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称，多个日志池按逗号（,）分隔
        :type PathPrefix: String
        :param From: 查询开始时间，unix时间戳，单位毫秒
        :type PathPrefix: Int
        :param To: 查询结束时间，unix时间戳，单位毫秒
        :type PathPrefix: Int
        :param Query: 查询分析语法。关于查询分析的详细语法，详见[查询语法](https://docs.ksyun.com/documents/37865)，不填的情况下 返回原始日志
        :type PathPrefix: String
        :param LogPoolId: 日志池id
        :type PathPrefix: String
        :param HitsOpen: 如果需要查询结果展示日志趋势，则需将该字段设为true。默认不会展示日志趋势。
        :type PathPrefix: Boolean
        :param Interval: 间隔。单位支持秒(s)、分(m)、时(h)、天(d)、周(w)。示例：10s、2m、4h、1d、1w。
        :type PathPrefix: String
        :param SortBy: 用于进行结果排序的字段，List<Map<String,String>>，key是需要排序的字段value是排序方式，值为asc或者descValuesKey
        :type PathPrefix: String
        :param Offset: 表示页数
        :type PathPrefix: Int
        :param Size: 分页大小
        :type PathPrefix: Int
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.From = None
        self.To = None
        self.Query = None
        self.LogPoolId = None
        self.HitsOpen = None
        self.Interval = None
        self.SortBy = None
        self.Offset = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("From"):
            self.From = params.get("From")
        if params.get("To"):
            self.To = params.get("To")
        if params.get("Query"):
            self.Query = params.get("Query")
        if params.get("LogPoolId"):
            self.LogPoolId = params.get("LogPoolId")
        if params.get("HitsOpen"):
            self.HitsOpen = params.get("HitsOpen")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Size"):
            self.Size = params.get("Size")


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
        :param Description: 快速查询的备注
        :type PathPrefix: String
        :param TimeRange: 查询数据的时间范围
        :type PathPrefix: String
        :param Query: 查询语句
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.QuickSearchName = None
        self.Description = None
        self.TimeRange = None
        self.Query = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("QuickSearchName"):
            self.QuickSearchName = params.get("QuickSearchName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("TimeRange"):
            self.TimeRange = params.get("TimeRange")
        if params.get("Query"):
            self.Query = params.get("Query")


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


class GetQuickSearchRequest(AbstractModel):
    """GetQuickSearch请求参数结构体
    """

    def __init__(self):
        r"""获取快速查询列表
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


class CreateDashboardRequest(AbstractModel):
    """CreateDashboard请求参数结构体
    """

    def __init__(self):
        r"""创建仪表盘
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param DashboardName: 仪表盘名称
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.DashboardName = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("DashboardName"):
            self.DashboardName = params.get("DashboardName")


class DeleteDashboardRequest(AbstractModel):
    """DeleteDashboard请求参数结构体
    """

    def __init__(self):
        r"""删除仪表盘
        :param DashboardId: 仪表盘ID
        :type PathPrefix: String
        """
        self.DashboardId = None

    def _deserialize(self, params):
        if params.get("DashboardId"):
            self.DashboardId = params.get("DashboardId")


class DescribeDashboardRequest(AbstractModel):
    """DescribeDashboard请求参数结构体
    """

    def __init__(self):
        r"""仪表盘信息
        :param DashboardId: 仪表盘ID
        :type PathPrefix: String
        """
        self.DashboardId = None

    def _deserialize(self, params):
        if params.get("DashboardId"):
            self.DashboardId = params.get("DashboardId")


class ListDashboardsRequest(AbstractModel):
    """ListDashboards请求参数结构体
    """

    def __init__(self):
        r"""获取仪表盘列表
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param Page: 返回的分页数，从0开始
        :type PathPrefix: Int
        :param Size: 每页返回最大条目，默认 500（最大值）
        :type PathPrefix: Int
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


class CreateChartRequest(AbstractModel):
    """CreateChart请求参数结构体
    """

    def __init__(self):
        r"""创建图表
        :param DashboardId: 仪表盘ID
        :type PathPrefix: String
        :param ChartName: 图表名称
        :type PathPrefix: String
        :param ChartType: 图表类型，line，table
        :type PathPrefix: String
        :param Search: 查询主体
        :type PathPrefix: String
        :param Display: 展示参数
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param TimeRange: 查询数据的时间范围
        :type PathPrefix: String
        :param Query: 查询语句
        :type PathPrefix: String
        """
        self.DashboardId = None
        self.ChartName = None
        self.ChartType = None
        self.Search = None
        self.Display = None
        self.LogPoolName = None
        self.TimeRange = None
        self.Query = None

    def _deserialize(self, params):
        if params.get("DashboardId"):
            self.DashboardId = params.get("DashboardId")
        if params.get("ChartName"):
            self.ChartName = params.get("ChartName")
        if params.get("ChartType"):
            self.ChartType = params.get("ChartType")
        if params.get("Search"):
            self.Search = params.get("Search")
        if params.get("Display"):
            self.Display = params.get("Display")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("TimeRange"):
            self.TimeRange = params.get("TimeRange")
        if params.get("Query"):
            self.Query = params.get("Query")


class DeleteChartRequest(AbstractModel):
    """DeleteChart请求参数结构体
    """

    def __init__(self):
        r"""删除图表
        :param ChartId: 图表ID
        :type PathPrefix: String
        """
        self.ChartId = None

    def _deserialize(self, params):
        if params.get("ChartId"):
            self.ChartId = params.get("ChartId")


class GetDashboardNamesByIdsRequest(AbstractModel):
    """GetDashboardNamesByIds请求参数结构体
    """

    def __init__(self):
        r"""获取仪表盘名称
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param DashboardIds: 仪表盘id列表
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.DashboardIds = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("DashboardIds"):
            self.DashboardIds = params.get("DashboardIds")


class GetChartNamesByIdsRequest(AbstractModel):
    """GetChartNamesByIds请求参数结构体
    """

    def __init__(self):
        r"""获取图表名称
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param ChartIds: 图表id列表
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.ChartIds = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("ChartIds"):
            self.ChartIds = params.get("ChartIds")


class UpdateDashboardRequest(AbstractModel):
    """UpdateDashboard请求参数结构体
    """

    def __init__(self):
        r"""修改仪表盘
        :param DashboardId: 仪表盘ID
        :type PathPrefix: String
        :param DashboardName: 仪表盘名称
        :type PathPrefix: String
        """
        self.DashboardId = None
        self.DashboardName = None

    def _deserialize(self, params):
        if params.get("DashboardId"):
            self.DashboardId = params.get("DashboardId")
        if params.get("DashboardName"):
            self.DashboardName = params.get("DashboardName")


class GetUsageRequest(AbstractModel):
    """GetUsage请求参数结构体
    """

    def __init__(self):
        r"""获取监控
        :param Projects: 工程名称列表
        :type PathPrefix: String
        :param Metrics: 指标名称列表，不传返回所有；WriteFlow，ReadFlow，Storage，SearchRequests，WriteRequests
        :type PathPrefix: String
        :param From: 开始时间戳
        :type PathPrefix: String
        :param To: 结束时间戳
        :type PathPrefix: String
        """
        self.Projects = None
        self.Metrics = None
        self.From = None
        self.To = None

    def _deserialize(self, params):
        if params.get("Projects"):
            self.Projects = params.get("Projects")
        if params.get("Metrics"):
            self.Metrics = params.get("Metrics")
        if params.get("From"):
            self.From = params.get("From")
        if params.get("To"):
            self.To = params.get("To")


class SetIndexTemplateRequest(AbstractModel):
    """SetIndexTemplate请求参数结构体
    """

    def __init__(self):
        r"""配置索引规则
        :param ProjectName: 工程名称
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param IndexStatus: 是否启用索引
        :type PathPrefix: Boolean
        :param FullTextIndex: 全文检索的配置项，包括区分大小写、分词符
        :type PathPrefix: String
        :param IndexFields: 字段索引配置项
        :type PathPrefix: String
        :param Lowercase: true表示索引不区分大小写，false表示索引区分大小写
        :type PathPrefix: Boolean
        :param Separator: 分词符
        :type PathPrefix: String
        :param FieldName: 字段名称
        :type PathPrefix: String
        :param FieldType: 数据类型,包括text、Int、double、date类型
        :type PathPrefix: String
        :param FieldAlias: 字段别名
        :type PathPrefix: String
        :param SeparatorStatus: 是否开启分词符
        :type PathPrefix: Boolean
        """
        self.ProjectName = None
        self.LogPoolName = None
        self.IndexStatus = None
        self.FullTextIndex = None
        self.IndexFields = None
        self.Lowercase = None
        self.Separator = None
        self.FieldName = None
        self.FieldType = None
        self.FieldAlias = None
        self.SeparatorStatus = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("IndexStatus"):
            self.IndexStatus = params.get("IndexStatus")
        if params.get("FullTextIndex"):
            self.FullTextIndex = params.get("FullTextIndex")
        if params.get("IndexFields"):
            self.IndexFields = params.get("IndexFields")
        if params.get("Lowercase"):
            self.Lowercase = params.get("Lowercase")
        if params.get("Separator"):
            self.Separator = params.get("Separator")
        if params.get("FieldName"):
            self.FieldName = params.get("FieldName")
        if params.get("FieldType"):
            self.FieldType = params.get("FieldType")
        if params.get("FieldAlias"):
            self.FieldAlias = params.get("FieldAlias")
        if params.get("SeparatorStatus"):
            self.SeparatorStatus = params.get("SeparatorStatus")


class GetIndexTemplateRequest(AbstractModel):
    """GetIndexTemplate请求参数结构体
    """

    def __init__(self):
        r"""获取当前用户已经设置的索引配置
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


class CreateDownloadTaskRequest(AbstractModel):
    """CreateDownloadTask请求参数结构体
    """

    def __init__(self):
        r"""创建下载任务
        :param From: 日志起始时间
        :type PathPrefix: String
        :param To: 日志截止时间，时间跨度不能超过24小时
        :type PathPrefix: String
        :param LogPoolName: 日志池名称
        :type PathPrefix: String
        :param ProjectName: 工程名称
        :type PathPrefix: String
        """
        self.From = None
        self.To = None
        self.LogPoolName = None
        self.ProjectName = None

    def _deserialize(self, params):
        if params.get("From"):
            self.From = params.get("From")
        if params.get("To"):
            self.To = params.get("To")
        if params.get("LogPoolName"):
            self.LogPoolName = params.get("LogPoolName")
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")


class ListDownloadTasksRequest(AbstractModel):
    """ListDownloadTasks请求参数结构体
    """

    def __init__(self):
        r"""列举下载任务
        :param Page: 页码
        :type PathPrefix: String
        :param Size: 每页大小
        :type PathPrefix: String
        :param ProjectName: 工程名称
        :type PathPrefix: String
        """
        self.Page = None
        self.Size = None
        self.ProjectName = None

    def _deserialize(self, params):
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")


class GetDownloadUrlsRequest(AbstractModel):
    """GetDownloadUrls请求参数结构体
    """

    def __init__(self):
        r"""获取下载Url
        :param DownloadID: 任务下载ID，通过获取下载任务列表获取
        :type PathPrefix: String
        :param ProjectName: 工程名称
        :type PathPrefix: String
        """
        self.DownloadID = None
        self.ProjectName = None

    def _deserialize(self, params):
        if params.get("DownloadID"):
            self.DownloadID = params.get("DownloadID")
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData请求参数结构体
    """

    def __init__(self):
        r"""获取监控数据
        """

    def _deserialize(self, params):
        return


class DescribeLogErrorReasonRequest(AbstractModel):
    """DescribeLogErrorReason请求参数结构体
    """

    def __init__(self):
        r"""获取日志数据错误原因
        """

    def _deserialize(self, params):
        return


class DeleteEtlTaskRequest(AbstractModel):
    """DeleteEtlTask请求参数结构体
    """

    def __init__(self):
        r"""删除加工任务
        """

    def _deserialize(self, params):
        return


class StopEtlTaskRequest(AbstractModel):
    """StopEtlTask请求参数结构体
    """

    def __init__(self):
        r"""停止加工任务
        """

    def _deserialize(self, params):
        return


class StartEtlTaskRequest(AbstractModel):
    """StartEtlTask请求参数结构体
    """

    def __init__(self):
        r"""开始加工任务
        """

    def _deserialize(self, params):
        return


class ListEtlTasksRequest(AbstractModel):
    """ListEtlTasks请求参数结构体
    """

    def __init__(self):
        r"""查询加工任务列表
        """

    def _deserialize(self, params):
        return


class DescribeEtlTaskRequest(AbstractModel):
    """DescribeEtlTask请求参数结构体
    """

    def __init__(self):
        r"""查询加工任务详情
        """

    def _deserialize(self, params):
        return


class ModifyEtlTaskRequest(AbstractModel):
    """ModifyEtlTask请求参数结构体
    """

    def __init__(self):
        r"""修改加工任务
        """

    def _deserialize(self, params):
        return


class CreateEtlTaskRequest(AbstractModel):
    """CreateEtlTask请求参数结构体
    """

    def __init__(self):
        r"""创建加工任务
        """

    def _deserialize(self, params):
        return


class DescribeEtlExceptionRequest(AbstractModel):
    """DescribeEtlException请求参数结构体
    """

    def __init__(self):
        r"""获取加工任务异常详情
        """

    def _deserialize(self, params):
        return


class DescribeEtlStatsRequest(AbstractModel):
    """DescribeEtlStats请求参数结构体
    """

    def __init__(self):
        r"""获取加工任务指标统计
        """

    def _deserialize(self, params):
        return


class ExecuteEtlDemoRequest(AbstractModel):
    """ExecuteEtlDemo请求参数结构体
    """

    def __init__(self):
        r"""执行加工函数预览
        """

    def _deserialize(self, params):
        return


class GetUserRegionRequest(AbstractModel):
    """GetUserRegion请求参数结构体
    """

    def __init__(self):
        r"""获取region
        """

    def _deserialize(self, params):
        return


class GetClustersByTypeRequest(AbstractModel):
    """GetClustersByType请求参数结构体
    """

    def __init__(self):
        r"""根据类型获取集群列表
        """

    def _deserialize(self, params):
        return


