from ksyun.common.abstract_model import AbstractModel

class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体
    """

    def __init__(self):
        r"""创建实例(指定实例类型)
        :param Mem: 内存大小

```json
只能购买特定规格的套餐
```
        :type PathPrefix: Int
        :param Disk: 磁盘大小


```json
只能购买特定规格的套餐
```
        :type PathPrefix: Int
        :param DBInstanceName: 实例名称

```json
不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
```
        :type PathPrefix: String
        :param Engine: 引擎名称

```json
区分大小写，取值范围：SQLServer
```
        :type PathPrefix: String
        :param EngineVersion: 引擎版本

```json
可根据用户及可用区配置；
2012sp4,2016sp2,2014sp2,2016sp2,2017
```
        :type PathPrefix: String
        :param DBInstanceType: 数据库实例类型

```json
HRDS_SS 高可用版
SS_HRDS_E 高可用云盘版
TRDS_SS 高可用临时版
SS_TRDS_E 临时云盘版
```
        :type PathPrefix: String
        :param MasterUserPassword: 数据库用户密码
```json
8-30个字符，必须包含大小写字母和数字，支持的特殊字符为!@#$%^&*()_+=-
```
        :type PathPrefix: String
        :param MasterUserName: 数据库用户名
```json
root, rdsrepladmin, rdsadmin不可用。
默认：admin 可以根据需求修改
```
        :type PathPrefix: String
        :param VpcId: VPC网络ID，可在网络控制台获取。
        :type PathPrefix: String
        :param SubnetId: SubnetId
        :type PathPrefix: String
        :param Port: 数据库连接端口
        :type PathPrefix: String
        :param PreferredBackupTime: 自动备份发起时间范围

```json
格式(hh:mm-hh:mm，如:01:00-02:00)，如不指定后台将随机分配
```
        :type PathPrefix: String
        :param DBParameterGroupId: 参数组id


```json
指定实例的参数组，如不指定，系统将采用默认的参数组来创建实例。用户需事先在控制台创建好参数组。
```
        :type PathPrefix: String
        :param SecurityGroupId: 安全组id，不传入默认为空
        :type PathPrefix: String
        :param BillType: 计费方式

```json
默认值：YEAR_MONTH;
取值范围：
YEAR_MONTH（包年包月）
DAY（按日计费）
HourlyInstantSettlement(按量计费)。

建议您指定计费方式！！！
```
        :type PathPrefix: String
        :param Duration: 购买时长
        :type PathPrefix: String
        :param DurationUnit: 购买时长单位


```json
取值范围：M（月），默认值：M（区分大小写）Y,M,D,H(年，月，天，小时)
```
        :type PathPrefix: String
        :param AvailabilityZone: 可用区字段

```json
示例(AvailabilityZone.1=cn-beijing-6a&AvailabilityZone.2=cn-beijing-6b)，表示实例的主副本在a区，备副本在b区。如果没有跨可用区的需求，建议将实例创建在云主机的可用区内已减少网络延时。
```
        :type PathPrefix: Filter
        :param ProjectId: 项目Id

