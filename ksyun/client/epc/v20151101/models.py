from ksyun.common.abstract_model import AbstractModel

class CreateEpcRequest(AbstractModel):
    """CreateEpc请求参数结构体
    """

    def __init__(self):
        r"""创建云物理主机
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
有效值：
- Jbod：直连模式
- Raid1：数据盘数量必须是2的倍数
- Raid5：数据盘的数量必须大于等于3
- Raid10：数据盘数量必须是4的倍数
- Raid50：数据盘的数量必须大于6且是2的倍数
- SRaid0：单盘SRaid0无限制，仅针对大数据业务自身有冗余的场景
说明：Raid与RaidId必填其一，RaidId优先级高
        :type PathPrefix: String
        :param RaidId: Raid模板Id
        :type PathPrefix: String
        :param ImageId: 镜像资源ID,参见DescribeImages
        :type PathPrefix: String
        :param NetworkInterfaceMode: 网卡模式
有效值：
bond4：bond模式
single：非bond模式
dual：双网卡模式
windows创建时，只支持非bond模式。
        :type PathPrefix: String
        :param SubnetId: 云物理主机的子网ID
        :type PathPrefix: String
        :param PrivateIpAddress: 内网资源IP地址
        :type PathPrefix: String
        :param keyId: 用户密钥对的资源ID
        :type PathPrefix: String
        :param SecurityGroupId: 裸金属服务器关联的安全组ID，一个裸金属服务器最多可以支持5个安全组
        :type PathPrefix: Filter
        :param DNS1: DNS1的值，当通过该接口进行修改网络配置时不填写此参数，保持与之前不变
        :type PathPrefix: String
        :param DNS2: DNS2的值，当通过该接口进行修改网络配置时不填写此参数，保持与之前不变
        :type PathPrefix: String
        :param HostName: 云物理主机名称
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 云物理主机计费类型，包年包月Monthly，按日月结Daily，试用Trial
-有效值：Monthly | Daily | Trial
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月时不可缺省。
        :type PathPrefix: Int
        :param Password: 系统的登录密码
        :type PathPrefix: String
        :param CloudMonitorAgent: 云监控
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
        :param SystemFileType: 系统盘文件格式(NTFS仅支持windows)
有效值：EXT4|XFS|NTFS
        :type PathPrefix: String
        :param DataFileType: 数据盘文件格式(NTFS仅支持windows)
有效值：EXT4|XFS|NTFS

        :type PathPrefix: String
        :param DataDiskCatalogue: 数据盘目录
有效值：

    /DATA/disk：在系统的DATA目录下，系统里展示内容如/DATA/disk1，/DATA/disk2
    /data：在系统的根目录下，系统里展示内容从/data1开始，如/data1，/data2

        :type PathPrefix: String
        :param DataDiskCatalogueSuffix: 数据盘目录后缀属性
有效值：

    NoSuffix ：不使用后缀，只有在数据盘有一块的时候，可以使用此参数
    NaturalNumber：后缀从1底层的整数
    NaturalNumberFromZero：后缀从0递增的整数

        :type PathPrefix: String
        :param HyperThreading: 对超线程的变更
有效值：

    Open：开启
    Close：关闭
    NoChange：不改变

        :type PathPrefix: String
        :param NvmeDataFileType: NVME数据盘类型
有效值：

    EXT4
    XFS

        :type PathPrefix: String
        :param NvmeDataDiskCatalogue: NVME数据盘目录
        :type PathPrefix: String
        :param NvmeDataDiskCatalogueSuffix: NVME数据盘目录后缀属性
        :type PathPrefix: String
        :param BondAttribute: bond名称
有效值： bond0|bond1
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
添加白名单的用户为必填项



        :type PathPrefix: String
        :param ZoneId: 创建pdns所需参数
        :type PathPrefix: String
        :param ZoneType: 创建pdns所需参数
        :type PathPrefix: String
        :param UseHotStandby: 是否开启热备机，有效值
support开启
unsupport不开启
onlyHotStandby只开热备机
        :type PathPrefix: String
        :param TimedRegularization: 释义：试用定时转正
有效值： 
    ▪ support：开启
    ▪ unsupport：关闭
默认值：unsupport，不传默认关闭
        :type PathPrefix: String
        :param PasswordInherit: 是否使用镜像预设的密码和密钥
有效值：
▪ support：开启
▪ unsupport：关闭
默认值：unsupport
        :type PathPrefix: String
        :param DataDiskMount: 是否对数据盘进行磁盘挂载
有效值：
▪ support：开启
▪ unsupport：关闭
默认值：support
        :type PathPrefix: String
        :param StorageRoceNetworkCardName: 存储网卡名称，有效值
eth8x_bond
storage_bond
        :type PathPrefix: String
        :param Anaconda.N: 裸金属服务器anaconda信息
类型： String
是否必填：否
        :type PathPrefix: String
        :param Framework.N: 裸金属服务器训练框架信息
类型： String
是否必填：否
        :type PathPrefix: String
        :param Engine.N: 裸金属服务器推理引擎信息
类型： String
是否必填：否
        :type PathPrefix: String
        :param AiModel.N: 裸金属服务器AI模型信息
类型： String
是否必填：否
        :type PathPrefix: String
        :param UserData: base64编码后的自定义脚本
        :type PathPrefix: String
        :param StorageRoceNetworkInterfaceMode: 存储网卡bond模式，仅支持bond3(bond)、single(非bond)
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
        self.PurchaseTime = None
        self.Password = None
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
        self.BondAttribute = None
        self.ContainerAgent = None
        self.KesAgent = None
        self.KmrAgent = None
        self.ComputerName = None
        self.OverclockingAttribute = None
        self.GpuImageDriverId = None
        self.SystemVolumeType = None
        self.SystemVolumeSize = None
        self.RoceNetwork = None
        self.ZoneId = None
        self.ZoneType = None
        self.UseHotStandby = None
        self.TimedRegularization = None
        self.PasswordInherit = None
        self.DataDiskMount = None
        self.StorageRoceNetworkCardName = None
        self.Anaconda.N = None
        self.Framework.N = None
        self.Engine.N = None
        self.AiModel.N = None
        self.UserData = None
        self.StorageRoceNetworkInterfaceMode = None

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
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("Password"):
            self.Password = params.get("Password")
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
        if params.get("BondAttribute"):
            self.BondAttribute = params.get("BondAttribute")
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
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("ZoneType"):
            self.ZoneType = params.get("ZoneType")
        if params.get("UseHotStandby"):
            self.UseHotStandby = params.get("UseHotStandby")
        if params.get("TimedRegularization"):
            self.TimedRegularization = params.get("TimedRegularization")
        if params.get("PasswordInherit"):
            self.PasswordInherit = params.get("PasswordInherit")
        if params.get("DataDiskMount"):
            self.DataDiskMount = params.get("DataDiskMount")
        if params.get("StorageRoceNetworkCardName"):
            self.StorageRoceNetworkCardName = params.get("StorageRoceNetworkCardName")
        if params.get("Anaconda.N"):
            self.Anaconda.N = params.get("Anaconda.N")
        if params.get("Framework.N"):
            self.Framework.N = params.get("Framework.N")
        if params.get("Engine.N"):
            self.Engine.N = params.get("Engine.N")
        if params.get("AiModel.N"):
            self.AiModel.N = params.get("AiModel.N")
        if params.get("UserData"):
            self.UserData = params.get("UserData")
        if params.get("StorageRoceNetworkInterfaceMode"):
            self.StorageRoceNetworkInterfaceMode = params.get("StorageRoceNetworkInterfaceMode")


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
        r"""物理机重装系统
        :param HostId: 裸金属服务器资源ID，也可填入EpcHostId
        :type PathPrefix: String
        :param ImageId: 镜像资源ID,参见DescribeImages
        :type PathPrefix: String
        :param keyId: 用户密钥对的资源ID
        :type PathPrefix: String
        :param Password: 系统的登录密码
        :type PathPrefix: String
        :param NetworkInterfaceMode: 网卡模式
有效值：
bond4：BOND模式
single：非BOND模式
dual：双网卡模式
1. centos、Debin、Ubuntu重装时，bond选项 限制：
    a. 若开机为双网卡模式，则只能重装成双网卡模式，无法重装为bond和非bond模式。
    b. bond/非bond重装时仅可选择bond/非bond 
