from ksyun.common.abstract_model import AbstractModel

class CreateVpcRequest(AbstractModel):
    """CreateVpc请求参数结构体
    """

    def __init__(self):
        r"""创建Vpc
        :param VpcName: Vpc的名称
        :type PathPrefix: String
        :param CidrBlock: Vpc的网络范围，例如：10.0.0.0/16
        :type PathPrefix: String
        :param ProvidedIpv6CidrBlock: 是否支持IPv6网段，目前只支持部分机房
        :type PathPrefix: Boolean
        """
        self.VpcName = None
        self.CidrBlock = None
        self.ProvidedIpv6CidrBlock = None

    def _deserialize(self, params):
        if params.get("VpcName"):
            self.VpcName = params.get("VpcName")
        if params.get("CidrBlock"):
            self.CidrBlock = params.get("CidrBlock")
        if params.get("ProvidedIpv6CidrBlock"):
            self.ProvidedIpv6CidrBlock = params.get("ProvidedIpv6CidrBlock")


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc请求参数结构体
    """

    def __init__(self):
        r"""删除Vpc
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        """
        self.VpcId = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs请求参数结构体
    """

    def __init__(self):
        r"""描述Vpc
        :param VpcId: 多个Vpc的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.VpcId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet请求参数结构体
    """

    def __init__(self):
        r"""创建子网
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param SubnetName: 子网的名称
        :type PathPrefix: String
        :param CidrBlock: 子网的网络范围，例如：10.0.0.0/24
        :type PathPrefix: String
        :param ProvidedIpv6CidrBlock: 是否支持IPv6网段，目前只支持部分机房
        :type PathPrefix: Boolean
        :param SubnetType: 子网的类型，终端子网（Reserve）、云服务器子网（Normal）、裸金属服务器子网（Physical）
        :type PathPrefix: String
        :param DhcpIpFrom: DHCP起始IP
        :type PathPrefix: String
        :param DhcpIpTo: DHCP结束IP
        :type PathPrefix: String
        :param Dns1: 子网的Dns1
        :type PathPrefix: String
        :param Dns2: 子网的Dns2
        :type PathPrefix: String
        :param GatewayIp: 网关的IP，当SubnetType为Normal或Physical不能为空
        :type PathPrefix: String
        :param SecondaryCidrId: 当子网的网络范围在附加网段内，需要输入附加网段ID
        :type PathPrefix: String
        :param AvailabilityZone: 可用区的名称，默认在可用区A创建，例如：cn-beijing-6a
        :type PathPrefix: String
        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.ProvidedIpv6CidrBlock = None
        self.SubnetType = None
        self.DhcpIpFrom = None
        self.DhcpIpTo = None
        self.Dns1 = None
        self.Dns2 = None
        self.GatewayIp = None
        self.SecondaryCidrId = None
        self.AvailabilityZone = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetName"):
            self.SubnetName = params.get("SubnetName")
        if params.get("CidrBlock"):
            self.CidrBlock = params.get("CidrBlock")
        if params.get("ProvidedIpv6CidrBlock"):
            self.ProvidedIpv6CidrBlock = params.get("ProvidedIpv6CidrBlock")
        if params.get("SubnetType"):
            self.SubnetType = params.get("SubnetType")
        if params.get("DhcpIpFrom"):
            self.DhcpIpFrom = params.get("DhcpIpFrom")
        if params.get("DhcpIpTo"):
            self.DhcpIpTo = params.get("DhcpIpTo")
        if params.get("Dns1"):
            self.Dns1 = params.get("Dns1")
        if params.get("Dns2"):
            self.Dns2 = params.get("Dns2")
        if params.get("GatewayIp"):
            self.GatewayIp = params.get("GatewayIp")
        if params.get("SecondaryCidrId"):
            self.SecondaryCidrId = params.get("SecondaryCidrId")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet请求参数结构体
    """

    def __init__(self):
        r"""删除子网
        :param SubnetId: 子网的ID
        :type PathPrefix: String
        """
        self.SubnetId = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets请求参数结构体
    """

    def __init__(self):
        r"""描述子网
        :param SubnetId: 多个子网的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.SubnetId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class AssociateNetworkAclRequest(AbstractModel):
    """AssociateNetworkAcl请求参数结构体
    """

    def __init__(self):
        r"""关联ACL
        :param SubnetId: 子网的ID
        :type PathPrefix: String
        :param NetworkAclId: ACL的ID
        :type PathPrefix: String
        """
        self.SubnetId = None
        self.NetworkAclId = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("NetworkAclId"):
            self.NetworkAclId = params.get("NetworkAclId")


class DisassociateNetworkAclRequest(AbstractModel):
    """DisassociateNetworkAcl请求参数结构体
    """

    def __init__(self):
        r"""解绑ACL
        :param SubnetId: 子网的ID
        :type PathPrefix: String
        :param NetworkAclId: ACL的ID
        :type PathPrefix: String
        """
        self.SubnetId = None
        self.NetworkAclId = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("NetworkAclId"):
            self.NetworkAclId = params.get("NetworkAclId")


class CreateRouteRequest(AbstractModel):
    """CreateRoute请求参数结构体
    """

    def __init__(self):
        r"""创建路由
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param RouteType: 路由的类型
        :type PathPrefix: String
        :param DestinationCidrBlock: 目标网段
        :type PathPrefix: String
        :param InstanceId: 云服务器的ID，只有主机路由需要填写此参数
        :type PathPrefix: String
        :param VpcPeeringConnectionId: 对等连接ID
        :type PathPrefix: String
        :param DirectConnectGatewayId: 专线网关的ID
        :type PathPrefix: String
        :param VpnTunnelId: VPN通道的ID
        :type PathPrefix: String
        :param NetworkInterfaceId: 网卡ID
        :type PathPrefix: String
        """
        self.VpcId = None
        self.RouteType = None
        self.DestinationCidrBlock = None
        self.InstanceId = None
        self.VpcPeeringConnectionId = None
        self.DirectConnectGatewayId = None
        self.VpnTunnelId = None
        self.NetworkInterfaceId = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("RouteType"):
            self.RouteType = params.get("RouteType")
        if params.get("DestinationCidrBlock"):
            self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("VpcPeeringConnectionId"):
            self.VpcPeeringConnectionId = params.get("VpcPeeringConnectionId")
        if params.get("DirectConnectGatewayId"):
            self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("VpnTunnelId"):
            self.VpnTunnelId = params.get("VpnTunnelId")
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")