```json
可从IAM获取ProjectId。可按项目来进行细粒度权限控制，将实例归类到某个项目下,不传时将实例归于默认项目
```
        :type PathPrefix: Int
        """
        self.Mem = None
        self.Disk = None
        self.DBInstanceName = None
        self.Engine = None
        self.EngineVersion = None
        self.DBInstanceType = None
        self.MasterUserPassword = None
        self.MasterUserName = None
        self.VpcId = None
        self.SubnetId = None
        self.Port = None
        self.PreferredBackupTime = None
        self.DBParameterGroupId = None
        self.SecurityGroupId = None
        self.BillType = None
        self.Duration = None
        self.DurationUnit = None
        self.AvailabilityZone = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("Mem"):
            self.Mem = params.get("Mem")
        if params.get("Disk"):
            self.Disk = params.get("Disk")
        if params.get("DBInstanceName"):
            self.DBInstanceName = params.get("DBInstanceName")
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("MasterUserPassword"):
            self.MasterUserPassword = params.get("MasterUserPassword")
        if params.get("MasterUserName"):
            self.MasterUserName = params.get("MasterUserName")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("Port"):
            self.Port = params.get("Port")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("DurationUnit"):
            self.DurationUnit = params.get("DurationUnit")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体
    """

    def __init__(self):
        r"""查询实例列表/详情
        :param DBInstanceIdentifier: 实例id 传入实例ID，获取的是该实例的详情，否则则获取list
        :type PathPrefix: String
        :param Keyword: 查询关键字

```json
支持：名称，ID，IP
```
        :type PathPrefix: String
        :param DBInstanceType: 实例类型


```json
高可用版：HRDS_SS
高可用云盘版：SS_HRDS_E
临时版：TRDS_SS
临时云盘版：SS_TRDS_E
```
        :type PathPrefix: String
        :param DBInstanceStatus: 实例状态-运行中/请续费

```json
运行中：active
请续费：invalid
注意：此类型为订单计费的情况
注意：控制台执行：状态-运行中，状态-请续费
```
        :type PathPrefix: String
        :param ExpiryDateLessThan: 实例状态-即将过期

```json
按照实例过期时间过滤，取值范围>0

注意：此参数一般用来概览实例计费情况
```
        :type PathPrefix: String
        :param Marker: 记录开始偏移量
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.Keyword = None
        self.DBInstanceType = None
        self.DBInstanceStatus = None
        self.ExpiryDateLessThan = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("DBInstanceStatus"):
            self.DBInstanceStatus = params.get("DBInstanceStatus")
        if params.get("ExpiryDateLessThan"):
            self.ExpiryDateLessThan = params.get("ExpiryDateLessThan")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class DeleteDBInstanceRequest(AbstractModel):
    """DeleteDBInstance请求参数结构体
    """

    def __init__(self):
        r"""删除实例(不支持批量)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifyDBInstanceRequest(AbstractModel):
    """ModifyDBInstance请求参数结构体
    """

    def __init__(self):
        r"""修改实例名称
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBInstanceName: 实例名称

```json
1-64个字符，支持中文，字母，数字，以及-_
```
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBInstanceName = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBInstanceName"):
            self.DBInstanceName = params.get("DBInstanceName")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""创建安全组
        :param SecurityGroupName: SecurityGroupName
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述
        :type PathPrefix: String
        :param DBInstanceIdentifier: 安全组绑定实例列表

```json
以英文逗号隔开。注意：需指定为绑定安全组的实例id
```
        :type PathPrefix: String
        :param SecurityGroupRule: 
        :type PathPrefix: Filter
        """
        self.SecurityGroupName = None
        self.SecurityGroupDescription = None
        self.DBInstanceIdentifier = None
        self.SecurityGroupRule = None

    def _deserialize(self, params):
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("SecurityGroupDescription"):
            self.SecurityGroupDescription = params.get("SecurityGroupDescription")
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("SecurityGroupRule"):
            self.SecurityGroupRule = params.get("SecurityGroupRule")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查询安全组列表/详情
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        """
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""删除安全组
        :param SecurityGroupIds: 安全组ID

```json
安全组ID，支持批量删除，每个ID中间用英文 ”,“  隔开
```
        :type PathPrefix: String
        """
        self.SecurityGroupIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")


class ModifySecurityGroupRequest(AbstractModel):
    """ModifySecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""修改安全组名称/描述
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupName: 安全组名称

```json
描述和名称至少填写一项
```


        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述
```json
描述和名称至少填写一项
```

        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDescription = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("SecurityGroupDescription"):
            self.SecurityGroupDescription = params.get("SecurityGroupDescription")


class CloneSecurityGroupRequest(AbstractModel):
    """CloneSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""克隆安全组
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupName: 安全组名称
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDescription = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("SecurityGroupDescription"):
            self.SecurityGroupDescription = params.get("SecurityGroupDescription")


