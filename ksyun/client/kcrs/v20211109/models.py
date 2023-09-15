from ksyun.common.abstract_model import AbstractModel

class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体
    """

    def __init__(self):
        r"""创建命名空间
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称，校验规则：长度为2-63位，支持填写小写字母和数字，且不能以数字开头
        :type PathPrefix: String
        :param Public: 命名空间属性，命名空间类型属性决定了该空间下镜像仓库的类型属性有效值：<br/>True：公有<br/>False：私有
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.Public = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("Public"):
            self.Public = params.get("Public")


class DescribeNamespaceRequest(AbstractModel):
    """DescribeNamespace请求参数结构体
    """

    def __init__(self):
        r"""查询命名空间
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称，若不填写，则默认返回该用户所有命名空间
        :type PathPrefix: String
        :param Public: 命名空间属性，有效值：<br/>True：公有<br/>False：私有<br/>注：若不填写，筛选所有命名空间
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.Public = None
        self.MaxResults = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("Public"):
            self.Public = params.get("Public")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ModifyNamespaceTypeRequest(AbstractModel):
    """ModifyNamespaceType请求参数结构体
    """

    def __init__(self):
        r"""修改命名空间类型
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        :param Public: 命名空间属性，有效值：<br/>True：公有<br/>False：私有
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.Public = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("Public"):
            self.Public = params.get("Public")


class DescribeNamespaceExistRequest(AbstractModel):
    """DescribeNamespaceExist请求参数结构体
    """

    def __init__(self):
        r"""查询命名空间是否存在
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体
    """

    def __init__(self):
        r"""删除命名空间
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体
    """

    def __init__(self):
        r"""查询镜像
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param ImageId: 镜像id，若不输入，则默认查询所选镜像仓库下所有镜像
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.RepoName = None
        self.ImageId = None
        self.MaxResults = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class DeleteImagesRequest(AbstractModel):
    """DeleteImages请求参数结构体
    """

    def __init__(self):
        r"""删除镜像
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param ImageId: 镜像id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.RepoName = None
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class DeleteRepoTagRequest(AbstractModel):
    """DeleteRepoTag请求参数结构体
    """

    def __init__(self):
        r"""删除tag
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param TagName: 镜像版本（Tag）名称
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.RepoName = None
        self.TagName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("TagName"):
            self.TagName = params.get("TagName")


class DescribeRepositoryRequest(AbstractModel):
    """DescribeRepository请求参数结构体
    """

    def __init__(self):
        r"""查询仓库
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        :param RepoName: 镜像仓库名称，若不输入，则默认查询所选命名空间下所有镜像仓库
        :type PathPrefix: Filter
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.RepoName = None
        self.MaxResults = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ModifyRepoDescRequest(AbstractModel):
    """ModifyRepoDesc请求参数结构体
    """

    def __init__(self):
        r"""修改仓库描述
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param Desc: 镜像仓库描述信息,长度256字符内
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.RepoName = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository请求参数结构体
    """

    def __init__(self):
        r"""删除仓库
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.RepoName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")


class StartImageScanRequest(AbstractModel):
    """StartImageScan请求参数结构体
    """

    def __init__(self):
        r"""扫描镜像
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param ImageId: 镜像id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.RepoName = None
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class DescribeImageScanRequest(AbstractModel):
    """DescribeImageScan请求参数结构体
    """

    def __init__(self):
        r"""查询镜像扫描
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param ImageId: 镜像id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.RepoName = None
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class CreateInstanceTokenRequest(AbstractModel):
    """CreateInstanceToken请求参数结构体
    """

    def __init__(self):
        r"""创建凭证
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param TokenType: 实例访问凭证过期时间类型，有效值：<br/>Hour：指定时长<br/>Day：指定天数<br/>NeverExpire：永不过期<br/>注：与参数TokenTime搭配使用，用于设置访问凭证到期时间
        :type PathPrefix: String
        :param TokenTime: 实例访问凭证过期时间<br/>注：当参数TokenType设置为NeverExpire时，该参数不生效
        :type PathPrefix: String
        :param Desc: 访问凭证描述信息,长度限制在256字节内
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.TokenType = None
        self.TokenTime = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TokenType"):
            self.TokenType = params.get("TokenType")
        if params.get("TokenTime"):
            self.TokenTime = params.get("TokenTime")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class DescribeInternalEndpointRequest(AbstractModel):
    """DescribeInternalEndpoint请求参数结构体
    """

    def __init__(self):
        r"""DescribeInternalEndpoint
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeInstanceTokenRequest(AbstractModel):
    """DescribeInstanceToken请求参数结构体
    """

    def __init__(self):
        r"""查询凭证
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认20， 最大99
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class CreateInternalEndpointRequest(AbstractModel):
    """CreateInternalEndpoint请求参数结构体
    """

    def __init__(self):
        r"""CreateInternalEndpoint
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param VpcId: vpc id
        :type PathPrefix: String
        :param ReserveSubnetId: 所在vpc的终端子网id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.VpcId = None
        self.ReserveSubnetId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("ReserveSubnetId"):
            self.ReserveSubnetId = params.get("ReserveSubnetId")


class ModifyInstanceTokenStatusRequest(AbstractModel):
    """ModifyInstanceTokenStatus请求参数结构体
    """

    def __init__(self):
        r"""开启/禁用凭证
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param TokenId: 实例访问凭证的id
        :type PathPrefix: String
        :param Enable: 启用/禁用实例访问凭证，有效值：<br/>True：启用<br/>False：禁用
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.TokenId = None
        self.Enable = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TokenId"):
            self.TokenId = params.get("TokenId")
        if params.get("Enable"):
            self.Enable = params.get("Enable")


