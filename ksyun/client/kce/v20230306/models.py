from ksyun.common.abstract_model import AbstractModel


class CreatePrometheusInstanceRequest(AbstractModel):
    """CreatePrometheusInstance请求参数结构体
    """

    def __init__(self):
        r"""创建Prometheus实例
        :param InstanceName: 实例名称，有效值：2-64个字符，支持中文，英文，数字，以及特殊.!$^*()%#&+/:;<=>[]_`{}~
        :type PathPrefix: String
        :param ChargeType: 实例计费方式，目前只支持按量付费有效值：DailyVolume
        :type PathPrefix: String
        :param DataRetentionTime: 数据存储时长，有效值：15、30、45、90、180、365
        :type PathPrefix: Int
        """
        self.InstanceName = None
        self.ChargeType = None
        self.DataRetentionTime = None

    def _deserialize(self, params):
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("DataRetentionTime"):
            self.DataRetentionTime = params.get("DataRetentionTime")


class DescribePrometheusInstanceRequest(AbstractModel):
    """DescribePrometheusInstance请求参数结构体
    """

    def __init__(self):
        r"""查询Prometheus实例
        :param InstanceId: 实例id，若不填，则默认查询该地域下的所有实例
        :type PathPrefix: Filter
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大100
        :type PathPrefix: Int
        :param Search: 模糊匹配，可匹配字段：InstanceName（实例名称）
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Marker = None
        self.MaxResults = None
        self.Search = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Search"):
            self.Search = params.get("Search")


class UpdatePrometheusInstanceRequest(AbstractModel):
    """UpdatePrometheusInstance请求参数结构体
    """

    def __init__(self):
        r"""更新Prometheus实例
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param InstanceName: 修改实例名称
        :type PathPrefix: String
        :param DataRetentionTime: 修改数据存储时长 有效值：15、30、45、90、180、365
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.DataRetentionTime = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("DataRetentionTime"):
            self.DataRetentionTime = params.get("DataRetentionTime")


class DeletePrometheusInstanceRequest(AbstractModel):
    """DeletePrometheusInstance请求参数结构体
    """

    def __init__(self):
        r"""删除Prometheus实例
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class EnableGrafanaRequest(AbstractModel):
    """EnableGrafana请求参数结构体
    """

    def __init__(self):
        r"""开通/关闭Grafana
        :param InstanceId: Grafana所关联的Prometheus的实例id
        :type PathPrefix: String
        :param EnableGrafana: 开通或关闭Grafana，true为开启，false 为不开启
        :type PathPrefix: Boolean
        :param Password: 开通Grafana时需设置Grafana密码有效值：6-24个字符，必须以数字或字母开头，且至少包含一个特殊字符，支持英文特殊字符@$!%*#?&
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.EnableGrafana = None
        self.Password = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("EnableGrafana"):
            self.EnableGrafana = params.get("EnableGrafana")
        if params.get("Password"):
            self.Password = params.get("Password")


class UpdateGrafanaPasswordRequest(AbstractModel):
    """UpdateGrafanaPassword请求参数结构体
    """

    def __init__(self):
        r"""更新Grafana密码
        :param InstanceId: Grafana所关联的Prometheus的实例id
        :type PathPrefix: String
        :param Password: 新的Grafana密码有效值：6-24个字符，必须以数字或字母开头，且至少包含一个特殊字符，支持英文特殊字符@$!%*#?&
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Password = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Password"):
            self.Password = params.get("Password")


class EnableGrafanaInternetRequest(AbstractModel):
    """EnableGrafanaInternet请求参数结构体
    """

    def __init__(self):
        r"""开启/关闭Grafana公网访问
        :param InstanceId: Grafana所关联的Prometheus的实例id
        :type PathPrefix: String
        :param EnableInternet: 开启或关闭公网访问，true为开启，false 为不开启
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.EnableInternet = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("EnableInternet"):
            self.EnableInternet = params.get("EnableInternet")


class DescribeGrafanaWhiteListRequest(AbstractModel):
    """DescribeGrafanaWhiteList请求参数结构体
    """

    def __init__(self):
        r"""查询可访问Grafana公网的IP白名单
        :param InstanceId: Grafana所关联的Prometheus的实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class UpdateGrafanaWhiteListRequest(AbstractModel):
    """UpdateGrafanaWhiteList请求参数结构体
    """

    def __init__(self):
        r"""更新可访问Grafana公网的IP白名单
        :param InstanceId: Grafana所关联的Prometheus的实例id
        :type PathPrefix: String
        :param WhiteList: 白名单数组，输入公网域名IP或网段，例如：127.0.0.1或127.0.0.1/24
        :type PathPrefix: Filter
        """
        self.InstanceId = None
        self.WhiteList = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("WhiteList"):
            self.WhiteList = params.get("WhiteList")


class AssociateClusterRequest(AbstractModel):
    """AssociateCluster请求参数结构体
    """

    def __init__(self):
        r"""关联集群
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class DisassociateClusterRequest(AbstractModel):
    """DisassociateCluster请求参数结构体
    """

    def __init__(self):
        r"""解除关联集群
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class DescribeAssociateClusterListRequest(AbstractModel):
    """DescribeAssociateClusterList请求参数结构体
    """

    def __init__(self):
        r"""查询关联集群列表
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部关联集群时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大关联集群数目，默认20，最大100
        :type PathPrefix: Int
        :param ClusterId: 集群id，支持输入多个集群id进行查询，若不填默认查询所有的关联集群
        :type PathPrefix: Filter
        """
        self.InstanceId = None
        self.Marker = None
        self.MaxResults = None
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class DescribeMonitorListRequest(AbstractModel):
    """DescribeMonitorList请求参数结构体
    """

    def __init__(self):
        r"""查询监控列表
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MonitorSource: 监控采集配置来源，有效值：
Basic
Custom
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回监控项时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大监控数目，默认20，最大100
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.ClusterId = None
        self.MonitorSource = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MonitorSource"):
            self.MonitorSource = params.get("MonitorSource")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class DescribeMonitorCollectionConfigRequest(AbstractModel):
    """DescribeMonitorCollectionConfig请求参数结构体
    """

    def __init__(self):
        r"""查询监控采集配置
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MonitorName: 监控采集配置名称
        :type PathPrefix: String
        :param Type: 监控采集配置类型，有效值：
RawJob
PodMonitor
ServiceMonitor
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ClusterId = None
        self.MonitorName = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MonitorName"):
            self.MonitorName = params.get("MonitorName")
        if params.get("Type"):
            self.Type = params.get("Type")


class UpdateMonitorCollectionConfigRequest(AbstractModel):
    """UpdateMonitorCollectionConfig请求参数结构体
    """

    def __init__(self):
        r"""更新监控采集配置
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MonitorName: 监控采集配置名称
        :type PathPrefix: String
        :param Type: 监控采集配置类型，有效值： 
