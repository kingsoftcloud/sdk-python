from ksyun.common.abstract_model import AbstractModel

class CreateSandboxTemplateRequest(AbstractModel):
    """CreateSandboxTemplate请求参数结构体
    """

    def __init__(self):
        r"""创建沙箱模板
        :param TemplateName: 模板名称。长度1-40位，允许字母、中文、数字、顿号、-、_、.、\、/、(、)
        :type PathPrefix: String
        :param Description: 模板描述，0~200位，允许字母、中文、数字、空格及TemplateName所含特殊字符
        :type PathPrefix: String
        :param TemplateCategory: 模板类别。可选值：Public， Private
        :type PathPrefix: String
        :param TemplateType: 模板类型。可选值：All-in-one、Browser、CodeInterpreter、Custom。使用公共镜像时自动匹配实际类型
        :type PathPrefix: String
        :param Command: 启动命令，TemplateCategory为Private且ImageConfig.ImageSource不为Public时生效
        :type PathPrefix: String
        :param Cpu: CPU核数，最小1，默认2。TemplateCategory为Private时生效；KecConfig.KecEnable=true时自动覆盖为机型对应核数
        :type PathPrefix: Int
        :param Memory: 内存（GB），最小1，默认4。TemplateCategory为Private时生效；KecConfig.KecEnable=true时自动覆盖为机型对应内存
        :type PathPrefix: Int
        :param Ports: 监听端口，TemplateCategory为Private且ImageConfig.ImageSource不为Public时生效，默认[8000]，最多10个，范围1~65535
        :type PathPrefix: Array
        :param Envs: 环境变量列表。
        :type PathPrefix: Array
        :param ImageConfig: 镜像配置，TemplateCategory为Private时必填
        :type PathPrefix: Object
        :param SkillConfig: Skills能力配置，TemplateCategory为Public或ImageConfig.ImageSource为Public时生效
        :type PathPrefix: Object
        :param NetworkConfig: 网络访问配置，TemplateCategory为Private时必填

        :type PathPrefix: Object
        :param KlogConfig: 日志采集配置，TemplateCategory为Private时生效
        :type PathPrefix: Object
        :param KpfsMountConfig: KPFS存储挂载配置，TemplateCategory为Private时生效
        :type PathPrefix: Object
        :param Ks3MountConfig: KS3存储挂载配置，TemplateCategory为Private时生效
        :type PathPrefix: Object
        :param AccessKey: Access Key，Ks3MountConfig.Ks3Enable=true或KpfsMountConfig.KpfsEnable=true时必填
        :type PathPrefix: String
        :param SecretAccessKey: Secret Access Key，Ks3MountConfig.Ks3Enable=true或KpfsMountConfig.KpfsEnable=true时必填
        :type PathPrefix: String
        :param KecConfig: 云主机机型配置。TemplateCategory为Private时生效
        :type PathPrefix: Object
        :param PreheatConfig: 预热配置，TemplateCategory为Private时生效
        :type PathPrefix: Object
        :param InstanceQuota: 单模板沙箱实例上限，最小0，不传时动态分配，最大10
        :type PathPrefix: Int
        """
        self.TemplateName = None
        self.Description = None
        self.TemplateCategory = None
        self.TemplateType = None
        self.Command = None
        self.Cpu = None
        self.Memory = None
        self.Ports = None
        self.Envs = None
        self.ImageConfig = None
        self.SkillConfig = None
        self.NetworkConfig = None
        self.KlogConfig = None
        self.KpfsMountConfig = None
        self.Ks3MountConfig = None
        self.AccessKey = None
        self.SecretAccessKey = None
        self.KecConfig = None
        self.PreheatConfig = None
        self.InstanceQuota = None

    def _deserialize(self, params):
        if params.get("TemplateName"):
            self.TemplateName = params.get("TemplateName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("TemplateCategory"):
            self.TemplateCategory = params.get("TemplateCategory")
        if params.get("TemplateType"):
            self.TemplateType = params.get("TemplateType")
        if params.get("Command"):
            self.Command = params.get("Command")
        if params.get("Cpu"):
            self.Cpu = params.get("Cpu")
        if params.get("Memory"):
            self.Memory = params.get("Memory")
        if params.get("Ports"):
            self.Ports = params.get("Ports")
        if params.get("Envs"):
            self.Envs = params.get("Envs")
        if params.get("ImageConfig"):
            self.ImageConfig = params.get("ImageConfig")
        if params.get("SkillConfig"):
            self.SkillConfig = params.get("SkillConfig")
        if params.get("NetworkConfig"):
            self.NetworkConfig = params.get("NetworkConfig")
        if params.get("KlogConfig"):
            self.KlogConfig = params.get("KlogConfig")
        if params.get("KpfsMountConfig"):
            self.KpfsMountConfig = params.get("KpfsMountConfig")
        if params.get("Ks3MountConfig"):
            self.Ks3MountConfig = params.get("Ks3MountConfig")
        if params.get("AccessKey"):
            self.AccessKey = params.get("AccessKey")
        if params.get("SecretAccessKey"):
            self.SecretAccessKey = params.get("SecretAccessKey")
        if params.get("KecConfig"):
            self.KecConfig = params.get("KecConfig")
        if params.get("PreheatConfig"):
            self.PreheatConfig = params.get("PreheatConfig")
        if params.get("InstanceQuota"):
            self.InstanceQuota = params.get("InstanceQuota")


class UpdateSandboxTemplateRequest(AbstractModel):
    """UpdateSandboxTemplate请求参数结构体
    """

    def __init__(self):
        r"""更新沙箱模板
        :param TemplateId: 模板ID
        :type PathPrefix: String
        :param TemplateName: 模板名称。长度1-40位，允许字母、中文、数字、顿号、-、_、.、\、/、(、)
        :type PathPrefix: String
        :param Description: 模板描述。最长200位，允许字母、中文、数字、顿号、-、_、\、/、(、)、.、空格
        :type PathPrefix: String
        :param Envs: 环境变量列表
        :type PathPrefix: Array
        :param TemplateType: 模板类型。可选值：All-in-one、Browser、CodeInterpreter、Custom。使用公共镜像时自动匹配实际类型


        :type PathPrefix: String
        :param TemplateCategory: 模板类别。可选值：Public， Private


        :type PathPrefix: String
        :param Command: 启动命令，TemplateCategory为Private且ImageConfig.ImageSource不为Public时生效


        :type PathPrefix: String
        :param Ports: 监听端口，TemplateCategory为Private且ImageConfig.ImageSource不为Public时生效，默认[8000]，最多10个，范围1~65535


        :type PathPrefix: Array
        :param ImageConfig: 镜像配置，TemplateCategory为Private时有效


        :type PathPrefix: Object
        :param SkillConfig: Skills能力配置，TemplateCategory为Public或ImageConfig.ImageSource为Public时生效


        :type PathPrefix: Object
        :param NetworkConfig: 网络访问配置，TemplateCategory为Private时生效


        :type PathPrefix: Object
        :param KlogConfig: 日志采集配置，TemplateCategory为Private时生效


        :type PathPrefix: Object
        :param KpfsMountConfig: KPFS存储挂载配置，TemplateCategory为Private时生效


        :type PathPrefix: Object
        :param Ks3MountConfig: KS3存储挂载配置，TemplateCategory为Private时生效


        :type PathPrefix: Object
        :param AccessKey: Access Key

        :type PathPrefix: String
        :param SecretAccessKey: Secret Access Key
        :type PathPrefix: String
        :param KecConfig: 云主机机型配置。TemplateCategory为Private时生效
        :type PathPrefix: Object
        :param PreheatConfig: 预热配置，TemplateCategory为Private时生效


        :type PathPrefix: Object
        :param InstanceQuota: 单模板沙箱实例上限，最小0，不传时动态分配，最大10


        :type PathPrefix: Int
        :param Cpu: CPU核数，最小1，默认2。TemplateCategory为Private时生效；KecConfig.KecEnable=true时自动覆盖为机型对应核数
        :type PathPrefix: Int
        :param Memory: 内存（GB），最小1，默认4。TemplateCategory为Private时生效；KecConfig.KecEnable=true时自动覆盖为机型对应内存
        :type PathPrefix: Int
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.Envs = None
        self.TemplateType = None
        self.TemplateCategory = None
        self.Command = None
        self.Ports = None
        self.ImageConfig = None
        self.SkillConfig = None
        self.NetworkConfig = None
        self.KlogConfig = None
        self.KpfsMountConfig = None
        self.Ks3MountConfig = None
        self.AccessKey = None
        self.SecretAccessKey = None
        self.KecConfig = None
        self.PreheatConfig = None
        self.InstanceQuota = None
        self.Cpu = None
        self.Memory = None

    def _deserialize(self, params):
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")
        if params.get("TemplateName"):
            self.TemplateName = params.get("TemplateName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Envs"):
            self.Envs = params.get("Envs")
        if params.get("TemplateType"):
            self.TemplateType = params.get("TemplateType")
        if params.get("TemplateCategory"):
            self.TemplateCategory = params.get("TemplateCategory")
        if params.get("Command"):
            self.Command = params.get("Command")
        if params.get("Ports"):
            self.Ports = params.get("Ports")
        if params.get("ImageConfig"):
            self.ImageConfig = params.get("ImageConfig")
        if params.get("SkillConfig"):
            self.SkillConfig = params.get("SkillConfig")
        if params.get("NetworkConfig"):
            self.NetworkConfig = params.get("NetworkConfig")
        if params.get("KlogConfig"):
            self.KlogConfig = params.get("KlogConfig")
        if params.get("KpfsMountConfig"):
            self.KpfsMountConfig = params.get("KpfsMountConfig")
        if params.get("Ks3MountConfig"):
            self.Ks3MountConfig = params.get("Ks3MountConfig")
        if params.get("AccessKey"):
            self.AccessKey = params.get("AccessKey")
        if params.get("SecretAccessKey"):
            self.SecretAccessKey = params.get("SecretAccessKey")
        if params.get("KecConfig"):
            self.KecConfig = params.get("KecConfig")
        if params.get("PreheatConfig"):
            self.PreheatConfig = params.get("PreheatConfig")
        if params.get("InstanceQuota"):
            self.InstanceQuota = params.get("InstanceQuota")
        if params.get("Cpu"):
            self.Cpu = params.get("Cpu")
        if params.get("Memory"):
            self.Memory = params.get("Memory")


class DeleteSandboxInstanceRequest(AbstractModel):
    """DeleteSandboxInstance请求参数结构体
    """

    def __init__(self):
        r"""删除沙箱实例
        :param InstanceIds: 沙箱实例ID列表

        :type PathPrefix: Array
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class GetSandboxInstanceRequest(AbstractModel):
    """GetSandboxInstance请求参数结构体
    """

    def __init__(self):
        r"""获取沙箱实例信息
        :param InstanceId: 沙箱实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class GetSandboxInstanceListRequest(AbstractModel):
    """GetSandboxInstanceList请求参数结构体
    """

    def __init__(self):
        r"""查询沙箱实例列表
        :param TemplateId: 按模板ID筛选
        :type PathPrefix: String
        :param TemplateName: 按模板名称筛选
        :type PathPrefix: String
        :param PageNum: 页码，默认1，最小1
        :type PathPrefix: Int
        :param PageSize: 每页条数，默认10，最小1，最大100

        :type PathPrefix: Int
        """
        self.TemplateId = None
        self.TemplateName = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")
        if params.get("TemplateName"):
            self.TemplateName = params.get("TemplateName")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class GetSandboxTemplateListRequest(AbstractModel):
    """GetSandboxTemplateList请求参数结构体
    """

    def __init__(self):
        r"""查询沙箱模板列表
        :param TemplateType: 按模板类型筛选
        :type PathPrefix: String
        :param TemplateName: 按名称筛选
        :type PathPrefix: String
        :param PageNum: 页码，默认1，最小1
        :type PathPrefix: Int
        :param PageSize: 每页条数，默认10，最小1，最大100
        :type PathPrefix: Int
        """
        self.TemplateType = None
        self.TemplateName = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("TemplateType"):
            self.TemplateType = params.get("TemplateType")
        if params.get("TemplateName"):
            self.TemplateName = params.get("TemplateName")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class StartSandboxInstanceRequest(AbstractModel):
    """StartSandboxInstance请求参数结构体
    """

    def __init__(self):
        r"""启动沙箱实例
        :param TemplateId: 模板ID
        :type PathPrefix: String
        :param Timeout: 过期时间（秒），范围60-86400，默认3600
        :type PathPrefix: Int
        :param Ks3MountConfig: KS3存储挂载配置，同创建模板结构，可覆盖模板配置
        :type PathPrefix: Object
        :param KpfsMountConfig: KPFS存储挂载配置，同创建模板结构，可覆盖模板配置

        :type PathPrefix: Object
        :param AccessKey: Access Key，未传则使用模板绑定的AK/SK
        :type PathPrefix: String
        :param SecretAccessKey: Secret Access Key，未传则使用模板绑定的AK/SK

        :type PathPrefix: String
        :param Envs: 环境变量列表，同创建模板结构,覆盖模板中同名变量，新增变量一并注入
        :type PathPrefix: Array
        """
        self.TemplateId = None
        self.Timeout = None
        self.Ks3MountConfig = None
        self.KpfsMountConfig = None
        self.AccessKey = None
        self.SecretAccessKey = None
        self.Envs = None

    def _deserialize(self, params):
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("Ks3MountConfig"):
            self.Ks3MountConfig = params.get("Ks3MountConfig")
        if params.get("KpfsMountConfig"):
            self.KpfsMountConfig = params.get("KpfsMountConfig")
        if params.get("AccessKey"):
            self.AccessKey = params.get("AccessKey")
        if params.get("SecretAccessKey"):
            self.SecretAccessKey = params.get("SecretAccessKey")
        if params.get("Envs"):
            self.Envs = params.get("Envs")


class DeleteSandboxTemplateRequest(AbstractModel):
    """DeleteSandboxTemplate请求参数结构体
    """

    def __init__(self):
        r"""删除沙箱模板
        :param TemplateId: 模板ID
        :type PathPrefix: String
        """
        self.TemplateId = None

    def _deserialize(self, params):
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")


class GetSandboxTemplateRequest(AbstractModel):
    """GetSandboxTemplate请求参数结构体
    """

    def __init__(self):
        r"""获取沙箱模板详情
        :param TemplateId: 模板ID。
        :type PathPrefix: String
        """
        self.TemplateId = None

    def _deserialize(self, params):
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")


class GetPublicImageListRequest(AbstractModel):
    """GetPublicImageList请求参数结构体
    """

    def __init__(self):
        r"""获取公共镜像列表
        """

    def _deserialize(self, params):
        return


class UpdateSandboxInstanceRequest(AbstractModel):
    """UpdateSandboxInstance请求参数结构体
    """

    def __init__(self):
        r"""更新沙箱实例
        :param InstanceId: 沙箱实例Id
        :type PathPrefix: String
        :param Timeout: 修改后，实例销毁时间为"当前时刻"加"新设置的生命周期时长"。
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.Timeout = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")


class CreateImageCacheRequest(AbstractModel):
    """CreateImageCache请求参数结构体
    """

    def __init__(self):
        r"""创建镜像缓存
        :param ImageConfigs: 镜像配置列表，支持批量多镜像；每个元素对应一条缓存记录，单镜像也需使用数组
        :type PathPrefix: Filter
        """
        self.ImageConfigs = None

    def _deserialize(self, params):
        if params.get("ImageConfigs"):
            self.ImageConfigs = params.get("ImageConfigs")


class GetImageCacheListRequest(AbstractModel):
    """GetImageCacheList请求参数结构体
    """

    def __init__(self):
        r"""查询镜像缓存列表
        :param Scope: 列表范围：custom（自定义镜像缓存）或 public（公共镜像目录）
        :type PathPrefix: String
        :param ImageCacheId: 按镜像缓存ID进行包含式模糊查询
        :type PathPrefix: String
        :param Image: 按镜像地址过滤
        :type PathPrefix: String
        :param Description: 按镜像描述进行包含式模糊查询
        :type PathPrefix: String
        :param Status: 按镜像缓存状态过滤（底层暂不支持，待支持后生效）
        :type PathPrefix: String
        :param PageNum: 页码，从1开始
        :type PathPrefix: Int
        :param PageSize: 每页数量，范围1-100
        :type PathPrefix: Int
        """
        self.Scope = None
        self.ImageCacheId = None
        self.Image = None
        self.Description = None
        self.Status = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("Scope"):
            self.Scope = params.get("Scope")
        if params.get("ImageCacheId"):
            self.ImageCacheId = params.get("ImageCacheId")
        if params.get("Image"):
            self.Image = params.get("Image")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DeleteImageCacheRequest(AbstractModel):
    """DeleteImageCache请求参数结构体
    """

    def __init__(self):
        r"""删除镜像缓存
        :param ImageCacheId: 镜像缓存记录ID
        :type PathPrefix: String
        """
        self.ImageCacheId = None

    def _deserialize(self, params):
        if params.get("ImageCacheId"):
            self.ImageCacheId = params.get("ImageCacheId")


class CreateSandboxInstanceCommitRequest(AbstractModel):
    """CreateSandboxInstanceCommit请求参数结构体
    """

    def __init__(self):
        r"""创建沙箱镜像提交任务
        :param InstanceId: 沙箱实例ID
        :type PathPrefix: String
        :param Image: 目标镜像完整地址，包含仓库、名称和Tag
        :type PathPrefix: String
        :param RegistryUsername: 目标仓库用户名，必须与RegistryPassword同时提供或同时省略
        :type PathPrefix: String
        :param RegistryPassword: 目标仓库密码，仅用于此次请求，不写入数据库或响应
        :type PathPrefix: String
        :param Pause: 提交期间是否暂停容器，默认true
        :type PathPrefix: Boolean
        :param TimeoutSeconds: KCI提交任务超时秒数，范围60-7200，默认1800
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.Image = None
        self.RegistryUsername = None
        self.RegistryPassword = None
        self.Pause = None
        self.TimeoutSeconds = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Image"):
            self.Image = params.get("Image")
        if params.get("RegistryUsername"):
            self.RegistryUsername = params.get("RegistryUsername")
        if params.get("RegistryPassword"):
            self.RegistryPassword = params.get("RegistryPassword")
        if params.get("Pause"):
            self.Pause = params.get("Pause")
        if params.get("TimeoutSeconds"):
            self.TimeoutSeconds = params.get("TimeoutSeconds")


class GetSandboxInstanceCommitRequest(AbstractModel):
    """GetSandboxInstanceCommit请求参数结构体
    """

    def __init__(self):
        r"""查询沙箱镜像提交任务
        :param InstanceId: 沙箱实例ID
        :type PathPrefix: String
        :param TaskId: 提交任务ID
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


