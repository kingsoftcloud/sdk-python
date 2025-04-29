from ksyun.common.abstract_model import AbstractModel


class ListInstanceRequest(AbstractModel):
    """ListInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse查询实例列表
        :param ProductType: 商品类型。可选：单副本（ClickHouse_Single）
；高可用（ClickHouse）。
        :type PathPrefix: String
        :param TagId: 根据TagId进行过滤。
        :type PathPrefix: String
        :param ProjectIds: 根据项目ID进行过滤，不填则表示全部项目。
        :type PathPrefix: Filter
        :param FuzzySearch: 模糊搜索。支持：实例ID、实例名称,VIP。
        :type PathPrefix: String
        :param OrderBy: 排序字段列表。
        :type PathPrefix: Filter
        :param Offset: 第几页，从0开始。
        :type PathPrefix: Int
        :param Limit: 每页最大记录数。默认为10。
        :type PathPrefix: Int
        """
        self.ProductType = None
        self.TagId = None
        self.ProjectIds = None
        self.FuzzySearch = None
        self.OrderBy = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("TagId"):
            self.TagId = params.get("TagId")
        if params.get("ProjectIds"):
            self.ProjectIds = params.get("ProjectIds")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse查看实例详情
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse创建实例
        :param ProductType: 商品类型。可选：ClickHouse_Single（单副本）；ClickHouse（高可用）。
        :type PathPrefix: String
        :param InstanceName: 实例名称。
        :type PathPrefix: String
        :param InstanceType: 实例套餐code。如：bd_ck_0，single_ck_0等。


        :type PathPrefix: String
        :param AdminUser: 管理员名称,默认admin。
        :type PathPrefix: String
        :param AdminPassword: 管理员密码。
        :type PathPrefix: String
        :param VpcId: VPC网络ID。
        :type PathPrefix: String
        :param SubnetId: 终端子网ID。
        :type PathPrefix: String
        :param Engine: 实例内核类型，默认：clickhouse。
        :type PathPrefix: String
        :param EngineVersion: 实例内核版本号。	可选"21.8"，"22.8"。
        :type PathPrefix: String
        :param ProjectId: 项目ID。
        :type PathPrefix: String
        :param BillType: 计费类型。87 按量计费
        :type PathPrefix: Int
        :param Duration: 计费区间(供包年包月计费方式使用),默认1。
        :type PathPrefix: Int
        :param EbsSize: 存储大小，单位：GB。
        :type PathPrefix: Int
        :param EbsType: 存储类型。可选：CloudDisk，LocalDisk默认：CloudDisk。
        :type PathPrefix: String
        :param Mem: 内存大小，单位：GB。需要同实例套餐中一致。
        :type PathPrefix: Int
        :param Cpu: cpu核数。需要同实例套餐中一致。
        :type PathPrefix: Int
        :param TcpPort: 实例tcp端口，默认：9000。
        :type PathPrefix: Int
        :param HttpPort: 实例http端口，默认：8123。
        :type PathPrefix: Int
        :param Az: 可用区。
        :type PathPrefix: String
        :param NodeNum: 实例节点数量，默认3。
        :type PathPrefix: Int
        :param PreferredBackupTime: 备份时段选择。格式：HH:mm-HH:mm。
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID，如果绑定安全组，需要添加。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.InstanceName = None
        self.InstanceType = None
        self.AdminUser = None
        self.AdminPassword = None
        self.VpcId = None
        self.SubnetId = None
        self.Engine = None
        self.EngineVersion = None
        self.ProjectId = None
        self.BillType = None
        self.Duration = None
        self.EbsSize = None
        self.EbsType = None
        self.Mem = None
        self.Cpu = None
        self.TcpPort = None
        self.HttpPort = None
        self.Az = None
        self.NodeNum = None
        self.PreferredBackupTime = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("AdminUser"):
            self.AdminUser = params.get("AdminUser")
        if params.get("AdminPassword"):
            self.AdminPassword = params.get("AdminPassword")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("EbsSize"):
            self.EbsSize = params.get("EbsSize")
        if params.get("EbsType"):
            self.EbsType = params.get("EbsType")
        if params.get("Mem"):
            self.Mem = params.get("Mem")
        if params.get("Cpu"):
            self.Cpu = params.get("Cpu")
        if params.get("TcpPort"):
            self.TcpPort = params.get("TcpPort")
        if params.get("HttpPort"):
            self.HttpPort = params.get("HttpPort")
        if params.get("Az"):
            self.Az = params.get("Az")
        if params.get("NodeNum"):
            self.NodeNum = params.get("NodeNum")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse删除实例
        :param InstanceIds: 实例ID列表。
        :type PathPrefix: Filter
        :param DeleteDirectly: 是否直接删除。默认：false 【参数说明：true：立刻删除，false：放入回收站】
        :type PathPrefix: Boolean
        """
        self.InstanceIds = None
        self.DeleteDirectly = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("DeleteDirectly"):
            self.DeleteDirectly = params.get("DeleteDirectly")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse重命名实例
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


class ListSecurityGroupRequest(AbstractModel):
    """ListSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse查看安全组列表
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        """
        self.ProductType = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse查看安全组详情
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse创建安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SecurityGroupName: 安全组名称。
        :type PathPrefix: String
        :param Description: 安全组描述。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.SecurityGroupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse删除安全组接口
        :param SecurityGroupIds: 安全组ID列表。
        :type PathPrefix: String
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        """
        self.SecurityGroupIds = None
        self.ProductType = None

    def _deserialize(self, params):
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")


