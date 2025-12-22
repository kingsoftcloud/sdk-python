from ksyun.common.abstract_model import AbstractModel

class RebootDBInstanceRequest(AbstractModel):
    """RebootDBInstance请求参数结构体
    """

    def __init__(self):
        r"""重启指定实例
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifyDBParameterGroupRequest(AbstractModel):
    """ModifyDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""修改参数组
        :param DBParameterGroupId: 参数组ID
        :type PathPrefix: String
        :param Parameters: 参数名	参数名与参数值同时填写；参数组名-参数值/参数组名称/参数组描述，至少填写一项
        :type PathPrefix: Filter
        :param DBParameterGroupName: 参数组名称	请勿修改实例唯一参数组；参数组名-参数值/参数组名称/参数组描述，至少填写一项
        :type PathPrefix: String
        :param Description: 参数组描述	请勿修改实例唯一参数组；参数组名-参数值/参数组名称/参数组描述，至少填写一项
        :type PathPrefix: String
        """
        self.DBParameterGroupId = None
        self.Parameters = None
        self.DBParameterGroupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("Parameters"):
            self.Parameters = params.get("Parameters")
        if params.get("DBParameterGroupName"):
            self.DBParameterGroupName = params.get("DBParameterGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")


class ResetDBParameterGroupRequest(AbstractModel):
    """ResetDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""重置参数组
        :param DBParameterGroupId: 参数组ID	通过[参数组-列表（详情）接口](https://docs.ksyun.com/documents/344)获取
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
        r"""参数组列表/详情
        :param DBParameterGroupId: 参数组ID	UUID
        :type PathPrefix: String
        :param Keyword: 搜索关键字	根据name或description匹配出对应参数组
        :type PathPrefix: String
        :param Marker: 开始查询条数	默认：0
        :type PathPrefix: Int
        :param MaxRecords: 每页展示条数	默认：10，区间：[10,100]
        :type PathPrefix: Int
        :param Source: 模板类型	模板类型，取值范围：TEMPLATE/DEFAULT/INSTANCE<br>默认值：<br>TEMPLATE
        :type PathPrefix: String
        """
        self.DBParameterGroupId = None
        self.Keyword = None
        self.Marker = None
        self.MaxRecords = None
        self.Source = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
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
        r"""查询默认参数模版(指定引擎及版本号)
        :param Engine: 数据库引擎名称
        :type PathPrefix: String
        :param EngineVersion: 数据库引擎版本
        :type PathPrefix: String
        """
        self.Engine = None
        self.EngineVersion = None

    def _deserialize(self, params):
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")


class CreateDBParameterGroupRequest(AbstractModel):
    """CreateDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""创建参数组
        :param DBParameterGroupName: 参数组名称
        :type PathPrefix: String
        :param Engine: 数据库引擎名称	不同的数据库引擎，需要不同的数据库参数组<br>Engine与EngineVersion的对应关系：<br>mysql      5.5、5.6、5.7、8.0 <br> percona 5.6<br>consistent_mysql     5.7<br>ebs_mysql  5.6、5.7
        :type PathPrefix: String
        :param EngineVersion: 数据库引擎版本
        :type PathPrefix: String
        :param Parameters.Name: 参数名	参数名与参数值同时填写
        :type PathPrefix: Filter
        :param Parameters.Value: 参数值	
        :type PathPrefix: Filter
        :param Description: 参数组描述
        :type PathPrefix: String
        """
        self.DBParameterGroupName = None
        self.Engine = None
        self.EngineVersion = None
        self.Parameters_Name = None
        self.Parameters_Value = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupName"):
            self.DBParameterGroupName = params.get("DBParameterGroupName")
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("Parameters.Name"):
            self.Parameters_Name = params.get("Parameters.Name")
        if params.get("Parameters.Value"):
            self.Parameters_Value = params.get("Parameters.Value")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteDBParameterGroupRequest(AbstractModel):
    """DeleteDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""删除参数组
        :param DBParameterGroupId: 参数组ID
        :type PathPrefix: String
        """
        self.DBParameterGroupId = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体
    """

    def __init__(self):
        r"""创建实例(不含只读类型)
        :param Mem: 内存大小	客户只能购买特定规格的套餐，否则将会报错
        :type PathPrefix: Int
        :param Disk: 磁盘大小	客户只能购买特定规格的套餐，否则将会报错
        :type PathPrefix: Int
        :param DBInstanceName: 实例名称	不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param Engine: 实例中数据库引擎的名称	区分大小写，取值范围：mysql、percona，企业版：consistent_mysql(5.7)，云盘版：ebs_mysql（5.6/5.7）
        :type PathPrefix: String
        :param EngineVersion: 实例中数据库引擎的版本	取值范围：其中mysql支持：5.5、5.6、5.7、8.0；其中percona支持：5.6
        :type PathPrefix: String
        :param MasterUserPassword: 数据库用户密码	8-30个字符，必须包含大小写字母和数字，支持的特殊字符为!@#$%^&*()_+=-
        :type PathPrefix: String
        :param MasterUserName: 数据库用户名	root, rdsrepladmin, rdsadmin不可用
        :type PathPrefix: String
        :param DBInstanceType: 数据库类型	区分大小写,取值范围：高可用实例：HRDS、单实例：SINGLERDS、企业版：ERDS、云盘版：CDS_HRDS
        :type PathPrefix: String
        :param VpcId: VPC网络ID，可在网络控制台获取。
        :type PathPrefix: String
        :param SubnetId: VPC 终端子网ID，可在网络控制台获取（注意类型必须为终端子网）。
        :type PathPrefix: String
        :param PreferredBackupTime: 自动备份发起时间范围	格式(hh:mm-hh:mm，如:01:00-02:00)，如不指定后台将随机分配
        :type PathPrefix: String
        :param DBParameterGroupId: 参数组ID 指定实例的参数组，如不指定，系统将采用默认的参数组来创建实例。用户需事先在控制台创建好参数组。
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID。不传入默认为空
        :type PathPrefix: String
        :param Port: 数据库连接端口	默认3306
        :type PathPrefix: String
        :param BillType: 计费方式	默认值：YEAR_MONTH
```json
包年包月:YEAR_MONTH
按量付费(按日月结):DAY
按量付费:HourlyInstantSettlement

备注：
1.按日月结（按日配置付费月结）
2.按量付费 (按小时实时结算，按量实时计费&结算）
```
        :type PathPrefix: String
        :param Duration: 购买时长	默认值：1
        :type PathPrefix: String
        :param DurationUnit: 购买时长单位	取值范围：M（月），默认值：M（区分大小写）
        :type PathPrefix: String
        :param AvailabilityZone: 可用区字段	示例(AvailabilityZone.1=cn-beijing-6a&AvailabilityZone.2=cn-beijing-6b)，表示实例的主副本在a区，备副本在b区。如果没有跨可用区的需求，建议将实例创建在云主机的可用区内已减少网络延时。其中企业版ERDS可用区为3个（1主2备）
        :type PathPrefix: Filter
        :param ProjectId: 项目ID	可从IAM获取ProjectId。可按项目来进行细粒度权限控制，将实例归类到某个项目下
        :type PathPrefix: Int
        :param TableNamesAreCaseSensitive: 表名是否区分大小写	取值范围：1：表名不区分大小写    0：表名区分大小写。不传则默认为不区分大小写
        :type PathPrefix: Int
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
        self.TableNamesAreCaseSensitive = None

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
        if params.get("TableNamesAreCaseSensitive"):
            self.TableNamesAreCaseSensitive = params.get("TableNamesAreCaseSensitive")


class RestoreDBInstanceFromDBBackupRequest(AbstractModel):
    """RestoreDBInstanceFromDBBackup请求参数结构体
    """

    def __init__(self):
        r"""基于备份创建实例(临时/高可用)
        :param DBInstanceName: 实例名称
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID
        :type PathPrefix: String
        :param DBInstanceType: 实例类型		如，临时实例:TRDS,高可用实例:HRDS
        :type PathPrefix: String
        :param ProjectId: 项目ID
        :type PathPrefix: String
        :param AvailabilityZone: 实例可用区
        :type PathPrefix: String
        :param Duration: 时长	时长 默认值：1(单位:月) 注：billType=1(包年包月)则必填
        :type PathPrefix: Int
        :param DurationUnit: 时长单位	时长单位 默认值：M
        :type PathPrefix: String
        :param Port: 端口号	支持修改端口号
        :type PathPrefix: Int
        :param BillType: 计费方式：
YEAR_MONTH(包年包月),DAY(按量付费-按日月结),HourlyInstantSettlement(按量付费-按小时结)
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


class CreateDBInstanceReadReplicaRequest(AbstractModel):
    """CreateDBInstanceReadReplica请求参数结构体
    """

    def __init__(self):
        r"""创建只读实例(基于高可用实例)
        :param DBInstanceIdentifier: 主实例ID。一个主实例最多只能有3个只读实例。
        :type PathPrefix: String
        :param DBInstanceName: 实例名称	不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param AttachedVipId: 共享同一主实例下的只读实例IP，默认创建一个新的IP
        :type PathPrefix: String
        :param BillType: 计费方式	YEAR_MONTH（包年包月）,DAY（按日计费），默认值：YEAR_MONTH
        :type PathPrefix: String
        :param Duration: 购买时长	时长 默认值：1(单位:月) 注：billType=1(包年包月)则必填
        :type PathPrefix: String
        :param DurationUnit: 购买时长单位	 取值范围：M（月），默认值：M（区分大小写）
        :type PathPrefix: String
        :param AvailabilityZone.1: 可用区	示例(AvailabilityZone.1=cn-beijing-6a)，默认情况下只读实例可用区与主实例一致，如果主实例是跨可用区实例，只读实例会随机分布。
        :type PathPrefix: String
        :param ProjectId: 项目ID	可从IAM获取ProjectId
        :type PathPrefix: Int
        :param Vip: 只读IP地址	选定的IP地址
        :type PathPrefix: String
        :param Mem: 实例内存	实例内存大小
        :type PathPrefix: Int
        :param Disk: 实例硬盘	实例硬盘大小
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.DBInstanceName = None
        self.AttachedVipId = None
        self.BillType = None
        self.Duration = None
        self.DurationUnit = None
        self.AvailabilityZone_1 = None
        self.ProjectId = None
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
        if params.get("AvailabilityZone.1"):
            self.AvailabilityZone_1 = params.get("AvailabilityZone.1")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Vip"):
            self.Vip = params.get("Vip")
        if params.get("Mem"):
            self.Mem = params.get("Mem")
        if params.get("Disk"):
            self.Disk = params.get("Disk")


class RestoreDBInstanceToPointInTimeRequest(AbstractModel):
    """RestoreDBInstanceToPointInTime请求参数结构体
    """

    def __init__(self):
        r"""恢复数据到指定时间点(本实例/临时实例)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param RestorableTime: 恢复到时间点		例如：2021-09-09 00:00:00
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.RestorableTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("RestorableTime"):
            self.RestorableTime = params.get("RestorableTime")


class DescribeDBInstanceRestorableTimeRequest(AbstractModel):
    """DescribeDBInstanceRestorableTime请求参数结构体
    """

    def __init__(self):
        r"""查询可恢复到的时间点区间
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
        r"""修改实例配置
        :param DBInstanceIdentifier: 实例ID	
        :type PathPrefix: String
        :param PreferredBackupTime: 备份时间段		例如：02:00-03:00，范围取值:[00:00-01:00,23:00-24:00],  间隔一小时的整点时刻
        :type PathPrefix: String
        :param DBInstanceName: 实例新名称,不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
	
        :type PathPrefix: String
        :param DBParameterGroupId: 参数组ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.PreferredBackupTime = None
        self.DBInstanceName = None
        self.DBParameterGroupId = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")
        if params.get("DBInstanceName"):
            self.DBInstanceName = params.get("DBInstanceName")
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles请求参数结构体
    """

    def __init__(self):
        r"""查询日志文件列表
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBLogType: 日志类型	大小写敏感，取值范围：SlowLog\/ErrorLog\/Binlog
        :type PathPrefix: String
        :param Marker: 偏移量	默认： 0
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数	默认：200，区间 = [10,200]
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.DBLogType = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBLogType"):
            self.DBLogType = params.get("DBLogType")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups请求参数结构体
    """

    def __init__(self):
        r"""查询备份列表
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param BackupType: 数据库快照类型	数据库快照类型，取值范围：AutoBackup（自动产生的备份）、Snapshot（手动发起的备份）
        :type PathPrefix: String
        :param Keyword: 备份搜索关键字	备份搜索关键字（根据备份名字）
        :type PathPrefix: String
        :param Marker: 获取记录开始偏移量	默认：0，获取记录开始偏移量  default=0
        :type PathPrefix: String
        :param MaxRecords: 每页结果中包含的最大条数	默认：10，每页结果中包含的最大条数  区间 [10,100]
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


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec请求参数结构体
    """

    def __init__(self):
        r"""实例更配(修改内存磁盘配置)
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


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体
    """

    def __init__(self):
        r"""查询实例列表(详情)
        :param DBInstanceIdentifier: 实例ID（传入实例ID，获取的是该实例的详情，否则则获取list）
        :type PathPrefix: String
        :param DBInstanceType: 实例类型
HRDS（高可用）
RR（只读实例）
TRDS（临时实例）
SINGLERDS(单机版)
ERDS（三节点企业版）
CDS_HRDS(高可用_云盘版)
CDS_TRDS（临时云盘版）
        :type PathPrefix: String
        :param DBInstanceStatus: 按实例状态过滤
ACTIVE（运行中）
INVALID（请续费）
        :type PathPrefix: String
        :param Keyword: 按名称/VIP模糊过滤
        :type PathPrefix: String
        :param Order: 排序方式
区分大小写，取值范围：DEFAULT（默认排序方式），GROUP（按复制组排序，会把只读实例排在所属主实例的后面）
        :type PathPrefix: String
        :param ProjectId: 项目制Id
默认值为所有项目
        :type PathPrefix: String
        :param Marker: 记录开始偏移量
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数
取值范围：10-10000
        :type PathPrefix: Int
        :param DBInstanceIdentifierIn: 实例ids
实例id多选筛选   例如：DBInstanceIdentifierIn.0=xxx&DBInstanceIdentifierIn.1=xxx
        :type PathPrefix: Filter
        :param DBInstanceNameIn: 按实例名称过滤
示例(DBInstanceNameIn.1=test1，DBInstanceNameIn.2=test2)
        :type PathPrefix: Filter
        :param VipIn: 按vip过滤
示例(VipIn.1=10.9.2.3，VipIn.2=10.9.2.4)
        :type PathPrefix: Filter
        :param EIPIn: 按eip过滤
        :type PathPrefix: Filter
        :param ExpiryDateLessThan: 按照实例过期时间过滤
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.DBInstanceType = None
        self.DBInstanceStatus = None
        self.Keyword = None
        self.Order = None
        self.ProjectId = None
        self.Marker = None
        self.MaxRecords = None
        self.DBInstanceIdentifierIn = None
        self.DBInstanceNameIn = None
        self.VipIn = None
        self.EIPIn = None
        self.ExpiryDateLessThan = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("DBInstanceStatus"):
            self.DBInstanceStatus = params.get("DBInstanceStatus")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("Order"):
            self.Order = params.get("Order")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")
        if params.get("DBInstanceIdentifierIn"):
            self.DBInstanceIdentifierIn = params.get("DBInstanceIdentifierIn")
        if params.get("DBInstanceNameIn"):
            self.DBInstanceNameIn = params.get("DBInstanceNameIn")
        if params.get("VipIn"):
            self.VipIn = params.get("VipIn")
        if params.get("EIPIn"):
            self.EIPIn = params.get("EIPIn")
        if params.get("ExpiryDateLessThan"):
            self.ExpiryDateLessThan = params.get("ExpiryDateLessThan")


class OverrideDBInstanceRequest(AbstractModel):
    """OverrideDBInstance请求参数结构体
    """

    def __init__(self):
        r"""基于备份恢复到本实例
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


class DescribeDBEngineVersionsRequest(AbstractModel):
    """DescribeDBEngineVersions请求参数结构体
    """

    def __init__(self):
        r"""查询数据库引擎版本(全量)
        """

    def _deserialize(self, params):
        return


class UpgradeDBInstanceEngineVersionRequest(AbstractModel):
    """UpgradeDBInstanceEngineVersion请求参数结构体
    """

    def __init__(self):
        r"""大版本升级(5.x)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Engine: 实例中数据库引擎的名称	区分大小写、取值范围：mysql、percona
        :type PathPrefix: String
        :param EngineVersion: 实例中数据库引擎的版本	取值范围：5.5、5.6、5.7<br>mysql暂时不支持由5.7升级到8.0
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Engine = None
        self.EngineVersion = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")


class ModifyDBInstanceTypeRequest(AbstractModel):
    """ModifyDBInstanceType请求参数结构体
    """

    def __init__(self):
        r"""实例类型转换
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBInstanceType: 实例类型	目前支持：<br>1：HRDS（临时实例）升级为HA（高可用）<br>2：仅mysql5.7版本的高可用升级为（ERDS）三节点企业版
        :type PathPrefix: String
        :param BillType: 计费类型	计费类型<br>'YEAR_MONTH'：包年包月 <br>'DAY'：按天结
        :type PathPrefix: String
        :param Duration: 时长
        :type PathPrefix: Int
        :param DurationUnit: 时长单位
        :type PathPrefix: String
        :param AvailabilityZone: 可用区名称	可用区名称（升级为ERDS不支持此参数）
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBInstanceType = None
        self.BillType = None
        self.Duration = None
        self.DurationUnit = None
        self.AvailabilityZone = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBInstanceType"):
            self.DBInstanceType = params.get("DBInstanceType")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("DurationUnit"):
            self.DurationUnit = params.get("DurationUnit")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")


class DescribeDBInstanceParametersRequest(AbstractModel):
    """DescribeDBInstanceParameters请求参数结构体
    """

    def __init__(self):
        r"""查看运行中参数
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifyDBBackupPolicyRequest(AbstractModel):
    """ModifyDBBackupPolicy请求参数结构体
    """

    def __init__(self):
        r"""修改备份策略
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param PreferredBackupTime: 备份时间段。	例如：02:00-03:00，范围取值:[00:00-01:00,23:00-24:00],  间隔一小时的整点时刻。
        :type PathPrefix: String
        :param ExpireAfter: 备份保留天数。取值范围[7,1830]。
        :type PathPrefix: Int
        :param IncrementalBackupCycle: 增量备份策略，单位小时。可选：8，12，24。
        :type PathPrefix: String
        :param FullBackupCycle: 全量备份策略，单位星期。如"1,3,7"表示选择在星期一、星期三、星期日做备份。
        :type PathPrefix: String
        :param BinlogExpireAfter: bing过期时间；
默认：7 单位：天
        :type PathPrefix: Int
        :param HighFrequencyBackup: 高频备份开关(暂不支持修改)；
默认关闭：false
状态：flase 关闭  true 开启  
        :type PathPrefix: Boolean
        """
        self.DBInstanceIdentifier = None
        self.PreferredBackupTime = None
        self.ExpireAfter = None
        self.IncrementalBackupCycle = None
        self.FullBackupCycle = None
        self.BinlogExpireAfter = None
        self.HighFrequencyBackup = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("PreferredBackupTime"):
            self.PreferredBackupTime = params.get("PreferredBackupTime")
        if params.get("ExpireAfter"):
            self.ExpireAfter = params.get("ExpireAfter")
        if params.get("IncrementalBackupCycle"):
            self.IncrementalBackupCycle = params.get("IncrementalBackupCycle")
        if params.get("FullBackupCycle"):
            self.FullBackupCycle = params.get("FullBackupCycle")
        if params.get("BinlogExpireAfter"):
            self.BinlogExpireAfter = params.get("BinlogExpireAfter")
        if params.get("HighFrequencyBackup"):
            self.HighFrequencyBackup = params.get("HighFrequencyBackup")


class DescribeDBBackupPolicyRequest(AbstractModel):
    """DescribeDBBackupPolicy请求参数结构体
    """

    def __init__(self):
        r"""查询备份策略
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class DeleteDBBackupRequest(AbstractModel):
    """DeleteDBBackup请求参数结构体
    """

    def __init__(self):
        r"""删除快照备份
        :param DBBackupIdentifier: 备份ID
        :type PathPrefix: String
        """
        self.DBBackupIdentifier = None

    def _deserialize(self, params):
        if params.get("DBBackupIdentifier"):
            self.DBBackupIdentifier = params.get("DBBackupIdentifier")


class CreateDBBackupRequest(AbstractModel):
    """CreateDBBackup请求参数结构体
    """

    def __init__(self):
        r"""创建快照备份
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupName: 备份名称	2-64个字符，支持字母，数字，以及-_
        :type PathPrefix: String
        :param Description: 备份描述			前端页面暂时没有填写入口，接口支持填写备份描述
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


class SwitchDBInstanceHARequest(AbstractModel):
    """SwitchDBInstanceHA请求参数结构体
    """

    def __init__(self):
        r"""主备库切换
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class GenerateDBAdminURLRequest(AbstractModel):
    """GenerateDBAdminURL请求参数结构体
    """

    def __init__(self):
        r"""获取登录链接
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class AllocateDBInstanceEipRequest(AbstractModel):
    """AllocateDBInstanceEip请求参数结构体
    """

    def __init__(self):
        r"""申请外网访问IP地址
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Port: EIP端口号		固定取值：[10000,65500]    未指定则默认随机分配
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
        r"""释放外网访问IP地址
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifyDBInstanceAvailabilityZoneRequest(AbstractModel):
    """ModifyDBInstanceAvailabilityZone请求参数结构体
    """

    def __init__(self):
        r"""迁移可用区
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param AvailabilityZone.1: 主可用区	主所在可用区不可变
        :type PathPrefix: String
        :param AvailabilityZone.2: 备可用区
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.AvailabilityZone_1 = None
        self.AvailabilityZone_2 = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("AvailabilityZone.1"):
            self.AvailabilityZone_1 = params.get("AvailabilityZone.1")
        if params.get("AvailabilityZone.2"):
            self.AvailabilityZone_2 = params.get("AvailabilityZone.2")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""创建安全组(GET)
        :param SecurityGroupName: 安全组名称
        :type PathPrefix: String
        :param SecurityGroupRule: 安全组规则，支持以英文逗号隔开的传值形式，或者List<String>传值形式
        :type PathPrefix: Filter
        :param DBInstanceIdentifier: 实例id
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述
        :type PathPrefix: String
        """
        self.SecurityGroupName = None
        self.SecurityGroupRule = None
        self.DBInstanceIdentifier = None
        self.SecurityGroupDescription = None

    def _deserialize(self, params):
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("SecurityGroupRule"):
            self.SecurityGroupRule = params.get("SecurityGroupRule")
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("SecurityGroupDescription"):
            self.SecurityGroupDescription = params.get("SecurityGroupDescription")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查询安全组列表/详情
        :param SecurityGroupId: 安全组id
        :type PathPrefix: String
        :param Type: 安全组类型：IPV4 / IPV6 （默认IPV4）
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("Type"):
            self.Type = params.get("Type")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""删除安全组
        :param SecurityGroupIdList: 安全组ID列表，支持批量，用英文逗号隔开
        :type PathPrefix: String
        """
        self.SecurityGroupIdList = None

    def _deserialize(self, params):
        if params.get("SecurityGroupIdList"):
            self.SecurityGroupIdList = params.get("SecurityGroupIdList")


class ModifySecurityGroupRequest(AbstractModel):
    """ModifySecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""修改安全组(描述/名称)
        :param SecurityGroupId: 安全组id
        :type PathPrefix: String
        :param SecurityGroupName: 预期修改后的安全组名称
        :type PathPrefix: String
        :param SecurityGroupDescription: 预期修改后的安全组描述
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
        r"""克隆安全组(仅含CIDR规则)
        :param SecurityGroupId: 源端安全组id
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
        r"""修改安全组规则
        :param SecurityGroupRuleAction: 取值范围：Attach|Delete|Cover
Attach: 将传入的规则列表（SecurityGroupRuleName，SecurityGroupRuleProtocol）追加到安全组规则列表内。所有绑定了此安全组的实例都会发生变化。
Delete：从安全组中删除传入的规则列表（SecurityGroupRuleId）。所有绑定了此安全组的实例都会发生变化。
Cover：用传入的规则列表（SecurityGroupRuleName，SecurityGroupRuleProtocol）覆盖安全组规则列表。所有绑定了此安全组的实例都会发生变化。
        :type PathPrefix: String
        :param SecurityGroupId: 安全组Id
        :type PathPrefix: String
        :param SecurityGroupRule.SecurityGroupRuleId.N: 规则id列表. 如SecurityGroupRule.SecurityGroupRuleId.1=*****
        :type PathPrefix: String
        :param SecurityGroupRule.SecurityGroupRuleName.N: 规则名称列表。不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线。如SecurityGroupRule.SecurityGroupRuleName.1=***
        :type PathPrefix: String
        :param SecurityGroupRule.SecurityGroupRuleCidr.N: 规则协议列表。	0.0.0.0/32格式
        :type PathPrefix: String
        """
        self.SecurityGroupRuleAction = None
        self.SecurityGroupId = None
        self.SecurityGroupRule_SecurityGroupRuleId_N = None
        self.SecurityGroupRule_SecurityGroupRuleName_N = None
        self.SecurityGroupRule_SecurityGroupRuleCidr_N = None

    def _deserialize(self, params):
        if params.get("SecurityGroupRuleAction"):
            self.SecurityGroupRuleAction = params.get("SecurityGroupRuleAction")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupRule.SecurityGroupRuleId.N"):
            self.SecurityGroupRule_SecurityGroupRuleId_N = params.get("SecurityGroupRule.SecurityGroupRuleId.N")
        if params.get("SecurityGroupRule.SecurityGroupRuleName.N"):
            self.SecurityGroupRule_SecurityGroupRuleName_N = params.get("SecurityGroupRule.SecurityGroupRuleName.N")
        if params.get("SecurityGroupRule.SecurityGroupRuleCidr.N"):
            self.SecurityGroupRule_SecurityGroupRuleCidr_N = params.get("SecurityGroupRule.SecurityGroupRuleCidr.N")


class SecurityGroupRelationRequest(AbstractModel):
    """SecurityGroupRelation请求参数结构体
    """

    def __init__(self):
        r"""修改安全组绑定关系
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param RelationAction: 安全组操作
Attach：绑定
Dettach：解绑
        :type PathPrefix: String
        :param DBInstanceIdentifier: 实例ID列表
        :type PathPrefix: Filter
        """
        self.SecurityGroupId = None
        self.RelationAction = None
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("RelationAction"):
            self.RelationAction = params.get("RelationAction")
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifySecurityGroupRuleNameRequest(AbstractModel):
    """ModifySecurityGroupRuleName请求参数结构体
    """

    def __init__(self):
        r"""修改安全组规则名称
        :param SecurityGroupRuleId: 安全组规则id
        :type PathPrefix: String
        :param SecurityGroupRuleName: 安全组规则名称
        :type PathPrefix: String
        """
        self.SecurityGroupRuleId = None
        self.SecurityGroupRuleName = None

    def _deserialize(self, params):
        if params.get("SecurityGroupRuleId"):
            self.SecurityGroupRuleId = params.get("SecurityGroupRuleId")
        if params.get("SecurityGroupRuleName"):
            self.SecurityGroupRuleName = params.get("SecurityGroupRuleName")


class DescribeLastLogRequest(AbstractModel):
    """DescribeLastLog请求参数结构体
    """

    def __init__(self):
        r"""获取实时日志
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBLogType: 日志类型	大小写敏感，取值范围：SlowLog/ErrorLog/Binlog
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBLogType = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBLogType"):
            self.DBLogType = params.get("DBLogType")


class StartAuditRequest(AbstractModel):
    """StartAudit请求参数结构体
    """

    def __init__(self):
        r"""开启审计
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class StopAuditRequest(AbstractModel):
    """StopAudit请求参数结构体
    """

    def __init__(self):
        r"""关闭审计
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ListAuditRequest(AbstractModel):
    """ListAudit请求参数结构体
    """

    def __init__(self):
        r"""查询审计列表
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param AccessSqlStatement: 根据SQL操作命令筛选结果		例如：SELECT/INSERT/LOGOUT/CALL 可组合查询,字段以`/`分开
        :type PathPrefix: String
        :param AccessSqlLanguage: 根据访问SQL类型筛选结果		例如：DQL/DML;可组合查询,字段以`/`分开
        :type PathPrefix: String
        :param AccessDBName: 根据访问数据库名称筛选结果		例如：products；可组合查询,字段以`/`分开
        :type PathPrefix: String
        :param SourceIp: 根据来源Ip筛选结果		例如：10.208.0.100；可组合查询,字段以`/`分开
        :type PathPrefix: String
        :param AccessUsername: 根据登录用户名筛选结果		例如：rdsrepladmin；可组合查询,字段以`/`分开
        :type PathPrefix: String
        :param AuditBeginTime: 查询开始时间		例如：2021-08-31 19:47:37；同查询结束时间一起填写
        :type PathPrefix: String
        :param AuditEndTime: 查询结束时间		例如：2021-08-31 19:47:37；同查询开始时间一起填写
        :type PathPrefix: String
        :param RunResult: 执行结果		默认成功。0: 失败，1 成功；可组合查询,字段以`/`分开
        :type PathPrefix: String
        :param KeyWord: SQL模糊查询		默认无；<br>注意:<br>1.以`/`为分隔符隔开,并在末尾追加`&`或者`
        :type PathPrefix: String
        :param SortBy: 排序字段		例如：ExecTime；<br>注意：<br>支持且仅支持如下字段(支持小驼峰传参)：<br>Duration<br>RowSent<br>ExecTime
        :type PathPrefix: String
        :param SortWay: 排序方式		默认按照ExecTime倒叙排序；1-正序 2-倒序
        :type PathPrefix: String
        :param Marker: Offset，默认0		默认0
        :type PathPrefix: String
        :param MaxRecords: Limit，默认10		默认10，范围[10,10000]
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.AccessSqlStatement = None
        self.AccessSqlLanguage = None
        self.AccessDBName = None
        self.SourceIp = None
        self.AccessUsername = None
        self.AuditBeginTime = None
        self.AuditEndTime = None
        self.RunResult = None
        self.KeyWord = None
        self.SortBy = None
        self.SortWay = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("AccessSqlStatement"):
            self.AccessSqlStatement = params.get("AccessSqlStatement")
        if params.get("AccessSqlLanguage"):
            self.AccessSqlLanguage = params.get("AccessSqlLanguage")
        if params.get("AccessDBName"):
            self.AccessDBName = params.get("AccessDBName")
        if params.get("SourceIp"):
            self.SourceIp = params.get("SourceIp")
        if params.get("AccessUsername"):
            self.AccessUsername = params.get("AccessUsername")
        if params.get("AuditBeginTime"):
            self.AuditBeginTime = params.get("AuditBeginTime")
        if params.get("AuditEndTime"):
            self.AuditEndTime = params.get("AuditEndTime")
        if params.get("RunResult"):
            self.RunResult = params.get("RunResult")
        if params.get("KeyWord"):
            self.KeyWord = params.get("KeyWord")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")
        if params.get("SortWay"):
            self.SortWay = params.get("SortWay")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class AuditStatisticRequest(AbstractModel):
    """AuditStatistic请求参数结构体
    """

    def __init__(self):
        r"""查询审计统计数据列表
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param AuditStatisticBeginTime: 统计开始时间
        :type PathPrefix: String
        :param AuditStatisticEndTime: 统计结束时间
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.AuditStatisticBeginTime = None
        self.AuditStatisticEndTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("AuditStatisticBeginTime"):
            self.AuditStatisticBeginTime = params.get("AuditStatisticBeginTime")
        if params.get("AuditStatisticEndTime"):
            self.AuditStatisticEndTime = params.get("AuditStatisticEndTime")


class GetCurrentDatabaseInfoRequest(AbstractModel):
    """GetCurrentDatabaseInfo请求参数结构体
    """

    def __init__(self):
        r"""查询当前库表信息(前置)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class GetTableRestorableTimeRequest(AbstractModel):
    """GetTableRestorableTime请求参数结构体
    """

    def __init__(self):
        r"""获取可恢复时间段(前置)
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
        r"""获取指定时间点/备份集附近的库表信息
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID		根据备份集查询必传
        :type PathPrefix: String
        :param RestorableTime: 恢复时间	例如：2021-09-22 00:00:00        根据时间查询必传
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


class OverrideDBInstanceByPointInTimeRequest(AbstractModel):
    """OverrideDBInstanceByPointInTime请求参数结构体
    """

    def __init__(self):
        r"""恢复到原实例(指定时间点/备份集)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID			指定备份集恢复必传
        :type PathPrefix: String
        :param RestorableTime: 恢复的时间点		指定时间点恢复必传  yyyy-MM-dd HH:mm:ss
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
        r"""恢复到原实例(指定库表)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID	根据备份恢复，必传备份ID，且必传SrcDatabases和DstDatabases
        :type PathPrefix: String
        :param RestorableTime: 恢复时间		根据时间点恢复，必传时间点，且必传SrcDatabases和DstDatabases；格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param SrcDatabases: 源		[{<br>  "DatabaseName": "wang",<br>"WholeDatabase":"True",<br>"TableNames": [<br>"li"]<br>}]
        :type PathPrefix: Filter
        :param DstDatabases: 目标		[{<br>"DatabaseName": "wang",<br>"WholeDatabase":"True",<br>"TableNames": [<br> "li"]<br> }]
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


class RestoreToSgInstanceRequest(AbstractModel):
    """RestoreToSgInstance请求参数结构体
    """

    def __init__(self):
        r"""恢复到临时实例
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID	根据备份恢复，必传备份ID，且必传SrcDatabases和DstDatabases
        :type PathPrefix: String
        :param RestorableTime: 恢复时间		根据时间点恢复，必传时间点，且必传SrcDatabases和DstDatabases；格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param SrcDatabases: 源		[{<br>  "DatabaseName": "wang",<br>"WholeDatabase":"True",<br>"TableNames": [<br>"li"]<br>}]
        :type PathPrefix: Filter
        :param DstDatabases: 目标		[{<br>"DatabaseName": "wang",<br>"WholeDatabase":"True",<br>"TableNames": [<br> "li"]<br> }]
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


class DescribeAuditHotCountRequest(AbstractModel):
    """DescribeAuditHotCount请求参数结构体
    """

    def __init__(self):
        r"""某时段SQL执行次数TOP10查询
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param TimeRange: 查询间隔		最近1小时：LASTEST_ONE_HOUR<br>最近3小时：LASTEST_THREE_HOUR<br>最近1天：LASTEST_ONE_DAY<br>最近1周：LASTEST_ONE_WEEK<br>自定义查询时间：CUSTOM<br>注意：自定义查询时间的时候必须填写startTime和endTime<br>注意：最近1小时，最近3小时均以5分钟为时间间隔聚合；最近一天以30分钟聚合；最近一周以6小时聚合
        :type PathPrefix: String
        :param StartTime: 查询开始时间
        :type PathPrefix: String
        :param EndTime: 查询结束时间
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.TimeRange = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("TimeRange"):
            self.TimeRange = params.get("TimeRange")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class DescribeAuditHotDurationRequest(AbstractModel):
    """DescribeAuditHotDuration请求参数结构体
    """

    def __init__(self):
        r"""某时段SQL执行耗时TOP10查询
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param TimeRange: 查询间隔		最近1小时：LASTEST_ONE_HOUR<br>最近3小时：LASTEST_THREE_HOUR<br>最近1天：LASTEST_ONE_DAY<br>最近1周：LASTEST_ONE_WEEK<br>自定义查询时间：CUSTOM<br>注意：自定义查询时间的时候必须填写startTime和endTime<br>注意：最近1小时，最近3小时均以5分钟为时间间隔聚合；最近一天以30分钟聚合；最近一周以6小时聚合
        :type PathPrefix: String
        :param StartTime: 查询开始时间
        :type PathPrefix: String
        :param EndTime: 查询结束时间
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.TimeRange = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("TimeRange"):
            self.TimeRange = params.get("TimeRange")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class SqlAuditReportRequest(AbstractModel):
    """SqlAuditReport请求参数结构体
    """

    def __init__(self):
        r"""某时段全量SQL统计
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param TimeRange: 查询间隔		最近1小时：LASTEST_ONE_HOUR<br>最近3小时：LASTEST_THREE_HOUR<br>最近1天：LASTEST_ONE_DAY<br>最近1周：LASTEST_ONE_WEEK<br>自定义查询时间：CUSTOM<br>注意：自定义查询时间的时候必须填写startTime和endTime<br>注意：最近1小时，最近3小时均以5分钟为时间间隔聚合；最近一天以30分钟聚合；最近一周以6小时聚合
        :type PathPrefix: String
        :param StartTime: 查询开始时间		例如：2021-09-01 14:42:51
        :type PathPrefix: String
        :param EndTime: 查询结束时间		例如：2021-09-01 13:42:51
        :type PathPrefix: String
        :param DbName: 数据库名称
        :type PathPrefix: String
        :param SortBy: 排序字段		默认执行次数(count)倒序排序：<br>排序字段：<br>count：执行次数<br>countRatio：执行次数比例<br>durationAvg: 平均执行耗时<br>durationRatio: 执行耗时占比
        :type PathPrefix: String
        :param SortWay: 排序方式		默认：1 <br>可填1：倒序(降序)<br>可填0：正序(降序)
        :type PathPrefix: Int
        :param Page: 页码		默认：1
        :type PathPrefix: Int
        :param Size: 每页条数		默认：15，可填区间:[15，100]
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.TimeRange = None
        self.StartTime = None
        self.EndTime = None
        self.DbName = None
        self.SortBy = None
        self.SortWay = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("TimeRange"):
            self.TimeRange = params.get("TimeRange")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("DbName"):
            self.DbName = params.get("DbName")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")
        if params.get("SortWay"):
            self.SortWay = params.get("SortWay")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class SqlAuditLineChartRequest(AbstractModel):
    """SqlAuditLineChart请求参数结构体
    """

    def __init__(self):
        r"""某时段全量SQL折线图
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param TimeRange: 查询间隔		最近1小时：LASTEST_ONE_HOUR<br>最近3小时：LASTEST_THREE_HOUR<br>最近1天：LASTEST_ONE_DAY<br>最近1周：LASTEST_ONE_WEEK<br>自定义查询时间：CUSTOM<br>注意：自定义查询时间的时候必须填写startTime和endTime<br>注意：最近1小时，最近3小时均以5分钟为时间间隔聚合；最近一天以30分钟聚合；最近一周以6小时聚合
        :type PathPrefix: String
        :param StartTime: 查询开始时间		例如：2021-09-01 14:42:51
        :type PathPrefix: String
        :param EndTime: 查询结束时间		例如：2021-09-01 13:42:51
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.TimeRange = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("TimeRange"):
            self.TimeRange = params.get("TimeRange")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class SlowLogReportRequest(AbstractModel):
    """SlowLogReport请求参数结构体
    """

    def __init__(self):
        r"""慢日志统计
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param StartTime: 时间区间开始		yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param EndTime: 时间区间结束		yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param SortBy: queryCount/ 查询条数
queryTimeAvg/ 查询平均时间
queryTimeMax/ 查询最大时间
lockTimeAvg/ 平均等待时间
lockTimeMax/ 最大等待时间
rowsExaminedAvg/ 平均扫描行
rowsExaminedMax/ 最大扫描行
rowsSentAvg/ 平均返回行
rowsSentMax 最大返回行
processingTime 处理时间(不传排序字段和方式默认处理时间倒序)
        :type PathPrefix: String
        :param SortWay: 排序规则
ASC 正序(升序)
DESC 倒序(倒列)
        :type PathPrefix: String
        :param HeadKey: 以INSERT、UPDATE、DELETE、SELECT为首进行匹配
        :type PathPrefix: String
        :param Marker: 偏移量
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数
默认：0，区间 [10,10000]
        :type PathPrefix: Int
        """
        self.DBInstanceIdentifier = None
        self.StartTime = None
        self.EndTime = None
        self.SortBy = None
        self.SortWay = None
        self.HeadKey = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")
        if params.get("SortWay"):
            self.SortWay = params.get("SortWay")
        if params.get("HeadKey"):
            self.HeadKey = params.get("HeadKey")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class SlowLogLineChartRequest(AbstractModel):
    """SlowLogLineChart请求参数结构体
    """

    def __init__(self):
        r"""慢日志趋势图(折线图展示)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param StartTime: 开始时间	yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param EndTime: 结束时间	yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class SlowLogDetailRequest(AbstractModel):
    """SlowLogDetail请求参数结构体
    """

    def __init__(self):
        r"""慢日志详情
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param StartTime: 时间区间开始
yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param EndTime: 时间区间结束
yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param SortBy: 排序字段

sqlExecTimeStamp：执行完成时间
currentUser：用户
hostname：客户端ip
queryTime： 执行耗时
lockTime：锁等待时间
rowsExamined：扫描行
rowsSent：返回行
        :type PathPrefix: String
        :param SortWay: 排序规则	
1-正序 2-倒序
        :type PathPrefix: String
        :param HeadKey: 多选匹配	
以INSERT、UPDATE、DELETE、SELECT为首进行匹配,支持多选以|隔开，例如：HeadKey: SELECT|IN
        :type PathPrefix: String
        :param FingerPrint: 具体模板
        :type PathPrefix: String
        :param checksum: 标识
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.StartTime = None
        self.EndTime = None
        self.SortBy = None
        self.SortWay = None
        self.HeadKey = None
        self.FingerPrint = None
        self.checksum = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")
        if params.get("SortWay"):
            self.SortWay = params.get("SortWay")
        if params.get("HeadKey"):
            self.HeadKey = params.get("HeadKey")
        if params.get("FingerPrint"):
            self.FingerPrint = params.get("FingerPrint")
        if params.get("checksum"):
            self.checksum = params.get("checksum")


class StartAuditDetailExportTaskRequest(AbstractModel):
    """StartAuditDetailExportTask请求参数结构体
    """

    def __init__(self):
        r"""创建导出任务
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param ExportFileds: 导出字段选择
例如：ExecTime,Sql
可选择多个参数，以,进行隔开
ExecTime:执行完成时间
Sql：SQL
DbName：数据库名称
UserName：用户名称
SourceIp：客户端IP
RunResult：状态
RowSent：更新行数
Duration：执行耗时
        :type PathPrefix: String
        :param AuditBeginTime: 导出开始时间
例如：2021-08-31 14:14:55
        :type PathPrefix: String
        :param AuditEndTime: 导出结束时间
例如：2021-08-31 14:14:55
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.ExportFileds = None
        self.AuditBeginTime = None
        self.AuditEndTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("ExportFileds"):
            self.ExportFileds = params.get("ExportFileds")
        if params.get("AuditBeginTime"):
            self.AuditBeginTime = params.get("AuditBeginTime")
        if params.get("AuditEndTime"):
            self.AuditEndTime = params.get("AuditEndTime")


class ListAuditDetailExportTaskRequest(AbstractModel):
    """ListAuditDetailExportTask请求参数结构体
    """

    def __init__(self):
        r"""导出任务列表(任务详情可下载)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Marker: 查询开始条数
        :type PathPrefix: String
        :param MaxRecords: 查询每页暂时条数
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class CreateInstanceAccountRequest(AbstractModel):
    """CreateInstanceAccount请求参数结构体
    """

    def __init__(self):
        r"""创建数据库账户(GET)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账号名称	。root, rdsrepladmin, rdsadmin, dtsroot, sa不可用；由大小写字母、数字或下划线组成，以小写字母开头，以小写字母或数字结尾，长度为2~16个字符。
        :type PathPrefix: String
        :param InstanceAccountPassword: 账号密码	。8-30个字符，必须包含大小写字母和数字；支持的特殊字符：!@#$%^&*()_+=-
        :type PathPrefix: String
        :param InstanceAccountDescription: 数据库账号描述。
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


class DescribeInstanceAccountsRequest(AbstractModel):
    """DescribeInstanceAccounts请求参数结构体
    """

    def __init__(self):
        r"""查询数据库账户列表
        :param DBInstanceIdentifier: 实例ID 
        :type PathPrefix: String
        :param Keyword: 模糊查询。
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
        r"""修改数据库账户信息
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 数据库帐号名称
        :type PathPrefix: String
        :param InstanceAccountPassword: 数据库帐号新密码		必须包含大小写字母和数字，支持的特殊字符为!@#$%^&*()_+=-
        :type PathPrefix: String
        :param InstanceAccountDescription: 数据库帐号描述		帐号描述不填则不作修改
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


class ModifyInstanceAccountPrivilegesRequest(AbstractModel):
    """ModifyInstanceAccountPrivileges请求参数结构体
    """

    def __init__(self):
        r"""数据库账户赋权(GET)
        :param DBInstanceIdentifier: 实例id
        :type PathPrefix: String
        :param InstanceAccountName: 实例名称
        :type PathPrefix: String
        :param InstanceAccountPrivileges: 账户权限
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
        r"""删除数据库账户(GET)
        :param DBInstanceIdentifier: 实例id。
        :type PathPrefix: String
        :param InstanceAccountName: 账户名称
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceAccountName = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")


class DescribeCollationsRequest(AbstractModel):
    """DescribeCollations请求参数结构体
    """

    def __init__(self):
        r"""查询字符集列表(指定实例)
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
        r"""创建实例数据库
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称。		由小写字母、数字、下划线或中划线组成，以字母开头，以字母或数字结尾，长度为2~64个字符
        :type PathPrefix: String
        :param InstanceDatabaseCollation: 数据库字符集		非必填，默认为UTF-8：utf8_general_ci （DescribeCollations接口获取)
        :type PathPrefix: String
        :param InstanceDatabaseDescription: 数据库描述		必须中文、英文字母开头，可以包含数字、中文、英文、下划线（_）、短横线（-）
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None
        self.InstanceDatabaseCollation = None
        self.InstanceDatabaseDescription = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")
        if params.get("InstanceDatabaseCollation"):
            self.InstanceDatabaseCollation = params.get("InstanceDatabaseCollation")
        if params.get("InstanceDatabaseDescription"):
            self.InstanceDatabaseDescription = params.get("InstanceDatabaseDescription")


class ModifyInstanceDatabasePrivilegesRequest(AbstractModel):
    """ModifyInstanceDatabasePrivileges请求参数结构体
    """

    def __init__(self):
        r"""数据库授权(GET)
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
        r"""查询实例库列表
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称准确查询
        :type PathPrefix: String
        :param Keyword: 数据库名称模糊查询
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None
        self.Keyword = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")


class ModifyInstanceDatabaseInfoRequest(AbstractModel):
    """ModifyInstanceDatabaseInfo请求参数结构体
    """

    def __init__(self):
        r"""修改数据库信息
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称
        :type PathPrefix: String
        :param InstanceDatabaseDescription: 数据库描述		不传为置空数据库描述
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


class StartSlowLogDetailExportTaskRequest(AbstractModel):
    """StartSlowLogDetailExportTask请求参数结构体
    """

    def __init__(self):
        r"""创建慢日志导出任务
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param AuditBeginTime: 开始时间	yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param AuditEndTime: 结束时间	yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param AccessSqlStatement: 查询类型		可多选,以\`,`分开； SELECT,INSERT,UPDATE,DELETE,OTHER
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.AuditBeginTime = None
        self.AuditEndTime = None
        self.AccessSqlStatement = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("AuditBeginTime"):
            self.AuditBeginTime = params.get("AuditBeginTime")
        if params.get("AuditEndTime"):
            self.AuditEndTime = params.get("AuditEndTime")
        if params.get("AccessSqlStatement"):
            self.AccessSqlStatement = params.get("AccessSqlStatement")


class ListSlowLogDetailExportTaskRequest(AbstractModel):
    """ListSlowLogDetailExportTask请求参数结构体
    """

    def __init__(self):
        r"""查询导出任务列表
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Marker: 当前条：默认0
        :type PathPrefix: String
        :param MaxRecords: 每页显示大小，默认10		区间 ：[10,10000]
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class CreateInstanceAccountActionRequest(AbstractModel):
    """CreateInstanceAccountAction请求参数结构体
    """

    def __init__(self):
        r"""创建数据库账户(POST)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账户名称：数字字母下滑线
        :type PathPrefix: String
        :param InstanceAccountPassword: 账户密码
        :type PathPrefix: String
        :param InstanceAccountDescription: 账户描述
        :type PathPrefix: String
        :param InstanceAccountPrivileges: 该账户对应的数据库权限
        :type PathPrefix: Array
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


class ModifyInstanceAccountPrivilegesActionRequest(AbstractModel):
    """ModifyInstanceAccountPrivilegesAction请求参数结构体
    """

    def __init__(self):
        r"""数据库账户赋权(POST)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 数据库账户名称
        :type PathPrefix: String
        :param InstanceAccountPrivileges: 数据库权限：不传则置空改账户数据库权限
        :type PathPrefix: Array
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


class DeleteInstanceAccountActionRequest(AbstractModel):
    """DeleteInstanceAccountAction请求参数结构体
    """

    def __init__(self):
        r"""删除数据库账户(POST)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 数据库账户名称，支持批量删除，使用“,”隔开
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceAccountName = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceAccountName"):
            self.InstanceAccountName = params.get("InstanceAccountName")


class DeleteInstanceDatabaseActionRequest(AbstractModel):
    """DeleteInstanceDatabaseAction请求参数结构体
    """

    def __init__(self):
        r"""删除实例数据库(POST)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称		支持批量删除，以为 “ , ”分隔开
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.InstanceDatabaseName = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("InstanceDatabaseName"):
            self.InstanceDatabaseName = params.get("InstanceDatabaseName")


class ModifyDBNetworkRequest(AbstractModel):
    """ModifyDBNetwork请求参数结构体
    """

    def __init__(self):
        r"""修改实例IP/VPC (POST)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param VpcId: 虚拟网路ID，可调用接口[DescribeVpcs](https://docs.ksyun.com/documents/89)获取
        :type PathPrefix: String
        :param SubnetId: SubnetId		虚拟网络下的子网ID，可调用接口[DescribeSubnets](https://docs.ksyun.com/documents/93)获取。
        :type PathPrefix: String
        :param Vip: IP		虚拟网络子网下可用IP，可调用接口[DescribeSubnetAllocatedIpAddresses](https://docs.ksyun.com/documents/2607)获取。
        :type PathPrefix: String
        :param Port: 端口
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Port = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("Vip"):
            self.Vip = params.get("Vip")
        if params.get("Port"):
            self.Port = params.get("Port")


class DescribeDBInstanceMonitorPeriodRequest(AbstractModel):
    """DescribeDBInstanceMonitorPeriod请求参数结构体
    """

    def __init__(self):
        r"""查询实例监控周期
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifyDBInstanceMonitorPeriodRequest(AbstractModel):
    """ModifyDBInstanceMonitorPeriod请求参数结构体
    """

    def __init__(self):
        r"""修改实例监控周期
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Period: 监控周期	。可选：5/15/30/60
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Period = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Period"):
            self.Period = params.get("Period")


class DescribeEngineParametersModifyHistoryRequest(AbstractModel):
    """DescribeEngineParametersModifyHistory请求参数结构体
    """

    def __init__(self):
        r"""参数组历史修改信息查询
        :param DBParameterGroupId: 参数组ID	通过[参数组-列表（详情）接口](https://docs.ksyun.com/documents/344)获取
        :type PathPrefix: String
        :param Name: 修改参数名称。
        :type PathPrefix: String
        :param MaxRecords: 每页记录条数。（默认为10）
        :type PathPrefix: Int
        :param Marker: 第n页数。默认为0。
        :type PathPrefix: Int
        """
        self.DBParameterGroupId = None
        self.Name = None
        self.MaxRecords = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class BatchApplyDBParameterGroupRequest(AbstractModel):
    """BatchApplyDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""批量应用参数组
        :param DBInstanceIdentifier: 实例ID.	如果需要批量应用参数组，则实例id之间用逗号隔开,至多允许批量应用10个实例（2022.01.07）
        :type PathPrefix: String
        :param DBParameterGroupId: 参数组ID	.通过参数组-列表(详情)接口获取
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.DBParameterGroupId = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")


class UpgradeDBInstanceLatesVersionRequest(AbstractModel):
    """UpgradeDBInstanceLatesVersion请求参数结构体
    """

    def __init__(self):
        r"""小版本升级(5.7.x)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class DescribeProxyInstanceRequest(AbstractModel):
    """DescribeProxyInstance请求参数结构体
    """

    def __init__(self):
        r"""查询代理实例详情
        :param DBInstanceIdentifier: 代理实例ID
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class SetUpProxyInstanceRequest(AbstractModel):
    """SetUpProxyInstance请求参数结构体
    """

    def __init__(self):
        r"""修改代理实例(只读权重/连接池设定)
        :param DBInstanceIdentifier: 代理实例ID
        :type PathPrefix: String
        :param ReadOnlyInstanceList: 只读实例列表
        :type PathPrefix: Filter
        """
        self.DBInstanceIdentifier = None
        self.ReadOnlyInstanceList = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("ReadOnlyInstanceList"):
            self.ReadOnlyInstanceList = params.get("ReadOnlyInstanceList")


class TemporaryCloseSwitchoverRequest(AbstractModel):
    """TemporaryCloseSwitchover请求参数结构体
    """

    def __init__(self):
        r"""关闭主备切换(临时)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param AutoSwitch: 是否自动切换(输入的为期望状态)；false时为关闭，必须传时间；


        :type PathPrefix: Boolean
        :param ExpireTime: 期望过期时间点
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.AutoSwitch = None
        self.ExpireTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("AutoSwitch"):
            self.AutoSwitch = params.get("AutoSwitch")
        if params.get("ExpireTime"):
            self.ExpireTime = params.get("ExpireTime")


class DescribeBackupOverviewRequest(AbstractModel):
    """DescribeBackupOverview请求参数结构体
    """

    def __init__(self):
        r"""查询备份总概览(单地域)
        """

    def _deserialize(self, params):
        return


class DescribeStatisticBackupDetailsRequest(AbstractModel):
    """DescribeStatisticBackupDetails请求参数结构体
    """

    def __init__(self):
        r"""查询备份总列表(单地域)
        :param DataType: 必传：数据类型，区分查询类型；
backup：实例备份；
binglog：实例binglog备份；
delbackup：已删除实例备份；
        :type PathPrefix: String
        :param BackupType: 快照：snapshot
自动备份：autobackup
        :type PathPrefix: String
        :param Marker: 数据开始条数
默认:0 
        :type PathPrefix: Int
        :param MaxRecords: 数据每页展示条数；
默认：10
        :type PathPrefix: Int
        """
        self.DataType = None
        self.BackupType = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("DataType"):
            self.DataType = params.get("DataType")
        if params.get("BackupType"):
            self.BackupType = params.get("BackupType")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class ModifyMaintenanceTimeRequest(AbstractModel):
    """ModifyMaintenanceTime请求参数结构体
    """

    def __init__(self):
        r"""修改操作时间窗口
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param StartTime: 时间窗口开始时间

```json
支持时间区间：[00-23]:[00-59]
```
        :type PathPrefix: String
        :param Duration: 时间间隔

```json
注意：设计为在如上开始时间后多久的时间内可以操作，故此字段代表的为小时；

支持间隔区间：[0.5-3.0]

默认区间：0.5
间隔单位：小时
```
        :type PathPrefix: Double
        """
        self.DBInstanceIdentifier = None
        self.StartTime = None
        self.Duration = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("Duration"):
            self.Duration = params.get("Duration")


class ModifyInstanceDatabasePrivilegesActionRequest(AbstractModel):
    """ModifyInstanceDatabasePrivilegesAction请求参数结构体
    """

    def __init__(self):
        r"""数据库授权(POST)
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceDatabaseName: 数据库名称(需要修改权限的数据库库名)
        :type PathPrefix: String
        :param InstanceDatabasePrivileges: 具体账户及其权限说明
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


class UpdateDBInstanceOrderRequest(AbstractModel):
    """UpdateDBInstanceOrder请求参数结构体
    """

    def __init__(self):
        r"""试用订单更新
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