class ModifySecurityGroupRuleRequest(AbstractModel):
    """ModifySecurityGroupRule请求参数结构体
    """

    def __init__(self):
        r"""修改安全组CIDR规则
        :param SecurityGroupRuleAction: 对安全组规则列表的操作

```json
Attach|Delete|Cover 
Attach: 将传入的规则列表（SecurityGroupRuleName，SecurityGroupRuleProtocol）追加到安全组规则列表内。所有绑定了此安全组的实例都会发生变化。 
Delete：从安全组中删除传入的规则列表（SecurityGroupRuleId）。所有绑定了此安全组的实例都会发生变化。 
Cover：用传入的规则列表（SecurityGroupRuleName，SecurityGroupRuleProtocol）覆盖安全组规则列表。所有绑定了此安全组的实例都会发生变化。
```
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupRule: 
        :type PathPrefix: Filter
        """
        self.SecurityGroupRuleAction = None
        self.SecurityGroupId = None
        self.SecurityGroupRule = None

    def _deserialize(self, params):
        if params.get("SecurityGroupRuleAction"):
            self.SecurityGroupRuleAction = params.get("SecurityGroupRuleAction")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupRule"):
            self.SecurityGroupRule = params.get("SecurityGroupRule")


class SecurityGroupRelationRequest(AbstractModel):
    """SecurityGroupRelation请求参数结构体
    """

    def __init__(self):
        r"""实例绑定/移除安全组
        :param RelationAction: 操作类型

```json
Attach | Dettach 
Attach: 添加实例Id到安全组 
Dettach：将实例Id从安全组解绑
```
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param DBInstanceIdentifier: 实例ID列表

```json
方式1：DBInstanceIdentifier.0=aaa&DBInstanceIdentifier.1=bbb
方式2：DBInstanceIdentifier=aaa,bbb
```
        :type PathPrefix: Filter
        """
        self.RelationAction = None
        self.SecurityGroupId = None
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("RelationAction"):
            self.RelationAction = params.get("RelationAction")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifySecurityGroupRuleNameRequest(AbstractModel):
    """ModifySecurityGroupRuleName请求参数结构体
    """

    def __init__(self):
        r"""修改安全组规则备注
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupRuleId: 安全组规则ID
        :type PathPrefix: String
        :param SecurityGroupRuleName: 安全组规则名称

```json
不传则清空当前备注
```
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupRuleId = None
        self.SecurityGroupRuleName = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupRuleId"):
            self.SecurityGroupRuleId = params.get("SecurityGroupRuleId")
        if params.get("SecurityGroupRuleName"):
            self.SecurityGroupRuleName = params.get("SecurityGroupRuleName")


class DescribeCollationsRequest(AbstractModel):
    """DescribeCollations请求参数结构体
    """

    def __init__(self):
        r"""查询支持字符集
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class CreateInstanceDatabaseRequest(AbstractModel):
    """CreateInstanceDatabase请求参数结构体
    """

    def __init__(self):
        r"""创建数据库
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称
        :type PathPrefix: String
        :param InstanceDatabaseCollation: 数据库字符集
        :type PathPrefix: String
        :param InstanceDatabaseDescription: 数据库描述

```json
必须中文、英文字母开头，可以包含数字、中文、英文、下划线（_）、短横线（-）
```
        :type PathPrefix: String
        :param InstanceDatabasePrivileges: 
        :type PathPrefix: Filter
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None
        self.InstanceDatabaseCollation = None
        self.InstanceDatabaseDescription = None
        self.InstanceDatabasePrivileges = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")
        if params.get("InstanceDatabaseCollation"):
            self.InstanceDatabaseCollation = params.get("InstanceDatabaseCollation")
        if params.get("InstanceDatabaseDescription"):
            self.InstanceDatabaseDescription = params.get("InstanceDatabaseDescription")
        if params.get("InstanceDatabasePrivileges"):
            self.InstanceDatabasePrivileges = params.get("InstanceDatabasePrivileges")


class ModifyInstanceDatabasePrivilegesRequest(AbstractModel):
    """ModifyInstanceDatabasePrivileges请求参数结构体
    """

    def __init__(self):
        r"""编辑数据库权限
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称
        :type PathPrefix: String
        :param InstanceDatabasePrivileges: 
        :type PathPrefix: Filter
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None
        self.InstanceDatabasePrivileges = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")
        if params.get("InstanceDatabasePrivileges"):
            self.InstanceDatabasePrivileges = params.get("InstanceDatabasePrivileges")


class DescribeInstanceDatabasesRequest(AbstractModel):
    """DescribeInstanceDatabases请求参数结构体
    """

    def __init__(self):
        r"""查询数据库列表/详情
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Keyword: 模糊查询
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Keyword = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")


class CreateInstanceAccountRequest(AbstractModel):
    """CreateInstanceAccount请求参数结构体
    """

    def __init__(self):
        r"""创建账号(可同时指定对应库权限)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账户名称

