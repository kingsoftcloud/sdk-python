from ksyun.common.abstract_model import AbstractModel

class DeleteBatchCfwAddrbookRequest(AbstractModel):
    """DeleteBatchCfwAddrbook请求参数结构体
    """

    def __init__(self):
        r"""批量删除地址簿
        :param AddrbookIds: 要删除的地址簿ID列表，单次删除数量不能超过1000条
        :type PathPrefix: Array
        :param CfwInstanceId: 防火墙实例ID
        :type PathPrefix: String
        """
        self.AddrbookIds = None
        self.CfwInstanceId = None

    def _deserialize(self, params):
        if params.get("AddrbookIds"):
            self.AddrbookIds = params.get("AddrbookIds")
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")


class DeleteServiceGroupBatchRequest(AbstractModel):
    """DeleteServiceGroupBatch请求参数结构体
    """

    def __init__(self):
        r"""批量删除服务组
        :param ServiceGroupIds: 服务组ID集合
        :type PathPrefix: Array
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        """
        self.ServiceGroupIds = None
        self.CfwInstanceId = None

    def _deserialize(self, params):
        if params.get("ServiceGroupIds"):
            self.ServiceGroupIds = params.get("ServiceGroupIds")
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")


class DeleteBatchHostbookRequest(AbstractModel):
    """DeleteBatchHostbook请求参数结构体
    """

    def __init__(self):
        r"""批量删除域名簿
        :param HostbookIds: 需要批量删除的域名簿ID列表。域名簿ID是创建域名簿时系统自动生成的唯一标识符，格式为UUID。支持一次性删除多个域名簿，但建议单次删除数量不超过100个。注意：被ACL规则引用的域名簿无法删除。
        :type PathPrefix: Array
        :param CfwInstanceId: 云防火墙实例ID。指定要删除域名簿的云防火墙实例，域名簿必须属于该防火墙实例。防火墙实例ID是创建防火墙时系统自动生成的唯一标识符，格式为UUID。
        :type PathPrefix: String
        """
        self.HostbookIds = None
        self.CfwInstanceId = None

    def _deserialize(self, params):
        if params.get("HostbookIds"):
            self.HostbookIds = params.get("HostbookIds")
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")


class ModifyHostbookRequest(AbstractModel):
    """ModifyHostbook请求参数结构体
    """

    def __init__(self):
        r"""修改已存在的域名簿信息，包括名称、域名列表和描述
        :param HostbookId: 域名簿ID，用于标识要修改的域名簿
        :type PathPrefix: String
        :param HostbookName: 域名簿名称，最大长度95个字符
        :type PathPrefix: String
        :param HostValue: 域名列表，修改时可为空表示不修改域名列表，最多1500个域名，每个域名最长67个字符
        :type PathPrefix: Array
        :param Description: 域名簿描述信息，最大长度255个字符
        :type PathPrefix: String
        """
        self.HostbookId = None
        self.HostbookName = None
        self.HostValue = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("HostbookId"):
            self.HostbookId = params.get("HostbookId")
        if params.get("HostbookName"):
            self.HostbookName = params.get("HostbookName")
        if params.get("HostValue"):
            self.HostValue = params.get("HostValue")
        if params.get("Description"):
            self.Description = params.get("Description")


class CreateHostbookRequest(AbstractModel):
    """CreateHostbook请求参数结构体
    """

    def __init__(self):
        r"""创建域名簿，用于管理防火墙的域名白名单
        :param CfwInstanceId: 云防火墙实例ID，用于指定要操作的防火墙实例
        :type PathPrefix: String
        :param HostbookName: 域名簿名称，长度不能超过95个字符
        :type PathPrefix: String
        :param HostValue: 域名列表，最多可添加1500个域名，支持完整域名和通配符域名
        :type PathPrefix: Array
        :param Description: 域名簿描述信息，长度不能超过255个字符
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.HostbookName = None
        self.HostValue = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("HostbookName"):
            self.HostbookName = params.get("HostbookName")
        if params.get("HostValue"):
            self.HostValue = params.get("HostValue")
        if params.get("Description"):
            self.Description = params.get("Description")


class DescribeHostbookRequest(AbstractModel):
    """DescribeHostbook请求参数结构体
    """

    def __init__(self):
        r"""查询域名簿
        :param CfwInstanceId: 防火墙实例ID
        :type PathPrefix: String
        :param HostbookIds: 查询的域名簿Id
        :type PathPrefix: Array
        :param MaxResults: 最大返回单次调用可返回的最大条目数量. 传入返回的 NextToken 值可以获取剩余的其它条目. 这个值可以允许的范围是 5 - 1000
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.HostbookIds = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("HostbookIds"):
            self.HostbookIds = params.get("HostbookIds")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class QueryCfwInstanceDetailRequest(AbstractModel):
    """QueryCfwInstanceDetail请求参数结构体
    """

    def __init__(self):
        r"""查询防火墙详情
        :param CfwInstanceId: 云防火墙id
        :type PathPrefix: String
        """
        self.CfwInstanceId = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")


