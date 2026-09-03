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
        :param Priority: 优先级，有效值：
- kaic-high 高优先级
- kaic-normal 中优先级
- kaic-low  低优先级
        :type PathPrefix: String
        :param QueueName: 队列名称
        :type PathPrefix: String
        :param Framework: 训练框架	，有效值：
- pytorch
- tensorflow
- custom
- ray
        :type PathPrefix: String
        :param AccessType: 权限配置-可见范围
        :type PathPrefix: String
        :param SelfHealing: 故障自愈
        :type PathPrefix: Boolean
        :param MaxRuntimeHour: 最长运行时长(小时)
        :type PathPrefix: Long
        :param JobRunOnCPU: 仅调度到CPU节点。当GPUNumber为空或值为0时，此值有效
        :type PathPrefix: Boolean
        :param SupportTensorboard: 开启Tensorboard
        :type PathPrefix: Boolean
        :param StorageConfigs: 存储配置信息
        :type PathPrefix: Array
        :param Roles: 角色资源配置信息
        :type PathPrefix: Array
        :param HoldingTimeMinutes: 实例保留时长（分钟）
        :type PathPrefix: Int
        :param EnableDeviceHealthCheck: 是否开启算力健康检测(只对pytorch框架生效)
        :type PathPrefix: Boolean
        :param DeviceHealthCheckConfig: 算力健康检测配置，pytorch框架下且EnableDeviceHealthCheck=true时生效
        :type PathPrefix: Object
        :param RuntimeEnv: 运行时环境配置（仅ray框架有效），必须是json字符串，且长度最大5000字符
        :type PathPrefix: String
        :param EntryPointCommand: ray框架下运行命令,当框架为ray时不能为空，其他框架忽略该参数
        :type PathPrefix: String
        :param UseIdleResource: 是否使用闲时资源，仅当所属队列开启借用AllowBorrowing时，支持开启
        :type PathPrefix: Boolean
        :param EnableRDMADepsCheck: 是否开启RDMA依赖包检测（只对pytorch框架生效）
        :type PathPrefix: Boolean
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
        self.HoldingTimeMinutes = None
        self.EnableDeviceHealthCheck = None
        self.DeviceHealthCheckConfig = None
        self.RuntimeEnv = None
        self.EntryPointCommand = None
        self.UseIdleResource = None
        self.EnableRDMADepsCheck = None

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
        if params.get("HoldingTimeMinutes"):
            self.HoldingTimeMinutes = params.get("HoldingTimeMinutes")
        if params.get("EnableDeviceHealthCheck"):
            self.EnableDeviceHealthCheck = params.get("EnableDeviceHealthCheck")
        if params.get("DeviceHealthCheckConfig"):
            self.DeviceHealthCheckConfig = params.get("DeviceHealthCheckConfig")
        if params.get("RuntimeEnv"):
            self.RuntimeEnv = params.get("RuntimeEnv")
        if params.get("EntryPointCommand"):
            self.EntryPointCommand = params.get("EntryPointCommand")
        if params.get("UseIdleResource"):
            self.UseIdleResource = params.get("UseIdleResource")
        if params.get("EnableRDMADepsCheck"):
            self.EnableRDMADepsCheck = params.get("EnableRDMADepsCheck")


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
        :param GPUType: GPU类型
        :type PathPrefix: String
        :param QueueId: 队列ID
        :type PathPrefix: String
        :param UseIdleResource: 是否使用闲时资源
        :type PathPrefix: Boolean
        :param SortKey: 排序关键字
        :type PathPrefix: String
        :param Sort: 排序方式
        :type PathPrefix: String
        """
        self.TrainJobId = None
        self.Filter = None
        self.PageSize = None
        self.Page = None
        self.TrainJobName = None
        self.GPUType = None
        self.QueueId = None
        self.UseIdleResource = None
        self.SortKey = None
        self.Sort = None

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
        if params.get("GPUType"):
            self.GPUType = params.get("GPUType")
        if params.get("QueueId"):
            self.QueueId = params.get("QueueId")
        if params.get("UseIdleResource"):
            self.UseIdleResource = params.get("UseIdleResource")
        if params.get("SortKey"):
            self.SortKey = params.get("SortKey")
        if params.get("Sort"):
            self.Sort = params.get("Sort")


class ModifyModelAccessRequest(AbstractModel):
    """ModifyModelAccess请求参数结构体
    """

    def __init__(self):
        r"""更新模型访问权限
        :param ModelId: 模型ID
        :type PathPrefix: String
        :param Users: 用户访问权限列表
        :type PathPrefix: Array
        :param ModelPermission: 模型权限，枚举值：
