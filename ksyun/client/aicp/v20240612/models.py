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


class EnableApikeyStatusRequest(AbstractModel):
    """EnableApikeyStatus请求参数结构体
    """

    def __init__(self):
        r"""启用API Key
        :param KeyId: API Key的ID
        :type PathPrefix: String
        :param Status: 启禁用状态：1启用，2禁用
        :type PathPrefix: String
        """
        self.KeyId = None
        self.Status = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("Status"):
            self.Status = params.get("Status")


class ModifyApikeyRequest(AbstractModel):
    """ModifyApikey请求参数结构体
    """

    def __init__(self):
        r"""编辑API Key
        :param KeyId: 
        :type PathPrefix: String
        :param Name: API Key 名称
        :type PathPrefix: String
        :param Description: API Key 描述
        :type PathPrefix: String
        :param AssociatedModelIds: API Key 关联的模型列表
        :type PathPrefix: Array
        :param AllAssociatedModel: 是否全选
        :type PathPrefix: Boolean
        """
        self.KeyId = None
        self.Name = None
        self.Description = None
        self.AssociatedModelIds = None
        self.AllAssociatedModel = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("AssociatedModelIds"):
            self.AssociatedModelIds = params.get("AssociatedModelIds")
        if params.get("AllAssociatedModel"):
            self.AllAssociatedModel = params.get("AllAssociatedModel")


class ActivateApiServiceRequest(AbstractModel):
    """ActivateApiService请求参数结构体
    """

    def __init__(self):
        r"""开通模型API服务
        :param Status: 状态：1 表示开通服务
        :type PathPrefix: String
        """
        self.Status = None

    def _deserialize(self, params):
        if params.get("Status"):
            self.Status = params.get("Status")


class DeleteApikeyRequest(AbstractModel):
    """DeleteApikey请求参数结构体
    """

    def __init__(self):
        r"""删除API Key
        :param KeyId: KeyId，例如：API-KEY-1158133806039134208
        :type PathPrefix: String
        """
        self.KeyId = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")


class DescribeModelsRequest(AbstractModel):
    """DescribeModels请求参数结构体
    """

    def __init__(self):
        r"""查询模型列表(支持分页)
        :param Marker: 分页页码，从1开始
        :type PathPrefix: Int
        :param MaxResults: 分页页长，最大100
        :type PathPrefix: Int
        :param ModelCategory: 模型类别筛选项
        :type PathPrefix: Filter
        :param Provider: 模型供应商
        :type PathPrefix: Filter
        :param ContextLength: 模型上下文长度
1 - 128k及以下
2 - 128k到256k
3 - 256k以上
        :type PathPrefix: Filter
        :param ModelName: 模型名称关键词
        :type PathPrefix: String
        """
        self.Marker = None
        self.MaxResults = None
        self.ModelCategory = None
        self.Provider = None
        self.ContextLength = None
        self.ModelName = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("ModelCategory"):
            self.ModelCategory = params.get("ModelCategory")
        if params.get("Provider"):
            self.Provider = params.get("Provider")
        if params.get("ContextLength"):
            self.ContextLength = params.get("ContextLength")
        if params.get("ModelName"):
            self.ModelName = params.get("ModelName")


class CreateApikeyRequest(AbstractModel):
    """CreateApikey请求参数结构体
    """

    def __init__(self):
        r"""创建API Key
        :param Name: API Key 名称
        :type PathPrefix: String
        :param Description: API Key 描述
        :type PathPrefix: String
        :param ProjectId: 项目ID
        :type PathPrefix: Int
        :param AssociatedModelIds: 关联的模型列表
        :type PathPrefix: Array
        :param AllAssociatedModel: 是否全选
        :type PathPrefix: Boolean
        :param AllowedIps: IP白名单，空数组表示不设置白名单
        :type PathPrefix: Array
        """
        self.Name = None
        self.Description = None
        self.ProjectId = None
        self.AssociatedModelIds = None
        self.AllAssociatedModel = None
        self.AllowedIps = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("AssociatedModelIds"):
            self.AssociatedModelIds = params.get("AssociatedModelIds")
        if params.get("AllAssociatedModel"):
            self.AllAssociatedModel = params.get("AllAssociatedModel")
        if params.get("AllowedIps"):
            self.AllowedIps = params.get("AllowedIps")


class GetModelDetailRequest(AbstractModel):
    """GetModelDetail请求参数结构体
    """

    def __init__(self):
        r"""查询模型详情
        :param ModelId: 
        :type PathPrefix: String
        """
        self.ModelId = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")


