from ksyun.common.abstract_model import AbstractModel

class ListInstancesRequest(AbstractModel):
    """ListInstances请求参数结构体
    """

    def __init__(self):
        r"""查询实例列表
        :param PageNumber: 当前页码 从0开始
        :type PathPrefix: Int
        :param PageSize: 当前页内数据的个数	
        :type PathPrefix: Int
        :param InstanceStatus: - “Running”: 集群当前正在运行并执行其任务。
- “Creating”: 集群正在创建或初始化中。
- “Upgrade”: 集群正在升级到更新的版本或配置。
- “Downgrade”: 集群正在降级到旧的版本或配置。
- “ScaleOut”: 集群正在通过增加更多资源或实例来扩展容量。
- “ScaleIn”: 集群正在通过移除资源或实例来缩减容量。
- “Restart”: 集群正在重启，通常是为了应用更新或从错误中恢复。
- “Reconfig”: 集群正在重新配置新的设置或参数。
- “Freezing”: 集群正在冻结或暂停中。
- “Freeze”: 集群当前已冻结或暂停。
- “CreateFailed”: 集群创建或初始化失败。
- “Terminated”: 集群已终止，不再运行。
- “Deleting”: 集群正在删除或移除中。
        :type PathPrefix: Array
        :param InstanceNameOrId: 实例名称或ID，用于标识特定的集群实例。
        :type PathPrefix: String
        """
        self.PageNumber = None
        self.PageSize = None
        self.InstanceStatus = None
        self.InstanceNameOrId = None

    def _deserialize(self, params):
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("InstanceStatus"):
            self.InstanceStatus = params.get("InstanceStatus")
        if params.get("InstanceNameOrId"):
            self.InstanceNameOrId = params.get("InstanceNameOrId")


class GetInstanceDetailRequest(AbstractModel):
    """GetInstanceDetail请求参数结构体
    """

    def __init__(self):
        r"""实例信息
        :param InstanceId: 实例ID，用于唯一标识一个实例
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class ModifyHostsRequest(AbstractModel):
    """ModifyHosts请求参数结构体
    """

    def __init__(self):
        r"""修改域名解析地址
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param TunaHosts: TunaHosts
        :type PathPrefix: Array
        """
        self.InstanceId = None
        self.TunaHosts = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TunaHosts"):
            self.TunaHosts = params.get("TunaHosts")


class ListAutoScaleHistoryRequest(AbstractModel):
    """ListAutoScaleHistory请求参数结构体
    """

    def __init__(self):
        r"""查看弹性伸缩策略历史
        :param InstanceId: 实例ID，用于唯一标识一个实例
        :type PathPrefix: String
        :param ExecAtStart: 执行时间范围的起始时间
        :type PathPrefix: String
        :param ExecAtEnd: 执行时间范围的结束时间
        :type PathPrefix: String
        :param PolicyName: 策略名称（左右模糊匹配）
        :type PathPrefix: String
        :param PageNumber: 页码，从0开始
        :type PathPrefix: Int
        :param PageSize: 每页记录数
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.ExecAtStart = None
        self.ExecAtEnd = None
        self.PolicyName = None
        self.PageNumber = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ExecAtStart"):
            self.ExecAtStart = params.get("ExecAtStart")
        if params.get("ExecAtEnd"):
            self.ExecAtEnd = params.get("ExecAtEnd")
        if params.get("PolicyName"):
            self.PolicyName = params.get("PolicyName")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class CreateAutoScalePolicyRequest(AbstractModel):
    """CreateAutoScalePolicy请求参数结构体
    """

    def __init__(self):
        r"""新增弹性伸缩策略
        :param InstanceId: 实例ID，用于唯一标识一个实例
        :type PathPrefix: String
        :param PolicyName: 策略名称
        :type PathPrefix: String
        :param ChargeType: 支持 Minutely (按量付费) 和 Daily (按量付费（按日月结）)
        :type PathPrefix: String
        :param ExecuteCycle: 支持如下参数：

- Daily 每天执行
- Weekly 每周特定天数
- Monthly 每月特定天数
- Once 仅执行一次
        :type PathPrefix: String
        :param ExecuteRules: 参数根据 ExecuteCycle 的不同而有所不同。请根据实际的执行周期传入对应的规则。
        :type PathPrefix: Object
        """
        self.InstanceId = None
        self.PolicyName = None
        self.ChargeType = None
        self.ExecuteCycle = None
        self.ExecuteRules = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("PolicyName"):
            self.PolicyName = params.get("PolicyName")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("ExecuteCycle"):
            self.ExecuteCycle = params.get("ExecuteCycle")
        if params.get("ExecuteRules"):
            self.ExecuteRules = params.get("ExecuteRules")


class ListAutoScalePolicyRequest(AbstractModel):
    """ListAutoScalePolicy请求参数结构体
    """

    def __init__(self):
        r"""查看弹性伸缩策略
        :param InstanceId: 实例ID，用于唯一标识一个实例
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DeleteAutoScalePolicyRequest(AbstractModel):
    """DeleteAutoScalePolicy请求参数结构体
    """

    def __init__(self):
        r"""删除弹性伸缩策略
        :param InstanceId: 实例ID，用于唯一标识一个实例
        :type PathPrefix: String
        :param PolicyId: 策略ID
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.PolicyId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("PolicyId"):
            self.PolicyId = params.get("PolicyId")