- Public，公开可见
- Private，仅自己可见
- Specified，指定范围
        :type PathPrefix: String
        :param SharedGroupList: 权限组共享列表（若传入，会进行全量覆盖式修改）
        :type PathPrefix: Array
        """
        self.ModelId = None
        self.Users = None
        self.ModelPermission = None
        self.SharedGroupList = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("Users"):
            self.Users = params.get("Users")
        if params.get("ModelPermission"):
            self.ModelPermission = params.get("ModelPermission")
        if params.get("SharedGroupList"):
            self.SharedGroupList = params.get("SharedGroupList")


class CreateModelAndVersionRequest(AbstractModel):
    """CreateModelAndVersion请求参数结构体
    """

    def __init__(self):
        r"""创建模型及版本
        :param ModelName: 模型名称
        :type PathPrefix: String
        :param ModelDescription: 模型描述
        :type PathPrefix: String
        :param ModelVersionName: 模型版本名称
        :type PathPrefix: String
        :param ModelVersionDescription: 模型版本描述
        :type PathPrefix: String
        :param SourceType: 来源类型，有效值：storage-config
        :type PathPrefix: String
        :param StorageConfigId: 存储配置ID
        :type PathPrefix: String
        :param Format: 模型格式(有效值请参考DescribeFormatAndFrameworks)
        :type PathPrefix: String
        :param Framework: 模型框架(有效值请参考DescribeFormatAndFrameworks)
        :type PathPrefix: String
        :param Users: 用户访问权限列表
        :type PathPrefix: Array
        :param ModelPermission: 模型权限，枚举值：
