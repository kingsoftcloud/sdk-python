from ksyun.common.abstract_model import AbstractModel


class CreateContainerGroupRequest(AbstractModel):
    """CreateContainerGroup请求参数结构体
    """

    def __init__(self):
        r"""创建容器实例组
        :param ContainerGroupName: 容器实例名称，不超过128个字符，只能包含小写字母、数字、和分隔符（“-”，“.”)，不能以分隔符开头或结尾
        :type PathPrefix: String
        :param SubnetId: 子网ID
        :type PathPrefix: String
        :param MultiSubnetId: 子网ID(多值传参用法)，如果SubnetId为空，则该参数为必填，最多传5个
        :type PathPrefix: Filter
        :param SecurityGroupId: 安全组ID，最多3个
        :type PathPrefix: Filter
        :param KciType: 容器实例类型，当前固定为RBKCI
        :type PathPrefix: String
        :param InstanceType: 容器实例底层机型套餐，如N3.4B,没有特殊需求可以不填写，系统以最小规格自动适配，有特殊资源要求的请联系产品咨询所在可用区是否售卖
        :type PathPrefix: String
        :param InstanceFamily: 指定容器实例底层资源机型列表，如N3，如果有多个以英文逗号分隔，如S6,X7。系统按填写顺序从InstanceFamily指定的机型列表自动适配规格。如果填写了InstanceType，则忽略该字段。
        :type PathPrefix: String
        :param ChargeType: 计费方式- HourlyInstantSettlement 按小时实时结算， 所有机型都支持- Spot 竞价实例，有折扣的机型，仅部分机型支持，需要联系产品
        :type PathPrefix: String
        :param SpotStrategy: 竞价实例策略，当计费方式为Spot时，该字段有效，当前固定为SpotAsPriceGo
        :type PathPrefix: String
        :param ProjectId: 项目ID，不填写默认0
        :type PathPrefix: Int
        :param Cpu: 容器实例CPU规格，支持三位小数，最大值256，系统会自动以标准规格适配，如指定的Cpu是2.5核，系统最终可能根据机型还要求开出4核，最小规格去适配
        :type PathPrefix: Double
        :param Memory: 容器实例内存规格，支持最多三位小数，最大512，单位GB。填写3G，最终系统根据机型以最小规格适配可能开出4G标准规格。
        :type PathPrefix: Double
        :param Gpu: Gpu颗数，创建Gpu容器实例时，系统根据Gpu指定的颗数创建符合条件的gpu容器实例，非Gpu机型实例该参数无效
        :type PathPrefix: Double
        :param KubeConfig: 当创建集群模式容器实例时，KubeConfig必须填写
        :type PathPrefix: String
        :param RetainIp: 是否保留ip，当RetainIp为true时，在相同子网下再次创建同名称的实例时，系统会继续使用上一次的ip，但不保证一定成功，ip可能被其它资源抢占。
        :type PathPrefix: Boolean
        :param RetainIpHours: ip保留时间，默认24小时，最大365*24，如果RetainIp为空或者false时，该字段无效
        :type PathPrefix: Int
        :param EipAllocationId: EIP实例ID，容器实例成功启动后会自动进行EIP绑定
        :type PathPrefix: String
        :param AutoMatchImageCache: 自动匹配镜像缓存，默认False
        :type PathPrefix: Boolean
        :param ImageCacheId: 镜像缓存ID，指定镜像缓存，则AutoMatchImageCache无效
        :type PathPrefix: String
        :param AdvanceSettings: 容器实例高级属性设置，主要用于控制容器实例底层KVM的启动配置
        :type PathPrefix: Object
        :param MachineDnsConfig: 容器实例底层云服务器DNS配置
        :type PathPrefix: Object
        :param MachineHostAliase: 容器实例底层云主机host配置，如使用场景：当有自建镜像仓库时，可通过此参数配置host，通过域名拉取vpc下自建仓库镜像
        :type PathPrefix: Filter
        :param RestartPolicy: **创建无集群模式实例时该字段才生效**，Pod重启策略，不填写默认 Always

- Always 总是重启
- OnFailure 失败时重启
- Never 从不重启
        :type PathPrefix: String
        :param ImageRegistryCredential: **创建无集群模式实例时该字段才生效**拉取镜像仓库私有镜像凭据，公开镜像无须填写。
        :type PathPrefix: Filter
        :param Volume: **创建无集群模式实例时该字段必填**
        :type PathPrefix: Filter
        :param Container: **创建无集群模式实例时该字段必填**
        :type PathPrefix: Filter
        :param DnsConfig: **创建无集群模式实例时该字段必填**pod dns配置
        :type PathPrefix: Object
        :param HostAliase: **创建无集群模式实例时该字段必填**pod host配置
        :type PathPrefix: Filter
        :param ClusterDns: **非Serverless集群模式容器实例创建时必填**集群DNS
        :type PathPrefix: String
        :param ClusterDomain: **非Serverless集群模式容器实例创建时必填**集群域名
        :type PathPrefix: String
        :param Label: 创建集群模式容器实例时，cluster-id、namespace、pod-name标签必填，通常该标签由virtual-kubelet组件自动传递。
        :type PathPrefix: Filter
        :param KubeProxy: **创建集群模式容器实例时该字段才生效**KubeProxy配置
        :type PathPrefix: Object
        :param KlogEnabled: **创建集群模式容器实例该字段才生效**pod日志是否采集到klog，默认false，若开启，则按照kce集群的配置的采集规则将日志输出到klog。
        :type PathPrefix: Boolean
        :param DataDisk: **创建集群模式容器实例该字段生效**
实例开机时需要创建的ebs数据盘，主要用于创建集群工作负载中指定了ebs类型的存储卷，最大8块ebs盘，这是底层云服务器的限制。
        :type PathPrefix: Filter
        :param ContainerSpec: **创建集群模式容器实例该字段生效**

pod内部所有容器申请的资源列表，不填写，开出的容器实例就是默认规格大小。
计算规格时，优先以Limit值进行计算，Limit值为空，再以Request值累加计算。
        :type PathPrefix: Filter
        """
        self.ContainerGroupName = None
        self.SubnetId = None
        self.MultiSubnetId = None
        self.SecurityGroupId = None
        self.KciType = None
        self.InstanceType = None
        self.InstanceFamily = None
        self.ChargeType = None
        self.SpotStrategy = None
        self.ProjectId = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.KubeConfig = None
        self.RetainIp = None
        self.RetainIpHours = None
        self.EipAllocationId = None
        self.AutoMatchImageCache = None
        self.ImageCacheId = None
        self.AdvanceSettings = None
        self.MachineDnsConfig = None
        self.MachineHostAliase = None
        self.RestartPolicy = None
        self.ImageRegistryCredential = None
        self.Volume = None
        self.Container = None
        self.DnsConfig = None
        self.HostAliase = None
        self.ClusterDns = None
        self.ClusterDomain = None
        self.Label = None
        self.KubeProxy = None
        self.KlogEnabled = None
        self.DataDisk = None
        self.ContainerSpec = None

    def _deserialize(self, params):
        if params.get("ContainerGroupName"):
            self.ContainerGroupName = params.get("ContainerGroupName")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("MultiSubnetId"):
            self.MultiSubnetId = params.get("MultiSubnetId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("KciType"):
            self.KciType = params.get("KciType")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("InstanceFamily"):
            self.InstanceFamily = params.get("InstanceFamily")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("SpotStrategy"):
            self.SpotStrategy = params.get("SpotStrategy")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Cpu"):
            self.Cpu = params.get("Cpu")
        if params.get("Memory"):
            self.Memory = params.get("Memory")
        if params.get("Gpu"):
            self.Gpu = params.get("Gpu")
        if params.get("KubeConfig"):
            self.KubeConfig = params.get("KubeConfig")
        if params.get("RetainIp"):
            self.RetainIp = params.get("RetainIp")
        if params.get("RetainIpHours"):
            self.RetainIpHours = params.get("RetainIpHours")
        if params.get("EipAllocationId"):
            self.EipAllocationId = params.get("EipAllocationId")
        if params.get("AutoMatchImageCache"):
            self.AutoMatchImageCache = params.get("AutoMatchImageCache")
        if params.get("ImageCacheId"):
            self.ImageCacheId = params.get("ImageCacheId")
        if params.get("AdvanceSettings"):
            self.AdvanceSettings = params.get("AdvanceSettings")
        if params.get("MachineDnsConfig"):
            self.MachineDnsConfig = params.get("MachineDnsConfig")
        if params.get("MachineHostAliase"):
            self.MachineHostAliase = params.get("MachineHostAliase")
        if params.get("RestartPolicy"):
            self.RestartPolicy = params.get("RestartPolicy")
        if params.get("ImageRegistryCredential"):
            self.ImageRegistryCredential = params.get("ImageRegistryCredential")
        if params.get("Volume"):
            self.Volume = params.get("Volume")
        if params.get("Container"):
            self.Container = params.get("Container")
        if params.get("DnsConfig"):
            self.DnsConfig = params.get("DnsConfig")
        if params.get("HostAliase"):
            self.HostAliase = params.get("HostAliase")
        if params.get("ClusterDns"):
            self.ClusterDns = params.get("ClusterDns")
        if params.get("ClusterDomain"):
            self.ClusterDomain = params.get("ClusterDomain")
        if params.get("Label"):
            self.Label = params.get("Label")
        if params.get("KubeProxy"):
            self.KubeProxy = params.get("KubeProxy")
        if params.get("KlogEnabled"):
            self.KlogEnabled = params.get("KlogEnabled")
        if params.get("DataDisk"):
            self.DataDisk = params.get("DataDisk")
        if params.get("ContainerSpec"):
            self.ContainerSpec = params.get("ContainerSpec")


class DescribeContainerGroupRequest(AbstractModel):
    """DescribeContainerGroup请求参数结构体
    """

    def __init__(self):
        r"""查询容器实例组
        :param ContainerGroupId: 容器实例ID
        :type PathPrefix: Filter
        :param MaxResults: 每页返回的最大记录数，最大100
        :type PathPrefix: Int
        :param Marker: 记录起始位置
        :type PathPrefix: Int
        :param ProjectId: 资源项目ID，不指定默认查询有权限的全部项目下资源
        :type PathPrefix: Filter
        :param Search: 容器实例名称关键字模糊匹配查询
        :type PathPrefix: String
        :param Filter: 支持的过滤筛选条件如下：
- subnet-id
- vpc-id
- availability-zone.name、
- status

status常用值范围
- 未知Unknown
- ImagePulling
- Running
- Failed
- Succeeded
        :type PathPrefix: Filter
        """
        self.ContainerGroupId = None
        self.MaxResults = None
        self.Marker = None
        self.ProjectId = None
        self.Search = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("ContainerGroupId"):
            self.ContainerGroupId = params.get("ContainerGroupId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Search"):
            self.Search = params.get("Search")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class DescribeContainerGroupListRequest(AbstractModel):
    """DescribeContainerGroupList请求参数结构体
    """

    def __init__(self):
        r"""用于控制台查询容器实例组列表
        :param Action: 请求Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class DeleteContainerGroupRequest(AbstractModel):
    """DeleteContainerGroup请求参数结构体
    """

    def __init__(self):
        r"""删除容器实例组
        :param ContainerGroupId: 容器实例ID，格式UUID
        :type PathPrefix: String
        """
        self.ContainerGroupId = None

    def _deserialize(self, params):
        if params.get("ContainerGroupId"):
            self.ContainerGroupId = params.get("ContainerGroupId")


class DescribeContainerLogRequest(AbstractModel):
    """DescribeContainerLog请求参数结构体
    """

    def __init__(self):
        r"""查询容器实例组日志
        :param ContainerGroupId: 容器实例ID
        :type PathPrefix: String
        :param ContainerName: 容器名称
        :type PathPrefix: String
        :param Tail: 默认查询最新500行日志，最大2000
        :type PathPrefix: Int
        """
        self.ContainerGroupId = None
        self.ContainerName = None
        self.Tail = None

    def _deserialize(self, params):
        if params.get("ContainerGroupId"):
            self.ContainerGroupId = params.get("ContainerGroupId")
        if params.get("ContainerName"):
            self.ContainerName = params.get("ContainerName")
        if params.get("Tail"):
            self.Tail = params.get("Tail")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体
    """

    def __init__(self):
        r"""查询有权限创建容器实例的机房列表
        :param Action: 请求接口
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class ExecContainerCommandRequest(AbstractModel):
    """ExecContainerCommand请求参数结构体
    """

    def __init__(self):
        r"""生成执行容器命令的webSocketUri
        :param ContainerGroupId: 容器实例ID
        :type PathPrefix: String
        :param ContainerName: 容器实例中运行的容器名
        :type PathPrefix: String
        :param Command: exec执行的命令，如/bin/sh 
        :type PathPrefix: Filter
        :param TTY: 是否保持连接，默认false
        :type PathPrefix: Boolean
        """
        self.ContainerGroupId = None
        self.ContainerName = None
        self.Command = None
        self.TTY = None

    def _deserialize(self, params):
        if params.get("ContainerGroupId"):
            self.ContainerGroupId = params.get("ContainerGroupId")
        if params.get("ContainerName"):
            self.ContainerName = params.get("ContainerName")
        if params.get("Command"):
            self.Command = params.get("Command")
        if params.get("TTY"):
            self.TTY = params.get("TTY")


class DescribeContainerGroupCountRequest(AbstractModel):
    """DescribeContainerGroupCount请求参数结构体
    """

    def __init__(self):
        r"""查询容器实例数量
        :param Label: 
        :type PathPrefix: Object
        """
        self.Label = None

    def _deserialize(self, params):
        if params.get("Label"):
            self.Label = params.get("Label")


class DescribeContainerGroupEventsRequest(AbstractModel):
    """DescribeContainerGroupEvents请求参数结构体
    """

    def __init__(self):
        r"""查询容器实例事件信息
        :param ContainerGroupId: 
        :type PathPrefix: String
        """
        self.ContainerGroupId = None

    def _deserialize(self, params):
        if params.get("ContainerGroupId"):
            self.ContainerGroupId = params.get("ContainerGroupId")


class DescribeKciPackagesRequest(AbstractModel):
    """DescribeKciPackages请求参数结构体
    """

    def __init__(self):
        r"""查询容器实例在各机房可用区支持的标准规格大小
        :param ChargeType: - HourlyInstantSettlement 按小时结算
- Spot 竞价实例
        :type PathPrefix: String
        :param AvailabilityZone: 可用区
        :type PathPrefix: String
        :param KciType: 当前固定值为RBKCI
        :type PathPrefix: String
        """
        self.ChargeType = None
        self.AvailabilityZone = None
        self.KciType = None

    def _deserialize(self, params):
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("KciType"):
            self.KciType = params.get("KciType")


class CreateImageCacheRequest(AbstractModel):
    """CreateImageCache请求参数结构体
    """

    def __init__(self):
        r"""创建容器实例镜像缓存
        :param ImageCacheName: 镜像缓存名称，最长63个字符，名称需符合
`^[a-zA-Z0-9]([-a-zA-Z0-9._]*[a-zA-Z0-9])?$` 格式
        :type PathPrefix: String
        :param SubnetId: 子网ID，创建缓存过程中会创建一个容器实例，占用该子网下一个ip
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param ImageCacheSize: 镜像缓存大小，单位GB，默认20GB，取值范围20-500G，请保证下载的镜像小于等于该大小。
        :type PathPrefix: Int
        :param RetentionDays: 镜像缓存保留天数，最大65536天，不填写或者0则表示永久保留
        :type PathPrefix: Int
        :param Image: 镜像数量，最多20个，镜像必须符合docker镜像格式
        :type PathPrefix: Filter
        :param ImageRegistryCredential: 拉取镜像仓库中私有镜像的凭据，公开镜像无须填写凭据
        :type PathPrefix: Array
        :param ImageCacheType: 镜像缓存类型
- Common 普通型
- Rapid 极速型
        :type PathPrefix: String
        :param EnableWarm: 是否预热，默认false
        :type PathPrefix: Boolean
        """
        self.ImageCacheName = None
        self.SubnetId = None
        self.SecurityGroupId = None
        self.ImageCacheSize = None
        self.RetentionDays = None
        self.Image = None
        self.ImageRegistryCredential = None
        self.ImageCacheType = None
        self.EnableWarm = None

    def _deserialize(self, params):
        if params.get("ImageCacheName"):
            self.ImageCacheName = params.get("ImageCacheName")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("ImageCacheSize"):
            self.ImageCacheSize = params.get("ImageCacheSize")
        if params.get("RetentionDays"):
            self.RetentionDays = params.get("RetentionDays")
        if params.get("Image"):
            self.Image = params.get("Image")
        if params.get("ImageRegistryCredential"):
            self.ImageRegistryCredential = params.get("ImageRegistryCredential")
        if params.get("ImageCacheType"):
            self.ImageCacheType = params.get("ImageCacheType")
        if params.get("EnableWarm"):
            self.EnableWarm = params.get("EnableWarm")


class DeleteImageCacheRequest(AbstractModel):
    """DeleteImageCache请求参数结构体
    """

    def __init__(self):
        r"""删除容器实例镜像缓存
        :param ImageCacheId: 镜像缓存ID
        :type PathPrefix: String
        """
        self.ImageCacheId = None

    def _deserialize(self, params):
        if params.get("ImageCacheId"):
            self.ImageCacheId = params.get("ImageCacheId")


class DescribeImageCacheRequest(AbstractModel):
    """DescribeImageCache请求参数结构体
    """

    def __init__(self):
        r"""查询容器实例镜像缓存
        :param ImageCacheId: 指定镜像缓存ID查询，其它参数ImageCacheName、Image则无效
        :type PathPrefix: Filter
        :param ImageCacheName: 镜像缓存名称关键字模糊匹配，最长63个字符，必须满足 `^[a-zA-Z0-9]([-a-zA-Z0-9._]*[a-zA-Z0-9])?$` 格式
        :type PathPrefix: String
        :param Image: 镜像字符串格式，模糊匹配，如nginx
        :type PathPrefix: String
        :param Marker: 记录起始值
        :type PathPrefix: Int
        :param MaxResults: 单次查询最大记录数，默认20，最大100
        :type PathPrefix: Int
        """
        self.ImageCacheId = None
        self.ImageCacheName = None
        self.Image = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ImageCacheId"):
            self.ImageCacheId = params.get("ImageCacheId")
        if params.get("ImageCacheName"):
            self.ImageCacheName = params.get("ImageCacheName")
        if params.get("Image"):
            self.Image = params.get("Image")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class MatchImageCacheRequest(AbstractModel):
    """MatchImageCache请求参数结构体
    """

    def __init__(self):
        r"""匹配容器实例镜像缓存
        :param Image: 镜像列表，最多支持5个镜像，镜像必须是正确的格式，如

- hub.kce.ksyun.com/ksyun/nginx:1.0
- nginx/nginx:1.0
- nginx:1.0@sha256:1f4f402b9c14f3ae92b11ada1dfe9893a88f0faeb0b2f4b903e2c67a0c3bf0de
        :type PathPrefix: Filter
        """
        self.Image = None

    def _deserialize(self, params):
        if params.get("Image"):
            self.Image = params.get("Image")


class DescribeImageCacheEventRequest(AbstractModel):
    """DescribeImageCacheEvent请求参数结构体
    """

    def __init__(self):
        r"""查询镜像缓存制作事件
        :param ImageCacheId: 镜像缓存ID
        :type PathPrefix: String
        """
        self.ImageCacheId = None

    def _deserialize(self, params):
        if params.get("ImageCacheId"):
            self.ImageCacheId = params.get("ImageCacheId")
