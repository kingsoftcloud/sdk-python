from ksyun.common.abstract_model import AbstractModel

class GetReportRequest(AbstractModel):
    """GetReport请求参数结构体
    """

    def __init__(self):
        r"""下载巡检报告
        :param taskIDs: 要下载的巡检报告任务 ID 列表
        :type PathPrefix: Array
        :param startTime: 下载指定时间范围内的巡检报告
        :type PathPrefix: String
        :param endTime: 下载指定时间范围内的巡检报告
        :type PathPrefix: String
        """
        self.taskIDs = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        if params.get("taskIDs"):
            self.taskIDs = params.get("taskIDs")
        if params.get("startTime"):
            self.startTime = params.get("startTime")
        if params.get("endTime"):
            self.endTime = params.get("endTime")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体
    """

    def __init__(self):
        r"""发起巡检报告
        :param inspectionItemIDs: 要发起巡检的巡检项 ID 列表
        :type PathPrefix: Array
        :param productGroupIds: 要发起巡检的产品线 ID 列表
        :type PathPrefix: Array
        :param inspectionItemTypes: 要发起巡检的巡检维度列表
1 安全
2 可靠
3 性能
4 成本
5 限制
        :type PathPrefix: Array
        """
        self.inspectionItemIDs = None
        self.productGroupIds = None
        self.inspectionItemTypes = None

    def _deserialize(self, params):
        if params.get("inspectionItemIDs"):
            self.inspectionItemIDs = params.get("inspectionItemIDs")
        if params.get("productGroupIds"):
            self.productGroupIds = params.get("productGroupIds")
        if params.get("inspectionItemTypes"):
            self.inspectionItemTypes = params.get("inspectionItemTypes")


class ListInspectionItemRequest(AbstractModel):
    """ListInspectionItem请求参数结构体
    """

    def __init__(self):
        r"""查询巡检项列表
        :param pageNum: 分页数 最小值 1
        :type PathPrefix: Int
        :param pageSize: 分页大小，最小值 1，最大值 100
        :type PathPrefix: Int
        """
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        if params.get("pageNum"):
            self.pageNum = params.get("pageNum")
        if params.get("pageSize"):
            self.pageSize = params.get("pageSize")


