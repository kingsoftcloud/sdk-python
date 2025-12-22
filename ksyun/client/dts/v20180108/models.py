from ksyun.common.abstract_model import AbstractModel

class SchemaStructRequest(AbstractModel):
    """SchemaStruct请求参数结构体
    """

    def __init__(self):
        r"""获取源库库表结构
        :param SourceInstanceId: 源端实例ID。
        :type PathPrefix: String
        :param SourceType: 表库类型。Public|SpecialLine|Krds|SubscriptionKrds（仅支持mysql）。
        :type PathPrefix: String
        :param SourceUsername: 源端数据库账号。
        :type PathPrefix: String
        :param SourcePassword: 源端数据库账号密码。
        :type PathPrefix: String
        :param SourceRegion: 源端地域
        :type PathPrefix: String
        """
        self.SourceInstanceId = None
        self.SourceType = None
        self.SourceUsername = None
        self.SourcePassword = None
        self.SourceRegion = None

    def _deserialize(self, params):
        if params.get("SourceInstanceId"):
            self.SourceInstanceId = params.get("SourceInstanceId")
        if params.get("SourceType"):
            self.SourceType = params.get("SourceType")
        if params.get("SourceUsername"):
            self.SourceUsername = params.get("SourceUsername")
        if params.get("SourcePassword"):
            self.SourcePassword = params.get("SourcePassword")
        if params.get("SourceRegion"):
            self.SourceRegion = params.get("SourceRegion")


class ConnectivityCheckRequest(AbstractModel):
    """ConnectivityCheck请求参数结构体
    """

    def __init__(self):
        r"""源库/目标库连通性
        """

    def _deserialize(self, params):
        return