class DescribeApikeysRequest(AbstractModel):
    """DescribeApikeys请求参数结构体
    """

    def __init__(self):
        r"""查询API Key列表（分页）
        :param Marker: 分页页码，从1开始
        :type PathPrefix: Int
        :param MaxResults: 每页条数，最多100
        :type PathPrefix: Int
        :param AssociatedModelId: 通过模型查关联的API Key
        :type PathPrefix: Filter
        :param Status: 按状态过滤查询
        :type PathPrefix: Filter
        :param Namekeyword: 名称搜索关键词
        :type PathPrefix: String
        :param DefaultKey: 是否默认只查默认Key
        :type PathPrefix: Boolean
        """
        self.Marker = None
        self.MaxResults = None
        self.AssociatedModelId = None
        self.Status = None
        self.Namekeyword = None
        self.DefaultKey = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("AssociatedModelId"):
            self.AssociatedModelId = params.get("AssociatedModelId")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("Namekeyword"):
            self.Namekeyword = params.get("Namekeyword")
        if params.get("DefaultKey"):
            self.DefaultKey = params.get("DefaultKey")


class QueryTokenDataRequest(AbstractModel):
    """QueryTokenData请求参数结构体
    """

    def __init__(self):
        r"""查询模型API token用量
        :param StartTimestamp: 开始时间，毫秒时间戳，仅支持最近180天内时间。
        :type PathPrefix: Int
        :param EndTimestamp: 截止时间，毫秒时间戳
        :type PathPrefix: Int
        :param MaxResults: 分页页长，最大10000
        :type PathPrefix: Int
        :param Keyword: 搜索关键词
        :type PathPrefix: String
        :param GroupBy: 分组字段：
model-按模型分组；keyId-按apikey分组。
        :type PathPrefix: String
        :param ReasoningType: 推理类型：normal-在线，batch-批量，web-在线体验，不传为查询全部。
        :type PathPrefix: String
        :param Marker: 页码，从1开始。
        :type PathPrefix: Int
        :param IsGlobalServer: 是否国际版：false-国内版，true-国际版
        :type PathPrefix: Boolean
        """
        self.StartTimestamp = None
        self.EndTimestamp = None
        self.MaxResults = None
        self.Keyword = None
        self.GroupBy = None
        self.ReasoningType = None
        self.Marker = None
        self.IsGlobalServer = None

    def _deserialize(self, params):
        if params.get("StartTimestamp"):
            self.StartTimestamp = params.get("StartTimestamp")
        if params.get("EndTimestamp"):
            self.EndTimestamp = params.get("EndTimestamp")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("GroupBy"):
            self.GroupBy = params.get("GroupBy")
        if params.get("ReasoningType"):
            self.ReasoningType = params.get("ReasoningType")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("IsGlobalServer"):
            self.IsGlobalServer = params.get("IsGlobalServer")


class DisableApikeyStatusRequest(AbstractModel):
    """DisableApikeyStatus请求参数结构体
    """

    def __init__(self):
        r"""禁用API Key
        :param KeyId: API Key的ID
        :type PathPrefix: String
        :param Status: 启禁用状态：1启用，2禁用
        :type PathPrefix: String
        """
        self.KeyId = None
        self.Status = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("Status"):
            self.Status = params.get("Status")


class GetApiServiceRequest(AbstractModel):
    """GetApiService请求参数结构体
    """

    def __init__(self):
        r"""查询API服务开通状态
        """

    def _deserialize(self, params):
        return


class GetBatchInferenceJobsFinalResultDownloadUrlRequest(AbstractModel):
    """GetBatchInferenceJobsFinalResultDownloadUrl请求参数结构体
    """

    def __init__(self):
        r"""查询批量推理任务最终结果下载链接
        :param BatchId: 
        :type PathPrefix: String
        """
        self.BatchId = None

    def _deserialize(self, params):
        if params.get("BatchId"):
            self.BatchId = params.get("BatchId")


class DescribeInferenceJobsKs3AuthInfoRequest(AbstractModel):
    """DescribeInferenceJobsKs3AuthInfo请求参数结构体
    """

    def __init__(self):
        r"""查询批量推理任务Ks3鉴权信息
        """

    def _deserialize(self, params):
        return


