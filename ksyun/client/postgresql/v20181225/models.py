from ksyun.common.abstract_model import AbstractModel


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体
    """

    def __init__(self):
        r"""create db instance
        :param Mem: 客户只能购买特定规格的套餐，否则将会报错,    注:各规格对应连接数和iops见下方附表.

| 实例规格 | 最大连接数 | 读IOPS | 写IOPS | 对应磁盘取值范围(步长均为5) |
| :- | - | - | - | - |
| **1G** | 200 | 1200 | 1200 | *5~40* |
| **2G** | 400 | 2400 | 2400 | *5~80* |
| **4G** | 800 | 4800 | 4800 | *5~200* |
| **8G** | 1600 | 9600 | 9600 | *5~300* |
| **12G** | 2400 | 14400 | 14400 | *5~500* |
| **16G** | 3200 | 19200 | 19200 | *5~600* |
| **24G** | 4800 | 28800 | 28800 | *5~1000* |
| **32G** | 6400 | 38400 | 38400 | *5~1500* |
| **48G** | 9600 | 57600 |  57600 | *5~2000* |
        :type PathPrefix: Int
        :param Disk: 客户只能购买特定规格的套餐，单位为G,否则将会报错
        :type PathPrefix: Int
        :param DBInstanceName: 实例名称
不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param Engine: 实例数据库引擎名称
取固定值：postgresql
        :type PathPrefix: String
        :param EngineVersion: 实例数据库引擎版本
取值范围：9.6 |  10  |   11  |   12.5  |   13
        :type PathPrefix: String
        :param MasterUserPassword: 数据库用户密码
8-30个字符，必须包含大小写字母和数字，支持的特殊字符为!@#$%^&*()_+=-
        :type PathPrefix: String
        :param MasterUserName: 数据库用户名
root, rdsrepladmin, rdsadmin,dtsroot, postgres不可用
        :type PathPrefix: String
        :param DBInstanceType: 数据库类型,区分大小写,取固定值：高可用实例：HRDS_PG

        :type PathPrefix: String
        :param VpcId: VPC网络ID，可在网络控制台获取。
        :type PathPrefix: String
        :param SubnetId: 终端子网ID，可在网络控制台获取（注意类型必须为终端子网）。
        :type PathPrefix: String
        :param PreferredBackupTime: 自动备份发起时间范围
格式(hh:mm-hh:mm，如:01:00-02:00)，如不指定后台将随机分配
        :type PathPrefix: String
        :param DBParameterGroupId: 参数组id
指定实例的参数组，如不指定，系统将采用默认的参数组来创建实例。用户需事先在控制台创建好参数组。
        :type PathPrefix: String
        :param SecurityGroupId: 安全组id，不传入默认为空
        :type PathPrefix: String
        :param Port: 数据库连接端口,默认:5432
        :type PathPrefix: String
        :param BillType: 计费方式
默认值：YEAR_MONTH，取值范围：YEAR_MONTH（包年包月）,DAY（按日计费）。
        :type PathPrefix: String
        :param Duration: 购买时长
默认值：1 单位为月,选择YEAR_MONTH时计费方式必传.
        :type PathPrefix: String
        :param DurationUnit: 购买时长单位
取值范围：M（月），默认值：M（区分大小写）,选择YEAR_MONTH时计费方式必传.
        :type PathPrefix: String
        :param AvailabilityZone: 可用区字段;
示例(AvailabilityZone.1=cn-beijing-6a&AvailabilityZone.2=cn-beijing-6b)，表示实例的主副本在a区，备副本在b区。如果没有跨可用区的需求，建议将实例创建在云主机的可用区内已减少网络延时。
        :type PathPrefix: Filter
        :param ProjectId: 项目Id
