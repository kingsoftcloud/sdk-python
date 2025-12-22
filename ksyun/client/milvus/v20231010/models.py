from ksyun.common.abstract_model import AbstractModel

class DeleteSecurityRulesRequest(AbstractModel):
    """DeleteSecurityRules请求参数结构体
    """

    def __init__(self):
        r"""删除安全组规则
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param RuleIds: 规则ID，支持批量(英文逗号隔开)
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.RuleIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("RuleIds"):
            self.RuleIds = params.get("RuleIds")


class CreateSecurityRulesRequest(AbstractModel):
    """CreateSecurityRules请求参数结构体
    """

    def __init__(self):
        r"""创建安全组规则
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param Rules: 安全组规则列表(支持多个)
        :type PathPrefix: Filter
        """
        self.SecurityGroupId = None
        self.Rules = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("Rules"):
            self.Rules = params.get("Rules")


class UnbindSecurityGroupInstancesRequest(AbstractModel):
    """UnbindSecurityGroupInstances请求参数结构体
    """

    def __init__(self):
        r"""解绑安全组已绑定实例
        :param SecurityGroupId: 安区组ID
        :type PathPrefix: String
        :param InstancesIds: 实例列表，支持批量(英文逗号隔开)
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.InstancesIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstancesIds"):
            self.InstancesIds = params.get("InstancesIds")


class BindSecurityGroupInstancesRequest(AbstractModel):
    """BindSecurityGroupInstances请求参数结构体
    """

    def __init__(self):
        r"""绑定实例至安全组
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param InstancesIds: 实例列表，支持批量(英文逗号隔开)
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.InstancesIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstancesIds"):
            self.InstancesIds = params.get("InstancesIds")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""删除安全组
        :param SecurityGroupIds: 安全组ID列表，支持批量(可英文逗号隔开)
        :type PathPrefix: String
        """
        self.SecurityGroupIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查询安全组详情
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        """
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""创建安全组
        :param Name: 安全组名称
        :type PathPrefix: String
        :param IpVersion: 安全组类型，现仅支持：ipv4
        :type PathPrefix: String
        :param Detail: 描述
        :type PathPrefix: String
        :param Rules: 安全组规则列表
        :type PathPrefix: Filter
        """
        self.Name = None
        self.IpVersion = None
        self.Detail = None
        self.Rules = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")
        if params.get("Detail"):
            self.Detail = params.get("Detail")
        if params.get("Rules"):
            self.Rules = params.get("Rules")


class ListSecurityGroupRequest(AbstractModel):
    """ListSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查询安全组列表
        :param Offset: 起始页，默认为0
        :type PathPrefix: Int
        :param Limit: 每页返回的条数
        :type PathPrefix: Int
        """
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体
    """

    def __init__(self):
        r"""删除milvus实例
        :param InstanceIds: 实例ID列表，可用英文逗号分隔，传递多个。
        :type PathPrefix: String
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体
    """

    def __init__(self):
        r"""查询milvus实例详情
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class ListInstanceRequest(AbstractModel):
    """ListInstance请求参数结构体
    """

    def __init__(self):
        r"""查询milvus实例列表
        :param Offset: 默认0开始，为第一页
        :type PathPrefix: String
        :param Limit: 请求是不传默认返回10条
        :type PathPrefix: String
        :param FuzzySearch: 支持实例ID/实例名称 模糊搜索
        :type PathPrefix: String
        :param SecBindingStatus: 支持过滤是否绑定安全组 可同模糊搜索一起使用
        :type PathPrefix: String
        """
        self.Offset = None
        self.Limit = None
        self.FuzzySearch = None
        self.SecBindingStatus = None

    def _deserialize(self, params):
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("SecBindingStatus"):
            self.SecBindingStatus = params.get("SecBindingStatus")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体
    """

    def __init__(self):
        r"""创建milvus实例
        :param InstanceName: 实例名称
        :type PathPrefix: String
        :param AdminPassword: 管理员账户密码
        :type PathPrefix: String
        :param SubnetId: 子网ID
        :type PathPrefix: String
        :param VnetId: 虚拟网络ID
        :type PathPrefix: String
        :param ProjectId: 项目id
        :type PathPrefix: String
        :param ProductType: 商品类型：现在仅支持容量型