```json
root, rdsrepladmin, rdsadmin, dtsroot, sa不可用；由大小写字母、数字或下划线组成，以小写字母开头，以小写字母或数字结尾，长度为2~16个字符
```
        :type PathPrefix: String
        :param InstanceAccountPassword: 账户密码

```json
8-30个字符，必须包含大小写字母和数字；支持的特殊字符：!@#$%^&*()_+=-
```
        :type PathPrefix: String
        :param InstanceAccountDescription: 实例账号说明/描述
        :type PathPrefix: String
        :param InstanceAccountPrivileges: 实例账号权限列表
        :type PathPrefix: Filter
        """
        self.DBInstanceIdentifier = None
        self.InstanceAccountName = None
        self.InstanceAccountPassword = None
        self.InstanceAccountDescription = None
        self.InstanceAccountPrivileges = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")
        if params.get("InstanceAccountPassword"):
            self.InstanceAccountPassword = params.get("InstanceAccountPassword")
        if params.get("InstanceAccountDescription"):
            self.InstanceAccountDescription = params.get("InstanceAccountDescription")
        if params.get("InstanceAccountPrivileges"):
            self.InstanceAccountPrivileges = params.get("InstanceAccountPrivileges")


class DescribeInstanceAccountsRequest(AbstractModel):
    """DescribeInstanceAccounts请求参数结构体
    """

    def __init__(self):
        r"""查询账号列表/详情
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Keyword: 模糊查询，指定模糊查询的字段
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Keyword = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")


class ModifyInstanceAccountInfoRequest(AbstractModel):
    """ModifyInstanceAccountInfo请求参数结构体
    """

    def __init__(self):
        r"""修改账号密码/描述
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账号名称
        :type PathPrefix: String
        :param InstanceAccountDescription: 账号描述
        :type PathPrefix: String
        :param InstanceAccountPassword: 账号密码
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceAccountName = None
        self.InstanceAccountDescription = None
        self.InstanceAccountPassword = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")
        if params.get("InstanceAccountDescription"):
            self.InstanceAccountDescription = params.get("InstanceAccountDescription")
        if params.get("InstanceAccountPassword"):
            self.InstanceAccountPassword = params.get("InstanceAccountPassword")


class ModifyInstanceAccountPrivilegesRequest(AbstractModel):
    """ModifyInstanceAccountPrivileges请求参数结构体
    """

    def __init__(self):
        r"""编辑账号权限
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账号名称
        :type PathPrefix: String
        :param InstanceAccountPrivileges: 
```json
库名称和权限必须输入。例如(Get请求传List示例)：InstanceAccountPrivileges.InstanceDatabaseName.1:db_test_1 InstanceAccountPrivileges.Privilege.1:DBOwner
```
        :type PathPrefix: Filter
        """
        self.DBInstanceIdentifier = None
        self.InstanceAccountName = None
        self.InstanceAccountPrivileges = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")
        if params.get("InstanceAccountPrivileges"):
            self.InstanceAccountPrivileges = params.get("InstanceAccountPrivileges")


class DeleteInstanceAccountRequest(AbstractModel):
    """DeleteInstanceAccount请求参数结构体
    """

    def __init__(self):
        r"""删除账号(不支持批量)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账号名称
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceAccountName = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")


class DeleteInstanceDatabaseRequest(AbstractModel):
    """DeleteInstanceDatabase请求参数结构体
    """

    def __init__(self):
        r"""删除数据库
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")


class ModifyInstanceDatabaseInfoRequest(AbstractModel):
    """ModifyInstanceDatabaseInfo请求参数结构体
    """

    def __init__(self):
        r"""修改数据库描述
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称
        :type PathPrefix: String
        :param InstanceDatabaseDescription: 数据库描述
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None
        self.InstanceDatabaseDescription = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")
        if params.get("InstanceDatabaseDescription"):
            self.InstanceDatabaseDescription = params.get("InstanceDatabaseDescription")