- Public，公开可见
- Private，仅自己可见
- Specified，指定范围（默认）
        :type PathPrefix: String
        :param SharedGroupList: 权限组共享列表
        :type PathPrefix: Array
        """
        self.ModelName = None
        self.ModelDescription = None
        self.ModelVersionName = None
        self.ModelVersionDescription = None
        self.SourceType = None
        self.StorageConfigId = None
        self.Format = None
        self.Framework = None
        self.Users = None
        self.ModelPermission = None
        self.SharedGroupList = None

    def _deserialize(self, params):
        if params.get("ModelName"):
            self.ModelName = params.get("ModelName")
        if params.get("ModelDescription"):
            self.ModelDescription = params.get("ModelDescription")
        if params.get("ModelVersionName"):
            self.ModelVersionName = params.get("ModelVersionName")
        if params.get("ModelVersionDescription"):
            self.ModelVersionDescription = params.get("ModelVersionDescription")
        if params.get("SourceType"):
            self.SourceType = params.get("SourceType")
        if params.get("StorageConfigId"):
            self.StorageConfigId = params.get("StorageConfigId")
        if params.get("Format"):
            self.Format = params.get("Format")
        if params.get("Framework"):
            self.Framework = params.get("Framework")
        if params.get("Users"):
            self.Users = params.get("Users")
        if params.get("ModelPermission"):
            self.ModelPermission = params.get("ModelPermission")
        if params.get("SharedGroupList"):
            self.SharedGroupList = params.get("SharedGroupList")


class ModifyModelRequest(AbstractModel):
    """ModifyModel请求参数结构体
    """

    def __init__(self):
        r"""更新模型信息
        :param ModelId: 模型ID
        :type PathPrefix: String
        :param ModelName: 模型名称
        :type PathPrefix: String
        :param ModelDescription: 模型描述
        :type PathPrefix: String
        """
        self.ModelId = None
        self.ModelName = None
        self.ModelDescription = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("ModelName"):
            self.ModelName = params.get("ModelName")
        if params.get("ModelDescription"):
            self.ModelDescription = params.get("ModelDescription")


class DescribeModelsRequest(AbstractModel):
    """DescribeModels请求参数结构体
    """

    def __init__(self):
        r"""查询模型列表
        :param ModelId.N: 模型ID列表
        :type PathPrefix: Array
        :param ModelName: 模型名称(支持模糊查询)
        :type PathPrefix: String
        :param Page: 页码
        :type PathPrefix: Int
        :param PageSize: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        """
        self.ModelId_N = None
        self.ModelName = None
        self.Page = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("ModelId.N"):
            self.ModelId_N = params.get("ModelId.N")
        if params.get("ModelName"):
            self.ModelName = params.get("ModelName")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DeleteModelRequest(AbstractModel):
    """DeleteModel请求参数结构体
    """

    def __init__(self):
        r"""删除指定模型
        :param ModelId: 模型ID
        :type PathPrefix: String
        """
        self.ModelId = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")


class CreateModelVersionRequest(AbstractModel):
    """CreateModelVersion请求参数结构体
    """

    def __init__(self):
        r"""创建推理模型版本
        :param ModelId: 模型ID
        :type PathPrefix: String
        :param ModelVersionName: 模型版本名称
        :type PathPrefix: String
        :param ModelVersionDescription: 模型版本描述
        :type PathPrefix: String
        :param SourceType: 来源类型，有效值：storage-config
        :type PathPrefix: String
        :param StorageConfigId: 存储配置ID
        :type PathPrefix: String
        :param Format: 模型格式（有效值请参考DescribeFormatAndFrameworks）
        :type PathPrefix: String
        :param Framework: 模型框架（有效值请参考DescribeFormatAndFrameworks）
        :type PathPrefix: String
        """
        self.ModelId = None
        self.ModelVersionName = None
        self.ModelVersionDescription = None
        self.SourceType = None
        self.StorageConfigId = None
        self.Format = None
        self.Framework = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("ModelVersionName"):
            self.ModelVersionName = params.get("ModelVersionName")
        if params.get("ModelVersionDescription"):
            self.ModelVersionDescription = params.get("ModelVersionDescription")
        if params.get("SourceType"):
            self.SourceType = params.get("SourceType")
        if params.get("StorageConfigId"):
            self.StorageConfigId = params.get("StorageConfigId")
        if params.get("Format"):
            self.Format = params.get("Format")
        if params.get("Framework"):
            self.Framework = params.get("Framework")


class DeleteModelVersionRequest(AbstractModel):
    """DeleteModelVersion请求参数结构体
    """

    def __init__(self):
        r"""删除模型版本
        :param ModelVersionId: 模型版本ID
        :type PathPrefix: String
        """
        self.ModelVersionId = None

    def _deserialize(self, params):
        if params.get("ModelVersionId"):
            self.ModelVersionId = params.get("ModelVersionId")


class ModifyModelVersionRequest(AbstractModel):
    """ModifyModelVersion请求参数结构体
    """

    def __init__(self):
        r"""更新模型版本
        :param ModelVersionId: 模型版本ID
        :type PathPrefix: String
        :param ModelVersionName: 模型版本名称
        :type PathPrefix: String
        :param ModelVersionDescription: 模型版本描述
        :type PathPrefix: String
        :param Format: 模型格式（有效值请参考DescribeFormatAndFrameworks）
        :type PathPrefix: String
        :param Framework: 模型框架（有效值请参考DescribeFormatAndFrameworks）
        :type PathPrefix: String
        :param SourceType: 来源类型，有效值：storage-config
        :type PathPrefix: String
        :param StorageConfigId: 存储配置ID
        :type PathPrefix: String
        """
        self.ModelVersionId = None
        self.ModelVersionName = None
        self.ModelVersionDescription = None
        self.Format = None
        self.Framework = None
        self.SourceType = None
        self.StorageConfigId = None

    def _deserialize(self, params):
        if params.get("ModelVersionId"):
            self.ModelVersionId = params.get("ModelVersionId")
        if params.get("ModelVersionName"):
            self.ModelVersionName = params.get("ModelVersionName")
        if params.get("ModelVersionDescription"):
            self.ModelVersionDescription = params.get("ModelVersionDescription")
        if params.get("Format"):
            self.Format = params.get("Format")
        if params.get("Framework"):
            self.Framework = params.get("Framework")
        if params.get("SourceType"):
            self.SourceType = params.get("SourceType")
        if params.get("StorageConfigId"):
            self.StorageConfigId = params.get("StorageConfigId")


class DescribeModelVersionsRequest(AbstractModel):
    """DescribeModelVersions请求参数结构体
    """

    def __init__(self):
        r"""查询模型版本
        :param ModelVersionId.N: 模型版本ID列表
        :type PathPrefix: Array
        :param ModelVersionName: 模型版本名称(支持模糊查询)
        :type PathPrefix: String
        :param ModelId: 模型ID
        :type PathPrefix: String
        :param Page: 页码
        :type PathPrefix: Int
        :param PageSize: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        """
        self.ModelVersionId_N = None
        self.ModelVersionName = None
        self.ModelId = None
        self.Page = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("ModelVersionId.N"):
            self.ModelVersionId_N = params.get("ModelVersionId.N")
        if params.get("ModelVersionName"):
            self.ModelVersionName = params.get("ModelVersionName")
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DescribeFormatAndFrameworksRequest(AbstractModel):
    """DescribeFormatAndFrameworks请求参数结构体
    """

    def __init__(self):
        r"""描述模型格式及框架
        """

    def _deserialize(self, params):
        return


class AddModelAccessRequest(AbstractModel):
    """AddModelAccess请求参数结构体
    """

    def __init__(self):
        r"""为用户/权限组添加模型权限
        :param ModelId: 模型ID
        :type PathPrefix: String
        :param UserId: 用户ID，与 SharedGroupId 二选一，不可同时为空或同时非空
        :type PathPrefix: String
        :param SharedGroupId: 权限组ID，与 UserId 二选一，不可同时为空或同时非空
        :type PathPrefix: String
        :param Permission: 模型访问权限，有效值：
