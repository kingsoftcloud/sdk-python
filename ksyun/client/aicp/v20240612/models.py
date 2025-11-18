from ksyun.common.abstract_model import AbstractModel

class SaveNotebookImageRequest(AbstractModel):
    """SaveNotebookImage请求参数结构体
    """

    def __init__(self):
        r"""保存开发任务镜像
        :param ImageName: 镜像名称
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        :param ImageType: 镜像类型 Personal-个人版实例，Official-企业版实例
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param NamespacePermission: 命名空间权限，Public-公有 / Private-私有
        :type PathPrefix: String
        :param ImageRepo: 镜像仓库
        :type PathPrefix: String
        :param ImageVersion: 版本号
        :type PathPrefix: String
        :param OfficialInstance: 企业版实例ID，当ImageType=Official 必填
        :type PathPrefix: String
        :param UserName: 用户名
        :type PathPrefix: String
        :param Password: 密码
        :type PathPrefix: String
        :param ImagePermission: 可见性 Public- 公开可见 / Private-仅自己可见
        :type PathPrefix: String
        :param NotebookId: 开发任务ID
        :type PathPrefix: String
        :param ImageDomain: 镜像仓库域名(参数已废弃)
        :type PathPrefix: String
        """
        self.ImageName = None
        self.Description = None
        self.ImageType = None
        self.Namespace = None
        self.NamespacePermission = None
        self.ImageRepo = None
        self.ImageVersion = None
        self.OfficialInstance = None
        self.UserName = None
        self.Password = None
        self.ImagePermission = None
        self.NotebookId = None
        self.ImageDomain = None

    def _deserialize(self, params):
        if params.get("ImageName"):
            self.ImageName = params.get("ImageName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ImageType"):
            self.ImageType = params.get("ImageType")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("NamespacePermission"):
            self.NamespacePermission = params.get("NamespacePermission")
        if params.get("ImageRepo"):
            self.ImageRepo = params.get("ImageRepo")
        if params.get("ImageVersion"):
            self.ImageVersion = params.get("ImageVersion")
        if params.get("OfficialInstance"):
            self.OfficialInstance = params.get("OfficialInstance")
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("ImagePermission"):
            self.ImagePermission = params.get("ImagePermission")
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")
        if params.get("ImageDomain"):
            self.ImageDomain = params.get("ImageDomain")