class DeleteRouteRequest(AbstractModel):
    """DeleteRoute请求参数结构体
    """

    def __init__(self):
        r"""删除路由
        :param RouteId: 路由的ID
        :type PathPrefix: String
        """
        self.RouteId = None

    def _deserialize(self, params):
        if params.get("RouteId"):
            self.RouteId = params.get("RouteId")


class DescribeRoutesRequest(AbstractModel):
    """DescribeRoutes请求参数结构体
    """

    def __init__(self):
        r"""描述路由
        :param RouteId: 多个路由的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.RouteId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("RouteId"):
            self.RouteId = params.get("RouteId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateNetworkAclRequest(AbstractModel):
    """CreateNetworkAcl请求参数结构体
    """

    def __init__(self):
        r"""创建ACL
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param NetworkAclName: ACL的名称
        :type PathPrefix: String
        :param Description: ACL的描述
        :type PathPrefix: String
        """
        self.VpcId = None
        self.NetworkAclName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("NetworkAclName"):
            self.NetworkAclName = params.get("NetworkAclName")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteNetworkAclRequest(AbstractModel):
    """DeleteNetworkAcl请求参数结构体
    """

    def __init__(self):
        r"""删除ACL
        :param NetworkAclId: ACL的ID
        :type PathPrefix: String
        """
        self.NetworkAclId = None

    def _deserialize(self, params):
        if params.get("NetworkAclId"):
            self.NetworkAclId = params.get("NetworkAclId")


class CreateNetworkAclEntryRequest(AbstractModel):
    """CreateNetworkAclEntry请求参数结构体
    """

    def __init__(self):
        r"""创建ACL规则
        :param NetworkAclId: ACL的ID
        :type PathPrefix: String
        :param Direction: ACL规则方向，in为入站规则，out为出站规则
        :type PathPrefix: String
        :param RuleNumber: ACL规则优先级，数字越小优先级越高，不可重复
        :type PathPrefix: Int
        :param Protocol: 协议(udp|tcp|ip|icmp)，IP代表所有协议
        :type PathPrefix: String
        :param IcmpType: ICMP协议，ICMP类型，只有协议为ICMP类型，才必填
        :type PathPrefix: Int
        :param IcmpCode: ICMP协议，ICMP代码，只有协议为ICMP类型，才必填
        :type PathPrefix: Int
        :param RuleAction: ACL规则行为，allow为允许，deny为拒绝
        :type PathPrefix: String
        :param PortRangeFrom: TCP或UDP协议的端口规则起始端口
        :type PathPrefix: Int
        :param PortRangeTo: TCP或UDP协议的端口规则结束端口
        :type PathPrefix: Int
        :param CidrBlock: ACL规则的网段
        :type PathPrefix: String
        :param Description: ACL的描述
        :type PathPrefix: String
        """
        self.NetworkAclId = None
        self.Direction = None
        self.RuleNumber = None
        self.Protocol = None
        self.IcmpType = None
        self.IcmpCode = None
        self.RuleAction = None
        self.PortRangeFrom = None
        self.PortRangeTo = None
        self.CidrBlock = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("NetworkAclId"):
            self.NetworkAclId = params.get("NetworkAclId")
        if params.get("Direction"):
            self.Direction = params.get("Direction")
        if params.get("RuleNumber"):
            self.RuleNumber = params.get("RuleNumber")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("IcmpType"):
            self.IcmpType = params.get("IcmpType")
        if params.get("IcmpCode"):
            self.IcmpCode = params.get("IcmpCode")
        if params.get("RuleAction"):
            self.RuleAction = params.get("RuleAction")
        if params.get("PortRangeFrom"):
            self.PortRangeFrom = params.get("PortRangeFrom")
        if params.get("PortRangeTo"):
            self.PortRangeTo = params.get("PortRangeTo")
        if params.get("CidrBlock"):
            self.CidrBlock = params.get("CidrBlock")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteNetworkAclEntryRequest(AbstractModel):
    """DeleteNetworkAclEntry请求参数结构体
    """

    def __init__(self):
        r"""删除ACLl规则
        :param NetworkAclId: ACL的ID
        :type PathPrefix: String
        :param NetworkAclEntryId: ACL规则的ID
        :type PathPrefix: String
        """
        self.NetworkAclId = None
        self.NetworkAclEntryId = None

    def _deserialize(self, params):
        if params.get("NetworkAclId"):
            self.NetworkAclId = params.get("NetworkAclId")
        if params.get("NetworkAclEntryId"):
            self.NetworkAclEntryId = params.get("NetworkAclEntryId")


class DescribeNetworkAclsRequest(AbstractModel):
    """DescribeNetworkAcls请求参数结构体
    """

    def __init__(self):
        r"""描述ACL
        :param NetworkAclId: 多个ACL的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.NetworkAclId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("NetworkAclId"):
            self.NetworkAclId = params.get("NetworkAclId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""创建安全组
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param SecurityGroupName: 安全组的名称
        :type PathPrefix: String
        :param Description: 安全组的描述
        :type PathPrefix: String
        """
        self.VpcId = None
        self.SecurityGroupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""删除安全组
        :param SecurityGroupId: 安全组的ID
        :type PathPrefix: String
        """
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class AuthorizeSecurityGroupEntryRequest(AbstractModel):
    """AuthorizeSecurityGroupEntry请求参数结构体
    """

    def __init__(self):
        r"""创建安全组规则
        :param Description: 安全组规则的描述
        :type PathPrefix: String
        :param SecurityGroupId: 安全组的ID
        :type PathPrefix: String
        :param CidrBlock: 安全组规则的网段
        :type PathPrefix: String
        :param Direction: 安全组规则方向，in为入站规则，out为出站规则
        :type PathPrefix: String
        :param Protocol: 协议，IP代表所有协议
        :type PathPrefix: String
        :param IcmpType: ICMP协议，ICMP类型，只有协议为ICMP类型，才必填
        :type PathPrefix: Int
        :param IcmpCode: ICMP协议，ICMP代码，只有协议为ICMP类型，才必填
        :type PathPrefix: Int
        :param PortRangeFrom: TCP或UDP协议的端口规则起始端口
        :type PathPrefix: Int
        :param PortRangeTo: TCP或UDP协议的端口规则结束端口
        :type PathPrefix: Int
        :param RuleTag: 安全组规则标签
        :type PathPrefix: String
        """
        self.Description = None
        self.SecurityGroupId = None
        self.CidrBlock = None
        self.Direction = None
        self.Protocol = None
        self.IcmpType = None
        self.IcmpCode = None
        self.PortRangeFrom = None
        self.PortRangeTo = None
        self.RuleTag = None

    def _deserialize(self, params):
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("CidrBlock"):
            self.CidrBlock = params.get("CidrBlock")
        if params.get("Direction"):
            self.Direction = params.get("Direction")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("IcmpType"):
            self.IcmpType = params.get("IcmpType")
        if params.get("IcmpCode"):
            self.IcmpCode = params.get("IcmpCode")
        if params.get("PortRangeFrom"):
            self.PortRangeFrom = params.get("PortRangeFrom")
        if params.get("PortRangeTo"):
            self.PortRangeTo = params.get("PortRangeTo")
        if params.get("RuleTag"):
            self.RuleTag = params.get("RuleTag")


class RevokeSecurityGroupEntryRequest(AbstractModel):
    """RevokeSecurityGroupEntry请求参数结构体
    """

    def __init__(self):
        r"""删除安全组规则
        :param SecurityGroupId: 安全组的ID
        :type PathPrefix: String
        :param SecurityGroupEntryId: 安全组规则的ID
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupEntryId = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupEntryId"):
            self.SecurityGroupEntryId = params.get("SecurityGroupEntryId")


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups请求参数结构体
    """

    def __init__(self):
        r"""描述安全组
        :param SecurityGroupId: 多个安全组的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateNatRequest(AbstractModel):
    """CreateNat请求参数结构体
    """

    def __init__(self):
        r"""创建Nat
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param NatLineId: Nat的线路ID
        :type PathPrefix: String
        :param BandWidth: Nat的带宽
        :type PathPrefix: Int
        :param NatName: Nat的名称
        :type PathPrefix: String
        :param NatType: Nat的类型，目前只支持public
        :type PathPrefix: String
        :param NatIpNumber: Nat的IP数量
        :type PathPrefix: Int
        :param NatMode: Nat的映射范围
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: Nat的计费类型
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月时不可缺省。
        :type PathPrefix: Int
        """
        self.VpcId = None
        self.NatLineId = None
        self.BandWidth = None
        self.NatName = None
        self.NatType = None
        self.NatIpNumber = None
        self.NatMode = None
        self.ProjectId = None
        self.ChargeType = None
        self.PurchaseTime = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("NatLineId"):
            self.NatLineId = params.get("NatLineId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")
        if params.get("NatName"):
            self.NatName = params.get("NatName")
        if params.get("NatType"):
            self.NatType = params.get("NatType")
        if params.get("NatIpNumber"):
            self.NatIpNumber = params.get("NatIpNumber")
        if params.get("NatMode"):
            self.NatMode = params.get("NatMode")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")


class DeleteNatRequest(AbstractModel):
    """DeleteNat请求参数结构体
    """

    def __init__(self):
        r"""删除Nat
        :param NatId: Nat的ID
        :type PathPrefix: String
        """
        self.NatId = None

    def _deserialize(self, params):
        if params.get("NatId"):
            self.NatId = params.get("NatId")


class DescribeNatsRequest(AbstractModel):
    """DescribeNats请求参数结构体
    """

    def __init__(self):
        r"""描述Nat
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param NatId: 多个Nat的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.NatId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("NatId"):
            self.NatId = params.get("NatId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class AssociateNatRequest(AbstractModel):
    """AssociateNat请求参数结构体
    """

    def __init__(self):
        r"""Nat关联子网
        :param NatId: Nat的ID
        :type PathPrefix: String
        :param SubnetId: 子网的ID
        :type PathPrefix: String
        """
        self.NatId = None
        self.SubnetId = None

    def _deserialize(self, params):
        if params.get("NatId"):
            self.NatId = params.get("NatId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")


class DisassociateNatRequest(AbstractModel):
    """DisassociateNat请求参数结构体
    """

    def __init__(self):
        r"""Nat解绑子网
        :param NatId: Nat的ID
        :type PathPrefix: String
        :param SubnetId: 子网的ID
        :type PathPrefix: String
        """
        self.NatId = None
        self.SubnetId = None

    def _deserialize(self, params):
        if params.get("NatId"):
            self.NatId = params.get("NatId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")


class DescribeInternetGatewaysRequest(AbstractModel):
    """DescribeInternetGateways请求参数结构体
    """

    def __init__(self):
        r"""描述InternetGateway
        :param InternetGatewayId: 多个InternetGateway的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.InternetGatewayId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("InternetGatewayId"):
            self.InternetGatewayId = params.get("InternetGatewayId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateVpcPeeringConnectionRequest(AbstractModel):
    """CreateVpcPeeringConnection请求参数结构体
    """

    def __init__(self):
        r"""创建对等连接
        :param VpcId: 发起端Vpc的ID
        :type PathPrefix: String
        :param PeeringName: 对等连接的名称
        :type PathPrefix: String
        :param PeerVpcId: 接受端Vpc的ID
        :type PathPrefix: String
        :param Region: 发起端region
        :type PathPrefix: String
        :param PeerRegion: 接受端Vpc的region
        :type PathPrefix: String
        :param PeerAccountId: 接受端账号ID
        :type PathPrefix: String
        :param BandWidth: 对等连接的带宽，同机房时可缺省，带宽值为1000且不可修改，跨机房时不可缺省
        :type PathPrefix: Int
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 对等连接的计费类型，同机房的对端连接此参数缺省
        :type PathPrefix: String
        """
        self.VpcId = None
        self.PeeringName = None
        self.PeerVpcId = None
        self.Region = None
        self.PeerRegion = None
        self.PeerAccountId = None
        self.BandWidth = None
        self.ProjectId = None
        self.ChargeType = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("PeeringName"):
            self.PeeringName = params.get("PeeringName")
        if params.get("PeerVpcId"):
            self.PeerVpcId = params.get("PeerVpcId")
        if params.get("Region"):
            self.Region = params.get("Region")
        if params.get("PeerRegion"):
            self.PeerRegion = params.get("PeerRegion")
        if params.get("PeerAccountId"):
            self.PeerAccountId = params.get("PeerAccountId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")


class DeleteVpcPeeringConnectionRequest(AbstractModel):
    """DeleteVpcPeeringConnection请求参数结构体
    """

    def __init__(self):
        r"""删除对等连接
        :param VpcPeeringConnectionId: 对等连接的ID
        :type PathPrefix: String
        """
        self.VpcPeeringConnectionId = None

    def _deserialize(self, params):
        if params.get("VpcPeeringConnectionId"):
            self.VpcPeeringConnectionId = params.get("VpcPeeringConnectionId")


class DescribeVpcPeeringConnectionsRequest(AbstractModel):
    """DescribeVpcPeeringConnections请求参数结构体
    """

    def __init__(self):
        r"""描述对等连接
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param VpcPeeringConnectionId: 多个对等连接的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.VpcPeeringConnectionId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("VpcPeeringConnectionId"):
            self.VpcPeeringConnectionId = params.get("VpcPeeringConnectionId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ModifyNetworkAclRequest(AbstractModel):
    """ModifyNetworkAcl请求参数结构体
    """

    def __init__(self):
        r"""修改ACL
        :param NetworkAclId: ACL的ID
        :type PathPrefix: String
        :param NetworkAclName: ACL的名称
        :type PathPrefix: String
        :param Description: ACL的描述
        :type PathPrefix: String
        """
        self.NetworkAclId = None
        self.NetworkAclName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("NetworkAclId"):
            self.NetworkAclId = params.get("NetworkAclId")
        if params.get("NetworkAclName"):
            self.NetworkAclName = params.get("NetworkAclName")
        if params.get("Description"):
            self.Description = params.get("Description")


class ModifySecurityGroupRequest(AbstractModel):
    """ModifySecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""更改安全组信息
        :param SecurityGroupId: 安全组的ID
        :type PathPrefix: String
        :param SecurityGroupName: 安全组的名称
        :type PathPrefix: String
        :param Description: 安全组的描述
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")


class ModifySubnetRequest(AbstractModel):
    """ModifySubnet请求参数结构体
    """

    def __init__(self):
        r"""修改子网
        :param SubnetId: 子网的ID
        :type PathPrefix: String
        :param SubnetName: 子网的名称
        :type PathPrefix: String
        :param Dns1: 子网的Dns1
        :type PathPrefix: String
        :param Dns2: 子网的Dns2
        :type PathPrefix: String
        """
        self.SubnetId = None
        self.SubnetName = None
        self.Dns1 = None
        self.Dns2 = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("SubnetName"):
            self.SubnetName = params.get("SubnetName")
        if params.get("Dns1"):
            self.Dns1 = params.get("Dns1")
        if params.get("Dns2"):
            self.Dns2 = params.get("Dns2")


class ModifyNatRequest(AbstractModel):
    """ModifyNat请求参数结构体
    """

    def __init__(self):
        r"""更新NAT信息
        :param NatId: Nat的ID
        :type PathPrefix: String
        :param NatName: Nat的名称
        :type PathPrefix: String
        :param BandWidth: Nat的带宽
        :type PathPrefix: Int
        """
        self.NatId = None
        self.NatName = None
        self.BandWidth = None

    def _deserialize(self, params):
        if params.get("NatId"):
            self.NatId = params.get("NatId")
        if params.get("NatName"):
            self.NatName = params.get("NatName")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces请求参数结构体
    """

    def __init__(self):
        r"""描述弹性网卡
        :param NetworkInterfaceId: 多个网卡的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.NetworkInterfaceId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeSubnetAvailableAddressesRequest(AbstractModel):
    """DescribeSubnetAvailableAddresses请求参数结构体
    """

    def __init__(self):
        r"""描述子网可用IP信息
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ModifyVpcRequest(AbstractModel):
    """ModifyVpc请求参数结构体
    """

    def __init__(self):
        r"""修改Vpc
        :param VpcName: Vpc的名称
        :type PathPrefix: String
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        """
        self.VpcName = None
        self.VpcId = None

    def _deserialize(self, params):
        if params.get("VpcName"):
            self.VpcName = params.get("VpcName")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")


class AcceptVpcPeeringConnectionRequest(AbstractModel):
    """AcceptVpcPeeringConnection请求参数结构体
    """

    def __init__(self):
        r"""接受对等连接
        :param VpcPeeringConnectionId: 对等连接的ID
        :type PathPrefix: String
        """
        self.VpcPeeringConnectionId = None

    def _deserialize(self, params):
        if params.get("VpcPeeringConnectionId"):
            self.VpcPeeringConnectionId = params.get("VpcPeeringConnectionId")


class RejectVpcPeeringConnectionRequest(AbstractModel):
    """RejectVpcPeeringConnection请求参数结构体
    """

    def __init__(self):
        r"""拒绝对等连接
        :param VpcPeeringConnectionId: 对等连接的ID
        :type PathPrefix: String
        """
        self.VpcPeeringConnectionId = None

    def _deserialize(self, params):
        if params.get("VpcPeeringConnectionId"):
            self.VpcPeeringConnectionId = params.get("VpcPeeringConnectionId")


class ModifyVpcPeeringConnectionRequest(AbstractModel):
    """ModifyVpcPeeringConnection请求参数结构体
    """

    def __init__(self):
        r"""修改对等连接
        :param VpcPeeringConnectionId: 对等连接的ID
        :type PathPrefix: String
        :param PeeringName: 对等连接的名称
        :type PathPrefix: String
        :param BandWidth: 对等连接的带宽
        :type PathPrefix: Int
        """
        self.VpcPeeringConnectionId = None
        self.PeeringName = None
        self.BandWidth = None

    def _deserialize(self, params):
        if params.get("VpcPeeringConnectionId"):
            self.VpcPeeringConnectionId = params.get("VpcPeeringConnectionId")
        if params.get("PeeringName"):
            self.PeeringName = params.get("PeeringName")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")


class DescribeAvailabilityZonesRequest(AbstractModel):
    """DescribeAvailabilityZones请求参数结构体
    """

    def __init__(self):
        r"""描述可用区信息
        """

    def _deserialize(self, params):
        return


class DescribeDirectConnectsRequest(AbstractModel):
    """DescribeDirectConnects请求参数结构体
    """

    def __init__(self):
        r"""描述物理端口
        :param DirectConnectId: 物理端口ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.DirectConnectId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("DirectConnectId"):
            self.DirectConnectId = params.get("DirectConnectId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateDirectConnectInterfaceRequest(AbstractModel):
    """CreateDirectConnectInterface请求参数结构体
    """

    def __init__(self):
        r"""创建连接通道
        :param DirectConnectId: 物理端口ID
        :type PathPrefix: String
        :param VlanId: 物理专线vlan id
        :type PathPrefix: Int
        :param RouteType: 路由模式
        :type PathPrefix: String
        :param DirectConnectInterfaceName: 连接通道的名称
        :type PathPrefix: String
        :param DirectConnectInterfaceAccountId: 连接通道所属的用户ID
        :type PathPrefix: String
        :param CustomerPeerIp: 客户侧IPv4互联IP
        :type PathPrefix: String
        :param LocalPeerIp: 金山云侧IPv4互联IP
        :type PathPrefix: String
        :param HaDirectConnectId: Ha物理专线的ID
        :type PathPrefix: String
        :param HaCustomerPeerIp: Ha客户侧IPv4互联IP
        :type PathPrefix: String
        :param HaLocalPeerIp: Ha金山云侧IPv4互联IP
        :type PathPrefix: String
        :param BgpPeer: 用户侧BGP ASN
        :type PathPrefix: String
        :param ReliabilityMethod: 可靠性方法
        :type PathPrefix: String
        :param BfdConfigId: BFD配置ID
        :type PathPrefix: String
        :param BgpClientToken: BGP 秘钥
        :type PathPrefix: String
        """
        self.DirectConnectId = None
        self.VlanId = None
        self.RouteType = None
        self.DirectConnectInterfaceName = None
        self.DirectConnectInterfaceAccountId = None
        self.CustomerPeerIp = None
        self.LocalPeerIp = None
        self.HaDirectConnectId = None
        self.HaCustomerPeerIp = None
        self.HaLocalPeerIp = None
        self.BgpPeer = None
        self.ReliabilityMethod = None
        self.BfdConfigId = None
        self.BgpClientToken = None

    def _deserialize(self, params):
        if params.get("DirectConnectId"):
            self.DirectConnectId = params.get("DirectConnectId")
        if params.get("VlanId"):
            self.VlanId = params.get("VlanId")
        if params.get("RouteType"):
            self.RouteType = params.get("RouteType")
        if params.get("DirectConnectInterfaceName"):
            self.DirectConnectInterfaceName = params.get("DirectConnectInterfaceName")
        if params.get("DirectConnectInterfaceAccountId"):
            self.DirectConnectInterfaceAccountId = params.get("DirectConnectInterfaceAccountId")
        if params.get("CustomerPeerIp"):
            self.CustomerPeerIp = params.get("CustomerPeerIp")
        if params.get("LocalPeerIp"):
            self.LocalPeerIp = params.get("LocalPeerIp")
        if params.get("HaDirectConnectId"):
            self.HaDirectConnectId = params.get("HaDirectConnectId")
        if params.get("HaCustomerPeerIp"):
            self.HaCustomerPeerIp = params.get("HaCustomerPeerIp")
        if params.get("HaLocalPeerIp"):
            self.HaLocalPeerIp = params.get("HaLocalPeerIp")
        if params.get("BgpPeer"):
            self.BgpPeer = params.get("BgpPeer")
        if params.get("ReliabilityMethod"):
            self.ReliabilityMethod = params.get("ReliabilityMethod")
        if params.get("BfdConfigId"):
            self.BfdConfigId = params.get("BfdConfigId")
        if params.get("BgpClientToken"):
            self.BgpClientToken = params.get("BgpClientToken")


class DeleteDirectConnectInterfaceRequest(AbstractModel):
    """DeleteDirectConnectInterface请求参数结构体
    """

    def __init__(self):
        r"""删除连接通道
        :param DirectConnectInterfaceId: 连接通道的ID
        :type PathPrefix: String
        """
        self.DirectConnectInterfaceId = None

    def _deserialize(self, params):
        if params.get("DirectConnectInterfaceId"):
            self.DirectConnectInterfaceId = params.get("DirectConnectInterfaceId")


class DescribeDirectConnectInterfacesRequest(AbstractModel):
    """DescribeDirectConnectInterfaces请求参数结构体
    """

    def __init__(self):
        r"""描述连接通道
        :param DirectConnectInterfaceId: 多个连接通道的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.DirectConnectInterfaceId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("DirectConnectInterfaceId"):
            self.DirectConnectInterfaceId = params.get("DirectConnectInterfaceId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateDirectConnectGatewayRequest(AbstractModel):
    """CreateDirectConnectGateway请求参数结构体
    """

    def __init__(self):
        r"""创建边界网关
        :param VpcId: VPC的ID
        :type PathPrefix: String
        :param DirectConnectGatewayName: 边界网关的名称
        :type PathPrefix: String
        """
        self.VpcId = None
        self.DirectConnectGatewayName = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("DirectConnectGatewayName"):
            self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")


class DeleteDirectConnectGatewayRequest(AbstractModel):
    """DeleteDirectConnectGateway请求参数结构体
    """

    def __init__(self):
        r"""删除边界网关
        :param DirectConnectGatewayId: 边界网关的ID
        :type PathPrefix: String
        """
        self.DirectConnectGatewayId = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayId"):
            self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")


class DescribeDirectConnectGatewaysRequest(AbstractModel):
    """DescribeDirectConnectGateways请求参数结构体
    """

    def __init__(self):
        r"""描述边界网关
        :param DirectConnectGatewayId: 多个边界网关的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.DirectConnectGatewayId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayId"):
            self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class AttachDirectConnectGatewayRequest(AbstractModel):
    """AttachDirectConnectGateway请求参数结构体
    """

    def __init__(self):
        r"""绑定边界网关
        :param DirectConnectGatewayId: 边界网关的ID
        :type PathPrefix: String
        :param DirectConnectInterfaceId: 连接通道的ID
        :type PathPrefix: String
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectInterfaceId = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayId"):
            self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("DirectConnectInterfaceId"):
            self.DirectConnectInterfaceId = params.get("DirectConnectInterfaceId")


class DetachDirectConnectGatewayRequest(AbstractModel):
    """DetachDirectConnectGateway请求参数结构体
    """

    def __init__(self):
        r"""解绑边界网关
        :param DirectConnectGatewayId: 边界网关的ID
        :type PathPrefix: String
        :param DirectConnectInterfaceId: 连接通道的ID
        :type PathPrefix: String
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectInterfaceId = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayId"):
            self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("DirectConnectInterfaceId"):
            self.DirectConnectInterfaceId = params.get("DirectConnectInterfaceId")


class ModifyDirectConnectInterfaceRequest(AbstractModel):
    """ModifyDirectConnectInterface请求参数结构体
    """

    def __init__(self):
        r"""修改连接通道
        :param DirectConnectInterfaceId: 连接通道的ID
        :type PathPrefix: String
        :param DirectConnectInterfaceName: 连接通道的名称
        :type PathPrefix: String
        """
        self.DirectConnectInterfaceId = None
        self.DirectConnectInterfaceName = None

    def _deserialize(self, params):
        if params.get("DirectConnectInterfaceId"):
            self.DirectConnectInterfaceId = params.get("DirectConnectInterfaceId")
        if params.get("DirectConnectInterfaceName"):
            self.DirectConnectInterfaceName = params.get("DirectConnectInterfaceName")


class ModifyDirectConnectGatewayRequest(AbstractModel):
    """ModifyDirectConnectGateway请求参数结构体
    """

    def __init__(self):
        r"""修改边界网关
        :param DirectConnectGatewayId: 边界网关的ID
        :type PathPrefix: String
        :param DirectConnectGatewayName: 边界网关的名称
        :type PathPrefix: String
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayId"):
            self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("DirectConnectGatewayName"):
            self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")


class CreateVpnGatewayRequest(AbstractModel):
    """CreateVpnGateway请求参数结构体
    """

    def __init__(self):
        r"""创建VPN网关
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param BandWidth: VPN网关的带宽
        :type PathPrefix: Int
        :param VpnGatewayName: VPN网关的名称
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: VPN网关的计费类型
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月时不可缺省。
        :type PathPrefix: Int
        """
        self.VpcId = None
        self.BandWidth = None
        self.VpnGatewayName = None
        self.ProjectId = None
        self.ChargeType = None
        self.PurchaseTime = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")
        if params.get("VpnGatewayName"):
            self.VpnGatewayName = params.get("VpnGatewayName")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")


class ModifyVpnGatewayRequest(AbstractModel):
    """ModifyVpnGateway请求参数结构体
    """

    def __init__(self):
        r"""修改VPN网关
        :param VpnGatewayId: VPN网关的ID
        :type PathPrefix: String
        :param BandWidth: VPN网关的带宽
        :type PathPrefix: Int
        :param VpnGatewayName: VPN网关的名称
        :type PathPrefix: String
        """
        self.VpnGatewayId = None
        self.BandWidth = None
        self.VpnGatewayName = None

    def _deserialize(self, params):
        if params.get("VpnGatewayId"):
            self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")
        if params.get("VpnGatewayName"):
            self.VpnGatewayName = params.get("VpnGatewayName")


class DeleteVpnGatewayRequest(AbstractModel):
    """DeleteVpnGateway请求参数结构体
    """

    def __init__(self):
        r"""删除VPN网关
        :param VpnGatewayId: VPN网关的ID
        :type PathPrefix: String
        """
        self.VpnGatewayId = None

    def _deserialize(self, params):
        if params.get("VpnGatewayId"):
            self.VpnGatewayId = params.get("VpnGatewayId")


class DescribeVpnGatewaysRequest(AbstractModel):
    """DescribeVpnGateways请求参数结构体
    """

    def __init__(self):
        r"""描述VPN网关
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param VpnGatewayId: VPN网关的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.VpnGatewayId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("VpnGatewayId"):
            self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateVpnTunnelRequest(AbstractModel):
    """CreateVpnTunnel请求参数结构体
    """

    def __init__(self):
        r"""创建VPN通道
        :param CustomerGatewayId: 客户网关的ID
        :type PathPrefix: String
        :param VpnGatewayId: VPN网关的ID
        :type PathPrefix: String
        :param VpnTunnelName: Vpn通道的名称
        :type PathPrefix: String
        :param IpsecAuthenAlgorithm: Ipsec认证算法
        :type PathPrefix: String
        :param IpsecEncryAlgorithm: Ipsec加密算法
        :type PathPrefix: String
        :param IkeAuthenAlgorithm: IKE认证算法(md5|sha)
        :type PathPrefix: String
        :param IkeEncryAlgorithm: IKE加密算法
        :type PathPrefix: String
        :param Type: 客户网关的类型(GreOverIpsec|Ipsec)
        :type PathPrefix: String
        :param PreSharedKey: 预共享密钥。对称加密的KEY，VPN端和客户端统一，用户自行填写
        :type PathPrefix: String
        :param IpsecLifetimeSecond: 生存周期（S）
        :type PathPrefix: Int
        :param IpsecLifetimeTraffic: 生存周期（Kb）
        :type PathPrefix: Int
        :param IkeDHGroup: 密钥加密算法的类型(1|2|5|14|24)
        :type PathPrefix: String
        :param EnableNatTraversal: 是否开启野蛮模式
        :type PathPrefix: Boolean
        :param VpnGreIp: GRE模式VPN的IP
        :type PathPrefix: String
        :param HaVpnGreIp: GRE模式开启HA模式VPN的IP
        :type PathPrefix: String
        :param CustomerGreIp: GRE模式客户的IP
        :type PathPrefix: String
        :param HaCustomerGreIp: GRE模式开启HA模式客户的IP
        :type PathPrefix: String
        """
        self.CustomerGatewayId = None
        self.VpnGatewayId = None
        self.VpnTunnelName = None
        self.IpsecAuthenAlgorithm = None
        self.IpsecEncryAlgorithm = None
        self.IkeAuthenAlgorithm = None
        self.IkeEncryAlgorithm = None
        self.Type = None
        self.PreSharedKey = None
        self.IpsecLifetimeSecond = None
        self.IpsecLifetimeTraffic = None
        self.IkeDHGroup = None
        self.EnableNatTraversal = None
        self.VpnGreIp = None
        self.HaVpnGreIp = None
        self.CustomerGreIp = None
        self.HaCustomerGreIp = None

    def _deserialize(self, params):
        if params.get("CustomerGatewayId"):
            self.CustomerGatewayId = params.get("CustomerGatewayId")
        if params.get("VpnGatewayId"):
            self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("VpnTunnelName"):
            self.VpnTunnelName = params.get("VpnTunnelName")
        if params.get("IpsecAuthenAlgorithm"):
            self.IpsecAuthenAlgorithm = params.get("IpsecAuthenAlgorithm")
        if params.get("IpsecEncryAlgorithm"):
            self.IpsecEncryAlgorithm = params.get("IpsecEncryAlgorithm")
        if params.get("IkeAuthenAlgorithm"):
            self.IkeAuthenAlgorithm = params.get("IkeAuthenAlgorithm")
        if params.get("IkeEncryAlgorithm"):
            self.IkeEncryAlgorithm = params.get("IkeEncryAlgorithm")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("PreSharedKey"):
            self.PreSharedKey = params.get("PreSharedKey")
        if params.get("IpsecLifetimeSecond"):
            self.IpsecLifetimeSecond = params.get("IpsecLifetimeSecond")
        if params.get("IpsecLifetimeTraffic"):
            self.IpsecLifetimeTraffic = params.get("IpsecLifetimeTraffic")
        if params.get("IkeDHGroup"):
            self.IkeDHGroup = params.get("IkeDHGroup")
        if params.get("EnableNatTraversal"):
            self.EnableNatTraversal = params.get("EnableNatTraversal")
        if params.get("VpnGreIp"):
            self.VpnGreIp = params.get("VpnGreIp")
        if params.get("HaVpnGreIp"):
            self.HaVpnGreIp = params.get("HaVpnGreIp")
        if params.get("CustomerGreIp"):
            self.CustomerGreIp = params.get("CustomerGreIp")
        if params.get("HaCustomerGreIp"):
            self.HaCustomerGreIp = params.get("HaCustomerGreIp")


class ModifyVpnTunnelRequest(AbstractModel):
    """ModifyVpnTunnel请求参数结构体
    """

    def __init__(self):
        r"""修改VPN通道
        :param VpnTunnelId: Vpn通道的ID
        :type PathPrefix: String
        :param VpnTunnelName: Vpn通道的名称
        :type PathPrefix: String
        """
        self.VpnTunnelId = None
        self.VpnTunnelName = None

    def _deserialize(self, params):
        if params.get("VpnTunnelId"):
            self.VpnTunnelId = params.get("VpnTunnelId")
        if params.get("VpnTunnelName"):
            self.VpnTunnelName = params.get("VpnTunnelName")


class DeleteVpnTunnelRequest(AbstractModel):
    """DeleteVpnTunnel请求参数结构体
    """

    def __init__(self):
        r"""删除VPN通道
        :param VpnTunnelId: Vpn通道的ID
        :type PathPrefix: String
        """
        self.VpnTunnelId = None

    def _deserialize(self, params):
        if params.get("VpnTunnelId"):
            self.VpnTunnelId = params.get("VpnTunnelId")


class DescribeVpnTunnelsRequest(AbstractModel):
    """DescribeVpnTunnels请求参数结构体
    """

    def __init__(self):
        r"""描述VPN通道
        :param VpnTunnelId: 多个Vpn通道的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.VpnTunnelId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("VpnTunnelId"):
            self.VpnTunnelId = params.get("VpnTunnelId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateCustomerGatewayRequest(AbstractModel):
    """CreateCustomerGateway请求参数结构体
    """

    def __init__(self):
        r"""创建客户网关
        :param CustomerGatewayName: 客户网关的名称
        :type PathPrefix: String
        :param CustomerGatewayAddress: 客户网关公网IP
        :type PathPrefix: String
        :param HaCustomerGatewayAddress: HA模式客户网关的公网IP
        :type PathPrefix: String
        """
        self.CustomerGatewayName = None
        self.CustomerGatewayAddress = None
        self.HaCustomerGatewayAddress = None

    def _deserialize(self, params):
        if params.get("CustomerGatewayName"):
            self.CustomerGatewayName = params.get("CustomerGatewayName")
        if params.get("CustomerGatewayAddress"):
            self.CustomerGatewayAddress = params.get("CustomerGatewayAddress")
        if params.get("HaCustomerGatewayAddress"):
            self.HaCustomerGatewayAddress = params.get("HaCustomerGatewayAddress")


class ModifyCustomerGatewayRequest(AbstractModel):
    """ModifyCustomerGateway请求参数结构体
    """

    def __init__(self):
        r"""修改客户网关信息
        :param CustomerGatewayId: 客户网关的ID
        :type PathPrefix: String
        :param CustomerGatewayName: 客户网关的名称
        :type PathPrefix: String
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None

    def _deserialize(self, params):
        if params.get("CustomerGatewayId"):
            self.CustomerGatewayId = params.get("CustomerGatewayId")
        if params.get("CustomerGatewayName"):
            self.CustomerGatewayName = params.get("CustomerGatewayName")


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway请求参数结构体
    """

    def __init__(self):
        r"""删除客户网关
        :param CustomerGatewayId: 客户网关的ID
        :type PathPrefix: String
        """
        self.CustomerGatewayId = None

    def _deserialize(self, params):
        if params.get("CustomerGatewayId"):
            self.CustomerGatewayId = params.get("CustomerGatewayId")


class ModifyDirectConnectRequest(AbstractModel):
    """ModifyDirectConnect请求参数结构体
    """

    def __init__(self):
        r"""修改物理端口
        :param DirectConnectId: 物理端口ID
        :type PathPrefix: String
        :param DirectConnectName: 专线的名称
        :type PathPrefix: String
        """
        self.DirectConnectId = None
        self.DirectConnectName = None

    def _deserialize(self, params):
        if params.get("DirectConnectId"):
            self.DirectConnectId = params.get("DirectConnectId")
        if params.get("DirectConnectName"):
            self.DirectConnectName = params.get("DirectConnectName")


class DescribeCustomerGatewaysRequest(AbstractModel):
    """DescribeCustomerGateways请求参数结构体
    """

    def __init__(self):
        r"""描述客户网关
        :param CustomerGatewayId: 多个客户网关的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.CustomerGatewayId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CustomerGatewayId"):
            self.CustomerGatewayId = params.get("CustomerGatewayId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeSubnetAllocatedIpAddressesRequest(AbstractModel):
    """DescribeSubnetAllocatedIpAddresses请求参数结构体
    """

    def __init__(self):
        r"""描述子网已用IP信息
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeleteNetworkInterfaceRequest(AbstractModel):
    """DeleteNetworkInterface请求参数结构体
    """

    def __init__(self):
        r"""删除弹性网卡
        :param NetworkInterfaceId: 网卡的ID
        :type PathPrefix: String
        """
        self.NetworkInterfaceId = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface请求参数结构体
    """

    def __init__(self):
        r"""创建弹性网卡
        :param SubnetId: 子网的ID
        :type PathPrefix: String
        :param NetworkInterfaceName: 网卡的名称
        :type PathPrefix: String
        :param PrivateIpAddress: 网卡的私网IP
        :type PathPrefix: String
        :param SecurityGroupId: 一个或多个安全组的ID，不能为空
        :type PathPrefix: Filter
        """
        self.SubnetId = None
        self.NetworkInterfaceName = None
        self.PrivateIpAddress = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("NetworkInterfaceName"):
            self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class ModifyNetworkInterfaceRequest(AbstractModel):
    """ModifyNetworkInterface请求参数结构体
    """

    def __init__(self):
        r"""修改弹性网卡名称
        :param NetworkInterfaceName: 网卡的名称
        :type PathPrefix: String
        :param NetworkInterfaceId: 网卡ID
        :type PathPrefix: String
        """
        self.NetworkInterfaceName = None
        self.NetworkInterfaceId = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceName"):
            self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip请求参数结构体
    """

    def __init__(self):
        r"""创建HaVip
        :param SubnetId: 子网的ID
        :type PathPrefix: String
        :param IpAddress: 高可用虚拟IP的IP地址
        :type PathPrefix: String
        """
        self.SubnetId = None
        self.IpAddress = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("IpAddress"):
            self.IpAddress = params.get("IpAddress")


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip请求参数结构体
    """

    def __init__(self):
        r"""删除HaVip
        :param HaVipId: 高可用虚拟IP的ID
        :type PathPrefix: String
        """
        self.HaVipId = None

    def _deserialize(self, params):
        if params.get("HaVipId"):
            self.HaVipId = params.get("HaVipId")


class AssociateHaVipRequest(AbstractModel):
    """AssociateHaVip请求参数结构体
    """

    def __init__(self):
        r"""绑定HaVip
        :param NetworkInterfaceId: 网卡的ID
        :type PathPrefix: String
        :param HaVipId: 高可用虚拟IP的ID
        :type PathPrefix: String
        """
        self.NetworkInterfaceId = None
        self.HaVipId = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("HaVipId"):
            self.HaVipId = params.get("HaVipId")


class UnAssociateHaVipRequest(AbstractModel):
    """UnAssociateHaVip请求参数结构体
    """

    def __init__(self):
        r"""解绑HaVip
        :param NetworkInterfaceId: 网卡的ID
        :type PathPrefix: String
        :param HaVipId: 高可用虚拟IP的ID
        :type PathPrefix: String
        """
        self.NetworkInterfaceId = None
        self.HaVipId = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("HaVipId"):
            self.HaVipId = params.get("HaVipId")


class DescribeHaVipRequest(AbstractModel):
    """DescribeHaVip请求参数结构体
    """

    def __init__(self):
        r"""查询HaVip
        :param HaVipId: 多个高可用虚拟IP的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.HaVipId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("HaVipId"):
            self.HaVipId = params.get("HaVipId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DeleteDirectConnectGatewayRouteRequest(AbstractModel):
    """DeleteDirectConnectGatewayRoute请求参数结构体
    """

    def __init__(self):
        r"""删除边界网关路由
        :param DirectConnectGatewayRouteId: 边界网关路由ID
        :type PathPrefix: String
        """
        self.DirectConnectGatewayRouteId = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayRouteId"):
            self.DirectConnectGatewayRouteId = params.get("DirectConnectGatewayRouteId")


class DescribeDirectConnectGatewayRouteRequest(AbstractModel):
    """DescribeDirectConnectGatewayRoute请求参数结构体
    """

    def __init__(self):
        r"""查询边界网关路由
        :param DirectConnectGatewayId: 边界网关的ID
        :type PathPrefix: String
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.DirectConnectGatewayId = None
        self.MaxResults = None
        self.Filter = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayId"):
            self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class PublishDirectConnectRouteRequest(AbstractModel):
    """PublishDirectConnectRoute请求参数结构体
    """

    def __init__(self):
        r"""发布边界网关路由到BGP
        :param DirectConnectGatewayRouteId: 边界网关路由ID
        :type PathPrefix: String
        """
        self.DirectConnectGatewayRouteId = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayRouteId"):
            self.DirectConnectGatewayRouteId = params.get("DirectConnectGatewayRouteId")


class UnpublishDirectConnectRouteRequest(AbstractModel):
    """UnpublishDirectConnectRoute请求参数结构体
    """

    def __init__(self):
        r"""从BGP取消发布边界网关路由
        :param DirectConnectGatewayRouteId: 边界网关路由ID
        :type PathPrefix: String
        """
        self.DirectConnectGatewayRouteId = None

    def _deserialize(self, params):
        if params.get("DirectConnectGatewayRouteId"):
            self.DirectConnectGatewayRouteId = params.get("DirectConnectGatewayRouteId")


class AddSecondaryCidrBlockRequest(AbstractModel):
    """AddSecondaryCidrBlock请求参数结构体
    """

    def __init__(self):
        r"""为VPC添加附加IPv4网段
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param CidrBlock: Vpc附加Ipv4网段的网络范围，不能与VPC已有Ipv4网段重叠，例如：10.0.0.0/16
        :type PathPrefix: String
        """
        self.VpcId = None
        self.CidrBlock = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("CidrBlock"):
            self.CidrBlock = params.get("CidrBlock")


class DeleteSecondaryCidrBlockRequest(AbstractModel):
    """DeleteSecondaryCidrBlock请求参数结构体
    """

    def __init__(self):
        r"""删除VPC附加IPv4网段
        :param VpcId: Vpc的ID
        :type PathPrefix: String
        :param SecondaryCidrId: Vpc附加网段的ID
        :type PathPrefix: String
        """
        self.VpcId = None
        self.SecondaryCidrId = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SecondaryCidrId"):
            self.SecondaryCidrId = params.get("SecondaryCidrId")


class AssignPrivateIpAddressRequest(AbstractModel):
    """AssignPrivateIpAddress请求参数结构体
    """

    def __init__(self):
        r"""AssignPrivateIpAddress
        :param NetworkInterfaceId: 网卡的ID
        :type PathPrefix: String
        :param PrivateIpAddress: 辅助私有IP地址
        :type PathPrefix: Filter
        :param SecondaryPrivateIpAddressCount: 分配辅助私网IP数量
        :type PathPrefix: Int
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None
        self.SecondaryPrivateIpAddressCount = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("SecondaryPrivateIpAddressCount"):
            self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")


class UnassignPrivateIpAddressRequest(AbstractModel):
    """UnassignPrivateIpAddress请求参数结构体
    """

    def __init__(self):
        r"""弹性网卡取消分配辅助私网ip
        :param NetworkInterfaceId: 网卡的ID
        :type PathPrefix: String
        :param PrivateIpAddress: 辅助私有IP地址
        :type PathPrefix: Filter
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")


