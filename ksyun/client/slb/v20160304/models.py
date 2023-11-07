from ksyun.common.abstract_model import AbstractModel

class DescribeListenersRequest(AbstractModel):
    """DescribeListeners请求参数结构体
    """

    def __init__(self):
        r"""描述监听器
        :param ListenerId: 多个监听器的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.ListenerId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeleteListenersRequest(AbstractModel):
    """DeleteListeners请求参数结构体
    """

    def __init__(self):
        r"""删除监听器
        :param ListenerId: 监听器的ID
        :type PathPrefix: String
        """
        self.ListenerId = None

    def _deserialize(self, params):
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")


class ModifyListenersRequest(AbstractModel):
    """ModifyListeners请求参数结构体
    """

    def __init__(self):
        r"""修改监听器配置
        :param ListenerId: 监听器的ID
        :type PathPrefix: String
        :param ListenerName: 监听器的名称
        :type PathPrefix: String
        :param ListenerState: 监听器的状态(start|stop)
        :type PathPrefix: String
        :param Method: 监听器的转发方式(RoundRobin|LeastConnections|MasterSlave|QUIC_CID|IPHash)
        :type PathPrefix: String
        :param BandWidthIn: 监听器的入带宽限速，单位Mbps，仅内网LB有此字段
        :type PathPrefix: Int
        :param BandWidthOut: 监听器的出带宽限速，单位Mbps，仅内网LB有此字段
        :type PathPrefix: Int
        :param HttpProtocol: 后端协议版本(HTTP1.0|HTTP1.1)
        :type PathPrefix: String
        :param TlsCipherPolicy: TLS安全策略
        :type PathPrefix: String
        :param EnableHttp2: 是否启用HTTP/2，HTTPS监听器需要传此参数
        :type PathPrefix: Boolean
        :param SessionState: 会话保持的状态
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param CookieType: 会话类型
        :type PathPrefix: String
        :param CookieName: Cookie的名称
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        :param RedirectListenerId: 重定向监听器ID
        :type PathPrefix: String
        """
        self.ListenerId = None
        self.ListenerName = None
        self.ListenerState = None
        self.Method = None
        self.BandWidthIn = None
        self.BandWidthOut = None
        self.HttpProtocol = None
        self.TlsCipherPolicy = None
        self.EnableHttp2 = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.CookieType = None
        self.CookieName = None
        self.CertificateId = None
        self.RedirectListenerId = None

    def _deserialize(self, params):
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")
        if params.get("ListenerName"):
            self.ListenerName = params.get("ListenerName")
        if params.get("ListenerState"):
            self.ListenerState = params.get("ListenerState")
        if params.get("Method"):
            self.Method = params.get("Method")
        if params.get("BandWidthIn"):
            self.BandWidthIn = params.get("BandWidthIn")
        if params.get("BandWidthOut"):
            self.BandWidthOut = params.get("BandWidthOut")
        if params.get("HttpProtocol"):
            self.HttpProtocol = params.get("HttpProtocol")
        if params.get("TlsCipherPolicy"):
            self.TlsCipherPolicy = params.get("TlsCipherPolicy")
        if params.get("EnableHttp2"):
            self.EnableHttp2 = params.get("EnableHttp2")
        if params.get("SessionState"):
            self.SessionState = params.get("SessionState")
        if params.get("SessionPersistencePeriod"):
            self.SessionPersistencePeriod = params.get("SessionPersistencePeriod")
        if params.get("CookieType"):
            self.CookieType = params.get("CookieType")
        if params.get("CookieName"):
            self.CookieName = params.get("CookieName")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("RedirectListenerId"):
            self.RedirectListenerId = params.get("RedirectListenerId")


class CreateListenersRequest(AbstractModel):
    """CreateListeners请求参数结构体
    """

    def __init__(self):
        r"""创建监听器
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param ListenerName: 监听器的名称
        :type PathPrefix: String
        :param ListenerState: 监听器的状态(start|stop)
        :type PathPrefix: String
        :param ListenerProtocol: 监听器的协议(TCP|HTTP|HTTPS|UDP)
        :type PathPrefix: String
        :param ListenerPort: 监听器的协议端口
        :type PathPrefix: Int
        :param Method: 监听器的转发方式(RoundRobin|LeastConnections|MasterSlave|QUIC_CID|IPHash)
        :type PathPrefix: String
        :param BandWidthIn: 监听器的入带宽限速，单位Mbps，仅内网LB有此字段
        :type PathPrefix: Int
        :param BandWidthOut: 监听器的出带宽限速，单位Mbps，仅内网LB有此字段
        :type PathPrefix: Int
        :param LoadBalancerAclId: LoadBalancerAcl的ID
        :type PathPrefix: String
        :param HttpProtocol: 后端协议版本(HTTP1.0|HTTP1.1)
        :type PathPrefix: String
        :param TlsCipherPolicy: TLS安全策略
        :type PathPrefix: String
        :param EnableHttp2: 是否启用HTTP/2，HTTPS监听器需要传此参数
        :type PathPrefix: Boolean
        :param RedirectListenerId: 重定向监听器ID
        :type PathPrefix: String
        :param SessionState: 会话保持的状态
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param CookieType: 会话类型
        :type PathPrefix: String
        :param CookieName: Cookie的名称
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        """
        self.LoadBalancerId = None
        self.ListenerName = None
        self.ListenerState = None
        self.ListenerProtocol = None
        self.ListenerPort = None
        self.Method = None
        self.BandWidthIn = None
        self.BandWidthOut = None
        self.LoadBalancerAclId = None
        self.HttpProtocol = None
        self.TlsCipherPolicy = None
        self.EnableHttp2 = None
        self.RedirectListenerId = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.CookieType = None
        self.CookieName = None
        self.CertificateId = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerName"):
            self.ListenerName = params.get("ListenerName")
        if params.get("ListenerState"):
            self.ListenerState = params.get("ListenerState")
        if params.get("ListenerProtocol"):
            self.ListenerProtocol = params.get("ListenerProtocol")
        if params.get("ListenerPort"):
            self.ListenerPort = params.get("ListenerPort")
        if params.get("Method"):
            self.Method = params.get("Method")
        if params.get("BandWidthIn"):
            self.BandWidthIn = params.get("BandWidthIn")
        if params.get("BandWidthOut"):
            self.BandWidthOut = params.get("BandWidthOut")
        if params.get("LoadBalancerAclId"):
            self.LoadBalancerAclId = params.get("LoadBalancerAclId")
        if params.get("HttpProtocol"):
            self.HttpProtocol = params.get("HttpProtocol")
        if params.get("TlsCipherPolicy"):
            self.TlsCipherPolicy = params.get("TlsCipherPolicy")
        if params.get("EnableHttp2"):
            self.EnableHttp2 = params.get("EnableHttp2")
        if params.get("RedirectListenerId"):
            self.RedirectListenerId = params.get("RedirectListenerId")
        if params.get("SessionState"):
            self.SessionState = params.get("SessionState")
        if params.get("SessionPersistencePeriod"):
            self.SessionPersistencePeriod = params.get("SessionPersistencePeriod")
        if params.get("CookieType"):
            self.CookieType = params.get("CookieType")
        if params.get("CookieName"):
            self.CookieName = params.get("CookieName")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")


class ModifyInstancesWithListenerRequest(AbstractModel):
    """ModifyInstancesWithListener请求参数结构体
    """

    def __init__(self):
        r"""修改真实服务器信息
        :param RegisterId: 后端服务器的ID
        :type PathPrefix: String
        :param Weight: 实例的权重
        :type PathPrefix: Int
        :param RealServerPort: 后端服务的端口
        :type PathPrefix: Int
        :param MasterSlaveType: RealServer的主备类型(Master | Slave)，仅MasterSlave监听器有此参数
        :type PathPrefix: String
        :param Tag: 标签
        :type PathPrefix: String
        """
        self.RegisterId = None
        self.Weight = None
        self.RealServerPort = None
        self.MasterSlaveType = None
        self.Tag = None

    def _deserialize(self, params):
        if params.get("RegisterId"):
            self.RegisterId = params.get("RegisterId")
        if params.get("Weight"):
            self.Weight = params.get("Weight")
        if params.get("RealServerPort"):
            self.RealServerPort = params.get("RealServerPort")
        if params.get("MasterSlaveType"):
            self.MasterSlaveType = params.get("MasterSlaveType")
        if params.get("Tag"):
            self.Tag = params.get("Tag")


class RegisterInstancesWithListenerRequest(AbstractModel):
    """RegisterInstancesWithListener请求参数结构体
    """

    def __init__(self):
        r"""监听器中绑定真实服务器
        :param RealServerType: 后端服务器的类型(host|DirectConnectGateway)
        :type PathPrefix: String
        :param ListenerId: 监听器的ID
        :type PathPrefix: String
        :param Weight: 实例的权重
        :type PathPrefix: Int
        :param RealServerIp: 真实服务的IP
        :type PathPrefix: String
        :param RealServerPort: 后端服务的端口
        :type PathPrefix: Int
        :param InstanceId: - 实例ID
