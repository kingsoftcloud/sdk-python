from ksyun.common.abstract_model import AbstractModel

class CreatePrivateDnsRequest(AbstractModel):
    """CreatePrivateDns请求参数结构体
    """

    def __init__(self):
        r"""创建内网DNS实例
        :param Action: Action
        :type PathPrefix: String
        :param Version: Version
        :type PathPrefix: String
        :param ProjectId: 项目ID
        :type PathPrefix: String
        """
        self.Action = None
        self.Version = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DeletePrivateDnsRequest(AbstractModel):
    """DeletePrivateDns请求参数结构体
    """

    def __init__(self):
        r"""删除内网DNS实例
        :param Action: Action
        :type PathPrefix: String
        :param Version: Version
        :type PathPrefix: String
        :param ProjectId: 项目ID
        :type PathPrefix: String
        """
        self.Action = None
        self.Version = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribePrivateDnsRequest(AbstractModel):
    """DescribePrivateDns请求参数结构体
    """

    def __init__(self):
        r"""描述内网DNS实例
        :param Action: Action
        :type PathPrefix: String
        :param Version: Version
        :type PathPrefix: String
        """
        self.Action = None
        self.Version = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")


class AssociateVpcsRequest(AbstractModel):
    """AssociateVpcs请求参数结构体
    """

    def __init__(self):
        r"""关联VPC
        :param Action: Action
        :type PathPrefix: String
        :param Version: Version
        :type PathPrefix: String
        :param VpcId: VpcId
该 VPC 将关联所属 Region 的 PrivateDns 实例
        :type PathPrefix: String
        """
        self.Action = None
        self.Version = None
        self.VpcId = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")


class DisassociateVpcsRequest(AbstractModel):
    """DisassociateVpcs请求参数结构体
    """

    def __init__(self):
        r"""解绑VPC
        :param Action: Action
        :type PathPrefix: String
        :param Version: Version
        :type PathPrefix: String
        :param VpcId: VpcId
该 VPC 将解关联 PrivateDns 实例
        :type PathPrefix: String
        """
        self.Action = None
        self.Version = None
        self.VpcId = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")


class CreateZoneRequest(AbstractModel):
    """CreateZone请求参数结构体
    """

    def __init__(self):
        r"""创建Zone
        :param Action: Action
        :type PathPrefix: String
        :param Version: Version
        :type PathPrefix: String
        :param ZoneName: ZoneName
        :type PathPrefix: String
        :param ZoneTtl: ZoneTtl
        :type PathPrefix: Int
        """
        self.Action = None
        self.Version = None
        self.ZoneName = None
        self.ZoneTtl = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")
        if params.get("ZoneName"):
            self.ZoneName = params.get("ZoneName")
        if params.get("ZoneTtl"):
            self.ZoneTtl = params.get("ZoneTtl")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone请求参数结构体
    """

    def __init__(self):
        r"""删除Zone
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone请求参数结构体
    """

    def __init__(self):
        r"""修改Zone
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class DescribeZoneRequest(AbstractModel):
    """DescribeZone请求参数结构体
    """

    def __init__(self):
        r"""描述Zone
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class CreateRecordRequest(AbstractModel):
    """CreateRecord请求参数结构体
    """

    def __init__(self):
        r"""添加解析记录
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord请求参数结构体
    """

    def __init__(self):
        r"""删除解析记录
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class ModifyRecordRequest(AbstractModel):
    """ModifyRecord请求参数结构体
    """

    def __init__(self):
        r"""修改解析记录
        :param RecordValue: 记录值
        :type PathPrefix: String
        """
        self.RecordValue = None

    def _deserialize(self, params):
        if params.get("RecordValue"):
            self.RecordValue = params.get("RecordValue")


class DescribeRecordRequest(AbstractModel):
    """DescribeRecord请求参数结构体
    """

    def __init__(self):
        r"""描述解析记录
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class CreateRecordDataRequest(AbstractModel):
    """CreateRecordData请求参数结构体
    """

    def __init__(self):
        r"""添加记录值
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class DeleteRecordDataRequest(AbstractModel):
    """DeleteRecordData请求参数结构体
    """

    def __init__(self):
        r"""删除记录值
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class CreatePdnsZoneRequest(AbstractModel):
    """CreatePdnsZone请求参数结构体
    """

    def __init__(self):
        r"""创建内网DNSzone
        :param ZoneName: Zone名称
        :type PathPrefix: String
        :param ZoneTtl: TTL
        :type PathPrefix: Int
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 有效值：
TrafficMonthly：按量付费（流量月结）。
        :type PathPrefix: String
        """
        self.ZoneName = None
        self.ZoneTtl = None
        self.ProjectId = None
        self.ChargeType = None

    def _deserialize(self, params):
        if params.get("ZoneName"):
            self.ZoneName = params.get("ZoneName")
        if params.get("ZoneTtl"):
            self.ZoneTtl = params.get("ZoneTtl")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")


class ModifyPdnsZoneRequest(AbstractModel):
    """ModifyPdnsZone请求参数结构体
    """

    def __init__(self):
        r"""修改Zone的ttl
        :param ZoneId: Zone的ID
        :type PathPrefix: String
        :param ZoneTtl: TTL
        :type PathPrefix: Int
        """
        self.ZoneId = None
        self.ZoneTtl = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("ZoneTtl"):
            self.ZoneTtl = params.get("ZoneTtl")


class DeletePdnsZoneRequest(AbstractModel):
    """DeletePdnsZone请求参数结构体
    """

    def __init__(self):
        r"""删除Zone-二期
        :param ZoneId: Zone的ID
        :type PathPrefix: String
        """
        self.ZoneId = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")


class DescribePdnsZonesRequest(AbstractModel):
    """DescribePdnsZones请求参数结构体
    """

    def __init__(self):
        r"""查询Zone-二期
        :param Filter: Zone的Id
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