PERFORMANCE："性能型"    CAPACITY："容量型"
        :type PathPrefix: String
        :param DBInstanceType: 实例类型：仅支持社区版
COMMUNITY 社区版
ENTERPRISE 企业版
        :type PathPrefix: String
        :param Az: 可用区列表(暂不支持多可用区)

```
支持指定可用区，现仅支持单可用区。
例如华北1(北京)：可指定cn-beijing-6a 或者 cn-beijing-6c
```
        :type PathPrefix: Array
        :param Engine: 引擎类型
        :type PathPrefix: String
        :param EngineVersion: 引擎版本(暂不支持其他版本)
        :type PathPrefix: String
        :param AdminUser: 管理员账户
        :type PathPrefix: String
        :param Cu: 配置信息(默认为1cu，若有需求请传入配置)
        :type PathPrefix: String
        """
        self.InstanceName = None
        self.AdminPassword = None
        self.SubnetId = None
        self.VnetId = None
        self.ProjectId = None
        self.ProductType = None
        self.DBInstanceType = None
        self.Az = None
        self.Engine = None
        self.EngineVersion = None
        self.AdminUser = None
        self.Cu = None

    def _deserialize(self, params):
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("AdminPassword"):
            self.AdminPassword = params.get("AdminPassword")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("Az"):
            self.Az = params.get("Az")
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("AdminUser"):
            self.AdminUser = params.get("AdminUser")
        if params.get("Cu"):
            self.Cu = params.get("Cu")


class ReleaseDBInstanceEipRequest(AbstractModel):
    """ReleaseDBInstanceEip请求参数结构体
    """

    def __init__(self):
        r"""实例-释放EIP
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class AllocateDBInstanceEipRequest(AbstractModel):
    """AllocateDBInstanceEip请求参数结构体
    """

    def __init__(self):
        r"""实例-申请EIP
        :param InstanceId: 实例Id
        :type PathPrefix: String
        :param Port: 是否指定EIP端口号，若不指定则自动分配
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.Port = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Port"):
            self.Port = params.get("Port")


class ListBackupRequest(AbstractModel):
    """ListBackup请求参数结构体
    """

    def __init__(self):
        r"""查询指定实例备份列表
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param BackupName: 备份名称(模糊查询)
        :type PathPrefix: String
        :param Offset: 开始页码

```json
注意：第一页默认页码0
```
        :type PathPrefix: Int
        :param Limit: 每页展示条数

```json
注意：默认每页展示10条
```
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.BackupName = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("BackupName"):
            self.BackupName = params.get("BackupName")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体
    """

    def __init__(self):
        r"""指定备份维度手动创建备份
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param BackupName: 备份名称
        :type PathPrefix: String
        :param DBCollection: 备份collection信息

```json
若要全部备份，则可以不填；
若要指定备份，则手动具体指定。
```
        :type PathPrefix: Array
        """
        self.InstanceId = None
        self.BackupName = None
        self.DBCollection = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("BackupName"):
            self.BackupName = params.get("BackupName")
        if params.get("DBCollection"):
            self.DBCollection = params.get("DBCollection")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup请求参数结构体
    """

    def __init__(self):
        r"""删除指定手动备份
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param BackupIds: 需要删除的备份id列表

```json
需要指定多个备份id，也用英文','间隔传入
```
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.BackupIds = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("BackupIds"):
            self.BackupIds = params.get("BackupIds")


class ListCollectionsRequest(AbstractModel):
    """ListCollections请求参数结构体
    """

    def __init__(self):
        r"""备份-查询实例库表详情
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Offset: 默认0开始，为第一页
        :type PathPrefix: Int
        :param Limit: 每页展示条数
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class UpdateInstanceTrialOrderRequest(AbstractModel):
    """UpdateInstanceTrialOrder请求参数结构体
    """

    def __init__(self):
        r"""适用类型订单实例转正/延期
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param OperateType: 操作类型

```json
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

注意：默认为87=按量付费
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