class StopBatchInferenceJobRequest(AbstractModel):
    """StopBatchInferenceJob请求参数结构体
    """

    def __init__(self):
        r"""终止批量推理任务
        :param BatchId: 
        :type PathPrefix: String
        """
        self.BatchId = None

    def _deserialize(self, params):
        if params.get("BatchId"):
            self.BatchId = params.get("BatchId")


class CreateBatchInferenceJobRequest(AbstractModel):
    """CreateBatchInferenceJob请求参数结构体
    """

    def __init__(self):
        r"""创建批量推理任务
        :param JobName: 
        :type PathPrefix: String
        :param JobDesc: 
        :type PathPrefix: String
        :param ApikeyId: 
        :type PathPrefix: String
        :param Model: 模型名，如：deepseek-r1-0528
        :type PathPrefix: String
        :param ExecuteTimeoutMs: 
        :type PathPrefix: Int
        :param InputDataType: 文件类型：user_ks3 用户ks3;upload_ks3 上传文件
        :type PathPrefix: String
        :param Ks3Region: 
        :type PathPrefix: String
        :param Ks3Ak: 
        :type PathPrefix: String
        :param Ks3Sk: 
        :type PathPrefix: String
        :param InBucket: 
        :type PathPrefix: String
        :param OutBucket: 
        :type PathPrefix: String
        :param InObjectName: 
        :type PathPrefix: String
        :param OutObjectName: 
        :type PathPrefix: String
        """
        self.JobName = None
        self.JobDesc = None
        self.ApikeyId = None
        self.Model = None
        self.ExecuteTimeoutMs = None
        self.InputDataType = None
        self.Ks3Region = None
        self.Ks3Ak = None
        self.Ks3Sk = None
        self.InBucket = None
        self.OutBucket = None
        self.InObjectName = None
        self.OutObjectName = None

    def _deserialize(self, params):
        if params.get("JobName"):
            self.JobName = params.get("JobName")
        if params.get("JobDesc"):
            self.JobDesc = params.get("JobDesc")
        if params.get("ApikeyId"):
            self.ApikeyId = params.get("ApikeyId")
        if params.get("Model"):
            self.Model = params.get("Model")
        if params.get("ExecuteTimeoutMs"):
            self.ExecuteTimeoutMs = params.get("ExecuteTimeoutMs")
        if params.get("InputDataType"):
            self.InputDataType = params.get("InputDataType")
        if params.get("Ks3Region"):
            self.Ks3Region = params.get("Ks3Region")
        if params.get("Ks3Ak"):
            self.Ks3Ak = params.get("Ks3Ak")
        if params.get("Ks3Sk"):
            self.Ks3Sk = params.get("Ks3Sk")
        if params.get("InBucket"):
            self.InBucket = params.get("InBucket")
        if params.get("OutBucket"):
            self.OutBucket = params.get("OutBucket")
        if params.get("InObjectName"):
            self.InObjectName = params.get("InObjectName")
        if params.get("OutObjectName"):
            self.OutObjectName = params.get("OutObjectName")


class ModifyBatchInferenceJobRequest(AbstractModel):
    """ModifyBatchInferenceJob请求参数结构体
    """

    def __init__(self):
        r"""更新批量推理任务（修改jobName和jobDesc）
        :param BatchId: 
        :type PathPrefix: String
        :param JobName: 
        :type PathPrefix: String
        :param JobDesc: 
        :type PathPrefix: String
        """
        self.BatchId = None
        self.JobName = None
        self.JobDesc = None

    def _deserialize(self, params):
        if params.get("BatchId"):
            self.BatchId = params.get("BatchId")
        if params.get("JobName"):
            self.JobName = params.get("JobName")
        if params.get("JobDesc"):
            self.JobDesc = params.get("JobDesc")


class DescribeBatchInferenceJobsRequest(AbstractModel):
    """DescribeBatchInferenceJobs请求参数结构体
    """

    def __init__(self):
        r"""查询批量推理任务(支持分页，按创建用户过滤)
        :param Marker: 页码，从1开始，默认是1
        :type PathPrefix: Int
        :param MaxResults: 页长，默认和最大都是100
        :type PathPrefix: Int
        :param JobNameKeyword: 任务名称模糊查询条件
        :type PathPrefix: String
        :param Status: 按状态过滤查询
init、queuing、running、terminated、completed、failed、timeout
        :type PathPrefix: Filter
        :param BatchId: 
        :type PathPrefix: String
        """
        self.Marker = None
        self.MaxResults = None
        self.JobNameKeyword = None
        self.Status = None
        self.BatchId = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("JobNameKeyword"):
            self.JobNameKeyword = params.get("JobNameKeyword")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("BatchId"):
            self.BatchId = params.get("BatchId")


