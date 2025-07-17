from ksyun.common.abstract_model import AbstractModel


class DescribeBackendServersRequest(AbstractModel):
    """DescribeBackendServers请求参数结构体
    """

    def __init__(self):
        r"""查询服务器信息
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param BackendServerId: 多个服务器ServerId
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.Filter = None
        self.BackendServerId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("BackendServerId"):
            self.BackendServerId = params.get("BackendServerId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ModifyBackendServerRequest(AbstractModel):
    """ModifyBackendServer请求参数结构体
    """

    def __init__(self):
        r"""修改服务器信息
        :param BackendServerId: 服务器id
        :type PathPrefix: String
        :param Weight: 服务器的权重
        :type PathPrefix: Int
        :param Port: 服务器端口
        :type PathPrefix: Int
        :param MasterSlaveType: 真实服务器的主备状态(Master | Slave)
        :type PathPrefix: String
        """
        self.BackendServerId = None
        self.Weight = None
        self.Port = None
        self.MasterSlaveType = None

    def _deserialize(self, params):
        if params.get("BackendServerId"):
            self.BackendServerId = params.get("BackendServerId")
        if params.get("Weight"):
            self.Weight = params.get("Weight")
        if params.get("Port"):
            self.Port = params.get("Port")
        if params.get("MasterSlaveType"):
            self.MasterSlaveType = params.get("MasterSlaveType")


class DeregisterBackendServerRequest(AbstractModel):
    """DeregisterBackendServer请求参数结构体
    """

    def __init__(self):
        r"""从服务器组移除服务器
        :param BackendServerId: 服务器id
        :type PathPrefix: String
        """
        self.BackendServerId = None

    def _deserialize(self, params):
        if params.get("BackendServerId"):
            self.BackendServerId = params.get("BackendServerId")


class RegisterBackendServerRequest(AbstractModel):
    """RegisterBackendServer请求参数结构体
    """

    def __init__(self):
        r"""注册服务器到服务组
        :param BackendServerGroupId: 服务器组id
        :type PathPrefix: String
        :param BackendServerIp: 服务器ip
        :type PathPrefix: String
        :param Port: 服务器端口
        :type PathPrefix: Int
        :param Weight: 服务器权重
        :type PathPrefix: Int
        :param NetworkInterfaceId: 网卡id
        :type PathPrefix: String
        :param DirectConnectGatewayId: 对等连接id
        :type PathPrefix: String
        :param MasterSlaveType: 真实服务器的主备状态
        :type PathPrefix: String
        """
        self.BackendServerGroupId = None
        self.BackendServerIp = None
        self.Port = None
        self.Weight = None
        self.NetworkInterfaceId = None
        self.DirectConnectGatewayId = None
        self.MasterSlaveType = None

    def _deserialize(self, params):
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("BackendServerIp"):
            self.BackendServerIp = params.get("BackendServerIp")
        if params.get("Port"):
            self.Port = params.get("Port")
        if params.get("Weight"):
            self.Weight = params.get("Weight")
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("DirectConnectGatewayId"):
            self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("MasterSlaveType"):
            self.MasterSlaveType = params.get("MasterSlaveType")


class DescribeBackendServerGroupsRequest(AbstractModel):
    """DescribeBackendServerGroups请求参数结构体
    """

    def __init__(self):
        r"""查询服务器组
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param BackendServerGroupId: 多个服务器组id
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.Filter = None
        self.BackendServerGroupId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ModifyBackendServerGroupRequest(AbstractModel):
    """ModifyBackendServerGroup请求参数结构体
    """

    def __init__(self):
        r"""修改服务器组
        :param BackendServerGroupId: 服务器组id
        :type PathPrefix: String
        :param Name: 负载均衡的名称
        :type PathPrefix: String
        :param UpstreamKeepalive: 后端长连接类型
        :type PathPrefix: String
        :param Method: 转发方式
        :type PathPrefix: String
        :param SessionState: 会话保持的状态(start|stop)
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param CookieType: 会话类型
        :type PathPrefix: String
        :param CookieName: Cookie的名称
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)
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
        :param HealthCheckConnectPort: 健康检查端口
        :type PathPrefix: Int
        :param HealthProtocol: 健康检查协议(TCP | ICMP| UDP | HTTP)
        :type PathPrefix: String
        :param HttpMethod: HTTP请求方式 (GET|HEAD)
        :type PathPrefix: String
        :param HealthCode: 健康状态返回码
        :type PathPrefix: String
        :param HealthCheckReq: UDP监听器健康检查的请求串
        :type PathPrefix: String
        :param HealthCheckExp: UDP监听器健康检查的响应串
        :type PathPrefix: String
        """
        self.BackendServerGroupId = None
        self.Name = None
        self.UpstreamKeepalive = None
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
        self.HealthCheckConnectPort = None
        self.HealthProtocol = None
        self.HttpMethod = None
        self.HealthCode = None
        self.HealthCheckReq = None
        self.HealthCheckExp = None

    def _deserialize(self, params):
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("UpstreamKeepalive"):
            self.UpstreamKeepalive = params.get("UpstreamKeepalive")
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
        if params.get("HealthCheckConnectPort"):
            self.HealthCheckConnectPort = params.get("HealthCheckConnectPort")
        if params.get("HealthProtocol"):
            self.HealthProtocol = params.get("HealthProtocol")
        if params.get("HttpMethod"):
            self.HttpMethod = params.get("HttpMethod")
        if params.get("HealthCode"):
            self.HealthCode = params.get("HealthCode")
        if params.get("HealthCheckReq"):
            self.HealthCheckReq = params.get("HealthCheckReq")
        if params.get("HealthCheckExp"):
            self.HealthCheckExp = params.get("HealthCheckExp")


