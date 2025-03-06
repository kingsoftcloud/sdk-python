from ksyun.common.abstract_model import AbstractModel

class DescribeClusterRequest(AbstractModel):
    """DescribeCluster请求参数结构体
    """

    def __init__(self):
        r"""集群详情
        :param ClusterId: 集群id
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class LaunchClusterRequest(AbstractModel):
    """LaunchCluster请求参数结构体
    """

    def __init__(self):
        r"""创建集群
        :param ClusterName: 集群名称
        :type PathPrefix: String
        :param Distribution: 集群类型
可选值：
- Hadoop
- Kafka
- RocketMQ
- Zookeeper
        :type PathPrefix: String
        :param MainVersion: 产品版本，对应于不同的集群类型
可选值：
- Hadoop版本：5.3.0，5.2.1，5.2.0，5.1.0，5.0.0
- Kafka版本：2.8.1，2.2.2
- RocketMQ版本：4.9.2
- Zookeeper版本：3.6.4，3.5.8，3.4.6
        :type PathPrefix: String
        :param ChargeType: 计费方式
可选值：
- 按日月结：Daily
- 按量付费：HourlyInstantSettlement
        :type PathPrefix: String
        :param DatabaseInfo: 元数组高可用信息：
        :type PathPrefix: Object
        :param Services: 组件列表：
1. Hadoop
 - 必选组件：	zookeeper(3.6.4)、hdfs(3.3.6)、yarn(3.3.6)、mapreduce(3.3.6)、tez(0.10.2)
 - 可选组件：hbase(2.5.5)、hive(3.1.3)、ranger(2.3.0)、spark(3.3.3)、flink(1.17.1)、presto(0.283)、trino(433)、sqoop(1.4.7)、hue(4.10.0)、zeppelin(0.10.0)、kafka(2.8.1)、iceberg(1.3.1)、hudi(0.12.3)、kudu(1.15.0)、impala(3.4.0)、prometheus(2.37.2)、grafana(8.5.15)、dolphinscheduler(3.1.9)、celeborn(0.5.0)
 2. Kafka
 - 必选组件：zookeeper(3.4.6)、kafka(2.8.1)
 3. RocketMQ
 - 必选组件：rocketmq(4.9.2)
 4. Zookeeper
 - 必选组件：zookeeper(3.6.4)
        :type PathPrefix: Array
        :param ProjectId: 项目 ID，参考「项目管理」，默认为 0
        :type PathPrefix: Int
        :param VpcDomainId: VPC 网络的 ID
        :type PathPrefix: String
        :param SecurityGroupId: 安全组的 ID
        :type PathPrefix: String
        :param InstanceGroups: 节点组信息
        :type PathPrefix: Array
        """
        self.ClusterName = None
        self.Distribution = None
        self.MainVersion = None
        self.ChargeType = None
        self.DatabaseInfo = None
        self.Services = None
        self.ProjectId = None
        self.VpcDomainId = None
        self.SecurityGroupId = None
        self.InstanceGroups = None

    def _deserialize(self, params):
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("Distribution"):
            self.Distribution = params.get("Distribution")
        if params.get("MainVersion"):
            self.MainVersion = params.get("MainVersion")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("DatabaseInfo"):
            self.DatabaseInfo = params.get("DatabaseInfo")
        if params.get("Services"):
            self.Services = params.get("Services")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("VpcDomainId"):
            self.VpcDomainId = params.get("VpcDomainId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstanceGroups"):
            self.InstanceGroups = params.get("InstanceGroups")


class ScaleInInstanceGroupsRequest(AbstractModel):
    """ScaleInInstanceGroups请求参数结构体
    """

    def __init__(self):
        r"""缩容集群
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param InstanceGroups: 要缩容的节点组，需要注意的是，一次只能对一个节点组进行操作
        :type PathPrefix: Array
        :param GracefulScaleIn: 是否开启优雅缩容
        :type PathPrefix: Boolean
        :param GracefulScaleInTimeout: 优雅缩容等待时间，如果开启优雅缩容，则需要设定该参数，范围0-120, 单位秒
        :type PathPrefix: Int
        """
        self.ClusterId = None
        self.InstanceGroups = None
        self.GracefulScaleIn = None
        self.GracefulScaleInTimeout = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceGroups"):
            self.InstanceGroups = params.get("InstanceGroups")
        if params.get("GracefulScaleIn"):
            self.GracefulScaleIn = params.get("GracefulScaleIn")
        if params.get("GracefulScaleInTimeout"):
            self.GracefulScaleInTimeout = params.get("GracefulScaleInTimeout")


class ScaleOutInstanceGroupsRequest(AbstractModel):
    """ScaleOutInstanceGroups请求参数结构体
    """

    def __init__(self):
        r"""扩容集群
        :param ClusterId: 集群ID

        :type PathPrefix: String
        :param InstanceGroups: 节点组信息
        :type PathPrefix: Array
        :param ProjectId: 项目 ID，参考「项目管理」
        :type PathPrefix: Int
        """
        self.ClusterId = None
        self.InstanceGroups = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceGroups"):
            self.InstanceGroups = params.get("InstanceGroups")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribeClusterInfoRequest(AbstractModel):
    """DescribeClusterInfo请求参数结构体
    """

    def __init__(self):
        r"""集群详情描述
        :param ClusterId: 集群ID

        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class ListServiceStatusRequest(AbstractModel):
    """ListServiceStatus请求参数结构体
    """

    def __init__(self):
        r"""查看服务列表
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class ListClustersRequest(AbstractModel):
    """ListClusters请求参数结构体
    """

    def __init__(self):
        r"""集群列表
        :param Marker: 分页参数
        :type PathPrefix: String
        """
        self.Marker = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ListClusterVersionsRequest(AbstractModel):
    """ListClusterVersions请求参数结构体
    """

    def __init__(self):
        r"""集群版本列表
        :param DistributionVersion: KMR 集群类型
