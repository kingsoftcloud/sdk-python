from ksyun.common.abstract_model import AbstractModel


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体
    """

    def __init__(self):
        r"""CreateInstance
        :param InstanceName: 实例名称。需满足以下规则：6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线及中划线
        :type PathPrefix: String
        :param EnableModules: 集群已开启的实例类型,多个模块用逗号分隔。如："tidb,pd,tikv,timonitor"。
        :type PathPrefix: String
        :param ModuleConfigs: 集群各个模块配置, 需与EnableModules参数中定义的各模块对应。Object:         {
            "moduleType": "tidb",
            "packageCode": "DB_1C2G",
            "replicas": 1,
            "cpu": 1,
            "mem": 2,
            "tidisk": 0
        }
        :type PathPrefix: Array
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
        :param BackupConfig.MaxBackups: 最大备份记录数。
        :type PathPrefix: Int
        :param BackupConfig.MaxReservedHours: 备份记录最大保留时长，单位：小时。
        :type PathPrefix: Int
        :param BackupConfig.PreferredBackupTime: 自动备份时间段。默认值："01:00-02:00"。
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
        self.BackupConfig.MaxBackups = None
        self.BackupConfig.MaxReservedHours = None
        self.BackupConfig.PreferredBackupTime = None
        self.EnableAutoBackup = None
        self.Engine = None
        self.EngineVersion = None
        self.ClientPort = None
        self.Az = None
        self.SecurityGroupId = None

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
        if params.get("BackupConfig.MaxBackups"):
            self.BackupConfig.MaxBackups = params.get("BackupConfig.MaxBackups")
        if params.get("BackupConfig.MaxReservedHours"):
            self.BackupConfig.MaxReservedHours = params.get("BackupConfig.MaxReservedHours")
        if params.get("BackupConfig.PreferredBackupTime"):
            self.BackupConfig.PreferredBackupTime = params.get("BackupConfig.PreferredBackupTime")
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


class ListInstanceRequest(AbstractModel):
    """ListInstance请求参数结构体
    """

    def __init__(self):
        r"""ListInstance
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
        """
        self.ProjectIds = None
        self.InstanceStatus = None
        self.FuzzySearch = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None

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


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体
    """

    def __init__(self):
        r"""DescribeInstance
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance请求参数结构体
    """

    def __init__(self):
        r"""RenameInstance
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
        r"""ListRegion
        :param ProductType: 取固定取值：577。
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
        r"""DescRegion
        :param RegionCode: 地域标识。例如：cn-shanghai-3。
        :type PathPrefix: String
        :param ProductType: 商品类型。取固定值：577。
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
        r"""CreateSecurityGroup
        :param ProductType: 商品类型。取固定值：577。
        :type PathPrefix: Int
        :param SecurityGroupName: 安全组名称。
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
        r"""ListSecurityGroup
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
        r"""DescribeSecurityGroup
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        """
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class UpdateSecurityGroupRequest(AbstractModel):
    """UpdateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""UpdateSecurityGroup
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
        r"""CloneSecurityGroup
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
        r"""BindSecurityGroup
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
        r"""UnbindSecurityGroup
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
        r"""RebindSecurityGroup
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
        r"""CreateSecurityRule
        :param Rules: 安全组规则。格式：{Rules: [{"Cidr": "***", "Desc": "***", "AclAction": "***"}]}。
请注意：1. Cidr为必填参数；2. AclAction（控制策略）可选：accept（放行），reject（拒绝）；默认为accept。
        :type PathPrefix: Array
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        """
        self.Rules = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("Rules"):
            self.Rules = params.get("Rules")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class UpdateSecurityRuleRequest(AbstractModel):
    """UpdateSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""UpdateSecurityRule
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


class ListUnsecuredInstanceRequest(AbstractModel):
    """ListUnsecuredInstance请求参数结构体
    """

    def __init__(self):
        r"""ListUnsecuredInstance
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
        r"""ListBackup
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