class RenameSecurityGroupRequest(AbstractModel):
    """RenameSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse重命名安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param SecurityGroupName: 安全组新名称。名称和描述至少传一个，否则名称或描述不会变更。
        :type PathPrefix: String
        :param Description: 安全组新描述。名称和描述至少传一个，否则名称或描述不会变更。


        :type PathPrefix: String
        """
        self.ProductType = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
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
        r"""Clickhouse克隆安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SrcSecurityGroupId: 被克隆安全组ID。
        :type PathPrefix: String
        :param SecurityGroupName: 新安全组名称。
        :type PathPrefix: String
        :param Description: 新安全组描述。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.SrcSecurityGroupId = None
        self.SecurityGroupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
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
        r"""Clickhouse绑定安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SecurityGroupIds: 安全组ID列表。
        :type PathPrefix: Array
        :param InstanceIds: 实例ID列表。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.SecurityGroupIds = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class UnbindSecurityGroupRequest(AbstractModel):
    """UnbindSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse解绑安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param InstanceIds: 实例ID列表。
        :type PathPrefix: Array
        """
        self.ProductType = None
        self.SecurityGroupId = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class CreateSecurityRuleRequest(AbstractModel):
    """CreateSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse创建安全规则
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param Cidrs: IP规则列表。IP段采用CIDR地址格式。
        :type PathPrefix: Array
        """
        self.ProductType = None
        self.SecurityGroupId = None
        self.Cidrs = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("Cidrs"):
            self.Cidrs = params.get("Cidrs")