可从IAM获取ProjectId。可按项目来进行细粒度权限控制，将实例归类到某个项目下
        :type PathPrefix: String
        """
        self.Mem = None
        self.Disk = None
        self.DBInstanceName = None
        self.Engine = None
        self.EngineVersion = None
        self.MasterUserPassword = None
        self.MasterUserName = None
        self.DBInstanceType = None
        self.VpcId = None
        self.SubnetId = None
        self.PreferredBackupTime = None
        self.DBParameterGroupId = None
        self.SecurityGroupId = None
        self.Port = None
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
        if params.get("MasterUserPassword"):
            self.MasterUserPassword = params.get("MasterUserPassword")
        if params.get("MasterUserName"):
            self.MasterUserName = params.get("MasterUserName")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("Port"):
            self.Port = params.get("Port")
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
        r"""describe db instances
        :param DBInstanceIdentifier: 实例id 传入实例ID，获取的是该实例的详情，否则则获取list
        :type PathPrefix: String
        :param DBInstanceType: 实例类型
取值范围: HRDS_PG高可用实例  TRDS_PG临时实例  RR_PG只读实例
        :type PathPrefix: String
        :param Keyword: 按单个名称/单个VIP模糊过滤
        :type PathPrefix: String
        :param Marker: 记录开始偏移量