- host类型，填写云主机或者云物理主机的ID
        :type PathPrefix: String
        :param Tag: 标签
        :type PathPrefix: String
        :param MasterSlaveType: RealServer的主备类型(Master | Slave)，仅MasterSlave监听器有此参数
        :type PathPrefix: String
        """
        self.RealServerType = None
        self.ListenerId = None
        self.Weight = None
        self.RealServerIp = None
        self.RealServerPort = None
        self.InstanceId = None
        self.Tag = None
        self.MasterSlaveType = None

    def _deserialize(self, params):
        if params.get("RealServerType"):
            self.RealServerType = params.get("RealServerType")
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")
        if params.get("Weight"):
            self.Weight = params.get("Weight")
        if params.get("RealServerIp"):
            self.RealServerIp = params.get("RealServerIp")
        if params.get("RealServerPort"):
            self.RealServerPort = params.get("RealServerPort")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Tag"):
            self.Tag = params.get("Tag")
        if params.get("MasterSlaveType"):
            self.MasterSlaveType = params.get("MasterSlaveType")


class DeregisterInstancesFromListenerRequest(AbstractModel):
    """DeregisterInstancesFromListener请求参数结构体
    """

    def __init__(self):
        r"""解绑真实服务器
        :param RegisterId: 后端服务器的ID
        :type PathPrefix: String
        """
        self.RegisterId = None

    def _deserialize(self, params):
        if params.get("RegisterId"):
            self.RegisterId = params.get("RegisterId")


class DescribeInstancesWithListenerRequest(AbstractModel):
    """DescribeInstancesWithListener请求参数结构体
    """

    def __init__(self):
        r"""描述监听器中的真实服务器
        :param RegisterId: 多个后端服务器的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.RegisterId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("RegisterId"):
            self.RegisterId = params.get("RegisterId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ModifyHealthCheckRequest(AbstractModel):
    """ModifyHealthCheck请求参数结构体
    """

    def __init__(self):
        r"""修改健康检查
        :param HealthCheckId: 健康检查的ID
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)
        :type PathPrefix: String
        :param HealthCheckConnectPort: 健康端口
        :type PathPrefix: Int
        :param HealthyThreshold: 健康阈值
        :type PathPrefix: Int
        :param Interval: 健康检查时间间隔
        :type PathPrefix: Int
        :param Timeout: 健康检查超时时间
        :type PathPrefix: Int
        :param UnhealthyThreshold: 不健康阈值
        :type PathPrefix: Int
        :param HttpMethod: HTTP请求方式 (GET|HEAD)
        :type PathPrefix: String
        :param UrlPath: HTTP类型监听器健康检查的链接
        :type PathPrefix: String
        :param HostName: HTTP类型健康检查的域名
        :type PathPrefix: String
        :param HealthCheckReq: UDP监听健康检查的请求串
        :type PathPrefix: String
        :param HealthCheckExp: UDP监听健康检查的响应串
        :type PathPrefix: String
        """
        self.HealthCheckId = None
        self.HealthCheckState = None
        self.HealthCheckConnectPort = None
        self.HealthyThreshold = None
        self.Interval = None
        self.Timeout = None
        self.UnhealthyThreshold = None
        self.HttpMethod = None
        self.UrlPath = None
        self.HostName = None
        self.HealthCheckReq = None
        self.HealthCheckExp = None

    def _deserialize(self, params):
        if params.get("HealthCheckId"):
            self.HealthCheckId = params.get("HealthCheckId")
        if params.get("HealthCheckState"):
            self.HealthCheckState = params.get("HealthCheckState")
        if params.get("HealthCheckConnectPort"):
            self.HealthCheckConnectPort = params.get("HealthCheckConnectPort")
        if params.get("HealthyThreshold"):
            self.HealthyThreshold = params.get("HealthyThreshold")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("UnhealthyThreshold"):
            self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        if params.get("HttpMethod"):
            self.HttpMethod = params.get("HttpMethod")
        if params.get("UrlPath"):
            self.UrlPath = params.get("UrlPath")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("HealthCheckReq"):
            self.HealthCheckReq = params.get("HealthCheckReq")
        if params.get("HealthCheckExp"):
            self.HealthCheckExp = params.get("HealthCheckExp")


class DeleteHealthCheckRequest(AbstractModel):
    """DeleteHealthCheck请求参数结构体
    """

    def __init__(self):
        r"""删除健康检查
        :param HealthCheckId: 健康检查的ID
        :type PathPrefix: String
        """
        self.HealthCheckId = None

    def _deserialize(self, params):
        if params.get("HealthCheckId"):
            self.HealthCheckId = params.get("HealthCheckId")


class DescribeHealthChecksRequest(AbstractModel):
    """DescribeHealthChecks请求参数结构体
    """

    def __init__(self):
        r"""描述健康检查
        :param HealthCheckId: 多个健康检查的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param Limit: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param Marker: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.HealthCheckId = None
        self.Filter = None
        self.Limit = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("HealthCheckId"):
            self.HealthCheckId = params.get("HealthCheckId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ConfigureHealthCheckRequest(AbstractModel):
    """ConfigureHealthCheck请求参数结构体
    """

    def __init__(self):
        r"""创建健康检查
        :param ListenerId: 监听器的ID
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)
        :type PathPrefix: String
        :param HealthCheckConnectPort: 健康检查端口
        :type PathPrefix: Int
        :param HealthyThreshold: 健康阈值
        :type PathPrefix: Int
        :param Interval: 健康检查时间间隔
        :type PathPrefix: Int
        :param Timeout: 健康检查超时时间
        :type PathPrefix: Int
        :param UnhealthyThreshold: 不健康阈值
        :type PathPrefix: Int
        :param HttpMethod: HTTP请求方式 (GET|HEAD)
        :type PathPrefix: String
        :param UrlPath: HTTP类型监听器健康检查的链接
        :type PathPrefix: String
        :param HostName: HTTP类型健康检查的域名
        :type PathPrefix: String
        :param HealthCheckReq: UDP监听健康检查的请求串
        :type PathPrefix: String
        :param HealthCheckExp: UDP监听健康检查的响应串
        :type PathPrefix: String
        """
        self.ListenerId = None
        self.HealthCheckState = None
        self.HealthCheckConnectPort = None
        self.HealthyThreshold = None
        self.Interval = None
        self.Timeout = None
        self.UnhealthyThreshold = None
        self.HttpMethod = None
        self.UrlPath = None
        self.HostName = None
        self.HealthCheckReq = None
        self.HealthCheckExp = None

    def _deserialize(self, params):
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")
        if params.get("HealthCheckState"):
            self.HealthCheckState = params.get("HealthCheckState")
        if params.get("HealthCheckConnectPort"):
            self.HealthCheckConnectPort = params.get("HealthCheckConnectPort")
        if params.get("HealthyThreshold"):
            self.HealthyThreshold = params.get("HealthyThreshold")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("UnhealthyThreshold"):
            self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        if params.get("HttpMethod"):
            self.HttpMethod = params.get("HttpMethod")
        if params.get("UrlPath"):
            self.UrlPath = params.get("UrlPath")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("HealthCheckReq"):
            self.HealthCheckReq = params.get("HealthCheckReq")
        if params.get("HealthCheckExp"):
            self.HealthCheckExp = params.get("HealthCheckExp")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体
    """

    def __init__(self):
        r"""描述负载均衡
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param LoadBalancerId: 多个负载均衡的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        :param State: 负载均衡的状态，已绑定(associate)，未绑定(disassociate)
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.LoadBalancerId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None
        self.State = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("State"):
            self.State = params.get("State")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer请求参数结构体
    """

    def __init__(self):
        r"""删除负载均衡
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        """
        self.LoadBalancerId = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")