2. 重装为window系统时，无法选择网卡类型，默认重装为非bond模式,且无法选择密钥验证。
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
        :param BondAttribute: 网卡bond的属性
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
        :param ContainerAgent: 容器引擎组件类型
        :type PathPrefix: String
        :param PasswordInherit: 是否使用镜像预设的密码和密钥
有效值：
▪ support：开启
▪ unsupport：关闭
默认值：unsupport
        :type PathPrefix: String
        :param DataDiskMount: 是否对数据盘进行磁盘挂载
有效值：
▪ support：开启
▪ unsupport：关闭
默认值：support
        :type PathPrefix: String
        :param StorageRoceNetworkCardName: RoCE存储卡名称，仅支持
eth8x_bond、storage_bond
        :type PathPrefix: String
        """
        self.HostId = None
        self.ImageId = None
        self.keyId = None
        self.Password = None
        self.NetworkInterfaceMode = None
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
        self.BondAttribute = None
        self.KesAgent = None
        self.KmrAgent = None
        self.ComputerName = None
        self.OverclockingAttribute = None
        self.DelayStart = None
        self.AvailabilityZone = None
        self.GpuImageDriverId = None
        self.ContainerAgent = None
        self.PasswordInherit = None
        self.DataDiskMount = None
        self.StorageRoceNetworkCardName = None

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
        if params.get("BondAttribute"):
            self.BondAttribute = params.get("BondAttribute")
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
        if params.get("ContainerAgent"):
            self.ContainerAgent = params.get("ContainerAgent")
        if params.get("PasswordInherit"):
            self.PasswordInherit = params.get("PasswordInherit")
        if params.get("DataDiskMount"):
            self.DataDiskMount = params.get("DataDiskMount")
        if params.get("StorageRoceNetworkCardName"):
            self.StorageRoceNetworkCardName = params.get("StorageRoceNetworkCardName")


class ModifySecurityGroupRequest(AbstractModel):
    """ModifySecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""修改安全组
        :param HostId: 裸金属服务器资源ID
        :type PathPrefix: String
        :param NetworkInterfaceId: 网卡的ID
        :type PathPrefix: String
        :param SecurityGroupId: 裸金属服务器关联的安全组ID，一个裸金属服务器最多可以支持5个安全组
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
        r"""查看云物理主机列表信息
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
        r"""查询镜像列表
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        :param ImageId.N: 镜像ID
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.NextToken = None
        self.ImageId.N = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("ImageId.N"):
            self.ImageId.N = params.get("ImageId.N")


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
        r"""修改网卡信息
        :param NetworkInterfaceId: 网卡ID
        :type PathPrefix: String
        :param HostId: 物理机实例ID
        :type PathPrefix: String
        :param SubnetId: SubnetId
        :type PathPrefix: String
        :param IpAddress: ip地址
        :type PathPrefix: String
        :param SecurityGroupIdList: 云物理主机关联的安全组ID，一个云物理主机最多可以支持5个安全组
        :type PathPrefix: Array
        :param SecurityGroupId: 安全组,更换vpc必填
        :type PathPrefix: Filter
        """
        self.NetworkInterfaceId = None
        self.HostId = None
        self.SubnetId = None
        self.IpAddress = None
        self.SecurityGroupIdList = None
        self.SecurityGroupId = None

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
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


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
        r"""查询云物理机型配置信息
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
        r"""查询工单信息
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
        r"""创建工单信息
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
        :param autoNocCase: 
        :type PathPrefix: Int
        :param LogFileName: 需要客户提供的文件名，需要带文件格式，需要与LogFile.N共同使用
例如：test.csv、test.log
        :type PathPrefix: Filter
        :param LogFile: 工单日志文件，base64编码，需要与LogFileName.N共同使用
E2LWQxOWU0ZWYwYjk2YSwwN2M4YThiZi0zMThmLTQxNjctYWVhNi1kMTllNGVmMGI5NmEsMjAyMC0wNS0xMiAyMTowNTo1NiwyMDIwLTA1LTEyIDIyOjU1OjQyLCJFUEPN0Lncv827p6Osv827p7j8u7u3/s7xxvfN+L+oo6zW2NDCyrax8E1BQ7Ki1tjG9Lf+zvHG96GjIiwsbnVsbCwsLCwKMjAwMDExNzcwMSwwMDkzNDU3UDIwMDdDMDAwNDIJLGNuLXNoYW5naGFpLTJhLM3QudxFUEO/zbuno6y4/Lu7zfi/qE1BQ7XY1re4/NDCsqLW2Mb0LLK7v8nS1NbYxvQszfi/qCwsLCwsLCw3OTg3YmVmOC0yNzY3LTRiZjktODdlMS01MjJkYjEwZTEyMGQs0tHN6rPJLDI1ZDk5ZDExLWQ0NTgtNDUyYy04ZWU5LTM1Yjk2MDIwNzcyNSwyNWQ5OWQxMS1kNDU4LTQ1MmMtOGVlOS0zNWI5NjAyMDc3MjUsMjAyMC0wNS0xMiAyMTowNTo1NiwyMDIwLTA1LTEyIDIyOjU1OjQyLCJFUEPN0Lncv827p6Osv827p7j8u7u3/s7xxvfN+L+oo6zW2NDCyrax8E1BQ7Ki1tjG9Lf+zvHG96GjIiwsbnVsbCwsLCwK
大小：大小低于10MB
        :type PathPrefix: Filter
        :param LogUrl: 支持上传已授权给金山云的ks3的bucket的URL
        :type PathPrefix: Filter
        :param AuthorizeCableReplace: 是否允许换线0否1是
        :type PathPrefix: Int
        :param EventId: 事件ID
        :type PathPrefix: String
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
        self.autoNocCase = None
        self.LogFileName = None
        self.LogFile = None
        self.LogUrl = None
        self.AuthorizeCableReplace = None
        self.EventId = None

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
        if params.get("autoNocCase"):
            self.autoNocCase = params.get("autoNocCase")
        if params.get("LogFileName"):
            self.LogFileName = params.get("LogFileName")
        if params.get("LogFile"):
            self.LogFile = params.get("LogFile")
        if params.get("LogUrl"):
            self.LogUrl = params.get("LogUrl")
        if params.get("AuthorizeCableReplace"):
            self.AuthorizeCableReplace = params.get("AuthorizeCableReplace")
        if params.get("EventId"):
            self.EventId = params.get("EventId")


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


class UpdateConfirmRequest(AbstractModel):
    """UpdateConfirm请求参数结构体
    """

    def __init__(self):
        r"""更新工单重启状态
        """

    def _deserialize(self, params):
        return


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
        :param AccountId: 接收共享镜像的账号ID列表
        :type PathPrefix: Filter
        """
        self.ImageId = None
        self.AccountId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("AccountId"):
            self.AccountId = params.get("AccountId")


class DeleteShareImageRequest(AbstractModel):
    """DeleteShareImage请求参数结构体
    """

    def __init__(self):
        r"""星曜取消共享镜像
        :param ImageId: 需要取消共享的镜像ID
        :type PathPrefix: String
        :param AccountId: 接收共享镜像的账号ID列表
        :type PathPrefix: Filter
        """
        self.ImageId = None
        self.AccountId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("AccountId"):
            self.AccountId = params.get("AccountId")


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


class DescribeManagedAccessoryRequest(AbstractModel):
    """DescribeManagedAccessory请求参数结构体
    """

    def __init__(self):
        r"""托管备件信息查询
        """

    def _deserialize(self, params):
        return


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


class ExportImageRequest(AbstractModel):
    """ExportImage请求参数结构体
    """

    def __init__(self):
        r"""自定义镜像导出
        :param ImageId: 
        :type PathPrefix: String
        :param Ks3Bucket: 
        :type PathPrefix: String
        :param ObjectName: 
        :type PathPrefix: String
        """
        self.ImageId = None
        self.Ks3Bucket = None
        self.ObjectName = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("Ks3Bucket"):
            self.Ks3Bucket = params.get("Ks3Bucket")
        if params.get("ObjectName"):
            self.ObjectName = params.get("ObjectName")


class QueryBucketsRequest(AbstractModel):
    """QueryBuckets请求参数结构体
    """

    def __init__(self):
        r"""查询ks3对象存储bucket桶列表
        """

    def _deserialize(self, params):
        return


class CancelImageExportRequest(AbstractModel):
    """CancelImageExport请求参数结构体
    """

    def __init__(self):
        r"""取消镜像导出
        :param ImageId: 
        :type PathPrefix: String
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class UseHotStandByEpcRequest(AbstractModel):
    """UseHotStandByEpc请求参数结构体
    """

    def __init__(self):
        r"""热备机替换
        :param HostId: 裸金属服务器的ID
        :type PathPrefix: String
        :param HotStandByHostId: 热备机的ID
        :type PathPrefix: String
        :param RetainInstanceInfo: 保留信息，有效值
