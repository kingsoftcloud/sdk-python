from ksyun.common.abstract_model import AbstractModel

class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体
    """

    def __init__(self):
        r"""创建实例(支持基于备份及指定时间点)
        :param InstanceName: 实例名称。需满足以下规则：6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线及中划线
        :type PathPrefix: String
        :param EnableModules: 集群已开启的实例类型,多个模块用逗号分隔。如："tidb,pd,tikv,timonitor,tidcd"。
        :type PathPrefix: String
        :param ModuleConfigs: 集群各个模块配置, 需与EnableModules参数中定义的各模块对应。Object:         {
            "moduleType": "tidb",
            "packageCode": "DB_1C2G",
            "replicas": 1,
            "cpu": 1,
            "mem": 2,
            "tidisk": 0
        }
        :type PathPrefix: Filter
        :param AdminUser: 管理员账号名称，默认：root。
        :type PathPrefix: String
        :param AdminPassword: 管理员账号密码。
        :type PathPrefix: String
        :param VpcId: 虚拟网络ID。
        :type PathPrefix: String
        :param SubnetId: 终端子网ID。
        :type PathPrefix: String
        :param BillType: 计费类型。可选：1(包年包月)；5（按量付费-按日月结）；87（按量付费）。
        :type PathPrefix: Int
        :param Duration: 仅计费类型为包年包月（BillType=1）时用。默认为1。
        :type PathPrefix: String
        :param ProductType: 商品类型。取固定值：577。
        :type PathPrefix: Int
        :param ProjectId: 项目制ID。如默认项目："0"。
        :type PathPrefix: String
        :param EnableAutoBackup: 开启自动备份。取固定值：true。
        :type PathPrefix: Boolean
        :param Engine: 实例引擎。默认：tidb。
        :type PathPrefix: String
        :param EngineVersion: 引擎版本。默认：4.0。
        :type PathPrefix: String
        :param ClientPort: 实例端口。默认：4000。
        :type PathPrefix: Int
        :param Az: 可用区。
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param BackupConfig: 备份配置
        :type PathPrefix: Object
        :param backupId: 实例备份id(指定备份恢复时需传)
        :type PathPrefix: String
        :param backupRestoreInstanceId: 备份恢复实例ID(根据时间点恢复的源实例)
```
指定时间点恢复，需要如下参数都传

注意：
backupRestoreInstanceId
backupRestoreTime
```
        :type PathPrefix: String
        :param backupRestoreTime: 备份恢复时间点(根据时间点恢复的指定时间点)
