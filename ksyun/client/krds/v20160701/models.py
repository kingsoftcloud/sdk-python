from ksyun.common.abstract_model import AbstractModel

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


class ModifyDBParameterGroupRequest(AbstractModel):
    """ModifyDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""modify db parameter group
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
        r"""reset db parameter group
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
        r"""describe db parameter group
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
        r"""describe engine default parameters
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
        r"""create db parameter group
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
        self.Parameters.Name = None
        self.Parameters.Value = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupName"):
            self.DBParameterGroupName = params.get("DBParameterGroupName")
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("Parameters.Name"):
            self.Parameters.Name = params.get("Parameters.Name")
        if params.get("Parameters.Value"):
            self.Parameters.Value = params.get("Parameters.Value")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteDBParameterGroupRequest(AbstractModel):
    """DeleteDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""delete db parameter group
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
        r"""create db instance
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
        :param BillType: 计费方式	默认值：YEAR_MONTH，取值范围：YEAR_MONTH（包年包月）,DAY（按日计费）。
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
        r"""restore db instance from db backup
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
        """
        self.DBInstanceName = None
        self.DBBackupIdentifier = None
        self.DBInstanceType = None
        self.ProjectId = None
        self.AvailabilityZone = None
        self.Duration = None
        self.DurationUnit = None
        self.Port = None

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


class DeleteDBInstanceRequest(AbstractModel):
    """DeleteDBInstance请求参数结构体
    """

    def __init__(self):
        r"""delete db instance
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
        self.AvailabilityZone.1 = None
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
            self.AvailabilityZone.1 = params.get("AvailabilityZone.1")
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
        r"""restore db instance to point in time
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
        r"""describe db instance restorable time
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
        r"""modify db instance
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
        r"""describe db log files
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
        r"""describe db backups
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
        r"""modify db instance spec
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
        r"""describe db instances
        :param DBInstanceIdentifier: 实例ID.（传入实例ID，获取的是该实例的详情，否则则获取实例列表）
        :type PathPrefix: String
        :param DBInstanceType: 实例类型。可选：HRDS（高可用）,RR（只读实例）,TRDS（临时实例）,SINGLERDS(单机版)，ERDS（三节点企业版），
CDS_HRDS(高可用_云盘版)、CDS_TRDS（临时云盘版）
        :type PathPrefix: String
        :param DBInstanceStatus: 按实例状态过滤。ACTIVE（运行中）、INVALID（请续费）
        :type PathPrefix: String
        :param Keyword: 按名称/VIP模糊过滤。
        :type PathPrefix: String
        :param Order: 排序方式。区分大小写，取值范围：DEFAULT（默认排序方式），GROUP（按复制组排序，会把只读实例排在所属主实例的后面）
        :type PathPrefix: String
        :param ProjectId: 项目制ID。默认值为所有项目	
        :type PathPrefix: String
        :param Marker: 记录开始偏移量。
        :type PathPrefix: Int
        :param MaxRecords: 每页结果中包含的最大条数。取值范围：1-100。
        :type PathPrefix: Int
        :param DBInstanceIdentifierIn: 实例IDs。实例ID多选筛选   例如：DBInstanceIdentifierIn.0=xxx&DBInstanceIdentifierIn.1=xxx
        :type PathPrefix: Filter
        :param DBInstanceNameIn: 按实例名称过滤。示例(DBInstanceNameIn.1=test1，DBInstanceNameIn.2=test2)
        :type PathPrefix: Filter
        :param VipIn: 	
按VIP过滤。示例(VipIn.1=10.9.2.3，VipIn.2=10.9.2.4)
        :type PathPrefix: Filter
        :param EIPIn: 按EIP过滤。示例(EIPIn.1=10.9.2.5，EIPIn.2=10.9.2.6)。
        :type PathPrefix: String
        :param ExpiryDateLessThan: 按照实例过期时间过滤。取值范围：>0
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
        r"""describe db engine versions
        """

    def _deserialize(self, params):
        return


class UpgradeDBInstanceEngineVersionRequest(AbstractModel):
    """UpgradeDBInstanceEngineVersion请求参数结构体
    """

    def __init__(self):
        r"""upgrade db instance engine version
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
        r"""modify db instance type
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
        r"""查看当前实例数据库参数运行值列表
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
        r"""delete db backup
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
        r"""create db backup
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


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance请求参数结构体
    """

    def __init__(self):
        r"""renew db instance
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param Duration: 时长
        :type PathPrefix: Int
        :param DurationUnit: 时长单位
        :type PathPrefix: String
        :param BillType: 计费方式	默认值：YEAR_MONTH，取值范围：YEAR_MONTH（包年包月）,DAY（按日计费）。
        :type PathPrefix: String
        :param EndTime: 结束时间	该参数按日计费时有效。默认值：NULL，填入日期（如：2018-03-22）代表服务结束时间。
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.Duration = None
        self.DurationUnit = None
        self.BillType = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("DurationUnit"):
            self.DurationUnit = params.get("DurationUnit")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class SwitchDBInstanceHARequest(AbstractModel):
    """SwitchDBInstanceHA请求参数结构体
    """

    def __init__(self):
        r"""switch db instance h a
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
        r"""generate db admin u r l
        :param DBInstanceIdentifier: 实例ID
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
        :param ExpiryDateLessThan: 过期时间	默认：7天以内；过滤出过期时间小于N天的实例，传入这个参数会给出状态EXPIRING_SOON统计；取值范围：>0
        :type PathPrefix: Int
        """
        self.ExpiryDateLessThan = None

    def _deserialize(self, params):
        if params.get("ExpiryDateLessThan"):
            self.ExpiryDateLessThan = params.get("ExpiryDateLessThan")


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
        r"""修改实例备库可用区
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param AvailabilityZone.1: 主可用区	主所在可用区不可变
        :type PathPrefix: String
        :param AvailabilityZone.2: 备可用区
        :type PathPrefix: String
        """
        self.DBInstanceIdentifier = None
        self.AvailabilityZone.1 = None
        self.AvailabilityZone.2 = None

    def _deserialize(self, params):
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("AvailabilityZone.1"):
            self.AvailabilityZone.1 = params.get("AvailabilityZone.1")
        if params.get("AvailabilityZone.2"):
            self.AvailabilityZone.2 = params.get("AvailabilityZone.2")


class DescribeDBInstanceRegionsRequest(AbstractModel):
    """DescribeDBInstanceRegions请求参数结构体
    """

    def __init__(self):
        r"""查看机房列表
        """

    def _deserialize(self, params):
        return


class DescribeDBInstancePackagesRequest(AbstractModel):
    """DescribeDBInstancePackages请求参数结构体
    """

    def __init__(self):
        r"""查看购买套餐
        :param RegionCode: 机房code。可从“查看机房列表
