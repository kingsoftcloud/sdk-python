from ksyun.common.abstract_model import AbstractModel

class GetLinesRequest(AbstractModel):
    """GetLines请求参数结构体
    """

    def __init__(self):
        r"""获取用户可选链路信息
        """

    def _deserialize(self, params):
        return


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses请求参数结构体
    """

    def __init__(self):
        r"""描述EIP
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param AllocationId: 多个弹性IP的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        :param State: 弹性IP的状态，已绑定(associate)，未绑定(disassociate)
        :type PathPrefix: String
        :param IpVersion: IP版本
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.AllocationId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None
        self.State = None
        self.IpVersion = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("State"):
            self.State = params.get("State")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")


class AllocateAddressRequest(AbstractModel):
    """AllocateAddress请求参数结构体
    """

    def __init__(self):
        r"""创建EIP
        :param LineId: 线路类型的ID，静态线路暂时停止售卖，请选择bgp线路
        :type PathPrefix: String
        :param BandWidth: 弹性IP的带宽
        :type PathPrefix: Int
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 弹性IP的计费类型
有效值:
- Monthly：包年包月，有到期时间，只能升带宽
- Peak：按量付费（月峰值），无到期时间，可升降带宽
- Daily：按量付费（按日月结），无到期时间，可升降带宽
- TrafficMonthly：按量付费（流量月结），无到期时间，可升降带宽
- DailyPaidByTransfer：按量付费（流量），无到期时间，可升降带宽
- HourlyInstantSettlement：按量付费，无到期时间，可升降带宽
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月时不可缺省。
        :type PathPrefix: Int
        """
        self.LineId = None
        self.BandWidth = None
        self.ProjectId = None
        self.ChargeType = None
        self.PurchaseTime = None

    def _deserialize(self, params):
        if params.get("LineId"):
            self.LineId = params.get("LineId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")


class ReleaseAddressRequest(AbstractModel):
    """ReleaseAddress请求参数结构体
    """

    def __init__(self):
        r"""删除EIP
        :param AllocationId: 弹性IP的ID
        :type PathPrefix: String
        """
        self.AllocationId = None

    def _deserialize(self, params):
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")


class AssociateAddressRequest(AbstractModel):
    """AssociateAddress请求参数结构体
    """

    def __init__(self):
        r"""绑定弹性IP
        :param AllocationId: 弹性IP的ID
        :type PathPrefix: String
        :param InstanceType: 绑定弹性IP的实例类型(Ipfwd|Slb|Havip)
        :type PathPrefix: String
        :param InstanceId: 弹性IP绑定的实例 ID
        :type PathPrefix: String
        :param NetworkInterfaceId: 绑定模式
        :type PathPrefix: String
        :param Mode: 绑定模式，EIP以可见模式绑定辅网卡时需填binded
        :type PathPrefix: String
        :param PrivateIpAddress: 私网IP地址，弹性公网IP以普通模式绑定辅网卡的辅助私网IP地址。主私网IP不填即可
        :type PathPrefix: String
        """
        self.AllocationId = None
        self.InstanceType = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.Mode = None
        self.PrivateIpAddress = None

    def _deserialize(self, params):
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Mode"):
            self.Mode = params.get("Mode")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress请求参数结构体
    """

    def __init__(self):
        r"""解绑弹性IP
        :param AllocationId: 弹性IP的ID
        :type PathPrefix: String
        """
        self.AllocationId = None

    def _deserialize(self, params):
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")


class ModifyAddressRequest(AbstractModel):
    """ModifyAddress请求参数结构体
    """

    def __init__(self):
        r"""更新弹性IP配置
        :param AllocationId: 弹性IP的ID
        :type PathPrefix: String
        :param BandWidth: 弹性IP的带宽
        :type PathPrefix: Int
        """
        self.AllocationId = None
        self.BandWidth = None

    def _deserialize(self, params):
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")