```
格式：2024-03-14 10:46:02

注意：
backupRestoreInstanceId
backupRestoreTime
```
        :type PathPrefix: String
        """
        self.InstanceName = None
        self.EnableModules = None
        self.ModuleConfigs = None
        self.AdminUser = None
        self.AdminPassword = None
        self.VpcId = None
        self.SubnetId = None
        self.BillType = None
        self.Duration = None
        self.ProductType = None
        self.ProjectId = None
        self.EnableAutoBackup = None
        self.Engine = None
        self.EngineVersion = None
        self.ClientPort = None
        self.Az = None
        self.SecurityGroupId = None
        self.BackupConfig = None
        self.backupId = None
        self.backupRestoreInstanceId = None
        self.backupRestoreTime = None

    def _deserialize(self, params):
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("EnableModules"):
            self.EnableModules = params.get("EnableModules")
        if params.get("ModuleConfigs"):
            self.ModuleConfigs = params.get("ModuleConfigs")
        if params.get("AdminUser"):
            self.AdminUser = params.get("AdminUser")
        if params.get("AdminPassword"):
            self.AdminPassword = params.get("AdminPassword")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("EnableAutoBackup"):
            self.EnableAutoBackup = params.get("EnableAutoBackup")
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("ClientPort"):
            self.ClientPort = params.get("ClientPort")
        if params.get("Az"):
            self.Az = params.get("Az")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("BackupConfig"):
            self.BackupConfig = params.get("BackupConfig")
        if params.get("backupId"):
            self.backupId = params.get("backupId")
        if params.get("backupRestoreInstanceId"):
            self.backupRestoreInstanceId = params.get("backupRestoreInstanceId")
        if params.get("backupRestoreTime"):
            self.backupRestoreTime = params.get("backupRestoreTime")


class ListInstanceRequest(AbstractModel):
    """ListInstance请求参数结构体
    """

    def __init__(self):
        r"""查询实例列表(区分Region)
        :param ProjectIds: 项目ID列表，多个项目ID以逗号分隔。不填表示全部项目。
        :type PathPrefix: String
        :param InstanceStatus: 实例状态。查询多种实例状态时，用逗号分隔。如：running,error
        :type PathPrefix: String
        :param FuzzySearch: 模糊查找。支持：实例ID、实例名称、项目名称、VIP、实例状态。
        :type PathPrefix: String
        :param Offset: 查找第几页数据，从0开始。
        :type PathPrefix: Int
        :param Limit: 每页最大记录数。默认：10。
        :type PathPrefix: Int
        :param OrderBy: 排序字段。
        :type PathPrefix: String
        :param ProductType: 商品类型，默认：577
        :type PathPrefix: Int
        """
        self.ProjectIds = None
        self.InstanceStatus = None
        self.FuzzySearch = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.ProductType = None

    def _deserialize(self, params):
        if params.get("ProjectIds"):
            self.ProjectIds = params.get("ProjectIds")
        if params.get("InstanceStatus"):
            self.InstanceStatus = params.get("InstanceStatus")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体
    """

    def __init__(self):
        r"""查询实例详情
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体
    """

    def __init__(self):
        r"""删除实例(支持批量)
        :param InstanceIds: 实例ID列表。多个实例ID请用英文逗号隔开。
        :type PathPrefix: String
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance请求参数结构体
    """

    def __init__(self):
        r"""修改名称(重命名)
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param InstanceName: 实例新名称。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstanceName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")


class ListRegionRequest(AbstractModel):
    """ListRegion请求参数结构体
    """

    def __init__(self):
        r"""查询地域列表
        :param ProductType: 产品线ID

```json
集群版:577
企业版:711
```
        :type PathPrefix: Int
        """
        self.ProductType = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")


class DescRegionRequest(AbstractModel):
    """DescRegion请求参数结构体
    """

    def __init__(self):
        r"""查询指定地域详情
        :param RegionCode: 地域标识。例如：cn-shanghai-2
        :type PathPrefix: String
        :param ProductType: 产品线商品ID

```json
集群版:577
企业版:711
```
        :type PathPrefix: Int
        """
        self.RegionCode = None
        self.ProductType = None

    def _deserialize(self, params):
        if params.get("RegionCode"):
            self.RegionCode = params.get("RegionCode")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""创建安全组
        :param ProductType: 商品类型。取固定值：577。
        :type PathPrefix: Int
        :param SecurityGroupName: 安全组名称。长度[2,64]
        :type PathPrefix: String
        :param IpVersion: 安全组IP类型。默认ipv4；取值：ipv4，ipv6。
        :type PathPrefix: String
        :param Description: 安全组描述。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.SecurityGroupName = None
        self.IpVersion = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")
        if params.get("Description"):
            self.Description = params.get("Description")


class ListSecurityGroupRequest(AbstractModel):
    """ListSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查询安全组列表
        :param FuzzySearch: 模糊查找。支持：安全组名称、安全组描述。
        :type PathPrefix: String
        :param Offset: 第几页，从0开始。默认为0。
        :type PathPrefix: Int
        :param Limit: 每页最大记录数。默认为10。
        :type PathPrefix: Int
        :param OrderBy: 排序字段。格式：col1.asc,col2.desc。
        :type PathPrefix: String
        """
        self.FuzzySearch = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None

    def _deserialize(self, params):
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查询安全组详情
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param RuleFuzzySearch: 规则模糊匹配，CIDR规则 or 描述
        :type PathPrefix: String
        :param InstanceFuzzySearch: 实例模糊匹配：实例名称 or IP
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.RuleFuzzySearch = None
        self.InstanceFuzzySearch = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("RuleFuzzySearch"):
            self.RuleFuzzySearch = params.get("RuleFuzzySearch")
        if params.get("InstanceFuzzySearch"):
            self.InstanceFuzzySearch = params.get("InstanceFuzzySearch")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""删除安全组(支持批量)
        :param SecurityGroupIds: 安全组ID列表。多个安全组ID请用英文逗号隔开。
        :type PathPrefix: String
        """
        self.SecurityGroupIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")