class CreatePrecheckRequest(AbstractModel):
    """CreatePrecheck请求参数结构体
    """

    def __init__(self):
        r"""创建预检查
        :param SourceType: 源端库类型

```json
公有云mysql：Krds
公有云主从redis：Kcs
公有云集群redis：ClusterKcs
公有云mongo：Kmgo
公有云pg：Kpg
订阅目标类型：Vpc

注：目前不支持创建pg任务，源库与目标库类型须一致
```
        :type PathPrefix: String
        :param TargetType: 目标端库类型

```json
公有云mysql：Krds
公有云主从redis：Kcs
公有云集群redis：ClusterKcs
公有云mongo：Kmgo
公有云pg：Kpg
订阅目标类型：Vpc

注：目前不支持创建pg任务，源库与目标库类型须一致
```
        :type PathPrefix: String
        :param TargetRegion: 目标库地域
        :type PathPrefix: String
        :param SourceRegion: 源端库地域
        :type PathPrefix: String
        :param DbSchema: 需要同步的源数据库结构

```json
注意：此处接受json字符串
例如："{\"is_full\":true}"表示为全部同步
```
        :type PathPrefix: String
        :param SubTasks: dts子任务

```json
1.MYSQL支持：SchemaMigration,BackupRecovery,RunReplication
2.Redis支持：FullSync
3.MongoDB支持：MgoBackupRecovery,MgoRunReplication
4.双向同步支持：BackupRecovery,ForwardRunReplication,ReverseRunReplication 
5.数据订阅：Subscription
```
        :type PathPrefix: String
        :param SourceInstanceId: 源端库实例ID
        :type PathPrefix: String
        :param TargetInstanceId: 目标库地域
        :type PathPrefix: String
        :param SourceUsername: 源端库账号名称
        :type PathPrefix: String
        :param SourcePassword: 源端库连接账号密码
        :type PathPrefix: String
        :param Type: dts任务类型

```json
范围： 
Synchronous数据同步 
Transmission数据迁移 
Subscription数据订阅 
Bisynchronous双向同步
```
        :type PathPrefix: String
        :param DTSParameter: 需要同步迁移参数时传递

```json
例如：
{
  "SourceType": "Krds",
  "TargetType": "Krds",
  "TargetRegion": "cn-beijing-6",
  "region": "cn-beijing-6",
  "DbSchema": "{\"is_full\":true}",
  "SubTasks": "BackupRecovery,RunReplication",
  "SourceRegion": "cn-beijing-6",
  "SourceInstanceId": "******",
  "TargetInstanceId": "******",
  "SourceUsername": "admin",
  "SourceUser": [
     {
        "Username":"testuser",
        "SourceHost":"%"
    }
  ],
  "DTSParameter": [
    {
      "DBParameter": "log_bin_trust_function_creators",
      "TargetDBParameterValue": "OFF"
    },
    {
      "DBParameter": "binlog_format",
      "TargetDBParameterValue": "ROW"
    }
  ],
  "SourcePassword": "******",
  "Type": "Transmission"
}
```
        :type PathPrefix: Filter
        :param SourceUser: 需要往目标库迁移'账号'时传递

```json
例如：
{
  "SourceType": "Krds",
  "TargetType": "Krds",
  "TargetRegion": "cn-beijing-6",
  "region": "cn-beijing-6",
  "DbSchema": "{\"is_full\":true}",
  "SubTasks": "BackupRecovery,RunReplication",
  "SourceRegion": "cn-beijing-6",
  "SourceInstanceId": "******",
  "TargetInstanceId": "******",
  "SourceUsername": "admin",
  "SourceUser": [
     {
        "Username":"testuser",
        "SourceHost":"%"
    }
  ],
  "DTSParameter": [
    {
      "DBParameter": "log_bin_trust_function_creators",
      "TargetDBParameterValue": "OFF"
    },
    {
      "DBParameter": "binlog_format",
      "TargetDBParameterValue": "ROW"
    }
  ],
  "SourcePassword": "******",
  "Type": "Transmission"
}
````
        :type PathPrefix: Filter
        """
        self.SourceType = None
        self.TargetType = None
        self.TargetRegion = None
        self.SourceRegion = None
        self.DbSchema = None
        self.SubTasks = None
        self.SourceInstanceId = None
        self.TargetInstanceId = None
        self.SourceUsername = None
        self.SourcePassword = None
        self.Type = None
        self.DTSParameter = None
        self.SourceUser = None

    def _deserialize(self, params):
        if params.get("SourceType"):
            self.SourceType = params.get("SourceType")
        if params.get("TargetType"):
            self.TargetType = params.get("TargetType")
        if params.get("TargetRegion"):
            self.TargetRegion = params.get("TargetRegion")
        if params.get("SourceRegion"):
            self.SourceRegion = params.get("SourceRegion")
        if params.get("DbSchema"):
            self.DbSchema = params.get("DbSchema")
        if params.get("SubTasks"):
            self.SubTasks = params.get("SubTasks")
        if params.get("SourceInstanceId"):
            self.SourceInstanceId = params.get("SourceInstanceId")
        if params.get("TargetInstanceId"):
            self.TargetInstanceId = params.get("TargetInstanceId")
        if params.get("SourceUsername"):
            self.SourceUsername = params.get("SourceUsername")
        if params.get("SourcePassword"):
            self.SourcePassword = params.get("SourcePassword")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("DTSParameter"):
            self.DTSParameter = params.get("DTSParameter")
        if params.get("SourceUser"):
            self.SourceUser = params.get("SourceUser")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体
    """

    def __init__(self):
        r"""创建任务(含迁移/同步/订阅)
        :param TaskName: TaskName
        :type PathPrefix: String
        :param SubTask: 子任务名称。	
Mysql支持：
SchemaMigration,BackupRecovery,RunReplication

双向同步支持：
BackupRecovery,ForwardRunReplication,ReverseRunReplication

Redis支持：
FullSync

mongo支持：
MgoBackupRecovery,MgoRunReplication

数据订阅支持：
Subscription
        :type PathPrefix: String
        :param TaskType: 默认Transmission