RawJob
PodMonitor
ServiceMonitor
        :type PathPrefix: String
        :param ConfigYaml: 监控采集配置yaml
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ClusterId = None
        self.MonitorName = None
        self.Type = None
        self.ConfigYaml = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MonitorName"):
            self.MonitorName = params.get("MonitorName")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("ConfigYaml"):
            self.ConfigYaml = params.get("ConfigYaml")


class DescribeMonitorMetricsListRequest(AbstractModel):
    """DescribeMonitorMetricsList请求参数结构体
    """

    def __init__(self):
        r"""查询监控指标
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MonitorName: 监控采集配置名称
        :type PathPrefix: String
        :param Type: 监控采集配置类型，有效值： 
RawJob
PodMonitor
ServiceMonitor
        :type PathPrefix: String
        :param IsCollect: 监控指标是否开启采集,有效值： 
true：已开启指标
false：废弃指标
        :type PathPrefix: Boolean
        :param Marker: 分页标识
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大指标数目，默认20，最大100
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.ClusterId = None
        self.MonitorName = None
        self.Type = None
        self.IsCollect = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MonitorName"):
            self.MonitorName = params.get("MonitorName")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("IsCollect"):
            self.IsCollect = params.get("IsCollect")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class DescribeTargetsListRequest(AbstractModel):
    """DescribeTargetsList请求参数结构体
    """

    def __init__(self):
        r"""查询采集目标列表
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MonitorName: 监控采集配置名称
        :type PathPrefix: String
        :param Type: 监控采集配置类型，有效值： 
RawJob
PodMonitor
ServiceMonitor
        :type PathPrefix: String
        :param Marker: 分页标识
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大targets数目，默认20，最大100
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.ClusterId = None
        self.MonitorName = None
        self.Type = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MonitorName"):
            self.MonitorName = params.get("MonitorName")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class DescribeAgentStatusRequest(AbstractModel):
    """DescribeAgentStatus请求参数结构体
    """

    def __init__(self):
        r"""查询agent状态
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class CreateMonitorCollectionConfigRequest(AbstractModel):
    """CreateMonitorCollectionConfig请求参数结构体
    """

    def __init__(self):
        r"""创建监控采集配置
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param Type: 监控采集配置类型，有效值：
RawJob
PodMonitor
ServiceMonitor
        :type PathPrefix: String
        :param ConfigYaml: 监控采集配置yaml
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ClusterId = None
        self.Type = None
        self.ConfigYaml = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("ConfigYaml"):
            self.ConfigYaml = params.get("ConfigYaml")


class DeleteMonitorCollectionConfigRequest(AbstractModel):
    """DeleteMonitorCollectionConfig请求参数结构体
    """

    def __init__(self):
        r"""删除监控采集配置
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MonitorName: 监控采集配置名称
        :type PathPrefix: String
        :param Type: 	
监控采集配置类型，有效值：
RawJob
PodMonitor
ServiceMonitor
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ClusterId = None
        self.MonitorName = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MonitorName"):
            self.MonitorName = params.get("MonitorName")
        if params.get("Type"):
            self.Type = params.get("Type")


class EnableMetricsRequest(AbstractModel):
    """EnableMetrics请求参数结构体
    """

    def __init__(self):
        r"""开启指标
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MonitorName: 监控采集配置名称
        :type PathPrefix: String
        :param Type: 	
监控采集配置类型，有效值：
RawJob
PodMonitor
ServiceMonitor
        :type PathPrefix: String
        :param MetricsName: 指标名称
        :type PathPrefix: Filter
        """
        self.InstanceId = None
        self.ClusterId = None
        self.MonitorName = None
        self.Type = None
        self.MetricsName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MonitorName"):
            self.MonitorName = params.get("MonitorName")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("MetricsName"):
            self.MetricsName = params.get("MetricsName")


class DropMetricsRequest(AbstractModel):
    """DropMetrics请求参数结构体
    """

    def __init__(self):
        r"""废弃指标
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MonitorName: 监控采集配置名称
        :type PathPrefix: String
        :param Type: 	
监控采集配置类型，有效值：
RawJob
PodMonitor
ServiceMonitor
        :type PathPrefix: String
        :param MetricsName: 指标名称
        :type PathPrefix: Filter
        """
        self.InstanceId = None
        self.ClusterId = None
        self.MonitorName = None
        self.Type = None
        self.MetricsName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MonitorName"):
            self.MonitorName = params.get("MonitorName")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("MetricsName"):
            self.MetricsName = params.get("MetricsName")
