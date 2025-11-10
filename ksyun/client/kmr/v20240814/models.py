from ksyun.common.abstract_model import AbstractModel

class DetailWorkspaceRequest(AbstractModel):
    """DetailWorkspace请求参数结构体
    """

    def __init__(self):
        r"""获取工作空间详情
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        """
        self.WorkspaceId = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")


class ListWorkspacesRequest(AbstractModel):
    """ListWorkspaces请求参数结构体
    """

    def __init__(self):
        r"""获取工作空间列表
        :param NameOrId: 工作空间名称/ID
        :type PathPrefix: String
        :param Status: 工作空间状态
RUNNING：运行中
TERMINATED：已删除
FREEZE：冻结中
        :type PathPrefix: Array
        :param PageNumber: 分页页码
        :type PathPrefix: Int
        :param PageSize: 分页大小
        :type PathPrefix: Int
        """
        self.NameOrId = None
        self.Status = None
        self.PageNumber = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("NameOrId"):
            self.NameOrId = params.get("NameOrId")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class StartJobRunRequest(AbstractModel):
    """StartJobRun请求参数结构体
    """

    def __init__(self):
        r"""提交Spark作业
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param AccessKeyId: AK
用于API请求认证
        :type PathPrefix: String
        :param AccessKeySecret: SK
用于API请求认证

        :type PathPrefix: String
        :param ReleaseVersion: Spark版本
        :type PathPrefix: String
        :param SparkSubmitData: 
        :type PathPrefix: Object
        """
        self.WorkspaceId = None
        self.AccessKeyId = None
        self.AccessKeySecret = None
        self.ReleaseVersion = None
        self.SparkSubmitData = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("AccessKeyId"):
            self.AccessKeyId = params.get("AccessKeyId")
        if params.get("AccessKeySecret"):
            self.AccessKeySecret = params.get("AccessKeySecret")
        if params.get("ReleaseVersion"):
            self.ReleaseVersion = params.get("ReleaseVersion")
        if params.get("SparkSubmitData"):
            self.SparkSubmitData = params.get("SparkSubmitData")


class GetJobRunRequest(AbstractModel):
    """GetJobRun请求参数结构体
    """

    def __init__(self):
        r"""获取Spark作业详情
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunId: 作业ID
        :type PathPrefix: String
        """
        self.WorkspaceId = None
        self.JobRunId = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunId"):
            self.JobRunId = params.get("JobRunId")


class ListJobRunsRequest(AbstractModel):
    """ListJobRuns请求参数结构体
    """

    def __init__(self):
        r"""获取Spark作业信息列表
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param MaxResults: 查询返回的最大记录数

        :type PathPrefix: Int
        """
        self.WorkspaceId = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class CancelJobRunRequest(AbstractModel):
    """CancelJobRun请求参数结构体
    """

    def __init__(self):
        r"""停止Spark作业运行
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunIds: 停止作业
支持批量停止
        :type PathPrefix: Array
        """
        self.WorkspaceId = None
        self.JobRunIds = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunIds"):
            self.JobRunIds = params.get("JobRunIds")


class ListExecutorRequest(AbstractModel):
    """ListExecutor请求参数结构体
    """

    def __init__(self):
        r"""获取作业Executor列表
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunId: 作业ID
        :type PathPrefix: String
        :param PageNumber: 请求页码
        :type PathPrefix: Int
        :param PageSize: 分页大小
        :type PathPrefix: Int
        """
        self.WorkspaceId = None
        self.JobRunId = None
        self.PageNumber = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunId"):
            self.JobRunId = params.get("JobRunId")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class StartRayJobRunRequest(AbstractModel):
    """StartRayJobRun请求参数结构体
    """

    def __init__(self):
        r"""提交Ray作业
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param AccessKeyId: AK
用于API请求认证
        :type PathPrefix: String
        :param AccessKeySecret: SK
用于API请求认证
        :type PathPrefix: String
        :param ReleaseVersion: Ray版本
        :type PathPrefix: String
        :param RaySubmitData: 
        :type PathPrefix: Object
        """
        self.WorkspaceId = None
        self.AccessKeyId = None
        self.AccessKeySecret = None
        self.ReleaseVersion = None
        self.RaySubmitData = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("AccessKeyId"):
            self.AccessKeyId = params.get("AccessKeyId")
        if params.get("AccessKeySecret"):
            self.AccessKeySecret = params.get("AccessKeySecret")
        if params.get("ReleaseVersion"):
            self.ReleaseVersion = params.get("ReleaseVersion")
        if params.get("RaySubmitData"):
            self.RaySubmitData = params.get("RaySubmitData")


class GetRayJobRunRequest(AbstractModel):
    """GetRayJobRun请求参数结构体
    """

    def __init__(self):
        r"""GetRayJobRun
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunId: 作业ID
        :type PathPrefix: String
        """
        self.WorkspaceId = None
        self.JobRunId = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunId"):
            self.JobRunId = params.get("JobRunId")