class UpdateSecurityGroupRequest(AbstractModel):
    """UpdateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""更新安全组
        :param SecurityGroupId: 安全组名称。
        :type PathPrefix: String
        :param SecurityGroupName: 安全组新名称。请注意：SecurityGroupName和Description参数必填其一。
        :type PathPrefix: String
        :param Description: 安全组新描述。请注意：SecurityGroupName和Description参数必填其一。
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")


class CloneSecurityGroupRequest(AbstractModel):
    """CloneSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""复制安全组(仅规则)
        :param SrcSecurityGroupId: 原安全组ID。
        :type PathPrefix: String
        :param SecurityGroupName: 新安全组名称。
        :type PathPrefix: String
        :param Description: 新安全组描述。
        :type PathPrefix: String
        """
        self.SrcSecurityGroupId = None
        self.SecurityGroupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("SrcSecurityGroupId"):
            self.SrcSecurityGroupId = params.get("SrcSecurityGroupId")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")


class BindSecurityGroupRequest(AbstractModel):
    """BindSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""实例绑定安全组
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param InstanceIds: 实例ID列表。多个ID请以英文逗号分隔。
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class UnbindSecurityGroupRequest(AbstractModel):
    """UnbindSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""实例解绑安全组
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param InstanceIds: 实例ID列表。多个ID以英文逗号分隔。
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class RebindSecurityGroupRequest(AbstractModel):
    """RebindSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""重新绑定实例安全组
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateSecurityRuleRequest(AbstractModel):
    """CreateSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""创建安全规则(CIDR)
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param Rules: 安全组规则。格式：{Rules: [{"Cidr": "***", "Desc": "***", "AclAction": "***"}]}。
请注意：1. Cidr为必填参数；2. AclAction（控制策略）可选：accept（放行），reject（拒绝）；默认为accept。
        :type PathPrefix: Object
        """
        self.SecurityGroupId = None
        self.Rules = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("Rules"):
            self.Rules = params.get("Rules")


class UpdateSecurityRuleRequest(AbstractModel):
    """UpdateSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""更新安全规则(CIDR)
        :param RuleId: 安全组规则ID。可通过DescribeSecurityGroup接口获取。
        :type PathPrefix: String
        :param Description: 安全组规则新描述。
        :type PathPrefix: String
        :param Cidr: 安全组新规则。
        :type PathPrefix: String
        """
        self.RuleId = None
        self.Description = None
        self.Cidr = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Cidr"):
            self.Cidr = params.get("Cidr")


class DeleteSecurityRuleRequest(AbstractModel):
    """DeleteSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""删除安全规则(CIDR)
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param RuleIds: 安全组规则ID列表。多个安全组规则ID请用英文逗号隔开。
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.RuleIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("RuleIds"):
            self.RuleIds = params.get("RuleIds")


class ListSecuredInstanceRequest(AbstractModel):
    """ListSecuredInstance请求参数结构体
    """

    def __init__(self):
        r"""查询已绑定安全组实例列表
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param ProjectIds: 不填表示全部项目，多个id以逗号分隔。
        :type PathPrefix: String
        :param FuzzySearch: 模糊搜索。支持：实例ID、实例名称、项目名称、VIP。
        :type PathPrefix: String
        :param Offset: 第几页，从0开始。默认为0。
        :type PathPrefix: Int
        :param Limit: 每页最大记录数。默认为10。
        :type PathPrefix: Int
        :param OrderBy: 排序字段列表。请注意，格式：col1.asc,col2.desc。
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.ProjectIds = None
        self.FuzzySearch = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("ProjectIds"):
            self.ProjectIds = params.get("ProjectIds")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")