class OverrideDBInstanceRequest(AbstractModel):
    """OverrideDBInstance请求参数结构体
    """

    def __init__(self):
        r"""恢复到当前实例(指定备份覆盖)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBBackupIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBBackupIdentifier"):
            self.DBBackupIdentifier = params.get("DBBackupIdentifier")


class RestoreDBInstanceFromDBBackupRequest(AbstractModel):
    """RestoreDBInstanceFromDBBackup请求参数结构体
    """

    def __init__(self):
        r"""恢复至新实例(基于备份)
        :param DBInstanceName: 数据库实例名称
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID


        :type PathPrefix: String
        :param DBInstanceType: 实例类型
        :type PathPrefix: String
        :param ProjectId: 项目ID


        :type PathPrefix: String
        :param AvailabilityZone: 实例可用区


        :type PathPrefix: String
        :param Duration: 时长 时长 默认值：1(单位:月) 注：billType=1(包年包月)则必填


        :type PathPrefix: Int
        :param DurationUnit: 时长单位 时长单位 默认值：M


        :type PathPrefix: String
        :param Port: 端口号 支持修改端口号


        :type PathPrefix: Int
        :param BillType: 计费方式：
	
```json
YEAR_MONTH(包年包月)
DAY(按量付费-按日月结)
HourlyInstantSettlement(按量付费-按小时结)
默认值：YEAR_MONTH
```
        :type PathPrefix: String
        """
        self.DBInstanceName = None
        self.DBBackupIdentifier = None
        self.DBInstanceType = None
        self.ProjectId = None
        self.AvailabilityZone = None
        self.Duration = None
        self.DurationUnit = None
        self.Port = None
        self.BillType = None

    def _deserialize(self, params):
        if params.get("DBInstanceName"):
            self.DBInstanceName = params.get("DBInstanceName")
        if params.get("DBBackupIdentifier"):
            self.DBBackupIdentifier = params.get("DBBackupIdentifier")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("DurationUnit"):
            self.DurationUnit = params.get("DurationUnit")
        if params.get("Port"):
            self.Port = params.get("Port")
        if params.get("BillType"):
            self.BillType = params.get("BillType")


class CreateDBBackupRequest(AbstractModel):
    """CreateDBBackup请求参数结构体
    """

    def __init__(self):
        r"""创建备份(手动备份)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupName: 数据库备份名称

```json
2-64个字符  
```
        :type PathPrefix: String
        :param Description: 备份描述

```json
2-128个字符
```
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBBackupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBBackupName"):
            self.DBBackupName = params.get("DBBackupName")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteDBBackupRequest(AbstractModel):
    """DeleteDBBackup请求参数结构体
    """

    def __init__(self):
        r"""删除备份(不支持批量)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBBackupIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBBackupIdentifier"):
            self.DBBackupIdentifier = params.get("DBBackupIdentifier")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups请求参数结构体
    """

    def __init__(self):
        r"""查询备份列表/详情
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Keyword: 模糊搜索

```json
依据备份名称过滤
```
        :type PathPrefix: String
        :param BackupType: 备份类型

```json
数据库快照类型，取值范围：
AutoBackup（自动产生的备份）
Snapshot（手动发起的备份）
```
        :type PathPrefix: String
        :param Marker: 获取记录开始偏移量
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.Keyword = None
        self.BackupType = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("BackupType"):
            self.BackupType = params.get("BackupType")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class ModifyDBBackupPolicyRequest(AbstractModel):
    """ModifyDBBackupPolicy请求参数结构体
    """

    def __init__(self):
        r"""修改备份策略
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param PreferredBackupTime: 全量备份时间段区间:
[00:00-01:00,23:00-24:00]
间隔一小时的整点时刻
        :type PathPrefix: String
        :param IncrementalBackupCycle: 增量备份时间间隔(小时):现在仅支持2,6或者12小时
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.PreferredBackupTime = None
        self.IncrementalBackupCycle = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")
        if params.get("IncrementalBackupCycle"):
            self.IncrementalBackupCycle = params.get("IncrementalBackupCycle")