（DescribeDBInstanceRegions）”获得
        :type PathPrefix: String
        """
        self.RegionCode = None

    def _deserialize(self, params):
        if params.get("RegionCode"):
            self.RegionCode = params.get("RegionCode")


class DescribeLastLogRequest(AbstractModel):
    """DescribeLastLog请求参数结构体
    """

    def __init__(self):
        r"""DescribeLastLog
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
        r"""获取审计结果
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
        r"""获取审计统计数据
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


class GetTableRestorableTimeRequest(AbstractModel):
    """GetTableRestorableTime请求参数结构体
    """

    def __init__(self):
        r"""获取数据库可恢复时间
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
        r"""获取指定时间点附近或者备份集的库表信息
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
        r"""恢复实例到当前时间点
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
        r"""库表级恢复到当前实例
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID	根据备份恢复，必传备份ID，且必传SrcDatabases和DstDatabases
        :type PathPrefix: String
        :param RestorableTime: 恢复时间		根据时间点恢复，必传时间点，且必传SrcDatabases和DstDatabases；格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param SrcDatabases: 源		[{<br>  "DatabaseName": "wang",<br>"WholeDatabase":"True",<br>"TableNames": [<br>"li"]<br>}]
        :type PathPrefix: Array
        :param DstDatabases: 目标		[{<br>"DatabaseName": "wang",<br>"WholeDatabase":"True",<br>"TableNames": [<br> "li"]<br> }]
        :type PathPrefix: Array
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
        r"""库表级恢复到临时实例
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param DBBackupIdentifier: 备份ID	根据备份恢复，必传备份ID，且必传SrcDatabases和DstDatabases
        :type PathPrefix: String
        :param RestorableTime: 恢复时间		根据时间点恢复，必传时间点，且必传SrcDatabases和DstDatabases；格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param SrcDatabases: 源		[{<br>  "DatabaseName": "wang",<br>"WholeDatabase":"True",<br>"TableNames": [<br>"li"]<br>}]
        :type PathPrefix: Array
        :param DstDatabases: 目标		[{<br>"DatabaseName": "wang",<br>"WholeDatabase":"True",<br>"TableNames": [<br> "li"]<br> }]
        :type PathPrefix: Array
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
        r"""某时间段SQL执行次数TOP10查询接口
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
        r"""某时间段SQL执行耗时TOP10查询接口
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
        r"""某时间段全量SQL统计查询接口
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
        r"""某时间段全量SQL折线图查询接口
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
        r"""某时间段慢SQL统计查询接口
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
        r"""某时间段慢SQL折线图查询接口
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
        r"""某时间段慢SQL查询接口
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
        r"""列出历史导出任务
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


class DescribeInstanceAccountsRequest(AbstractModel):
    """DescribeInstanceAccounts请求参数结构体
    """

    def __init__(self):
        r"""DescribeInstanceAccounts
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
        r"""ModifyInstanceAccountInfo
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


class DescribeCollationsRequest(AbstractModel):
    """DescribeCollations请求参数结构体
    """

    def __init__(self):
        r"""DescribeCollations
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
        r"""CreateInstanceDatabase
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
        r"""ModifyInstanceDatabasePrivileges
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
        r"""DescribeInstanceDatabases
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
        r"""ModifyInstanceDatabaseInfo
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
        r"""StartSlowLogDetailExportTask
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
        r"""ListSlowLogDetailExportTask
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
        r"""CreateInstanceAccountAction
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 账号名称			数字字母下滑线
        :type PathPrefix: String
        :param InstanceAccountPassword: 账号密码
        :type PathPrefix: String
        :param InstanceAccountDescription: 数据库账号描述
        :type PathPrefix: String
        :param InstanceAccountPrivileges: 该账号对应的数据库权限
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
        r"""ModifyInstanceAccountPrivilegesAction
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 数据库帐号名称
        :type PathPrefix: String
        :param InstanceAccountPrivileges: 数据库权限		不传则置空改帐号数据库权限
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
        r"""DeleteInstanceAccountAction
        :param DBInstanceIdentifier: 实例ID
        :type PathPrefix: String
        :param InstanceAccountName: 数据库帐号名称		支持批量删除，使用“,”隔开
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
        r"""DeleteInstanceDatabaseAction
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
        r"""修改ip/vpc
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