class ListRayJobRunsRequest(AbstractModel):
    """ListRayJobRuns请求参数结构体
    """

    def __init__(self):
        r"""ListRayJobRuns
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param NameOrId: 作业名称/ID
        :type PathPrefix: String
        :param Status: 筛选条件，作业状态
INIT：初始化
RUNNING：运行中
WAITING：等待中
DELETED：已停止
SUBMITTED：已提交
CREATED_FAILED：创建失败
        :type PathPrefix: Array
        :param PageNumber: 分页页码
        :type PathPrefix: Int
        :param PageSize: 分页大小
        :type PathPrefix: Int
        """
        self.WorkspaceId = None
        self.NameOrId = None
        self.Status = None
        self.PageNumber = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("NameOrId"):
            self.NameOrId = params.get("NameOrId")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class CancelRayJobRunRequest(AbstractModel):
    """CancelRayJobRun请求参数结构体
    """

    def __init__(self):
        r"""停止Ray作业运行
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunIds: 停止作业运行
支持批量停止
        :type PathPrefix: Array
        """
        self.WorkspaceId = None
        self.JobRunIds = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunIds"):
            self.JobRunIds = params.get("JobRunIds")


class StartFlinkJobRunRequest(AbstractModel):
    """StartFlinkJobRun请求参数结构体
    """

    def __init__(self):
        r"""提交Flink作业
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param AccessKeyId: 用于API请求认证
        :type PathPrefix: String
        :param AccessKeySecret: 用于API请求认证
        :type PathPrefix: String
        :param ReleaseVersion: Flink版本
        :type PathPrefix: String
        :param SubmitData: 
        :type PathPrefix: Object
        """
        self.WorkspaceId = None
        self.AccessKeyId = None
        self.AccessKeySecret = None
        self.ReleaseVersion = None
        self.SubmitData = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("AccessKeyId"):
            self.AccessKeyId = params.get("AccessKeyId")
        if params.get("AccessKeySecret"):
            self.AccessKeySecret = params.get("AccessKeySecret")
        if params.get("ReleaseVersion"):
            self.ReleaseVersion = params.get("ReleaseVersion")
        if params.get("SubmitData"):
            self.SubmitData = params.get("SubmitData")


class GetFlinkJobRunRequest(AbstractModel):
    """GetFlinkJobRun请求参数结构体
    """

    def __init__(self):
        r"""获取Flink作业详情
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunId: 作业ID
        :type PathPrefix: String
        """
        self.WorkspaceId = None
        self.JobRunId = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunId"):
            self.JobRunId = params.get("JobRunId")


class ListFlinkJobRunsRequest(AbstractModel):
    """ListFlinkJobRuns请求参数结构体
    """

    def __init__(self):
        r"""获取Flink作业列表
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param NameOrId: 作业名称或者作业ID
        :type PathPrefix: String
        :param Status: 工作空间状态的过滤条件
默认空展示全部
有效值：
RUNNING：运行中
COMPLETED：完成
INIT：初始化
DELETED：已删除
SUBMITTED：已提交
CREATED_FAILED：创建失败


        :type PathPrefix: Array
        :param PageNumber: 分页页码
        :type PathPrefix: Int
        :param PageSize: 分页页大小
        :type PathPrefix: Int
        """
        self.WorkspaceId = None
        self.NameOrId = None
        self.Status = None
        self.PageNumber = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("NameOrId"):
            self.NameOrId = params.get("NameOrId")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class CancelFlinkJobRunRequest(AbstractModel):
    """CancelFlinkJobRun请求参数结构体
    """

    def __init__(self):
        r"""停止Flink作业运行
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunIds: 
        :type PathPrefix: Array
        """
        self.WorkspaceId = None
        self.JobRunIds = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunIds"):
            self.JobRunIds = params.get("JobRunIds")


class SuspendFlinkJobRunRequest(AbstractModel):
    """SuspendFlinkJobRun请求参数结构体
    """

    def __init__(self):
        r"""挂起Flink作业
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunId: 作业ID
        :type PathPrefix: String
        """
        self.WorkspaceId = None
        self.JobRunId = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunId"):
            self.JobRunId = params.get("JobRunId")


class RestartFlinkJobRunRequest(AbstractModel):
    """RestartFlinkJobRun请求参数结构体
    """

    def __init__(self):
        r"""重启Flink作业
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param JobRunId: 作业ID
        :type PathPrefix: String
        """
        self.WorkspaceId = None
        self.JobRunId = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("JobRunId"):
            self.JobRunId = params.get("JobRunId")


class DescribeMetricListRequest(AbstractModel):
    """DescribeMetricList请求参数结构体
    """

    def __init__(self):
        r"""获取监控指标项
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param ProductType: 作业类型：flink，spark，ray
        :type PathPrefix: String
        """
        self.WorkspaceId = None
        self.ProductType = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")


class QueryMetricsRequest(AbstractModel):
    """QueryMetrics请求参数结构体
    """

    def __init__(self):
        r"""获取监控指标详情
        :param WorkspaceId: 工作空间ID
        :type PathPrefix: String
        :param ProductType: 作业类型：flink，spark，ray
        :type PathPrefix: String
        :param QueryData: 查询指标的详细信息
        :type PathPrefix: Object
        """
        self.WorkspaceId = None
        self.ProductType = None
        self.QueryData = None

    def _deserialize(self, params):
        if params.get("WorkspaceId"):
            self.WorkspaceId = params.get("WorkspaceId")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("QueryData"):
            self.QueryData = params.get("QueryData")