class DeleteCloudFireWallInstanceRequest(AbstractModel):
    """DeleteCloudFireWallInstance请求参数结构体
    """

    def __init__(self):
        r"""退订云防火墙
        :param CfwInstanceId: 云防火墙id
        :type PathPrefix: String
        """
        self.CfwInstanceId = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")


class QueryOverviewDetailRequest(AbstractModel):
    """QueryOverviewDetail请求参数结构体
    """

    def __init__(self):
        r"""查询指定防火墙实例在指定时间段内的总览统计数据，包括ACL拒绝次数、IPS检测次数、入站和出站流量峰值等信息
        :param CfwInstanceId: 云防火墙id
        :type PathPrefix: String
        :param StartTime: yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param EndTime: yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class DescribeTrafficLogRequest(AbstractModel):
    """DescribeTrafficLog请求参数结构体
    """

    def __init__(self):
        r"""流量日志查询
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param StartTime: 开始时间 格式yyyy-MM-dd HH:mm
        :type PathPrefix: String
        :param EndTime: 结束时间，格式yyyy-MM-dd HH:mm
        :type PathPrefix: String
        :param QueryKeyword: 查询关键字
        :type PathPrefix: String
        :param MaxResults: 最大值1000
        :type PathPrefix: Int
        :param NextToken: 下一页token
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.QueryKeyword = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("QueryKeyword"):
            self.QueryKeyword = params.get("QueryKeyword")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeAttackLogRequest(AbstractModel):
    """DescribeAttackLog请求参数结构体
    """

    def __init__(self):
        r"""根据指定的时间范围和条件查询防火墙攻击日志，支持关键字搜索和分页查询
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param StartTime: 开始时间 格式yyyy-MM-dd HH:mm
        :type PathPrefix: String
        :param EndTime: 结束时间，格式yyyy-MM-dd HH:mm
        :type PathPrefix: String
        :param QueryKeyword: 查询关键字
        :type PathPrefix: String
        :param MaxResults: 最大值1000
        :type PathPrefix: String
        :param NextToken: 下一页token
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.QueryKeyword = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("QueryKeyword"):
            self.QueryKeyword = params.get("QueryKeyword")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeAclLogRequest(AbstractModel):
    """DescribeAclLog请求参数结构体
    """

    def __init__(self):
        r"""访问控制日志查询
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param StartTime: 开始时间 格式yyyy-MM-dd HH:mm
        :type PathPrefix: String
        :param EndTime: 结束时间，格式yyyy-MM-dd HH:mm
        :type PathPrefix: String
        :param QueryKeyword: 查询关键字
        :type PathPrefix: String
        :param MaxResults: 最大值1000
        :type PathPrefix: Int
        :param NextToken: 下一页token
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.QueryKeyword = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("QueryKeyword"):
            self.QueryKeyword = params.get("QueryKeyword")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ModifyCloudFireWallFeatureRequest(AbstractModel):
    """ModifyCloudFireWallFeature请求参数结构体
    """

    def __init__(self):
        r"""修改云防火墙名称
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param InstanceName: 防火墙名称
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.InstanceName = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")


class DescribeCfwAddrbookRequest(AbstractModel):
    """DescribeCfwAddrbook请求参数结构体
    """

    def __init__(self):
        r"""查询地址簿
        :param CfwInstanceId: 云防火墙id
        :type PathPrefix: String
        :param AddrbookIds: 访问控制策略id集合
        :type PathPrefix: Array
        :param MaxResults: 5到1000
        :type PathPrefix: Int
        :param NextToken: 下一页token
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.AddrbookIds = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("AddrbookIds"):
            self.AddrbookIds = params.get("AddrbookIds")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeleteCfwAddrbookRequest(AbstractModel):
    """DeleteCfwAddrbook请求参数结构体
    """

    def __init__(self):
        r"""删除地址簿
        :param AddrbookId: 地址簿id
        :type PathPrefix: String
        """
        self.AddrbookId = None

    def _deserialize(self, params):
        if params.get("AddrbookId"):
            self.AddrbookId = params.get("AddrbookId")


