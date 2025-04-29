from ksyun.common.abstract_model import AbstractModel


class CreateBandWidthShareRequest(AbstractModel):
    """CreateBandWidthShare请求参数结构体
    """

    def __init__(self):
        r"""创建共享带宽
        :param LineId: 线路类型的ID
        :type PathPrefix: String
        :param BandWidth: 共享带宽的带宽
        :type PathPrefix: Int
        :param BandWidthShareName: 共享带宽的名称
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 共享带宽的计费类型
        :type PathPrefix: String
        """
        self.LineId = None
        self.BandWidth = None
        self.BandWidthShareName = None
        self.ProjectId = None
        self.ChargeType = None

    def _deserialize(self, params):
        if params.get("LineId"):
            self.LineId = params.get("LineId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")
        if params.get("BandWidthShareName"):
            self.BandWidthShareName = params.get("BandWidthShareName")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")


class DescribeBandWidthSharesRequest(AbstractModel):
    """DescribeBandWidthShares请求参数结构体
    """

    def __init__(self):
        r"""描述共享带宽
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param BandWidthShareId: 多个共享带宽的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.BandWidthShareId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class AssociateBandWidthShareRequest(AbstractModel):
    """AssociateBandWidthShare请求参数结构体
    """

    def __init__(self):
        r"""绑定共享带宽
        :param BandWidthShareId: 共享带宽的ID
        :type PathPrefix: String
        :param AllocationId: 弹性IP的ID
        :type PathPrefix: String
        """
        self.BandWidthShareId = None
        self.AllocationId = None

    def _deserialize(self, params):
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")


class DisassociateBandWidthShareRequest(AbstractModel):
    """DisassociateBandWidthShare请求参数结构体
    """

    def __init__(self):
        r"""解绑共享带宽
        :param BandWidthShareId: 共享带宽的ID
        :type PathPrefix: String
        :param AllocationId: 弹性IP的ID
        :type PathPrefix: String
        :param BandWidth: 弹性IP的带宽
        :type PathPrefix: Int
        """
        self.BandWidthShareId = None
        self.AllocationId = None
        self.BandWidth = None

    def _deserialize(self, params):
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")
        if params.get("AllocationId"):
            self.AllocationId = params.get("AllocationId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")


class ModifyBandWidthShareRequest(AbstractModel):
    """ModifyBandWidthShare请求参数结构体
    """

    def __init__(self):
        r"""更新共享带宽配置
        :param BandWidthShareId: 共享带宽的ID
        :type PathPrefix: String
        :param BandWidth: 共享带宽的带宽
        :type PathPrefix: Int
        :param BandWidthShareName: 共享带宽的名称
        :type PathPrefix: String
        """
        self.BandWidthShareId = None
        self.BandWidth = None
        self.BandWidthShareName = None

    def _deserialize(self, params):
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")
        if params.get("BandWidthShareName"):
            self.BandWidthShareName = params.get("BandWidthShareName")


class DeleteBandWidthShareRequest(AbstractModel):
    """DeleteBandWidthShare请求参数结构体
    """

    def __init__(self):
        r"""删除共享带宽
        :param BandWidthShareId: 共享带宽的ID
        :type PathPrefix: String
        """
        self.BandWidthShareId = None

    def _deserialize(self, params):
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")


class QueryBwsTopEipMonitorRequest(AbstractModel):
    """QueryBwsTopEipMonitor请求参数结构体
    """

    def __init__(self):
        r"""查询BWS下EIP流量排名的TOP 50的网卡
        :param BandWidthShareId: 共享带宽的ID
        :type PathPrefix: String
        :param StartTime: 开始时间，开始时间和结束时间相差10分钟,例如：2023-09-14T13:30:01
        :type PathPrefix: String
        :param EndTime: 结束时间，开始时间和结束时间相差10分钟，例如：2023-09-14T13:40:01
        :type PathPrefix: String
        :param SortType: 排序顺序，默认是OUT，可选OUT|IN,区分大小写，填写其他的字符按OUT排序
        :type PathPrefix: String
        :param PublicIp: 筛选ip
        :type PathPrefix: String
        """
        self.BandWidthShareId = None
        self.StartTime = None
        self.EndTime = None
        self.SortType = None
        self.PublicIp = None

    def _deserialize(self, params):
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("SortType"):
            self.SortType = params.get("SortType")
        if params.get("PublicIp"):
            self.PublicIp = params.get("PublicIp")