class DeleteInternalEndpointRequest(AbstractModel):
    """DeleteInternalEndpoint请求参数结构体
    """

    def __init__(self):
        r"""DeleteInternalEndpoint
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param VpcId: vpcid
        :type PathPrefix: String
        :param EniLBIp: 内网访问链路ip
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("EniLBIp"):
            self.EniLBIp = params.get("EniLBIp")


class ModifyInstanceTokenInformationRequest(AbstractModel):
    """ModifyInstanceTokenInformation请求参数结构体
    """

    def __init__(self):
        r"""修改凭证信息
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param TokenId: 实例访问凭证的id
        :type PathPrefix: String
        :param TokenType: 实例访问凭证过期时间类型，有效值：<br/>Hour：指定时长  <br/>Day：指定天数<br/>NeverExpire：永不过期<br/>注：与参数TokenTime搭配使用，用于设置访问凭证到期时间
        :type PathPrefix: String
        :param TokenTime: 实例访问凭证过期时间<br/>注：当参数TokenType设置为NeverExpire时，该参数不生效
        :type PathPrefix: String
        :param Desc: 访问凭证描述信息
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.TokenId = None
        self.TokenType = None
        self.TokenTime = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TokenId"):
            self.TokenId = params.get("TokenId")
        if params.get("TokenType"):
            self.TokenType = params.get("TokenType")
        if params.get("TokenTime"):
            self.TokenTime = params.get("TokenTime")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class DescribeInternalEndpointDnsRequest(AbstractModel):
    """DescribeInternalEndpointDns请求参数结构体
    """

    def __init__(self):
        r"""DescribeInternalEndpointDns
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param VpcId: vpcid
        :type PathPrefix: String
        :param EniLBIp: 内网访问链路ip
        :type PathPrefix: String
        :param InternalEndpointDns: 解析的域名，有效值：<br/>PrivateDomain：内网域名<br/>注：若不填，则默认查询所有域名
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.InternalEndpointDns = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("EniLBIp"):
            self.EniLBIp = params.get("EniLBIp")
        if params.get("InternalEndpointDns"):
            self.InternalEndpointDns = params.get("InternalEndpointDns")


class DeleteInstanceTokenRequest(AbstractModel):
    """DeleteInstanceToken请求参数结构体
    """

    def __init__(self):
        r"""删除凭证
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param TokenId: 实例访问凭证的id
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.TokenId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("TokenId"):
            self.TokenId = params.get("TokenId")