class ModifyNotebookRequest(AbstractModel):
    """ModifyNotebook请求参数结构体
    """

    def __init__(self):
        r"""修改开发任务
        :param NotebookId: 开发任务ID
        :type PathPrefix: String
        :param NotebookName: 名称
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        :param ImageId: 镜像ID
        :type PathPrefix: String
        :param QueueName: 队列名称
        :type PathPrefix: String
        :param GPUType: GPU类型
        :type PathPrefix: String
        :param GPUNumber: GPU核数，允许范围为0~10000
        :type PathPrefix: Int
        :param CPUNum: Cpu数量，允许范围为0~10000
        :type PathPrefix: Int
        :param Memory: 内存G，允许范围为0~10000	
        :type PathPrefix: Int
        :param AccessType: 可见范围:
• Creator ：仅实例创建者可见
• QueueMember ：队列内成员可见

        :type PathPrefix: String
        :param EnablePublicNetworkSsh: 是否开启公网SSH访问模式，当EnableSsh=true时可设置该参数
        :type PathPrefix: Boolean
        :param SshAuthorizedKeys: SSH公钥，当EnableSsh=true时必传该参数
        :type PathPrefix: String
        :param StorageConfigs: 存储配置列表
（覆盖修改，需要传入全量的配置列表）
        :type PathPrefix: Array
        :param ServiceConfigs: 服务开放端口列表
        :type PathPrefix: Array
        :param AutoSave: 
        :type PathPrefix: Boolean
        :param RunOnCPU: 仅调度CPU
        :type PathPrefix: String
        :param EnableSSH: 是否开启SSH访问
        :type PathPrefix: String
        :param SSHPort: SSH端口，范围为1~65535
        :type PathPrefix: Int
        :param SSHAuthorizedKeys: SSH公钥，当EnableSsh=true时必传该参数
        :type PathPrefix: String
        :param EnablePublicNetworkSSH: 是否开启公网SSH访问模式，当EnableSsh=true时可设置该参数
        :type PathPrefix: Boolean
        :param AllocationId: 弹性IP ID，当EnablePublicNetworkSsh=true时，此参数必传
        :type PathPrefix: String
        :param ImageTagId: 第三方镜像tagId
        :type PathPrefix: String
        :param ImageSource: 镜像来源，当改变镜像来源时，需传入该值。
- Official 官方镜像
- Personal 个人镜像
- ThirdParty 第三方镜像

当修改镜像类型为第三方镜像时，需同时传入"ImageRegistryId", "ImageRepoId", "ImageTagId"三个入参

        :type PathPrefix: String
        :param ImageRepoId: 第三方镜像仓库ID
        :type PathPrefix: String
        :param ImageRegistryId: 第三方镜像ID
        :type PathPrefix: String
        """
        self.NotebookId = None
        self.NotebookName = None
        self.Description = None
        self.ImageId = None
        self.QueueName = None
        self.GPUType = None
        self.GPUNumber = None
        self.CPUNum = None
        self.Memory = None
        self.AccessType = None
        self.EnablePublicNetworkSsh = None
        self.SshAuthorizedKeys = None
        self.StorageConfigs = None
        self.ServiceConfigs = None
        self.AutoSave = None
        self.RunOnCPU = None
        self.EnableSSH = None
        self.SSHPort = None
        self.SSHAuthorizedKeys = None
        self.EnablePublicNetworkSSH = None
        self.AllocationId = None
        self.ImageTagId = None
        self.ImageSource = None
        self.ImageRepoId = None
        self.ImageRegistryId = None

    def _deserialize(self, params):
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")
        if params.get("NotebookName"):
            self.NotebookName = params.get("NotebookName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("QueueName"):
            self.QueueName = params.get("QueueName")
        if params.get("GPUType"):
            self.GPUType = params.get("GPUType")
        if params.get("GPUNumber"):
            self.GPUNumber = params.get("GPUNumber")
        if params.get("CPUNum"):
            self.CPUNum = params.get("CPUNum")
        if params.get("Memory"):
            self.Memory = params.get("Memory")
        if params.get("AccessType"):
            self.AccessType = params.get("AccessType")
        if params.get("EnablePublicNetworkSsh"):
            self.EnablePublicNetworkSsh = params.get("EnablePublicNetworkSsh")
        if params.get("SshAuthorizedKeys"):
            self.SshAuthorizedKeys = params.get("SshAuthorizedKeys")
        if params.get("StorageConfigs"):
            self.StorageConfigs = params.get("StorageConfigs")
        if params.get("ServiceConfigs"):
            self.ServiceConfigs = params.get("ServiceConfigs")
        if params.get("AutoSave"):
            self.AutoSave = params.get("AutoSave")
        if params.get("RunOnCPU"):
            self.RunOnCPU = params.get("RunOnCPU")
        if params.get("EnableSSH"):
            self.EnableSSH = params.get("EnableSSH")
        if params.get("SSHPort"):
            self.SSHPort = params.get("SSHPort")
        if params.get("SSHAuthorizedKeys"):
            self.SSHAuthorizedKeys = params.get("SSHAuthorizedKeys")
        if params.get("EnablePublicNetworkSSH"):
            self.EnablePublicNetworkSSH = params.get("EnablePublicNetworkSSH")
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")
        if params.get("ImageTagId"):
            self.ImageTagId = params.get("ImageTagId")
        if params.get("ImageSource"):
            self.ImageSource = params.get("ImageSource")
        if params.get("ImageRepoId"):
            self.ImageRepoId = params.get("ImageRepoId")
        if params.get("ImageRegistryId"):
            self.ImageRegistryId = params.get("ImageRegistryId")


class DeleteNotebookRequest(AbstractModel):
    """DeleteNotebook请求参数结构体
    """

    def __init__(self):
        r"""删除开发任务
        :param NotebookId: 开发任务ID
        :type PathPrefix: String
        """
        self.NotebookId = None

    def _deserialize(self, params):
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")


class DescribeNotebooksRequest(AbstractModel):
    """DescribeNotebooks请求参数结构体
    """

    def __init__(self):
        r"""查询开发任务
        :param NotebookId: 开发任务ID
        :type PathPrefix: Filter
        :param Name: 开发任务名称
        :type PathPrefix: String
        :param Marker: 页数
        :type PathPrefix: Int
        :param MaxResults: 每页查询数目
        :type PathPrefix: Int
        :param State: 开发任务状态
        :type PathPrefix: String
        :param Filter: 条件过滤
        :type PathPrefix: Filter
        :param QueueId: 队列ID
        :type PathPrefix: String
        """
        self.NotebookId = None
        self.Name = None
        self.Marker = None
        self.MaxResults = None
        self.State = None
        self.Filter = None
        self.QueueId = None

    def _deserialize(self, params):
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("State"):
            self.State = params.get("State")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("QueueId"):
            self.QueueId = params.get("QueueId")


class CreateNotebookRequest(AbstractModel):
    """CreateNotebook请求参数结构体
    """

    def __init__(self):
        r"""创建开发任务
        :param NotebookName: 任务名称
        :type PathPrefix: String
        :param Description: 描述信息
        :type PathPrefix: String
        :param ResourcePoolId: 资源池ID
        :type PathPrefix: String
        :param QueueName: 队列名称
        :type PathPrefix: String
        :param GPUType: GPU类型
        :type PathPrefix: String
        :param GPUNumber: GPU核数，允许范围为0~10000
        :type PathPrefix: Int
        :param CPUNum: Cpu数量，允许范围为0~10000
        :type PathPrefix: Int
        :param Memory: 内存G，允许范围为0~10000
        :type PathPrefix: Int
        :param AccessType: 可见范围，Creator(创建者可见)，QueueMember（队列成员可见）
        :type PathPrefix: String
        :param StorageConfigs: 存储配置列表
        :type PathPrefix: Array
        :param AutoSave: 是否自动保存镜像
        :type PathPrefix: Boolean
        :param ServiceConfigs: 开放服务端口列表
        :type PathPrefix: Array
        :param ImageSource: 镜像来源
- 官方镜像 Official
- 个人镜像 Personal
- 第三方镜 ThirdParty

当传入值为ThirdParty时，"ImageRegistryId", "ImageRepoId", "ImageTagId"必须传入
        :type PathPrefix: String
        :param ImageId: 镜像ID
当镜像来源为第三方来源时，此参数不传递，其他镜像来源，此参数为必填项
        :type PathPrefix: String
        :param ImageRegistryId: 仓库连接 Id
        :type PathPrefix: String
        :param ImageRepoId: 仓库 Id
        :type PathPrefix: String
        :param ImageTagId: tagId
        :type PathPrefix: String
        :param EnableSSH: 是否开启SSH
        :type PathPrefix: Boolean
        :param SSHAuthorizedKeys: SSH公钥，当EnableSsh=true时必传该参数
        :type PathPrefix: String
        :param SSHPort: SSH端口，默认为22，范围为1~65535
        :type PathPrefix: Int
        :param EnablePublicNetworkSSH: 是否开启公网SSH访问模式，当EnableSsh=true时可设置该参数
        :type PathPrefix: Boolean
        :param AllocationId: 弹性IP ID，当EnablePublicNetworkSsh=true时，此参数必传
        :type PathPrefix: String
        :param RunOnCPU: 开启后，仅调度CPU
        :type PathPrefix: String
        """
        self.NotebookName = None
        self.Description = None
        self.ResourcePoolId = None
        self.QueueName = None
        self.GPUType = None
        self.GPUNumber = None
        self.CPUNum = None
        self.Memory = None
        self.AccessType = None
        self.StorageConfigs = None
        self.AutoSave = None
        self.ServiceConfigs = None
        self.ImageSource = None
        self.ImageId = None
        self.ImageRegistryId = None
        self.ImageRepoId = None
        self.ImageTagId = None
        self.EnableSSH = None
        self.SSHAuthorizedKeys = None
        self.SSHPort = None
        self.EnablePublicNetworkSSH = None
        self.AllocationId = None
        self.RunOnCPU = None

    def _deserialize(self, params):
        if params.get("NotebookName"):
            self.NotebookName = params.get("NotebookName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ResourcePoolId"):
            self.ResourcePoolId = params.get("ResourcePoolId")
        if params.get("QueueName"):
            self.QueueName = params.get("QueueName")
        if params.get("GPUType"):
            self.GPUType = params.get("GPUType")
        if params.get("GPUNumber"):
            self.GPUNumber = params.get("GPUNumber")
        if params.get("CPUNum"):
            self.CPUNum = params.get("CPUNum")
        if params.get("Memory"):
            self.Memory = params.get("Memory")
        if params.get("AccessType"):
            self.AccessType = params.get("AccessType")
        if params.get("StorageConfigs"):
            self.StorageConfigs = params.get("StorageConfigs")
        if params.get("AutoSave"):
            self.AutoSave = params.get("AutoSave")
        if params.get("ServiceConfigs"):
            self.ServiceConfigs = params.get("ServiceConfigs")
        if params.get("ImageSource"):
            self.ImageSource = params.get("ImageSource")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("ImageRegistryId"):
            self.ImageRegistryId = params.get("ImageRegistryId")
        if params.get("ImageRepoId"):
            self.ImageRepoId = params.get("ImageRepoId")
        if params.get("ImageTagId"):
            self.ImageTagId = params.get("ImageTagId")
        if params.get("EnableSSH"):
            self.EnableSSH = params.get("EnableSSH")
        if params.get("SSHAuthorizedKeys"):
            self.SSHAuthorizedKeys = params.get("SSHAuthorizedKeys")
        if params.get("SSHPort"):
            self.SSHPort = params.get("SSHPort")
        if params.get("EnablePublicNetworkSSH"):
            self.EnablePublicNetworkSSH = params.get("EnablePublicNetworkSSH")
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")
        if params.get("RunOnCPU"):
            self.RunOnCPU = params.get("RunOnCPU")


class StopNotebookRequest(AbstractModel):
    """StopNotebook请求参数结构体
    """

    def __init__(self):
        r"""停止开发任务
        :param NotebookId: 开发任务ID
        :type PathPrefix: String
        """
        self.NotebookId = None

    def _deserialize(self, params):
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")


class StartNotebookRequest(AbstractModel):
    """StartNotebook请求参数结构体
    """

    def __init__(self):
        r"""启动开发任务
        :param NotebookId: 开发任务ID
        :type PathPrefix: String
        """
        self.NotebookId = None

    def _deserialize(self, params):
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")


class GetWebIdeUrlRequest(AbstractModel):
    """GetWebIdeUrl请求参数结构体
    """

    def __init__(self):
        r"""获取开发任务连接地址
        :param NotebookId: 开发任务ID
        :type PathPrefix: String
        :param ExpirationMinute: 过期时间（分钟），默认时间是720分钟
        :type PathPrefix: String
        """
        self.NotebookId = None
        self.ExpirationMinute = None

    def _deserialize(self, params):
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")
        if params.get("ExpirationMinute"):
            self.ExpirationMinute = params.get("ExpirationMinute")


class DescribeNotebookEventsRequest(AbstractModel):
    """DescribeNotebookEvents请求参数结构体
    """

    def __init__(self):
        r"""查询开发任务事件列表
        :param NotebookId: 开发任务ID
        :type PathPrefix: String
        """
        self.NotebookId = None

    def _deserialize(self, params):
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")


class DescribeNotebookLogRequest(AbstractModel):
    """DescribeNotebookLog请求参数结构体
    """

    def __init__(self):
        r"""查看开发机日志
        """

    def _deserialize(self, params):
        return


class StopNotebookSavingImageRequest(AbstractModel):
    """StopNotebookSavingImage请求参数结构体
    """

    def __init__(self):
        r"""终止开发任务镜像保存
        :param NotebookId: 开发任务ID
        :type PathPrefix: String
        """
        self.NotebookId = None

    def _deserialize(self, params):
        if params.get("NotebookId"):
            self.NotebookId = params.get("NotebookId")


class CreateTrainJobRequest(AbstractModel):
    """CreateTrainJob请求参数结构体
    """

    def __init__(self):
        r"""创建训练任务
        :param TrainJobName: 训练任务名称，名称规范：1-64个字符，允许字母 中文 数字 - _ . / ( )
        :type PathPrefix: String
        :param Description: 训练任务描述信息 0-200字符
        :type PathPrefix: String
        :param ResourcePoolId: 资源池id
        :type PathPrefix: String
        :param QueueName: 队列名称
        :type PathPrefix: String
        :param Priority: 优先级
可选项：
• kaic-high 高 
• kaic-normal 中
• kaic-low 低
默认kaic-normal
        :type PathPrefix: String
        :param Command: 启动命令
        :type PathPrefix: String
        :param Framework: 训练框架
可选项：
• pytorch
• tensorflow
默认pytorch

        :type PathPrefix: String
        :param ImageSource: 镜像类型
可选项：
• Official 官方镜像
• Personal 自定义镜像
• ThirdParty 第三方镜像
        :type PathPrefix: String
        :param FrameworkReplicas: 框架副本配置
        :type PathPrefix: Object
        :param RestartPolicy: 重启策略，可选值：
· Always
· OnFailure
· Never
        :type PathPrefix: String
        :param Envs: 环境变量
        :type PathPrefix: Array
        :param SupportTensorboard: 是否开启Tensorboard，默认不开启
        :type PathPrefix: Boolean
        :param ImageId: 镜像ID
        :type PathPrefix: String
        :param ImageRegistryId: 镜像仓库id
        :type PathPrefix: String
        :param ImageRepoId: 镜像RepoId
        :type PathPrefix: String
        :param ImageTagId: 镜像tagId
        :type PathPrefix: String
        :param GPUType: GPU卡型
        :type PathPrefix: String
        :param GPUNumber: 范围0-10000
        :type PathPrefix: Int
        :param CPUNum: 范围0-10000
        :type PathPrefix: Int
        :param Memory: 0-10000
        :type PathPrefix: Int
        :param StorageConfigs: 存储配置

        :type PathPrefix: Array
        :param AccessType: 任务可见性，可选：Creator|QueueMember 默认：Creator
        :type PathPrefix: String
        :param MaxRuntime: 运行时长0-240000,单位h
        :type PathPrefix: Int
        :param SelfHealing: 是否开启自愈，默认true
        :type PathPrefix: Boolean
        :param RunOnCPU: 任务是否仅运行在cpu节点上，默认false
        :type PathPrefix: Boolean
        """
        self.TrainJobName = None
        self.Description = None
        self.ResourcePoolId = None
        self.QueueName = None
        self.Priority = None
        self.Command = None
        self.Framework = None
        self.ImageSource = None
        self.FrameworkReplicas = None
        self.RestartPolicy = None
        self.Envs = None
        self.SupportTensorboard = None
        self.ImageId = None
        self.ImageRegistryId = None
        self.ImageRepoId = None
        self.ImageTagId = None
        self.GPUType = None
        self.GPUNumber = None
        self.CPUNum = None
        self.Memory = None
        self.StorageConfigs = None
        self.AccessType = None
        self.MaxRuntime = None
        self.SelfHealing = None
        self.RunOnCPU = None

    def _deserialize(self, params):
        if params.get("TrainJobName"):
            self.TrainJobName = params.get("TrainJobName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ResourcePoolId"):
            self.ResourcePoolId = params.get("ResourcePoolId")
        if params.get("QueueName"):
            self.QueueName = params.get("QueueName")
        if params.get("Priority"):
            self.Priority = params.get("Priority")
        if params.get("Command"):
            self.Command = params.get("Command")
        if params.get("Framework"):
            self.Framework = params.get("Framework")
        if params.get("ImageSource"):
            self.ImageSource = params.get("ImageSource")
        if params.get("FrameworkReplicas"):
            self.FrameworkReplicas = params.get("FrameworkReplicas")
        if params.get("RestartPolicy"):
            self.RestartPolicy = params.get("RestartPolicy")
        if params.get("Envs"):
            self.Envs = params.get("Envs")
        if params.get("SupportTensorboard"):
            self.SupportTensorboard = params.get("SupportTensorboard")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("ImageRegistryId"):
            self.ImageRegistryId = params.get("ImageRegistryId")
        if params.get("ImageRepoId"):
            self.ImageRepoId = params.get("ImageRepoId")
        if params.get("ImageTagId"):
            self.ImageTagId = params.get("ImageTagId")
        if params.get("GPUType"):
            self.GPUType = params.get("GPUType")
        if params.get("GPUNumber"):
            self.GPUNumber = params.get("GPUNumber")
        if params.get("CPUNum"):
            self.CPUNum = params.get("CPUNum")
        if params.get("Memory"):
            self.Memory = params.get("Memory")
        if params.get("StorageConfigs"):
            self.StorageConfigs = params.get("StorageConfigs")
        if params.get("AccessType"):
            self.AccessType = params.get("AccessType")
        if params.get("MaxRuntime"):
            self.MaxRuntime = params.get("MaxRuntime")
        if params.get("SelfHealing"):
            self.SelfHealing = params.get("SelfHealing")
        if params.get("RunOnCPU"):
            self.RunOnCPU = params.get("RunOnCPU")


class DescribeTrainJobEventsRequest(AbstractModel):
    """DescribeTrainJobEvents请求参数结构体
    """

    def __init__(self):
        r"""查询训练任务pod事件
        :param ResourcePoolId: 
        :type PathPrefix: String
        :param TrainJobId: 
        :type PathPrefix: String
        """
        self.ResourcePoolId = None
        self.TrainJobId = None

    def _deserialize(self, params):
        if params.get("ResourcePoolId"):
            self.ResourcePoolId = params.get("ResourcePoolId")
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")


class StopTrainJobRequest(AbstractModel):
    """StopTrainJob请求参数结构体
    """

    def __init__(self):
        r"""关停训练任务
        :param TrainJobId: 训练任务Id
        :type PathPrefix: String
        """
        self.TrainJobId = None

    def _deserialize(self, params):
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")


class DescribeTrainJobRequest(AbstractModel):
    """DescribeTrainJob请求参数结构体
    """

    def __init__(self):
        r"""查询训练任务
        :param TrainJobId: 训练任务Id,多个TrainJobId.1=xx& TrainJobId.2=xx 
        :type PathPrefix: Filter
        :param Filter: 
        :type PathPrefix: Filter
        :param Marker: 分页参数
        :type PathPrefix: Int
        :param MaxResults: 返回最大值，默认1000
        :type PathPrefix: Int
        """
        self.TrainJobId = None
        self.Filter = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class StartTrainJobRequest(AbstractModel):
    """StartTrainJob请求参数结构体
    """

    def __init__(self):
        r"""开启训练任务
        :param TrainJobId: 
        :type PathPrefix: String
        """
        self.TrainJobId = None

    def _deserialize(self, params):
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")


class DeleteTrainJobRequest(AbstractModel):
    """DeleteTrainJob请求参数结构体
    """

    def __init__(self):
        r"""删除训练任务
        :param TrainJobId: 训练任务Id
        :type PathPrefix: String
        """
        self.TrainJobId = None

    def _deserialize(self, params):
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")


class ModifyTrainJobRequest(AbstractModel):
    """ModifyTrainJob请求参数结构体
    """

    def __init__(self):
        r"""修改训练任务
        :param TrainJobId: 训练任务Id
        :type PathPrefix: String
        :param Priority: 优先级，可选值：
 ·kaic-high
 ·kaic-normal
 ·kaic-low
        :type PathPrefix: String
        """
        self.TrainJobId = None
        self.Priority = None

    def _deserialize(self, params):
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")
        if params.get("Priority"):
            self.Priority = params.get("Priority")


class DescribeTrainJobPodLogsRequest(AbstractModel):
    """DescribeTrainJobPodLogs请求参数结构体
    """

    def __init__(self):
        r"""查询训练任务pod日志
        :param ResourcePoolId: 资源池Id
        :type PathPrefix: String
        :param TrainJobId: 训练任务ID
        :type PathPrefix: String
        :param PodName: PodName名称
        :type PathPrefix: String
        :param SinceSeconds: 秒，默认86400
        :type PathPrefix: Int
        :param TailLines: 行数
        :type PathPrefix: Int
        """
        self.ResourcePoolId = None
        self.TrainJobId = None
        self.PodName = None
        self.SinceSeconds = None
        self.TailLines = None

    def _deserialize(self, params):
        if params.get("ResourcePoolId"):
            self.ResourcePoolId = params.get("ResourcePoolId")
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")
        if params.get("PodName"):
            self.PodName = params.get("PodName")
        if params.get("SinceSeconds"):
            self.SinceSeconds = params.get("SinceSeconds")
        if params.get("TailLines"):
            self.TailLines = params.get("TailLines")


class DescribeTrainJobPodsRequest(AbstractModel):
    """DescribeTrainJobPods请求参数结构体
    """

    def __init__(self):
        r"""查询训练任务pod列表
        :param Marker: 
        :type PathPrefix: String
        :param MaxResults: 
        :type PathPrefix: String
        :param TrainJobId: 
        :type PathPrefix: String
        :param Filter: 
        :type PathPrefix: Filter
        """
        self.Marker = None
        self.MaxResults = None
        self.TrainJobId = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("TrainJobId"):
            self.TrainJobId = params.get("TrainJobId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