class ModifyLoadBalancerRequest(AbstractModel):
    """ModifyLoadBalancer请求参数结构体
    """

    def __init__(self):
        r"""修改负载均衡信息
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param LoadBalancerName: 负载均衡的名称
        :type PathPrefix: String
        :param LoadBalancerState: 负载均衡的开启状态(start|stop)
        :type PathPrefix: String
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerState = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("LoadBalancerName"):
            self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("LoadBalancerState"):
            self.LoadBalancerState = params.get("LoadBalancerState")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer请求参数结构体
    """

    def __init__(self):
        r"""创建负载均衡
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param LoadBalancerName: 负载均衡的名称
        :type PathPrefix: String
        :param Type: 负载均衡的类型，public 为公网负载均衡，internal 为内网负载均衡
        :type PathPrefix: String
        :param SubnetId: 终端子网的 ID，Type 为 public 时忽略此参数，为internal 时此参数必填
        :type PathPrefix: String
        :param PrivateIpAddress: 私网负载均衡的IP，Type 为 Public 时忽略此参数
        :type PathPrefix: String
        :param IpVersion: 负载均衡的IP版本
        :type PathPrefix: String
        :param LbType: 负载均衡类型(classic|application)
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        """
        self.VpcId = None
        self.LoadBalancerName = None
        self.Type = None
        self.SubnetId = None
        self.PrivateIpAddress = None
        self.IpVersion = None
        self.LbType = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("LoadBalancerName"):
            self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")
        if params.get("LbType"):
            self.LbType = params.get("LbType")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class CreateHostHeaderRequest(AbstractModel):
    """CreateHostHeader请求参数结构体
    """

    def __init__(self):
        r"""创建经典型负载均衡域名
        :param ListenerId: 监听器的ID
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        :param HostHeader: 域名
        :type PathPrefix: String
        """
        self.ListenerId = None
        self.CertificateId = None
        self.HostHeader = None

    def _deserialize(self, params):
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("HostHeader"):
            self.HostHeader = params.get("HostHeader")


class ModifyHostHeaderRequest(AbstractModel):
    """ModifyHostHeader请求参数结构体
    """

    def __init__(self):
        r"""修改经典型负载均衡域名
        :param HostHeaderId: 域名的ID
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        """
        self.HostHeaderId = None
        self.CertificateId = None

    def _deserialize(self, params):
        if params.get("HostHeaderId"):
            self.HostHeaderId = params.get("HostHeaderId")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")


class DeleteHostHeaderRequest(AbstractModel):
    """DeleteHostHeader请求参数结构体
    """

    def __init__(self):
        r"""删除经典型负载均衡域名
        :param HostHeaderId: 域名的ID
        :type PathPrefix: String
        """
        self.HostHeaderId = None

    def _deserialize(self, params):
        if params.get("HostHeaderId"):
            self.HostHeaderId = params.get("HostHeaderId")


class DescribeHostHeadersRequest(AbstractModel):
    """DescribeHostHeaders请求参数结构体
    """

    def __init__(self):
        r"""获取经典型负载均衡域名列表
        :param HostHeaderId: 多个域名的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.HostHeaderId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("HostHeaderId"):
            self.HostHeaderId = params.get("HostHeaderId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体
    """

    def __init__(self):
        r"""删除经典型负载均衡规则
        :param RuleId: 规则的ID
        :type PathPrefix: String
        """
        self.RuleId = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体
    """

    def __init__(self):
        r"""获取经典型负载均衡规则列表
        :param RuleId: 多个规则的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.RuleId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateBackendServerGroupRequest(AbstractModel):
    """CreateBackendServerGroup请求参数结构体
    """

    def __init__(self):
        r"""创建后端服务组
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param BackendServerGroupName: 后端服务组的名称
        :type PathPrefix: String
        :param BackendServerGroupType: 后端服务组类型(Server: 服务器|Mirror: 镜像服务器)
        :type PathPrefix: String
        :param HostName: HTTP类型健康检查的域名
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)
        :type PathPrefix: String
        :param HealthyThreshold: 健康阈值，此参数镜像服务器不可为空
        :type PathPrefix: Int
        :param Interval: 健康检查时间间隔，此参数镜像服务器不可为空
        :type PathPrefix: Int
        :param Timeout: 健康检查超时时间，此参数镜像服务器不可为空
        :type PathPrefix: Int
        :param UnhealthyThreshold: 不健康阈值，此参数镜像服务器不可为空
        :type PathPrefix: Int
        :param UrlPath: HTTP类型监听器健康检查的链接
        :type PathPrefix: String
        :param Region: Region机房
        :type PathPrefix: String
        :param Type: 类型(Host|DirectConnect)
        :type PathPrefix: String
        """
        self.VpcId = None
        self.BackendServerGroupName = None
        self.BackendServerGroupType = None
        self.HostName = None
        self.HealthCheckState = None
        self.HealthyThreshold = None
        self.Interval = None
        self.Timeout = None
        self.UnhealthyThreshold = None
        self.UrlPath = None
        self.Region = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("BackendServerGroupName"):
            self.BackendServerGroupName = params.get("BackendServerGroupName")
        if params.get("BackendServerGroupType"):
            self.BackendServerGroupType = params.get("BackendServerGroupType")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("HealthCheckState"):
            self.HealthCheckState = params.get("HealthCheckState")
        if params.get("HealthyThreshold"):
            self.HealthyThreshold = params.get("HealthyThreshold")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("UnhealthyThreshold"):
            self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        if params.get("UrlPath"):
            self.UrlPath = params.get("UrlPath")
        if params.get("Region"):
            self.Region = params.get("Region")
        if params.get("Type"):
            self.Type = params.get("Type")


class DeleteBackendServerGroupRequest(AbstractModel):
    """DeleteBackendServerGroup请求参数结构体
    """

    def __init__(self):
        r"""删除后端服务组
        :param BackendServerGroupId: 后端服务组的ID
        :type PathPrefix: String
        """
        self.BackendServerGroupId = None

    def _deserialize(self, params):
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")


class ModifyBackendServerGroupRequest(AbstractModel):
    """ModifyBackendServerGroup请求参数结构体
    """

    def __init__(self):
        r"""修改后端服务组
        :param BackendServerGroupId: 服务器组的ID
        :type PathPrefix: String
        :param BackendServerGroupName: 服务器组的名称
        :type PathPrefix: String
        """
        self.BackendServerGroupId = None
        self.BackendServerGroupName = None

    def _deserialize(self, params):
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("BackendServerGroupName"):
            self.BackendServerGroupName = params.get("BackendServerGroupName")