- writer 管理员
- reader 普通成员
        :type PathPrefix: String
        """
        self.ModelId = None
        self.UserId = None
        self.SharedGroupId = None
        self.Permission = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("UserId"):
            self.UserId = params.get("UserId")
        if params.get("SharedGroupId"):
            self.SharedGroupId = params.get("SharedGroupId")
        if params.get("Permission"):
            self.Permission = params.get("Permission")


class ModifyModelAccessRoleRequest(AbstractModel):
    """ModifyModelAccessRole请求参数结构体
    """

    def __init__(self):
        r"""修改用户/权限组模型权限
        :param ModelId: 模型ID
        :type PathPrefix: String
        :param UserId: 用户ID，与 SharedGroupId 二选一，不可同时为空或同时非空
        :type PathPrefix: String
        :param SharedGroupId: 权限组ID，与 UserId 二选一，不可同时为空或同时非空
        :type PathPrefix: String
        :param Permission: 模型访问权限，有效值：
- writer 管理员
- reader 普通成员
        :type PathPrefix: String
        """
        self.ModelId = None
        self.UserId = None
        self.SharedGroupId = None
        self.Permission = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("UserId"):
            self.UserId = params.get("UserId")
        if params.get("SharedGroupId"):
            self.SharedGroupId = params.get("SharedGroupId")
        if params.get("Permission"):
            self.Permission = params.get("Permission")


class RemoveModelAccessRequest(AbstractModel):
    """RemoveModelAccess请求参数结构体
    """

    def __init__(self):
        r"""移除用户/权限组模型权限
        :param ModelId: 模型ID
        :type PathPrefix: String
        :param UserId: 用户ID，与 SharedGroupId 二选一，不可同时为空或同时非空
        :type PathPrefix: String
        :param SharedGroupId: 权限组ID，与 UserId 二选一，不可同时为空或同时非空
        :type PathPrefix: String
        """
        self.ModelId = None
        self.UserId = None
        self.SharedGroupId = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("UserId"):
            self.UserId = params.get("UserId")
        if params.get("SharedGroupId"):
            self.SharedGroupId = params.get("SharedGroupId")