class DeleteBatchInferenceJobRequest(AbstractModel):
    """DeleteBatchInferenceJob请求参数结构体
    """

    def __init__(self):
        r"""删除批量推理任务
        :param BatchId: 
        :type PathPrefix: String
        """
        self.BatchId = None

    def _deserialize(self, params):
        if params.get("BatchId"):
            self.BatchId = params.get("BatchId")


class EnableModelsRequest(AbstractModel):
    """EnableModels请求参数结构体
    """

    def __init__(self):
        r"""开通模型，支持批量
        :param ModelIds: 
        :type PathPrefix: Array
        """
        self.ModelIds = None

    def _deserialize(self, params):
        if params.get("ModelIds"):
            self.ModelIds = params.get("ModelIds")


class DescribeModelQuotasRequest(AbstractModel):
    """DescribeModelQuotas请求参数结构体
    """

    def __init__(self):
        r"""查询模型配额列表
        :param Marker: 分页页码，从1开始
        :type PathPrefix: Int
        :param MaxResults: 分页页长，最大100
        :type PathPrefix: Int
        :param Keyword: 模型搜索关键词
        :type PathPrefix: String
        :param Type: 文本模型/视觉模型
        :type PathPrefix: String
        """
        self.Marker = None
        self.MaxResults = None
        self.Keyword = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("Type"):
            self.Type = params.get("Type")


class DisableModelsRequest(AbstractModel):
    """DisableModels请求参数结构体
    """

    def __init__(self):
        r"""禁用对应模型
        :param ModelIds: 
        :type PathPrefix: Array
        """
        self.ModelIds = None

    def _deserialize(self, params):
        if params.get("ModelIds"):
            self.ModelIds = params.get("ModelIds")


class EnableOverFreeLimitRequest(AbstractModel):
    """EnableOverFreeLimit请求参数结构体
    """

    def __init__(self):
        r"""免费配额用完后禁用对应模型
        :param ModelIds: 
        :type PathPrefix: Array
        """
        self.ModelIds = None

    def _deserialize(self, params):
        if params.get("ModelIds"):
            self.ModelIds = params.get("ModelIds")


class DisableOverFreeLimitRequest(AbstractModel):
    """DisableOverFreeLimit请求参数结构体
    """

    def __init__(self):
        r"""即免费配额用完后继续使用计费配额
        :param ModelIds: 
        :type PathPrefix: Array
        """
        self.ModelIds = None

    def _deserialize(self, params):
        if params.get("ModelIds"):
            self.ModelIds = params.get("ModelIds")


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