class DescribeBackendServerGroupsRequest(AbstractModel):
    """DescribeBackendServerGroups请求参数结构体
    """

    def __init__(self):
        r"""获取后端服务器组列表
        :param BackendServerGroupId: 多个服务器组的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.BackendServerGroupId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class RegisterBackendServerRequest(AbstractModel):
    """RegisterBackendServer请求参数结构体
    """

    def __init__(self):
        r"""注册后端服务
        :param BackendServerGroupId: 所属后端服务组的ID
        :type PathPrefix: String
        :param BackendServerIp: 后端服务的IP
        :type PathPrefix: String
        :param BackendServerPort: 后端服务的端口
        :type PathPrefix: Int
        :param Weight: 实例的权重
        :type PathPrefix: Int
        """
        self.BackendServerGroupId = None
        self.BackendServerIp = None
        self.BackendServerPort = None
        self.Weight = None

    def _deserialize(self, params):
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("BackendServerIp"):
            self.BackendServerIp = params.get("BackendServerIp")
        if params.get("BackendServerPort"):
            self.BackendServerPort = params.get("BackendServerPort")
        if params.get("Weight"):
            self.Weight = params.get("Weight")


class DeregisterBackendServerRequest(AbstractModel):
    """DeregisterBackendServer请求参数结构体
    """

    def __init__(self):
        r"""解除后端服务
        :param RegisterId: 绑定服务器组的注册ID
        :type PathPrefix: String
        """
        self.RegisterId = None

    def _deserialize(self, params):
        if params.get("RegisterId"):
            self.RegisterId = params.get("RegisterId")


class DescribeBackendServersRequest(AbstractModel):
    """DescribeBackendServers请求参数结构体
    """

    def __init__(self):
        r"""获取后端服务器列表
        :param RegisterId: 多个绑定服务器组的注册ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.RegisterId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("RegisterId"):
            self.RegisterId = params.get("RegisterId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateLoadBalancerAclRequest(AbstractModel):
    """CreateLoadBalancerAcl请求参数结构体
    """

    def __init__(self):
        r"""创建负载均衡ACL
        :param LoadBalancerAclName: LoadBalancerAcl的名称
        :type PathPrefix: String
        :param IpVersion: Ip版本(ipv6|ipv4)
        :type PathPrefix: String
        """
        self.LoadBalancerAclName = None
        self.IpVersion = None

    def _deserialize(self, params):
        if params.get("LoadBalancerAclName"):
            self.LoadBalancerAclName = params.get("LoadBalancerAclName")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")


class DeleteLoadBalancerAclRequest(AbstractModel):
    """DeleteLoadBalancerAcl请求参数结构体
    """

    def __init__(self):
        r"""删除负载均衡ACL
        :param LoadBalancerAclId: LoadBalancerAcl的ID
        :type PathPrefix: String
        """
        self.LoadBalancerAclId = None

    def _deserialize(self, params):
        if params.get("LoadBalancerAclId"):
            self.LoadBalancerAclId = params.get("LoadBalancerAclId")


class ModifyLoadBalancerAclRequest(AbstractModel):
    """ModifyLoadBalancerAcl请求参数结构体
    """

    def __init__(self):
        r"""修改负载均衡ACL名称
        :param LoadBalancerAclId: LoadBalancerAcl的ID
        :type PathPrefix: String
        :param LoadBalancerAclName: LoadBalancerAcl的名称
        :type PathPrefix: String
        """
        self.LoadBalancerAclId = None
        self.LoadBalancerAclName = None

    def _deserialize(self, params):
        if params.get("LoadBalancerAclId"):
            self.LoadBalancerAclId = params.get("LoadBalancerAclId")
        if params.get("LoadBalancerAclName"):
            self.LoadBalancerAclName = params.get("LoadBalancerAclName")


class CreateLoadBalancerAclEntryRequest(AbstractModel):
    """CreateLoadBalancerAclEntry请求参数结构体
    """

    def __init__(self):
        r"""创建负载均衡ACL规则
        :param LoadBalancerAclId: ACL的ID
        :type PathPrefix: String
        :param CidrBlock: LoadBalancerAcl规则的网段
        :type PathPrefix: String
        :param RuleNumber: LoadBalancerAcl规则优先级，1-32766，数字越小优先级越高，不可重复
        :type PathPrefix: Int
        :param RuleAction: LoadBalancerAcl规则行为，接受(allow)，拒绝(deny)
        :type PathPrefix: String
        :param Protocol: 协议，IP代表所有协议(ip)
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        """
        self.LoadBalancerAclId = None
        self.CidrBlock = None
        self.RuleNumber = None
        self.RuleAction = None
        self.Protocol = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("LoadBalancerAclId"):
            self.LoadBalancerAclId = params.get("LoadBalancerAclId")
        if params.get("CidrBlock"):
            self.CidrBlock = params.get("CidrBlock")
        if params.get("RuleNumber"):
            self.RuleNumber = params.get("RuleNumber")
        if params.get("RuleAction"):
            self.RuleAction = params.get("RuleAction")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteLoadBalancerAclEntryRequest(AbstractModel):
    """DeleteLoadBalancerAclEntry请求参数结构体
    """

    def __init__(self):
        r"""删除负载均衡ACL规则
        :param LoadBalancerAclEntryId: ACL规则ID
        :type PathPrefix: String
        """
        self.LoadBalancerAclEntryId = None

    def _deserialize(self, params):
        if params.get("LoadBalancerAclEntryId"):
            self.LoadBalancerAclEntryId = params.get("LoadBalancerAclEntryId")


class AssociateLoadBalancerAclRequest(AbstractModel):
    """AssociateLoadBalancerAcl请求参数结构体
    """

    def __init__(self):
        r"""关联负载均衡ACL
        :param LoadBalancerAclId: LoadBalancerAcl的ID
        :type PathPrefix: String
        :param ListenerId: 监听器的ID
        :type PathPrefix: String
        """
        self.LoadBalancerAclId = None
        self.ListenerId = None

    def _deserialize(self, params):
        if params.get("LoadBalancerAclId"):
            self.LoadBalancerAclId = params.get("LoadBalancerAclId")
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")


class DisassociateLoadBalancerAclRequest(AbstractModel):
    """DisassociateLoadBalancerAcl请求参数结构体
    """

    def __init__(self):
        r"""解除关联负载均衡ACL
        :param ListenerId: 监听器的ID
        :type PathPrefix: String
        """
        self.ListenerId = None

    def _deserialize(self, params):
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")


class DescribeLoadBalancerAclsRequest(AbstractModel):
    """DescribeLoadBalancerAcls请求参数结构体
    """

    def __init__(self):
        r"""查询负载均衡ACL
        :param LoadBalancerAclId: 多个LoadBalancerAcl的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.LoadBalancerAclId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("LoadBalancerAclId"):
            self.LoadBalancerAclId = params.get("LoadBalancerAclId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateSlbRuleRequest(AbstractModel):
    """CreateSlbRule请求参数结构体
    """

    def __init__(self):
        r"""创建域名规则
        :param Path: Url路径
        :type PathPrefix: String
        :param HostHeaderId: 域名的ID
        :type PathPrefix: String
        :param BackendServerGroupId: 后端服务器组的ID
        :type PathPrefix: String
        :param ListenerSync: 是否同步监听器的健康检查、会话保持和转发算法
        :type PathPrefix: String
        :param Method: 监听器的转发方式(RoundRobin|LeastConnections|MasterSlave|QUIC_CID|IPHash)
        :type PathPrefix: String
        :param SessionState: 会话保持的状态，在ListenerSync为off时有效
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param cookieType: 会话类型(ImplantCookie|RewriteCookie)
        :type PathPrefix: String
        :param CookieName: cookie名字
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)，在ListenerSync为off时有效
        :type PathPrefix: String
        :param HealthyThreshold: 健康阈值
        :type PathPrefix: String
        :param Interval: 健康检查时间间隔
        :type PathPrefix: Int
        :param Timeout: 健康检查超时时间
        :type PathPrefix: Int
        :param UnhealthyThreshold: 不健康阈值
        :type PathPrefix: Int
        :param UrlPath: HTTP类型监听器健康检查的链接
        :type PathPrefix: String
        :param HostName: HTTP类型健康检查的域名
        :type PathPrefix: String
        """
        self.Path = None
        self.HostHeaderId = None
        self.BackendServerGroupId = None
        self.ListenerSync = None
        self.Method = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.cookieType = None
        self.CookieName = None
        self.HealthCheckState = None
        self.HealthyThreshold = None
        self.Interval = None
        self.Timeout = None
        self.UnhealthyThreshold = None
        self.UrlPath = None
        self.HostName = None

    def _deserialize(self, params):
        if params.get("Path"):
            self.Path = params.get("Path")
        if params.get("HostHeaderId"):
            self.HostHeaderId = params.get("HostHeaderId")
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("ListenerSync"):
            self.ListenerSync = params.get("ListenerSync")
        if params.get("Method"):
            self.Method = params.get("Method")
        if params.get("SessionState"):
            self.SessionState = params.get("SessionState")
        if params.get("SessionPersistencePeriod"):
            self.SessionPersistencePeriod = params.get("SessionPersistencePeriod")
        if params.get("cookieType"):
            self.cookieType = params.get("cookieType")
        if params.get("CookieName"):
            self.CookieName = params.get("CookieName")
        if params.get("HealthCheckState"):
            self.HealthCheckState = params.get("HealthCheckState")
        if params.get("HealthyThreshold"):
            self.HealthyThreshold = params.get("HealthyThreshold")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("UnhealthyThreshold"):
            self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        if params.get("UrlPath"):
            self.UrlPath = params.get("UrlPath")
        if params.get("HostName"):
            self.HostName = params.get("HostName")


class ModifySlbRuleRequest(AbstractModel):
    """ModifySlbRule请求参数结构体
    """

    def __init__(self):
        r"""修改域名规则
        :param Path: Url路径
        :type PathPrefix: String
        :param RuleId: 规则的ID
        :type PathPrefix: String
        :param BackendServerGroupId: 后端服务器组的ID
        :type PathPrefix: String
        :param ListenerSync: 是否同步监听器的健康检查、会话保持和转发算法
        :type PathPrefix: String
        :param Method: 监听器的转发方式(RoundRobin|LeastConnections|MasterSlave|QUIC_CID|IPHash)
        :type PathPrefix: String
        :param SessionState: 会话保持的状态，在ListenerSync为off时有效
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param cookieType: 会话类型(ImplantCookie|RewriteCookie)
        :type PathPrefix: String
        :param CookieName: cookie名字
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)，在ListenerSync为off时有效
        :type PathPrefix: String
        :param HealthyThreshold: 健康阈值
        :type PathPrefix: String
        :param Interval: 健康检查时间间隔
        :type PathPrefix: Int
        :param Timeout: 健康检查超时时间
        :type PathPrefix: Int
        :param UnhealthyThreshold: 不健康阈值
        :type PathPrefix: Int
        :param UrlPath: HTTP类型监听器健康检查的链接
        :type PathPrefix: String
        :param HostName: HTTP类型健康检查的域名
        :type PathPrefix: String
        """
        self.Path = None
        self.RuleId = None
        self.BackendServerGroupId = None
        self.ListenerSync = None
        self.Method = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.cookieType = None
        self.CookieName = None
        self.HealthCheckState = None
        self.HealthyThreshold = None
        self.Interval = None
        self.Timeout = None
        self.UnhealthyThreshold = None
        self.UrlPath = None
        self.HostName = None

    def _deserialize(self, params):
        if params.get("Path"):
            self.Path = params.get("Path")
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("ListenerSync"):
            self.ListenerSync = params.get("ListenerSync")
        if params.get("Method"):
            self.Method = params.get("Method")
        if params.get("SessionState"):
            self.SessionState = params.get("SessionState")
        if params.get("SessionPersistencePeriod"):
            self.SessionPersistencePeriod = params.get("SessionPersistencePeriod")
        if params.get("cookieType"):
            self.cookieType = params.get("cookieType")
        if params.get("CookieName"):
            self.CookieName = params.get("CookieName")
        if params.get("HealthCheckState"):
            self.HealthCheckState = params.get("HealthCheckState")
        if params.get("HealthyThreshold"):
            self.HealthyThreshold = params.get("HealthyThreshold")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("UnhealthyThreshold"):
            self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        if params.get("UrlPath"):
            self.UrlPath = params.get("UrlPath")
        if params.get("HostName"):
            self.HostName = params.get("HostName")


class CreatePrivateLinkServerRequest(AbstractModel):
    """CreatePrivateLinkServer请求参数结构体
    """

    def __init__(self):
        r"""发布PrivateLink服务
        :param PrivateLinkServerName: privateLink名称
        :type PathPrefix: String
        :param ListenerId: 关联监听器ID
        :type PathPrefix: String
        :param Description: PrivateLinkServer的描述
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        """
        self.PrivateLinkServerName = None
        self.ListenerId = None
        self.Description = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("PrivateLinkServerName"):
            self.PrivateLinkServerName = params.get("PrivateLinkServerName")
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribePrivateLinkServerRequest(AbstractModel):
    """DescribePrivateLinkServer请求参数结构体
    """

    def __init__(self):
        r"""查看PrivateLink服务
        :param PrivateLinkServerId: PrivateLinkServer的ID
        :type PathPrefix: Filter
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.PrivateLinkServerId = None
        self.ProjectId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("PrivateLinkServerId"):
            self.PrivateLinkServerId = params.get("PrivateLinkServerId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeletePrivateLinkServerRequest(AbstractModel):
    """DeletePrivateLinkServer请求参数结构体
    """

    def __init__(self):
        r"""删除PrivateLink服务
        :param PrivateLinkServerId: PrivateLinkServer的ID
        :type PathPrefix: String
        """
        self.PrivateLinkServerId = None

    def _deserialize(self, params):
        if params.get("PrivateLinkServerId"):
            self.PrivateLinkServerId = params.get("PrivateLinkServerId")


class ModifyPrivateLinkServerRequest(AbstractModel):
    """ModifyPrivateLinkServer请求参数结构体
    """

    def __init__(self):
        r"""更新PrivateLink服务
        :param PrivateLinkServerId: PrivateLinkServer的ID
        :type PathPrefix: String
        :param PrivateLinkServerName: PrivateLinkServer名称
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        """
        self.PrivateLinkServerId = None
        self.PrivateLinkServerName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("PrivateLinkServerId"):
            self.PrivateLinkServerId = params.get("PrivateLinkServerId")
        if params.get("PrivateLinkServerName"):
            self.PrivateLinkServerName = params.get("PrivateLinkServerName")
        if params.get("Description"):
            self.Description = params.get("Description")


class AssociatePrivateLinkServerRequest(AbstractModel):
    """AssociatePrivateLinkServer请求参数结构体
    """

    def __init__(self):
        r"""申请连接PrivateLink服务
        :param PrivateLinkServerId: PrivateLinkServer的ID
        :type PathPrefix: String
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param ListenerPort: 监听器的协议端口
        :type PathPrefix: Int
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        """
        self.PrivateLinkServerId = None
        self.LoadBalancerId = None
        self.ListenerPort = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("PrivateLinkServerId"):
            self.PrivateLinkServerId = params.get("PrivateLinkServerId")
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerPort"):
            self.ListenerPort = params.get("ListenerPort")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribePrivateLinkRequest(AbstractModel):
    """DescribePrivateLink请求参数结构体
    """

    def __init__(self):
        r"""查询PrivateLink
        :param PrivateLinkId: PrivateLinkId的ID
        :type PathPrefix: Filter
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.PrivateLinkId = None
        self.ProjectId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("PrivateLinkId"):
            self.PrivateLinkId = params.get("PrivateLinkId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeletePrivateLinkRequest(AbstractModel):
    """DeletePrivateLink请求参数结构体
    """

    def __init__(self):
        r"""删除已建立的PrivateLink
        :param PrivateLinkId: PrivateLink的ID
        :type PathPrefix: String
        """
        self.PrivateLinkId = None

    def _deserialize(self, params):
        if params.get("PrivateLinkId"):
            self.PrivateLinkId = params.get("PrivateLinkId")


class ModifyLoadBalancerAclEntryRequest(AbstractModel):
    """ModifyLoadBalancerAclEntry请求参数结构体
    """

    def __init__(self):
        r"""修改负载均衡ACL规则
        :param LoadBalancerAclEntryId: ACL规则ID
        :type PathPrefix: String
        :param RuleNumber: LoadBalancerAcl规则优先级，1-32766，数字越小优先级越高
        :type PathPrefix: Int
        :param RuleAction: LoadBalancerAcl规则行为，接受(allow)，拒绝(deny)
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        """
        self.LoadBalancerAclEntryId = None
        self.RuleNumber = None
        self.RuleAction = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("LoadBalancerAclEntryId"):
            self.LoadBalancerAclEntryId = params.get("LoadBalancerAclEntryId")
        if params.get("RuleNumber"):
            self.RuleNumber = params.get("RuleNumber")
        if params.get("RuleAction"):
            self.RuleAction = params.get("RuleAction")
        if params.get("Description"):
            self.Description = params.get("Description")


class AcceptPrivateLinkRequest(AbstractModel):
    """AcceptPrivateLink请求参数结构体
    """

    def __init__(self):
        r"""同意PrivateLink申请
        :param PrivateLinkId: PrivateLink的ID
        :type PathPrefix: String
        """
        self.PrivateLinkId = None

    def _deserialize(self, params):
        if params.get("PrivateLinkId"):
            self.PrivateLinkId = params.get("PrivateLinkId")


class RejectPrivateLinkRequest(AbstractModel):
    """RejectPrivateLink请求参数结构体
    """

    def __init__(self):
        r"""RejectPrivateLink
        :param PrivateLinkId: PrivateLink的ID
        :type PathPrefix: String
        """
        self.PrivateLinkId = None

    def _deserialize(self, params):
        if params.get("PrivateLinkId"):
            self.PrivateLinkId = params.get("PrivateLinkId")


class ListPrivateLinkServerRequest(AbstractModel):
    """ListPrivateLinkServer请求参数结构体
    """

    def __init__(self):
        r"""查询已建立连接的privatelink列表
        :param PrivateLinkServerId: PrivateLinkServer的ID
        :type PathPrefix: String
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        """
        self.PrivateLinkServerId = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("PrivateLinkServerId"):
            self.PrivateLinkServerId = params.get("PrivateLinkServerId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class RemovePrivateLinkRequest(AbstractModel):
    """RemovePrivateLink请求参数结构体
    """

    def __init__(self):
        r"""RemovePrivateLink
        :param PrivateLinkServerId: PrivateLinkServer的ID
        :type PathPrefix: String
        :param PrivateLinkId: PrivateLink的ID
        :type PathPrefix: String
        """
        self.PrivateLinkServerId = None
        self.PrivateLinkId = None

    def _deserialize(self, params):
        if params.get("PrivateLinkServerId"):
            self.PrivateLinkServerId = params.get("PrivateLinkServerId")
        if params.get("PrivateLinkId"):
            self.PrivateLinkId = params.get("PrivateLinkId")


class CreateAlbRequest(AbstractModel):
    """CreateAlb请求参数结构体
    """

    def __init__(self):
        r"""CreateAlb
        :param AlbName: 应用型负载均衡的名称
        :type PathPrefix: String
        :param AlbVersion: 应用型负载均衡支持的版本
        :type PathPrefix: String
        :param AlbType: 应用型负载均衡的类型，public 为公网负载均衡，internal 为内网负载均衡
        :type PathPrefix: String
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param IpVersion: 负载均衡的IP版本
ipv4 
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param AllocationId: 弹性IP的ID
        :type PathPrefix: String
        :param ChargeType: 计费类型(PrePaidByHourUsage，按小时用量实时付费（小时结))
        :type PathPrefix: String
        """
        self.AlbName = None
        self.AlbVersion = None
        self.AlbType = None
        self.VpcId = None
        self.IpVersion = None
        self.ProjectId = None
        self.AllocationId = None
        self.ChargeType = None

    def _deserialize(self, params):
        if params.get("AlbName"):
            self.AlbName = params.get("AlbName")
        if params.get("AlbVersion"):
            self.AlbVersion = params.get("AlbVersion")
        if params.get("AlbType"):
            self.AlbType = params.get("AlbType")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")


class DeleteAlbRequest(AbstractModel):
    """DeleteAlb请求参数结构体
    """

    def __init__(self):
        r"""DeleteAlb
        :param AlbId: 应用型负载均衡的ID
        :type PathPrefix: String
        """
        self.AlbId = None

    def _deserialize(self, params):
        if params.get("AlbId"):
            self.AlbId = params.get("AlbId")


class SetAlbNameRequest(AbstractModel):
    """SetAlbName请求参数结构体
    """

    def __init__(self):
        r"""SetAlbName
        :param AlbId: 应用型负载均衡的ID
        :type PathPrefix: String
        :param AlbName: 应用型负载均衡的名称
        :type PathPrefix: String
        """
        self.AlbId = None
        self.AlbName = None

    def _deserialize(self, params):
        if params.get("AlbId"):
            self.AlbId = params.get("AlbId")
        if params.get("AlbName"):
            self.AlbName = params.get("AlbName")


class SetAlbStatusRequest(AbstractModel):
    """SetAlbStatus请求参数结构体
    """

    def __init__(self):
        r"""SetAlbStatus
        :param AlbId: 应用型负载均衡的ID
        :type PathPrefix: String
        :param State: 应用型负载均衡的开启状态(start|stop)
        :type PathPrefix: String
        """
        self.AlbId = None
        self.State = None

    def _deserialize(self, params):
        if params.get("AlbId"):
            self.AlbId = params.get("AlbId")
        if params.get("State"):
            self.State = params.get("State")


class DescribeAlbsRequest(AbstractModel):
    """DescribeAlbs请求参数结构体
    """

    def __init__(self):
        r"""DescribeAlbs
        :param AlbId: 多个应用型负载均衡的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.AlbId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("AlbId"):
            self.AlbId = params.get("AlbId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateAlbListenerRequest(AbstractModel):
    """CreateAlbListener请求参数结构体
    """

    def __init__(self):
        r"""CreateAlbListener
        :param AlbId: 应用型负载均衡的ID
        :type PathPrefix: String
        :param AlbListenerName: 应用型负载均衡监听器的名称
        :type PathPrefix: String
        :param Method: 监听器的转发方式(RoundRobin|LeastConnections)
        :type PathPrefix: String
        :param Protocol: 监听器的协议(HTTP|HTTPS)
        :type PathPrefix: String
        :param Port: 监听器的协议端口
        :type PathPrefix: Int
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        :param TlsCipherPolicy: TLS安全策略
        :type PathPrefix: String
        :param AlbListenerAclId: LoadBalancerAcl的ID
        :type PathPrefix: String
        :param AlbListenerState: 应用型监听器的状态(start|stop)
        :type PathPrefix: String
        :param SessionState: 会话保持的状态(start|stop)
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param CookieType: 会话类型
        :type PathPrefix: String
        :param CookieName: Cookie的名称
        :type PathPrefix: String
        :param EnableHttp2: 是否启用HTTP/2
        :type PathPrefix: Boolean
        :param HttpProtocol: 后端协议版本(HTTP1.0|HTTP1.1)
        :type PathPrefix: String
        """
        self.AlbId = None
        self.AlbListenerName = None
        self.Method = None
        self.Protocol = None
        self.Port = None
        self.CertificateId = None
        self.TlsCipherPolicy = None
        self.AlbListenerAclId = None
        self.AlbListenerState = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.CookieType = None
        self.CookieName = None
        self.EnableHttp2 = None
        self.HttpProtocol = None

    def _deserialize(self, params):
        if params.get("AlbId"):
            self.AlbId = params.get("AlbId")
        if params.get("AlbListenerName"):
            self.AlbListenerName = params.get("AlbListenerName")
        if params.get("Method"):
            self.Method = params.get("Method")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("Port"):
            self.Port = params.get("Port")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("TlsCipherPolicy"):
            self.TlsCipherPolicy = params.get("TlsCipherPolicy")
        if params.get("AlbListenerAclId"):
            self.AlbListenerAclId = params.get("AlbListenerAclId")
        if params.get("AlbListenerState"):
            self.AlbListenerState = params.get("AlbListenerState")
        if params.get("SessionState"):
            self.SessionState = params.get("SessionState")
        if params.get("SessionPersistencePeriod"):
            self.SessionPersistencePeriod = params.get("SessionPersistencePeriod")
        if params.get("CookieType"):
            self.CookieType = params.get("CookieType")
        if params.get("CookieName"):
            self.CookieName = params.get("CookieName")
        if params.get("EnableHttp2"):
            self.EnableHttp2 = params.get("EnableHttp2")
        if params.get("HttpProtocol"):
            self.HttpProtocol = params.get("HttpProtocol")


class ModifyAlbListenerRequest(AbstractModel):
    """ModifyAlbListener请求参数结构体
    """

    def __init__(self):
        r"""ModifyAlbListener
        :param AlbListenerId: 应用型监听器的ID
        :type PathPrefix: String
        :param AlbListenerName: 应用型负载均衡监听器的名称
        :type PathPrefix: String
        :param AlbListenerState: 应用型监听器的状态
        :type PathPrefix: String
        :param Method: 监听器的转发方式(RoundRobin|LeastConnections)
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        :param TlsCipherPolicy: TLS安全策略
        :type PathPrefix: String
        :param AlbListenerAclId: LoadBalancerAcl的ID
        :type PathPrefix: String
        :param HttpProtocol: 后端协议版本(HTTP1.0|HTTP1.1)
        :type PathPrefix: String
        :param SessionState: 会话保持的状态
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param CookieType: 会话类型
        :type PathPrefix: String
        :param CookieName: Cookie的名称
        :type PathPrefix: String
        :param EnableHttp2: 是否启用HTTP/2
        :type PathPrefix: Boolean
        """
        self.AlbListenerId = None
        self.AlbListenerName = None
        self.AlbListenerState = None
        self.Method = None
        self.CertificateId = None
        self.TlsCipherPolicy = None
        self.AlbListenerAclId = None
        self.HttpProtocol = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.CookieType = None
        self.CookieName = None
        self.EnableHttp2 = None

    def _deserialize(self, params):
        if params.get("AlbListenerId"):
            self.AlbListenerId = params.get("AlbListenerId")
        if params.get("AlbListenerName"):
            self.AlbListenerName = params.get("AlbListenerName")
        if params.get("AlbListenerState"):
            self.AlbListenerState = params.get("AlbListenerState")
        if params.get("Method"):
            self.Method = params.get("Method")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("TlsCipherPolicy"):
            self.TlsCipherPolicy = params.get("TlsCipherPolicy")
        if params.get("AlbListenerAclId"):
            self.AlbListenerAclId = params.get("AlbListenerAclId")
        if params.get("HttpProtocol"):
            self.HttpProtocol = params.get("HttpProtocol")
        if params.get("SessionState"):
            self.SessionState = params.get("SessionState")
        if params.get("SessionPersistencePeriod"):
            self.SessionPersistencePeriod = params.get("SessionPersistencePeriod")
        if params.get("CookieType"):
            self.CookieType = params.get("CookieType")
        if params.get("CookieName"):
            self.CookieName = params.get("CookieName")
        if params.get("EnableHttp2"):
            self.EnableHttp2 = params.get("EnableHttp2")


class DeleteAlbListenerRequest(AbstractModel):
    """DeleteAlbListener请求参数结构体
    """

    def __init__(self):
        r"""DeleteAlbListener
        :param AlbListenerId: 应用型监听器的ID
        :type PathPrefix: String
        """
        self.AlbListenerId = None

    def _deserialize(self, params):
        if params.get("AlbListenerId"):
            self.AlbListenerId = params.get("AlbListenerId")


class DescribeAlbListenersRequest(AbstractModel):
    """DescribeAlbListeners请求参数结构体
    """

    def __init__(self):
        r"""DescribeAlbListeners
        :param AlbListenerId: 多个应用型监听器的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.AlbListenerId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("AlbListenerId"):
            self.AlbListenerId = params.get("AlbListenerId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateAlbRuleGroupRequest(AbstractModel):
    """CreateAlbRuleGroup请求参数结构体
    """

    def __init__(self):
        r"""CreateAlbRuleGroup
        :param AlbRuleGroupName: 转发策略的名称
        :type PathPrefix: String
        :param AlbListenerId: 应用型负载均衡监听器的ID
        :type PathPrefix: String
        :param BackendServerGroupId: 后端服务器组的ID
        :type PathPrefix: String
        :param ListenerSync: 是否同步监听器的健康检查、会话保持和转发算法(on|off)
        :type PathPrefix: String
        :param Method: 监听器的转发方式(RoundRobin|LeastConnections)
        :type PathPrefix: String
        :param SessionState: 会话保持的状态，在ListenerSync为off时有效
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param CookieType: 会话类型(ImplantCookie|RewriteCookie)
        :type PathPrefix: String
        :param CookieName: Cookie的名称
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)，在ListenerSync为off时有效
        :type PathPrefix: String
        :param Timeout: 健康检查超时时间
        :type PathPrefix: Int
        :param Interval: 健康检查时间间隔
        :type PathPrefix: Int
        :param HealthyThreshold: 健康阈值
        :type PathPrefix: Int
        :param UnhealthyThreshold: 不健康阈值
        :type PathPrefix: Int
        :param UrlPath: HTTP类型监听器健康检查的链接
        :type PathPrefix: String
        :param HostName: HTTP类型健康检查的域名
        :type PathPrefix: String
        :param AlbRuleSet: 规则的信息
        :type PathPrefix: Array
        :param RedirectHttpCode: 重定向状态码