class ModifyCfwAddrbookRequest(AbstractModel):
    """ModifyCfwAddrbook请求参数结构体
    """

    def __init__(self):
        r"""修改云防火墙地址簿的配置信息，包括地址簿名称、IP地址列表、描述信息等。支持批量更新多个IP地址，最多支持640个IP地址成员。
        :param CfwInstanceId: 云防火墙id
        :type PathPrefix: String
        :param AddrbookName: 地址簿名称
        :type PathPrefix: String
        :param IpAddress: ip集合
        :type PathPrefix: Array
        :param Description: 描述
        :type PathPrefix: String
        :param IpVersion: IPv4
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.AddrbookName = None
        self.IpAddress = None
        self.Description = None
        self.IpVersion = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("AddrbookName"):
            self.AddrbookName = params.get("AddrbookName")
        if params.get("IpAddress"):
            self.IpAddress = params.get("IpAddress")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")


class CreateCfwAddrbookRequest(AbstractModel):
    """CreateCfwAddrbook请求参数结构体
    """

    def __init__(self):
        r"""创建地址簿
        :param CfwInstanceId: 云防火墙id
        :type PathPrefix: String
        :param AddrbookName: 地址簿名称
        :type PathPrefix: String
        :param IpAddress: ip地址
        :type PathPrefix: Array
        :param Description: 描述
        :type PathPrefix: String
        :param IpVersion: IPv4
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.AddrbookName = None
        self.IpAddress = None
        self.Description = None
        self.IpVersion = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("AddrbookName"):
            self.AddrbookName = params.get("AddrbookName")
        if params.get("IpAddress"):
            self.IpAddress = params.get("IpAddress")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")


class AlterCfwAclStatusRequest(AbstractModel):
    """AlterCfwAclStatus请求参数结构体
    """

    def __init__(self):
        r"""用于批量修改云防火墙ACL规则的启用状态，支持同时开启或关闭多个ACL规则，操作后规则状态将立即生效
        :param AclIds: 访问控制策略id集合
        :type PathPrefix: Array
        :param Status: 开启：start|关闭：stop
        :type PathPrefix: String
        """
        self.AclIds = None
        self.Status = None

    def _deserialize(self, params):
        if params.get("AclIds"):
            self.AclIds = params.get("AclIds")
        if params.get("Status"):
            self.Status = params.get("Status")


class ResetCfwAclHitCountRequest(AbstractModel):
    """ResetCfwAclHitCount请求参数结构体
    """

    def __init__(self):
        r"""ACL重置命中数
        :param AclIds: 访问控制策略集合
        :type PathPrefix: Array
        """
        self.AclIds = None

    def _deserialize(self, params):
        if params.get("AclIds"):
            self.AclIds = params.get("AclIds")


class AlterAclPriorityRequest(AbstractModel):
    """AlterAclPriority请求参数结构体
    """

    def __init__(self):
        r"""改acl优先级
        :param PriorityPosition: 优先级(after/before+优先级)
before为置顶，after为置底
after+优先级 表示设置为该优先级+1 且之后的规则所有优先级都+1
before+优先级 表示设置为该优先级 原优先级规则及其之后所有规则优先级都+1

        :type PathPrefix: String
        :param AclId: 访问控制策略id
        :type PathPrefix: String
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        """
        self.PriorityPosition = None
        self.AclId = None
        self.CfwInstanceId = None

    def _deserialize(self, params):
        if params.get("PriorityPosition"):
            self.PriorityPosition = params.get("PriorityPosition")
        if params.get("AclId"):
            self.AclId = params.get("AclId")
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")


class DeleteCfwAclRequest(AbstractModel):
    """DeleteCfwAcl请求参数结构体
    """

    def __init__(self):
        r"""删除ACL
        :param AclIds: 访问控制集合
        :type PathPrefix: Array
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        """
        self.AclIds = None
        self.CfwInstanceId = None

    def _deserialize(self, params):
        if params.get("AclIds"):
            self.AclIds = params.get("AclIds")
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")


