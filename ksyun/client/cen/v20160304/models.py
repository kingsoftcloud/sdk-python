from ksyun.common.abstract_model import AbstractModel

class CreateCenRequest(AbstractModel):
    """CreateCen请求参数结构体
    """

    def __init__(self):
        r"""CreateCen
        :param CenName: 云企业网的名称
        :type PathPrefix: String
        :param Description: 云企业网的描述
        :type PathPrefix: String
        """
        self.CenName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("CenName"):
            self.CenName = params.get("CenName")
        if params.get("Description"):
            self.Description = params.get("Description")


class ModifyCenRequest(AbstractModel):
    """ModifyCen请求参数结构体
    """

    def __init__(self):
        r"""ModifyCen
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param CenName: 云企业网的名称
        :type PathPrefix: String
        :param Description: 云企业网的描述
        :type PathPrefix: String
        """
        self.CenId = None
        self.CenName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("CenName"):
            self.CenName = params.get("CenName")
        if params.get("Description"):
            self.Description = params.get("Description")


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
        r"""查询云企业网信息
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


class CreateCenBandWidthPackageRequest(AbstractModel):
    """CreateCenBandWidthPackage请求参数结构体
    """

    def __init__(self):
        r"""CreateCenBandWidthPackage
        :param CenId: 云企业网ID
        :type PathPrefix: String
        :param CenBandWidthPackageName: 带宽包的名称
        :type PathPrefix: String
        :param LocalAreaId: 本端区域ID
        :type PathPrefix: String
        :param RemoteAreaId: 远端区域ID
        :type PathPrefix: String
        :param PackageBandWidth: 带宽值
        :type PathPrefix: Int
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 计费类型 (Monthly|Daily)
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月Monthly时不可缺省。
        :type PathPrefix: Int
        """
        self.CenId = None
        self.CenBandWidthPackageName = None
        self.LocalAreaId = None
        self.RemoteAreaId = None
        self.PackageBandWidth = None
        self.ProjectId = None
        self.ChargeType = None
        self.PurchaseTime = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("CenBandWidthPackageName"):
            self.CenBandWidthPackageName = params.get("CenBandWidthPackageName")
        if params.get("LocalAreaId"):
            self.LocalAreaId = params.get("LocalAreaId")
        if params.get("RemoteAreaId"):
            self.RemoteAreaId = params.get("RemoteAreaId")
        if params.get("PackageBandWidth"):
            self.PackageBandWidth = params.get("PackageBandWidth")
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
        :param PackageBandWidth: 带宽值
        :type PathPrefix: Int
        :param CenBandWidthPackageName: 带宽包的名称
        :type PathPrefix: String
        """
        self.CenBandWidthPackageId = None
        self.PackageBandWidth = None
        self.CenBandWidthPackageName = None

    def _deserialize(self, params):
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")
        if params.get("PackageBandWidth"):
            self.PackageBandWidth = params.get("PackageBandWidth")
        if params.get("CenBandWidthPackageName"):
            self.CenBandWidthPackageName = params.get("CenBandWidthPackageName")


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
        :param TagKey: 多个标签的键
        :type PathPrefix: Filter
        :param TagKV: 多个标签的键
        :type PathPrefix: Filter
        """
        self.ProjectId = None
        self.CenBandWidthPackageId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None
        self.TagKey = None
        self.TagKV = None

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
        if params.get("TagKey"):
            self.TagKey = params.get("TagKey")
        if params.get("TagKV"):
            self.TagKV = params.get("TagKV")


class CreateCenRegionBandwidthRequest(AbstractModel):
    """CreateCenRegionBandwidth请求参数结构体
    """

    def __init__(self):
        r"""CreateCenRegionBandwidth
        :param LocalRegion: 本端机房Code
        :type PathPrefix: String
        :param RemoteRegion: 远端机房Code
        :type PathPrefix: String
        :param CenBandWidthPackageId: 云企业网带宽包的ID
        :type PathPrefix: String
        :param InterBandWidth: 跨地域的带宽值
        :type PathPrefix: Int
        """
        self.LocalRegion = None
        self.RemoteRegion = None
        self.CenBandWidthPackageId = None
        self.InterBandWidth = None

    def _deserialize(self, params):
        if params.get("LocalRegion"):
            self.LocalRegion = params.get("LocalRegion")
        if params.get("RemoteRegion"):
            self.RemoteRegion = params.get("RemoteRegion")
        if params.get("CenBandWidthPackageId"):
            self.CenBandWidthPackageId = params.get("CenBandWidthPackageId")
        if params.get("InterBandWidth"):
            self.InterBandWidth = params.get("InterBandWidth")


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
        :param InterBandWidth: 跨地域间分配的带宽
        :type PathPrefix: String
        """
        self.CenRegionBandwidthId = None
        self.InterBandWidth = None

    def _deserialize(self, params):
        if params.get("CenRegionBandwidthId"):
            self.CenRegionBandwidthId = params.get("CenRegionBandwidthId")
        if params.get("InterBandWidth"):
            self.InterBandWidth = params.get("InterBandWidth")


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