范围：
Synchronous数据同步
Transmission数据迁移
Subscription数据订阅
        :type PathPrefix: String
        :param PrecheckId: 成功的预检查ID。请注意：创建任务与预检查任务的参数任务类型和子任务需保持一致。
        :type PathPrefix: String
        :param BillType: 默认1。1：包年包月 86：按量付费（流量）
        :type PathPrefix: Int
        :param Duration: 计费时长。单位：月，计费方式为包年包月时必填。
        :type PathPrefix: Int
        """
        self.TaskName = None
        self.SubTask = None
        self.TaskType = None
        self.PrecheckId = None
        self.BillType = None
        self.Duration = None

    def _deserialize(self, params):
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")
        if params.get("SubTask"):
            self.SubTask = params.get("SubTask")
        if params.get("TaskType"):
            self.TaskType = params.get("TaskType")
        if params.get("PrecheckId"):
            self.PrecheckId = params.get("PrecheckId")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体
    """

    def __init__(self):
        r"""查询任务(列表/详情)
        :param TaskId: 主任务ID
        :type PathPrefix: String
        :param TargetType: 目标端数据库类型。范围：Krds Kcs ClusterKcs Kmgo Kpg
        :type PathPrefix: String
        :param TaskType: 任务类型。默认Transmission，若为数据迁移任务，可不传此参数，其他类型必传。范围：
数据迁移Transmission 数据同步Synchronous数据订阅Subscription
        :type PathPrefix: String
        :param TaskStatus: 不传默认查询所有状态，范围：UNSTARTED RUNNING RELOADING PAUSED PAUSING STOPED FINISHED ERROR
        :type PathPrefix: Filter
        :param TaskName: 任务名称
        :type PathPrefix: String
        :param TargetInstanceId: 目标库实例ID。通过目标库实例ID筛选符合条件的任务
        :type PathPrefix: String
        :param SourceInstanceId: 源库实例ID。通过源库实例ID筛选符合条件的任务。
        :type PathPrefix: String
        :param OrderByType: 根据任务创建时间排序。默认DESC
        :type PathPrefix: String
        :param Marker: 当前查询开始行数。默认0。
        :type PathPrefix: Int
        :param MaxRecords: 当前页最大行数。	默认10。
        :type PathPrefix: Int
        """
        self.TaskId = None
        self.TargetType = None
        self.TaskType = None
        self.TaskStatus = None
        self.TaskName = None
        self.TargetInstanceId = None
        self.SourceInstanceId = None
        self.OrderByType = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("TargetType"):
            self.TargetType = params.get("TargetType")
        if params.get("TaskType"):
            self.TaskType = params.get("TaskType")
        if params.get("TaskStatus"):
            self.TaskStatus = params.get("TaskStatus")
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")
        if params.get("TargetInstanceId"):
            self.TargetInstanceId = params.get("TargetInstanceId")
        if params.get("SourceInstanceId"):
            self.SourceInstanceId = params.get("SourceInstanceId")
        if params.get("OrderByType"):
            self.OrderByType = params.get("OrderByType")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class OperateTaskRequest(AbstractModel):
    """OperateTask请求参数结构体
    """

    def __init__(self):
        r"""任务操作(启动/暂停/停止/删除)
        :param TaskId: 主任务ID
        :type PathPrefix: String
        :param ActionName: 操作类型。可选范围：Start|Stop|Delete|Pause
        :type PathPrefix: String
        :param TaskType: 任务类型。默认Transmission，若为数据迁移任务，可不传此参数，其他类型必传。范围：数据迁移Transmission 数据同步Synchron
        :type PathPrefix: String
        :param ErrSkip: 任务出错跳过功能。默认0   
范围：0不跳过 1跳过 ；
0报错手动修复报错内容，重载任务时选择不跳过错误。
1重载任务时选择跳过当前错误（请自行评估跳过错误的风险）
        :type PathPrefix: Int
        """
        self.TaskId = None
        self.ActionName = None
        self.TaskType = None
        self.ErrSkip = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("ActionName"):
            self.ActionName = params.get("ActionName")
        if params.get("TaskType"):
            self.TaskType = params.get("TaskType")
        if params.get("ErrSkip"):
            self.ErrSkip = params.get("ErrSkip")


class DescribeConnConfigRequest(AbstractModel):
    """DescribeConnConfig请求参数结构体
    """

    def __init__(self):
        r"""查询任务配置信息(通过配置ID获取)
        :param ConnConfigId: 任务配置ID
        :type PathPrefix: String
        """
        self.ConnConfigId = None

    def _deserialize(self, params):
        if params.get("ConnConfigId"):
            self.ConnConfigId = params.get("ConnConfigId")


class DescribePrecheckRequest(AbstractModel):
    """DescribePrecheck请求参数结构体
    """

    def __init__(self):
        r"""查询预检查结果(含未通过异常反馈)
        :param PrecheckId: 预检查任务ID
        :type PathPrefix: String
        """
        self.PrecheckId = None

    def _deserialize(self, params):
        if params.get("PrecheckId"):
            self.PrecheckId = params.get("PrecheckId")