class DeleteBackendServerGroupRequest(AbstractModel):
    """DeleteBackendServerGroup请求参数结构体
    """

    def __init__(self):
        r"""删除服务器组
        :param BackendServerGroupId: 服务器组id
        :type PathPrefix: String
        """
        self.BackendServerGroupId = None

    def _deserialize(self, params):
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")


class CreateBackendServerGroupRequest(AbstractModel):
    """CreateBackendServerGroup请求参数结构体
    """

    def __init__(self):
        r"""创建服务器组
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param Name: 负载均衡的名称
        :type PathPrefix: String
        :param BackendServerType: 服务器组的服务器类型
        :type PathPrefix: String
        :param Method: 调度算法（RoundRobin | LeastConnections | MasterSlave | QUIC_CID | IPHash）
        :type PathPrefix: String
        :param SessionState: 会话保持的状态(start|stop)
        :type PathPrefix: String
        :param SessionPersistencePeriod: 会话保持超时时间
        :type PathPrefix: Int
        :param CookieType: 会话类型
        :type PathPrefix: String
        :param CookieName: Cookie的名称
        :type PathPrefix: String
        :param UpstreamKeepalive: 后端长连接类型
        :type PathPrefix: String
        :param Protocol: 后端协议 (TCP | UDP |HTTP | gRPC | HTTPS)
        :type PathPrefix: String
        :param HealthCheckState: 健康检查保持的状态(start|stop)
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
        :param HealthCheckConnectPort: 健康检查端口
        :type PathPrefix: Int
        :param HealthProtocol(TCP | ICMP| UDP | HTTP): 健康检查协议
        :type PathPrefix: String
        :param HttpMethod: HTTP请求方式 (GET|HEAD)
        :type PathPrefix: String
        :param HealthCheckReq: UDP监听器健康检查的请求串
        :type PathPrefix: String
        :param HealthCheckExp: UDP监听器健康检查的响应串
        :type PathPrefix: String
        :param HealthCode: 健康状态返回码
        :type PathPrefix: String
        """
        self.VpcId = None
        self.Name = None
        self.BackendServerType = None
        self.Method = None
        self.SessionState = None
        self.SessionPersistencePeriod = None
        self.CookieType = None
        self.CookieName = None
        self.UpstreamKeepalive = None
        self.Protocol = None
        self.HealthCheckState = None
        self.Timeout = None
        self.Interval = None
        self.HealthyThreshold = None
        self.UnhealthyThreshold = None
        self.UrlPath = None
        self.HostName = None
        self.HealthCheckConnectPort = None
        self.HealthProtocol = None
        self.HttpMethod = None
        self.HealthCheckReq = None
        self.HealthCheckExp = None
        self.HealthCode = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("BackendServerType"):
            self.BackendServerType = params.get("BackendServerType")
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
        if params.get("UpstreamKeepalive"):
            self.UpstreamKeepalive = params.get("UpstreamKeepalive")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
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
        if params.get("HealthCheckConnectPort"):
            self.HealthCheckConnectPort = params.get("HealthCheckConnectPort")
        if params.get("HealthProtocol"):
            self.HealthProtocol = params.get("HealthProtocol")
        if params.get("HttpMethod"):
            self.HttpMethod = params.get("HttpMethod")
        if params.get("HealthCheckReq"):
            self.HealthCheckReq = params.get("HealthCheckReq")
        if params.get("HealthCheckExp"):
            self.HealthCheckExp = params.get("HealthCheckExp")
        if params.get("HealthCode"):
            self.HealthCode = params.get("HealthCode")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners请求参数结构体
    """

    def __init__(self):
        r"""查询监听器
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