class ListUnsecuredInstanceRequest(AbstractModel):
    """ListUnsecuredInstance请求参数结构体
    """

    def __init__(self):
        r"""查询未绑定安全组实例列表
        :param ProjectIds: 项目ID列表。不填表示全部项目，多个id以逗号分隔。
        :type PathPrefix: String
        :param FuzzySearch: 模糊搜索。支持：实例ID、实例名称、项目名称、VIP。
        :type PathPrefix: String
        :param Offset: 第几页，从0开始。
        :type PathPrefix: Int
        :param Limit: 每页最大记录数。
        :type PathPrefix: Int
        :param OrderBy: 排序字段列表。请注意，格式为：col1.asc,col2.desc。
        :type PathPrefix: String
        """
        self.ProjectIds = None
        self.FuzzySearch = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None

    def _deserialize(self, params):
        if params.get("ProjectIds"):
            self.ProjectIds = params.get("ProjectIds")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")


class ListBackupRequest(AbstractModel):
    """ListBackup请求参数结构体
    """

    def __init__(self):
        r"""查询备份列表
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param Keyword: 备份名称模糊查询。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Keyword = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体
    """

    def __init__(self):
        r"""创建备份(手动)
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param BackupName: 备份名称。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.BackupName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("BackupName"):
            self.BackupName = params.get("BackupName")


class UpdateBackupRuleRequest(AbstractModel):
    """UpdateBackupRule请求参数结构体
    """

    def __init__(self):
        r"""更新自动备份规则
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param PreferredBackupTime: 备份时段选择：
格式：HH:mm-HH:mm
        :type PathPrefix: String
        :param EnableAutobackup: 是否开启自动备份
```
false 未开启； true 开启
```
        :type PathPrefix: Boolean
        :param EnableIncremental: 是否开启增量备份
```
false 未开启； true 开启
```
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.PreferredBackupTime = None
        self.EnableAutobackup = None
        self.EnableIncremental = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")
        if params.get("EnableAutobackup"):
            self.EnableAutobackup = params.get("EnableAutobackup")
        if params.get("EnableIncremental"):
            self.EnableIncremental = params.get("EnableIncremental")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup请求参数结构体
    """

    def __init__(self):
        r"""批量删除备份记录
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param BackupIds: 备份ID列表。多个备份ID请用英文逗号隔开。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.BackupIds = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("BackupIds"):
            self.BackupIds = params.get("BackupIds")


class CreateRestoreRequest(AbstractModel):
    """CreateRestore请求参数结构体
    """

    def __init__(self):
        r"""创建恢复任务
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param BackupId: 恢复关联的备份记录ID
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.BackupId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("BackupId"):
            self.BackupId = params.get("BackupId")


class OpenTiMonitorRequest(AbstractModel):
    """OpenTiMonitor请求参数结构体
    """

    def __init__(self):
        r"""打开timonitor监控
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体
    """

    def __init__(self):
        r"""创建任务(TICDC)
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param TaskName: 任务名称，不可重复
        :type PathPrefix: String
        :param TargetId: 目标端实例ID
        :type PathPrefix: String
        :param VpcId: 目标端VpcId
仅Kafka需要传，Mysql不需要
        :type PathPrefix: String
        :param VnetId: 目标端VnetId
仅Kafka需要传，Mysql不需要
        :type PathPrefix: String
        :param TargetType: 目标端实例类型
仅支持：MySQLKAFKA
        :type PathPrefix: String
        :param TargetMySQL: 目标端拓展信息
若TargetType=MySQL，根据需要填写
        :type PathPrefix: Object
        :param TargetKafka: 目标端拓展信息
若TargetType=KAFKA，根据需要填写
        :type PathPrefix: Object
        """
        self.InstanceId = None
        self.TaskName = None
        self.TargetId = None
        self.VpcId = None
        self.VnetId = None
        self.TargetType = None
        self.TargetMySQL = None
        self.TargetKafka = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")
        if params.get("TargetId"):
            self.TargetId = params.get("TargetId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("TargetType"):
            self.TargetType = params.get("TargetType")
        if params.get("TargetMySQL"):
            self.TargetMySQL = params.get("TargetMySQL")
        if params.get("TargetKafka"):
            self.TargetKafka = params.get("TargetKafka")


class OperationTasksRequest(AbstractModel):
    """OperationTasks请求参数结构体
    """

    def __init__(self):
        r"""任务操作(TICDC)
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param TaskList: 任务名称列表，多个任务以  英文逗号分隔
        :type PathPrefix: String
        :param Operation: 操作类型：