class AllocateDBInstanceEipRequest(AbstractModel):
    """AllocateDBInstanceEip请求参数结构体
    """

    def __init__(self):
        r"""申请外网EIP
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Port: 放行端口号

```json
注意：[10000,65500]
```
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Port = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Port"):
            self.Port = params.get("Port")


class ReleaseDBInstanceEipRequest(AbstractModel):
    """ReleaseDBInstanceEip请求参数结构体
    """

    def __init__(self):
        r"""释放外网EIP
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ListSlowLogsRequest(AbstractModel):
    """ListSlowLogs请求参数结构体
    """

    def __init__(self):
        r"""查询慢日志列表信息
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Time: 查询时间
        :type PathPrefix: String
        :param OrderBy: 排序字段

```json
支持多个字段，中间以英文逗号隔开。若不传则默认以慢日志收集时间倒叙排序。
```
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Time = None
        self.OrderBy = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Time"):
            self.Time = params.get("Time")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")


class ListErrorLogsRequest(AbstractModel):
    """ListErrorLogs请求参数结构体
    """

    def __init__(self):
        r"""查询错误日志列表信息
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param StartTime: 开始时间
        :type PathPrefix: String
        :param EndTime: 结束时间
        :type PathPrefix: String
        :param Marker: 偏移量
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数

```json
Marker,MaxRecords类似数据库limit分页
```
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.StartTime = None
        self.EndTime = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec请求参数结构体
    """

    def __init__(self):
        r"""更配实例配置
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Mem: 内存规格
        :type PathPrefix: Int
        :param Disk: 磁盘规格
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.Mem = None
        self.Disk = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Mem"):
            self.Mem = params.get("Mem")
        if params.get("Disk"):
            self.Disk = params.get("Disk")


class DescribeImportTaskRequest(AbstractModel):
    """DescribeImportTask请求参数结构体
    """

    def __init__(self):
        r"""查询任务列表
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Keyword: 模糊查询
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Keyword = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")


class DescribeImportFileRequest(AbstractModel):
    """DescribeImportFile请求参数结构体
    """

    def __init__(self):
        r"""查询任务详情
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param ImportTaskId: 导入任务ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.ImportTaskId = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("ImportTaskId"):
            self.ImportTaskId = params.get("ImportTaskId")


class CreateImportTaskRequest(AbstractModel):
    """CreateImportTask请求参数结构体
    """

    def __init__(self):
        r"""创建任务(指定KS3桶备份)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param KS3Region: ks3的区域所在
        :type PathPrefix: String
        :param KS3Bucket: ks3的桶名称
        :type PathPrefix: String
        :param KS3Key: ks3中文件名称
        :type PathPrefix: String
        :param KS3FileSize: ks3文件大小
        :type PathPrefix: String
        :param ImportTaskId: 任务ID
        :type PathPrefix: String
        :param DBName: 数据库名称
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.KS3Region = None
        self.KS3Bucket = None
        self.KS3Key = None
        self.KS3FileSize = None
        self.ImportTaskId = None
        self.DBName = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("KS3Region"):
            self.KS3Region = params.get("KS3Region")
        if params.get("KS3Bucket"):
            self.KS3Bucket = params.get("KS3Bucket")
        if params.get("KS3Key"):
            self.KS3Key = params.get("KS3Key")
        if params.get("KS3FileSize"):
            self.KS3FileSize = params.get("KS3FileSize")
        if params.get("ImportTaskId"):
            self.ImportTaskId = params.get("ImportTaskId")
        if params.get("DBName"):
            self.DBName = params.get("DBName")


class FinishImportTaskRequest(AbstractModel):
    """FinishImportTask请求参数结构体
    """

    def __init__(self):
        r"""结束导入任务
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param ImportTaskId: 任务ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.ImportTaskId = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("ImportTaskId"):
            self.ImportTaskId = params.get("ImportTaskId")


class DescribeDBInstanceRestorableTimeRequest(AbstractModel):
    """DescribeDBInstanceRestorableTime请求参数结构体
    """

    def __init__(self):
        r"""查看实例恢复时间(库表恢复用)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class GetHistoryDatabaseInfoRequest(AbstractModel):
    """GetHistoryDatabaseInfo请求参数结构体
    """

    def __init__(self):
        r"""查询指定时间点/备份集附近的库表信息(库表恢复用)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID 根据备份集查询必传


        :type PathPrefix: String
        :param RestorableTime: 恢复时间 例如：2021-09-22 00:00:00 根据时间查询必传


        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBBackupIdentifier = None
        self.RestorableTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBBackupIdentifier"):
            self.DBBackupIdentifier = params.get("DBBackupIdentifier")
        if params.get("RestorableTime"):
            self.RestorableTime = params.get("RestorableTime")