RetainPrivateIP保留内网IP
Notretain不保留，默认值
        :type PathPrefix: String
        """
        self.HostId = None
        self.HotStandByHostId = None
        self.RetainInstanceInfo = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")
        if params.get("HotStandByHostId"):
            self.HotStandByHostId = params.get("HotStandByHostId")
        if params.get("RetainInstanceInfo"):
            self.RetainInstanceInfo = params.get("RetainInstanceInfo")


class ActivateHotStandbyEpcRequest(AbstractModel):
    """ActivateHotStandbyEpc请求参数结构体
    """

    def __init__(self):
        r"""激活热备机
        :param HostId: 待激活热备机实例ID
        :type PathPrefix: String
        """
        self.HostId = None

    def _deserialize(self, params):
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class BatchCreateEpcRequest(AbstractModel):
    """BatchCreateEpc请求参数结构体
    """

    def __init__(self):
        r"""批量创建云物理主机
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
有效值：
bond4：BOND模式
single：非BOND模式
dual：双网卡模式
windows创建时，只支持非bond模式。
        :type PathPrefix: String
        :param SubnetId: 云物理主机的子网ID
        :type PathPrefix: String
        :param keyId: 用户密钥对的资源ID
        :type PathPrefix: String
        :param SecurityGroupId: 裸金属服务器关联的安全组ID，一个裸金属服务器最多可以支持5个安全组
        :type PathPrefix: Filter
        :param DNS1: DNS1的值，当通过该接口进行修改网络配置时不填写此参数，保持与之前不变
        :type PathPrefix: String
        :param DNS2: DNS2的值，当通过该接口进行修改网络配置时不填写此参数，保持与之前不变
        :type PathPrefix: String
        :param HostName: 云物理主机名称
        :type PathPrefix: String
        :param ProjectId: 项目的ID
        :type PathPrefix: String
        :param ChargeType: 云物理主机计费类型，包年包月Monthly，按日月结Daily，试用Trial
-有效值：Monthly | Daily| Trial
        :type PathPrefix: String
        :param Sn: 云物理主机序列号
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，计费类型为包年包月时不可缺省。
        :type PathPrefix: Int
        :param Password: 系统的登录密码
        :type PathPrefix: String
        :param CloudMonitorAgent: 监控组件类型
- classic：经典版
- no：不开启
        :type PathPrefix: String
        :param ExtensionSubnetId: 从网卡的子网ID
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
        :param SystemFileType: 系统盘文件格式(NTFS仅支持windows)
有效值：EXT4|XFS|NTFS
        :type PathPrefix: String
        :param DataFileType: 数据盘文件格式(NTFS仅支持windows)
有效值：EXT4|XFS|NTFS

        :type PathPrefix: String
        :param DataDiskCatalogue: 数据盘目录
有效值：

    /DATA/disk：在系统的DATA目录下，系统里展示内容如/DATA/disk1，/DATA/disk2
    /data：在系统的根目录下，系统里展示内容从/data1开始，如/data1，/data2

        :type PathPrefix: String
        :param DataDiskCatalogueSuffix: 数据盘目录后缀属性
有效值：

    NoSuffix ：不使用后缀，只有在数据盘有一块的时候，可以使用此参数
    NaturalNumber：后缀从1底层的整数
    NaturalNumberFromZero：后缀从0递增的整数

        :type PathPrefix: String
        :param HyperThreading: 对超线程的变更
有效值：

    Open：开启
    Close：关闭
    NoChange：不改变

        :type PathPrefix: String
        :param NvmeDataFileType: NVME数据盘类型
有效值：

    EXT4
    XFS

        :type PathPrefix: String
        :param NvmeDataDiskCatalogue: NVME数据盘目录
        :type PathPrefix: String
        :param NvmeDataDiskCatalogueSuffix: NVME数据盘目录后缀属性
        :type PathPrefix: String
        :param BondAttribute: 网卡bond的属性
有效值： bond0|bond1
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
添加白名单的用户为必填项



        :type PathPrefix: String
        :param ZoneId: 创建pdns所需参数
        :type PathPrefix: String
        :param ZoneType: 创建pdns所需参数
        :type PathPrefix: String
        :param HostNameStartNo: 实例起始值
        :type PathPrefix: Int
        :param ComputerNameStartNo: 计算机名称起始值
        :type PathPrefix: Int
        :param Amount: 数量
        :type PathPrefix: Int
        :param TimedRegularization: 释义：试用定时转正
有效值： 
    ▪ support：开启
    ▪ unsupport：关闭
默认值：unsupport，不传默认关闭
        :type PathPrefix: String
        :param PasswordInherit: 有效值：
▪ support：开启
▪ unsupport：关闭
默认值：unsupport
        :type PathPrefix: String
        :param DataDiskMount: 有效值：
▪ support：开启
▪ unsupport：关闭
默认值：support
        :type PathPrefix: String
        :param StorageRoceNetworkCardName: 存储网卡名称，有效值：
eth8x_bond
storage_bond
        :type PathPrefix: String
        """
        self.HostType = None
        self.AvailabilityZone = None
        self.Raid = None
        self.RaidId = None
        self.ImageId = None
        self.NetworkInterfaceMode = None
        self.SubnetId = None
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
        self.CloudMonitorAgent = None
        self.ExtensionSubnetId = None
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
        self.BondAttribute = None
        self.ContainerAgent = None
        self.KesAgent = None
        self.KmrAgent = None
        self.ComputerName = None
        self.OverclockingAttribute = None
        self.GpuImageDriverId = None
        self.SystemVolumeType = None
        self.SystemVolumeSize = None
        self.RoceNetwork = None
        self.ZoneId = None
        self.ZoneType = None
        self.HostNameStartNo = None
        self.ComputerNameStartNo = None
        self.Amount = None
        self.TimedRegularization = None
        self.PasswordInherit = None
        self.DataDiskMount = None
        self.StorageRoceNetworkCardName = None

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
        if params.get("CloudMonitorAgent"):
            self.CloudMonitorAgent = params.get("CloudMonitorAgent")
        if params.get("ExtensionSubnetId"):
            self.ExtensionSubnetId = params.get("ExtensionSubnetId")
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
        if params.get("BondAttribute"):
            self.BondAttribute = params.get("BondAttribute")
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
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("ZoneType"):
            self.ZoneType = params.get("ZoneType")
        if params.get("HostNameStartNo"):
            self.HostNameStartNo = params.get("HostNameStartNo")
        if params.get("ComputerNameStartNo"):
            self.ComputerNameStartNo = params.get("ComputerNameStartNo")
        if params.get("Amount"):
            self.Amount = params.get("Amount")
        if params.get("TimedRegularization"):
            self.TimedRegularization = params.get("TimedRegularization")
        if params.get("PasswordInherit"):
            self.PasswordInherit = params.get("PasswordInherit")
        if params.get("DataDiskMount"):
            self.DataDiskMount = params.get("DataDiskMount")
        if params.get("StorageRoceNetworkCardName"):
            self.StorageRoceNetworkCardName = params.get("StorageRoceNetworkCardName")


class DescribeUseHotStandbyRecordsRequest(AbstractModel):
    """DescribeUseHotStandbyRecords请求参数结构体
    """

    def __init__(self):
        r"""DescribeUseHotStandbyRecords
        :param Filter.N: 有效值：

fault-host-id，故障机实例ID，仅支持精确查询
hot-standby-host-id，热备机实例ID
fault-sn，故障机SN
fault-private-ip，故障机内网ip
fault-host-type，故障机类型
hot-standby-sn，热备机sn
hot-standby-private-ip，热备机内网ip
hot-standby-host-type，热备机机型
replace-type，热备替换类型
        :type PathPrefix: Object
        :param MaxResults: 每页条数
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.Filter.N = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("Filter.N"):
            self.Filter.N = params.get("Filter.N")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeGpuRoceTopologyRequest(AbstractModel):
    """DescribeGpuRoceTopology请求参数结构体
    """

    def __init__(self):
        r"""查询拓扑结构接口
        :param SpineName: Spine名称
        :type PathPrefix: String
        """
        self.SpineName = None

    def _deserialize(self, params):
        if params.get("SpineName"):
            self.SpineName = params.get("SpineName")