class BindZoneVpcRequest(AbstractModel):
    """BindZoneVpc请求参数结构体
    """

    def __init__(self):
        r"""为Zone绑定VPC
        :param ZoneId: Zone的ID
        :type PathPrefix: String
        :param Vpcs: 筛选Filter
        :type PathPrefix: Filter
        """
        self.ZoneId = None
        self.Vpcs = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("Vpcs"):
            self.Vpcs = params.get("Vpcs")


class UnbindZoneVpcRequest(AbstractModel):
    """UnbindZoneVpc请求参数结构体
    """

    def __init__(self):
        r"""Zone解绑VPC
        :param ZoneId: Zone的ID
        :type PathPrefix: String
        :param Vpcs: 筛选Filter
        :type PathPrefix: Filter
        """
        self.ZoneId = None
        self.Vpcs = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("Vpcs"):
            self.Vpcs = params.get("Vpcs")


class CreateZoneRecordRequest(AbstractModel):
    """CreateZoneRecord请求参数结构体
    """

    def __init__(self):
        r"""创建Zone解析记录-二期
        :param ZoneId: Zone的ID
        :type PathPrefix: String
        :param RecordName: 记录名称
        :type PathPrefix: String
        :param Type: 记录类型(A | AAAA | MX | CNAME | TXT | SRV | PTR)
        :type PathPrefix: String
        :param RecordTtl: 记录ttl
        :type PathPrefix: Int
        :param RecordValue: 记录值
        :type PathPrefix: String
        """
        self.ZoneId = None
        self.RecordName = None
        self.Type = None
        self.RecordTtl = None
        self.RecordValue = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("RecordName"):
            self.RecordName = params.get("RecordName")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("RecordTtl"):
            self.RecordTtl = params.get("RecordTtl")
        if params.get("RecordValue"):
            self.RecordValue = params.get("RecordValue")


class DeleteZoneRecordRequest(AbstractModel):
    """DeleteZoneRecord请求参数结构体
    """

    def __init__(self):
        r"""删除Zone解析记录
        :param ZoneId: Zone的ID
        :type PathPrefix: String
        :param RecordId: 记录ID
        :type PathPrefix: String
        :param RecordValue: 记录值
        :type PathPrefix: String
        :param Priority: 优先级,记录的Type 为 MX、SRV 需要传入
        :type PathPrefix: String
        :param Weight: 权重,记录的Type 为 SRV 需要传入
        :type PathPrefix: String
        :param Port: 端口,记录的Type 为 SRV 需要传入
        :type PathPrefix: String
        """
        self.ZoneId = None
        self.RecordId = None
        self.RecordValue = None
        self.Priority = None
        self.Weight = None
        self.Port = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("RecordId"):
            self.RecordId = params.get("RecordId")
        if params.get("RecordValue"):
            self.RecordValue = params.get("RecordValue")
        if params.get("Priority"):
            self.Priority = params.get("Priority")
        if params.get("Weight"):
            self.Weight = params.get("Weight")
        if params.get("Port"):
            self.Port = params.get("Port")


class ModifyZoneRecordRequest(AbstractModel):
    """ModifyZoneRecord请求参数结构体
    """

    def __init__(self):
        r"""修改Zone解析记录
        :param ZoneId: Zone的ID
        :type PathPrefix: String
        :param RecordId: 记录ID
        :type PathPrefix: String
        :param RecordValue: 记录值
        :type PathPrefix: String
        :param RecordTtl: 记录ttl
        :type PathPrefix: Int
        """
        self.ZoneId = None
        self.RecordId = None
        self.RecordValue = None
        self.RecordTtl = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("RecordId"):
            self.RecordId = params.get("RecordId")
        if params.get("RecordValue"):
            self.RecordValue = params.get("RecordValue")
        if params.get("RecordTtl"):
            self.RecordTtl = params.get("RecordTtl")


class DescribeZoneRecordRequest(AbstractModel):
    """DescribeZoneRecord请求参数结构体
    """

    def __init__(self):
        r"""查询Zone解析记录 - 二期
        :param ZoneId: Zone的ID
        :type PathPrefix: String
        :param RecordId: 记录的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        """
        self.ZoneId = None
        self.RecordId = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("RecordId"):
            self.RecordId = params.get("RecordId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


