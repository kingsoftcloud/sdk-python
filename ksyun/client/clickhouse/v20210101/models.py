from ksyun.common.abstract_model import AbstractModel

class ListInstanceRequest(AbstractModel):
    """ListInstance请求参数结构体
    """

    def __init__(self):
        r"""查询实例列表
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
        r"""查询实例详情
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
        r"""创建实例(支持指定计费方式)
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
        :param ProductWhat: 产品类型(是否试用)

```json
1:正式产品
2:试用产品
```
        :type PathPrefix: Int
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
        self.ProductWhat = None

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
        if params.get("ProductWhat"):
            self.ProductWhat = params.get("ProductWhat")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体
    """

    def __init__(self):
        r"""删除实例(默认放入回收站)
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


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体
    """

    def __init__(self):
        r"""重启实例(指定实例ID重启)
        :param instanceIds: 实例ID列表

```json
批量操作可使用英文','分隔
```
        :type PathPrefix: String
        """
        self.instanceIds = None

    def _deserialize(self, params):
        if params.get("instanceIds"):
            self.instanceIds = params.get("instanceIds")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance请求参数结构体
    """

    def __init__(self):
        r"""修改实例名称
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
        r"""查看安全组列表
        :param ProductType: 商品类型
```json
高可用版:523
单副本版:676
```
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
        r"""查看安全组详情
        :param ProductType: 商品类型
```json
高可用版:523
单副本版:676
```
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
        r"""创建安全组
        :param ProductType: 商品类型

```json
高可用版:523
单副本版:676

注意：仅做标记，取默认值即可
```
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
        r"""删除安全组
        :param SecurityGroupIds: 安全组ID列表。
        :type PathPrefix: String
        :param ProductType: 商品类型：Clickhouse固定取值：523。

```json
高可用版:523
单副本版:676
```
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
        r"""重命名安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。

```json
高可用版:523
单副本版:676
```
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
        r"""克隆安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。

```json
高可用版:523
单副本版:676
```
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
        r"""绑定安全组
        :param ProductType: 商品类型：Clickhouse固定取值：523。
```json
高可用版:523
单副本版:676
```
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
        r"""解绑安全组
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
        r"""创建安全规则(添加自定义IP地址+绑定云主机IP)
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
        r"""删除安全规则(移除IP地址)
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
        r"""查询已绑定安全组的实例列表
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
        r"""查询未绑定安全组的实例列表
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
        r"""查询实例列表(回收站)
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
        r"""恢复实例(回收站实例重新移入正常实例列表)
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
        r"""彻底删除实例(回收站清空)
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
        r"""查询地域列表
        :param ProductType: 商品类型

```json
高可用版:523
单副本版:676
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
        r"""查询可用区详情
        :param ProductType: 商品类型
```json
高可用版:523
单副本版:676
```
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
        r"""修改安全规则备注(具体的IP规则描述)
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
        r"""重新绑定安全组
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
        r"""查询实例默认参数
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
        r"""修改实例参数
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param Parameters: 参数变更列表。

```json
请求体中传值(key-value形式放入所有要变更的参数-参数值)。
例如：
{
    "InstanceId": "***",
    "Parameters": {
        "keep_alive_timeout": "500"
    },
    "ConfigType": "Config"
}
```
        :type PathPrefix: String
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
        r"""查询实例当前参数
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
        r"""重置实例参数
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


class DescribeBucketsRequest(AbstractModel):
    """DescribeBuckets请求参数结构体
    """

    def __init__(self):
        r"""查询当前用桶列表
        """

    def _deserialize(self, params):
        return


class OperateHotAndColdSeparationRequest(AbstractModel):
    """OperateHotAndColdSeparation请求参数结构体
    """

    def __init__(self):
        r"""冷热数据分层配置
        """

    def _deserialize(self, params):
        return


class CreateInstanceAccountRequest(AbstractModel):
    """CreateInstanceAccount请求参数结构体
    """

    def __init__(self):
        r"""创建指定实例的数据库账号(普通用户)
        :param Name: 账号名称
        :type PathPrefix: String
        :param Password: 账号密码
        :type PathPrefix: String
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param Description: 账号描述
        :type PathPrefix: String
        """
        self.Name = None
        self.Password = None
        self.InstanceId = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Description"):
            self.Description = params.get("Description")


class ModifyInstanceAccountPrivilegesRequest(AbstractModel):
    """ModifyInstanceAccountPrivileges请求参数结构体
    """

    def __init__(self):
        r"""修改实例指定用户的数据库权限
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账号名称
        :type PathPrefix: String
        :param InstanceAccountPrivileges: 
        :type PathPrefix: Filter
        """
        self.InstanceId = None
        self.InstanceAccountName = None
        self.InstanceAccountPrivileges = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")
        if params.get("InstanceAccountPrivileges"):
            self.InstanceAccountPrivileges = params.get("InstanceAccountPrivileges")


class DeleteInstanceAccountRequest(AbstractModel):
    """DeleteInstanceAccount请求参数结构体
    """

    def __init__(self):
        r"""删除指定实例数据库账号
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账号名称
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstanceAccountName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")


class DescribeInstanceAccountsRequest(AbstractModel):
    """DescribeInstanceAccounts请求参数结构体
    """

    def __init__(self):
        r"""查询指定实例数据库账号列表
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeInstanceDatabasesRequest(AbstractModel):
    """DescribeInstanceDatabases请求参数结构体
    """

    def __init__(self):
        r"""查询库表列表
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class ModifyInstanceAccountInfoRequest(AbstractModel):
    """ModifyInstanceAccountInfo请求参数结构体
    """

    def __init__(self):
        r"""修改实例账号密码或者描述
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账号名称
        :type PathPrefix: String
        :param InstanceAccountPassword: 账号密码

```json
账号密码或者描述必须填写一项
```
        :type PathPrefix: String
        :param InstanceAccountDescription: 账号描述

```json
账号密码或者描述必须填写一项
```
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstanceAccountName = None
        self.InstanceAccountPassword = None
        self.InstanceAccountDescription = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")
        if params.get("InstanceAccountPassword"):
            self.InstanceAccountPassword = params.get("InstanceAccountPassword")
        if params.get("InstanceAccountDescription"):
            self.InstanceAccountDescription = params.get("InstanceAccountDescription")


class DescribeInstanceShardInfoRequest(AbstractModel):
    """DescribeInstanceShardInfo请求参数结构体
    """

    def __init__(self):
        r"""查询集群拓扑图(拓扑关系数据)
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class UpdateInstanceTrialOrderRequest(AbstractModel):
    """UpdateInstanceTrialOrder请求参数结构体
    """

    def __init__(self):
        r"""试用订单转正/延期
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param OperateType: 操作类型

```
延期：delay
购买：buy  

注意：无默认，不区分大小写
```
        :type PathPrefix: String
        :param Duration: 延期或转正时间指定

```json
默认1，按日结算和按量付费不用指定
```
        :type PathPrefix: Int
        :param BillType: 计费类型

```json
按量付费：87
按量付费（按日月结）：5
包年包月： 1
```
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.OperateType = None
        self.Duration = None
        self.BillType = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("OperateType"):
            self.OperateType = params.get("OperateType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("BillType"):
            self.BillType = params.get("BillType")