默认0
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数；
默认10 取值10~10000
        :type PathPrefix: Int
        :param GroupId: 实例分组id
        :type PathPrefix: String
        :param ProjectId: 项目制Id，默认值为所有项目
        :type PathPrefix: String
        :param DBInstanceIdentifierIn: 实例id列表,中间用逗号隔开
        :type PathPrefix: String
        :param DBInstanceNameIn: 实例名称列表,用逗号隔开,支持模糊查询
        :type PathPrefix: String
        :param VipIn: vip列表，按IP地址筛选,可多选,中间逗号隔开
        :type PathPrefix: String
        :param ExpiryDateLessThan: 按照实例过期时间过滤，取值范围>0
        :type PathPrefix: Int
        :param Order: 排序方式，区分大小写，取值范围：DEFAULT（默认排序方式），GROUP（按复制组排序，会把只读实例排在所属主实例的后面）
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBInstanceType = None
        self.Keyword = None
        self.Marker = None
        self.MaxRecords = None
        self.GroupId = None
        self.ProjectId = None
        self.DBInstanceIdentifierIn = None
        self.DBInstanceNameIn = None
        self.VipIn = None
        self.ExpiryDateLessThan = None
        self.Order = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")
        if params.get("GroupId"):
            self.GroupId = params.get("GroupId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("DBInstanceIdentifierIn"):
            self.DBInstanceIdentifierIn = params.get("DBInstanceIdentifierIn")
        if params.get("DBInstanceNameIn"):
            self.DBInstanceNameIn = params.get("DBInstanceNameIn")
        if params.get("VipIn"):
            self.VipIn = params.get("VipIn")
        if params.get("ExpiryDateLessThan"):
            self.ExpiryDateLessThan = params.get("ExpiryDateLessThan")
        if params.get("Order"):
            self.Order = params.get("Order")


class DeleteDBInstanceRequest(AbstractModel):
    """DeleteDBInstance请求参数结构体
    """

    def __init__(self):
        r"""delete db instance
        :param DBInstanceIdentifier: 实例id
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class StatisticDBInstancesRequest(AbstractModel):
    """StatisticDBInstances请求参数结构体
    """

    def __init__(self):
        r"""statistic db instances
        :param ExpiryDateLessThan: 按照实例过期时间过滤，取值范围>1
        :type PathPrefix: String
        :param GroupId: 实例分组id
        :type PathPrefix: String
        :param Keyword: 按名称/VIP模糊过滤
        :type PathPrefix: String
        """
        self.ExpiryDateLessThan = None
        self.GroupId = None
        self.Keyword = None

    def _deserialize(self, params):
        if params.get("ExpiryDateLessThan"):
            self.ExpiryDateLessThan = params.get("ExpiryDateLessThan")
        if params.get("GroupId"):
            self.GroupId = params.get("GroupId")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")


class ModifyDBInstanceRequest(AbstractModel):
    """ModifyDBInstance请求参数结构体
    """

    def __init__(self):
        r"""modify db instance
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param PreferredBackupTime: 自动备份发起时间

格式(hh:mm-hh:mm，如:01:00-02:00)
        :type PathPrefix: String
        :param DBInstanceName: 实例新名称

不超过256个字节，仅支持中文、大小写字母、数字、减号、下划线和@#
        :type PathPrefix: String
        :param MasterUserPassword: 数据库用户密码

8-30个字符，必须包含大小写字母和数字，支持的特殊字符为!@#$%^&*()_=-   注：[不支持 + 号]
        :type PathPrefix: String
        :param DBParameterGroupId: 参数组id

租户的参数组id或者是官方的默认参数组id
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.PreferredBackupTime = None
        self.DBInstanceName = None
        self.MasterUserPassword = None
        self.DBParameterGroupId = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")
        if params.get("DBInstanceName"):
            self.DBInstanceName = params.get("DBInstanceName")
        if params.get("MasterUserPassword"):
            self.MasterUserPassword = params.get("MasterUserPassword")
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""create security group
        :param SecurityGroupName: 安全组名称
```json 
不超过256字符，中文，字母，数字，中划线，下划线
```
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述
```json
不超过256字符，中文，字母，数字，中划线，下划线
```
        :type PathPrefix: String
        :param DBInstanceIdentifier: 安全组绑定的实例列表

```json 
UUID格式，可填写未绑定过安全组的实例ID
```
        :type PathPrefix: Filter
        :param SecurityGroupRule: 安全组规则
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
        r"""describe security group
        :param SecurityGroupId: 安全组ID

```json
根据安全组ID筛选,若不指定则为查询列表
```
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
        r"""delete security group
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        """
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class ModifySecurityGroupRequest(AbstractModel):
    """ModifySecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""modify security group
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupName: 安全组名称
```json
不超过256个字符，中文，字母，数字，中划线，下划线
```
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述
```json
不超过256个字符，中文，字母，数字，中划线，下划线
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
        r"""clone security group
        :param SecurityGroupId: 安全组ID(源安全组ID)
        :type PathPrefix: String
        :param SecurityGroupName: 安全组名称

##### 不可超过256个字符，中文，字母，数字，中划线，下划线
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述

##### 安全组描述 支持1-64个字符 不可超过256个字符，中文，字母，数字，中划线，下划线
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
        r"""modify security grooup rule
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupRuleAction: 安全组规则操作

```json
1.取值范围:Attach|Delete|Cover
2.Attach: 将传入的规则列表（SecurityGroupRuleName，SecurityGroupRuleProtocol）追加到安全组规则列表内。所有绑定了此安全组的实例都会发生变化。 
3.Delete：从安全组中删除传入的规则列表（SecurityGroupRuleId）。所有绑定了此安全组的实例都会发生变化。
4.Cover：用传入的规则列表（SecurityGroupRuleName，SecurityGroupRuleProtocol）覆盖安全组规则列表。所有绑定了此安全组的实例都会发生变化。
```
        :type PathPrefix: String
        :param SecurityGroupRule: 
        :type PathPrefix: Filter
        """
        self.SecurityGroupId = None
        self.SecurityGroupRuleAction = None
        self.SecurityGroupRule = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupRuleAction"):
            self.SecurityGroupRuleAction = params.get("SecurityGroupRuleAction")
        if params.get("SecurityGroupRule"):
            self.SecurityGroupRule = params.get("SecurityGroupRule")


class SecurityGroupRelationRequest(AbstractModel):
    """SecurityGroupRelation请求参数结构体
    """

    def __init__(self):
        r"""security group relation
        :param RelationAction: 操作类型

```json
1.取值范围:Attach|Dettach 
2.Attach: 添加实例Id到安全组 
3.Dettach：将实例Id从安全组解绑
```
        :type PathPrefix: String
        :param SecurityGroupId: 安全组id
        :type PathPrefix: String
        :param DBInstanceIdentifier: 实例ID列表，支持批量
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
        r"""modify security group rule name
        :param SecurityGroupRuleId: 安全组规则ID
        :type PathPrefix: String
        :param SecurityGroupRuleName: 安全组规则名称

```json
安全组规则备注，不指定默认''
```
        :type PathPrefix: String
        """
        self.SecurityGroupRuleId = None
        self.SecurityGroupRuleName = None

    def _deserialize(self, params):
        if params.get("SecurityGroupRuleId"):
            self.SecurityGroupRuleId = params.get("SecurityGroupRuleId")
        if params.get("SecurityGroupRuleName"):
            self.SecurityGroupRuleName = params.get("SecurityGroupRuleName")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles请求参数结构体
    """

    def __init__(self):
        r"""describe db log files
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBLogType: 日志类型

##### 取值范围：Log/SlowLog/ErrorLog/Binlog
        :type PathPrefix: String
        :param StartTime: 日志开始记录时间
##### 按照yyyy-MM-dd HH:mm:ss格式
        :type PathPrefix: String
        :param EndTime: 日志结束记录时间
##### 按照yyyy-MM-dd HH:mm:ss格式
        :type PathPrefix: String
        :param MaxFileSize: 最大文件大小
##### 过滤文件大小大于MaxFileSize的文件，单位：字节
        :type PathPrefix: Int
        :param Marker: 偏移量
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数
##### 默认：200，区间 = [10,200]
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.DBLogType = None
        self.StartTime = None
        self.EndTime = None
        self.MaxFileSize = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBLogType"):
            self.DBLogType = params.get("DBLogType")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("MaxFileSize"):
            self.MaxFileSize = params.get("MaxFileSize")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class CreateDBBackupRequest(AbstractModel):
    """CreateDBBackup请求参数结构体
    """

    def __init__(self):
        r"""create db backup
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupName: 备份名称
        :type PathPrefix: String
        :param Description: 备份描述，控制台页面暂无填写入口，接口支持备份描述写入
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
        r"""delete db backup
        :param DBBackupIdentifier: 备份ID
        :type PathPrefix: String
        """
        self.DBBackupIdentifier = None

    def _deserialize(self, params):
        if params.get("DBBackupIdentifier"):
            self.DBBackupIdentifier = params.get("DBBackupIdentifier")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups请求参数结构体
    """

    def __init__(self):
        r"""describe db backups
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param BackupType: 数据库快照类型，取值范围：AutoBackup（自动产生的备份）、Snapshot（手动发起的备份）
        :type PathPrefix: String
        :param Keyword: 备份搜索关键字
        :type PathPrefix: String
        :param Marker: 获取记录开始偏移量

默认：0
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数

默认：10,区间10~100
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.BackupType = None
        self.Keyword = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("BackupType"):
            self.BackupType = params.get("BackupType")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class ModifyDBBackupPolicyRequest(AbstractModel):
    """ModifyDBBackupPolicy请求参数结构体
    """

    def __init__(self):
        r"""modify db backup policy
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param PreferredBackupTime: 备份时间段

例如：02:00-03:00，范围取值:[00:00-01:00,23:00-24:00], 间隔一小时的整点时刻
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.PreferredBackupTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")


class OverrideDBInstanceRequest(AbstractModel):
    """OverrideDBInstance请求参数结构体
    """

    def __init__(self):
        r"""override db instance
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


class CreateDBParameterGroupRequest(AbstractModel):
    """CreateDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""create db parameter group
        :param Engine: #### 数据库引擎名称
取值范围:PostgreSQL
        :type PathPrefix: String
        :param EngineVersion: #### 数据库引擎版本
取值范围:  9.6/12.5/9.4/11/10/13
        :type PathPrefix: String
        :param DBParameterGroupName: #### 参数组名称
        :type PathPrefix: String
        :param Description: #### 参数组描述
        :type PathPrefix: String
        :param Parameters: #### 参数详情
不传入指定参数及数值，则按照默认模板创建参数组
        :type PathPrefix: Filter
        """
        self.Engine = None
        self.EngineVersion = None
        self.DBParameterGroupName = None
        self.Description = None
        self.Parameters = None

    def _deserialize(self, params):
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("DBParameterGroupName"):
            self.DBParameterGroupName = params.get("DBParameterGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Parameters"):
            self.Parameters = params.get("Parameters")


class ModifyDBParameterGroupRequest(AbstractModel):
    """ModifyDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""modify db parameter group
        :param DBParameterGroupId: 参数组ID
        :type PathPrefix: String
        :param DBParameterGroupName: 参数组名称

	参数组名-参数值/参数组名称/参数组描述，至少填写一项
        :type PathPrefix: String
        :param Description: 参数组描述

	参数组名-参数值/参数组名称/参数组描述，至少填写一项
        :type PathPrefix: String
        :param Parameters: 参数值

	参数名与参数值同时填写；参数组名-参数值/参数组名称/参数组描述，至少填写一项
        :type PathPrefix: Filter
        """
        self.DBParameterGroupId = None
        self.DBParameterGroupName = None
        self.Description = None
        self.Parameters = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("DBParameterGroupName"):
            self.DBParameterGroupName = params.get("DBParameterGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Parameters"):
            self.Parameters = params.get("Parameters")


class DeleteDBParameterGroupRequest(AbstractModel):
    """DeleteDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""delete db parameter group
        :param DBParameterGroupId: #### 参数组ID
        :type PathPrefix: String
        """
        self.DBParameterGroupId = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")


class ResetDBParameterGroupRequest(AbstractModel):
    """ResetDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""reset db parameter grooup
        :param DBParameterGroupId: 参数组ID
        :type PathPrefix: String
        """
        self.DBParameterGroupId = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")


class DescribeDBParameterGroupRequest(AbstractModel):
    """DescribeDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""describe db parameter group
        :param DBParameterGroupId: 参数组id
        :type PathPrefix: String
        :param Marker: 获取记录开始偏移量

##### 默认：0,仅查询列表生效
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数

##### 默认：10,区间10~100，仅查询列表生效
        :type PathPrefix: Int
        :param Source: 参数模版类型

##### 默认查询：TEMPLATE 自建；DEFAULT 系统默认模版；INSTANCE 实例本身模版(参数配置)
##### 注意：切勿修改操作内置和实例本身模板(可能造成实例异常)！！！！！
        :type PathPrefix: String
        """
        self.DBParameterGroupId = None
        self.Marker = None
        self.MaxRecords = None
        self.Source = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")
        if params.get("Source"):
            self.Source = params.get("Source")


class DescribeEngineDefaultParametersRequest(AbstractModel):
    """DescribeEngineDefaultParameters请求参数结构体
    """

    def __init__(self):
        r"""describe engine default parameters
        :param Engine: 数据库引擎名称

	固定PostgreSQL
        :type PathPrefix: String
        :param EngineVersion: 引擎版本

	引擎名称和版本必须对应,目前支持的版本:9.6/10/11/12.5/13
        :type PathPrefix: String
        """
        self.Engine = None
        self.EngineVersion = None

    def _deserialize(self, params):
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")


class DescribeDBInstanceParametersRequest(AbstractModel):
    """DescribeDBInstanceParameters请求参数结构体
    """

    def __init__(self):
        r"""查看实例参数组
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class RebootDBInstanceRequest(AbstractModel):
    """RebootDBInstance请求参数结构体
    """

    def __init__(self):
        r"""reboot db instance
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class DescribeDBEngineVersionsRequest(AbstractModel):
    """DescribeDBEngineVersions请求参数结构体
    """

    def __init__(self):
        r"""describe db engine version
        """

    def _deserialize(self, params):
        return


class AllocateDBInstanceEipRequest(AbstractModel):
    """AllocateDBInstanceEip请求参数结构体
    """

    def __init__(self):
        r"""allocate db instance eip
        :param DBInstanceIdentifier: 实例id
        :type PathPrefix: String
        :param Port: 外网访问端口号,可设置外网访问端口号 范围:10000~65500
        :type PathPrefix: Int
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
        r"""release db instance eip
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec请求参数结构体
    """

    def __init__(self):
        r"""modify db instance spec
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Mem: 内存大小，客户只能购买特定规格的套餐，且需>=原规格.否则将会报错    注:各规格对应连接数和iops见下方附表.

| 实例规格 | 最大连接数 | 读IOPS | 写IOPS | 对应磁盘取值范围(步长均为5) |
| :- | - | - | - | - |
| **1G** | 200 | 1200 | 1200 | *5~40* |
| **2G** | 400 | 2400 | 2400 | *5~80* |
| **4G** | 800 | 4800 | 4800 | *5~200* |
| **8G** | 1600 | 9600 | 9600 | *5~300* |
| **12G** | 2400 | 14400 | 14400 | *5~500* |
| **16G** | 3200 | 19200 | 19200 | *5~600* |
| **24G** | 4800 | 28800 | 28800 | *5~1000* |
| **32G** | 6400 | 38400 | 38400 | *5~1500* |
| **48G** | 9600 | 57600 |  57600 | *5~2000* |
        :type PathPrefix: Int
        :param Disk: 磁盘大小，客户只能购买特定规格的套餐，单位为G,同规格内存只支持升配磁盘.否则将会报错    注:各配置取值范围见下方附表

| 实例规格 | 最大连接数 | 读IOPS | 写IOPS | 对应磁盘取值范围(步长均为5) |
| :- | - | - | - | - |
| **1G** | 200 | 1200 | 1200 | *5~40* |
| **2G** | 400 | 2400 | 2400 | *5~80* |
| **4G** | 800 | 4800 | 4800 | *5~200* |
| **8G** | 1600 | 9600 | 9600 | *5~300* |
| **12G** | 2400 | 14400 | 14400 | *5~500* |
| **16G** | 3200 | 19200 | 19200 | *5~600* |
| **24G** | 4800 | 28800 | 28800 | *5~1000* |
| **32G** | 6400 | 38400 | 38400 | *5~1500* |
| **48G** | 9600 | 57600 |  57600 | *5~2000* |
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


class RestoreDBInstanceFromDBBackupRequest(AbstractModel):
    """RestoreDBInstanceFromDBBackup请求参数结构体
    """

    def __init__(self):
        r"""restore db instance from db backup
        :param DBBackupIdentifier: #### 备份ID
        :type PathPrefix: String
        :param DBInstanceType: #### 实例类型
区分大小写，取固定值：高可用实例：HRDS_PG，临时实例：TRDS_PG
        :type PathPrefix: String
        :param DBInstanceName: #### 实例名称
不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param BillType: #### 计费方式
默认值：YEAR_MONTH，取值范围：YEAR_MONTH（包年包月）,DAY（按日计费）。
        :type PathPrefix: String
        :param Duration: #### 购买时长
取值范围：默认1。选择YEAR_MONTH时计费方式必传.
        :type PathPrefix: Int
        :param DurationUnit: #### 购买时长单位
取值范围：M（月），默认值：M（区分大小写）,选择YEAR_MONTH时计费方式必传.
        :type PathPrefix: String
        :param AvailabilityZone: #### 可用区字段
示例(AvailabilityZone.1=cn-beijing-6a&AvailabilityZone.2=cn-beijing-6b)，表示实例的主副本在a区，备副本在b区。如果没有跨可用区的需求，建议将实例创建在云主机的可用区内已减少网络延时。
        :type PathPrefix: Filter
        :param VpcId: ##### VPC网络ID，可在网络控制台获取。不传默认与原备份一致
        :type PathPrefix: String
        :param SubnetId: ##### 终端子网ID，可在网络控制台获取（注意类型必须为终端子网）。不传默认与原备份一致
        :type PathPrefix: String
        """
        self.DBBackupIdentifier = None
        self.DBInstanceType = None
        self.DBInstanceName = None
        self.BillType = None
        self.Duration = None
        self.DurationUnit = None
        self.AvailabilityZone = None
        self.VpcId = None
        self.SubnetId = None

    def _deserialize(self, params):
        if params.get("DBBackupIdentifier"):
            self.DBBackupIdentifier = params.get("DBBackupIdentifier")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("DBInstanceName"):
            self.DBInstanceName = params.get("DBInstanceName")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("DurationUnit"):
            self.DurationUnit = params.get("DurationUnit")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")


class SwitchDBInstanceHARequest(AbstractModel):
    """SwitchDBInstanceHA请求参数结构体
    """

    def __init__(self):
        r"""switch db instance ha
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class CreateDBInstanceReadReplicaRequest(AbstractModel):
    """CreateDBInstanceReadReplica请求参数结构体
    """

    def __init__(self):
        r"""create db instance read replica
        :param DBInstanceIdentifier: 主实例Id
        :type PathPrefix: String
        :param DBInstanceName: 实例名称

不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param AttachedVipId: 只读实例ip

共享同一主实例下的只读实例ip，默认创建一个新的ip
        :type PathPrefix: String
        :param BillType: 计费方式

YEAR_MONTH（包年包月）,DAY（按日计费），默认值：YEAR_MONTH
        :type PathPrefix: String
        :param Duration: 购买时长

时长 默认值：1(单位:月) 注：billType=1(包年包月)则必填
        :type PathPrefix: String
        :param DurationUnit: 购买时长单位

取值范围：M（月），默认值：M（区分大小写）
        :type PathPrefix: String
        :param AvailabilityZone: 可用区

示例(AvailabilityZone.1=cn-beijing-6a)，默认情况下只读实例可用区与主实例一致，如果主实例是跨可用区实例，只读实例会随机分布。
        :type PathPrefix: Filter
        :param Vip: 只读ip地址

选定的IP地址
        :type PathPrefix: String
        :param Mem: 实例内存大小,，参照附表范围填写
        :type PathPrefix: Int
        :param Disk: 实例硬盘大小，参照附表范围填写
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.DBInstanceName = None
        self.AttachedVipId = None
        self.BillType = None
        self.Duration = None
        self.DurationUnit = None
        self.AvailabilityZone = None
        self.Vip = None
        self.Mem = None
        self.Disk = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBInstanceName"):
            self.DBInstanceName = params.get("DBInstanceName")
        if params.get("AttachedVipId"):
            self.AttachedVipId = params.get("AttachedVipId")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("DurationUnit"):
            self.DurationUnit = params.get("DurationUnit")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("Vip"):
            self.Vip = params.get("Vip")
        if params.get("Mem"):
            self.Mem = params.get("Mem")
        if params.get("Disk"):
            self.Disk = params.get("Disk")


class ModifyInstanceAccountInfoRequest(AbstractModel):
    """ModifyInstanceAccountInfo请求参数结构体
    """

    def __init__(self):
        r"""modify instance account info
        :param DBInstanceIdentifier: 实例id
        :type PathPrefix: String
        :param InstanceAccountName: 实例名称
        :type PathPrefix: String
        :param InstanceAccountPassword: 实例密码
        :type PathPrefix: String
        :param InstanceAccountDescription: 数据库账户描述
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceAccountName = None
        self.InstanceAccountPassword = None
        self.InstanceAccountDescription = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")
        if params.get("InstanceAccountPassword"):
            self.InstanceAccountPassword = params.get("InstanceAccountPassword")
        if params.get("InstanceAccountDescription"):
            self.InstanceAccountDescription = params.get("InstanceAccountDescription")


class DescribeInstanceDatabasesRequest(AbstractModel):
    """DescribeInstanceDatabases请求参数结构体
    """

    def __init__(self):
        r"""获取实例数据库列表
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class DescribeDBInstanceExtensionsRequest(AbstractModel):
    """DescribeDBInstanceExtensions请求参数结构体
    """

    def __init__(self):
        r"""describe db instance extensions
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param KeyWord: 绑定类型(绑定/未绑定) 

```json
支持接口选定查询是否绑定，不传则都查询出来(绑定+解绑)；
installed
uninstalled
```
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.KeyWord = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("KeyWord"):
            self.KeyWord = params.get("KeyWord")


class ModifyDBInstanceExtensionRequest(AbstractModel):
    """ModifyDBInstanceExtension请求参数结构体
    """

    def __init__(self):
        r"""modify db instance extension
        :param DBInstanceIdentifier: 实例Id
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称

```json
注意：插件是'database'级别的，必须指定db
```
        :type PathPrefix: String
        :param Operation: 操作类型 

```json
1.默认放的:install
2.Install 安装
3.Uninstall 卸载(不支持)
```
        :type PathPrefix: String
        :param Extension: 插件列表

```json
注意：支持普通GET传List<string>的方式，也支持以Extension=aaa,bbb,ccc的形式传值
```
        :type PathPrefix: Filter
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None
        self.Operation = None
        self.Extension = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")
        if params.get("Operation"):
            self.Operation = params.get("Operation")
        if params.get("Extension"):
            self.Extension = params.get("Extension")
