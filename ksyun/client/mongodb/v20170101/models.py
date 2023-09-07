from ksyun.common.abstract_model import AbstractModel

class CreateMongoDBInstanceRequest(AbstractModel):
    """CreateMongoDBInstance请求参数结构体
    """

    def __init__(self):
        r"""创建副本集实例
        :param PayType: 计费方式：默认为byMonth。取值范围：byMonth（包年包月）,byDay（按日计费），hourlyInstantSettlement（按小时实时结算）。
        :type PathPrefix: String
        :param AvailabilityZone: 可用区信息
        :type PathPrefix: Filter
        :param Name: 6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线及中划线
        :type PathPrefix: String
        :param DbVersion: MongoDB引擎版本  可选值为：3.2，3.6， 4.0。
        :type PathPrefix: String
        :param NodeNum: 默认为3，取值范围：3、5、7。为实例所有节点数，每个实例包含一个primary一个hidden节点，其余为secondary节点。
        :type PathPrefix: Int
        :param Storage: 硬盘存储空间。
        :type PathPrefix: Int
        :param Duration: 时长 默认值：1(单位:月) ；PayType=byMonth(包年包月)则必填，最大支持范围是(1 ~36月)
        :type PathPrefix: Int
        :param IamProjectId: 所属项目id。默认：0（默认项目）
        :type PathPrefix: String
        :param VpcId: VPC网络ID，可在网络控制台获取。
        :type PathPrefix: String
        :param VnetId: 终端子网id,  可在网络控制台获取。
        :type PathPrefix: String
        :param InstancePassword: 实例管理员密码  8~30个字符 必须包含大小写字母和数字 支持的特殊字符为!@#$%^&*()-_+=
        :type PathPrefix: String
        :param InstanceClass: 副本集实例配置。

        :type PathPrefix: String
        """
        self.PayType = None
        self.AvailabilityZone = None
        self.Name = None
        self.DbVersion = None
        self.NodeNum = None
        self.Storage = None
        self.Duration = None
        self.IamProjectId = None
        self.VpcId = None
        self.VnetId = None
        self.InstancePassword = None
        self.InstanceClass = None

    def _deserialize(self, params):
        if params.get("PayType"):
            self.PayType = params.get("PayType")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("DbVersion"):
            self.DbVersion = params.get("DbVersion")
        if params.get("NodeNum"):
            self.NodeNum = params.get("NodeNum")
        if params.get("Storage"):
            self.Storage = params.get("Storage")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")
        if params.get("InstanceClass"):
            self.InstanceClass = params.get("InstanceClass")


class DeleteMongoDBInstanceRequest(AbstractModel):
    """DeleteMongoDBInstance请求参数结构体
    """

    def __init__(self):
        r"""删除实例
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeMongoDBInstanceRequest(AbstractModel):
    """DescribeMongoDBInstance请求参数结构体
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