class ModifyCfwAclRequest(AbstractModel):
    """ModifyCfwAcl请求参数结构体
    """

    def __init__(self):
        r"""修改ACL
        :param AclId: 访问控制策略id
        :type PathPrefix: String
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param AclName: 访问控制名称
        :type PathPrefix: String
        :param Direction: 出入向(入向：in, 出向：out)
        :type PathPrefix: String
        :param SrcType: 源地址类型(IP：ip|地址簿：addrbook|地域：zone|Any：any)
        :type PathPrefix: String
        :param SrcIps: 源ip，当SrcType为ip时必填
仅支持填写公网IPv4地址，支持IP地址段、IP地址范围。通过英文",“隔开，格式为：10.1.1.1/32,10.1.1.2/24,192.168.1.1-192.168.1.63”
1、地址段：可输入多个IP+掩码，中间通过英文逗号“,”隔开如192.168.1.1/32,110.1.1.1/24。
2、地址范围：多个连续的IP地址，中间通过"-"隔开如192.168.1.1–192.168.1.253
        :type PathPrefix: Array
        :param SrcAddrbooks: 地址簿id集合，当SrcType为addrbook时必填
        :type PathPrefix: Array
        :param SrcZones: 源地址地域，当SrcType为zone时必填，示例[{“areaCode”:“CN_HB”,“areaName”:“湖北省”}]
        :type PathPrefix: Array
        :param DestType: 目的类型：（IP：ip，地址簿：addrbook，地域：zone，域名簿：hostbook，域名：host，Any：any）
        :type PathPrefix: String
        :param DestIps: 目的ip，当DestType为ip时必填
仅支持填写公网IPv4地址，支持IP地址段、IP地址范围。通过英文",“隔开，格式为：10.1.1.1/32,10.1.1.2/24,192.168.1.1-192.168.1.63”
1、地址段：可输入多个IP+掩码，中间通过英文逗号“,”隔开如192.168.1.1/32,110.1.1.1/24。
2、地址范围：多个连续的IP地址，中间通过"-"隔开如192.168.1.1–192.168.1.253
        :type PathPrefix: Array
        :param DestAddrbooks: 目的地址簿id集合，当DestType为addrbook时必填
        :type PathPrefix: Array
        :param DestZones: 目的地址地域，当DestType为zone时必填，示例[{“areaCode”:“CN_HB”,“areaName”:“湖北省”}]
        :type PathPrefix: Array
        :param DestHost: 域名，目前只允许传一个域名，泛域名示例*.ksyun.con，完整域名示例uss.ksyun.com
        :type PathPrefix: Array
        :param DestHostbook: 域名簿id集合，目前只允许传一个
        :type PathPrefix: Array
        :param ServiceType: 服务类型，服务：service，服务组：servicegroup，Any：any
        :type PathPrefix: String
        :param ServiceInfos: 服务信息，ServiceType为service时必填，（协议:源端口最小-源端口最大/目的最小-目的最大 ）例：TCP:1-100/2-200,UDP:22/33,ICMP
        :type PathPrefix: Array
        :param ServiceGroups: 服务组id集合，ServiceType为servicegroup时必填
        :type PathPrefix: Array
        :param AppType: app|any
        :type PathPrefix: String
        :param AppValue: AppType为app时必填，TCP支持的应用集合(“HTTP”, “HTTPS”, “SMTP”, “SMTPS”, “IMAP4”, “MYSQL”,“POP3”, “POP3S”, “SSH”, “TLS1”, “VNC”, “DNS”, “RDP”)，UDP支持的应用集合(“DNS”, “RDP”)，ICMP只能填any
        :type PathPrefix: Array
        :param Policy: 动作，允许：accept，拒绝：deny
        :type PathPrefix: String
        :param Status: 开启：start，关闭：stop
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        """
        self.AclId = None
        self.CfwInstanceId = None
        self.AclName = None
        self.Direction = None
        self.SrcType = None
        self.SrcIps = None
        self.SrcAddrbooks = None
        self.SrcZones = None
        self.DestType = None
        self.DestIps = None
        self.DestAddrbooks = None
        self.DestZones = None
        self.DestHost = None
        self.DestHostbook = None
        self.ServiceType = None
        self.ServiceInfos = None
        self.ServiceGroups = None
        self.AppType = None
        self.AppValue = None
        self.Policy = None
        self.Status = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("AclId"):
            self.AclId = params.get("AclId")
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("AclName"):
            self.AclName = params.get("AclName")
        if params.get("Direction"):
            self.Direction = params.get("Direction")
        if params.get("SrcType"):
            self.SrcType = params.get("SrcType")
        if params.get("SrcIps"):
            self.SrcIps = params.get("SrcIps")
        if params.get("SrcAddrbooks"):
            self.SrcAddrbooks = params.get("SrcAddrbooks")
        if params.get("SrcZones"):
            self.SrcZones = params.get("SrcZones")
        if params.get("DestType"):
            self.DestType = params.get("DestType")
        if params.get("DestIps"):
            self.DestIps = params.get("DestIps")
        if params.get("DestAddrbooks"):
            self.DestAddrbooks = params.get("DestAddrbooks")
        if params.get("DestZones"):
            self.DestZones = params.get("DestZones")
        if params.get("DestHost"):
            self.DestHost = params.get("DestHost")
        if params.get("DestHostbook"):
            self.DestHostbook = params.get("DestHostbook")
        if params.get("ServiceType"):
            self.ServiceType = params.get("ServiceType")
        if params.get("ServiceInfos"):
            self.ServiceInfos = params.get("ServiceInfos")
        if params.get("ServiceGroups"):
            self.ServiceGroups = params.get("ServiceGroups")
        if params.get("AppType"):
            self.AppType = params.get("AppType")
        if params.get("AppValue"):
            self.AppValue = params.get("AppValue")
        if params.get("Policy"):
            self.Policy = params.get("Policy")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("Description"):
            self.Description = params.get("Description")


