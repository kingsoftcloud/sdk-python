from ksyun.common.abstract_model import AbstractModel

class CreateTrainJobRequest(AbstractModel):
    """CreateTrainJob请求参数结构体
    """

    def __init__(self):
        r"""创建训练任务
        :param TrainJobName: 训练任务名称，名称规范：1-64个字符，允许字母 中文 数字 - _ . / ( )
        :type PathPrefix: String
        :param Description: 描述信息
        :type PathPrefix: String
        :param ResourcePoolId: 资源组ID
        :type PathPrefix: String
        :param Priority: 优先级
        :type PathPrefix: String
        :param QueueName: 队列名称
        :type PathPrefix: String
        :param Framework: 训练框架
        :type PathPrefix: String
        :param AccessType: 权限配置-可见范围
        :type PathPrefix: String
        :param SelfHealing: GPU故障自愈
        :type PathPrefix: Boolean
        :param MaxRuntimeHour: 最长运行时长(小时)
        :type PathPrefix: Int
        :param JobRunOnCPU: 节点亲和性-仅调度到CPU节点
        :type PathPrefix: Boolean
        :param SupportTensorboard: 开启Tensorboard
        :type PathPrefix: Boolean
        :param StorageConfigs: 存储配置信息
        :type PathPrefix: Array
        :param Roles: 角色资源配置信息
        :type PathPrefix: Array
        """
        self.TrainJobName = None
        self.Description = None
        self.ResourcePoolId = None
        self.Priority = None
        self.QueueName = None
        self.Framework = None
        self.AccessType = None
        self.SelfHealing = None
        self.MaxRuntimeHour = None
        self.JobRunOnCPU = None
        self.SupportTensorboard = None
        self.StorageConfigs = None
        self.Roles = None

    def _deserialize(self, params):
        if params.get("TrainJobName"):
            self.TrainJobName = params.get("TrainJobName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ResourcePoolId"):
            self.ResourcePoolId = params.get("ResourcePoolId")
        if params.get("Priority"):
            self.Priority = params.get("Priority")
        if params.get("QueueName"):
            self.QueueName = params.get("QueueName")
        if params.get("Framework"):
            self.Framework = params.get("Framework")
        if params.get("AccessType"):
            self.AccessType = params.get("AccessType")
        if params.get("SelfHealing"):
            self.SelfHealing = params.get("SelfHealing")
        if params.get("MaxRuntimeHour"):
            self.MaxRuntimeHour = params.get("MaxRuntimeHour")
        if params.get("JobRunOnCPU"):
            self.JobRunOnCPU = params.get("JobRunOnCPU")
        if params.get("SupportTensorboard"):
            self.SupportTensorboard = params.get("SupportTensorboard")
        if params.get("StorageConfigs"):
            self.StorageConfigs = params.get("StorageConfigs")
        if params.get("Roles"):
            self.Roles = params.get("Roles")


class DescribeTrainJobsRequest(AbstractModel):
    """DescribeTrainJobs请求参数结构体
    """

    def __init__(self):
        r"""查询训练任务
        :param TrainJobId: 多个训练任务的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param PageSize: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param Page: 页码
        :type PathPrefix: Int
        :param TrainJobName: 训练任务名称(支持模糊搜索)
        :type PathPrefix: String
        """
        self.TrainJobId = None
        self.Filter = None
        self.PageSize = None
        self.Page = None
        self.TrainJobName = None

    def _deserialize(self, params):
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("TrainJobName"):
            self.TrainJobName = params.get("TrainJobName")