class ModifyProcessRequest(AbstractModel):
    """ModifyProcess请求参数结构体
    """

    def __init__(self):
        r"""修改工单信息
        :param OperationProcessId: 工单id
        :type PathPrefix: String
        :param Confirm: 确认是否可以重启，只允许从不允许重启调整到允许重启
有效值：
• 0：可以重启

        :type PathPrefix: String
        :param Status: 客户主动修改工单状态，支持客户关闭，用户选择关闭后如已发起NOC工单则需要取消NOC工单
有效值：
• UserClose
        :type PathPrefix: String
        :param Content: 工单内容
        :type PathPrefix: String
        """
        self.OperationProcessId = None
        self.Confirm = None
        self.Status = None
        self.Content = None

    def _deserialize(self, params):
        if params.get("OperationProcessId"):
            self.OperationProcessId = params.get("OperationProcessId")
        if params.get("Confirm"):
            self.Confirm = params.get("Confirm")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("Content"):
            self.Content = params.get("Content")


class ConfirmProcessRequest(AbstractModel):
    """ConfirmProcess请求参数结构体
    """

    def __init__(self):
        r"""客户评价工单
        :param OperationProcessId: 工单id
状态要求：仅支持工单状态为已完成的工单进行客户评价

        :type PathPrefix: String
        :param UserConfirmAvailable: 客户确认是否维修完成可恢复业务
有效值：
• Available
• Unavailable
        :type PathPrefix: String
        """
        self.OperationProcessId = None
        self.UserConfirmAvailable = None

    def _deserialize(self, params):
        if params.get("OperationProcessId"):
            self.OperationProcessId = params.get("OperationProcessId")
        if params.get("UserConfirmAvailable"):
            self.UserConfirmAvailable = params.get("UserConfirmAvailable")


class DescribeModelConfigRequest(AbstractModel):
    """DescribeModelConfig请求参数结构体
    """

    def __init__(self):
        r"""查询AI模型配置
        :param MaxResults: 单次调用可返回的最大条目数量. 传入返回的 NextToken 值可以获取剩余的其它条目. 这个值可以允许的范围是 5- 1000.
类型: Int
是否必填：否
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
类型: String
是否必填：否
        :type PathPrefix: String
        :param ImageId: 镜像ID
        :type PathPrefix: String
        :param HostType: 实例类型
        :type PathPrefix: String
        :param GpuImageDriverId: gpu驱动ID
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.NextToken = None
        self.ImageId = None
        self.HostType = None
        self.GpuImageDriverId = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("HostType"):
            self.HostType = params.get("HostType")
        if params.get("GpuImageDriverId"):
            self.GpuImageDriverId = params.get("GpuImageDriverId")


class DescribeRoceEventRequest(AbstractModel):
    """DescribeRoceEvent请求参数结构体
    """

    def __init__(self):
        r"""查询Roce事件告警
        :param MaxResults: 每页大小
        :type PathPrefix: Int
        :param NextToken: 第几条
        :type PathPrefix: String
        :param Filter.N: 
        :type PathPrefix: Object
        :param HostId.N: 实例ID
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.NextToken = None
        self.Filter.N = None
        self.HostId.N = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("Filter.N"):
            self.Filter.N = params.get("Filter.N")
        if params.get("HostId.N"):
            self.HostId.N = params.get("HostId.N")