class DescribeCfwAclRequest(AbstractModel):
    """DescribeCfwAcl请求参数结构体
    """

    def __init__(self):
        r"""查询ACL
        :param CfwInstanceId: 云防火墙id
        :type PathPrefix: String
        :param AclIds: 访问控制id集合
        :type PathPrefix: Array
        :param MaxResults: 5到1000
        :type PathPrefix: Int
        :param NextToken: 下一页token
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.AclIds = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("AclIds"):
            self.AclIds = params.get("AclIds")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateCfwAclRequest(AbstractModel):
    """CreateCfwAcl请求参数结构体
    """

    def __init__(self):
        r"""创建ACL
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param AclName: 访问控制名称
        :type PathPrefix: String
        :param Direction: 出入向(入向：in, 出向：out)
        :type PathPrefix: String
        :param SrcType: 源地址类型(IP：ip|地址簿：addrbook|地域：zone|Any：any)
        :type PathPrefix: String
        :param SrcIps: 源ip，当SrcType为ip时必填
仅支持填写公网IPv4地址，支持IP地址段、IP地址范围。格式为：10.1.1.1/32,10.1.1.2/24,192.168.1.1-192.168.1.63"
1、地址段：可输入多个IP+掩码，中间通过英文逗号“,”隔开如192.168.1.1/32,110.1.1.1/24。
2、地址范围：多个连续的IP地址，中间通过"-"隔开如192.168.1.1-192.168.1.253
        :type PathPrefix: Array
        :param SrcAddrbooks: 地址簿id集合，当SrcType为addrbook时必填
        :type PathPrefix: Array
        :param SrcZones: 源地址地域，当SrcType为zone时必填，示例[{"areaCode":"CN_HB","areaName":"湖北省"}]
        :type PathPrefix: Array
        :param DestType: 目的类型：（IP：ip，地址簿：addrbook，地域：zone，域名簿：hostbook，域名：host，Any：any）
        :type PathPrefix: String
        :param DestIps: 目的ip，当DestType为ip时必填