class DescribeNetworkInstancesRequest(AbstractModel):
    """DescribeNetworkInstances请求参数结构体
    """

    def __init__(self):
        r"""DescribeNetworkInstances
        :param NetworkInstanceId: 多个云企业网关联的实例ID的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.NetworkInstanceId = None
        self.MaxResults = None
        self.Filter = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("NetworkInstanceId"):
            self.NetworkInstanceId = params.get("NetworkInstanceId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateCenGrantRequest(AbstractModel):
    """CreateCenGrant请求参数结构体
    """

    def __init__(self):
        r"""CreateCenGrant
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param InstanceType: 实例类型
        :type PathPrefix: String
        :param NetworkInstanceId: 云企业网关联的实例ID
        :type PathPrefix: String
        :param CenAccountId: 云企业网账号的ID
        :type PathPrefix: String
        """
        self.CenId = None
        self.InstanceType = None
        self.NetworkInstanceId = None
        self.CenAccountId = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("NetworkInstanceId"):
            self.NetworkInstanceId = params.get("NetworkInstanceId")
        if params.get("CenAccountId"):
            self.CenAccountId = params.get("CenAccountId")


class DescribeInterAreasRequest(AbstractModel):
    """DescribeInterAreas请求参数结构体
    """

    def __init__(self):
        r"""DescribeInterAreas
        :param InterAreaId: 互通大区的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.InterAreaId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("InterAreaId"):
            self.InterAreaId = params.get("InterAreaId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeInterRegionsRequest(AbstractModel):
    """DescribeInterRegions请求参数结构体
    """

    def __init__(self):
        r"""DescribeInterRegions
        :param InterRegionId: 云企业网地域ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.InterRegionId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("InterRegionId"):
            self.InterRegionId = params.get("InterRegionId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class AttachNetworkInstanceRequest(AbstractModel):
    """AttachNetworkInstance请求参数结构体
    """

    def __init__(self):
        r"""AttachNetworkInstance
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param InstanceType: 网络实例类型
        :type PathPrefix: String
        :param InstanceRegion: 金山云地域名称
        :type PathPrefix: String
        :param NetworkInstanceId: 网络实例ID
        :type PathPrefix: String
        :param InstanceAccountId: 其他账号的ID，当前账号可缺省
        :type PathPrefix: String
        """
        self.CenId = None
        self.InstanceType = None
        self.InstanceRegion = None
        self.NetworkInstanceId = None
        self.InstanceAccountId = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("InstanceRegion"):
            self.InstanceRegion = params.get("InstanceRegion")
        if params.get("NetworkInstanceId"):
            self.NetworkInstanceId = params.get("NetworkInstanceId")
        if params.get("InstanceAccountId"):
            self.InstanceAccountId = params.get("InstanceAccountId")


class DetachNetworkInstanceRequest(AbstractModel):
    """DetachNetworkInstance请求参数结构体
    """

    def __init__(self):
        r"""DetachNetworkInstance
        :param CenId: 云企业网的ID
        :type PathPrefix: String
        :param NetworkInstanceId: 网络实例ID
        :type PathPrefix: String
        """
        self.CenId = None
        self.NetworkInstanceId = None

    def _deserialize(self, params):
        if params.get("CenId"):
            self.CenId = params.get("CenId")
        if params.get("NetworkInstanceId"):
            self.NetworkInstanceId = params.get("NetworkInstanceId")


class CenCidrPublishRequest(AbstractModel):
    """CenCidrPublish请求参数结构体
    """

    def __init__(self):
        r"""发布云企业网网络实例的路由
        :param NetworkInstanceId: 网络实例的ID
        :type PathPrefix: String
        :param InstanceType: 网络实例类型
        :type PathPrefix: String
        :param NetworkRouteId: 网络路由的ID
        :type PathPrefix: Filter
        :param SelfDefineCidr: 网络实例发布的自定义网段
        :type PathPrefix: Filter
        :param CenId: CenId
        :type PathPrefix: String
        """
        self.NetworkInstanceId = None
        self.InstanceType = None
        self.NetworkRouteId = None
        self.SelfDefineCidr = None
        self.CenId = None

    def _deserialize(self, params):
        if params.get("NetworkInstanceId"):
            self.NetworkInstanceId = params.get("NetworkInstanceId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("NetworkRouteId"):
            self.NetworkRouteId = params.get("NetworkRouteId")
        if params.get("SelfDefineCidr"):
            self.SelfDefineCidr = params.get("SelfDefineCidr")
        if params.get("CenId"):
            self.CenId = params.get("CenId")


class CenCidrDeleteRequest(AbstractModel):
    """CenCidrDelete请求参数结构体
    """

    def __init__(self):
        r"""撤销云企业网网络实例的路由
        :param NetworkInstanceId: 网络实例的ID
        :type PathPrefix: String
        :param InstanceType: 网络实例类型
        :type PathPrefix: String
        :param NetworkRouteId: 网络路由的ID
        :type PathPrefix: Filter
        :param SelfRouteId: 自定义网段路由的ID
        :type PathPrefix: Filter
        :param CenId: 云企业网ID
        :type PathPrefix: String
        """
        self.NetworkInstanceId = None
        self.InstanceType = None
        self.NetworkRouteId = None
        self.SelfRouteId = None
        self.CenId = None

    def _deserialize(self, params):
        if params.get("NetworkInstanceId"):
            self.NetworkInstanceId = params.get("NetworkInstanceId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("NetworkRouteId"):
            self.NetworkRouteId = params.get("NetworkRouteId")
        if params.get("SelfRouteId"):
            self.SelfRouteId = params.get("SelfRouteId")
        if params.get("CenId"):
            self.CenId = params.get("CenId")