可选值：
- Hadoop
- Kafka
- Zookeeper
- RocketMQ
        :type PathPrefix: String
        """
        self.DistributionVersion = None

    def _deserialize(self, params):
        if params.get("DistributionVersion"):
            self.DistributionVersion = params.get("DistributionVersion")


class DescribeServiceRequest(AbstractModel):
    """DescribeService请求参数结构体
    """

    def __init__(self):
        r"""查看服务详情
        :param ClusterId: 集群ID

        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class ListConfigurationsRequest(AbstractModel):
    """ListConfigurations请求参数结构体
    """

    def __init__(self):
        r"""配置列表
        :param ClusterId: 
        :type PathPrefix: String
        :param ServiceName: 服务名称：hdfs,mapreduce,yarn,gaea,zookeeper,spark,spark2,flink,flink1,hive,tez,presto,trino,oozie,sqoop,hue,zeppelin,hbase,kafka,knox,rocketmq,impala,iceberg,hudi,kudu,gatherer,prometheus,grafana,kerberos,ranger,dolphinscheduler,celeborn
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.ServiceName = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ServiceName"):
            self.ServiceName = params.get("ServiceName")


class ListConfigurationHistoryRequest(AbstractModel):
    """ListConfigurationHistory请求参数结构体
    """

    def __init__(self):
        r"""配置历史
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param ServiceName: 服务名称：hdfs,mapreduce,yarn,gaea,zookeeper,spark,spark2,flink,flink1,hive,tez,presto,trino,oozie,sqoop,hue,zeppelin,hbase,kafka,knox,rocketmq,impala,iceberg,hudi,kudu,gatherer,prometheus,grafana,kerberos,ranger,dolphinscheduler,celeborn
        :type PathPrefix: String
        :param Marker: 分页信息
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.ServiceName = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ServiceName"):
            self.ServiceName = params.get("ServiceName")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ListTagValuesRequest(AbstractModel):
    """ListTagValues请求参数结构体
    """

    def __init__(self):
        r"""标签值列表
        :param ClusterId: 集群ID

        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class ListTagKeysRequest(AbstractModel):
    """ListTagKeys请求参数结构体
    """

    def __init__(self):
        r"""标签列表
        :param ClusterId: 集群ID

        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class BindTagsRequest(AbstractModel):
    """BindTags请求参数结构体
    """

    def __init__(self):
        r"""绑定标签
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param Tags: 标签列表
        :type PathPrefix: Array
        """
        self.ClusterId = None
        self.Tags = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("Tags"):
            self.Tags = params.get("Tags")


class StartInstancesRequest(AbstractModel):
    """StartInstances请求参数结构体
    """

    def __init__(self):
        r"""启动实例
        :param ClusterId: 集群ID

        :type PathPrefix: String
        :param InstanceIds: 主机实例ID

        :type PathPrefix: Array
        """
        self.ClusterId = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class RestartInstancesRequest(AbstractModel):
    """RestartInstances请求参数结构体
    """

    def __init__(self):
        r"""重启实例
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param InstanceIds: 主机实例ID
        :type PathPrefix: Array
        :param Interval: 滚动重启间隔时间，RollingRestart为true时填写，默认60s
        :type PathPrefix: Int
        :param RollingRestart: 是否滚动重启
        :type PathPrefix: Boolean
        :param ForceReboot: 是否强制重启
        :type PathPrefix: Boolean
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.Interval = None
        self.RollingRestart = None
        self.ForceReboot = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("RollingRestart"):
            self.RollingRestart = params.get("RollingRestart")
        if params.get("ForceReboot"):
            self.ForceReboot = params.get("ForceReboot")


class StopInstancesRequest(AbstractModel):
    """StopInstances请求参数结构体
    """

    def __init__(self):
        r"""停止实例
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param InstanceIds: 主机实例ID
        :type PathPrefix: Array
        """
        self.ClusterId = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class ListScaleStrategyRequest(AbstractModel):
    """ListScaleStrategy请求参数结构体
    """

    def __init__(self):
        r"""弹性策略列表
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class ModifyScaleStrategyRequest(AbstractModel):
    """ModifyScaleStrategy请求参数结构体
    """

    def __init__(self):
        r"""弹性策略描述
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class DeleteScaleStrategyRequest(AbstractModel):
    """DeleteScaleStrategy请求参数结构体
    """

    def __init__(self):
        r"""删除弹性策略
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param StrategyId: 弹性策略的ID
        :type PathPrefix: String
        :param StrategyModule: 弹性策略的类型
- 时间弹性：Time-Based
- 负载弹性：Load-Based
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.StrategyId = None
        self.StrategyModule = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")
        if params.get("StrategyModule"):
            self.StrategyModule = params.get("StrategyModule")


class ListScaleHistoryRequest(AbstractModel):
    """ListScaleHistory请求参数结构体
    """

    def __init__(self):
        r"""弹性伸缩历史
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class AddLoadBasedScaleStrategyRequest(AbstractModel):
    """AddLoadBasedScaleStrategy请求参数结构体
    """

    def __init__(self):
        r"""添加负载弹性策略
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class ModifyLoadBasedScaleStrategyRequest(AbstractModel):
    """ModifyLoadBasedScaleStrategy请求参数结构体
    """

    def __init__(self):
        r"""修改负载弹性策略
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