class DescribeMongoDBInstancesRequest(AbstractModel):
    """DescribeMongoDBInstances请求参数结构体
    """

    def __init__(self):
        r"""查询账号下实例列表
        :param Area: 按可用区筛选。
        :type PathPrefix: String
        :param Vip: 实例IP地址。
        :type PathPrefix: String
        :param VpcId: 虚拟专用网络ID。                        只适用于VPC网络下的服务。
        :type PathPrefix: String
        :param VnetId: 终端子网ID。
        :type PathPrefix: String
        :param IamProjectId: 项目ID。                           
 默认是0(默认项目),如果查询全部项目，需要传入所有的项目ID，‘,’隔开。
        :type PathPrefix: String
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        :param Name: 实例名称。
        :type PathPrefix: String
        :param Mode: 实例类型: repset(副本集) ，cluster(分片集群)。
        :type PathPrefix: String
        :param DbVersion: 按实例版本筛选。实例版本 3.2，3.6/4.0。
        :type PathPrefix: String
        :param Status: 实例当前状态，如取值running   可查询running状态中的实例。

可选（ 共11种）：running，deleting，restarting，locking，unlocking，locked，backuping，restoring，restoring_backup，switching_role，migrating。  
        :type PathPrefix: String
        :param FuzzySearch: 支持模糊查询实例名称，实例id。
        :type PathPrefix: String
        :param TagKey: 实例所属的TagKey。TagKey和TagValue必须同时传入，否则不生效。
        :type PathPrefix: String
        :param TagValue: 实例所属的TagValue。TagKey和TagValue必须同时传入，否则不生效。
        :type PathPrefix: String
        :param Offset: 查询数据的起始位置。默认为0。
        :type PathPrefix: Int
        :param Limit: 需要从起始位置开始查询的缓存服务的个数。取值范围为[1~100]，默认为10。
        :type PathPrefix: Int
        :param OrderBy: 排序字段。可传值为{name,asc；name,desc；created,asc；created,desc}，默认按照创建时间降序，只有排序字段时，默认按照升序排列。
        :type PathPrefix: String
        """
        self.Area = None
        self.Vip = None
        self.VpcId = None
        self.VnetId = None
        self.IamProjectId = None
        self.InstanceId = None
        self.Name = None
        self.Mode = None
        self.DbVersion = None
        self.Status = None
        self.FuzzySearch = None
        self.TagKey = None
        self.TagValue = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None

    def _deserialize(self, params):
        if params.get("Area"):
            self.Area = params.get("Area")
        if params.get("Vip"):
            self.Vip = params.get("Vip")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Mode"):
            self.Mode = params.get("Mode")
        if params.get("DbVersion"):
            self.DbVersion = params.get("DbVersion")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("TagKey"):
            self.TagKey = params.get("TagKey")
        if params.get("TagValue"):
            self.TagValue = params.get("TagValue")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")


class DescribeMongoDBInstanceNodeRequest(AbstractModel):
    """DescribeMongoDBInstanceNode请求参数结构体
    """

    def __init__(self):
        r"""查询副本集实例节点信息
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param NodeId: 分片集群的shard节点的ID。暂不支持批量查询。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.NodeId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")


class RenameMongoDBInstanceRequest(AbstractModel):
    """RenameMongoDBInstance请求参数结构体
    """

    def __init__(self):
        r"""实例重命名
        :param InstanceId: 服务ID
        :type PathPrefix: String
        :param Name: 服务名称
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Name = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Name"):
            self.Name = params.get("Name")


class ResetPasswordMongoDBInstanceRequest(AbstractModel):
    """ResetPasswordMongoDBInstance请求参数结构体
    """

    def __init__(self):
        r"""修改密码
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param InstancePassword: 实例修改后的密码。8-30个字符，必须包含大小写字母和数字，支持特殊字符字符为!@#$%^&*()_+=-
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstancePassword = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")


class RestartMongoDBInstanceRequest(AbstractModel):
    """RestartMongoDBInstance请求参数结构体
    """

    def __init__(self):
        r"""重启实例
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateMongoDBSnapshotRequest(AbstractModel):
    """CreateMongoDBSnapshot请求参数结构体
    """

    def __init__(self):
        r"""创建手动备份
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        :param Name: 备份名称
        :type PathPrefix: String
        :param BackupMode: 备份模式。可选：Physical（物理备份），  Logical（逻辑备份）。默认物理备份。 注意：逻辑备份不支持恢复！
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Name = None
        self.BackupMode = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("BackupMode"):
            self.BackupMode = params.get("BackupMode")


class SetMongoDBTimingSnapshotRequest(AbstractModel):
    """SetMongoDBTimingSnapshot请求参数结构体
    """

    def __init__(self):
        r"""自动备份设置
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param TimingSwitch: 定时任务开关。定时任务开关On / Off当TimingSwitch=On时；Timezone与TimeCycle必填当TimingSwitch=Off时；Timezone与TimeCycle将被忽略。
        :type PathPrefix: String
        :param Timezone: 备份的时间段。可选:00:00-01:00, 01:00-02:00, ..., 23:00-24:00等24个区间。
        :type PathPrefix: String
        :param TimeCycle: 备份周期。每周选择哪几天备份，可以指定多个值。可选：Mon,Tues,Wed,Thur,Fri,Sat,Sun,Ever（以逗号间隔）。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.TimingSwitch = None
        self.Timezone = None
        self.TimeCycle = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TimingSwitch"):
            self.TimingSwitch = params.get("TimingSwitch")
        if params.get("Timezone"):
            self.Timezone = params.get("Timezone")
        if params.get("TimeCycle"):
            self.TimeCycle = params.get("TimeCycle")


