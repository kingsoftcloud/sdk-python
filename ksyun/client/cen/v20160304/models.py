from ksyun.common.abstract_model import AbstractModel

class CreateCenRequest(AbstractModel):
    """CreateCen请求参数结构体
    """

    def __init__(self):
        r"""CreateCen
        :param CenName: 云企业网的名称
        :type PathPrefix: String
        """
        self.CenName = None

    def _deserialize(self, params):
        if params.get("CenName"):
            self.CenName = params.get("CenName")


class ModifyCenRequest(AbstractModel):
    """ModifyCen请求参数结构体
    """

    def __init__(self):
        r"""ModifyCen
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param CenName: 云企业网的名称
        :type PathPrefix: String
        """
        self.CenId = None
        self.CenName = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("CenName"):
            self.CenName = params.get("CenName")


class DeleteCenRequest(AbstractModel):
    """DeleteCen请求参数结构体
    """

    def __init__(self):
        r"""DeleteCen
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        """
        self.CenId = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")


class DescribeCensRequest(AbstractModel):
    """DescribeCens请求参数结构体
    """

    def __init__(self):
        r"""DescribeCens
        :param CenId: 多个云企业网的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.CenId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class AttachCenInstanceRequest(AbstractModel):
    """AttachCenInstance请求参数结构体
    """

    def __init__(self):
        r"""AttachCenInstance
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param InstanceType: 实例类型
        :type PathPrefix: String
        :param CenRegion: 金山云地域名称
        :type PathPrefix: String
        :param CenInstanceId: 云企业网关联的实例ID
        :type PathPrefix: String
        :param InstanceAccountId: 其他账号的ID，当前账号可缺省
        :type PathPrefix: String
        """
        self.CenId = None
        self.InstanceType = None
        self.CenRegion = None
        self.CenInstanceId = None
        self.InstanceAccountId = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("CenRegion"):
            self.CenRegion = params.get("CenRegion")
        if params.get("CenInstanceId"):
            self.CenInstanceId = params.get("CenInstanceId")
        if params.get("InstanceAccountId"):
            self.InstanceAccountId = params.get("InstanceAccountId")


class DetachCenInstanceRequest(AbstractModel):
    """DetachCenInstance请求参数结构体
    """

    def __init__(self):
        r"""DetachCenInstance
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param CenInstanceId: 云企业网关联的实例ID
        :type PathPrefix: String
        """
        self.CenId = None
        self.CenInstanceId = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("CenInstanceId"):
            self.CenInstanceId = params.get("CenInstanceId")


class DescribeCenInstancesRequest(AbstractModel):
    """DescribeCenInstances请求参数结构体
    """

    def __init__(self):
        r"""DescribeCenInstances
        :param CenInstanceId: 多个云企业网关联的实例ID的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.CenInstanceId = None
        self.MaxResults = None
        self.Filter = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CenInstanceId"):
            self.CenInstanceId = params.get("CenInstanceId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreatCenGrantRequest(AbstractModel):
    """CreatCenGrant请求参数结构体
    """

    def __init__(self):
        r"""CreatCenGrant
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param InstanceType: 实例类型
        :type PathPrefix: String
        :param CenInstanceId: 云企业网关联的实例ID
        :type PathPrefix: String
        :param CenAccountId: 云企业网账号的ID
        :type PathPrefix: String
        """
        self.CenId = None
        self.InstanceType = None
        self.CenInstanceId = None
        self.CenAccountId = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("CenInstanceId"):
            self.CenInstanceId = params.get("CenInstanceId")
        if params.get("CenAccountId"):
            self.CenAccountId = params.get("CenAccountId")


class DeleteCenGrantRequest(AbstractModel):
    """DeleteCenGrant请求参数结构体
    """

    def __init__(self):
        r"""DeleteCenGrant
        :param CenGrantId: 云企业网授权的ID
        :type PathPrefix: String
        """
        self.CenGrantId = None

    def _deserialize(self, params):
        if params.get("CenGrantId"):
            self.CenGrantId = params.get("CenGrantId")


class DescribeCenGrantsRequest(AbstractModel):
    """DescribeCenGrants请求参数结构体
    """

    def __init__(self):
        r"""DescribeCenGrants
        :param CenGrantId: 多个云企业网授权的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.CenGrantId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CenGrantId"):
            self.CenGrantId = params.get("CenGrantId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeRegionGroupsRequest(AbstractModel):
    """DescribeRegionGroups请求参数结构体
    """

    def __init__(self):
        r"""DescribeRegionGroups
        :param RegionGroupId: 多个地域组的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.RegionGroupId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("RegionGroupId"):
            self.RegionGroupId = params.get("RegionGroupId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateCenBandWidthPackageRequest(AbstractModel):
    """CreateCenBandWidthPackage请求参数结构体
    """

    def __init__(self):
        r"""CreateCenBandWidthPackage
        :param CenId: 云企业网ID
        :type PathPrefix: String
        :param Name: 带宽包的名称
        :type PathPrefix: String
        :param RegionAGroupId: 地域组A的ID
        :type PathPrefix: String
        :param RegionBGroupId: 地域组B的ID
        :type PathPrefix: String
        :param BandWidth: 带宽值
        :type PathPrefix: Int
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 计费类型 (Monthly|Peak|Daily|Hourly|PrepaidByTime|PostpaidByTime|TrafficMonthly)
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月时不可缺省。
        :type PathPrefix: Int
        """
        self.CenId = None
        self.Name = None
        self.RegionAGroupId = None
        self.RegionBGroupId = None
        self.BandWidth = None
        self.ProjectId = None
        self.ChargeType = None
        self.PurchaseTime = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("RegionAGroupId"):
            self.RegionAGroupId = params.get("RegionAGroupId")
        if params.get("RegionBGroupId"):
            self.RegionBGroupId = params.get("RegionBGroupId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")


class ModifyCenBandWidthPackageRequest(AbstractModel):
    """ModifyCenBandWidthPackage请求参数结构体
    """

    def __init__(self):
        r"""ModifyCenBandWidthPackage
        :param CenBandWidthPackageId: 云企业网带宽包的ID
        :type PathPrefix: String
        :param BandWidth: 带宽值
        :type PathPrefix: Int
        """
        self.CenBandWidthPackageId = None
        self.BandWidth = None

    def _deserialize(self, params):
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")


class DeleteCenBandWidthPackageRequest(AbstractModel):
    """DeleteCenBandWidthPackage请求参数结构体
    """

    def __init__(self):
        r"""DeleteCenBandWidthPackage
        :param CenBandWidthPackageId: 云企业网带宽包的ID
        :type PathPrefix: String
        """
        self.CenBandWidthPackageId = None

    def _deserialize(self, params):
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")


class AttachCenBandWidthPackageRequest(AbstractModel):
    """AttachCenBandWidthPackage请求参数结构体
    """

    def __init__(self):
        r"""AttachCenBandWidthPackage
        :param CenBandWidthPackageId: 云企业网带宽包的ID
        :type PathPrefix: String
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        """
        self.CenBandWidthPackageId = None
        self.CenId = None

    def _deserialize(self, params):
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")
        if params.get("CenId"):
            self.CenId = params.get("CenId")


class DetachCenBandWidthPackageRequest(AbstractModel):
    """DetachCenBandWidthPackage请求参数结构体
    """

    def __init__(self):
        r"""DetachCenBandWidthPackage
        :param CenBandWidthPackageId: 云企业网带宽包的ID
        :type PathPrefix: String
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        """
        self.CenBandWidthPackageId = None
        self.CenId = None

    def _deserialize(self, params):
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")
        if params.get("CenId"):
            self.CenId = params.get("CenId")


class DescribeCenBandWidthPackagesRequest(AbstractModel):
    """DescribeCenBandWidthPackages请求参数结构体
    """

    def __init__(self):
        r"""DescribeCenBandWidthPackages
        :param ProjectId: 项目的ID
        :type PathPrefix: Filter
        :param CenBandWidthPackageId: 多个带宽包的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.CenBandWidthPackageId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateCenRegionBandwidthRequest(AbstractModel):
    """CreateCenRegionBandwidth请求参数结构体
    """

    def __init__(self):
        r"""CreateCenRegionBandwidth
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param RegionA: A机房Code
        :type PathPrefix: String
        :param RegionB: B机房Code
        :type PathPrefix: String
        :param CenBandWidthPackageId: 云企业网带宽包ID
        :type PathPrefix: String
        :param BandWidth: 带宽
        :type PathPrefix: Int
        """
        self.CenId = None
        self.RegionA = None
        self.RegionB = None
        self.CenBandWidthPackageId = None
        self.BandWidth = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("RegionA"):
            self.RegionA = params.get("RegionA")
        if params.get("RegionB"):
            self.RegionB = params.get("RegionB")
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")


class DeleteCenRegionBandwidthRequest(AbstractModel):
    """DeleteCenRegionBandwidth请求参数结构体
    """

    def __init__(self):
        r"""DeleteCenRegionBandwidth
        :param CenRegionBandwidthId: 跨地域带宽的ID
        :type PathPrefix: String
        """
        self.CenRegionBandwidthId = None

    def _deserialize(self, params):
        if params.get("CenRegionBandwidthId"):
            self.CenRegionBandwidthId = params.get("CenRegionBandwidthId")


class ModifyCenRegionBandwidthRequest(AbstractModel):
    """ModifyCenRegionBandwidth请求参数结构体
    """

    def __init__(self):
        r"""ModifyCenRegionBandwidth
        :param CenRegionBandwidthId: 跨地域带宽的ID
        :type PathPrefix: String
        :param BandWidth: 带宽
        :type PathPrefix: String
        """
        self.CenRegionBandwidthId = None
        self.BandWidth = None

    def _deserialize(self, params):
        if params.get("CenRegionBandwidthId"):
            self.CenRegionBandwidthId = params.get("CenRegionBandwidthId")
        if params.get("BandWidth"):
            self.BandWidth = params.get("BandWidth")


class DescribeCenRegionBandwidthsRequest(AbstractModel):
    """DescribeCenRegionBandwidths请求参数结构体
    """

    def __init__(self):
        r"""DescribeCenRegionBandwidths
        :param CenRegionBandwidthId: 多个跨地域带宽的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.CenRegionBandwidthId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CenRegionBandwidthId"):
            self.CenRegionBandwidthId = params.get("CenRegionBandwidthId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeCenRoutesRequest(AbstractModel):
    """DescribeCenRoutes请求参数结构体
    """

    def __init__(self):
        r"""DescribeCenRoutes
        :param CenRouteId: 多个云企业网路由的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.CenRouteId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CenRouteId"):
            self.CenRouteId = params.get("CenRouteId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeCenRegionsRequest(AbstractModel):
    """DescribeCenRegions请求参数结构体
    """

    def __init__(self):
        r"""DescribeCenRegions
        :param CenRegionId: 多个云企业网机房的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.CenRegionId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("CenRegionId"):
            self.CenRegionId = params.get("CenRegionId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeCenBandWidthPackageUsageRequest(AbstractModel):
    """DescribeCenBandWidthPackageUsage请求参数结构体
    """

    def __init__(self):
        r"""DescribeCenBandWidthPackageUsage
        :param CenBandWidthPackageId: 云企业网带宽包的ID
        :type PathPrefix: String
        """
        self.CenBandWidthPackageId = None

    def _deserialize(self, params):
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")