class DeleteSecurityRuleRequest(AbstractModel):
    """DeleteSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse删除安全规则
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param RuleIds: 安全组规则ID列表。多个安全组规则ID用逗号隔开。安全组规则ID可通过DescribeSecurityGroup接口获取。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.SecurityGroupId = None
        self.RuleIds = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("RuleIds"):
            self.RuleIds = params.get("RuleIds")


class ListSecuredInstanceRequest(AbstractModel):
    """ListSecuredInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse查询已绑定安全组的实例列表
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param ProjectIds: 项目组ID列表。不填表示全部项目。
        :type PathPrefix: Filter
        :param FuzzySearch: 模糊搜索。支持：实例ID、实例名称、项目名称、VIP。
        :type PathPrefix: String
        :param Offset: 第几页，从0开始。
        :type PathPrefix: Int
        :param Limit: 每页最大记录数
        :type PathPrefix: Int
        :param OrderBy: 排序字段。
        :type PathPrefix: Filter
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
        r"""Clickhouse查询未绑定安全组的实例列表
        :param FuzzySearch: 模糊搜索。
        :type PathPrefix: String
        :param Offset: 第几页，从0开始。
        :type PathPrefix: Int
        :param Limit: 每页最大记录数。
        :type PathPrefix: Int
        :param OrderBy: 排序字段。
        :type PathPrefix: Filter
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


class ListRecycledInstanceRequest(AbstractModel):
    """ListRecycledInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse查询回收站实例列表
        :param ProductType: 商品类型。可选：ClickHouse_Single（单副本）；ClickHouse（高可用）。
        :type PathPrefix: String
        :param ProjectIds: 项目ID列表，不填表示全部项目。
        :type PathPrefix: Filter
        :param FuzzySearch: 模糊查询字段。支持：实例ID、实例名称、VIP。
        :type PathPrefix: String
        :param OrderBy: 排序字段。
        :type PathPrefix: Filter
        :param Offset: 第几页，从0开始。默认：0。
        :type PathPrefix: Int
        :param Limit: 每页最大记录数。	默认：10。
        :type PathPrefix: Int
        """
        self.ProductType = None
        self.ProjectIds = None
        self.FuzzySearch = None
        self.OrderBy = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("ProjectIds"):
            self.ProjectIds = params.get("ProjectIds")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class RecoverRecycledInstanceRequest(AbstractModel):
    """RecoverRecycledInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse恢复实例
        :param InstanceIds: 实例ID列表。
        :type PathPrefix: Array
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class DropRecycledInstanceRequest(AbstractModel):
    """DropRecycledInstance请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse彻底删除实例
        :param InstanceIds: 实例ID列表。
        :type PathPrefix: Filter
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class ListRegionRequest(AbstractModel):
    """ListRegion请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse查询地域列表
        :param ProductType: 商品类型：Clickhouse固定取值：523。
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
        r"""Clickhouse查询地域详情
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param RegionCode: 地域编码。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.RegionCode = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("RegionCode"):
            self.RegionCode = params.get("RegionCode")


class UpdateSecurityRuleRequest(AbstractModel):
    """UpdateSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse更新安全规则备注
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param RuleId: 安全组规则ID。安全组规则ID可通过DescribeSecurityGroup接口获取。
        :type PathPrefix: String
        :param Description: 安全组规则备注。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.RuleId = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("Description"):
            self.Description = params.get("Description")


class RebindSecurityGroupRequest(AbstractModel):
    """RebindSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse实例重新绑定安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。
        :type PathPrefix: Int
        :param SecurityGroupId: 安全组ID。
        :type PathPrefix: String
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        """
        self.ProductType = None
        self.SecurityGroupId = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeEngineDefaultParametersRequest(AbstractModel):
    """DescribeEngineDefaultParameters请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse根据版本查询实例默认参数配置
        :param EngineVersion: 引擎版本。可选：21.8、22.8。
        :type PathPrefix: String
        :param ConfigType: 参数类型。可选：Users，Config。
        :type PathPrefix: String
        """
        self.EngineVersion = None
        self.ConfigType = None

    def _deserialize(self, params):
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("ConfigType"):
            self.ConfigType = params.get("ConfigType")


class ModifyDBParameterGroupRequest(AbstractModel):
    """ModifyDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse修改实例参数
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param Parameters: 参数变更列表。请求体中传值(key-value形式放入所有要变更的参数-参数值)。如：{
  "InstanceId": "***",
  "Parameters": {
    "keep_alive_timeout": "350"
  },
  "ConfigType": "Config"
}
        :type PathPrefix: Filter
        :param ConfigType: 参数类型。可选：Users，Config。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Parameters = None
        self.ConfigType = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Parameters"):
            self.Parameters = params.get("Parameters")
        if params.get("ConfigType"):
            self.ConfigType = params.get("ConfigType")


class DescribeDBInstanceParametersRequest(AbstractModel):
    """DescribeDBInstanceParameters请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse查询当前实例参数配置
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param ConfigType: 参数类型。可选：Users，Config。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ConfigType = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ConfigType"):
            self.ConfigType = params.get("ConfigType")


class ResetDBParameterRequest(AbstractModel):
    """ResetDBParameter请求参数结构体
    """

    def __init__(self):
        r"""Clickhouse重置实例参数
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param ConfigType: 参数类型。可选：Users，Config。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ConfigType = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ConfigType"):
            self.ConfigType = params.get("ConfigType")
