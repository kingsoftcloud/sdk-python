from ksyun.common.abstract_model import AbstractModel

class CreateEpcRequest(AbstractModel):
    """CreateEpc请求参数结构体
    """

    def __init__(self):
        r"""CreateEpc
        :param HostType: 
- 裸金属服务器机型
- 有效值:
	- CPU型
		- CAL：标准计算型
		- CAL-III：标准计算III型
		- CAL-IV：标准计算IV型
		- CAL-V：标准计算V型
		- MI-I1：标准计算II型
		- DB：标准存储型
		- DB-I：存储I型
		- DB-II：标准存储II型
		- DB-III：标准存储III型
		- DB-III-I：标准存储III型-I
		- DB-IV：标准存储IV型
		- DB-V：标准存储V型
		- DB-VI：标准存储VI型
		- DB-VII：标准存储VII型
		- DB-VIII：标准存储VIII型
		- SSD：计算优化型
		- SSD-III：计算效能型
		- SSD-III-II：计算效能型-II
		- SSD-VI：计算效能II型
		- MI-I2：存储优化型
		- MEM-I：内存I型
		- EC-I：高性能计算型
		- EIO-I：极致IO型
		- EIO-III：极致IO型-III
		- EIOS：极致IO存储型
		- SSDS-II：存储优化II型
		- SSDS-III：存储优化III型
		- SSDS-V：存储优化V型
		- EC-I-V-III：高性能计算型-V-III
		- EC-I-V-V：高性能计算型-V-V
		- EC-I-V-VI：高性能计算型-V-VI
	- GPU型	
		- GPU-I：GPU I型
		- P3E：GPU裸金属服务器实例标准型
		- P3E-R：GPU裸金属服务器实例标准集群型
		- P3X：GPU裸金属服务器实例效能型
		- P3X-R：GPU裸金属服务器实例效能集群型
		- P3S：GPU裸金属服务器实例性能型
		- P3IE：GPU裸金属服务器实例推理型
		- P4E.56F8：标准计算型
		- P4X.56D8：效能计算型
		- GN6-I：推理II型-I
		- GN6-II：推理II型-II
		- GN6-III：推理II型-III
		- GN3-II：推理I型-II
		- GN3-III：推理I型-III
		- GND5：效能V型
		- CMLU1：寒武纪I型
		- ...
        :type PathPrefix: String
        :param AvailabilityZone: 可用区的名称
        :type PathPrefix: String
        :param Raid: 数据盘Raid级别,和数据盘的数量直接相关 
有效值：  Raid1：数据盘数量必须是2的倍数
Raid5：数据盘的数量必须大于等于3
Raid10：数据盘数量必须是4的倍数
Raid50：数据盘的数量必须大于6且是2的倍数
SRaid0：单盘SRaid0无限制，仅针对大数据业务自身有冗余的场景
与RaidId必填其一，RaidId优先级高
        :type PathPrefix: String
        :param RaidId: Raid模板Id
        :type PathPrefix: String
        :param ImageId: 镜像资源ID,参见DescribeImages
        :type PathPrefix: String
        :param NetworkInterfaceMode: 网卡模式
-有效值：
-bond4：BOND模式
-single ：非BOND模式
-dual：双网卡模式
        :type PathPrefix: String
        :param SubnetId: 云物理主机的子网ID
        :type PathPrefix: String
        :param PrivateIpAddress: 内网资源IP地址
        :type PathPrefix: String
        :param keyId: 用户密钥对的资源ID
        :type PathPrefix: String
        :param SecurityGroupId: 裸金属服务器关联的安全组ID，一个裸金属服务器最多可以支持3个安全组
        :type PathPrefix: Filter
        :param DNS1: DNS1的值，当通过该接口进行修改网络配置时不填写此参数，保持与之前不变
        :type PathPrefix: String
        :param DNS2: DNS2的值，当通过该接口进行修改网络配置时不填写此参数，保持与之前不变
        :type PathPrefix: String
        :param HostName: 云物理主机名称
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 云物理主机计费类型，包年包月Monthly，按日月结Daily
-有效值：Monthly | Daily
        :type PathPrefix: String
        :param Sn: 云物理主机序列号
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月时不可缺省。
        :type PathPrefix: Int
        :param Password: 系统的登录密码
        :type PathPrefix: String
        :param SecurityAgent: 安全组件类型
- classic：经典版
- no：不开启
        :type PathPrefix: String
        :param CloudMonitorAgent: 安全组件类型
- classic：经典版
- no：不开启
        :type PathPrefix: String
        :param ExtensionSubnetId: 从网卡的子网ID
        :type PathPrefix: String
        :param ExtensionPrivateIpAddress: 从网卡在VPC中的IP
        :type PathPrefix: String
        :param ExtensionDNS1: DNS1的值
        :type PathPrefix: String
        :param ExtensionDNS2: DNS2的值
        :type PathPrefix: String
        :param Description: 描述信息
        :type PathPrefix: String
        :param AddressBandWidth: 弹性IP的带宽
        :type PathPrefix: String
        :param LineId: 弹性IP的链路类型的ID
        :type PathPrefix: String
        :param BandWidthShareId: 共享带宽ID
        :type PathPrefix: String
        :param AddressChargeType: 弹性IP的计费类型
        :type PathPrefix: String
        :param AddressPurchaseTime: 购买时长，只有购买包年包月弹性IP时不可缺省
        :type PathPrefix: String
        :param AddressProjectId: 弹性IP项目的ID
        :type PathPrefix: String
        :param SystemFileType: 系统盘文件格式
        :type PathPrefix: String
        :param DataFileType: 数据盘文件格式
        :type PathPrefix: String
        :param DataDiskCatalogue: 数据盘目录
        :type PathPrefix: String
        :param DataDiskCatalogueSuffix: 数据盘目录后缀属性
        :type PathPrefix: String
        :param HyperThreading: 对超线程的变更
        :type PathPrefix: String
        :param NvmeDataFileType: NVME数据盘类型
        :type PathPrefix: String
        :param NvmeDataDiskCatalogue: NVME数据盘目录
        :type PathPrefix: String
        :param NvmeDataDiskCatalogueSuffix: NVME数据盘目录后缀属性
        :type PathPrefix: String
        :param bondAttribute: 网卡bond的属性
        :type PathPrefix: String
        :param ContainerAgent: 容器引擎组件类型
        :type PathPrefix: String
        :param KesAgent: kes组件类型
        :type PathPrefix: String
        :param KmrAgent: KMR组件类型
        :type PathPrefix: String
        :param ComputerName: 计算机系统内名称
        :type PathPrefix: String
        :param OverclockingAttribute: 超频
        :type PathPrefix: String
        :param GpuImageDriverId: gpu版本
        :type PathPrefix: String
        :param SystemVolumeType: 云硬盘的系统盘类型
        :type PathPrefix: String
        :param SystemVolumeSize: 云硬盘系统盘大小
        :type PathPrefix: String
        :param RoceNetwork: roce网络
有效值： Open：开启  Close：关闭 




        :type PathPrefix: String
        """
        self.HostType = None
        self.AvailabilityZone = None
        self.Raid = None
        self.RaidId = None
        self.ImageId = None
        self.NetworkInterfaceMode = None
        self.SubnetId = None
        self.PrivateIpAddress = None
        self.keyId = None
        self.SecurityGroupId = None
        self.DNS1 = None
        self.DNS2 = None
        self.HostName = None
        self.ProjectId = None
        self.ChargeType = None
        self.Sn = None
        self.PurchaseTime = None
        self.Password = None
        self.SecurityAgent = None
        self.CloudMonitorAgent = None
        self.ExtensionSubnetId = None
        self.ExtensionPrivateIpAddress = None
        self.ExtensionDNS1 = None
        self.ExtensionDNS2 = None
        self.Description = None
        self.AddressBandWidth = None
        self.LineId = None
        self.BandWidthShareId = None
        self.AddressChargeType = None
        self.AddressPurchaseTime = None
        self.AddressProjectId = None
        self.SystemFileType = None
        self.DataFileType = None
        self.DataDiskCatalogue = None
        self.DataDiskCatalogueSuffix = None
        self.HyperThreading = None
        self.NvmeDataFileType = None
        self.NvmeDataDiskCatalogue = None
        self.NvmeDataDiskCatalogueSuffix = None
        self.bondAttribute = None
        self.ContainerAgent = None
        self.KesAgent = None
        self.KmrAgent = None
        self.ComputerName = None
        self.OverclockingAttribute = None
        self.GpuImageDriverId = None
        self.SystemVolumeType = None
        self.SystemVolumeSize = None
        self.RoceNetwork = None

    def _deserialize(self, params):
        if params.get("HostType"):
            self.HostType = params.get("HostType")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("Raid"):
            self.Raid = params.get("Raid")
        if params.get("RaidId"):
            self.RaidId = params.get("RaidId")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("NetworkInterfaceMode"):
            self.NetworkInterfaceMode = params.get("NetworkInterfaceMode")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("keyId"):
            self.keyId = params.get("keyId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("DNS1"):
            self.DNS1 = params.get("DNS1")
        if params.get("DNS2"):
            self.DNS2 = params.get("DNS2")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("Sn"):
            self.Sn = params.get("Sn")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("SecurityAgent"):
            self.SecurityAgent = params.get("SecurityAgent")
        if params.get("CloudMonitorAgent"):
            self.CloudMonitorAgent = params.get("CloudMonitorAgent")
        if params.get("ExtensionSubnetId"):
            self.ExtensionSubnetId = params.get("ExtensionSubnetId")
        if params.get("ExtensionPrivateIpAddress"):
            self.ExtensionPrivateIpAddress = params.get("ExtensionPrivateIpAddress")
        if params.get("ExtensionDNS1"):
            self.ExtensionDNS1 = params.get("ExtensionDNS1")
        if params.get("ExtensionDNS2"):
            self.ExtensionDNS2 = params.get("ExtensionDNS2")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("AddressBandWidth"):
            self.AddressBandWidth = params.get("AddressBandWidth")
        if params.get("LineId"):
            self.LineId = params.get("LineId")
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")
        if params.get("AddressChargeType"):
            self.AddressChargeType = params.get("AddressChargeType")
        if params.get("AddressPurchaseTime"):
            self.AddressPurchaseTime = params.get("AddressPurchaseTime")
        if params.get("AddressProjectId"):
            self.AddressProjectId = params.get("AddressProjectId")
        if params.get("SystemFileType"):
            self.SystemFileType = params.get("SystemFileType")
        if params.get("DataFileType"):
            self.DataFileType = params.get("DataFileType")
        if params.get("DataDiskCatalogue"):
            self.DataDiskCatalogue = params.get("DataDiskCatalogue")
        if params.get("DataDiskCatalogueSuffix"):
            self.DataDiskCatalogueSuffix = params.get("DataDiskCatalogueSuffix")
        if params.get("HyperThreading"):
            self.HyperThreading = params.get("HyperThreading")
        if params.get("NvmeDataFileType"):
            self.NvmeDataFileType = params.get("NvmeDataFileType")
        if params.get("NvmeDataDiskCatalogue"):
            self.NvmeDataDiskCatalogue = params.get("NvmeDataDiskCatalogue")
        if params.get("NvmeDataDiskCatalogueSuffix"):
            self.NvmeDataDiskCatalogueSuffix = params.get("NvmeDataDiskCatalogueSuffix")
        if params.get("bondAttribute"):
            self.bondAttribute = params.get("bondAttribute")
        if params.get("ContainerAgent"):
            self.ContainerAgent = params.get("ContainerAgent")
        if params.get("KesAgent"):
            self.KesAgent = params.get("KesAgent")
        if params.get("KmrAgent"):
            self.KmrAgent = params.get("KmrAgent")
        if params.get("ComputerName"):
            self.ComputerName = params.get("ComputerName")
        if params.get("OverclockingAttribute"):
            self.OverclockingAttribute = params.get("OverclockingAttribute")
        if params.get("GpuImageDriverId"):
            self.GpuImageDriverId = params.get("GpuImageDriverId")
        if params.get("SystemVolumeType"):
            self.SystemVolumeType = params.get("SystemVolumeType")
        if params.get("SystemVolumeSize"):
            self.SystemVolumeSize = params.get("SystemVolumeSize")
        if params.get("RoceNetwork"):
            self.RoceNetwork = params.get("RoceNetwork")


class StartEpcRequest(AbstractModel):
    """StartEpc请求参数结构体
    """

    def __init__(self):
        r"""StartEpc
        :param HostId: 裸金属服务器资源ID，也可填入EpcHostId
        :type PathPrefix: String
        """
        self.HostId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class RebootEpcRequest(AbstractModel):
    """RebootEpc请求参数结构体
    """

    def __init__(self):
        r"""RebootEpc
        :param HostId: 裸金属服务器资源ID，也可填入EpcHostId
        :type PathPrefix: String
        """
        self.HostId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class DeleteEpcRequest(AbstractModel):
    """DeleteEpc请求参数结构体
    """

    def __init__(self):
        r"""DeleteEpc
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        """
        self.HostId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class ReinstallEpcRequest(AbstractModel):
    """ReinstallEpc请求参数结构体
    """

    def __init__(self):
        r"""ReinstallEpc
        :param HostId: 裸金属服务器资源ID，也可填入EpcHostId
        :type PathPrefix: String
        :param ImageId: 镜像资源ID,参见DescribeImages
        :type PathPrefix: String
        :param keyId: 用户密钥对的资源ID
        :type PathPrefix: String
        :param Password: 系统的登录密码
        :type PathPrefix: String
        :param NetworkInterfaceMode: 是否支持Bond，是：“Yes”；不是:”No”
        :type PathPrefix: String
        :param SecurityAgent: 安全组件类型
- classic：经典版
- no：不开启
        :type PathPrefix: String
        :param CloudMonitorAgent: 安全组件类型
- classic：经典版
- no：不开启
        :type PathPrefix: String
        :param Raid: 数据盘Raid级别,和数据盘的数量直接相关 
有效值：  Raid1：数据盘数量必须是2的倍数
Raid5：数据盘的数量必须大于等于3
Raid10：数据盘数量必须是4的倍数
Raid50：数据盘的数量必须大于6且是2的倍数
SRaid0：单盘SRaid0无限制，仅针对大数据业务自身有冗余的场景
与RaidId必填其一，RaidId优先级高
        :type PathPrefix: String
        :param RaidId: Raid模板Id
        :type PathPrefix: String
        :param HostName: 云物理主机名称
        :type PathPrefix: String
        :param SystemFileType: 系统盘文件格式
        :type PathPrefix: String
        :param DataFileType: 数据盘文件格式
        :type PathPrefix: String
        :param DataDiskCatalogue: 数据盘目录
        :type PathPrefix: String
        :param DataDiskCatalogueSuffix: 数据盘目录后缀属性
        :type PathPrefix: String
        :param HyperThreading: 对超线程的变更
        :type PathPrefix: String
        :param NvmeDataFileType: NVME数据盘类型
        :type PathPrefix: String
        :param NvmeDataDiskCatalogue: NVME数据盘目录
        :type PathPrefix: String
        :param NvmeDataDiskCatalogueSuffix: NVME数据盘目录后缀属性
        :type PathPrefix: String
        :param bondAttribute: 网卡bond的属性
        :type PathPrefix: String
        :param KesAgent: kes组件类型
        :type PathPrefix: String
        :param KmrAgent: KMR组件类型
        :type PathPrefix: String
        :param ComputerName: 计算机系统内名称
        :type PathPrefix: String
        :param OverclockingAttribute: 超频
        :type PathPrefix: String
        :param DelayStart: 是否延迟开始，0:不延迟开始PxeOn;1:延迟开始PxeOn
        :type PathPrefix: Int
        :param AvailabilityZone: 可用区的名称
        :type PathPrefix: String
        :param GpuImageDriverId: gpu版本
        :type PathPrefix: String
        :param containerAgent: 容器引擎组件类型
        :type PathPrefix: String
        """
        self.HostId = None
        self.ImageId = None
        self.keyId = None
        self.Password = None
        self.NetworkInterfaceMode = None
        self.SecurityAgent = None
        self.CloudMonitorAgent = None
        self.Raid = None
        self.RaidId = None
        self.HostName = None
        self.SystemFileType = None
        self.DataFileType = None
        self.DataDiskCatalogue = None
        self.DataDiskCatalogueSuffix = None
        self.HyperThreading = None
        self.NvmeDataFileType = None
        self.NvmeDataDiskCatalogue = None
        self.NvmeDataDiskCatalogueSuffix = None
        self.bondAttribute = None
        self.KesAgent = None
        self.KmrAgent = None
        self.ComputerName = None
        self.OverclockingAttribute = None
        self.DelayStart = None
        self.AvailabilityZone = None
        self.GpuImageDriverId = None
        self.containerAgent = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("keyId"):
            self.keyId = params.get("keyId")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("NetworkInterfaceMode"):
            self.NetworkInterfaceMode = params.get("NetworkInterfaceMode")
        if params.get("SecurityAgent"):
            self.SecurityAgent = params.get("SecurityAgent")
        if params.get("CloudMonitorAgent"):
            self.CloudMonitorAgent = params.get("CloudMonitorAgent")
        if params.get("Raid"):
            self.Raid = params.get("Raid")
        if params.get("RaidId"):
            self.RaidId = params.get("RaidId")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("SystemFileType"):
            self.SystemFileType = params.get("SystemFileType")
        if params.get("DataFileType"):
            self.DataFileType = params.get("DataFileType")
        if params.get("DataDiskCatalogue"):
            self.DataDiskCatalogue = params.get("DataDiskCatalogue")
        if params.get("DataDiskCatalogueSuffix"):
            self.DataDiskCatalogueSuffix = params.get("DataDiskCatalogueSuffix")
        if params.get("HyperThreading"):
            self.HyperThreading = params.get("HyperThreading")
        if params.get("NvmeDataFileType"):
            self.NvmeDataFileType = params.get("NvmeDataFileType")
        if params.get("NvmeDataDiskCatalogue"):
            self.NvmeDataDiskCatalogue = params.get("NvmeDataDiskCatalogue")
        if params.get("NvmeDataDiskCatalogueSuffix"):
            self.NvmeDataDiskCatalogueSuffix = params.get("NvmeDataDiskCatalogueSuffix")
        if params.get("bondAttribute"):
            self.bondAttribute = params.get("bondAttribute")
        if params.get("KesAgent"):
            self.KesAgent = params.get("KesAgent")
        if params.get("KmrAgent"):
            self.KmrAgent = params.get("KmrAgent")
        if params.get("ComputerName"):
            self.ComputerName = params.get("ComputerName")
        if params.get("OverclockingAttribute"):
            self.OverclockingAttribute = params.get("OverclockingAttribute")
        if params.get("DelayStart"):
            self.DelayStart = params.get("DelayStart")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("GpuImageDriverId"):
            self.GpuImageDriverId = params.get("GpuImageDriverId")
        if params.get("containerAgent"):
            self.containerAgent = params.get("containerAgent")


class ModifySecurityGroupRequest(AbstractModel):
    """ModifySecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""ModifySecurityGroup
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param NetworkInterfaceId: 网卡的ID
        :type PathPrefix: String
        :param SecurityGroupId: 裸金属服务器关联的安全组ID，一个裸金属服务器最多可以支持3个安全组
        :type PathPrefix: Filter
        """
        self.HostId = None
        self.NetworkInterfaceId = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class CreateKeyRequest(AbstractModel):
    """CreateKey请求参数结构体
    """

    def __init__(self):
        r"""CreateKey
        :param KeyName: 密钥名称
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        """
        self.KeyName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("KeyName"):
            self.KeyName = params.get("KeyName")
        if params.get("Description"):
            self.Description = params.get("Description")


class DescribeEpcsRequest(AbstractModel):
    """DescribeEpcs请求参数结构体
    """

    def __init__(self):
        r"""DescribeEpcs
        :param ProjectId: 服务器所属项目的ID
        :type PathPrefix: Filter
        :param HostId: 裸金属服务器资源ID，可查询多个ID的实例信息
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.HostId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class GetDynamicCodeRequest(AbstractModel):
    """GetDynamicCode请求参数结构体
    """

    def __init__(self):
        r"""GetDynamicCode
        :param RemoteManagementId: 带外管理的ID
        :type PathPrefix: String
        """
        self.RemoteManagementId = None

    def _deserialize(self, params):
        if params.get("RemoteManagementId"):
            self.RemoteManagementId = params.get("RemoteManagementId")


class DescribeVpnsRequest(AbstractModel):
    """DescribeVpns请求参数结构体
    """

    def __init__(self):
        r"""DescribeVpns
        :param DynamicCode: 手机动态码
        :type PathPrefix: String
        :param Pin: 个人识别码
        :type PathPrefix: String
        :param RemoteManagementId: 带外管理的ID
        :type PathPrefix: String
        """
        self.DynamicCode = None
        self.Pin = None
        self.RemoteManagementId = None

    def _deserialize(self, params):
        if params.get("DynamicCode"):
            self.DynamicCode = params.get("DynamicCode")
        if params.get("Pin"):
            self.Pin = params.get("Pin")
        if params.get("RemoteManagementId"):
            self.RemoteManagementId = params.get("RemoteManagementId")


class CreateImageRequest(AbstractModel):
    """CreateImage请求参数结构体
    """

    def __init__(self):
        r"""CreateImage
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param ImageName: 镜像名称
        :type PathPrefix: String
        :param ImageMode: 镜像类型：SystemDisk|AllDisk
        :type PathPrefix: String
        :param ImageInitialization: 裸金属服务器自定义镜像初始化选项:Initialization|Uninitialized
        :type PathPrefix: String
        """
        self.HostId = None
        self.ImageName = None
        self.ImageMode = None
        self.ImageInitialization = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("ImageName"):
            self.ImageName = params.get("ImageName")
        if params.get("ImageMode"):
            self.ImageMode = params.get("ImageMode")
        if params.get("ImageInitialization"):
            self.ImageInitialization = params.get("ImageInitialization")


class ModifyImageRequest(AbstractModel):
    """ModifyImage请求参数结构体
    """

    def __init__(self):
        r"""ModifyImage
        :param ImageName: 镜像名称
        :type PathPrefix: String
        :param ImageId: 原镜像ID
        :type PathPrefix: String
        """
        self.ImageName = None
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageName"):
            self.ImageName = params.get("ImageName")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage请求参数结构体
    """

    def __init__(self):
        r"""DeleteImage
        :param ImageId: 原镜像ID
        :type PathPrefix: String
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体
    """

    def __init__(self):
        r"""DescribeImages
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ModifyDnsRequest(AbstractModel):
    """ModifyDns请求参数结构体
    """

    def __init__(self):
        r"""ModifyDns
        :param NetworkInterfaceId: 网卡的ID
        :type PathPrefix: String
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param DNS1: DNS1的值
        :type PathPrefix: String
        :param DNS2: DNS2的值
        :type PathPrefix: String
        """
        self.NetworkInterfaceId = None
        self.HostId = None
        self.DNS1 = None
        self.DNS2 = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("DNS1"):
            self.DNS1 = params.get("DNS1")
        if params.get("DNS2"):
            self.DNS2 = params.get("DNS2")


class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
    """ModifyNetworkInterfaceAttribute请求参数结构体
    """

    def __init__(self):
        r"""ModifyNetworkInterfaceAttribute
        :param NetworkInterfaceId: 网卡ID
        :type PathPrefix: String
        :param HostId: 物理机实例ID
        :type PathPrefix: String
        :param SubnetId: SubnetId
        :type PathPrefix: String
        :param IpAddress: ip地址
        :type PathPrefix: String
        :param SecurityGroupIdList: 云物理主机关联的安全组ID，一个云物理主机最多可以支持3个安全组
        :type PathPrefix: Array
        """
        self.NetworkInterfaceId = None
        self.HostId = None
        self.SubnetId = None
        self.IpAddress = None
        self.SecurityGroupIdList = None

    def _deserialize(self, params):
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("IpAddress"):
            self.IpAddress = params.get("IpAddress")
        if params.get("SecurityGroupIdList"):
            self.SecurityGroupIdList = params.get("SecurityGroupIdList")


class DescribePhysicalMonitorRequest(AbstractModel):
    """DescribePhysicalMonitor请求参数结构体
    """

    def __init__(self):
        r"""DescribePhysicalMonitor
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        """
        self.HostId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class DescribeEpcManagementsRequest(AbstractModel):
    """DescribeEpcManagements请求参数结构体
    """

    def __init__(self):
        r"""DescribeEpcManagements
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        :param DynamicCode: 手机动态码
        :type PathPrefix: String
        :param Pin: 个人识别码
        :type PathPrefix: String
        :param EpcManagementId: 远程管理的ID
        :type PathPrefix: Filter
        :param RemoteManagementId: 带外管理的ID
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.NextToken = None
        self.DynamicCode = None
        self.Pin = None
        self.EpcManagementId = None
        self.RemoteManagementId = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("DynamicCode"):
            self.DynamicCode = params.get("DynamicCode")
        if params.get("Pin"):
            self.Pin = params.get("Pin")
        if params.get("EpcManagementId"):
            self.EpcManagementId = params.get("EpcManagementId")
        if params.get("RemoteManagementId"):
            self.RemoteManagementId = params.get("RemoteManagementId")


class DescribeRemoteManagementsRequest(AbstractModel):
    """DescribeRemoteManagements请求参数结构体
    """

    def __init__(self):
        r"""DescribeRemoteManagements
        :param RemoteManagementId: 远程管理的ID
        :type PathPrefix: Filter
        """
        self.RemoteManagementId = None

    def _deserialize(self, params):
        if params.get("RemoteManagementId"):
            self.RemoteManagementId = params.get("RemoteManagementId")


class StopEpcRequest(AbstractModel):
    """StopEpc请求参数结构体
    """

    def __init__(self):
        r"""StopEpc
        :param HostId: 裸金属服务器资源ID，也可填入EpcHostId
        :type PathPrefix: String
        """
        self.HostId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class ModifyEpcRequest(AbstractModel):
    """ModifyEpc请求参数结构体
    """

    def __init__(self):
        r"""ModifyEpc
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param HostName: 云物理主机名称
        :type PathPrefix: String
        :param Description: 描述信息
        :type PathPrefix: String
        """
        self.HostId = None
        self.HostName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("Description"):
            self.Description = params.get("Description")


class ModifyRemoteManagementRequest(AbstractModel):
    """ModifyRemoteManagement请求参数结构体
    """

    def __init__(self):
        r"""ModifyRemoteManagement
        :param RemoteManagementId: 带外管理的ID
        :type PathPrefix: String
        :param DynamicCode: 手机动态码
        :type PathPrefix: String
        :param Pin: 个人识别码
        :type PathPrefix: String
        :param NewPhoneNumber: 新手机号码
        :type PathPrefix: String
        :param NewPin: 个人识别码
        :type PathPrefix: String
        :param Name: 姓名
        :type PathPrefix: String
        :param VersionId: 版本ID
        :type PathPrefix: Int
        """
        self.RemoteManagementId = None
        self.DynamicCode = None
        self.Pin = None
        self.NewPhoneNumber = None
        self.NewPin = None
        self.Name = None
        self.VersionId = None

    def _deserialize(self, params):
        if params.get("RemoteManagementId"):
            self.RemoteManagementId = params.get("RemoteManagementId")
        if params.get("DynamicCode"):
            self.DynamicCode = params.get("DynamicCode")
        if params.get("Pin"):
            self.Pin = params.get("Pin")
        if params.get("NewPhoneNumber"):
            self.NewPhoneNumber = params.get("NewPhoneNumber")
        if params.get("NewPin"):
            self.NewPin = params.get("NewPin")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("VersionId"):
            self.VersionId = params.get("VersionId")


class CreateRemoteManagementRequest(AbstractModel):
    """CreateRemoteManagement请求参数结构体
    """

    def __init__(self):
        r"""CreateRemoteManagement
        :param DynamicCode: 手机动态码
        :type PathPrefix: String
        :param Pin: 个人识别码
        :type PathPrefix: String
        :param PhoneNumber: 手机号码
        :type PathPrefix: String
        :param Name: 姓名
        :type PathPrefix: String
        :param VersionId: 版本ID
        :type PathPrefix: Int
        """
        self.DynamicCode = None
        self.Pin = None
        self.PhoneNumber = None
        self.Name = None
        self.VersionId = None

    def _deserialize(self, params):
        if params.get("DynamicCode"):
            self.DynamicCode = params.get("DynamicCode")
        if params.get("Pin"):
            self.Pin = params.get("Pin")
        if params.get("PhoneNumber"):
            self.PhoneNumber = params.get("PhoneNumber")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("VersionId"):
            self.VersionId = params.get("VersionId")


class ReinstallCustomerEpcRequest(AbstractModel):
    """ReinstallCustomerEpc请求参数结构体
    """

    def __init__(self):
        r"""ReinstallCustomerEpc
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param ServerIp: PXE server的IP
        :type PathPrefix: String
        :param Path: PXE server的路径
        :type PathPrefix: String
        """
        self.HostId = None
        self.ServerIp = None
        self.Path = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("ServerIp"):
            self.ServerIp = params.get("ServerIp")
        if params.get("Path"):
            self.Path = params.get("Path")


class DeleteRemoteManagementRequest(AbstractModel):
    """DeleteRemoteManagement请求参数结构体
    """

    def __init__(self):
        r"""DeleteRemoteManagement
        :param RemoteManagementId: 带外管理的ID
        :type PathPrefix: String
        """
        self.RemoteManagementId = None

    def _deserialize(self, params):
        if params.get("RemoteManagementId"):
            self.RemoteManagementId = params.get("RemoteManagementId")


class ResetPasswordRequest(AbstractModel):
    """ResetPassword请求参数结构体
    """

    def __init__(self):
        r"""重置密码
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param Password: 云物理主机的root密码
        :type PathPrefix: String
        """
        self.HostId = None
        self.Password = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("Password"):
            self.Password = params.get("Password")


class ModifyHyperThreadingRequest(AbstractModel):
    """ModifyHyperThreading请求参数结构体
    """

    def __init__(self):
        r"""修改超线程
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param HyperThreadingStatus: 超线程状态，start|stop
        :type PathPrefix: String
        """
        self.HostId = None
        self.HyperThreadingStatus = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("HyperThreadingStatus"):
            self.HyperThreadingStatus = params.get("HyperThreadingStatus")


class AssociateClusterRequest(AbstractModel):
    """AssociateCluster请求参数结构体
    """

    def __init__(self):
        r"""AssociateCluster
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param ClusterId: 容器ID
        :type PathPrefix: String
        """
        self.HostId = None
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class DisassociateClusterRequest(AbstractModel):
    """DisassociateCluster请求参数结构体
    """

    def __init__(self):
        r"""DisassociateCluster
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        """
        self.HostId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class DescribeInspectionsRequest(AbstractModel):
    """DescribeInspections请求参数结构体
    """

    def __init__(self):
        r"""DescribeInspections
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        """
        self.MaxResults = None
        self.NextToken = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class DescribeEpcStocksRequest(AbstractModel):
    """DescribeEpcStocks请求参数结构体
    """

    def __init__(self):
        r"""DescribeEpcStocks
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        """
        self.Filter = None

    def _deserialize(self, params):
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class DescribeEpcDeviceAttributesRequest(AbstractModel):
    """DescribeEpcDeviceAttributes请求参数结构体
    """

    def __init__(self):
        r"""DescribeEpcDeviceAttributes
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param DeviceAttributeId: 设备的ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.Filter = None
        self.DeviceAttributeId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("DeviceAttributeId"):
            self.DeviceAttributeId = params.get("DeviceAttributeId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeProcessesRequest(AbstractModel):
    """DescribeProcesses请求参数结构体
    """

    def __init__(self):
        r"""DescribeProcesses
        :param OperationProcessId: 流程的ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.OperationProcessId = None
        self.Filter = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("OperationProcessId"):
            self.OperationProcessId = params.get("OperationProcessId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class CreateProcessRequest(AbstractModel):
    """CreateProcess请求参数结构体
    """

    def __init__(self):
        r"""CreateProcess
        :param ProcessId: 云物理工单ID
        :type PathPrefix: String
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param Sn: 云物理主机序列号
        :type PathPrefix: String
        :param AvailabilityZone: 可用区
        :type PathPrefix: String
        :param CreateTime: 创建时间
        :type PathPrefix: String
        :param Attribute: 问题属性
        :type PathPrefix: String
        :param Content: 描述
        :type PathPrefix: String
        :param MachineCount: 服务器数量，通常填写1
        :type PathPrefix: Int
        :param Title: 标题
        :type PathPrefix: String
        :param Type: 操作类型,有效值:fix
        :type PathPrefix: String
        :param Confirm: 确认是否操作 有效值：0,1
        :type PathPrefix: String
        :param ProcessSource: 工单来源，0:客户 1：售后代提
        :type PathPrefix: Int
        """
        self.ProcessId = None
        self.InstanceId = None
        self.Sn = None
        self.AvailabilityZone = None
        self.CreateTime = None
        self.Attribute = None
        self.Content = None
        self.MachineCount = None
        self.Title = None
        self.Type = None
        self.Confirm = None
        self.ProcessSource = None

    def _deserialize(self, params):
        if params.get("ProcessId"):
            self.ProcessId = params.get("ProcessId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Sn"):
            self.Sn = params.get("Sn")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("CreateTime"):
            self.CreateTime = params.get("CreateTime")
        if params.get("Attribute"):
            self.Attribute = params.get("Attribute")
        if params.get("Content"):
            self.Content = params.get("Content")
        if params.get("MachineCount"):
            self.MachineCount = params.get("MachineCount")
        if params.get("Title"):
            self.Title = params.get("Title")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("Confirm"):
            self.Confirm = params.get("Confirm")
        if params.get("ProcessSource"):
            self.ProcessSource = params.get("ProcessSource")


class DeleteProcessRequest(AbstractModel):
    """DeleteProcess请求参数结构体
    """

    def __init__(self):
        r"""DeleteProcess
        :param OperationProcessId: 流程的ID
        :type PathPrefix: String
        """
        self.OperationProcessId = None

    def _deserialize(self, params):
        if params.get("OperationProcessId"):
            self.OperationProcessId = params.get("OperationProcessId")


class ReplyProcessRequest(AbstractModel):
    """ReplyProcess请求参数结构体
    """

    def __init__(self):
        r"""ReplyProcess
        :param OperationProcessId: 流程的ID
        :type PathPrefix: String
        :param Remarks: 回复内容
        :type PathPrefix: String
        """
        self.OperationProcessId = None
        self.Remarks = None

    def _deserialize(self, params):
        if params.get("OperationProcessId"):
            self.OperationProcessId = params.get("OperationProcessId")
        if params.get("Remarks"):
            self.Remarks = params.get("Remarks")


class DescribeEpcTrashesRequest(AbstractModel):
    """DescribeEpcTrashes请求参数结构体
    """

    def __init__(self):
        r"""DescribeEpcTrashes
        :param MaxResults: 单次调用可返回的最大条目数量. 传入返回的 NextToken 值可以获取剩余的其它条目. 这个值可以允许的范围是 5- 1000
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class ReturnEpcRequest(AbstractModel):
    """ReturnEpc请求参数结构体
    """

    def __init__(self):
        r"""ReturnEpc
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        """
        self.HostId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class CreateResourceRequirementRequest(AbstractModel):
    """CreateResourceRequirement请求参数结构体
    """

    def __init__(self):
        r"""创建资源需求工单
        :param AvailabilityZone: 可用区
        :type PathPrefix: String
        :param RequirementCount: 服务器需求数量
        :type PathPrefix: Int
        :param ProjectName: 项目名称
        :type PathPrefix: String
        :param UsageDate: 使用时间，yyyyMMdd
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        :param HostType: 物理机类型
        :type PathPrefix: String
        """
        self.AvailabilityZone = None
        self.RequirementCount = None
        self.ProjectName = None
        self.UsageDate = None
        self.Description = None
        self.HostType = None

    def _deserialize(self, params):
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("RequirementCount"):
            self.RequirementCount = params.get("RequirementCount")
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("UsageDate"):
            self.UsageDate = params.get("UsageDate")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("HostType"):
            self.HostType = params.get("HostType")


class AttachVolumeRequest(AbstractModel):
    """AttachVolume请求参数结构体
    """

    def __init__(self):
        r"""EPC挂载EBS
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param VolumeId: EBS的ID
        :type PathPrefix: String
        """
        self.HostId = None
        self.VolumeId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")


class DetachVolumeRequest(AbstractModel):
    """DetachVolume请求参数结构体
    """

    def __init__(self):
        r"""EPC卸载EBS
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param VolumeId: EBS的ID
        :type PathPrefix: String
        """
        self.HostId = None
        self.VolumeId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")


class DescribePriceRequest(AbstractModel):
    """DescribePrice请求参数结构体
    """

    def __init__(self):
        r"""查询价格信息
        :param ChargeType: 主机计费类型，包年包月Monthly，按日月结Daily
-有效值：Monthly|Daily|PostPaidByDay|PrePaidByMonth
        :type PathPrefix: String
        :param HostType: 物理机类型
        :type PathPrefix: String
        :param AvailabilityZone: 可用区的名称
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月时不可缺省。
        :type PathPrefix: Int
        :param Amount: 购买的数量
        :type PathPrefix: Int
        """
        self.ChargeType = None
        self.HostType = None
        self.AvailabilityZone = None
        self.PurchaseTime = None
        self.Amount = None

    def _deserialize(self, params):
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("HostType"):
            self.HostType = params.get("HostType")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("Amount"):
            self.Amount = params.get("Amount")


class ModifyOverclockingAttributeRequest(AbstractModel):
    """ModifyOverclockingAttribute请求参数结构体
    """

    def __init__(self):
        r"""修改超频
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param OverclockingAttribute: 超频属性，Open|Close
        :type PathPrefix: String
        """
        self.HostId = None
        self.OverclockingAttribute = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("OverclockingAttribute"):
            self.OverclockingAttribute = params.get("OverclockingAttribute")


class CopyImageRequest(AbstractModel):
    """CopyImage请求参数结构体
    """

    def __init__(self):
        r"""复制镜像
        :param DestinationName: 镜像名称
        :type PathPrefix: String
        :param ImageId: 自定义镜像ID
        :type PathPrefix: String
        :param DestinationRegion: 目标机房
        :type PathPrefix: String
        :param CopyTag: 是否复制Tag,yes|no
        :type PathPrefix: String
        """
        self.DestinationName = None
        self.ImageId = None
        self.DestinationRegion = None
        self.CopyTag = None

    def _deserialize(self, params):
        if params.get("DestinationName"):
            self.DestinationName = params.get("DestinationName")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("DestinationRegion"):
            self.DestinationRegion = params.get("DestinationRegion")
        if params.get("CopyTag"):
            self.CopyTag = params.get("CopyTag")


class DescribeEpcRaidAttributesRequest(AbstractModel):
    """DescribeEpcRaidAttributes请求参数结构体
    """

    def __init__(self):
        r"""查询多raid信息
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


class DescribeGpuImageDriverRequest(AbstractModel):
    """DescribeGpuImageDriver请求参数结构体
    """

    def __init__(self):
        r"""查询GPU镜像驱动
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        :param ImageId: 镜像ID
        :type PathPrefix: String
        :param HostType: 云物理主机类型
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.NextToken = None
        self.ImageId = None
        self.HostType = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("HostType"):
            self.HostType = params.get("HostType")


class CreateShareImageRequest(AbstractModel):
    """CreateShareImage请求参数结构体
    """

    def __init__(self):
        r"""星曜共享镜像
        :param ImageId: 需要共享的镜像ID
        :type PathPrefix: String
        :param AccountId.N: 接收共享镜像的账号ID列表
        :type PathPrefix: String
        """
        self.ImageId = None
        self.AccountId.N = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("AccountId.N"):
            self.AccountId.N = params.get("AccountId.N")


class DeleteShareImageRequest(AbstractModel):
    """DeleteShareImage请求参数结构体
    """

    def __init__(self):
        r"""星曜取消共享镜像
        :param ImageId: 需要取消共享的镜像ID
        :type PathPrefix: String
        :param AccountId.N: 接收共享镜像的账号ID列表
        :type PathPrefix: String
        """
        self.ImageId = None
        self.AccountId.N = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("AccountId.N"):
            self.AccountId.N = params.get("AccountId.N")


class DescribeShareImageAccountListRequest(AbstractModel):
    """DescribeShareImageAccountList请求参数结构体
    """

    def __init__(self):
        r"""星曜获取已共享镜像的账户列表信息
        :param ImageId: 共享的镜像ID
        :type PathPrefix: String
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class DescribeShareImageRequest(AbstractModel):
    """DescribeShareImage请求参数结构体
    """

    def __init__(self):
        r"""星曜获取共享镜像列表信息
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的token.
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class AcceptShareImageRequest(AbstractModel):
    """AcceptShareImage请求参数结构体
    """

    def __init__(self):
        r"""星曜接收共享镜像
        :param ImageId: 
        :type PathPrefix: String
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class RejectShareImageRequest(AbstractModel):
    """RejectShareImage请求参数结构体
    """

    def __init__(self):
        r"""星曜拒绝共享镜像
        :param ImageId: 
        :type PathPrefix: String
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class AutoDeleteEpcRequest(AbstractModel):
    """AutoDeleteEpc请求参数结构体
    """

    def __init__(self):
        r"""AutoDeleteEpc
        :param HostId: 实例ID
        :type PathPrefix: String
        :param AutoDeleteTime: 预约删除时间
        :type PathPrefix: String
        :param AutoDeleteEip: 是否删除EIP信息
yes/no 默认no
        :type PathPrefix: String
        """
        self.HostId = None
        self.AutoDeleteTime = None
        self.AutoDeleteEip = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("AutoDeleteTime"):
            self.AutoDeleteTime = params.get("AutoDeleteTime")
        if params.get("AutoDeleteEip"):
            self.AutoDeleteEip = params.get("AutoDeleteEip")