class DescribeMongoDBSnapshotRequest(AbstractModel):
    """DescribeMongoDBSnapshot请求参数结构体
    """

    def __init__(self):
        r"""查询实例备份记录列表
        :param InstanceId: 实例Id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DeleteMongoDBSnapshotRequest(AbstractModel):
    """DeleteMongoDBSnapshot请求参数结构体
    """

    def __init__(self):
        r"""删除备份
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        :param SnapshotId: 备份Id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class RenameMongoDBSnapshotRequest(AbstractModel):
    """RenameMongoDBSnapshot请求参数结构体
    """

    def __init__(self):
        r"""备份重命名
        :param InstanceId: 实例id

        :type PathPrefix: String
        :param SnapshotId: 备份Id
        :type PathPrefix: String
        :param Name: 备份名称。支持2-64个字符，支持中文，字母，数字，以及-_。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.SnapshotId = None
        self.Name = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")
        if params.get("Name"):
            self.Name = params.get("Name")


class AddSecurityGroupRuleRequest(AbstractModel):
    """AddSecurityGroupRule请求参数结构体
    """

    def __init__(self):
        r"""添加安全组规则
        :param InstanceId: 服务ID
        :type PathPrefix: String
        :param Cidrs: 安全规则IP地址  
  0.0.0.0/16,0.0.0.0/24,多个","分隔
        :type PathPrefix: String
        :param Type: 网络类型。可选：IPV4 或者 IPV6。请注意，字段值严格大写。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Cidrs = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Cidrs"):
            self.Cidrs = params.get("Cidrs")
        if params.get("Type"):
            self.Type = params.get("Type")


class ListSecurityGroupRulesRequest(AbstractModel):
    """ListSecurityGroupRules请求参数结构体
    """

    def __init__(self):
        r"""查询安全组列表
        :param InstanceId: 实例ID 
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class UpdateMongoDBInstanceRequest(AbstractModel):
    """UpdateMongoDBInstance请求参数结构体
    """

    def __init__(self):
        r"""副本集实例更配
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param InstanceClass: 实例配置套餐。 可选:  1C2G        2C4G        4C8G  8C16G    8C32G  16C32G    16C64G    16C128G    32C64G。
        :type PathPrefix: String
        :param Storage: 硬盘大小,单位GB。
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.InstanceClass = None
        self.Storage = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceClass"):
            self.InstanceClass = params.get("InstanceClass")
        if params.get("Storage"):
            self.Storage = params.get("Storage")


class AddSecondaryInstanceRequest(AbstractModel):
    """AddSecondaryInstance请求参数结构体
    """

    def __init__(self):
        r"""副本集实例添加secondary节点
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param NodeNum: 新增节点数量。可选：3、5、7
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.NodeNum = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NodeNum"):
            self.NodeNum = params.get("NodeNum")


class DescribeMongoDBShardNodeRequest(AbstractModel):
    """DescribeMongoDBShardNode请求参数结构体
    """

    def __init__(self):
        r"""分片集群实例shard节点查询
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeValidRegionRequest(AbstractModel):
    """DescribeValidRegion请求参数结构体
    """

    def __init__(self):
        r"""查询用户可用机房详情
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class AllocateEipRequest(AbstractModel):
    """AllocateEip请求参数结构体
    """

    def __init__(self):
        r"""实例绑定外网eip
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Type: ip地址类型。ipv4默认不用填写,若为ipv6则需要填写
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Type"):
            self.Type = params.get("Type")


