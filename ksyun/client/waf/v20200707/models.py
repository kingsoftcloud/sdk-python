from ksyun.common.abstract_model import AbstractModel


class CreateDomainRequest(AbstractModel):
    """CreateDomain请求参数结构体
    """

    def __init__(self):
        r"""创建域名（3.0）
        :param ResourceRecord: 描述：域名记录
        :type PathPrefix: String
        :param HttpRewrite: 描述：https强制跳转开启状态
        :type PathPrefix: Boolean
        :param HttpSource: 描述：http回源开启状态
        :type PathPrefix: Boolean
        :param CertificateId: 描述：域名使用证书的ID
        :type PathPrefix: String
        :param CertificateRegion: 描述：域名使用证书的region
        :type PathPrefix: String
        :param LbMethod: 描述：负载均衡方式
        :type PathPrefix: String
        :param HasProxy: 描述：前置代理设置状态
        :type PathPrefix: Boolean
        :param ProjectId: 描述：域名所属项目的ID
        :type PathPrefix: Int
        :param HeaderMark: 描述：域名流量标记header字段名称
        :type PathPrefix: String
        :param HeaderValue: 描述：域名流量标记header字段值
        :type PathPrefix: String
        :param HealthMonitor: 描述：健康检测
        :type PathPrefix: String
        :param HttpPort: 描述：http协议端口列表
        :type PathPrefix: Filter
        :param HttpsPort: 描述：https协议端口列表
        :type PathPrefix: Filter
        :param Sources: 描述：域名回源信息列表
        :type PathPrefix: String
        """
        self.ResourceRecord = None
        self.HttpRewrite = None
        self.HttpSource = None
        self.CertificateId = None
        self.CertificateRegion = None
        self.LbMethod = None
        self.HasProxy = None
        self.ProjectId = None
        self.HeaderMark = None
        self.HeaderValue = None
        self.HealthMonitor = None
        self.HttpPort = None
        self.HttpsPort = None
        self.Sources = None

    def _deserialize(self, params):
        if params.get("ResourceRecord"):
            self.ResourceRecord = params.get("ResourceRecord")
        if params.get("HttpRewrite"):
            self.HttpRewrite = params.get("HttpRewrite")
        if params.get("HttpSource"):
            self.HttpSource = params.get("HttpSource")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("CertificateRegion"):
            self.CertificateRegion = params.get("CertificateRegion")
        if params.get("LbMethod"):
            self.LbMethod = params.get("LbMethod")
        if params.get("HasProxy"):
            self.HasProxy = params.get("HasProxy")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("HeaderMark"):
            self.HeaderMark = params.get("HeaderMark")
        if params.get("HeaderValue"):
            self.HeaderValue = params.get("HeaderValue")
        if params.get("HealthMonitor"):
            self.HealthMonitor = params.get("HealthMonitor")
        if params.get("HttpPort"):
            self.HttpPort = params.get("HttpPort")
        if params.get("HttpsPort"):
            self.HttpsPort = params.get("HttpsPort")
        if params.get("Sources"):
            self.Sources = params.get("Sources")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体
    """

    def __init__(self):
        r"""描述域名（3.0）
        :param ResourceRecord: 
        :type PathPrefix: String
        """
        self.ResourceRecord = None

    def _deserialize(self, params):
        if params.get("ResourceRecord"):
            self.ResourceRecord = params.get("ResourceRecord")


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain请求参数结构体
    """

    def __init__(self):
        r"""修改域名（3.0）
        :param ResourceRecordId: 描述：域名记录的ID
        :type PathPrefix: String
        :param HttpRewrite: 描述：https强制跳转开启状态
        :type PathPrefix: Boolean
        :param HttpSource: 描述：http回源开启状态
        :type PathPrefix: Boolean
        :param CertificateId: 描述：域名使用证书的id
        :type PathPrefix: String
        :param CertificateRegion: 描述：域名使用证书的region
        :type PathPrefix: String
        :param LbMethod: 描述：负载均衡方式
        :type PathPrefix: String
        :param HasProxy: 描述：前置代理设置状态
        :type PathPrefix: Boolean
        :param ProjectId: 描述：域名所属项目的ID
        :type PathPrefix: Int
        :param HeaderMark: 描述：域名流量标记header字段名称
        :type PathPrefix: String
        :param HeaderValue: 描述：域名流量标记header字段值
        :type PathPrefix: String
        :param HealthMonitor: 描述：健康检测
        :type PathPrefix: String
        :param HttpPort: 描述：http协议端口列表
        :type PathPrefix: Filter
        :param HttpsPort: 描述：https协议端口列表
        :type PathPrefix: Filter
        :param Sources: 描述：域名回源信息列表
        :type PathPrefix: String
        """
        self.ResourceRecordId = None
        self.HttpRewrite = None
        self.HttpSource = None
        self.CertificateId = None
        self.CertificateRegion = None
        self.LbMethod = None
        self.HasProxy = None
        self.ProjectId = None
        self.HeaderMark = None
        self.HeaderValue = None
        self.HealthMonitor = None
        self.HttpPort = None
        self.HttpsPort = None
        self.Sources = None

    def _deserialize(self, params):
        if params.get("ResourceRecordId"):
            self.ResourceRecordId = params.get("ResourceRecordId")
        if params.get("HttpRewrite"):
            self.HttpRewrite = params.get("HttpRewrite")
        if params.get("HttpSource"):
            self.HttpSource = params.get("HttpSource")
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("CertificateRegion"):
            self.CertificateRegion = params.get("CertificateRegion")
        if params.get("LbMethod"):
            self.LbMethod = params.get("LbMethod")
        if params.get("HasProxy"):
            self.HasProxy = params.get("HasProxy")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("HeaderMark"):
            self.HeaderMark = params.get("HeaderMark")
        if params.get("HeaderValue"):
            self.HeaderValue = params.get("HeaderValue")
        if params.get("HealthMonitor"):
            self.HealthMonitor = params.get("HealthMonitor")
        if params.get("HttpPort"):
            self.HttpPort = params.get("HttpPort")
        if params.get("HttpsPort"):
            self.HttpsPort = params.get("HttpsPort")
        if params.get("Sources"):
            self.Sources = params.get("Sources")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体
    """

    def __init__(self):
        r"""删除域名（3.0）
        :param ResourceRecordId: 描述：域名记录的ID
        :type PathPrefix: String
        """
        self.ResourceRecordId = None

    def _deserialize(self, params):
        if params.get("ResourceRecordId"):
            self.ResourceRecordId = params.get("ResourceRecordId")


class CreateAccessControlRuleRequest(AbstractModel):
    """CreateAccessControlRule请求参数结构体
    """

    def __init__(self):
        r"""创建访问控制规则（3.0）
        :param ResourceRecordId: 描述：域名记录ID
        :type PathPrefix: String
        :param RuleName: 描述：防护规则名称
        :type PathPrefix: String
        :param RuleType: 描述：规则匹配字段
        :type PathPrefix: String
        :param ArgName: 描述：参数名
        :type PathPrefix: String
        :param RuleData: 描述：防护规则数据
        :type PathPrefix: String
        :param MatchRule: 描述：匹配条件
        :type PathPrefix: Int
        :param Level: 描述：风险等级
        :type PathPrefix: Int
        :param RuleAction: 描述：防护动作
        :type PathPrefix: Int
        :param Status: 描述：规则开启状态
        :type PathPrefix: Boolean
        """
        self.ResourceRecordId = None
        self.RuleName = None
        self.RuleType = None
        self.ArgName = None
        self.RuleData = None
        self.MatchRule = None
        self.Level = None
        self.RuleAction = None
        self.Status = None

    def _deserialize(self, params):
        if params.get("ResourceRecordId"):
            self.ResourceRecordId = params.get("ResourceRecordId")
        if params.get("RuleName"):
            self.RuleName = params.get("RuleName")
        if params.get("RuleType"):
            self.RuleType = params.get("RuleType")
        if params.get("ArgName"):
            self.ArgName = params.get("ArgName")
        if params.get("RuleData"):
            self.RuleData = params.get("RuleData")
        if params.get("MatchRule"):
            self.MatchRule = params.get("MatchRule")
        if params.get("Level"):
            self.Level = params.get("Level")
        if params.get("RuleAction"):
            self.RuleAction = params.get("RuleAction")
        if params.get("Status"):
            self.Status = params.get("Status")


class DescribeAccessControlRulesRequest(AbstractModel):
    """DescribeAccessControlRules请求参数结构体
    """

    def __init__(self):
        r"""描述访问控制规则（3.0）
        :param RuleId: 描述：防护规则ID
        :type PathPrefix: String
        :param ResourceRecordId: 描述：防护域名ID
        :type PathPrefix: String
        :param RuleName: 描述：防护规则名称
        :type PathPrefix: String
        """
        self.RuleId = None
        self.ResourceRecordId = None
        self.RuleName = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("ResourceRecordId"):
            self.ResourceRecordId = params.get("ResourceRecordId")
        if params.get("RuleName"):
            self.RuleName = params.get("RuleName")


class ModifyAccessControlRuleRequest(AbstractModel):
    """ModifyAccessControlRule请求参数结构体
    """

    def __init__(self):
        r"""修改访问控制规则（3.0）
        :param RuleId: 描述：防护规则ID
        :type PathPrefix: String
        :param RuleName: 描述：防护规则名称
        :type PathPrefix: String
        :param RuleType: 描述：规则匹配字段
        :type PathPrefix: String
        :param RuleData: 描述：防护规则数据
        :type PathPrefix: String
        :param MatchRule: 描述：匹配条件
        :type PathPrefix: String
        :param ArgName: 描述：参数名
        :type PathPrefix: String
        :param Level: 描述：风险等级
        :type PathPrefix: Int
        :param RuleAction: 描述：防护动作
        :type PathPrefix: Int
        :param Status: 规则开启状态
        :type PathPrefix: Boolean
        """
        self.RuleId = None
        self.RuleName = None
        self.RuleType = None
        self.RuleData = None
        self.MatchRule = None
        self.ArgName = None
        self.Level = None
        self.RuleAction = None
        self.Status = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("RuleName"):
            self.RuleName = params.get("RuleName")
        if params.get("RuleType"):
            self.RuleType = params.get("RuleType")
        if params.get("RuleData"):
            self.RuleData = params.get("RuleData")
        if params.get("MatchRule"):
            self.MatchRule = params.get("MatchRule")
        if params.get("ArgName"):
            self.ArgName = params.get("ArgName")
        if params.get("Level"):
            self.Level = params.get("Level")
        if params.get("RuleAction"):
            self.RuleAction = params.get("RuleAction")
        if params.get("Status"):
            self.Status = params.get("Status")


class DeleteAccessControlRuleRequest(AbstractModel):
    """DeleteAccessControlRule请求参数结构体
    """

    def __init__(self):
        r"""删除访问控制规则（3.0）
        :param RuleId: 描述：防护规则ID
        :type PathPrefix: String
        """
        self.RuleId = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates请求参数结构体
    """

    def __init__(self):
        r"""描述证书信息（3.0）
        :param Request: rs（请求参数）
        :type PathPrefix: String
        """
        self.Request = None

    def _deserialize(self, params):
        if params.get("Request"):
            self.Request = params.get("Request")


class CreateIpv6ProtectionRequest(AbstractModel):
    """CreateIpv6Protection请求参数结构体
    """

    def __init__(self):
        r"""开启IPv6防护（3.0）
        :param ResourceRecordId: 
        :type PathPrefix: Array
        """
        self.ResourceRecordId = None

    def _deserialize(self, params):
        if params.get("ResourceRecordId"):
            self.ResourceRecordId = params.get("ResourceRecordId")


class DeleteIpv6ProtectionRequest(AbstractModel):
    """DeleteIpv6Protection请求参数结构体
    """

    def __init__(self):
        r"""关闭IPv6防护（3.0）
        :param ResourceRecordId: 
        :type PathPrefix: Array
        """
        self.ResourceRecordId = None

    def _deserialize(self, params):
        if params.get("ResourceRecordId"):
            self.ResourceRecordId = params.get("ResourceRecordId")