class DescribeResourcePoolsRequest(AbstractModel):
    """DescribeResourcePools请求参数结构体
    """

    def __init__(self):
        r"""查询资源组列表
        :param Sort: 排序方式：默认倒序
- DESC 倒序
- ASC 正序
        :type PathPrefix: String
        :param Page: 页码
        :type PathPrefix: Int
        :param PageSize: 单次调用所返回的最大实例数目，默认1000， 范围[5-1000]。
        :type PathPrefix: Int
        :param ResourcePoolName: 资源池名称，可模糊匹配
        :type PathPrefix: String
        :param Component: 组件名称:
- spark
- ray
        :type PathPrefix: String
        :param ResourcePoolId: 资源组ID
        :type PathPrefix: Filter
        :param Filter: 一个或者多个过滤器
        :type PathPrefix: Filter
        """
        self.Sort = None
        self.Page = None
        self.PageSize = None
        self.ResourcePoolName = None
        self.Component = None
        self.ResourcePoolId = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("Sort"):
            self.Sort = params.get("Sort")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("ResourcePoolName"):
            self.ResourcePoolName = params.get("ResourcePoolName")
        if params.get("Component"):
            self.Component = params.get("Component")
        if params.get("ResourcePoolId"):
            self.ResourcePoolId = params.get("ResourcePoolId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class DescribeResourcePoolInstancesRequest(AbstractModel):
    """DescribeResourcePoolInstances请求参数结构体
    """

    def __init__(self):
        r"""查询资源组节点列表
        :param ResourcePoolId: 	
资源组d
        :type PathPrefix: String
        :param PageSize: 单次调用所返回的最大实例数目，默认1000, 范围值为[5, 1000]
        :type PathPrefix: Int
        :param Page: 页码
        :type PathPrefix: Int
        :param InstanceName: 实例名称，可模糊匹配


        :type PathPrefix: String
        :param InstanceId: 	
实例ID
        :type PathPrefix: Filter
        :param ProjectId: 项目制
        :type PathPrefix: Filter
        :param Filter: 一个或者多个过滤器
        :type PathPrefix: Filter
        """
        self.ResourcePoolId = None
        self.PageSize = None
        self.Page = None
        self.InstanceName = None
        self.InstanceId = None
        self.ProjectId = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("ResourcePoolId"):
            self.ResourcePoolId = params.get("ResourcePoolId")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class CreateInferenceEndpointRequest(AbstractModel):
    """CreateInferenceEndpoint请求参数结构体
    """

    def __init__(self):
        r"""创建接入点
        :param EndpointName: 推理接入点名称,1-64个字符，允许字母中文，数字，特殊字符-_、()
        :type PathPrefix: String
        :param ProjectId: 项目制Id
        :type PathPrefix: String
        :param ModelName: 默认绑定的模型名称
        :type PathPrefix: String
        :param RateLimit : 接入点限流配置
        :type PathPrefix: Object
        :param ModelId: ModelId 模型名称
        :type PathPrefix: String
        """
        self.EndpointName = None
        self.ProjectId = None
        self.ModelName = None
        self.RateLimit_ = None
        self.ModelId = None

    def _deserialize(self, params):
        if params.get("EndpointName"):
            self.EndpointName = params.get("EndpointName")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ModelName"):
            self.ModelName = params.get("ModelName")
        if params.get("RateLimit "):
            self.RateLimit_ = params.get("RateLimit ")
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")


class DescribeInferenceEndpointsRequest(AbstractModel):
    """DescribeInferenceEndpoints请求参数结构体
    """

    def __init__(self):
        r"""查询接入点
        :param EndpointId: 推理接入点 ID列表，范围为1-100
        :type PathPrefix: Filter
        :param EndpointName: 
        :type PathPrefix: String
        :param Marker: 
        :type PathPrefix: Int
        :param MaxResults: 
        :type PathPrefix: Int
        :param ProjectId: 
        :type PathPrefix: Filter
        :param Filter: 条件过滤，支持按照state状态和project过滤
        :type PathPrefix: Array
        """
        self.EndpointId = None
        self.EndpointName = None
        self.Marker = None
        self.MaxResults = None
        self.ProjectId = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("EndpointId"):
            self.EndpointId = params.get("EndpointId")
        if params.get("EndpointName"):
            self.EndpointName = params.get("EndpointName")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class StartInferenceEndpointRequest(AbstractModel):
    """StartInferenceEndpoint请求参数结构体
    """

    def __init__(self):
        r"""关闭接入点
        :param EndpointName: 推理接入点名称
        :type PathPrefix: String
        :param ProjectId: 项目制Id
        :type PathPrefix: String
        :param ModelName: 默认绑定的模型名称
        :type PathPrefix: String
        :param RateLimit : 接入点限流配置
        :type PathPrefix: Object
        :param EndpointId: 
        :type PathPrefix: String
        """
        self.EndpointName = None
        self.ProjectId = None
        self.ModelName = None
        self.RateLimit_ = None
        self.EndpointId = None

    def _deserialize(self, params):
        if params.get("EndpointName"):
            self.EndpointName = params.get("EndpointName")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ModelName"):
            self.ModelName = params.get("ModelName")
        if params.get("RateLimit "):
            self.RateLimit_ = params.get("RateLimit ")
        if params.get("EndpointId"):
            self.EndpointId = params.get("EndpointId")


class DeleteInferenceEndpointRequest(AbstractModel):
    """DeleteInferenceEndpoint请求参数结构体
    """

    def __init__(self):
        r"""删除接入点
        :param EndpointId: 
        :type PathPrefix: String
        """
        self.EndpointId = None

    def _deserialize(self, params):
        if params.get("EndpointId"):
            self.EndpointId = params.get("EndpointId")


class DisableEndpointRateLimitRequest(AbstractModel):
    """DisableEndpointRateLimit请求参数结构体
    """

    def __init__(self):
        r"""关闭接入点限流
        :param EndpointId: 
        :type PathPrefix: String
        """
        self.EndpointId = None

    def _deserialize(self, params):
        if params.get("EndpointId"):
            self.EndpointId = params.get("EndpointId")