class DeallocateEipRequest(AbstractModel):
    """DeallocateEip请求参数结构体
    """

    def __init__(self):
        r"""实例解绑外网eip
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体
    """

    def __init__(self):
        r"""查询机房可用区
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class CreateMongoDBShardInstanceRequest(AbstractModel):
    """CreateMongoDBShardInstance请求参数结构体
    """

    def __init__(self):
        r"""创建分片集群实例
        :param PayType: 计费方式：默认为byMonth
 取值范围：byMonth（包年包月）,byDay（按日计费），hourlyInstantSettlement（按小时实时结算）。
        :type PathPrefix: String
        :param AvailabilityZone: 可用区信息，默认为默认为当前Region A区。可[查询可用机房及可用区](https://docs.ksyun.com/documents/6679)
        :type PathPrefix: Filter
        :param Name: 实例名称
 支持6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线和中划线
        :type PathPrefix: String
        :param DbVersion: 数据库版本。如：3.6。
        :type PathPrefix: String
        :param Storage: 硬盘存储空间  根据实例配置选择   单位：GB。只能购买特定规格的套餐,否则将会报错
        :type PathPrefix: String
        :param Duration: 时长 默认值：1(单位:月) 。PayType=byMonth(包年包月)则必填，最大支持范围是(1 ~36月)
        :type PathPrefix: Int
        :param IamProjectId: 项目ID                       
 默认为0：默认项目
        :type PathPrefix: String
        :param VpcId: 虚拟专用网络
 VPC网络ID，可在网络控制台获取。
        :type PathPrefix: String
        :param VnetId: 终端子网id.
        :type PathPrefix: String
        :param InstancePassword: 实例管理员密码.
        :type PathPrefix: String
        :param ShardClass: shard配置。         
        :type PathPrefix: String
        :param ShardNum: shard数量                
  取值范围[2-32]
        :type PathPrefix: Int
        :param MongosNum: mongos数量                
 最小为2，范围[2~32]
        :type PathPrefix: Int
        :param MongosClass: mongos配置 。         
        :type PathPrefix: String
        """
        self.PayType = None
        self.AvailabilityZone = None
        self.Name = None
        self.DbVersion = None
        self.Storage = None
        self.Duration = None
        self.IamProjectId = None
        self.VpcId = None
        self.VnetId = None
        self.InstancePassword = None
        self.ShardClass = None
        self.ShardNum = None
        self.MongosNum = None
        self.MongosClass = None

    def _deserialize(self, params):
        if params.get("PayType"):
            self.PayType = params.get("PayType")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("DbVersion"):
            self.DbVersion = params.get("DbVersion")
        if params.get("Storage"):
            self.Storage = params.get("Storage")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")
        if params.get("ShardClass"):
            self.ShardClass = params.get("ShardClass")
        if params.get("ShardNum"):
            self.ShardNum = params.get("ShardNum")
        if params.get("MongosNum"):
            self.MongosNum = params.get("MongosNum")
        if params.get("MongosClass"):
            self.MongosClass = params.get("MongosClass")


class DownloadSnapshotRequest(AbstractModel):
    """DownloadSnapshot请求参数结构体
    """

    def __init__(self):
        r"""下载备份
        :param SnapshotId: 备份ID。请注意：暂不支持分片集群实例备份的下载。

        :type PathPrefix: String
        """
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class CloneInstanceRequest(AbstractModel):
    """CloneInstance请求参数结构体
    """

    def __init__(self):
        r"""基于备份文件恢复至新实例
        :param PayType: 计费方式。  默认为 原实例计费方式。取值范围：byMonth（包年包月）,byDay（按日计费），hourlyInstantSettlement（按小时实时结算）。
        :type PathPrefix: String
        :param AvailabilityZone: 可用区信息。默认为当前Region A区。

        :type PathPrefix: String
        :param Name: 实例名称。6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线及中划线
        :type PathPrefix: String
        :param Duration: 时长. 包年包月计费方式必填 单位月 例如: duration:6 
        :type PathPrefix: Int
        :param IamProjectId: 所属项目id。默认为：0（默认项目）
        :type PathPrefix: String
        :param VpcId: VPC网络ID，可在网络控制台获取。
        :type PathPrefix: String
        :param VnetId: 终端子网ID,  可在网络控制台获取。
        :type PathPrefix: String
        :param InstancePassword: 实例管理员密码  8~30个字符 必须包含大小写字母和数字 支持的特殊字符为!@#$%^&*()-_+=
        :type PathPrefix: String
        :param SnapshotId: 备份ID。
        :type PathPrefix: String
        :param InstanceId: 副本集实例ID。
        :type PathPrefix: String
        """
        self.PayType = None
        self.AvailabilityZone = None
        self.Name = None
        self.Duration = None
        self.IamProjectId = None
        self.VpcId = None
        self.VnetId = None
        self.InstancePassword = None
        self.SnapshotId = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("PayType"):
            self.PayType = params.get("PayType")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeShardNodeRequest(AbstractModel):
    """DescribeShardNode请求参数结构体
    """

    def __init__(self):
        r"""查询分片集群shard节点列表
        :param InstanceId: 分片集群实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeInstanceStatisticRequest(AbstractModel):
    """DescribeInstanceStatistic请求参数结构体
    """

    def __init__(self):
        r"""概览页统计接口
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class AddClusterNodeRequest(AbstractModel):
    """AddClusterNode请求参数结构体
    """

    def __init__(self):
        r"""添加分片集群的节点。支持mongos和shard节点。
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param NodeType: 节点类型。可选 mongos    shard
        :type PathPrefix: String
        :param NodeClass: mongos或shard的节点规格，必传。只能填规定的规格，如2C4G。
        :type PathPrefix: String
        :param NodeStorage: shard节点的磁盘大小。nodeType选择shard时必填。 
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.NodeType = None
        self.NodeClass = None
        self.NodeStorage = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NodeType"):
            self.NodeType = params.get("NodeType")
        if params.get("NodeClass"):
            self.NodeClass = params.get("NodeClass")
        if params.get("NodeStorage"):
            self.NodeStorage = params.get("NodeStorage")


class DeleteClusterNodeRequest(AbstractModel):
    """DeleteClusterNode请求参数结构体
    """

    def __init__(self):
        r"""删除分片集群节点，只支持mongos节点。
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param NodeId: mongos节点id。可在控制台查看节点id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.NodeId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")


class DescribeSlowLogDetailRequest(AbstractModel):
    """DescribeSlowLogDetail请求参数结构体
    """

    def __init__(self):
        r"""DescribeSlowLogDetail
        :param InstanceId: 实例ID。

        :type PathPrefix: String
        :param NodeId: 节点ID。选填节点ID则查询该节点下的慢SQL详情。
        :type PathPrefix: String
        :param InstanceType: 节点类型 ：HighIO（副本集）、Cluster（分片集群）
        :type PathPrefix: String
        :param Database: 选择要查询的数据库
        :type PathPrefix: String
        :param StartTime: 开始查询时间。yyyy-MM-dd HH:mm:ss 格式。
        :type PathPrefix: String
        :param EndTime: 结束时间。yyyy-MM-dd HH:mm:ss 格式。

        :type PathPrefix: String
        :param Marker: 起始页 默认0页
        :type PathPrefix: Int
        :param MaxRecords: 展示条数	。展示条数 默认10条
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.NodeId = None
        self.InstanceType = None
        self.Database = None
        self.StartTime = None
        self.EndTime = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("Database"):
            self.Database = params.get("Database")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class DescribeSlowLogStatisticsRequest(AbstractModel):
    """DescribeSlowLogStatistics请求参数结构体
    """

    def __init__(self):
        r"""DescribeSlowLogStatistics
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param NodeId: 节点ID。选填节点ID则查询该节点下的慢SQL统计数据
        :type PathPrefix: String
        :param InstanceType: 节点的类型 ：HighIO（副本集）、Cluster（分片集群）
        :type PathPrefix: String
        :param StartTime: 开始查询时间。yyyy-MM-dd HH:mm:ss 格式。
        :type PathPrefix: String
        :param EndTime: 结束时间。yyyy-MM-dd HH:mm:ss 格式。

        :type PathPrefix: String
        :param Marker: 起始页, 默认0页。
        :type PathPrefix: Int
        :param MaxRecords: 展示条数	, 默认10条。
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.NodeId = None
        self.InstanceType = None
        self.StartTime = None
        self.EndTime = None
        self.Marker = None
        self.MaxRecords = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxRecords"):
            self.MaxRecords = params.get("MaxRecords")


class DescribeSlowLogDatabaseRequest(AbstractModel):
    """DescribeSlowLogDatabase请求参数结构体
    """

    def __init__(self):
        r"""DescribeSlowLogDatabase
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param NodeId: 节点ID。加上节点ID则查询该节点下的慢SQL数据库信息。
        :type PathPrefix: String
        :param InstanceType: 节点类型 ：HighIO（副本集）、Cluster（分片集群）
        :type PathPrefix: String
        :param StartTime: 开始查询时间。yyyy-MM-dd HH:mm:ss 格式。
        :type PathPrefix: String
        :param EndTime: 结束时间。yyyy-MM-dd HH:mm:ss 格式。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.NodeId = None
        self.InstanceType = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class DescribeSlowLogLineChartRequest(AbstractModel):
    """DescribeSlowLogLineChart请求参数结构体
    """

    def __init__(self):
        r"""慢查询产生趋势折线图，反映慢查询趋势。
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param NodeId: 加上节点id择查询该节点下的慢SQL折线图数据
        :type PathPrefix: String
        :param InstanceType: 节点类型。节点类型 ：HighIO（副本集）、Cluster（分片集群）
        :type PathPrefix: String
        :param StartTime: yyyy-MM-dd HH:mm:ss 格式
        :type PathPrefix: String
        :param EndTime: 结束时间	。yyyy-MM-dd HH:mm:ss 格式
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.NodeId = None
        self.InstanceType = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class UpdateMongoDBInstanceClusterRequest(AbstractModel):
    """UpdateMongoDBInstanceCluster请求参数结构体
    """

    def __init__(self):
        r"""分片集群节点更配
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param InstanceClass: 实例套餐 可选:  1C2G        2C4G        4C8G         8C16G    8C32G    16C64G
        :type PathPrefix: String
        :param NodeType: 分片集群的更配类型  mongos 或者 shard
        :type PathPrefix: String
        :param NodeId: mongos节点ID 或者 shard节点ID。

        :type PathPrefix: String
        :param Storage: 磁盘大小,单位GB。mongos节点更配不填，shard节点更配必填。
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.InstanceClass = None
        self.NodeType = None
        self.NodeId = None
        self.Storage = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceClass"):
            self.InstanceClass = params.get("InstanceClass")
        if params.get("NodeType"):
            self.NodeType = params.get("NodeType")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")
        if params.get("Storage"):
            self.Storage = params.get("Storage")


class DescribeClusterForRestoreRequest(AbstractModel):
    """DescribeClusterForRestore请求参数结构体
    """

    def __init__(self):
        r"""查询分片集群可恢复配置
        :param InstanceId: MongoDB分片集群实例ID。
        :type PathPrefix: String
        :param ResetTimePoint: 恢复时间点。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ResetTimePoint = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ResetTimePoint"):
            self.ResetTimePoint = params.get("ResetTimePoint")