仅支持填写公网IPv4地址，支持IP地址段、IP地址范围。通过英文",“隔开，格式为：10.1.1.1/32,10.1.1.2/24,192.168.1.1-192.168.1.63”
1、地址段：可输入多个IP+掩码，中间通过英文逗号“,”隔开如192.168.1.1/32,110.1.1.1/24。
2、地址范围：多个连续的IP地址，中间通过"-"隔开如192.168.1.1–192.168.1.253
        :type PathPrefix: Array
        :param DestAddrbooks: 目的地址簿id集合，当DestType为addrbook时必填
        :type PathPrefix: Array
        :param DestZones: 目的地址地域，当DestType为zone时必填，示例[{“areaCode”:“CN_HB”,“areaName”:“湖北省”}]
        :type PathPrefix: Array
        :param DestHost: 域名，目前只允许传一个域名，泛域名示例*.ksyun.con，完整域名示例uss.ksyun.com
        :type PathPrefix: Array
        :param DestHostbook: 域名簿id集合，目前只允许传一个

        :type PathPrefix: Array
        :param ServiceType: 服务类型，服务：service，服务组：servicegroup，Any：any
        :type PathPrefix: String
        :param ServiceInfos: 服务信息，ServiceType为service时必填，（协议:源端口最小-源端口最大/目的最小-目的最大 ）例：TCP:1-100/2-200,UDP:22/33,ICMP
        :type PathPrefix: Array
        :param ServiceGroups: 服务组id集合，ServiceType为servicegroup时必填
        :type PathPrefix: Array
        :param AppType: app|any
        :type PathPrefix: String
        :param AppValue: AppType为app时必填，TCP支持的应用集合("HTTP", "HTTPS", "SMTP", "SMTPS", "IMAP4", "MYSQL","POP3", "POP3S", "SSH", "TLS1", "VNC", "DNS", "RDP"),UDP支持的应用集合("DNS", "RDP"),ICMP只能填any
        :type PathPrefix: Array
        :param Policy: 动作，允许：accept，拒绝：deny
        :type PathPrefix: String
        :param Status: 开启：start，关闭：stop
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        :param PriorityPosition: 优先级(after/before优先级)
before为置顶，after为置底
after+优先级 表示设置为该优先级+1 且之后的规则所有优先级都+1
before优先级 表示设置为该优先级 原优先级规则及其之后所有规则优先级都+1
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.AclName = None
        self.Direction = None
        self.SrcType = None
        self.SrcIps = None
        self.SrcAddrbooks = None
        self.SrcZones = None
        self.DestType = None
        self.DestIps = None
        self.DestAddrbooks = None
        self.DestZones = None
        self.DestHost = None
        self.DestHostbook = None
        self.ServiceType = None
        self.ServiceInfos = None
        self.ServiceGroups = None
        self.AppType = None
        self.AppValue = None
        self.Policy = None
        self.Status = None
        self.Description = None
        self.PriorityPosition = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("AclName"):
            self.AclName = params.get("AclName")
        if params.get("Direction"):
            self.Direction = params.get("Direction")
        if params.get("SrcType"):
            self.SrcType = params.get("SrcType")
        if params.get("SrcIps"):
            self.SrcIps = params.get("SrcIps")
        if params.get("SrcAddrbooks"):
            self.SrcAddrbooks = params.get("SrcAddrbooks")
        if params.get("SrcZones"):
            self.SrcZones = params.get("SrcZones")
        if params.get("DestType"):
            self.DestType = params.get("DestType")
        if params.get("DestIps"):
            self.DestIps = params.get("DestIps")
        if params.get("DestAddrbooks"):
            self.DestAddrbooks = params.get("DestAddrbooks")
        if params.get("DestZones"):
            self.DestZones = params.get("DestZones")
        if params.get("DestHost"):
            self.DestHost = params.get("DestHost")
        if params.get("DestHostbook"):
            self.DestHostbook = params.get("DestHostbook")
        if params.get("ServiceType"):
            self.ServiceType = params.get("ServiceType")
        if params.get("ServiceInfos"):
            self.ServiceInfos = params.get("ServiceInfos")
        if params.get("ServiceGroups"):
            self.ServiceGroups = params.get("ServiceGroups")
        if params.get("AppType"):
            self.AppType = params.get("AppType")
        if params.get("AppValue"):
            self.AppValue = params.get("AppValue")
        if params.get("Policy"):
            self.Policy = params.get("Policy")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("PriorityPosition"):
            self.PriorityPosition = params.get("PriorityPosition")