301|302|307
        :type PathPrefix: String
        :param RedirectAlbListenerId: 重定向的监听器ID
        :type PathPrefix: String
        """
        self.AlbRuleGroupName = None
        self.AlbListenerId = None
        self.BackendServerGroupId = None
        self.ListenerSync = None
        self.Method = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.CookieType = None
        self.CookieName = None
        self.HealthCheckState = None
        self.Timeout = None
        self.Interval = None
        self.HealthyThreshold = None
        self.UnhealthyThreshold = None
        self.UrlPath = None
        self.HostName = None
        self.AlbRuleSet = None
        self.RedirectHttpCode = None
        self.RedirectAlbListenerId = None

    def _deserialize(self, params):
        if params.get("AlbRuleGroupName"):
            self.AlbRuleGroupName = params.get("AlbRuleGroupName")
        if params.get("AlbListenerId"):
            self.AlbListenerId = params.get("AlbListenerId")
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("ListenerSync"):
            self.ListenerSync = params.get("ListenerSync")
        if params.get("Method"):
            self.Method = params.get("Method")
        if params.get("SessionState"):
            self.SessionState = params.get("SessionState")
        if params.get("SessionPersistencePeriod"):
            self.SessionPersistencePeriod = params.get("SessionPersistencePeriod")
        if params.get("CookieType"):
            self.CookieType = params.get("CookieType")
        if params.get("CookieName"):
            self.CookieName = params.get("CookieName")
        if params.get("HealthCheckState"):
            self.HealthCheckState = params.get("HealthCheckState")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("HealthyThreshold"):
            self.HealthyThreshold = params.get("HealthyThreshold")
        if params.get("UnhealthyThreshold"):
            self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        if params.get("UrlPath"):
            self.UrlPath = params.get("UrlPath")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("AlbRuleSet"):
            self.AlbRuleSet = params.get("AlbRuleSet")
        if params.get("RedirectHttpCode"):
            self.RedirectHttpCode = params.get("RedirectHttpCode")
        if params.get("RedirectAlbListenerId"):
            self.RedirectAlbListenerId = params.get("RedirectAlbListenerId")


class DeleteAlbRuleGroupRequest(AbstractModel):
    """DeleteAlbRuleGroup请求参数结构体
    """

    def __init__(self):
        r"""DeleteAlbRuleGroup
        :param AlbRuleGroupId: 转发策略的ID
        :type PathPrefix: String
        """
        self.AlbRuleGroupId = None

    def _deserialize(self, params):
        if params.get("AlbRuleGroupId"):
            self.AlbRuleGroupId = params.get("AlbRuleGroupId")


class DescribeAlbRuleGroupsRequest(AbstractModel):
    """DescribeAlbRuleGroups请求参数结构体
    """

    def __init__(self):
        r"""DescribeAlbRuleGroups
        :param AlbRuleGroupId: 多个转发策略的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.AlbRuleGroupId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("AlbRuleGroupId"):
            self.AlbRuleGroupId = params.get("AlbRuleGroupId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ModifyAlbRuleGroupRequest(AbstractModel):
    """ModifyAlbRuleGroup请求参数结构体
    """

    def __init__(self):
        r"""ModifyAlbRuleGroup
        :param AlbRuleGroupId: 转发策略的ID
        :type PathPrefix: String
        :param AlbRuleGroupName: 转发策略的名称
        :type PathPrefix: String
        :param BackendServerGroupId: 后端服务器组的ID
        :type PathPrefix: String
        :param ListenerSync: 是否同步监听器的健康检查、会话保持和转发算法(on | off)
        :type PathPrefix: String
        :param Method: 监听器的转发方式(RoundRobin|LeastConnections)
        :type PathPrefix: String
        :param SessionState: 会话保持的状态，在ListenerSync为off时有效
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param CookieType: 会话类型(ImplantCookie|RewriteCookie)
        :type PathPrefix: String
        :param CookieName: Cookie的名称
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)，在ListenerSync为off时有效
        :type PathPrefix: String
        :param Timeout: 健康检查超时时间
        :type PathPrefix: Int
        :param Interval: 健康检查时间间隔
        :type PathPrefix: Int
        :param HealthyThreshold: 健康阈值
        :type PathPrefix: Int
        :param UnhealthyThreshold: 不健康阈值
        :type PathPrefix: Int
        :param UrlPath: HTTP类型监听器健康检查的链接
        :type PathPrefix: String
        :param HostName: HTTP类型健康检查的域名
        :type PathPrefix: String
        :param AlbRuleSet: 规则的信息
        :type PathPrefix: Array
        :param RedirectHttpCode: 重定向状态码
        :type PathPrefix: String
        :param RedirectAlbListenerId: 重定向的监听器ID
        :type PathPrefix: String
        """
        self.AlbRuleGroupId = None
        self.AlbRuleGroupName = None
        self.BackendServerGroupId = None
        self.ListenerSync = None
        self.Method = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.CookieType = None
        self.CookieName = None
        self.HealthCheckState = None
        self.Timeout = None
        self.Interval = None
        self.HealthyThreshold = None
        self.UnhealthyThreshold = None
        self.UrlPath = None
        self.HostName = None
        self.AlbRuleSet = None
        self.RedirectHttpCode = None
        self.RedirectAlbListenerId = None

    def _deserialize(self, params):
        if params.get("AlbRuleGroupId"):
            self.AlbRuleGroupId = params.get("AlbRuleGroupId")
        if params.get("AlbRuleGroupName"):
            self.AlbRuleGroupName = params.get("AlbRuleGroupName")
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("ListenerSync"):
            self.ListenerSync = params.get("ListenerSync")
        if params.get("Method"):
            self.Method = params.get("Method")
        if params.get("SessionState"):
            self.SessionState = params.get("SessionState")
        if params.get("SessionPersistencePeriod"):
            self.SessionPersistencePeriod = params.get("SessionPersistencePeriod")
        if params.get("CookieType"):
            self.CookieType = params.get("CookieType")
        if params.get("CookieName"):
            self.CookieName = params.get("CookieName")
        if params.get("HealthCheckState"):
            self.HealthCheckState = params.get("HealthCheckState")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("HealthyThreshold"):
            self.HealthyThreshold = params.get("HealthyThreshold")
        if params.get("UnhealthyThreshold"):
            self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        if params.get("UrlPath"):
            self.UrlPath = params.get("UrlPath")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("AlbRuleSet"):
            self.AlbRuleSet = params.get("AlbRuleSet")
        if params.get("RedirectHttpCode"):
            self.RedirectHttpCode = params.get("RedirectHttpCode")
        if params.get("RedirectAlbListenerId"):
            self.RedirectAlbListenerId = params.get("RedirectAlbListenerId")


class AddAlbRuleRequest(AbstractModel):
    """AddAlbRule请求参数结构体
    """

    def __init__(self):
        r"""AddAlbRule
        :param AlbRuleGroupId: 转发策略的ID
        :type PathPrefix: String
        :param AlbRuleType: 匹配规则类型(domain|url)
        :type PathPrefix: String
        :param AlbRuleValue: 匹配规则的值
        :type PathPrefix: String
        """
        self.AlbRuleGroupId = None
        self.AlbRuleType = None
        self.AlbRuleValue = None

    def _deserialize(self, params):
        if params.get("AlbRuleGroupId"):
            self.AlbRuleGroupId = params.get("AlbRuleGroupId")
        if params.get("AlbRuleType"):
            self.AlbRuleType = params.get("AlbRuleType")
        if params.get("AlbRuleValue"):
            self.AlbRuleValue = params.get("AlbRuleValue")


class DeleteAlbRuleRequest(AbstractModel):
    """DeleteAlbRule请求参数结构体
    """

    def __init__(self):
        r"""DeleteAlbRule
        :param AlbRuleGroupId: 转发策略的ID
        :type PathPrefix: String
        :param AlbRuleType: 匹配规则类型(domain|url)
        :type PathPrefix: String
        :param AlbRuleValue: 匹配规则的值
        :type PathPrefix: String
        """
        self.AlbRuleGroupId = None
        self.AlbRuleType = None
        self.AlbRuleValue = None

    def _deserialize(self, params):
        if params.get("AlbRuleGroupId"):
            self.AlbRuleGroupId = params.get("AlbRuleGroupId")
        if params.get("AlbRuleType"):
            self.AlbRuleType = params.get("AlbRuleType")
        if params.get("AlbRuleValue"):
            self.AlbRuleValue = params.get("AlbRuleValue")


class CreateAlbListenerCertGroupRequest(AbstractModel):
    """CreateAlbListenerCertGroup请求参数结构体
    """

    def __init__(self):
        r"""CreateAlbListenerCertGroup
        :param AlbListenerId: 应用型负载均衡监听器的ID
        :type PathPrefix: String
        """
        self.AlbListenerId = None

    def _deserialize(self, params):
        if params.get("AlbListenerId"):
            self.AlbListenerId = params.get("AlbListenerId")


class DeleteAlbListenerCertGroupRequest(AbstractModel):
    """DeleteAlbListenerCertGroup请求参数结构体
    """

    def __init__(self):
        r"""DeleteAlbListenerCertGroup
        :param AlbListenerCertGroupId: 证书组的ID
        :type PathPrefix: String
        """
        self.AlbListenerCertGroupId = None

    def _deserialize(self, params):
        if params.get("AlbListenerCertGroupId"):
            self.AlbListenerCertGroupId = params.get("AlbListenerCertGroupId")


class DescribeAlbListenerCertGroupsRequest(AbstractModel):
    """DescribeAlbListenerCertGroups请求参数结构体
    """

    def __init__(self):
        r"""DescribeAlbListenerCertGroups
        :param AlbListenerCertGroupId: 多个证书组的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.AlbListenerCertGroupId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("AlbListenerCertGroupId"):
            self.AlbListenerCertGroupId = params.get("AlbListenerCertGroupId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class AssociateCertificateWithGroupRequest(AbstractModel):
    """AssociateCertificateWithGroup请求参数结构体
    """

    def __init__(self):
        r"""AssociateCertificateWithGroup
        :param AlbListenerCertGroupId: 证书组的ID
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        """
        self.AlbListenerCertGroupId = None
        self.CertificateId = None

    def _deserialize(self, params):
        if params.get("AlbListenerCertGroupId"):
            self.AlbListenerCertGroupId = params.get("AlbListenerCertGroupId")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")


class DissociateCertificateWithGroupRequest(AbstractModel):
    """DissociateCertificateWithGroup请求参数结构体
    """

    def __init__(self):
        r"""DissociateCertificateWithGroup
        :param AlbListenerCertGroupId: 证书组的ID
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        """
        self.AlbListenerCertGroupId = None
        self.CertificateId = None

    def _deserialize(self, params):
        if params.get("AlbListenerCertGroupId"):
            self.AlbListenerCertGroupId = params.get("AlbListenerCertGroupId")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")


class SetEnableAlbAccessLogRequest(AbstractModel):
    """SetEnableAlbAccessLog请求参数结构体
    """

    def __init__(self):
        r"""SetEnableAlbAccessLog
        :param AlbId: 应用型负载均衡的ID
        :type PathPrefix: String
        :param EnabledLog: 是否开启日志服务
        :type PathPrefix: Boolean
        """
        self.AlbId = None
        self.EnabledLog = None

    def _deserialize(self, params):
        if params.get("AlbId"):
            self.AlbId = params.get("AlbId")
        if params.get("EnabledLog"):
            self.EnabledLog = params.get("EnabledLog")


class SetAlbAccessLogRequest(AbstractModel):
    """SetAlbAccessLog请求参数结构体
    """

    def __init__(self):
        r"""SetAlbAccessLog
        :param AlbId: 应用型负载均衡的ID
        :type PathPrefix: String
        :param ProjectName: 访问日志投递的日志库
        :type PathPrefix: String
        :param LogpoolName: 访问日志投递的日志池
        :type PathPrefix: String
        """
        self.AlbId = None
        self.ProjectName = None
        self.LogpoolName = None

    def _deserialize(self, params):
        if params.get("AlbId"):
            self.AlbId = params.get("AlbId")
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogpoolName"):
            self.LogpoolName = params.get("LogpoolName")


class CloneLoadBalancerRequest(AbstractModel):
    """CloneLoadBalancer请求参数结构体
    """

    def __init__(self):
        r"""克隆负载均衡
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param LoadBalancerName: 负载均衡的名称
        :type PathPrefix: String
        :param Type: 负载均衡的类型，public 为公网负载均衡，internal 为内网负载均衡
        :type PathPrefix: String
        """
        self.VpcId = None
        self.LoadBalancerName = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("LoadBalancerName"):
            self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Type"):
            self.Type = params.get("Type")