class DescribeSourceUserConfigRequest(AbstractModel):
    """DescribeSourceUserConfig请求参数结构体
    """

    def __init__(self):
        r"""获取迁移账号配置信息
        :param TaskId: 主任务ID
        :type PathPrefix: String
        """
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class SetConsistencyCheckRequest(AbstractModel):
    """SetConsistencyCheck请求参数结构体
    """

    def __init__(self):
        r"""打开或关闭DTS一致性校验定时任务
        :param TaskId: 主任务ID
        :type PathPrefix: String
        :param ConsistencyCheckAuto: 校验开关。范围：True|False
        :type PathPrefix: Boolean
        :param ConsistencyCheckCycle: 自动校验周期。	开启定时校验任务必传。
        :type PathPrefix: Int
        :param ConsistencyCheckFixedTime: 校验时间。开启定时校验任务必传。
        :type PathPrefix: String
        """
        self.TaskId = None
        self.ConsistencyCheckAuto = None
        self.ConsistencyCheckCycle = None
        self.ConsistencyCheckFixedTime = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("ConsistencyCheckAuto"):
            self.ConsistencyCheckAuto = params.get("ConsistencyCheckAuto")
        if params.get("ConsistencyCheckCycle"):
            self.ConsistencyCheckCycle = params.get("ConsistencyCheckCycle")
        if params.get("ConsistencyCheckFixedTime"):
            self.ConsistencyCheckFixedTime = params.get("ConsistencyCheckFixedTime")


class DescribeConsistencyCheckRequest(AbstractModel):
    """DescribeConsistencyCheck请求参数结构体
    """

    def __init__(self):
        r"""查询定时一致性校验任务状态
        :param TaskId: 主任务ID
        :type PathPrefix: String
        """
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class DescribeDTSParameterRequest(AbstractModel):
    """DescribeDTSParameter请求参数结构体
    """

    def __init__(self):
        r"""获取迁移实例参数信息(参数对齐功能使用)
        :param SourceType: 源端实例类型。如：Public|SpecialLine|Krds|SubscriptionKrds（仅支持mysql）等。
        :type PathPrefix: String
        :param TargetType: 目标端实例类型。
        :type PathPrefix: String
        :param TargetInstanceId: 目标端数据库实例ID。
        :type PathPrefix: String
        :param TargetRegion: 目标端实例机房。
        :type PathPrefix: String
        :param SourceInstanceId: 源端数据库实例ID。
        :type PathPrefix: String
        :param SourceHost: 源端实例IP。
        :type PathPrefix: String
        :param SourcePort: 源端实例端口。
        :type PathPrefix: String
        :param SourceUsername: 源端数据库用户名。
        :type PathPrefix: String
        :param SourcePassword: 源端数据库账号密码。
        :type PathPrefix: String
        :param SourceRegion: 源端实例机房。
        :type PathPrefix: String
        """
        self.SourceType = None
        self.TargetType = None
        self.TargetInstanceId = None
        self.TargetRegion = None
        self.SourceInstanceId = None
        self.SourceHost = None
        self.SourcePort = None
        self.SourceUsername = None
        self.SourcePassword = None
        self.SourceRegion = None

    def _deserialize(self, params):
        if params.get("SourceType"):
            self.SourceType = params.get("SourceType")
        if params.get("TargetType"):
            self.TargetType = params.get("TargetType")
        if params.get("TargetInstanceId"):
            self.TargetInstanceId = params.get("TargetInstanceId")
        if params.get("TargetRegion"):
            self.TargetRegion = params.get("TargetRegion")
        if params.get("SourceInstanceId"):
            self.SourceInstanceId = params.get("SourceInstanceId")
        if params.get("SourceHost"):
            self.SourceHost = params.get("SourceHost")
        if params.get("SourcePort"):
            self.SourcePort = params.get("SourcePort")
        if params.get("SourceUsername"):
            self.SourceUsername = params.get("SourceUsername")
        if params.get("SourcePassword"):
            self.SourcePassword = params.get("SourcePassword")
        if params.get("SourceRegion"):
            self.SourceRegion = params.get("SourceRegion")