class CreateInternalEndpointDnsRequest(AbstractModel):
    """CreateInternalEndpointDns请求参数结构体
    """

    def __init__(self):
        r"""CreateInternalEndpointDns
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param VpcId: vpcid
        :type PathPrefix: String
        :param EniLBIp: 实例内网访问链路ip
        :type PathPrefix: String
        :param InternalEndpointDns: 解析的域名，有效值：<br/>PrivateDomain：内网域名
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.InternalEndpointDns = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("EniLBIp"):
            self.EniLBIp = params.get("EniLBIp")
        if params.get("InternalEndpointDns"):
            self.InternalEndpointDns = params.get("InternalEndpointDns")


class DeleteInternalEndpointDnsRequest(AbstractModel):
    """DeleteInternalEndpointDns请求参数结构体
    """

    def __init__(self):
        r"""DeleteInternalEndpointDns
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param VpcId: vpcid
        :type PathPrefix: String
        :param EniLBIp: 内网访问链路ip
        :type PathPrefix: String
        :param InternalEndpointDns: 解析的域名，有效值：<br/>PrivateDomain：内网域名
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.InternalEndpointDns = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("EniLBIp"):
            self.EniLBIp = params.get("EniLBIp")
        if params.get("InternalEndpointDns"):
            self.InternalEndpointDns = params.get("InternalEndpointDns")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体
    """

    def __init__(self):
        r"""创建仓库实例
        :param InstanceName: 实例名称<br />校验规则：长度为2-30个字符，支持填写小写英文字母、数字，且不能以数字开头
        :type PathPrefix: String
        :param ChargeType: 实例计费方式，有效值：<br />HourlyInstantSettlement：按量付费<br /> Monthly：包年包月<br />默认值：HourlyInstantSettlement
        :type PathPrefix: String
        :param InstanceType: 实例规格，有效值：<br />basic：基础版<br />premium：高级版
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，单位为月（按年付费请输入12的整数倍）<br />注：当ChargeType参数设置为Monthly时，此项必填
        :type PathPrefix: String
        :param ProjectId: 实例所属项目ID，若不填，则默认为默认项目
        :type PathPrefix: String
        """
        self.InstanceName = None
        self.ChargeType = None
        self.InstanceType = None
        self.PurchaseTime = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体
    """

    def __init__(self):
        r"""删除实例
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param DeleteBucket: 是否随实例删除关联的KS3 Bucket，有效值：<br />True：是<br />False：否<br />默认值：False
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DeleteBucket = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DeleteBucket"):
            self.DeleteBucket = params.get("DeleteBucket")


class DescribeInstanceUsageRequest(AbstractModel):
    """DescribeInstanceUsage请求参数结构体
    """

    def __init__(self):
        r"""查询实例配额
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体
    """

    def __init__(self):
        r"""查询镜像实例信息
        :param InstanceId: 实例id，若不填，则默认查询该地域下的所有实例
        :type PathPrefix: Filter
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99
        :type PathPrefix: String
        :param ProjectId: 实例所属项目ID，若不填，则默认查询默认项目
        :type PathPrefix: Filter
        :param InstanceName: 实例名称，只支持精准匹配
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Marker = None
        self.MaxResults = None
        self.ProjectId = None
        self.InstanceName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")


class CreateWebhookTriggerRequest(AbstractModel):
    """CreateWebhookTrigger请求参数结构体
    """

    def __init__(self):
        r"""创建触发器
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param Trigger: 触发器参数
        :type PathPrefix: String
        :param TriggerName: 触发器名称
        :type PathPrefix: String
        :param EventType: 触发动作，有效值：<br/>PushImage<br/>DeleteImage
        :type PathPrefix: Filter
        :param TriggerUrl: 触发器URL
        :type PathPrefix: String
        :param Header: 自定义Header
        :type PathPrefix: Filter
        :param Enabled: 启用触发器，有效值：<br/>True：是<br/>False：否<br/>默认值：True
        :type PathPrefix: String
        :param Key: Header Key
        :type PathPrefix: String
        :param Value: Header Values
        :type PathPrefix: Filter
        """
        self.InstanceId = None
        self.Namespace = None
        self.Trigger = None
        self.TriggerName = None
        self.EventType = None
        self.TriggerUrl = None
        self.Header = None
        self.Enabled = None
        self.Key = None
        self.Value = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("Trigger"):
            self.Trigger = params.get("Trigger")
        if params.get("TriggerName"):
            self.TriggerName = params.get("TriggerName")
        if params.get("EventType"):
            self.EventType = params.get("EventType")
        if params.get("TriggerUrl"):
            self.TriggerUrl = params.get("TriggerUrl")
        if params.get("Header"):
            self.Header = params.get("Header")
        if params.get("Enabled"):
            self.Enabled = params.get("Enabled")
        if params.get("Key"):
            self.Key = params.get("Key")
        if params.get("Value"):
            self.Value = params.get("Value")