DeleteTask 删除 
RetryTask  重试 
PauseTask  暂停 
ResumeTask 恢复
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.TaskList = None
        self.Operation = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TaskList"):
            self.TaskList = params.get("TaskList")
        if params.get("Operation"):
            self.Operation = params.get("Operation")


class CheckTaskNameRequest(AbstractModel):
    """CheckTaskName请求参数结构体
    """

    def __init__(self):
        r"""名称列表(TICDC)
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体
    """

    def __init__(self):
        r"""任务详情(TICDC)
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param TaskName: 任务名称
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.TaskName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")


class ListTasksRequest(AbstractModel):
    """ListTasks请求参数结构体
    """

    def __init__(self):
        r"""任务列表(TICDC)
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体
    """

    def __init__(self):
        r"""查询库表列表
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体
    """

    def __init__(self):
        r"""查询账号列表
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体
    """

    def __init__(self):
        r"""创建账号(指定实例)
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param AccountName: 账户名称

```json
注：支持数字字母,中划线,下划线。不支持保留字符串。
```
        :type PathPrefix: String
        :param AccountPassword: 账户密码
        :type PathPrefix: String
        :param Describe: 账户描述
        :type PathPrefix: String
        :param Privileges: 权限列表，支持多传,接收参数为Map<String,String>

例如："Privileges":{"test":"onlyDdl"}
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None
        self.AccountPassword = None
        self.Describe = None
        self.Privileges = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")
        if params.get("AccountPassword"):
            self.AccountPassword = params.get("AccountPassword")
        if params.get("Describe"):
            self.Describe = params.get("Describe")
        if params.get("Privileges"):
            self.Privileges = params.get("Privileges")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体
    """

    def __init__(self):
        r"""删除账号(支持批量)
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param AccountName: 账户名称，支持批量删除，中间用  ',' 分隔 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")


class ModifyAccountInfoRequest(AbstractModel):
    """ModifyAccountInfo请求参数结构体
    """

    def __init__(self):
        r"""编辑账号信息(修改密码)
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param AccountName: 账户名
        :type PathPrefix: String
        :param AccountPassword: 账户密码
        :type PathPrefix: String
        :param AccountType: 账户类型:非必传，修改管理员用户的时候需指定'admin' 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None
        self.AccountPassword = None
        self.AccountType = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")
        if params.get("AccountPassword"):
            self.AccountPassword = params.get("AccountPassword")
        if params.get("AccountType"):
            self.AccountType = params.get("AccountType")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges请求参数结构体
    """

    def __init__(self):
        r"""编辑账号权限
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param AccountName: 账户名称
        :type PathPrefix: String
        :param OldPrivileges: 旧权限列表:Map<string,string> 
        :type PathPrefix: String
        :param NewPrivileges: 新权限:Map<string,string> 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None
        self.OldPrivileges = None
        self.NewPrivileges = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")
        if params.get("OldPrivileges"):
            self.OldPrivileges = params.get("OldPrivileges")
        if params.get("NewPrivileges"):
            self.NewPrivileges = params.get("NewPrivileges")


class ConfigurationInstanceEipRequest(AbstractModel):
    """ConfigurationInstanceEip请求参数结构体
    """

    def __init__(self):
        r"""申请/释放外网EIP
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param Operation: 操作类型
        :type PathPrefix: String
        :param EipPort: 端口号

```json
自定义支持区间：[10000, 65500] 
```
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.Operation = None
        self.EipPort = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Operation"):
            self.Operation = params.get("Operation")
        if params.get("EipPort"):
            self.EipPort = params.get("EipPort")


class UpdateInstanceTrialOrderRequest(AbstractModel):
    """UpdateInstanceTrialOrder请求参数结构体
    """

    def __init__(self):
        r"""试用订单转正/延期
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param OperateType: 操作类型

```json
试用延期：delay
试用转正：buy

注意：无默认，不区分大小写
```
        :type PathPrefix: String
        :param BillType: 计费类型

```json
包年包月：1
按量付费：87
按量付费（按日月结）：5
```
        :type PathPrefix: Int
        :param Duration: 延期或转正时间

```json
默认1天/年，按日结算和按量付费不用指定
```
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.OperateType = None
        self.BillType = None
        self.Duration = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("OperateType"):
            self.OperateType = params.get("OperateType")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")