class DescribeDTSParameterConfigRequest(AbstractModel):
    """DescribeDTSParameterConfig请求参数结构体
    """

    def __init__(self):
        r"""查询DTS任务的实例参数配置
        :param TaskId: 主任务ID。
        :type PathPrefix: String
        """
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class DescribeSourceUserRequest(AbstractModel):
    """DescribeSourceUser请求参数结构体
    """

    def __init__(self):
        r"""获取源端实例用户账号信息
        :param SourceInstanceId: 源端mysql实例id
        :type PathPrefix: String
        :param SourceType: 源库类型
        :type PathPrefix: String
        :param SourceUsername: 源端mysql连接用户名
        :type PathPrefix: String
        :param SourcePassword: 源端mysql连接密码
        :type PathPrefix: String
        :param SourceRegion: 源端可用区
        :type PathPrefix: String
        :param TargetType: 目标端实例类型
        :type PathPrefix: String
        :param TargetInstanceId: 目标端实例id
        :type PathPrefix: String
        :param TargetRegion: 目标端可用区
        :type PathPrefix: String
        """
        self.SourceInstanceId = None
        self.SourceType = None
        self.SourceUsername = None
        self.SourcePassword = None
        self.SourceRegion = None
        self.TargetType = None
        self.TargetInstanceId = None
        self.TargetRegion = None

    def _deserialize(self, params):
        if params.get("SourceInstanceId"):
            self.SourceInstanceId = params.get("SourceInstanceId")
        if params.get("SourceType"):
            self.SourceType = params.get("SourceType")
        if params.get("SourceUsername"):
            self.SourceUsername = params.get("SourceUsername")
        if params.get("SourcePassword"):
            self.SourcePassword = params.get("SourcePassword")
        if params.get("SourceRegion"):
            self.SourceRegion = params.get("SourceRegion")
        if params.get("TargetType"):
            self.TargetType = params.get("TargetType")
        if params.get("TargetInstanceId"):
            self.TargetInstanceId = params.get("TargetInstanceId")
        if params.get("TargetRegion"):
            self.TargetRegion = params.get("TargetRegion")


class DescribeSubTaskRequest(AbstractModel):
    """DescribeSubTask请求参数结构体
    """

    def __init__(self):
        r"""查询一致性校验任务(子任务/一致性校验任务)
        :param TaskId: 主任务ID。须同子任务名称一同填入生效，多用于查询一致性校验子任务列表。
        :type PathPrefix: String
        :param SubTaskId: 子任务ID。选填子任务ID，则查询子任务详情。请务必填写子任务ID与主任务ID其中一个。
        :type PathPrefix: String
        :param SubTaskName: 子任务名称。须同主任务ID一同填入生效，多用于查询一致性校验子任务列表。

一致性校验子任务名称：

一致性校验：ConsistencyCheck,用户手工触发一致性校验：UserConsistencyCheck,定时触发一致性校验：FixedConsistencyCheck
        :type PathPrefix: String
        :param OrderByType: 排序方式。查询子任务列表时根据子任务创建时间拍排序,默认DESC
        :type PathPrefix: String
        :param ObjectStatus: 子任务table执行状态。查询子任务table迁移详情时可传入。范围：迁移完成：finish 待迁移:unstart  迁移失败:error  迁移中:running  跳过:skip
        :type PathPrefix: String
        :param Marker: 当前查询开始行数。默认0。
        :type PathPrefix: Int
        :param MaxRecords: 当前页最大行数。默认10。
        :type PathPrefix: Int
        """
        self.TaskId = None
        self.SubTaskId = None
        self.SubTaskName = None
        self.OrderByType = None
        self.ObjectStatus = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("SubTaskId"):
            self.SubTaskId = params.get("SubTaskId")
        if params.get("SubTaskName"):
            self.SubTaskName = params.get("SubTaskName")
        if params.get("OrderByType"):
            self.OrderByType = params.get("OrderByType")
        if params.get("ObjectStatus"):
            self.ObjectStatus = params.get("ObjectStatus")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class CreateConsistencyCheckRequest(AbstractModel):
    """CreateConsistencyCheck请求参数结构体
    """

    def __init__(self):
        r"""创建一致性校验任务(子任务)
        :param TaskId: 主任务ID。
        :type PathPrefix: String
        """
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class StopConsistencyCheckRequest(AbstractModel):
    """StopConsistencyCheck请求参数结构体
    """

    def __init__(self):
        r"""结束一致性校验任务(手动)
        :param TaskId: 主任务ID。
        :type PathPrefix: String
        """
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class DescribeRegionConfigRequest(AbstractModel):
    """DescribeRegionConfig请求参数结构体
    """

    def __init__(self):
        r"""查询支持的地域信息
        """

    def _deserialize(self, params):
        return


class TaskBirdViewRequest(AbstractModel):
    """TaskBirdView请求参数结构体
    """

    def __init__(self):
        r"""分类型概览任务统计数据
        :param taskType: 任务类型

```json
默认：Transmission 
 
范围：
数据迁移	Transmission 
数据同步	Synchronous 
数据订阅	Subscription
```
        :type PathPrefix: String
        """
        self.taskType = None

    def _deserialize(self, params):
        if params.get("taskType"):
            self.taskType = params.get("taskType")