class DescribeWebhookTriggerRequest(AbstractModel):
    """DescribeWebhookTrigger请求参数结构体
    """

    def __init__(self):
        r"""查询触发器
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param TriggerId: 触发器ID
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认10， 最大99
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.TriggerId = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("TriggerId"):
            self.TriggerId = params.get("TriggerId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class ModifyWebhookTriggerRequest(AbstractModel):
    """ModifyWebhookTrigger请求参数结构体
    """

    def __init__(self):
        r"""修改触发器
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param Trigger: 触发器属性
        :type PathPrefix: String
        :param TriggerId: 触发器ID
        :type PathPrefix: String
        :param TriggerName: 触发器名称
        :type PathPrefix: String
        :param EventType: 触发动作，有效值：<br/>PushImage<br/>DeleteImage
        :type PathPrefix: Filter
        :param TriggerUrl: 触发器URL
        :type PathPrefix: String
        :param Header: 自定义Headers
        :type PathPrefix: Filter
        :param Enabled: 启用触发器，有效值：<br/>True：是<br/>False：否
        :type PathPrefix: String
        :param Key: Header Key
        :type PathPrefix: String
        :param Value: Header Values
        :type PathPrefix: Filter
        """
        self.InstanceId = None
        self.Namespace = None
        self.Trigger = None
        self.TriggerId = None
        self.TriggerName = None
        self.EventType = None
        self.TriggerUrl = None
        self.Header = None
        self.Enabled = None
        self.Key = None
        self.Value = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("Trigger"):
            self.Trigger = params.get("Trigger")
        if params.get("TriggerId"):
            self.TriggerId = params.get("TriggerId")
        if params.get("TriggerName"):
            self.TriggerName = params.get("TriggerName")
        if params.get("EventType"):
            self.EventType = params.get("EventType")
        if params.get("TriggerUrl"):
            self.TriggerUrl = params.get("TriggerUrl")
        if params.get("Header"):
            self.Header = params.get("Header")
        if params.get("Enabled"):
            self.Enabled = params.get("Enabled")
        if params.get("Key"):
            self.Key = params.get("Key")
        if params.get("Value"):
            self.Value = params.get("Value")


class DescribeWebhookTriggerLogRequest(AbstractModel):
    """DescribeWebhookTriggerLog请求参数结构体
    """

    def __init__(self):
        r"""查询触发器日志
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param TriggerId: 触发器ID
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认10， 最大99
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.TriggerId = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("TriggerId"):
            self.TriggerId = params.get("TriggerId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class DeleteWebhookTriggerRequest(AbstractModel):
    """DeleteWebhookTrigger请求参数结构体
    """

    def __init__(self):
        r"""删除触发器
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param TriggerId: 触发器ID
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Namespace = None
        self.TriggerId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("TriggerId"):
            self.TriggerId = params.get("TriggerId")


class DescribeAllRepositoryRequest(AbstractModel):
    """DescribeAllRepository请求参数结构体
    """

    def __init__(self):
        r"""查询指定命名空间全部仓库
        """

    def _deserialize(self, params):
        return


class GetMetadataRequest(AbstractModel):
    """GetMetadata请求参数结构体
    """

    def __init__(self):
        r"""获取清理元数据
        """

    def _deserialize(self, params):
        return


class CreateRetentionRuleRequest(AbstractModel):
    """CreateRetentionRule请求参数结构体
    """

    def __init__(self):
        r"""创建镜像清理规则
        """

    def _deserialize(self, params):
        return


class UpdateRetentionRuleRequest(AbstractModel):
    """UpdateRetentionRule请求参数结构体
    """

    def __init__(self):
        r"""更新镜像清理规则
        """

    def _deserialize(self, params):
        return


class DeleteRetentionRuleRequest(AbstractModel):
    """DeleteRetentionRule请求参数结构体
    """

    def __init__(self):
        r"""删除镜像清理规则
        """

    def _deserialize(self, params):
        return


class DescribeRetentionRuleRequest(AbstractModel):
    """DescribeRetentionRule请求参数结构体
    """

    def __init__(self):
        r"""描述镜像清理规则
        """

    def _deserialize(self, params):
        return


class RunRetentionPolicyRequest(AbstractModel):
    """RunRetentionPolicy请求参数结构体
    """

    def __init__(self):
        r"""运行清理保留规则
        """

    def _deserialize(self, params):
        return


class GetRetentionPolicyLogsRequest(AbstractModel):
    """GetRetentionPolicyLogs请求参数结构体
    """

    def __init__(self):
        r"""获取运行日志列表
        """

    def _deserialize(self, params):
        return


class GetRetentionPolicyLogDetailRequest(AbstractModel):
    """GetRetentionPolicyLogDetail请求参数结构体
    """

    def __init__(self):
        r"""获取日志运行详情
        """

    def _deserialize(self, params):
        return


class GetRetentionPolicyLogRequest(AbstractModel):
    """GetRetentionPolicyLog请求参数结构体
    """

    def __init__(self):
        r"""获取日志保留结果
        """

    def _deserialize(self, params):
        return


class GetRetentionTriggerRequest(AbstractModel):
    """GetRetentionTrigger请求参数结构体
    """

    def __init__(self):
        r"""获取触发器
        """

    def _deserialize(self, params):
        return


class UpdateRetentionTriggerRequest(AbstractModel):
    """UpdateRetentionTrigger请求参数结构体
    """

    def __init__(self):
        r"""修改触发器
        """

    def _deserialize(self, params):
        return


class GetNamespacePolicyRequest(AbstractModel):
    """GetNamespacePolicy请求参数结构体
    """

    def __init__(self):
        r"""获取命名空间是否绑定清理规则
        """

    def _deserialize(self, params):
        return


class ScheduleRequest(AbstractModel):
    """Schedule请求参数结构体
    """

    def __init__(self):
        r"""ks3清理
        """

    def _deserialize(self, params):
        return