class RestoreToCurInstanceRequest(AbstractModel):
    """RestoreToCurInstance请求参数结构体
    """

    def __init__(self):
        r"""恢复至源实例(指定具体库表)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID 根据备份恢复，必传备份ID，且必传SrcDatabases和DstDatabases


        :type PathPrefix: String
        :param RestorableTime: 恢复时间 根据时间点恢复，必传时间点，且必传SrcDatabases和DstDatabases；格式：yyyy-MM-dd HH:mm:ss


        :type PathPrefix: String
        :param SrcDatabases: ```json
源 [{
“DatabaseName”: “wang”,
“WholeDatabase”:“True”,
“TableNames”: [
“li”]
}]
```
        :type PathPrefix: Filter
        :param DstDatabases: ```json
目标 [{
“DatabaseName”: “wang”,
“WholeDatabase”:“True”,
“TableNames”: [
“li”]
}]
```
        :type PathPrefix: Filter
        """
        self.DBInstanceIdentifier = None
        self.DBBackupIdentifier = None
        self.RestorableTime = None
        self.SrcDatabases = None
        self.DstDatabases = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBBackupIdentifier"):
            self.DBBackupIdentifier = params.get("DBBackupIdentifier")
        if params.get("RestorableTime"):
            self.RestorableTime = params.get("RestorableTime")
        if params.get("SrcDatabases"):
            self.SrcDatabases = params.get("SrcDatabases")
        if params.get("DstDatabases"):
            self.DstDatabases = params.get("DstDatabases")


class ModifyInstanceDatabaseNameRequest(AbstractModel):
    """ModifyInstanceDatabaseName请求参数结构体
    """

    def __init__(self):
        r"""修改数据库名称
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称
        :type PathPrefix: String
        :param InstanceDatabaseNameNew: 数据库名称--新
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None
        self.InstanceDatabaseNameNew = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")
        if params.get("InstanceDatabaseNameNew"):
            self.InstanceDatabaseNameNew = params.get("InstanceDatabaseNameNew")


class RebootDBInstanceRequest(AbstractModel):
    """RebootDBInstance请求参数结构体
    """

    def __init__(self):
        r"""重启实例(指定实例)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class DescribeDBBackupPolicyRequest(AbstractModel):
    """DescribeDBBackupPolicy请求参数结构体
    """

    def __init__(self):
        r"""查询备份配置信息
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class UpdateDBInstanceOrderRequest(AbstractModel):
    """UpdateDBInstanceOrder请求参数结构体
    """

    def __init__(self):
        r"""试用订单延期/转正
        :param DBInstanceIdentifier: 实例Id
        :type PathPrefix: String
        :param UpdateUse: 操作类型

```json
试用延期：Renew
试用转正：Buy

```
        :type PathPrefix: String
        :param Duration: 持续时间

```json
注意：选定续费或者转正方式为包年包月是，需要指定持续时间；
```
        :type PathPrefix: Int
        :param BillType: 计费类型

```json
包年包月：YEAR_MONTH
按日月结（按日配置付费月结）：DAY
按小时实时结算：HourlyInstantSettlement

注意：若不选定计费类型，则默认为HourlyInstantSettlement
```
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.UpdateUse = None
        self.Duration = None
        self.BillType = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("UpdateUse"):
            self.UpdateUse = params.get("UpdateUse")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("BillType"):
            self.BillType = params.get("BillType")


class UpdateResourceProtectionRequest(AbstractModel):
    """UpdateResourceProtection请求参数结构体
    """

    def __init__(self):
        r"""删除保护设置
        :param DBInstanceIdentifier: 实例id
        :type PathPrefix: String
        :param ProtectionSwitch: 保护开关

```json
开启：ON 关闭：OFF 
```
        :type PathPrefix: String
        :param ProtectionReason: 操作理由
```json
限定64字符 
```
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.ProtectionSwitch = None
        self.ProtectionReason = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("ProtectionSwitch"):
            self.ProtectionSwitch = params.get("ProtectionSwitch")
        if params.get("ProtectionReason"):
            self.ProtectionReason = params.get("ProtectionReason")