class ModifyCfwEipProtectRequest(AbstractModel):
    """ModifyCfwEipProtect请求参数结构体
    """

    def __init__(self):
        r"""Eip开启/关闭防护
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param EipIds: eip的主键id集合
        :type PathPrefix: Array
        :param EipProtectStatus: 防护状态(start|stop)
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.EipIds = None
        self.EipProtectStatus = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("EipIds"):
            self.EipIds = params.get("EipIds")
        if params.get("EipProtectStatus"):
            self.EipProtectStatus = params.get("EipProtectStatus")


class DescribeCfwEipsRequest(AbstractModel):
    """DescribeCfwEips请求参数结构体
    """

    def __init__(self):
        r"""查询EIP
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param MaxResults: 查询数量最大1000
        :type PathPrefix: Int
        :param NextToken: 下一页token
        :type PathPrefix: String
        :param EipAddress: 要查询的ip
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.MaxResults = None
        self.NextToken = None
        self.EipAddress = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("EipAddress"):
            self.EipAddress = params.get("EipAddress")


class DescribeServiceGroupRequest(AbstractModel):
    """DescribeServiceGroup请求参数结构体
    """

    def __init__(self):
        r"""查询服务组
        :param CfwInstanceId: 防火墙id
        :type PathPrefix: String
        :param ServiceGroupIds: 服务组id集合
        :type PathPrefix: Array
        """
        self.CfwInstanceId = None
        self.ServiceGroupIds = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("ServiceGroupIds"):
            self.ServiceGroupIds = params.get("ServiceGroupIds")


class ModifyCfwServiceGroupRequest(AbstractModel):
    """ModifyCfwServiceGroup请求参数结构体
    """

    def __init__(self):
        r"""修改服务组
        :param ServiceGroupId: 服务组id
        :type PathPrefix: String
        :param ServiceGroupName: 服务组名称
        :type PathPrefix: String
        :param ServiceInfo: 服务信息（协议:源端口最小-源端口最大/目的最小-目的最大 ）
例：TCP:1-100/2-200,UDP:22/33,ICMP
        :type PathPrefix: Array
        :param Description: 描述
        :type PathPrefix: String
        """
        self.ServiceGroupId = None
        self.ServiceGroupName = None
        self.ServiceInfo = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("ServiceGroupId"):
            self.ServiceGroupId = params.get("ServiceGroupId")
        if params.get("ServiceGroupName"):
            self.ServiceGroupName = params.get("ServiceGroupName")
        if params.get("ServiceInfo"):
            self.ServiceInfo = params.get("ServiceInfo")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteCfwServiceGroupRequest(AbstractModel):
    """DeleteCfwServiceGroup请求参数结构体
    """

    def __init__(self):
        r"""删除服务组
        :param ServiceGroupId: 服务组id
        :type PathPrefix: String
        """
        self.ServiceGroupId = None

    def _deserialize(self, params):
        if params.get("ServiceGroupId"):
            self.ServiceGroupId = params.get("ServiceGroupId")


class CreateCfwServiceGroupRequest(AbstractModel):
    """CreateCfwServiceGroup请求参数结构体
    """

    def __init__(self):
        r"""创建服务组
        :param CfwInstanceId: 云防火墙id
        :type PathPrefix: String
        :param ServiceGroupName: 服务组名称
        :type PathPrefix: String
        :param ServiceInfo: 服务信息（最多添加64个）服务信息（协议:源端口最小-源端口最大/目的最小-目的最大 ）
例：TCP:1-100/2-200,UDP:22/33,ICMP

        :type PathPrefix: Array
        :param Description: 描述
        :type PathPrefix: String
        """
        self.CfwInstanceId = None
        self.ServiceGroupName = None
        self.ServiceInfo = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("CfwInstanceId"):
            self.CfwInstanceId = params.get("CfwInstanceId")
        if params.get("ServiceGroupName"):
            self.ServiceGroupName = params.get("ServiceGroupName")
        if params.get("ServiceInfo"):
            self.ServiceInfo = params.get("ServiceInfo")
        if params.get("Description"):
            self.Description = params.get("Description")


class DescribeCloudFireWallInstanceRequest(AbstractModel):
    """DescribeCloudFireWallInstance请求参数结构体
    """

    def __init__(self):
        r"""查询防火墙
        :param CfwInstanceIds: 防火墙主键id
        :type PathPrefix: Array
        """
        self.CfwInstanceIds = None

    def _deserialize(self, params):
        if params.get("CfwInstanceIds"):
            self.CfwInstanceIds = params.get("CfwInstanceIds")