class ModifyListenerRequest(AbstractModel):
    """ModifyListener请求参数结构体
    """

    def __init__(self):
        r"""修改监听器
        :param ListenerId: 监听器的ID
        :type PathPrefix: String
        :param ListenerName: 负载均衡监听器的名称
        :type PathPrefix: String
        :param ListenerState: 监听器的状态
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        :param TlsCipherPolicy: TLS安全策略
        :type PathPrefix: String
        :param ListenerAclId: LoadBalancerAcl的ID
        :type PathPrefix: String
        :param HttpProtocol: 后端协议版本(HTTP1.0|HTTP1.1)
        :type PathPrefix: String
        :param EnableHttp2: 是否启用HTTP/2
        :type PathPrefix: Boolean
        :param CaEnabled: 是否开启双向认证
        :type PathPrefix: Boolean
        :param CaCertificateId: 客户端证书
        :type PathPrefix: String
        :param EnableQuicUpgrade: 是否开启QUIC
        :type PathPrefix: Boolean
        :param QuicListenerId: QUIC监听器id
        :type PathPrefix: String
        :param ServerGroupId: 服务器组 ID
        :type PathPrefix: String
        """
        self.ListenerId = None
        self.ListenerName = None
        self.ListenerState = None
        self.CertificateId = None
        self.TlsCipherPolicy = None
        self.ListenerAclId = None
        self.HttpProtocol = None
        self.EnableHttp2 = None
        self.CaEnabled = None
        self.CaCertificateId = None
        self.EnableQuicUpgrade = None
        self.QuicListenerId = None
        self.ServerGroupId = None

    def _deserialize(self, params):
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")
        if params.get("ListenerName"):
            self.ListenerName = params.get("ListenerName")
        if params.get("ListenerState"):
            self.ListenerState = params.get("ListenerState")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("TlsCipherPolicy"):
            self.TlsCipherPolicy = params.get("TlsCipherPolicy")
        if params.get("ListenerAclId"):
            self.ListenerAclId = params.get("ListenerAclId")
        if params.get("HttpProtocol"):
            self.HttpProtocol = params.get("HttpProtocol")
        if params.get("EnableHttp2"):
            self.EnableHttp2 = params.get("EnableHttp2")
        if params.get("CaEnabled"):
            self.CaEnabled = params.get("CaEnabled")
        if params.get("CaCertificateId"):
            self.CaCertificateId = params.get("CaCertificateId")
        if params.get("EnableQuicUpgrade"):
            self.EnableQuicUpgrade = params.get("EnableQuicUpgrade")
        if params.get("QuicListenerId"):
            self.QuicListenerId = params.get("QuicListenerId")
        if params.get("ServerGroupId"):
            self.ServerGroupId = params.get("ServerGroupId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener请求参数结构体
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


class CreateListenerRequest(AbstractModel):
    """CreateListener请求参数结构体
    """

    def __init__(self):
        r"""创建监听器
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param ListenerName: 负载均衡监听器的名称
        :type PathPrefix: String
        :param Protocol: 监听器的协议(TCP|UDP|TCPSSL|HTTP|HTTPS|QUIC)
        :type PathPrefix: String
        :param Port: 监听器的协议端口
        :type PathPrefix: Int
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        :param TlsCipherPolicy: TLS安全策略
        :type PathPrefix: String
        :param ListenerAclId: LoadBalancerAcl的ID
        :type PathPrefix: String
        :param ListenerState: 监听器的状态(start|stop)
        :type PathPrefix: String
        :param RedirectListenerId: 重定向监听器ID
        :type PathPrefix: String
        :param RedirectHttpCode: 重定向状态码
        :type PathPrefix: String
        :param EnableHttp2: 是否启用HTTP/2
        :type PathPrefix: Boolean
        :param BackendServerGroupId: 默认转发策略绑定的服务器组ID,目前仅支持创建转发类型的默认转发策略
        :type PathPrefix: String
        :param FixedResponseConfig: 返回固定响应信息
        :type PathPrefix: Object
        :param RewriteConfig: 返回固定响应信息
        :type PathPrefix: Object
        :param CaEnabled: 是否开启双向认证
        :type PathPrefix: Boolean
        :param CaCertificateId: 客户端证书
        :type PathPrefix: String
        :param EnableQuicUpgrade: 是否开启QUIC
        :type PathPrefix: Boolean
        :param QuicListenerId: QUIC监听器id
        :type PathPrefix: String
        :param ServerGroupId: 服务器组 ID
        :type PathPrefix: String
        """
        self.LoadBalancerId = None
        self.ListenerName = None
        self.Protocol = None
        self.Port = None
        self.CertificateId = None
        self.TlsCipherPolicy = None
        self.ListenerAclId = None
        self.ListenerState = None
        self.RedirectListenerId = None
        self.RedirectHttpCode = None
        self.EnableHttp2 = None
        self.BackendServerGroupId = None
        self.FixedResponseConfig = None
        self.RewriteConfig = None
        self.CaEnabled = None
        self.CaCertificateId = None
        self.EnableQuicUpgrade = None
        self.QuicListenerId = None
        self.ServerGroupId = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerName"):
            self.ListenerName = params.get("ListenerName")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("Port"):
            self.Port = params.get("Port")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("TlsCipherPolicy"):
            self.TlsCipherPolicy = params.get("TlsCipherPolicy")
        if params.get("ListenerAclId"):
            self.ListenerAclId = params.get("ListenerAclId")
        if params.get("ListenerState"):
            self.ListenerState = params.get("ListenerState")
        if params.get("RedirectListenerId"):
            self.RedirectListenerId = params.get("RedirectListenerId")
        if params.get("RedirectHttpCode"):
            self.RedirectHttpCode = params.get("RedirectHttpCode")
        if params.get("EnableHttp2"):
            self.EnableHttp2 = params.get("EnableHttp2")
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("FixedResponseConfig"):
            self.FixedResponseConfig = params.get("FixedResponseConfig")
        if params.get("RewriteConfig"):
            self.RewriteConfig = params.get("RewriteConfig")
        if params.get("CaEnabled"):
            self.CaEnabled = params.get("CaEnabled")
        if params.get("CaCertificateId"):
            self.CaCertificateId = params.get("CaCertificateId")
        if params.get("EnableQuicUpgrade"):
            self.EnableQuicUpgrade = params.get("EnableQuicUpgrade")
        if params.get("QuicListenerId"):
            self.QuicListenerId = params.get("QuicListenerId")
        if params.get("ServerGroupId"):
            self.ServerGroupId = params.get("ServerGroupId")


class SetAccessLogRequest(AbstractModel):
    """SetAccessLog请求参数结构体
    """

    def __init__(self):
        r"""创建/修改访问日志对接klog
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param ProjectName: 访问日志投递的日志库
        :type PathPrefix: String
        :param LogpoolName: 访问日志投递的日志池
        :type PathPrefix: String
        """
        self.LoadBalancerId = None
        self.ProjectName = None
        self.LogpoolName = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("LogpoolName"):
            self.LogpoolName = params.get("LogpoolName")


class SetEnableAccessLogRequest(AbstractModel):
    """SetEnableAccessLog请求参数结构体
    """

    def __init__(self):
        r"""设置访问日志对接klog开关
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param EnabledLog: 是否开启日志服务
        :type PathPrefix: Boolean
        """
        self.LoadBalancerId = None
        self.EnabledLog = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("EnabledLog"):
            self.EnabledLog = params.get("EnabledLog")


class SetLbProtocolLayersRequest(AbstractModel):
    """SetLbProtocolLayers请求参数结构体
    """

    def __init__(self):
        r"""设置LB的协议层数
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param ProtocolLayers: 实例规格,可选 L4 / L7 / L4-L7 ,分别代指4层、7层、4-7层网络协议负载均衡
        :type PathPrefix: String
        """
        self.LoadBalancerId = None
        self.ProtocolLayers = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ProtocolLayers"):
            self.ProtocolLayers = params.get("ProtocolLayers")


class ModifyLoadBalancerRequest(AbstractModel):
    """ModifyLoadBalancer请求参数结构体
    """

    def __init__(self):
        r"""修改高阶/hpa配置接口
        """

    def _deserialize(self, params):
        return


class SetLoadBalancerStatusRequest(AbstractModel):
    """SetLoadBalancerStatus请求参数结构体
    """

    def __init__(self):
        r"""设置负载均衡状态
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param State: 负载均衡的开启状态(start|stop)
        :type PathPrefix: String
        """
        self.LoadBalancerId = None
        self.State = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("State"):
            self.State = params.get("State")


class SetLoadBalancerNameRequest(AbstractModel):
    """SetLoadBalancerName请求参数结构体
    """

    def __init__(self):
        r"""设置负载均衡名称
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param LoadBalancerName: 负载均衡的名称
        :type PathPrefix: String
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("LoadBalancerName"):
            self.LoadBalancerName = params.get("LoadBalancerName")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体
    """

    def __init__(self):
        r"""查询负载均衡
        :param LoadBalancerId: 多个负载均衡的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param IsContainTag: 是否在返回值中包含资源标签信息
        :type PathPrefix: Boolean
        :param TagKey: 多个标签的键
        :type PathPrefix: Filter
        :param TagKV: 多个标签的键
        :type PathPrefix: Filter
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.LoadBalancerId = None
        self.Filter = None
        self.IsContainTag = None
        self.TagKey = None
        self.TagKV = None
        self.ProjectId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("IsContainTag"):
            self.IsContainTag = params.get("IsContainTag")
        if params.get("TagKey"):
            self.TagKey = params.get("TagKey")
        if params.get("TagKV"):
            self.TagKV = params.get("TagKV")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


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


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer请求参数结构体
    """

    def __init__(self):
        r"""创建负载均衡
        :param LoadBalancerName: 负载均衡的名称
        :type PathPrefix: String
        :param LoadBalancerVersion: 负载均衡支持的版本
        :type PathPrefix: String
        :param LoadBalancerType: 负载均衡的类型，public 为公网负载均衡，internal 为内网负载均衡
        :type PathPrefix: String
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param IpVersion: 负载均衡的IP版本
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param AllocationId: 弹性IP的ID
        :type PathPrefix: String
        :param ChargeType: 计费类型(PrePaidByHourUsage，按小时用量实时付费（小时结))
        :type PathPrefix: String
        :param SubnetId: 子网id
        :type PathPrefix: String
        :param PrivateIpAddress: 私网ip
        :type PathPrefix: String
        :param EnabledQuic: 是否开启QUIC功能
        :type PathPrefix: Boolean
        :param EnableHpa: 是否开启弹性伸缩
        :type PathPrefix: Boolean
        :param ProtocolLayers: 实例规格,可选 L4 / L7 / L4-L7 ,分别代指4层、7层、4-7层网络协议负载均衡
        :type PathPrefix: String
        :param DeleteProtection: 是否开启删除保护on/off
        :type PathPrefix: String
        :param ModificationProtection: 是否开启修改保护on/off
        :type PathPrefix: String
        """
        self.LoadBalancerName = None
        self.LoadBalancerVersion = None
        self.LoadBalancerType = None
        self.VpcId = None
        self.IpVersion = None
        self.ProjectId = None
        self.AllocationId = None
        self.ChargeType = None
        self.SubnetId = None
        self.PrivateIpAddress = None
        self.EnabledQuic = None
        self.EnableHpa = None
        self.ProtocolLayers = None
        self.DeleteProtection = None
        self.ModificationProtection = None

    def _deserialize(self, params):
        if params.get("LoadBalancerName"):
            self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("LoadBalancerVersion"):
            self.LoadBalancerVersion = params.get("LoadBalancerVersion")
        if params.get("LoadBalancerType"):
            self.LoadBalancerType = params.get("LoadBalancerType")
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
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("EnabledQuic"):
            self.EnabledQuic = params.get("EnabledQuic")
        if params.get("EnableHpa"):
            self.EnableHpa = params.get("EnableHpa")
        if params.get("ProtocolLayers"):
            self.ProtocolLayers = params.get("ProtocolLayers")
        if params.get("DeleteProtection"):
            self.DeleteProtection = params.get("DeleteProtection")
        if params.get("ModificationProtection"):
            self.ModificationProtection = params.get("ModificationProtection")


class ModifyCertificateWithGroupRequest(AbstractModel):
    """ModifyCertificateWithGroup请求参数结构体
    """

    def __init__(self):
        r"""监听器维度更换同域名的证书
        :param ListenerCertGroupId: 证书组的ID
        :type PathPrefix: String
        :param OldCertificateId: 旧证书的ID
        :type PathPrefix: String
        :param CertificateId: 新证书的ID
        :type PathPrefix: String
        """
        self.ListenerCertGroupId = None
        self.OldCertificateId = None
        self.CertificateId = None

    def _deserialize(self, params):
        if params.get("ListenerCertGroupId"):
            self.ListenerCertGroupId = params.get("ListenerCertGroupId")
        if params.get("OldCertificateId"):
            self.OldCertificateId = params.get("OldCertificateId")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")


class DissociateCertificateWithGroupRequest(AbstractModel):
    """DissociateCertificateWithGroup请求参数结构体
    """

    def __init__(self):
        r"""移除证书出证书组
        :param ListenerCertGroupId: 证书组的ID
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        """
        self.ListenerCertGroupId = None
        self.CertificateId = None

    def _deserialize(self, params):
        if params.get("ListenerCertGroupId"):
            self.ListenerCertGroupId = params.get("ListenerCertGroupId")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")


class AssociateCertificateWithGroupRequest(AbstractModel):
    """AssociateCertificateWithGroup请求参数结构体
    """

    def __init__(self):
        r"""添加证书进证书组
        :param ListenerCertGroupId: 证书组的ID
        :type PathPrefix: String
        :param CertificateId: 证书的ID
        :type PathPrefix: String
        """
        self.ListenerCertGroupId = None
        self.CertificateId = None

    def _deserialize(self, params):
        if params.get("ListenerCertGroupId"):
            self.ListenerCertGroupId = params.get("ListenerCertGroupId")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")


class DescribeListenerCertGroupsRequest(AbstractModel):
    """DescribeListenerCertGroups请求参数结构体
    """

    def __init__(self):
        r"""描述证书组
        :param ListenerCertGroupId: 多个证书组的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.ListenerCertGroupId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("ListenerCertGroupId"):
            self.ListenerCertGroupId = params.get("ListenerCertGroupId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeleteListenerCertGroupRequest(AbstractModel):
    """DeleteListenerCertGroup请求参数结构体
    """

    def __init__(self):
        r"""删除证书组
        :param ListenerCertGroupId: 证书组的ID
        :type PathPrefix: String
        """
        self.ListenerCertGroupId = None

    def _deserialize(self, params):
        if params.get("ListenerCertGroupId"):
            self.ListenerCertGroupId = params.get("ListenerCertGroupId")


class CreateListenerCertGroupRequest(AbstractModel):
    """CreateListenerCertGroup请求参数结构体
    """

    def __init__(self):
        r"""创建证书组
        :param ListenerId: 应用型负载均衡监听器的ID
        :type PathPrefix: String
        """
        self.ListenerId = None

    def _deserialize(self, params):
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")


class AddRulesRequest(AbstractModel):
    """AddRules请求参数结构体
    """

    def __init__(self):
        r"""添加多个转发规则
        :param RuleGroupId: 转发策略的ID
        :type PathPrefix: String
        :param RuleType: 匹配规则类型(domain|url|method|sourceIp|header|query|cookie)
        :type PathPrefix: String
        :param RuleValue: 匹配规则的值
        :type PathPrefix: String
        :param MethodValue: HTTP请求方法
        :type PathPrefix: Array
        :param SourceIpValue: SourceIp
        :type PathPrefix: Array
        :param HeaderValue: HTTP标头
        :type PathPrefix: Array
        :param QueryValue: 查询字符串
        :type PathPrefix: Array
        :param CookieValue: Cookie转发条件
        :type PathPrefix: Array
        """
        self.RuleGroupId = None
        self.RuleType = None
        self.RuleValue = None
        self.MethodValue = None
        self.SourceIpValue = None
        self.HeaderValue = None
        self.QueryValue = None
        self.CookieValue = None

    def _deserialize(self, params):
        if params.get("RuleGroupId"):
            self.RuleGroupId = params.get("RuleGroupId")
        if params.get("RuleType"):
            self.RuleType = params.get("RuleType")
        if params.get("RuleValue"):
            self.RuleValue = params.get("RuleValue")
        if params.get("MethodValue"):
            self.MethodValue = params.get("MethodValue")
        if params.get("SourceIpValue"):
            self.SourceIpValue = params.get("SourceIpValue")
        if params.get("HeaderValue"):
            self.HeaderValue = params.get("HeaderValue")
        if params.get("QueryValue"):
            self.QueryValue = params.get("QueryValue")
        if params.get("CookieValue"):
            self.CookieValue = params.get("CookieValue")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体
    """

    def __init__(self):
        r"""删除转发策略规则
        :param RuleGroupId: 转发策略的ID
        :type PathPrefix: String
        :param RuleType: 匹配规则类型(domain|url)
        :type PathPrefix: String
        :param RuleValue: 匹配规则的值
        :type PathPrefix: String
        """
        self.RuleGroupId = None
        self.RuleType = None
        self.RuleValue = None

    def _deserialize(self, params):
        if params.get("RuleGroupId"):
            self.RuleGroupId = params.get("RuleGroupId")
        if params.get("RuleType"):
            self.RuleType = params.get("RuleType")
        if params.get("RuleValue"):
            self.RuleValue = params.get("RuleValue")


class AddRuleRequest(AbstractModel):
    """AddRule请求参数结构体
    """

    def __init__(self):
        r"""创建转发策略规则
        :param RuleGroupId: 转发策略的ID
        :type PathPrefix: String
        :param RuleType: 匹配规则类型(domain|url)
        :type PathPrefix: String
        :param RuleValue: 匹配规则的值
        :type PathPrefix: String
        """
        self.RuleGroupId = None
        self.RuleType = None
        self.RuleValue = None

    def _deserialize(self, params):
        if params.get("RuleGroupId"):
            self.RuleGroupId = params.get("RuleGroupId")
        if params.get("RuleType"):
            self.RuleType = params.get("RuleType")
        if params.get("RuleValue"):
            self.RuleValue = params.get("RuleValue")


class ModifyRuleGroupRequest(AbstractModel):
    """ModifyRuleGroup请求参数结构体
    """

    def __init__(self):
        r"""修改转发策略
        :param RuleGroupId: 转发策略的ID
        :type PathPrefix: String
        :param RuleGroupName: 转发策略的名称
        :type PathPrefix: String
        :param BackendServerGroupId: 后端服务器组的ID
        :type PathPrefix: String
        :param Type: 转发动作类型
        :type PathPrefix: String
        :param RuleSet: 规则的信息
        :type PathPrefix: Array
        :param RedirectListenerId: 重定向监听器ID
        :type PathPrefix: String
        :param RedirectHttpCode: 重定向状态码,301|302|307
        :type PathPrefix: String
        :param FixedResponseConfig: 返回固定响应信息
        :type PathPrefix: Object
        :param RewriteConfig: 重写
        :type PathPrefix: Object
        """
        self.RuleGroupId = None
        self.RuleGroupName = None
        self.BackendServerGroupId = None
        self.Type = None
        self.RuleSet = None
        self.RedirectListenerId = None
        self.RedirectHttpCode = None
        self.FixedResponseConfig = None
        self.RewriteConfig = None

    def _deserialize(self, params):
        if params.get("RuleGroupId"):
            self.RuleGroupId = params.get("RuleGroupId")
        if params.get("RuleGroupName"):
            self.RuleGroupName = params.get("RuleGroupName")
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("RuleSet"):
            self.RuleSet = params.get("RuleSet")
        if params.get("RedirectListenerId"):
            self.RedirectListenerId = params.get("RedirectListenerId")
        if params.get("RedirectHttpCode"):
            self.RedirectHttpCode = params.get("RedirectHttpCode")
        if params.get("FixedResponseConfig"):
            self.FixedResponseConfig = params.get("FixedResponseConfig")
        if params.get("RewriteConfig"):
            self.RewriteConfig = params.get("RewriteConfig")


class DescribeRuleGroupsRequest(AbstractModel):
    """DescribeRuleGroups请求参数结构体
    """

    def __init__(self):
        r"""描述转发策略
        :param RuleGroupId: 多个转发策略的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.RuleGroupId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("RuleGroupId"):
            self.RuleGroupId = params.get("RuleGroupId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeleteRuleGroupRequest(AbstractModel):
    """DeleteRuleGroup请求参数结构体
    """

    def __init__(self):
        r"""删除转发策略
        :param RuleGroupId: 转发策略的ID
        :type PathPrefix: String
        """
        self.RuleGroupId = None

    def _deserialize(self, params):
        if params.get("RuleGroupId"):
            self.RuleGroupId = params.get("RuleGroupId")


class CreateRuleGroupRequest(AbstractModel):
    """CreateRuleGroup请求参数结构体
    """

    def __init__(self):
        r"""创建转发策略
        :param RuleGroupName: 转发策略的名称
        :type PathPrefix: String
        :param ListenerId: 负载均衡监听器的ID
        :type PathPrefix: String
        :param BackendServerGroupId: 后端服务器组的ID
        :type PathPrefix: String
        :param Type: 转发动作类型
        :type PathPrefix: String
        :param RuleSet: 规则的信息
        :type PathPrefix: Array
        :param RedirectListenerId: 重定向监听器ID
        :type PathPrefix: String
        :param RedirectHttpCode: 重定向状态码,301|302|307
        :type PathPrefix: String
        :param FixedResponseConfig: 返回固定响应信息
        :type PathPrefix: Object
        :param RewriteConfig: 重写
        :type PathPrefix: Object
        """
        self.RuleGroupName = None
        self.ListenerId = None
        self.BackendServerGroupId = None
        self.Type = None
        self.RuleSet = None
        self.RedirectListenerId = None
        self.RedirectHttpCode = None
        self.FixedResponseConfig = None
        self.RewriteConfig = None

    def _deserialize(self, params):
        if params.get("RuleGroupName"):
            self.RuleGroupName = params.get("RuleGroupName")
        if params.get("ListenerId"):
            self.ListenerId = params.get("ListenerId")
        if params.get("BackendServerGroupId"):
            self.BackendServerGroupId = params.get("BackendServerGroupId")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("RuleSet"):
            self.RuleSet = params.get("RuleSet")
        if params.get("RedirectListenerId"):
            self.RedirectListenerId = params.get("RedirectListenerId")
        if params.get("RedirectHttpCode"):
            self.RedirectHttpCode = params.get("RedirectHttpCode")
        if params.get("FixedResponseConfig"):
            self.FixedResponseConfig = params.get("FixedResponseConfig")
        if params.get("RewriteConfig"):
            self.RewriteConfig = params.get("RewriteConfig")


class SetLBModificationProtectionRequest(AbstractModel):
    """SetLBModificationProtection请求参数结构体
    """

    def __init__(self):
        r"""负载均衡修改保护
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param ModificationProtection: 是否开启修改保护on/off
        :type PathPrefix: Boolean
        """
        self.LoadBalancerId = None
        self.ModificationProtection = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModificationProtection"):
            self.ModificationProtection = params.get("ModificationProtection")


class SetLBDeleteProtectionRequest(AbstractModel):
    """SetLBDeleteProtection请求参数结构体
    """

    def __init__(self):
        r"""负载均衡删除保护
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: String
        :param DeleteProtection: 是否开启删除保护on/off
        :type PathPrefix: Boolean
        """
        self.LoadBalancerId = None
        self.DeleteProtection = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("DeleteProtection"):
            self.DeleteProtection = params.get("DeleteProtection")