class DescribeRoceEventDetailsRequest(AbstractModel):
    """DescribeRoceEventDetails请求参数结构体
    """

    def __init__(self):
        r"""查询Roce事件告警历史
        :param EventId: 事件ID
        :type PathPrefix: String
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 
获取另一页返回结果的 token
        :type PathPrefix: String
        """
        self.EventId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("EventId"):
            self.EventId = params.get("EventId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class BatchCreateProcessRequest(AbstractModel):
    """BatchCreateProcess请求参数结构体
    """

    def __init__(self):
        r"""批量创建工单
        :param InstanceId: 发起工单的实例ID

        :type PathPrefix: Filter
        :param AvailabilityZone: 可用区
        :type PathPrefix: String
        :param Attribute: 问题属性
默认值：Other
有效值：Move|DevicePort|Network|Disk|Memory|Cpu|Gpu|RaidCard|NetworkInterfaceCard|Other
        :type PathPrefix: String
        :param Content: 工单描述
        :type PathPrefix: String
        :param LogFileName: 需要客户提供的文件名，需要带文件格式，需要与LogFile.N共同使用
例如：test.csv、test.log
        :type PathPrefix: Filter
        :param LogFile: 工单日志文件，base64编码，需要与LogFileName.N共同使用
E2LWQxOWU0ZWYwYjk2YSwwN2M4YThiZi0zMThmLTQxNjctYWVhNi1kMTllNGVmMGI5NmEsMjAyMC0wNS0xMiAyMTowNTo1NiwyMDIwLTA1LTEyIDIyOjU1OjQyLCJFUEPN0Lncv827p6Osv827p7j8u7u3/s7xxvfN+L+oo6zW2NDCyrax8E1BQ7Ki1tjG9Lf+zvHG96GjIiwsbnVsbCwsLCwKMjAwMDExNzcwMSwwMDkzNDU3UDIwMDdDMDAwNDIJLGNuLXNoYW5naGFpLTJhLM3QudxFUEO/zbuno6y4/Lu7zfi/qE1BQ7XY1re4/NDCsqLW2Mb0LLK7v8nS1NbYxvQszfi/qCwsLCwsLCw3OTg3YmVmOC0yNzY3LTRiZjktODdlMS01MjJkYjEwZTEyMGQs0tHN6rPJLDI1ZDk5ZDExLWQ0NTgtNDUyYy04ZWU5LTM1Yjk2MDIwNzcyNSwyNWQ5OWQxMS1kNDU4LTQ1MmMtOGVlOS0zNWI5NjAyMDc3MjUsMjAyMC0wNS0xMiAyMTowNTo1NiwyMDIwLTA1LTEyIDIyOjU1OjQyLCJFUEPN0Lncv827p6Osv827p7j8u7u3/s7xxvfN+L+oo6zW2NDCyrax8E1BQ7Ki1tjG9Lf+zvHG96GjIiwsbnVsbCwsLCwK大小：大小低于100MB
        :type PathPrefix: Filter
        :param LogUrl: 支持上传已授权给金山云的ks3的bucket的URL
        :type PathPrefix: Filter
        :param MachineCount: 服务器数量，数量需与实例id数量一致，单次最大支持50个
默认值：1
        :type PathPrefix: Int
        :param Title: 工单标题
        :type PathPrefix: String
        :param Type: 操作类型
有效值：fix
        :type PathPrefix: String
        :param Confirm: 确认是否重启
有效值：0禁止重启，1可以重启
        :type PathPrefix: String
        :param ProcessSource: 工单来源，0：客户自己提 1：售后代提
默认值：0
        :type PathPrefix: Int
        :param AutoNocCase: 是否自动发起NOC工单，0：不发起 1：发起
默认值：0
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.AvailabilityZone = None
        self.Attribute = None
        self.Content = None
        self.LogFileName = None
        self.LogFile = None
        self.LogUrl = None
        self.MachineCount = None
        self.Title = None
        self.Type = None
        self.Confirm = None
        self.ProcessSource = None
        self.AutoNocCase = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("Attribute"):
            self.Attribute = params.get("Attribute")
        if params.get("Content"):
            self.Content = params.get("Content")
        if params.get("LogFileName"):
            self.LogFileName = params.get("LogFileName")
        if params.get("LogFile"):
            self.LogFile = params.get("LogFile")
        if params.get("LogUrl"):
            self.LogUrl = params.get("LogUrl")
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
        if params.get("AutoNocCase"):
            self.AutoNocCase = params.get("AutoNocCase")


class CreateInspectHostRequest(AbstractModel):
    """CreateInspectHost请求参数结构体
    """

    def __init__(self):
        r"""发起故障检测
        :param InspectType: 故障检测类型
• 有效值：
    ◦ nccl：需要通过NCCL检查异常情况
    ◦ xid：需要通过XID检查异常情况
        :type PathPrefix: String
        :param InspectName: 故障检测名称
        :type PathPrefix: String
        :param HostId: 裸金属服务器资源ID，多个ID的实例信息，查看详细ID.N使用方式
        :type PathPrefix: Filter
        """
        self.InspectType = None
        self.InspectName = None
        self.HostId = None

    def _deserialize(self, params):
        if params.get("InspectType"):
            self.InspectType = params.get("InspectType")
        if params.get("InspectName"):
            self.InspectName = params.get("InspectName")
        if params.get("HostId"):
            self.HostId = params.get("HostId")


class DescribeInspectHostResultsRequest(AbstractModel):
    """DescribeInspectHostResults请求参数结构体
    """

    def __init__(self):
        r"""查询故障检测结果
        :param InspectId: 故障检测工单ID，可查询多个ID的信息，查看详细ID.N使用方式
        :type PathPrefix: Filter
        :param MaxResults: 单次调用可返回的最大条目数量. 传入返回的 NextToken 值可以获取剩余的其它条目. 这个值可以允许的范围是 5- 1000.
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        """
        self.InspectId = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("InspectId"):
            self.InspectId = params.get("InspectId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class DescribeXidDetailsRequest(AbstractModel):
    """DescribeXidDetails请求参数结构体
    """

    def __init__(self):
        r"""查询Xid事件详情
        :param StartTime: 事件开始时间
        :type PathPrefix: String
        :param EndTime: 事件结束时间
        :type PathPrefix: String
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Name: 事件名称
XidError
SXidError
默认：
XidError
        :type PathPrefix: String
        :param MaxResults: 每页条数
        :type PathPrefix: Int
        :param NextToken: 页码偏移量
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.InstanceId = None
        self.Name = None
        self.MaxResults = None
        self.NextToken = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")


class RunSoInstancesRequest(AbstractModel):
    """RunSoInstances请求参数结构体
    """

    def __init__(self):
        r"""创建星海实例
        :param ImageId: 镜像ID
        :type PathPrefix: String
        :param InstanceName: 实例名称
        :type PathPrefix: String
        :param InstanceTypeId: 机型
        :type PathPrefix: String
        :param SecurityGroupId: 安全组
        :type PathPrefix: Filter
        :param SubnetId: 子网ID
        :type PathPrefix: String
        :param Volumes: 
        :type PathPrefix: Object
        :param ZoneId: 可用区
        :type PathPrefix: String
        :param Description: 实例的描述，默认为空字符串。
    ◦ 必须以字母或中文开头。
    ◦ 只能包含中文、字母、数字、点号“.”、空格、下划线“_”、中划线“-”、等号“=”、英文逗号“,”、中文逗号“，”和中文句号“。”
    ◦ 长度限制在255个字符以内。
示例值：用于测试的云服务器实例
        :type PathPrefix: String
        :param HostName: 实例主机名，即实例操作系统内部的计算机名。
    ◦ Linux实例：
    ◦ 允许使用字母、数字、点号“.”或中划线“-”。
    ◦ 不能以中划线、点号开头或结尾，且不能连续使用中划线和点号。
    ◦ Linux系统长度限制在2～63个字符之间。
        :type PathPrefix: String
        :param InstanceChargeType: 实例和云盘的计费类型，取值：
    ◦ 包年包月Monthly
    ◦ 按量付费（按日月结）Daily（默认）
        :type PathPrefix: String
        :param KeepImageCredential: 是否保留镜像设置，取值：
    ◦ true：保留镜像设置，保留后将使用镜像预设的密码或密钥对登录实例。
    ◦ false（默认）：不保留镜像设置。
    说明
    ◦ 仅自定义镜像支持该功能。
    ◦ 该参数取值为true时，请勿传入PassWord和KeyPairName。
示例值：true
        :type PathPrefix: Boolean
        :param KeyPairName: 如需使用“SSH密钥”方式登录实例，请指定已创建密钥对的名称。
    说明
    ◦ Windows实例不支持SSH密钥方式，即使传入了该参数，仍旧只生效密码Password。
    ◦ Linux实例支持密码或密钥对登录。调用该接口时如果同时设置了密钥对KeyPairName和密码Password，则仅生效密钥对KeyPairName。
示例值：kp-test-123
        :type PathPrefix: String
        :param Password: 如需使用“密码”方式登录实例，请通过该参数指定实例的管理员账号初始登录密码。其中Linux管理员账号为root，Windows管理员账号为Administrator。
    密码复杂度要求如下：
    ◦ 长度限制在8～30之间。
    ◦ 密码只能由大写字母、小写字母、数字和特殊字符组成，且必须包含至少三项。
    ◦ 特殊字符可以使用：`~!@#$%^&*()_-+=|{}[]:;'<>,.?/
    ◦ 不能以“/”和“$6$”开头。
    说明：登录凭证支持“密码”、“密钥对”、“保留镜像设置”三种方式，使用“密码”方式登录实例时，建议增加密码复杂度以提高安全性。
        :type PathPrefix: String
        :param Period: 购买资源的时长（月）。
    ◦ 取值：1、2、3、4、5、6、7、8、9、12、24、36、48、60
    ◦ 默认值：1
说明：仅当参数InstanceChargeType取值为Monthly时，该参数生效且为必选值
        :type PathPrefix: Int
        :param SuffixIndex: 有序后缀的起始序号，取值：1～999，默认值为1。
示例值：1
        :type PathPrefix: Int
        :param UniqueSuffix: 表示当创建多台实例时，是否为Hostname和InstanceName自动添加有序后缀，取值：
    ◦ true：开启有序后缀。
    ◦ false（默认）：关闭有序后缀。
        :type PathPrefix: Boolean
        :param InstallRunCommandAgent: 创建实例时是否安装云助手Agent，取值：
    ◦ true：创建时安装。
    ◦ false（默认）：创建时不安装。

        :type PathPrefix: Boolean
        :param Count: 创建数量，取值范围：1～100；传入0时，会默认为1。
示例值：1
        :type PathPrefix: Int
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ImageId = None
        self.InstanceName = None
        self.InstanceTypeId = None
        self.SecurityGroupId = None
        self.SubnetId = None
        self.Volumes = None
        self.ZoneId = None
        self.Description = None
        self.HostName = None
        self.InstanceChargeType = None
        self.KeepImageCredential = None
        self.KeyPairName = None
        self.Password = None
        self.Period = None
        self.SuffixIndex = None
        self.UniqueSuffix = None
        self.InstallRunCommandAgent = None
        self.Count = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstanceTypeId"):
            self.InstanceTypeId = params.get("InstanceTypeId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("Volumes"):
            self.Volumes = params.get("Volumes")
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("InstanceChargeType"):
            self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("KeepImageCredential"):
            self.KeepImageCredential = params.get("KeepImageCredential")
        if params.get("KeyPairName"):
            self.KeyPairName = params.get("KeyPairName")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("Period"):
            self.Period = params.get("Period")
        if params.get("SuffixIndex"):
            self.SuffixIndex = params.get("SuffixIndex")
        if params.get("UniqueSuffix"):
            self.UniqueSuffix = params.get("UniqueSuffix")
        if params.get("InstallRunCommandAgent"):
            self.InstallRunCommandAgent = params.get("InstallRunCommandAgent")
        if params.get("Count"):
            self.Count = params.get("Count")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DescribeSoImagesRequest(AbstractModel):
    """DescribeSoImages请求参数结构体
    """

    def __init__(self):
        r"""查询星海镜像
        :param ImageId: 镜像的ID，最多支持100个ID。
• 参数 - N：表示镜像ID的序号。
• 多个镜像ID之间用&分隔。
        :type PathPrefix: Filter
        :param ImageName: 镜像名称。
        :type PathPrefix: String
        :param IsSupportCloudInit: 镜像是否支持Cloud-init。取值：
• true：支持
• false：不支持
        :type PathPrefix: Boolean
        :param MaxResults: 分页查询时设置的每页行数。
• 取值范围：1 ~ 100
• 默认值：15
        :type PathPrefix: Int
        :param NextToken: 分页查询凭证，用于标记分页的位置，初次调用该接口时无需设置。下次查询时，取值为上一次API调用返回的NextToken参数值。
        :type PathPrefix: String
        :param OsType: 操作系统类型。取值：
• Linux
• Windows
        :type PathPrefix: String
        :param Platform: 镜像操作系统的发行版本。取值：
• CentOS
• Debian
• Windows Server
• Ubuntu
        :type PathPrefix: String
        :param Status: 镜像状态，最多支持10个。取值：
• available（默认）：可用
• creating：创建中
• error：错误
说明
• 参数 - N：表示镜像状态的序号。
• 多个镜像状态之间用&分隔。
        :type PathPrefix: Filter
        :param Visibility: 镜像的可见性。取值：
• public：公共镜像
• private：自定义镜像
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ImageId = None
        self.ImageName = None
        self.IsSupportCloudInit = None
        self.MaxResults = None
        self.NextToken = None
        self.OsType = None
        self.Platform = None
        self.Status = None
        self.Visibility = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("ImageName"):
            self.ImageName = params.get("ImageName")
        if params.get("IsSupportCloudInit"):
            self.IsSupportCloudInit = params.get("IsSupportCloudInit")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("OsType"):
            self.OsType = params.get("OsType")
        if params.get("Platform"):
            self.Platform = params.get("Platform")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("Visibility"):
            self.Visibility = params.get("Visibility")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class RebootSoInstanceRequest(AbstractModel):
    """RebootSoInstance请求参数结构体
    """

    def __init__(self):
        r"""重启星海实例
        :param ForceStop: 重启实例前是否强制关机，取值：
• true：强制关机。相当于典型的断电操作，所有未写入存储设备的缓存数据会丢失。
• false（默认）：正常关机。
说明
以下类型的实例，ForceStop无论取值为true还是false，实例均会执行强制关机。
• 弹性裸金属实例。
• 高性能计算GPU型ebmhpcpni2l 、ebmhpcpni2、ebmhpchfpni2实例。
示例值：false

        :type PathPrefix: Boolean
        :param InstanceIds: 实例ID，最多支持100个ID。
• 参数 - N：表示实例的序号。
• 多个Instance ID之间用&分隔。
示例值：InstanceIds.1=8981d45e-b3dc-44c6-b02f-2d1969551316&InstanceIds.2=8981d45e-b3dc-44c6-b02f-2d1969551318
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ForceStop = None
        self.InstanceIds = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ForceStop"):
            self.ForceStop = params.get("ForceStop")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DeleteSoImagesRequest(AbstractModel):
    """DeleteSoImages请求参数结构体
    """

    def __init__(self):
        r"""删除星海自定义镜像
        :param ImageIds: 自定义镜像ID，最多支持100个ID。
• 参数 -N：表示镜像的序号。
• 多个Image ID之间用&分隔。
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ImageIds = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ImageIds"):
            self.ImageIds = params.get("ImageIds")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DeleteSoVpcRequest(AbstractModel):
    """DeleteSoVpc请求参数结构体
    """

    def __init__(self):
        r"""删除星海私有网络
        :param VpcId: 待删除VPC的ID。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.VpcId = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DescribeSoAvailableResourceRequest(AbstractModel):
    """DescribeSoAvailableResource请求参数结构体
    """

    def __init__(self):
        r"""查询可用区资源的库存信息
        :param InstanceChargeType: 资源的计费类型。取值：
• 包年包月Monthly
• 按日月结Daily
• 试用Trial
示例值：Daily

        :type PathPrefix: String
        :param InstanceTypeId: 指定一个要查询的实例规格。
示例值：SO-GM404-I
        :type PathPrefix: String
        :param ZoneId: 可用区ID。
说明：默认为空，表示返回当前地域（RegionId）下的所有可用区中所有符合条件的资源。
示例值：cn-beijing-6a
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.InstanceChargeType = None
        self.InstanceTypeId = None
        self.ZoneId = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("InstanceChargeType"):
            self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceTypeId"):
            self.InstanceTypeId = params.get("InstanceTypeId")
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DescribeSoInstancesRequest(AbstractModel):
    """DescribeSoInstances请求参数结构体
    """

    def __init__(self):
        r"""获取星海实例信息
        :param InstanceChargeType: 实例的计费方式，取值：
• PostPaid：按量计费
• PrePaid：包年包月
示例值：PostPaid
        :type PathPrefix: String
        :param InstanceTypeId: 根据规格过滤实例，最多支持100个实例规格。
• 参数 - N：表示实例的序号。
undefined多个实例规格之间用&分隔
        :type PathPrefix: Filter
        :param KeyPairName: 密钥对的名称。
        :type PathPrefix: String
        :param MaxResults: 分页查询时设置的每页行数。
        :type PathPrefix: Int
        :param NextToken: 分页查询凭证。
        :type PathPrefix: String
        :param PrimaryIpAddress: 实例的私网IP地址，例如主网卡或辅助网卡IP地址。
        :type PathPrefix: String
        :param Status: 实例的状态，取值：
• CREATING：创建中
• RUNNING：运行中
• STOPPING：停止中
• STOPPED：已停止
• REBOOTING: 重启中
• STARTING：启动中
• REBUILDING：重装中
• RESIZING：更配中
• ERROR：错误
• DELETING：删除中
        :type PathPrefix: String
        :param VpcId: 私有网络ID。
        :type PathPrefix: String
        :param ZoneId: 实例所属可用区ID。
        :type PathPrefix: String
        :param InstanceIds: 实例ID，最多支持100个。
• 参数 - N：表示实例的序号。
• 多个Instance ID之间用&分隔。
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.InstanceChargeType = None
        self.InstanceTypeId = None
        self.KeyPairName = None
        self.MaxResults = None
        self.NextToken = None
        self.PrimaryIpAddress = None
        self.Status = None
        self.VpcId = None
        self.ZoneId = None
        self.InstanceIds = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("InstanceChargeType"):
            self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceTypeId"):
            self.InstanceTypeId = params.get("InstanceTypeId")
        if params.get("KeyPairName"):
            self.KeyPairName = params.get("KeyPairName")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("PrimaryIpAddress"):
            self.PrimaryIpAddress = params.get("PrimaryIpAddress")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DeleteSoInstanceRequest(AbstractModel):
    """DeleteSoInstance请求参数结构体
    """

    def __init__(self):
        r"""删除星海实例
        :param InstanceIds: 实例ID，最多支持100个ID。
• 参数 - N：表示实例的序号。
• 多个Instance ID之间用&分隔。
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.InstanceIds = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DescribeSoSecurityGroupsRequest(AbstractModel):
    """DescribeSoSecurityGroups请求参数结构体
    """

    def __init__(self):
        r"""查询星海安全组信息
        :param VpcId: 安全组所属VPC的ID。
        :type PathPrefix: String
        :param SecurityGroupIds: 安全组的ID列表。
• 参数 - N：表示安全组ID的序号，单次调用数量上限为100个。
• 多个安全组用&分隔。
        :type PathPrefix: Filter
        :param NextToken: 分页查询凭证，用于标记分页的位置。
• 不填则从头开始查询。
• 传入之前调用本API返回的NextToken，则从该次API调用标记分页的位置往后开始查询。
        :type PathPrefix: String
        :param MaxResults: 查询的数量，默认为 10，最大为100。
        :type PathPrefix: Int
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.VpcId = None
        self.SecurityGroupIds = None
        self.NextToken = None
        self.MaxResults = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class CreateSoVpcRequest(AbstractModel):
    """CreateSoVpc请求参数结构体
    """

    def __init__(self):
        r"""创建星海私有网络
        :param VpcName: VPC的名称。
        :type PathPrefix: String
        :param Description: VPC的描述信息。
        :type PathPrefix: String
        :param CidrBlock: VPC的IPv4网段。可以使用以下网段或其子集作为VPC的IPv4网段：
• 192.168.0.0/16 ~ 24
• 10.0.0.0/8 ~ 24
• 172.16.0.0/12 ~ 24
        :type PathPrefix: String
        :param DnsServers: VPC的DNS服务器地址。
• 参数 - N：表示DNS服务器地址的序号，单次调用数量上限为5个，每个DnsServer必须以合法IP形式给出。
• 多个IP之间用&分隔。
• 不填则配置为默认DNS服务器地址。
        :type PathPrefix: Filter
        :param AttachVpcId: 关联的VPC ID
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.VpcName = None
        self.Description = None
        self.CidrBlock = None
        self.DnsServers = None
        self.AttachVpcId = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("VpcName"):
            self.VpcName = params.get("VpcName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("CidrBlock"):
            self.CidrBlock = params.get("CidrBlock")
        if params.get("DnsServers"):
            self.DnsServers = params.get("DnsServers")
        if params.get("AttachVpcId"):
            self.AttachVpcId = params.get("AttachVpcId")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DeleteSoSubnetRequest(AbstractModel):
    """DeleteSoSubnet请求参数结构体
    """

    def __init__(self):
        r"""删除星海子网信息
        :param SubnetId: 待删除子网的ID。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.SubnetId = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DescribeSoKeyPairsRequest(AbstractModel):
    """DescribeSoKeyPairs请求参数结构体
    """

    def __init__(self):
        r"""查询星海密钥对
        :param FingerPrint: 密钥对的指纹。根据RFC4716定义的公钥指纹格式，采用MD5信息摘要算法。
        :type PathPrefix: String
        :param KeyPairIds: 密钥对ID，最多支持100个。
• 参数 - N：表示密钥对ID的序号。
• 多个密钥对ID之间用&分隔。
示例值：KeyPairIds.1=2c67be69-b508-48e4-a460-fe491e8d49ba
        :type PathPrefix: Filter
        :param KeyPairName: 密钥对名称，支持模糊搜索。
        :type PathPrefix: String
        :param KeyPairNames: 密钥对名称，最多支持100个。
• 参数 - N：表示密钥对的序号。
• 多个密钥对之间用&分隔。
        :type PathPrefix: Filter
        :param MaxResults: 分页查询时设置的每页行数。
• 最大值：500
• 默认值：10
        :type PathPrefix: Int
        :param NextToken: 分页查询凭证，用于标记分页的位置，初次调用该接口时无需设置。下次查询时，取值为上一次API调用返回的NextToken参数值。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.FingerPrint = None
        self.KeyPairIds = None
        self.KeyPairName = None
        self.KeyPairNames = None
        self.MaxResults = None
        self.NextToken = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("FingerPrint"):
            self.FingerPrint = params.get("FingerPrint")
        if params.get("KeyPairIds"):
            self.KeyPairIds = params.get("KeyPairIds")
        if params.get("KeyPairName"):
            self.KeyPairName = params.get("KeyPairName")
        if params.get("KeyPairNames"):
            self.KeyPairNames = params.get("KeyPairNames")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class StartSoInstanceRequest(AbstractModel):
    """StartSoInstance请求参数结构体
    """

    def __init__(self):
        r"""启动星海实例
        :param InstanceIds: 实例ID。
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.InstanceIds = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DescribeSoInstanceTypesRequest(AbstractModel):
    """DescribeSoInstanceTypes请求参数结构体
    """

    def __init__(self):
        r"""获取实例规格信息
        :param ImageId: 镜像ID，查询该镜像可创建的实例规格
        :type PathPrefix: String
        :param InstanceTypeId: 指定查询的实例规格
• 参数 - N：表示实例规格的序号，取值范围：1～100。N大于100时，仅前100个生效。
• 多个InstanceTypeId 之间用&分隔。
说明：不传则默认查询所有实例规格的信息。
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ImageId = None
        self.InstanceTypeId = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("InstanceTypeId"):
            self.InstanceTypeId = params.get("InstanceTypeId")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class ModifySoSubnetAttributesRequest(AbstractModel):
    """ModifySoSubnetAttributes请求参数结构体
    """

    def __init__(self):
        r"""修改星海指定子网信息
        :param SubnetId: 待修改信息的子网的ID。
        :type PathPrefix: String
        :param SubnetName: 子网的名称。
        :type PathPrefix: String
        :param Description: 子网的描述信息。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.SubnetId = None
        self.SubnetName = None
        self.Description = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("SubnetName"):
            self.SubnetName = params.get("SubnetName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DescribeSoSubnetRequest(AbstractModel):
    """DescribeSoSubnet请求参数结构体
    """

    def __init__(self):
        r"""查询星海子网信息
        :param ZoneId: 子网所属可用区的ID。
        :type PathPrefix: String
        :param SubnetName: 子网的名称。
        :type PathPrefix: String
        :param VpcId: 子网所属VPC的ID。
        :type PathPrefix: String
        :param SubnetIds: 子网的ID。
• 参数 - N：表示子网ID的序号，单次调用数量上限为100个。
• 多个ID之间用&分隔。
        :type PathPrefix: Filter
        :param NextToken: 分页查询凭证，用于标记分页的位置。
• 不填则从头开始查询。
• 传入之前调用本API返回的NextToken，则从该次API调用标记分页的位置往后开始查询。
        :type PathPrefix: String
        :param MaxResults: 查询的数量，默认为 10，最大为100。
        :type PathPrefix: Int
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ZoneId = None
        self.SubnetName = None
        self.VpcId = None
        self.SubnetIds = None
        self.NextToken = None
        self.MaxResults = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("SubnetName"):
            self.SubnetName = params.get("SubnetName")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetIds"):
            self.SubnetIds = params.get("SubnetIds")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class ModifySoKeyPairAttributeRequest(AbstractModel):
    """ModifySoKeyPairAttribute请求参数结构体
    """

    def __init__(self):
        r"""修改星海密钥对信息
        :param Description: 密钥对的描述，默认值为空字符串。
• 必须以字母或中文开头。
• 只能包含中文、字母、数字、点“.”、空格、下划线“_”、中划线“-”、等号“=”、英文逗号“,”、中文逗号“，”和中文句号“。”
• 长度限制在255个字符以内。
• 传入空字符串时，将清空原有描述信息。
        :type PathPrefix: String
        :param KeyPairId: 密钥对唯一ID。
• KeyPairName与KeyPairId不允许同时为空。
• 如果同时设置了KeyPairName与KeyPairId，则优先生效KeyPairId。
        :type PathPrefix: String
        :param KeyPairName: 密钥对名称。
• KeyPairName与KeyPairId不允许同时为空。
• 如果同时设置了KeyPairName与KeyPairId，则优先生效KeyPairId。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.Description = None
        self.KeyPairId = None
        self.KeyPairName = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("KeyPairId"):
            self.KeyPairId = params.get("KeyPairId")
        if params.get("KeyPairName"):
            self.KeyPairName = params.get("KeyPairName")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class ModifySoImageAttributeRequest(AbstractModel):
    """ModifySoImageAttribute请求参数结构体
    """

    def __init__(self):
        r"""修改星海镜像信息
        :param BootMode: 镜像的启动模式，不填则保持原有配置。取值：
• BIOS：BIOS启动模式
• UEFI：UEFI启动模式
        :type PathPrefix: String
        :param Description: 镜像描述
        :type PathPrefix: String
        :param ImageId: 自定义镜像ID。
        :type PathPrefix: String
        :param ImageName: 镜像名称。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.BootMode = None
        self.Description = None
        self.ImageId = None
        self.ImageName = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("BootMode"):
            self.BootMode = params.get("BootMode")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("ImageName"):
            self.ImageName = params.get("ImageName")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class ModifySoVpcAttributesRequest(AbstractModel):
    """ModifySoVpcAttributes请求参数结构体
    """

    def __init__(self):
        r"""修改星海私有网络
        :param VpcId: 待修改信息的VPC的ID。
        :type PathPrefix: String
        :param Description: VPC的描述信息。
        :type PathPrefix: String
        :param DnsServers: VPC的DNS服务器地址。
• 参数 - N：表示DNS服务器地址的序号，单次调用数量上限为5个，每个DnsServer必须以合法IP形式给出。
• 多个IP之间用&分隔。
• 不填则配置为默认DNS服务器地址。
        :type PathPrefix: Filter
        :param VpcName: VPC的名称。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.VpcId = None
        self.Description = None
        self.DnsServers = None
        self.VpcName = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("DnsServers"):
            self.DnsServers = params.get("DnsServers")
        if params.get("VpcName"):
            self.VpcName = params.get("VpcName")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class ReplaceSoSystemVolumeRequest(AbstractModel):
    """ReplaceSoSystemVolume请求参数结构体
    """

    def __init__(self):
        r"""星海更换操作系统
        :param ImageId: 更换操作系统时使用的镜像ID。
        :type PathPrefix: String
        :param InstanceId: 实例ID。
        :type PathPrefix: String
        :param KeepImageCredential: 使用镜像预设密码/密钥对登录实例。取值：
• true：使用镜像预设密码/密钥对登录。
• false（默认）：不使用镜像预设密码/密钥对登录。
说明
• 仅自定义镜像支持使用该功能。
• 该参数为true时，请勿传入PassWord和KeyPairName。
        :type PathPrefix: Boolean
        :param KeyPairName: 重置密钥对。
说明
• 仅对Linux操作系统的实例生效。
• KeepImageCredential为false时，本参数与Password不能同时为空。
• 若同时设置了密钥对KeyPairName和密码Password，则仅生效密钥对KeyPairName。
        :type PathPrefix: String
        :param Password: 重置密码
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ImageId = None
        self.InstanceId = None
        self.KeepImageCredential = None
        self.KeyPairName = None
        self.Password = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("KeepImageCredential"):
            self.KeepImageCredential = params.get("KeepImageCredential")
        if params.get("KeyPairName"):
            self.KeyPairName = params.get("KeyPairName")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class CreateSoSubnetRequest(AbstractModel):
    """CreateSoSubnet请求参数结构体
    """

    def __init__(self):
        r"""创建星海子网
        :param VpcId: 要创建的子网所属VPC的ID。
        :type PathPrefix: String
        :param ZoneId: 要创建的子网所属的可用区ID
        :type PathPrefix: String
        :param SubnetName: 子网的名称。
        :type PathPrefix: String
        :param Description: 子网的描述信息。
        :type PathPrefix: String
        :param CidrBlock: 子网的网段。
• 子网的网段必须从属于子网所属VPC的网段。
• 子网网段不能与所属VPC路由条目的目标网段相同，但可以是目标网段的子集。
• 子网网段的掩码长度与VPC网段相关，具体如下：
    ◦ 10.XX.XX.XX网段掩码范围：8 ~ 29
    ◦ 172.16.XX.XX网段掩码范围：12 ~ 29
    ◦ 192.168.XX.XX网段掩码范围：16 ~ 29
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.VpcId = None
        self.ZoneId = None
        self.SubnetName = None
        self.Description = None
        self.CidrBlock = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("ZoneId"):
            self.ZoneId = params.get("ZoneId")
        if params.get("SubnetName"):
            self.SubnetName = params.get("SubnetName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("CidrBlock"):
            self.CidrBlock = params.get("CidrBlock")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DescribeSoVpcsRequest(AbstractModel):
    """DescribeSoVpcs请求参数结构体
    """

    def __init__(self):
        r"""查询星海私有网络
        :param VpcName: VPC的名称。
        :type PathPrefix: String
        :param VpcIds: VPC的ID。
• 参数 - N：表示VPC ID的序号，单次调用数量上限为100个。
• 多个VPC ID之间用&分隔。
        :type PathPrefix: Filter
        :param NextToken: 分页查询凭证，用于标记分页的位置。
• 不填则从头开始查询。
• 传入之前调用本API返回的NextToken，则从该次API调用标记分页的位置往后开始查询。
        :type PathPrefix: String
        :param MaxResults: 
        :type PathPrefix: Int
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.VpcName = None
        self.VpcIds = None
        self.NextToken = None
        self.MaxResults = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("VpcName"):
            self.VpcName = params.get("VpcName")
        if params.get("VpcIds"):
            self.VpcIds = params.get("VpcIds")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class StopSoInstanceRequest(AbstractModel):
    """StopSoInstance请求参数结构体
    """

    def __init__(self):
        r"""停止星海实例
        :param ForceStop: 是否强制关机，取值：
• true：强制关机。相当于典型的断电操作，所有未写入存储设备的缓存数据会丢失。
• false（默认）：正常关机。
说明
以下类型的实例，ForceStop无论取值为true还是false，实例均会执行强制关机。
• 弹性裸金属实例。
• 高性能计算GPU型ebmhpcpni2l 、ebmhpcpni2、ebmhpchfpni2实例。该类实例正在邀测中，如需试用，请联系客户经理申请。
示例值：false
        :type PathPrefix: Boolean
        :param InstanceIds: 实例ID，最多支持100个。
• 参数 - N：表示实例的序号。
• 多个Instance ID之间用&分隔。
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ForceStop = None
        self.InstanceIds = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ForceStop"):
            self.ForceStop = params.get("ForceStop")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class DeleteSoKeyPairsRequest(AbstractModel):
    """DeleteSoKeyPairs请求参数结构体
    """

    def __init__(self):
        r"""删除星海密钥对
        :param KeyPairNames: 密钥对名称，最多支持100个。
• 参数 - N：表示密钥对的序号。
• 多个密钥对之间用&分隔。
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.KeyPairNames = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("KeyPairNames"):
            self.KeyPairNames = params.get("KeyPairNames")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class CreateSoImageRequest(AbstractModel):
    """CreateSoImage请求参数结构体
    """

    def __init__(self):
        r"""创建星海自定义镜像
        :param ForceStop: 重启实例前是否强制关机，取值：
• true：强制关机。相当于典型的断电操作，所有未写入存储设备的缓存数据会丢失。
• false（默认）：正常关机。
说明
以下类型的实例，ForceStop无论取值为true还是false，实例均会执行强制关机。
• 弹性裸金属实例。
• 高性能计算GPU型ebmhpcpni2l 、ebmhpcpni2、ebmhpchfpni2实例。
示例值：false

        :type PathPrefix: Boolean
        :param InstanceIds: 实例ID，最多支持100个ID。
• 参数 - N：表示实例的序号。
• 多个Instance ID之间用&分隔。
示例值：InstanceIds.1=8981d45e-b3dc-44c6-b02f-2d1969551316&InstanceIds.2=8981d45e-b3dc-44c6-b02f-2d1969551318
        :type PathPrefix: Filter
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.ForceStop = None
        self.InstanceIds = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("ForceStop"):
            self.ForceStop = params.get("ForceStop")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class ModifySoInstanceAttributeRequest(AbstractModel):
    """ModifySoInstanceAttribute请求参数结构体
    """

    def __init__(self):
        r"""修改指定实例的信息
        :param DeletionProtection: 实例删除保护属性，指定是否支持通过控制台或API删除实例。取值：
• true：开启实例删除保护。
• false：关闭实例删除保护。
示例值：true
        :type PathPrefix: String
        :param Description: 实例的描述。
• 必须以字母或中文开头。
• 只能包含中文、字母、数字、点“.”、空格、下划线“_”、中划线“-”、等号“=”、英文逗号“,”、中文逗号“，”和中文句号“。”
• 长度限制在255个字符以内。
说明 传入空字符串时，将清空原有描述信息。
示例值：ECS instance for testing.
        :type PathPrefix: String
        :param Hostname: 实例主机名，即实例操作系统内部的计算机名。
• Linux实例：
    ◦ 允许使用字母、数字、点号“.”或中划线“-”。
    ◦ 不能以中划线、点号开头或结尾，且不能连续使用中划线和点号。
    ◦ Linux系统长度限制在2～63个字符之间。
• Windows实例：
    ◦ 允许使用字母、数字或中划线“-”，不能完全是数字。
    ◦ 不能以中划线开头或结尾，且不能连续使用中划线。
    ◦ Windows系统长度限制在2～15个字符之间。
示例值：instance-host-name
        :type PathPrefix: String
        :param InstanceId: 实例ID。
示例值：4f35e8f7-f549-5c55-9531-5f43ca78****
        :type PathPrefix: String
        :param InstanceName: 实例的名称。
• 以字母或中文开头。
• 只能包含中文、字母、数字、下划线“_”、中划线“-”和点号“.”。
• 长度限制为1～128个字符。
示例值：instance-test
        :type PathPrefix: String
        :param Password: 示例值：password@123
使用“密码”方式登录实例时，请设置实例的登录密码。
• 长度限制在8～30之间。
• 密码只能由大写字母、小写字母、数字和特殊字符组成，且必须包含至少三项。
• 特殊字符可以使用：`~!@#$%^&*()_-+=|{}[]:;'<>,.?/
• 不能以“/”和“$6$”开头。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.DeletionProtection = None
        self.Description = None
        self.Hostname = None
        self.InstanceId = None
        self.InstanceName = None
        self.Password = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("DeletionProtection"):
            self.DeletionProtection = params.get("DeletionProtection")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Hostname"):
            self.Hostname = params.get("Hostname")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


class CreateSoKeyPairRequest(AbstractModel):
    """CreateSoKeyPair请求参数结构体
    """

    def __init__(self):
        r"""创建星海密钥对
        :param KeyPairName: 密钥对名称。
• 不可与已有名称重复。
• 长度限制在 2～64 个字符之间。
• 允许使用点号“.”分隔字符成多段，每段允许使用大小写字母、数字或连字符“-”。
• 不能以“-”和“.”开头或结尾，不能连续使用“-”或者“.”。
        :type PathPrefix: String
        :param Description: 密钥对的描述，默认值为空字符串。
• 必须以字母或中文开头。
• 只能包含中文、字母、数字、点“.”、空格、下划线“_”、中划线“-”、等号“=”、英文逗号“,”、中文逗号“，”和中文句号“。”
• 长度限制在255个字符以内。
        :type PathPrefix: String
        :param SoZoneId: 星海专区
        :type PathPrefix: String
        """
        self.KeyPairName = None
        self.Description = None
        self.SoZoneId = None

    def _deserialize(self, params):
        if params.get("KeyPairName"):
            self.KeyPairName = params.get("KeyPairName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("SoZoneId"):
            self.SoZoneId = params.get("SoZoneId")


