from ksyun.common.abstract_model import AbstractModel

class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体
    """

    def __init__(self):
        r"""描述实例信息
        :param MaxResults: 单次调用所返回的最大实例数目
5~1000
        :type PathPrefix: Int
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0

        :type PathPrefix: Int
        :param InstanceId: 待返回描述信息的实例ID列表，N的范围为1-100
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: Filter
        :param ProjectId: 待返回实例信息的项目ID列表，N的范围为1-100

        :type PathPrefix: Filter
        :param Filter: 待返回实例信息的项目ID列表，N的范围为1-100
支持如下过滤器名称<br>instance-id 实例ID<br>subnet-id 子网ID<br>vpc-id vpc ID<br>instance-name 实例名称<br>instance-type 实例类型<br>private-ip-address 内网IP<br>image-id 镜像ID<br>charge-type 计费模式（1（包年包月）、5（按量付费（按日月结））、87（按量付费）、810（竞价型实例））2（按小时计费）, 

84（PostPaidByHour)
<br>ProjectId.N 所属项目<br>network-interface.subnet-id 网络接口关联的子网ID<br>network-interface.network-interface-id 网卡的ID<br>network-interface.group-id 网络接口关联的安全组ID<br>instance-state.name [实例状态](https://docs.ksyun.com/documents/836)<br>availability-zone-name [可用区（AvailabilityZone）](https://docs.ksyun.com/documents/67)
        :type PathPrefix: Filter
        :param Sort: 筛选器
支持如下筛选器名称：<br>InstanceName –主机名称<br>CreationDate –创建时间<br>PrivateIpAddress - 主机内网IP（主网卡）
        :type PathPrefix: String
        :param Search: 搜索条件，模糊匹配
支持字段：实例名（InstanceName）、主网卡私有IP地址（PrivateIpAddress）
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.Marker = None
        self.InstanceId = None
        self.ProjectId = None
        self.Filter = None
        self.Sort = None
        self.Search = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("Sort"):
            self.Sort = params.get("Sort")
        if params.get("Search"):
            self.Search = params.get("Search")


class RunInstancesRequest(AbstractModel):
    """RunInstances请求参数结构体
    """

    def __init__(self):
        r"""创建实例
        :param ImageId: 镜像ID
        :type PathPrefix: String
        :param DedicatedHostId: 专属宿主机ID
        :type PathPrefix: String
        :param InstanceConfigure.VCPU: 实例VCPU核数
        :type PathPrefix: String
        :param InstanceConfigure.MemoryGb: 实例内存
        :type PathPrefix: String
        :param InstanceType: 实例套餐类型
        :type PathPrefix: String
        :param DataDiskGb: 数据卷容量，单位GB
        :type PathPrefix: Int
        :param MaxCount: 最大实例数，如果指定的实例数大于金山云在本人Region所能创建的最大实例数，则会创建大于MinCount数量的最大允许实例数。
        :type PathPrefix: Int
        :param MinCount: 最小实例数，如果指定的实例数大于金山云在本Region所能创建的最大实例数，则不会创建任何实例。
        :type PathPrefix: Int
        :param SubnetId: VPC环境下的子网ID，绑定到主网卡
        :type PathPrefix: String
        :param InstancePassword: 实例开机密码
        :type PathPrefix: String
        :param ChargeType: 计费类型，调用时需要明确指定，无默认值
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，单位月
        :type PathPrefix: Int
        :param SecurityGroupId: 实例绑定的安全组，目前仅支持绑定一个安全组
        :type PathPrefix: String
        :param PrivateIpAddress: 私有IP地址，指定子网IP地址范围内的任意有效值，代表实例的主IP地址，只能选择一个，绑定到主网卡；如果未指定该参数，系统自动从有效地址池中随机选取一个
        :type PathPrefix: String
        :param InstanceName: 实例名称，如果未指定，则自动生成，形如`KSC-IN-[A-Z0-9]{10}`
        :type PathPrefix: String
        :param InstanceNameSuffix: 实例名称后缀，InstanceName参数如果缺省，此参数不生效；当大于1台的批量创建主机，后缀编号自动+1，例如后缀输入5，主机名输入"host"，批量3台，则生成的三台主机名分别为："host-5"、"host-6"、"host-7"；
        :type PathPrefix: String
        :param ProjectId: 实例所属项目ID
        :type PathPrefix: Int
        :param DataDisk: 数据盘是否随实例释放
        :type PathPrefix: Filter
        :param NetworkInterface: 辅网卡
        :type PathPrefix: Filter
        :param UserData: 用户自定义数据
        :type PathPrefix: String
        :param SystemDisk.DiskType: 系统盘类型
        :type PathPrefix: String
        :param SystemDisk.DiskSize: 系统盘大小
        :type PathPrefix: Int
        :param ModelId: 实例启动模版ID，如填写了此项，则启动模板中已包含的RunInstances其他参数不生效，启动模板未指定的参数若调用RunInstances时额外传入则可生效，如果批量创建，实例名称后缀依然存在。【传modelId，使用默认版本。传modelId和modelVersion，使用传递的版本】
示例值：3f0d6229-ed2d-4c9c-8554-b9433517cf8b
        :type PathPrefix: String
        :param ModelVersion: 实例启动模板版本号。如不指定，则采用默认版本号
        :type PathPrefix: Int
        :param AssembledImageDataDiskType: 整机镜像所开云盘数据盘的类型
        :type PathPrefix: String
        :param AutoCreateEbs: 整机镜像是否展开镜像中的数据盘
        :type PathPrefix: Boolean
        :param LineId: 弹性IP的链路类型的ID 
        :type PathPrefix: String
        :param AddressBandWidth: 弹性IP的带宽，1，如果购买EIP，AddressBandWidth、LineId、AddressChargeType三个接口参数必须同时存在，如有其中任意一个接口参数，判断是否存在其他两个参数；2，如果选择预付费计费方式，必须有购买时长参数； |
        :type PathPrefix: Int
        :param AddressChargeType: PrePaidByMonth ：包年包月，有到期时间，只能升带宽；PostPaidByPeak：按峰值月结，无到期时间，可升降带宽；PostPaidByDay：按日月结，无到期时间，可升降带宽；PostPaidByTransfer：按流量月结，无到期时间，可升降带宽；PostPaidByHour：按小时月结，无到期时间，可升降带宽
        :type PathPrefix: String
        :param AddressProjectId: 弹性IP项目的ID,默认值为0
        :type PathPrefix: String
        :param AddressPurchaseTime: 购买时长
        :type PathPrefix: Int
        :param KeyId: 秘钥ID
        :type PathPrefix: Filter
        :param keepImageLogin: 是否保持镜像登录
        :type PathPrefix: Boolean
        :param HostName: 操作系统内部的计算机名
        :type PathPrefix: String
        :param HostNameSuffix: 创建多台实例时为HostName增加有序后缀，有序后缀从1增加，例如host-1
        :type PathPrefix: Int
        :param Password: 开机密码
        :type PathPrefix: String
        :param FailureAutoDelete: 开机失败是否对外删除 ，默认值是false
        :type PathPrefix: Boolean
        """
        self.ImageId = None
        self.DedicatedHostId = None
        self.InstanceConfigure.VCPU = None
        self.InstanceConfigure.MemoryGb = None
        self.InstanceType = None
        self.DataDiskGb = None
        self.MaxCount = None
        self.MinCount = None
        self.SubnetId = None
        self.InstancePassword = None
        self.ChargeType = None
        self.PurchaseTime = None
        self.SecurityGroupId = None
        self.PrivateIpAddress = None
        self.InstanceName = None
        self.InstanceNameSuffix = None
        self.ProjectId = None
        self.DataDisk = None
        self.NetworkInterface = None
        self.UserData = None
        self.SystemDisk.DiskType = None
        self.SystemDisk.DiskSize = None
        self.ModelId = None
        self.ModelVersion = None
        self.AssembledImageDataDiskType = None
        self.AutoCreateEbs = None
        self.LineId = None
        self.AddressBandWidth = None
        self.AddressChargeType = None
        self.AddressProjectId = None
        self.AddressPurchaseTime = None
        self.KeyId = None
        self.keepImageLogin = None
        self.HostName = None
        self.HostNameSuffix = None
        self.Password = None
        self.FailureAutoDelete = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("DedicatedHostId"):
            self.DedicatedHostId = params.get("DedicatedHostId")
        if params.get("InstanceConfigure.VCPU"):
            self.InstanceConfigure.VCPU = params.get("InstanceConfigure.VCPU")
        if params.get("InstanceConfigure.MemoryGb"):
            self.InstanceConfigure.MemoryGb = params.get("InstanceConfigure.MemoryGb")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("DataDiskGb"):
            self.DataDiskGb = params.get("DataDiskGb")
        if params.get("MaxCount"):
            self.MaxCount = params.get("MaxCount")
        if params.get("MinCount"):
            self.MinCount = params.get("MinCount")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstanceNameSuffix"):
            self.InstanceNameSuffix = params.get("InstanceNameSuffix")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("DataDisk"):
            self.DataDisk = params.get("DataDisk")
        if params.get("NetworkInterface"):
            self.NetworkInterface = params.get("NetworkInterface")
        if params.get("UserData"):
            self.UserData = params.get("UserData")
        if params.get("SystemDisk.DiskType"):
            self.SystemDisk.DiskType = params.get("SystemDisk.DiskType")
        if params.get("SystemDisk.DiskSize"):
            self.SystemDisk.DiskSize = params.get("SystemDisk.DiskSize")
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("ModelVersion"):
            self.ModelVersion = params.get("ModelVersion")
        if params.get("AssembledImageDataDiskType"):
            self.AssembledImageDataDiskType = params.get("AssembledImageDataDiskType")
        if params.get("AutoCreateEbs"):
            self.AutoCreateEbs = params.get("AutoCreateEbs")
        if params.get("LineId"):
            self.LineId = params.get("LineId")
        if params.get("AddressBandWidth"):
            self.AddressBandWidth = params.get("AddressBandWidth")
        if params.get("AddressChargeType"):
            self.AddressChargeType = params.get("AddressChargeType")
        if params.get("AddressProjectId"):
            self.AddressProjectId = params.get("AddressProjectId")
        if params.get("AddressPurchaseTime"):
            self.AddressPurchaseTime = params.get("AddressPurchaseTime")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("keepImageLogin"):
            self.keepImageLogin = params.get("keepImageLogin")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("HostNameSuffix"):
            self.HostNameSuffix = params.get("HostNameSuffix")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("FailureAutoDelete"):
            self.FailureAutoDelete = params.get("FailureAutoDelete")


class StartInstancesRequest(AbstractModel):
    """StartInstances请求参数结构体
    """

    def __init__(self):
        r"""启动实例
        :param InstanceId: 待启动实例ID列表，N的范围为1-100
        :type PathPrefix: Filter
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class StopInstancesRequest(AbstractModel):
    """StopInstances请求参数结构体
    """

    def __init__(self):
        r"""关闭实例
        :param InstanceId: 待关闭实例ID列表，N的范围为1-100

        :type PathPrefix: Filter
        :param ForceStop: 强制关闭
        :type PathPrefix: Boolean
        :param StoppedMode: 关闭模式
 KeepCharging （默认参数）  保留并收费<br>StopCharging    关机不收费
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ForceStop = None
        self.StoppedMode = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ForceStop"):
            self.ForceStop = params.get("ForceStop")
        if params.get("StoppedMode"):
            self.StoppedMode = params.get("StoppedMode")


class RebootInstancesRequest(AbstractModel):
    """RebootInstances请求参数结构体
    """

    def __init__(self):
        r"""重启实例
        :param InstanceId: 待重启实例ID列表，N的范围为1-100
        :type PathPrefix: Filter
        :param ForceReboot: 强制重启
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.ForceReboot = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ForceReboot"):
            self.ForceReboot = params.get("ForceReboot")


class ModifyInstanceAttributeRequest(AbstractModel):
    """ModifyInstanceAttribute请求参数结构体
    """

    def __init__(self):
        r"""修改实例属性信息
        :param InstanceId: 待修改属性的实例ID
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param InstanceName: 实例名称，修改实例名称不需要关闭实例。
最短2字符，最长64字符，支持中英文
        :type PathPrefix: String
        :param InstancePassword: 实例开机密码
最短8字符，最长32字符，必须包含大小写英文字符和数字，支持其他可见字符
        :type PathPrefix: String
        :param HostName: 操作系统内部的计算机名
字符长度为[2, 64]，不支持点号（.），每段允许字母（不限制大小写）、数字和短横线（-）组成
        :type PathPrefix: String
        :param RestartMode: 重启模式描述,注:若已选择请求参数InstancePassword，则RestartMode不可缺省
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstancePassword = None
        self.HostName = None
        self.RestartMode = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")
        if params.get("HostName"):
            self.HostName = params.get("HostName")
        if params.get("RestartMode"):
            self.RestartMode = params.get("RestartMode")


class ModifyInstanceTypeRequest(AbstractModel):
    """ModifyInstanceType请求参数结构体
    """

    def __init__(self):
        r"""升级实例套餐类型
        :param InstanceId: 待调整配置的实例ID

        :type PathPrefix: String
        :param InstanceType: 实例目标套餐规格
[实例套餐类型有效值](https://docs.ksyun.com/documents/40858) <br>若对应实例为专属虚机，该值需填写DVM1.NONE(专属型)、DVM2.NONE(专属型2.0)、DVM3.NONE（专属型3.0），专属虚机只支持升降配，不支持变更实例类型。<br>具体套餐信息参考[实例套餐类型定义](https://docs.ksyun.com/documents/705)
        :type PathPrefix: String
        :param InstanceConfigure.VCPU: 目标CPU值；当需变更实例为专属虚机时需填写该值

        :type PathPrefix: String
        :param InstanceConfigure.MemoryGb: 目标内存值
        :type PathPrefix: String
        :param DataDiskGb: 数据卷容量，单位GB，数据卷只能扩容或者保持不变，且不能低于[实例套餐类型定义](https://docs.ksyun.com/documents/705)的最小值。

        :type PathPrefix: Int
        :param CrossInstanceMigrate: 当前操作是否为变更实例套餐类型，若当前操作变更实例类型必须指定为true。（变更过程中必须保持云服务器关机状态；变更完成后启动云服务器生效；涉及本地盘类型的机型变更需加白名单）
true/false
        :type PathPrefix: Boolean
        :param SystemDisk.DiskType: 不能给默认值，不传默认按价格体系配置systemDisk属性中第一个创建
        :type PathPrefix: String
        :param DataDisk: 目标套餐数据盘类型（当本地盘机型变更为云盘机型时才需填写此参数，此参数仅对源本地数据盘生效）

        :type PathPrefix: Filter
        :param StopInstance: 是否对运行中的实例选择关机：是-true，否-false(默认)
        :type PathPrefix: Boolean
        :param AutoRestart: 变更实例类型后是否自动重启: 是-true，否-false(默认)
        :type PathPrefix: Boolean
        :param SystemDisk.DiskSize: 系统盘大小，最大值500，最小值0
        :type PathPrefix: Int
        :param SystemDisk.ResizeType: 扩容 offline 离线扩容| online 在线扩容
        :type PathPrefix: String
        :param InstantAccess: 	
支持快速开盘/快速变更，该参数仅对本地盘/本地盘机型/本地盘快照生效
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.InstanceType = None
        self.InstanceConfigure.VCPU = None
        self.InstanceConfigure.MemoryGb = None
        self.DataDiskGb = None
        self.CrossInstanceMigrate = None
        self.SystemDisk.DiskType = None
        self.DataDisk = None
        self.StopInstance = None
        self.AutoRestart = None
        self.SystemDisk.DiskSize = None
        self.SystemDisk.ResizeType = None
        self.InstantAccess = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("InstanceConfigure.VCPU"):
            self.InstanceConfigure.VCPU = params.get("InstanceConfigure.VCPU")
        if params.get("InstanceConfigure.MemoryGb"):
            self.InstanceConfigure.MemoryGb = params.get("InstanceConfigure.MemoryGb")
        if params.get("DataDiskGb"):
            self.DataDiskGb = params.get("DataDiskGb")
        if params.get("CrossInstanceMigrate"):
            self.CrossInstanceMigrate = params.get("CrossInstanceMigrate")
        if params.get("SystemDisk.DiskType"):
            self.SystemDisk.DiskType = params.get("SystemDisk.DiskType")
        if params.get("DataDisk"):
            self.DataDisk = params.get("DataDisk")
        if params.get("StopInstance"):
            self.StopInstance = params.get("StopInstance")
        if params.get("AutoRestart"):
            self.AutoRestart = params.get("AutoRestart")
        if params.get("SystemDisk.DiskSize"):
            self.SystemDisk.DiskSize = params.get("SystemDisk.DiskSize")
        if params.get("SystemDisk.ResizeType"):
            self.SystemDisk.ResizeType = params.get("SystemDisk.ResizeType")
        if params.get("InstantAccess"):
            self.InstantAccess = params.get("InstantAccess")


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances请求参数结构体
    """

    def __init__(self):
        r"""销毁实例
        :param InstanceId: 待销毁实例ID列表，N的范围为1-100
        :type PathPrefix: Filter
        :param ForceDelete: 强制销毁
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.ForceDelete = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ForceDelete"):
            self.ForceDelete = params.get("ForceDelete")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体
    """

    def __init__(self):
        r"""描述镜像信息
        :param ImageId: 镜像ID。
b1e3731b-c200-4499-be42-f6bfbbda990e。
        :type PathPrefix: String
        :param ImageType: 镜像分类。
system
        :type PathPrefix: String
        """
        self.ImageId = None
        self.ImageType = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("ImageType"):
            self.ImageType = params.get("ImageType")


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute请求参数结构体
    """

    def __init__(self):
        r"""修改镜像属性信息
        :param ImageId: 待修改属性的镜像ID。
16f55e1d-8ab3-4026-ba4d-5ae9e6f083db
        :type PathPrefix: String
        :param Name: 新镜像的名称。
2-64个字符，支持中文、字母、数字以及-_@#.字符
        :type PathPrefix: String
        :param OsVersion: 版本名称
        :type PathPrefix: String
        :param CloudInitSupport: 客户自行安装cloudinit后，需要将该值修改为true，本接口取值：true,false
        :type PathPrefix: Boolean
        """
        self.ImageId = None
        self.Name = None
        self.OsVersion = None
        self.CloudInitSupport = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("OsVersion"):
            self.OsVersion = params.get("OsVersion")
        if params.get("CloudInitSupport"):
            self.CloudInitSupport = params.get("CloudInitSupport")


class ModifyInstanceImageRequest(AbstractModel):
    """ModifyInstanceImage请求参数结构体
    """

    def __init__(self):
        r"""更换或者重新安装实例操作系统
        :param InstanceId: 待更换或者重新安装操作系统的实例ID
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param ImageId: 待更换的镜像ID；如果缺省，表明无需改变镜像，只需重新安装实例的操作系统。
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param SystemDisk.DiskSize: 云主机系统盘配置参数。若不指定该参数，则按照系统默认值进行分配。通用型N2、N3主机支持更换操作系统时指定系统盘大小。
[SystemDisk](https://docs.ksyun.com/documents/5866)
        :type PathPrefix: Int
        :param InstancePassword: 实例开机密码
最短8字符，最长32字符，必须包含大小写英文字符和数字，支持其他可见字符
        :type PathPrefix: String
        :param KeyId: 密钥ID
        :type PathPrefix: Filter
        :param KeepImageLogin: 保留镜像设置登录。该参数只对使用自定义镜像有效。当该值填写为true，默认InstancePassword参数无效。该参数与InstancePassword必须填写一个。
true/false,默认false
        :type PathPrefix: Boolean
        :param SystemDisk.DiskType: 不能给默认值，不传默认按价格体系配置systemDisk属性中第一个创建
        :type PathPrefix: String
        :param SystemDisk.ResizeType: 扩容 offline 离线扩容| online 在线扩容
        :type PathPrefix: String
        :param UserData: 用户自定义数据，必须是base64编码
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.ImageId = None
        self.SystemDisk.DiskSize = None
        self.InstancePassword = None
        self.KeyId = None
        self.KeepImageLogin = None
        self.SystemDisk.DiskType = None
        self.SystemDisk.ResizeType = None
        self.UserData = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("SystemDisk.DiskSize"):
            self.SystemDisk.DiskSize = params.get("SystemDisk.DiskSize")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("KeepImageLogin"):
            self.KeepImageLogin = params.get("KeepImageLogin")
        if params.get("SystemDisk.DiskType"):
            self.SystemDisk.DiskType = params.get("SystemDisk.DiskType")
        if params.get("SystemDisk.ResizeType"):
            self.SystemDisk.ResizeType = params.get("SystemDisk.ResizeType")
        if params.get("UserData"):
            self.UserData = params.get("UserData")


class CreateImageRequest(AbstractModel):
    """CreateImage请求参数结构体
    """

    def __init__(self):
        r"""创建镜像
        :param InstanceId: 待创建镜像的实例ID。
标准UUID格式，形如^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type PathPrefix: String
        :param Name: 新镜像的名称。
2-64个字符，支持中文、字母、数字以及-_@#.字符
        :type PathPrefix: String
        :param Type: 自定义镜像类型，分为本地镜像和普通镜像。
LocalImage 和 CommonImage
        :type PathPrefix: String
        :param DataDiskIds: 实例需要制作镜像的数据盘ID。
标准UUID格式，形如[1]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type PathPrefix: Filter
        :param SnapshotIds: 实例需要制作镜像的快照ID，里面必须包含一个系统盘快照ID。
标准UUID格式，形如[2]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type PathPrefix: Filter
        :param InstantAccess: 支持快速开盘/快速变更，该参数仅对本地盘/本地盘机型/本地盘快照生效
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.Name = None
        self.Type = None
        self.DataDiskIds = None
        self.SnapshotIds = None
        self.InstantAccess = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("DataDiskIds"):
            self.DataDiskIds = params.get("DataDiskIds")
        if params.get("SnapshotIds"):
            self.SnapshotIds = params.get("SnapshotIds")
        if params.get("InstantAccess"):
            self.InstantAccess = params.get("InstantAccess")


class RemoveImagesRequest(AbstractModel):
    """RemoveImages请求参数结构体
    """

    def __init__(self):
        r"""删除镜像
        :param ImageId: 待删除的镜像ID。
标准UUID格式，形如^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type PathPrefix: String
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
    """ModifyNetworkInterfaceAttribute请求参数结构体
    """

    def __init__(self):
        r"""修改网络接口
        :param InstanceId: 待修改属性的实例ID
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param NetworkInterfaceId: 待修改属性的网络接口ID
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param SubnetId: 新的子网ID
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param SecurityGroupId: 实例绑定的安全组，SecurityGroupId.N可以绑定多个安全组。已绑定的安全组，未重新指定时会被删除。
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param PrivateIpAddress: 私有IP地址，子网IP地址范围内的任意有效值。
标准IP地址格式
        :type PathPrefix: String
        :param DNS1: DNS 1的值，当通过该接口进行修改网络配置时不填写此参数，保持与之前不变。
标准IP地址格式
        :type PathPrefix: String
        :param DNS2: DNS 2的值，当通过该接口进行修改网络配置时不填写此参数，保持与之前不变。
标准IP地址格式
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.SubnetId = None
        self.SecurityGroupId = None
        self.PrivateIpAddress = None
        self.DNS1 = None
        self.DNS2 = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("DNS1"):
            self.DNS1 = params.get("DNS1")
        if params.get("DNS2"):
            self.DNS2 = params.get("DNS2")


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface请求参数结构体
    """

    def __init__(self):
        r"""实例添加弹性网卡
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param NetworkInterfaceId: 弹性网卡ID（保留已经上线的参数，该参数与已经上线参数不可同时指定）
        :type PathPrefix: String
        :param SubnetId: 
        :type PathPrefix: String
        :param SecurityGroupId: 安全组id
        :type PathPrefix: String
        :param PrivateIpAddress: 
        :type PathPrefix: String
        :param SecurityGroupIds: 
        :type PathPrefix: Array
        :param VpcIpv6: 指定子网下的ipv6地址
        :type PathPrefix: String
        :param MacAddress: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.SubnetId = None
        self.SecurityGroupId = None
        self.PrivateIpAddress = None
        self.SecurityGroupIds = None
        self.VpcIpv6 = None
        self.MacAddress = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("VpcIpv6"):
            self.VpcIpv6 = params.get("VpcIpv6")
        if params.get("MacAddress"):
            self.MacAddress = params.get("MacAddress")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface请求参数结构体
    """

    def __init__(self):
        r"""实例卸载弹性网卡
        :param InstanceId: 实例ID
        :type PathPrefix: String
        :param NetworkInterfaceId: 弹性网卡ID
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.NetworkInterfaceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("NetworkInterfaceId"):
            self.NetworkInterfaceId = params.get("NetworkInterfaceId")


class DescribeLocalVolumesRequest(AbstractModel):
    """DescribeLocalVolumes请求参数结构体
    """

    def __init__(self):
        r"""查询本地盘信息
        :param InstanceName: 实例名字
        :type PathPrefix: String
        :param Marker: 页数
        :type PathPrefix: Int
        :param MaxResults: 每页最大条数
        :type PathPrefix: Int
        :param LocalVolumeId: 本地盘id
        :type PathPrefix: String
        :param InstanceState: 主机状态
        :type PathPrefix: String
        :param LocalVolumeCategory: root/data 磁盘的类型：　系统盘／　数据盘
        :type PathPrefix: String
        :param LocalVolumeSize: 查询大于等于多少G的磁盘
        :type PathPrefix: Int
        :param BindSnapshotPolicy: 硬盘是否绑定了备份策略
        :type PathPrefix: Boolean
        :param AutoSnapshotPolicyId: 策略ID
        :type PathPrefix: String
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceName = None
        self.Marker = None
        self.MaxResults = None
        self.LocalVolumeId = None
        self.InstanceState = None
        self.LocalVolumeCategory = None
        self.LocalVolumeSize = None
        self.BindSnapshotPolicy = None
        self.AutoSnapshotPolicyId = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("LocalVolumeId"):
            self.LocalVolumeId = params.get("LocalVolumeId")
        if params.get("InstanceState"):
            self.InstanceState = params.get("InstanceState")
        if params.get("LocalVolumeCategory"):
            self.LocalVolumeCategory = params.get("LocalVolumeCategory")
        if params.get("LocalVolumeSize"):
            self.LocalVolumeSize = params.get("LocalVolumeSize")
        if params.get("BindSnapshotPolicy"):
            self.BindSnapshotPolicy = params.get("BindSnapshotPolicy")
        if params.get("AutoSnapshotPolicyId"):
            self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateLocalVolumeSnapshotRequest(AbstractModel):
    """CreateLocalVolumeSnapshot请求参数结构体
    """

    def __init__(self):
        r"""创建本地盘快照
        :param LocalVolumeId: 待创建快照的本地盘ID。
        :type PathPrefix: String
        :param LocalVolumeSnapshotName: 快照名称。
        :type PathPrefix: String
        :param LocalVolumeSnapshotDesc: 快照详情描述。
        :type PathPrefix: String
        :param InstantAccess: 支持快速开盘/快速变更，该参数仅对本地盘/本地盘机型/本地盘快照生效
        :type PathPrefix: Boolean
        """
        self.LocalVolumeId = None
        self.LocalVolumeSnapshotName = None
        self.LocalVolumeSnapshotDesc = None
        self.InstantAccess = None

    def _deserialize(self, params):
        if params.get("LocalVolumeId"):
            self.LocalVolumeId = params.get("LocalVolumeId")
        if params.get("LocalVolumeSnapshotName"):
            self.LocalVolumeSnapshotName = params.get("LocalVolumeSnapshotName")
        if params.get("LocalVolumeSnapshotDesc"):
            self.LocalVolumeSnapshotDesc = params.get("LocalVolumeSnapshotDesc")
        if params.get("InstantAccess"):
            self.InstantAccess = params.get("InstantAccess")


class DescribeLocalVolumeSnapshotsRequest(AbstractModel):
    """DescribeLocalVolumeSnapshots请求参数结构体
    """

    def __init__(self):
        r"""描述本地盘快照信息
        :param Action: Action
        :type PathPrefix: String
        :param Version: Version
        :type PathPrefix: String
        :param LocalVolumeName: 本地硬盘名称。

        :type PathPrefix: String
        :param SourceLocalVolumeId: 本地硬盘快照ID。

        :type PathPrefix: String
        """
        self.Action = None
        self.Version = None
        self.LocalVolumeName = None
        self.SourceLocalVolumeId = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")
        if params.get("LocalVolumeName"):
            self.LocalVolumeName = params.get("LocalVolumeName")
        if params.get("SourceLocalVolumeId"):
            self.SourceLocalVolumeId = params.get("SourceLocalVolumeId")


class RollbackLocalVolumeRequest(AbstractModel):
    """RollbackLocalVolume请求参数结构体
    """

    def __init__(self):
        r"""快照回滚本地盘
        :param LocalVolumeSnapshotId: 快照Id。
        :type PathPrefix: String
        """
        self.LocalVolumeSnapshotId = None

    def _deserialize(self, params):
        if params.get("LocalVolumeSnapshotId"):
            self.LocalVolumeSnapshotId = params.get("LocalVolumeSnapshotId")


class DeleteLocalVolumeSnapshotRequest(AbstractModel):
    """DeleteLocalVolumeSnapshot请求参数结构体
    """

    def __init__(self):
        r"""删除本地盘快照
        :param LocalVolumeSnapshotId: 快照Id，支持批量删除，格式为LocalVolumeSnapshotId.N=XXX，N=1,2,3…100。
        :type PathPrefix: Filter
        """
        self.LocalVolumeSnapshotId = None

    def _deserialize(self, params):
        if params.get("LocalVolumeSnapshotId"):
            self.LocalVolumeSnapshotId = params.get("LocalVolumeSnapshotId")


class ModifyDataGuardGroupsRequest(AbstractModel):
    """ModifyDataGuardGroups请求参数结构体
    """

    def __init__(self):
        r"""修改容灾分组信息
        :param DataGuardId: 待修改的容灾分组ID

        :type PathPrefix: String
        :param DataGuardName: 容灾分组名称

        :type PathPrefix: String
        """
        self.DataGuardId = None
        self.DataGuardName = None

    def _deserialize(self, params):
        if params.get("DataGuardId"):
            self.DataGuardId = params.get("DataGuardId")
        if params.get("DataGuardName"):
            self.DataGuardName = params.get("DataGuardName")


class DescribeDataGuardCapacityRequest(AbstractModel):
    """DescribeDataGuardCapacity请求参数结构体
    """

    def __init__(self):
        r"""查询用户区域容灾分组容量
        """

    def _deserialize(self, params):
        return


class CreateDataGuardGroupRequest(AbstractModel):
    """CreateDataGuardGroup请求参数结构体
    """

    def __init__(self):
        r"""创建容灾分组
        :param DataGuardName: 容灾分组名称
        :type PathPrefix: String
        """
        self.DataGuardName = None

    def _deserialize(self, params):
        if params.get("DataGuardName"):
            self.DataGuardName = params.get("DataGuardName")


class DeleteDataGuardGroupsRequest(AbstractModel):
    """DeleteDataGuardGroups请求参数结构体
    """

    def __init__(self):
        r"""删除容灾分组
        :param DataGuardId: 待删除的容灾分组ID
        :type PathPrefix: Filter
        """
        self.DataGuardId = None

    def _deserialize(self, params):
        if params.get("DataGuardId"):
            self.DataGuardId = params.get("DataGuardId")


class DescribeDataGuardGroupRequest(AbstractModel):
    """DescribeDataGuardGroup请求参数结构体
    """

    def __init__(self):
        r"""描述容灾分组信息
        :param DataGuardId: 待查询的容灾分组ID
        :type PathPrefix: String
        :param DataGuardName: 容灾分组名称
        :type PathPrefix: String
        """
        self.DataGuardId = None
        self.DataGuardName = None

    def _deserialize(self, params):
        if params.get("DataGuardId"):
            self.DataGuardId = params.get("DataGuardId")
        if params.get("DataGuardName"):
            self.DataGuardName = params.get("DataGuardName")


class RemoveVmFromDataGuardRequest(AbstractModel):
    """RemoveVmFromDataGuard请求参数结构体
    """

    def __init__(self):
        r"""容灾分组中移除实例
        :param DataGuardId: 待修改的容灾分组ID
        :type PathPrefix: String
        :param InstanceId: 待移除的实例ID
        :type PathPrefix: Filter
        """
        self.DataGuardId = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("DataGuardId"):
            self.DataGuardId = params.get("DataGuardId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateDedicatedHostsRequest(AbstractModel):
    """CreateDedicatedHosts请求参数结构体
    """

    def __init__(self):
        r"""创建专属宿主机
        :param DedicatedType: 物理机类型
        :type PathPrefix: String
        :param Number: 购买数量
        :type PathPrefix: Int
        :param Name: 物理机名称（如果未指定，则自动生成）
        :type PathPrefix: String
        :param ChargeType: 购买方式
        :type PathPrefix: String
        :param PurchaseTime: 购买时长
        :type PathPrefix: Int
        :param InstanceNameSuffix: 物理机名称后缀（购买多台物理机时使用）
        :type PathPrefix: String
        :param DedicatedClusterId: 
        :type PathPrefix: String
        :param Tag: 创建的专属宿主机的标签键，N取值范围1~10。若填写了Tag.N.Value，Tag.N.Key为必填，且两个参数的N值需保持一致
        :type PathPrefix: Filter
        """
        self.DedicatedType = None
        self.Number = None
        self.Name = None
        self.ChargeType = None
        self.PurchaseTime = None
        self.InstanceNameSuffix = None
        self.DedicatedClusterId = None
        self.Tag = None

    def _deserialize(self, params):
        if params.get("DedicatedType"):
            self.DedicatedType = params.get("DedicatedType")
        if params.get("Number"):
            self.Number = params.get("Number")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("InstanceNameSuffix"):
            self.InstanceNameSuffix = params.get("InstanceNameSuffix")
        if params.get("DedicatedClusterId"):
            self.DedicatedClusterId = params.get("DedicatedClusterId")
        if params.get("Tag"):
            self.Tag = params.get("Tag")


class DeleteDedicatedHostRequest(AbstractModel):
    """DeleteDedicatedHost请求参数结构体
    """

    def __init__(self):
        r"""删除专属宿主机
        :param DedicatedHostId: 专属宿主机id
        :type PathPrefix: Filter
        :param IsRefund: 是否退订(默认true）
        :type PathPrefix: Boolean
        """
        self.DedicatedHostId = None
        self.IsRefund = None

    def _deserialize(self, params):
        if params.get("DedicatedHostId"):
            self.DedicatedHostId = params.get("DedicatedHostId")
        if params.get("IsRefund"):
            self.IsRefund = params.get("IsRefund")


class DescribeDedicatedHostsRequest(AbstractModel):
    """DescribeDedicatedHosts请求参数结构体
    """

    def __init__(self):
        r"""描述专属宿主机信息
        :param DedicatedHostId: 专属宿主机id
        :type PathPrefix: String
        :param search: 查询条件（宿主机id或者名称）
        :type PathPrefix: String
        :param ProjectId: 项目制id列表
        :type PathPrefix: Filter
        """
        self.DedicatedHostId = None
        self.search = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("DedicatedHostId"):
            self.DedicatedHostId = params.get("DedicatedHostId")
        if params.get("search"):
            self.search = params.get("search")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribeScalingConfigurationRequest(AbstractModel):
    """DescribeScalingConfiguration请求参数结构体
    """

    def __init__(self):
        r"""查询启动配置
        :param ScalingConfigurationName: 启动配置名称 
 
        :type PathPrefix: String
        :param ScalingConfigurationId: 待查询的各启动配置ID构成的数组数组下标从0开始，最多可指定20个 
 
        :type PathPrefix: Filter
        :param Marker: 偏移量，默认为0偏移量，默认为0 
 
        :type PathPrefix: Int
        :param ProjectId: 项目组id 
 
        :type PathPrefix: Filter
        :param MaxResults: 一次最多可查询的启动配置数量 
 默认为10，最小为5
        :type PathPrefix: Int
        """
        self.ScalingConfigurationName = None
        self.ScalingConfigurationId = None
        self.Marker = None
        self.ProjectId = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ScalingConfigurationName"):
            self.ScalingConfigurationName = params.get("ScalingConfigurationName")
        if params.get("ScalingConfigurationId"):
            self.ScalingConfigurationId = params.get("ScalingConfigurationId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class CreateScalingConfigurationRequest(AbstractModel):
    """CreateScalingConfiguration请求参数结构体
    """

    def __init__(self):
        r"""创建启动配置
        :param ScalingConfigurationName: 启动配置名称 
 
        :type PathPrefix: String
        :param ImageId: 镜像ID 
 
        :type PathPrefix: String
        :param Password: 实例密码 
 
        :type PathPrefix: String
        :param InstanceType: 选择一个云主机类型 
 
        :type PathPrefix: String
        :param ChargeType: 选择云主机计费方式 
 
        :type PathPrefix: String
        :param DataDiskGb: 本地数据盘容量 
 
        :type PathPrefix: Int
        :param ProjectId: 项目制id，默认0 
 
        :type PathPrefix: Int
        :param KeepImageLogin: 保留镜像设置 
 
        :type PathPrefix: Boolean
        :param KeyId: 密钥对 
 
        :type PathPrefix: Filter
        :param DataDisk: 云盘数据盘类型 
 
        :type PathPrefix: Filter
        :param SystemDisk.DiskSize: 系统盘大小，最小值为0，最大值为500
        :type PathPrefix: String
        :param AddressBandWidth: 弹性IP的带宽 
 
        :type PathPrefix: Int
        :param BandWidthShareId: 弹性IP指定的共享带宽ID 
 
        :type PathPrefix: String
        :param LineId: 弹性IP的链路类型的ID 
 
        :type PathPrefix: String
        :param AddressProjectId: 弹性IP项目的ID 
 
        :type PathPrefix: Int
        :param InstanceName: 实例名称 
 
        :type PathPrefix: String
        :param InstanceNameSuffix: 实例名称后缀 
 
        :type PathPrefix: String
        :param UserData:  用户自定义数据 
 
        :type PathPrefix: String
        :param InstanceNameTimeSuffix:  实例名称时间戳后缀，true/false 
 
        :type PathPrefix: Boolean
        :param Tag:  启动配置创建的ECS实例的标签键 
 支持1-128个字符，仅支持中英文字符、数字及±=._/@:
        :type PathPrefix: Filter
        :param SystemDisk.DiskType: 不能给默认值，不传默认按价格体系配置systemDisk属性中第一个创建
        :type PathPrefix: String
        :param SystemDisk.ResizeType: 扩容 offline 离线扩容| online 在线扩容
        :type PathPrefix: String
        """
        self.ScalingConfigurationName = None
        self.ImageId = None
        self.Password = None
        self.InstanceType = None
        self.ChargeType = None
        self.DataDiskGb = None
        self.ProjectId = None
        self.KeepImageLogin = None
        self.KeyId = None
        self.DataDisk = None
        self.SystemDisk.DiskSize = None
        self.AddressBandWidth = None
        self.BandWidthShareId = None
        self.LineId = None
        self.AddressProjectId = None
        self.InstanceName = None
        self.InstanceNameSuffix = None
        self.UserData = None
        self.InstanceNameTimeSuffix = None
        self.Tag = None
        self.SystemDisk.DiskType = None
        self.SystemDisk.ResizeType = None

    def _deserialize(self, params):
        if params.get("ScalingConfigurationName"):
            self.ScalingConfigurationName = params.get("ScalingConfigurationName")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("DataDiskGb"):
            self.DataDiskGb = params.get("DataDiskGb")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("KeepImageLogin"):
            self.KeepImageLogin = params.get("KeepImageLogin")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("DataDisk"):
            self.DataDisk = params.get("DataDisk")
        if params.get("SystemDisk.DiskSize"):
            self.SystemDisk.DiskSize = params.get("SystemDisk.DiskSize")
        if params.get("AddressBandWidth"):
            self.AddressBandWidth = params.get("AddressBandWidth")
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")
        if params.get("LineId"):
            self.LineId = params.get("LineId")
        if params.get("AddressProjectId"):
            self.AddressProjectId = params.get("AddressProjectId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstanceNameSuffix"):
            self.InstanceNameSuffix = params.get("InstanceNameSuffix")
        if params.get("UserData"):
            self.UserData = params.get("UserData")
        if params.get("InstanceNameTimeSuffix"):
            self.InstanceNameTimeSuffix = params.get("InstanceNameTimeSuffix")
        if params.get("Tag"):
            self.Tag = params.get("Tag")
        if params.get("SystemDisk.DiskType"):
            self.SystemDisk.DiskType = params.get("SystemDisk.DiskType")
        if params.get("SystemDisk.ResizeType"):
            self.SystemDisk.ResizeType = params.get("SystemDisk.ResizeType")


class DeleteScalingConfigurationRequest(AbstractModel):
    """DeleteScalingConfiguration请求参数结构体
    """

    def __init__(self):
        r"""删除启动配置
        :param ScalingConfigurationId: 待删除的启动配置ID 
 
        :type PathPrefix: Filter
        """
        self.ScalingConfigurationId = None

    def _deserialize(self, params):
        if params.get("ScalingConfigurationId"):
            self.ScalingConfigurationId = params.get("ScalingConfigurationId")


class CreateScalingGroupRequest(AbstractModel):
    """CreateScalingGroup请求参数结构体
    """

    def __init__(self):
        r"""创建伸缩组接口
        :param ScalingGroupName: 伸缩组名称 
 
        :type PathPrefix: String
        :param ScalingConfigurationId: 待创建伸缩组所要使用的启动配置ID 
 标准UUID格式
        :type PathPrefix: String
        :param MinSize: 最小伸缩数最小伸缩数，即伸缩组内最小云服务器数 
 
        :type PathPrefix: String
        :param DesiredCapacity: 期望实例数期望实例数，即伸缩组刚创建时的云服务器数量 
 0-10,必须在最小伸缩数与最大伸缩数之间
        :type PathPrefix: Int
        :param RemovePolicy: 移除策略 
 有效值：RemoveOldestInstance，表示移除最旧云服务器；RemoveNewestInstance，表示移除最新云服务器
        :type PathPrefix: String
        :param SubnetId: 子网ID 
 
        :type PathPrefix: Filter
        :param SubnetStrategy: 多子网扩展策略当绑定多个子网时，此项必填，有效值：balanced-distribution(均衡分布），choice-first（选择优先）默认值：balanced-distribution 
 
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID 
 
        :type PathPrefix: String
        :param Slb: 与伸缩组绑定的各负载均衡的ID 
 
        :type PathPrefix: Filter
        """
        self.ScalingGroupName = None
        self.ScalingConfigurationId = None
        self.MinSize = None
        self.DesiredCapacity = None
        self.RemovePolicy = None
        self.SubnetId = None
        self.SubnetStrategy = None
        self.SecurityGroupId = None
        self.Slb = None

    def _deserialize(self, params):
        if params.get("ScalingGroupName"):
            self.ScalingGroupName = params.get("ScalingGroupName")
        if params.get("ScalingConfigurationId"):
            self.ScalingConfigurationId = params.get("ScalingConfigurationId")
        if params.get("MinSize"):
            self.MinSize = params.get("MinSize")
        if params.get("DesiredCapacity"):
            self.DesiredCapacity = params.get("DesiredCapacity")
        if params.get("RemovePolicy"):
            self.RemovePolicy = params.get("RemovePolicy")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("SubnetStrategy"):
            self.SubnetStrategy = params.get("SubnetStrategy")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("Slb"):
            self.Slb = params.get("Slb")


class DescribeScalingGroupRequest(AbstractModel):
    """DescribeScalingGroup请求参数结构体
    """

    def __init__(self):
        r"""查询伸缩组列表接口
        :param ScalingGroupId: 待查询的各伸缩组组成的数组数组下标从0开始 
 
        :type PathPrefix: Filter
        :param ScalingGroupName: 待查询的伸缩组名称 
 
        :type PathPrefix: String
        :param ScalingConfigurationId: 待查询的伸缩组所使用的启动配置ID 
 
        :type PathPrefix: String
        :param VpcId: 私有网络ID不传则查询全部网络伸缩组，传0表示基础网络, 如需指定vpc网络 
 
        :type PathPrefix: String
        :param Marker: 分页标识单次调用未返回全部伸缩组时，标记下次调用的返回值的起点，默认值是0 
 
        :type PathPrefix: Int
        :param MaxResults: 一次显示的最多条目数 
 默认为10，最小为5
        :type PathPrefix: Int
        :param ScalingActivityId: 弹性伸缩活动id列表
        :type PathPrefix: Filter
        """
        self.ScalingGroupId = None
        self.ScalingGroupName = None
        self.ScalingConfigurationId = None
        self.VpcId = None
        self.Marker = None
        self.MaxResults = None
        self.ScalingActivityId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingGroupName"):
            self.ScalingGroupName = params.get("ScalingGroupName")
        if params.get("ScalingConfigurationId"):
            self.ScalingConfigurationId = params.get("ScalingConfigurationId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("ScalingActivityId"):
            self.ScalingActivityId = params.get("ScalingActivityId")


class ModifyScalingGroupRequest(AbstractModel):
    """ModifyScalingGroup请求参数结构体
    """

    def __init__(self):
        r"""修改伸缩组接口
        :param ScalingGroupId: 待修改的伸缩组ID 
 
        :type PathPrefix: String
        :param MinSize: 修改后的最小实例数 
 
        :type PathPrefix: Int
        :param MaxSize: 修改后的最大实例数 
 
        :type PathPrefix: Int
        :param DesiredCapacity: 修改后的期望实例数 
 
        :type PathPrefix: Int
        :param RemovePolicy: 伸缩组移除策略 
 RemoveOldestInstance：表示移除最早加入伸缩组的云服务器；RemoveNewestInstance：表示移除最新加入伸缩组的云服务器
        :type PathPrefix: String
        :param ScalingGroupName: 伸缩组名称 
 
        :type PathPrefix: String
        :param ScalingConfigurationId: 与伸缩组绑定的启动配置ID 
 
        :type PathPrefix: String
        :param SubnetId: 子网ID 
 
        :type PathPrefix: Filter
        :param SubnetStrategy: 多子网扩展策略当绑定多个子网时，此项必填，有效值：balanced-distribution(均衡分布），choice-first（选择优先）默认值：balanced-distribution 
 balanced-distribution(均衡分布），choice-first（选择优先）默认值：balanced-distribution
        :type PathPrefix: String
        :param Slb: 与伸缩组绑定的各负载均衡的ID即将废弃 
 
        :type PathPrefix: Filter
        :param ContainerSubnetId: 支持容器业务线指定子网扩容 
 
        :type PathPrefix: Filter
        """
        self.ScalingGroupId = None
        self.MinSize = None
        self.MaxSize = None
        self.DesiredCapacity = None
        self.RemovePolicy = None
        self.ScalingGroupName = None
        self.ScalingConfigurationId = None
        self.SubnetId = None
        self.SubnetStrategy = None
        self.Slb = None
        self.ContainerSubnetId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("MinSize"):
            self.MinSize = params.get("MinSize")
        if params.get("MaxSize"):
            self.MaxSize = params.get("MaxSize")
        if params.get("DesiredCapacity"):
            self.DesiredCapacity = params.get("DesiredCapacity")
        if params.get("RemovePolicy"):
            self.RemovePolicy = params.get("RemovePolicy")
        if params.get("ScalingGroupName"):
            self.ScalingGroupName = params.get("ScalingGroupName")
        if params.get("ScalingConfigurationId"):
            self.ScalingConfigurationId = params.get("ScalingConfigurationId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("SubnetStrategy"):
            self.SubnetStrategy = params.get("SubnetStrategy")
        if params.get("Slb"):
            self.Slb = params.get("Slb")
        if params.get("ContainerSubnetId"):
            self.ContainerSubnetId = params.get("ContainerSubnetId")


class SetKvmProtectedDetachRequest(AbstractModel):
    """SetKvmProtectedDetach请求参数结构体
    """

    def __init__(self):
        r"""设置子机移除保护
        :param ScalingGroupId: 伸缩组ID 
 
        :type PathPrefix: String
        :param ScalingInstanceId: 需设置移除保护的云服务器数组，下标从0开始 
 
        :type PathPrefix: Filter
        :param ProtectedFromDetach: 移除保护标志位 
 1：设置云服务器移除保护；0：取消云服务器移除保护
        :type PathPrefix: Int
        """
        self.ScalingGroupId = None
        self.ScalingInstanceId = None
        self.ProtectedFromDetach = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingInstanceId"):
            self.ScalingInstanceId = params.get("ScalingInstanceId")
        if params.get("ProtectedFromDetach"):
            self.ProtectedFromDetach = params.get("ProtectedFromDetach")


class DescribeScalingInstanceRequest(AbstractModel):
    """DescribeScalingInstance请求参数结构体
    """

    def __init__(self):
        r"""查询伸缩组绑定的云服务器
        :param ScalingGroupId: 伸缩组ID 
 
        :type PathPrefix: String
        :param ScalingInstanceId: 待查询的云服务器ID默认显示与伸缩组绑定的所有云服务器 
 
        :type PathPrefix: Filter
        :param CreationType: 待查询的与伸缩组绑定的云服务器类型 
 Auto：表示伸缩组自动创建生成的实例；Manual：表示用户手动创建的实例
        :type PathPrefix: String
        :param HealthStatus: 待查询的与伸缩组绑定的云服务器健康状态 
 Healthy：表示健康；UnHealthy：表示不健康
        :type PathPrefix: String
        :param Marker: 分页标识单次调用未返回全部伸缩组时，标记下次调用的返回值的起点，默认值是0 
 
        :type PathPrefix: Int
        :param MaxResults: 返回最大条目数范围为5-1000 
 
        :type PathPrefix: Int
        """
        self.ScalingGroupId = None
        self.ScalingInstanceId = None
        self.CreationType = None
        self.HealthStatus = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingInstanceId"):
            self.ScalingInstanceId = params.get("ScalingInstanceId")
        if params.get("CreationType"):
            self.CreationType = params.get("CreationType")
        if params.get("HealthStatus"):
            self.HealthStatus = params.get("HealthStatus")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class AttachInstanceRequest(AbstractModel):
    """AttachInstance请求参数结构体
    """

    def __init__(self):
        r"""绑定伸缩组云服务器
        :param ScalingGroupId: 伸缩组ID 
 
        :type PathPrefix: String
        :param ScalingInstanceId: 待添加的云服务器ID必须与伸缩组处于同一VPC和子网下 
 
        :type PathPrefix: Filter
        """
        self.ScalingGroupId = None
        self.ScalingInstanceId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingInstanceId"):
            self.ScalingInstanceId = params.get("ScalingInstanceId")


class DetachInstanceRequest(AbstractModel):
    """DetachInstance请求参数结构体
    """

    def __init__(self):
        r"""解绑伸缩组云服务器
        :param ScalingGroupId: 伸缩组ID 
 
        :type PathPrefix: String
        :param ScalingInstanceId: 待从伸缩组中移除的云服务器ID 
 
        :type PathPrefix: Filter
        """
        self.ScalingGroupId = None
        self.ScalingInstanceId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingInstanceId"):
            self.ScalingInstanceId = params.get("ScalingInstanceId")


class DescribeScalingActivityRequest(AbstractModel):
    """DescribeScalingActivity请求参数结构体
    """

    def __init__(self):
        r"""查询伸缩活动
        :param ScalingGroupId: 待查询的伸缩组ID 
 
        :type PathPrefix: String
        :param ScalingActivityId: 伸缩活动ID可指定查询某些伸缩活动记录 
 
        :type PathPrefix: Filter
        :param Marker: 分页标识单次调用未返回全部伸缩组时，标记下次调用的返回值的起点，默认值是0 
 
        :type PathPrefix: Int
        :param MaxResults: 返回最大条目数范围为5-1000 
 
        :type PathPrefix: Int
        :param StartTime: 指定开始时间 
 举例：2018-03-15 00:00:00
        :type PathPrefix: String
        :param EndTime: 指定结束时间 
 举例：2018-03-15 00:00:00
        :type PathPrefix: String
        """
        self.ScalingGroupId = None
        self.ScalingActivityId = None
        self.Marker = None
        self.MaxResults = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingActivityId"):
            self.ScalingActivityId = params.get("ScalingActivityId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class DeleteScalingGroupRequest(AbstractModel):
    """DeleteScalingGroup请求参数结构体
    """

    def __init__(self):
        r"""删除伸缩组
        :param ScalingGroupId:  
 
        :type PathPrefix: String
        """
        self.ScalingGroupId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")


class DisableScalingGroupRequest(AbstractModel):
    """DisableScalingGroup请求参数结构体
    """

    def __init__(self):
        r"""停用伸缩组
        :param ScalingGroupId: 需要停用得伸缩组ID 
 
        :type PathPrefix: String
        """
        self.ScalingGroupId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")


class EnableScalingGroupRequest(AbstractModel):
    """EnableScalingGroup请求参数结构体
    """

    def __init__(self):
        r"""启用伸缩组
        :param ScalingGroupId: 待启用的伸缩组ID 
 
        :type PathPrefix: String
        """
        self.ScalingGroupId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")


class DescribeScalingNotificationRequest(AbstractModel):
    """DescribeScalingNotification请求参数结构体
    """

    def __init__(self):
        r"""查询通知
        :param ScalingGroupId: 查询的通知所在的伸缩组ID
        :type PathPrefix: String
        :param ScalingNotificationId: 告警通知id
        :type PathPrefix: Filter
        :param Marker: 
        :type PathPrefix: Int
        :param MaxResults: 一次查询的条数，最小为5，最大为1000
        :type PathPrefix: Int
        """
        self.ScalingGroupId = None
        self.ScalingNotificationId = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingNotificationId"):
            self.ScalingNotificationId = params.get("ScalingNotificationId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class CreateScalingNotificationRequest(AbstractModel):
    """CreateScalingNotification请求参数结构体
    """

    def __init__(self):
        r"""创建通知
        :param ScalingNotificationType: 通知类型，即为需要订阅的通知类型集合，范围从1到6,  具体映射关系如下：<br/>1：扩容成功<br/>2：扩容失败<br/>3：缩容成功<br/>4：缩容失败<br/>5：替换不健康子机成功<br/>6：替换不健康子机失败 
        :type PathPrefix: Filter
        :param ScalingGroupId: 弹性伸缩组id
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        """
        self.ScalingNotificationType = None
        self.ScalingGroupId = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("ScalingNotificationType"):
            self.ScalingNotificationType = params.get("ScalingNotificationType")
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("Description"):
            self.Description = params.get("Description")


class ModifyScalingNotificationRequest(AbstractModel):
    """ModifyScalingNotification请求参数结构体
    """

    def __init__(self):
        r"""修改通知
        :param ScalingGroupId: 要修改的通知所在的伸缩组ID
        :type PathPrefix: String
        :param ScalingNotificationId: 要修改的通知ID，目前仅支持主账号
        :type PathPrefix: Int
        :param NotificationType: 通知类型数组，即为需要订阅的伸缩活动通知集合，范围从1到6。具体映射关系如下：<br/>1：扩容成功<br/>2：扩容失败<br/>3：缩容成功<br/>4：缩容失败<br/>5：替换不健康子机成功<br/>6：替换不健康子机失败
        :type PathPrefix: Filter
        """
        self.ScalingGroupId = None
        self.ScalingNotificationId = None
        self.NotificationType = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingNotificationId"):
            self.ScalingNotificationId = params.get("ScalingNotificationId")
        if params.get("NotificationType"):
            self.NotificationType = params.get("NotificationType")


class CreateScheduledTaskRequest(AbstractModel):
    """CreateScheduledTask请求参数结构体
    """

    def __init__(self):
        r"""创建定时任务
        :param ScalingGroupId: 弹性伸缩组id
        :type PathPrefix: String
        :param ScalingScheduledTaskName: 弹性伸缩定时任务名称
        :type PathPrefix: String
        :param ReadjustMinSize: 定时任务触发时，重设伸缩组中最小伸缩数的值    
        :type PathPrefix: Int
        :param ReadjustMaxSize: 定时任务触发时，重设伸缩组中最大伸缩数的值
        :type PathPrefix: Int
        :param ReadjustExpectSize: 定时任务触发时，重设伸缩组中期望实例数
        :type PathPrefix: Int
        :param StartTime: 定时任务的开始时间
        :type PathPrefix: String
        :param EndTime: 定时任务重复执行时的结束时间，若定时任务需要重复执行，则必填此参数
        :type PathPrefix: String
        :param Recurrence: 定时任务的重复方式，为标准的crontab格式 `* * * * *` ，其中分钟与小时的星号不能指定(第一位与第二位)。若定时任务需要重复执行，则必填此参数
        :type PathPrefix: String
        :param RepeatUnit: 重复执行的单位，日、月、周Day表示日，Month表示月，Week表示周
        :type PathPrefix: String
        :param RepeatCycle: 重复执行的周期，逗号隔开的字符串，如果多个参数'.例如：按天 ["2"] 表示每2天，按月 ["2"，"5"] 表示每月2到5日，按周 ["1","2","3"] 表示周一、二、三
        :type PathPrefix: String
        """
        self.ScalingGroupId = None
        self.ScalingScheduledTaskName = None
        self.ReadjustMinSize = None
        self.ReadjustMaxSize = None
        self.ReadjustExpectSize = None
        self.StartTime = None
        self.EndTime = None
        self.Recurrence = None
        self.RepeatUnit = None
        self.RepeatCycle = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingScheduledTaskName"):
            self.ScalingScheduledTaskName = params.get("ScalingScheduledTaskName")
        if params.get("ReadjustMinSize"):
            self.ReadjustMinSize = params.get("ReadjustMinSize")
        if params.get("ReadjustMaxSize"):
            self.ReadjustMaxSize = params.get("ReadjustMaxSize")
        if params.get("ReadjustExpectSize"):
            self.ReadjustExpectSize = params.get("ReadjustExpectSize")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Recurrence"):
            self.Recurrence = params.get("Recurrence")
        if params.get("RepeatUnit"):
            self.RepeatUnit = params.get("RepeatUnit")
        if params.get("RepeatCycle"):
            self.RepeatCycle = params.get("RepeatCycle")


class DescribeScheduledTaskRequest(AbstractModel):
    """DescribeScheduledTask请求参数结构体
    """

    def __init__(self):
        r"""查询定时任务
        :param ScalingGroupId: 弹性伸缩组id
        :type PathPrefix: String
        :param ScalingScheduledTaskId: 弹性伸缩定时任务id列表
        :type PathPrefix: Filter
        :param ScalingScheduledTaskName: 弹性伸缩定时任务名称
        :type PathPrefix: String
        :param Marker: 
        :type PathPrefix: Int
        :param MaxResults: 
        :type PathPrefix: Int
        """
        self.ScalingGroupId = None
        self.ScalingScheduledTaskId = None
        self.ScalingScheduledTaskName = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingScheduledTaskId"):
            self.ScalingScheduledTaskId = params.get("ScalingScheduledTaskId")
        if params.get("ScalingScheduledTaskName"):
            self.ScalingScheduledTaskName = params.get("ScalingScheduledTaskName")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class ModifyScheduledTaskRequest(AbstractModel):
    """ModifyScheduledTask请求参数结构体
    """

    def __init__(self):
        r"""修改定时任务
        """

    def _deserialize(self, params):
        return


class DeleteScheduledTaskRequest(AbstractModel):
    """DeleteScheduledTask请求参数结构体
    """

    def __init__(self):
        r"""删除定时任务
        :param ScalingScheduledTaskId: 定时任务id
        :type PathPrefix: String
        :param ScalingGroupId: 弹性伸缩组id
        :type PathPrefix: String
        """
        self.ScalingScheduledTaskId = None
        self.ScalingGroupId = None

    def _deserialize(self, params):
        if params.get("ScalingScheduledTaskId"):
            self.ScalingScheduledTaskId = params.get("ScalingScheduledTaskId")
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")


class CreateScalingPolicyRequest(AbstractModel):
    """CreateScalingPolicy请求参数结构体
    """

    def __init__(self):
        r"""创建告警触发策略
        :param ScalingGroupId: 要创建告警触发策略的伸缩组Id
        :type PathPrefix: String
        :param ScalingPolicyName: 用户自定义的告警策略名称
        :type PathPrefix: String
        :param Metric: metric参数规定了具体的伸缩策略，格式为json格式。<br/>{"dimensionName":"cpu_usage","comparisonOperator":"Greater","threshold":50,"repeatTimes":2,"function":"avg","period":120}<br/>cpu使用率大于50%,且在接下来的2个周期(5分钟为1周期)都符合此规则，则促发伸缩行为，增加或减少对应的云主机
        :type PathPrefix: String
        :param AdjustmentType: 伸缩规则的调整方式。只有3种取值：<br/>TotalCapacity： 将当前伸缩组的实例数量调整到指定数量。<br/>QuantityChangeInCapacity：增加或减少指定数量的实例。<br/>PercentChangeInCapacity：增加或减少指定比例的实例(百分比)。
        :type PathPrefix: String
        :param AdjustmentValue: 伸缩规则的调整值，若为负号表示减小实例。 adjustmentType的3种取值范围分别如下：<br/>TotalCapacity：0至10<br/>QuantityChangeInCapacity : -10至10 <br/>PercentChangeInCapacity:-100至100。
        :type PathPrefix: Int
        :param CoolDown: 冷却时间，单位为秒，表示在同一伸缩组内，一个伸缩活动执行完成后的一段锁定时间。在这段时间内，该伸缩组不能执行其他伸缩活动
        :type PathPrefix: Int
        """
        self.ScalingGroupId = None
        self.ScalingPolicyName = None
        self.Metric = None
        self.AdjustmentType = None
        self.AdjustmentValue = None
        self.CoolDown = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingPolicyName"):
            self.ScalingPolicyName = params.get("ScalingPolicyName")
        if params.get("Metric"):
            self.Metric = params.get("Metric")
        if params.get("AdjustmentType"):
            self.AdjustmentType = params.get("AdjustmentType")
        if params.get("AdjustmentValue"):
            self.AdjustmentValue = params.get("AdjustmentValue")
        if params.get("CoolDown"):
            self.CoolDown = params.get("CoolDown")


class DescribeScalingPolicyRequest(AbstractModel):
    """DescribeScalingPolicy请求参数结构体
    """

    def __init__(self):
        r"""查询告警触发策略
        :param ScalingGroupId: 伸缩组ID，表示待查询告警触发策略所在的伸缩组ID
        :type PathPrefix: String
        :param ScalingPolicyId: 待查询的告警触发策略ID数组，数组下标从0开始
        :type PathPrefix: Filter
        :param ScalingPolicyName: 待查询的告警触发策略名称
        :type PathPrefix: String
        :param Marker: 偏移量，默认为0
        :type PathPrefix: Int
        :param MaxResults: 一次最多显示的CVM实例数量，默认为10,最小为5
        :type PathPrefix: Int
        """
        self.ScalingGroupId = None
        self.ScalingPolicyId = None
        self.ScalingPolicyName = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingPolicyId"):
            self.ScalingPolicyId = params.get("ScalingPolicyId")
        if params.get("ScalingPolicyName"):
            self.ScalingPolicyName = params.get("ScalingPolicyName")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class ModifyScalingPolicyRequest(AbstractModel):
    """ModifyScalingPolicy请求参数结构体
    """

    def __init__(self):
        r"""修改告警触发策略
        :param ScalingPolicyId: 要修改的告警触发策略Id
 
        :type PathPrefix: String
        :param ScalingGroupId: 要修改告警触发策略的伸缩组Id
        :type PathPrefix: String
        :param ScalingPolicyName: 用户自定义的告警策略名称
        :type PathPrefix: String
        :param Metric: metric参数规定了具体的伸缩策略，格式为json格式。<br/>{"dimensionName":"cpu_usage","comparisonOperator":"Greater","threshold":50,"repeatTimes":2,"function":"avg","period":120}<br/>cpu使用率大于50%,且在接下来的2个周期(5分钟为1周期)都符合此规则，则促发伸缩行为，增加或减少对应的云主机
        :type PathPrefix: String
        :param AdjustmentType: 伸缩规则的调整方式。只有3种取值：<br/>TotalCapacity： 将当前伸缩组的实例数量调整到指定数量。<br/>QuantityChangeInCapacity：增加或减少指定数量的实例。<br/>PercentChangeInCapacity：增加或减少指定比例的实例(百分比)。
        :type PathPrefix: String
        :param AdjustmentValue: 伸缩规则的调整值，若为负号表示减小实例。 adjustmentType的3种取值范围分别如下：<br/>TotalCapacity：0至10<br/>QuantityChangeInCapacity : -10至10 <br/>PercentChangeInCapacity:-100至100。
        :type PathPrefix: Int
        :param CoolDown: 冷却时间，单位为秒，表示在同一伸缩组内，一个伸缩活动执行完成后的一段锁定时间。在这段时间内，该伸缩组不能执行其他伸缩活动
        :type PathPrefix: Int
        """
        self.ScalingPolicyId = None
        self.ScalingGroupId = None
        self.ScalingPolicyName = None
        self.Metric = None
        self.AdjustmentType = None
        self.AdjustmentValue = None
        self.CoolDown = None

    def _deserialize(self, params):
        if params.get("ScalingPolicyId"):
            self.ScalingPolicyId = params.get("ScalingPolicyId")
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingPolicyName"):
            self.ScalingPolicyName = params.get("ScalingPolicyName")
        if params.get("Metric"):
            self.Metric = params.get("Metric")
        if params.get("AdjustmentType"):
            self.AdjustmentType = params.get("AdjustmentType")
        if params.get("AdjustmentValue"):
            self.AdjustmentValue = params.get("AdjustmentValue")
        if params.get("CoolDown"):
            self.CoolDown = params.get("CoolDown")


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy请求参数结构体
    """

    def __init__(self):
        r"""删除告警触发策略
        :param ScalingGroupId: 伸缩组Id，表示待删除告警策略所在的伸缩组
        :type PathPrefix: String
        :param ScalingPolicyId: 告警触发策略Id，待删除的告警触发策略Id
        :type PathPrefix: String
        """
        self.ScalingGroupId = None
        self.ScalingPolicyId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")
        if params.get("ScalingPolicyId"):
            self.ScalingPolicyId = params.get("ScalingPolicyId")


class ImportImageRequest(AbstractModel):
    """ImportImage请求参数结构体
    """

    def __init__(self):
        r"""镜像导入
        :param ImageName: 镜像名称。
2-64个字符，支持中文、字母、数字以及-_@#.字符
        :type PathPrefix: String
        :param Architecture: 系统架构。
i386，x86_64
        :type PathPrefix: String
        :param Platform: 操作系统版本。
centos：centos-5<br>centos-6<br>centos-7  <br>redhat：redhat-5<br>redhat-6<br>redhat7  <br>ubuntu：ubuntu-12<br>ubuntu-14<br>ubuntu-16  <br>debian：debian8/debian9 <br>fedora：fedora-20  <br>other linux：other-linux  <br>windows：windows-/server_2012_r2_datacenter_64_zh<br>windows-server_2012_r2_datacenter_64_en<br>windows-server_2008_r2_datacenter_64_zh<br>windows-server_2008_r2_datacenter_64_en
        :type PathPrefix: String
        :param ImageUrl: 存放镜像的ks3对应的bucket地址。[如何开通ks3?](https://docs.ksyun.com/documents/858)[如何获取bucket地址？](https://docs.ksyun.com/documents/906#18)
http开头，有效的bucket地址
        :type PathPrefix: String
        :param ImageFormat: 选择上传的镜像格式。
raw、vhd、qcow2、vmdk
        :type PathPrefix: String
        :param DataImageUrl: 存放数据盘镜像的ks3对应的bucket地址。
http开头，有效的bucket地址
        :type PathPrefix: Filter
        :param DataImageSize: 数据盘磁盘容量。
2-64个字符，支持中文、字母、数字以及-_@#.字符
        :type PathPrefix: Filter
        :param DataImageFormat: 选择上传的数据盘镜像格式。
raw
        :type PathPrefix: Filter
        """
        self.ImageName = None
        self.Architecture = None
        self.Platform = None
        self.ImageUrl = None
        self.ImageFormat = None
        self.DataImageUrl = None
        self.DataImageSize = None
        self.DataImageFormat = None

    def _deserialize(self, params):
        if params.get("ImageName"):
            self.ImageName = params.get("ImageName")
        if params.get("Architecture"):
            self.Architecture = params.get("Architecture")
        if params.get("Platform"):
            self.Platform = params.get("Platform")
        if params.get("ImageUrl"):
            self.ImageUrl = params.get("ImageUrl")
        if params.get("ImageFormat"):
            self.ImageFormat = params.get("ImageFormat")
        if params.get("DataImageUrl"):
            self.DataImageUrl = params.get("DataImageUrl")
        if params.get("DataImageSize"):
            self.DataImageSize = params.get("DataImageSize")
        if params.get("DataImageFormat"):
            self.DataImageFormat = params.get("DataImageFormat")


class CopyImageRequest(AbstractModel):
    """CopyImage请求参数结构体
    """

    def __init__(self):
        r"""镜像复制
        :param ImageId: 源自定义镜像的ID列表。
cc27b87a-b74c-4da8-93b0-33edce5399cf
        :type PathPrefix: Filter
        :param DestinationRegion: 复制到目标地域的列表。
=cn-beijing-6
        :type PathPrefix: Filter
        :param DestinationImageName: 复制后的镜像的名称，默认值：源镜像名称。
2-64个字符，支持中文、字母、数字以及-_@#.字符
        :type PathPrefix: String
        """
        self.ImageId = None
        self.DestinationRegion = None
        self.DestinationImageName = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("DestinationRegion"):
            self.DestinationRegion = params.get("DestinationRegion")
        if params.get("DestinationImageName"):
            self.DestinationImageName = params.get("DestinationImageName")


class ModifyImageSharePermissionRequest(AbstractModel):
    """ModifyImageSharePermission请求参数结构体
    """

    def __init__(self):
        r"""镜像共享，取消共享接口
        :param ImageId: 需要共享的镜像ID。
标准UUID格式，形如^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type PathPrefix: String
        :param AccountId: 接收分享镜像的账号ID列表。
2000001278
        :type PathPrefix: Filter
        :param Permission: 操作类型。
share，cancel；share为共享，cancel为取消共享
        :type PathPrefix: String
        """
        self.ImageId = None
        self.AccountId = None
        self.Permission = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("AccountId"):
            self.AccountId = params.get("AccountId")
        if params.get("Permission"):
            self.Permission = params.get("Permission")


class DescribeImageSharePermissionRequest(AbstractModel):
    """DescribeImageSharePermission请求参数结构体
    """

    def __init__(self):
        r"""镜像共享的账户列表
        :param ImageId: 共享的镜像ID。
标准UUID格式，形如^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type PathPrefix: String
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体
    """

    def __init__(self):
        r"""用户有权限机房
        """

    def _deserialize(self, params):
        return


class AttachKeyRequest(AbstractModel):
    """AttachKey请求参数结构体
    """

    def __init__(self):
        r"""主机绑定密钥
        :param Action: 动作
        :type PathPrefix: String
        :param InstanceId: 待绑定密钥的实例。
标准UUID格式，形如[1]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$	
        :type PathPrefix: Filter
        :param KeyId: 待绑定的密钥列表。
标准UUID格式，形如[2]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$	
        :type PathPrefix: Filter
        """
        self.Action = None
        self.InstanceId = None
        self.KeyId = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")


class DetachKeyRequest(AbstractModel):
    """DetachKey请求参数结构体
    """

    def __init__(self):
        r"""主机解绑密钥
        :param Action: 动作
        :type PathPrefix: String
        :param InstanceId: 待解绑定密钥的实例。

        :type PathPrefix: Filter
        :param KeyId: 待解绑定的密钥。

        :type PathPrefix: Filter
        """
        self.Action = None
        self.InstanceId = None
        self.KeyId = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")


class DescribeAvailabilityZonesRequest(AbstractModel):
    """DescribeAvailabilityZones请求参数结构体
    """

    def __init__(self):
        r"""查询可用区列表
        """

    def _deserialize(self, params):
        return


class DescribeInstanceTypeConfigsRequest(AbstractModel):
    """DescribeInstanceTypeConfigs请求参数结构体
    """

    def __init__(self):
        r"""查询机型套餐配置信息
        :param Filter: 
支持如下过滤器名称
instance-family 实例族
instance-type 实例类型
availability-zone 可用区
        :type PathPrefix: Filter
        """
        self.Filter = None

    def _deserialize(self, params):
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class DescribeInstanceFamilysRequest(AbstractModel):
    """DescribeInstanceFamilys请求参数结构体
    """

    def __init__(self):
        r"""查询机型配置信息
        """

    def _deserialize(self, params):
        return


class AddVmIntoDataGuardRequest(AbstractModel):
    """AddVmIntoDataGuard请求参数结构体
    """

    def __init__(self):
        r"""存量虚机迁入容灾分组
        :param DataGuardId: 容灾分组ID
        :type PathPrefix: String
        :param InstanceId: 实例ID
        :type PathPrefix: Filter
        """
        self.DataGuardId = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("DataGuardId"):
            self.DataGuardId = params.get("DataGuardId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateFileSystemRequest(AbstractModel):
    """CreateFileSystem请求参数结构体
    """

    def __init__(self):
        r"""创建一个新的文件系统
        :param AvailabilityZone: 产品服务地点，在支持可用区的Region下有效；<br>cn-beijing-6a：华北1（北京）可用区A
        :type PathPrefix: String
        :param VpcId: 主网卡VPC ID。标准UUID格式，[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type PathPrefix: String
        :param StorageType: 文件系统类型，当前支持容量型。有效值： Capacity
        :type PathPrefix: String
        :param ProtocolType: 协议类型，支持NFS，CIFS
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，有效值：长度2-64字符，支持中文，字母，数字，以及-_；
        :type PathPrefix: String
        :param ProjectId: 项目制id
        :type PathPrefix: Int
        """
        self.AvailabilityZone = None
        self.VpcId = None
        self.StorageType = None
        self.ProtocolType = None
        self.FileSystemName = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("StorageType"):
            self.StorageType = params.get("StorageType")
        if params.get("ProtocolType"):
            self.ProtocolType = params.get("ProtocolType")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DeleteFileSystemRequest(AbstractModel):
    """DeleteFileSystem请求参数结构体
    """

    def __init__(self):
        r"""删除文件系统信息
        :param FileSystemId: 预删除的文件系统ID
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class DescribeFileSystemsRequest(AbstractModel):
    """DescribeFileSystems请求参数结构体
    """

    def __init__(self):
        r"""查询文件系统信息
        :param FileSystemId: 预查看的文件系统ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用所返回的最大实例数目，取值为5~1000，超过1000记为1000
        :type PathPrefix: Int
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: Int
        :param ProjectId: 项目制id，默认为0
        :type PathPrefix: Filter
        :param IncludeDel: 是否包含删除的，默认为false
        :type PathPrefix: Boolean
        :param Filter: 可查询file-system-name和ip-address
        :type PathPrefix: Filter
        """
        self.FileSystemId = None
        self.MaxResults = None
        self.Marker = None
        self.ProjectId = None
        self.IncludeDel = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("IncludeDel"):
            self.IncludeDel = params.get("IncludeDel")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class ModifyFileSystemRequest(AbstractModel):
    """ModifyFileSystem请求参数结构体
    """

    def __init__(self):
        r"""修改文件系统（名称）
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，有效值：长度2-64字符，支持中文，字母，数字，以及-_；
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.FileSystemName = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")


class CreateMountTargetRequest(AbstractModel):
    """CreateMountTarget请求参数结构体
    """

    def __init__(self):
        r"""创建文件系统挂载点
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param SubnetId: 终端子网ID。有效值：标准UUID格式，形如^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type PathPrefix: String
        :param IpVersion: 取值为【ipv4，ipv6】，默认为 ipv4，如果选择了不支持ipv6的VPC且ip version选择 ipv6则报错
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.SubnetId = None
        self.IpVersion = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("IpVersion"):
            self.IpVersion = params.get("IpVersion")


class DeleteMountTargetRequest(AbstractModel):
    """DeleteMountTarget请求参数结构体
    """

    def __init__(self):
        r"""删除文件系统挂载点
        :param MountTargetId: 挂载点ID
        :type PathPrefix: String
        """
        self.MountTargetId = None

    def _deserialize(self, params):
        if params.get("MountTargetId"):
            self.MountTargetId = params.get("MountTargetId")


class DescribeMountTargetsRequest(AbstractModel):
    """DescribeMountTargets请求参数结构体
    """

    def __init__(self):
        r"""查询挂载点信息
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param MountTargetId: 挂载点ID
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，取值为5~1000，超过1000记为1000
        :type PathPrefix: Int
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.MountTargetId = None
        self.MaxResults = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("MountTargetId"):
            self.MountTargetId = params.get("MountTargetId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class CreateModelRequest(AbstractModel):
    """CreateModel请求参数结构体
    """

    def __init__(self):
        r"""创建实例启动模版
        :param ImageId: 镜像ID
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param InstanceType: 实例套餐类型，如果调用时未指定实例套餐类型，默认值为I1.1A
[实例套餐类型有效值](https://docs.ksyun.com/documents/40858) <br>具体套餐信息参考[实例套餐类型定义](https://docs.ksyun.com/documents/705)
        :type PathPrefix: String
        :param SystemDisk.DiskSize: 系统盘内存大小，最小值为0，最大值为500
        :type PathPrefix: String
        :param DataDiskGb: 数据卷容量，单位GB，容量限制依据[实例套餐类型定义](https://docs.ksyun.com/documents/705)变化，如果调用时未指定，则为相应实例套餐类型最小值。InstanceType为通用型主机时，此参数不生效。
        :type PathPrefix: Int
        :param SubnetId: VPC环境下的子网ID，绑定到主网卡。
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param DataDisk: 数据盘（云盘）的类型，数据盘n的类型，n 的取值范围为 [1, 8]。只支持I2、I2联网增强、N1、N2、N3、S3和I3。DataDisk.n.Type与DataDisk.n.Size必须都填写才有效。
SSD3.0，EHDD
        :type PathPrefix: Filter
        :param KeepImageLogin: 保留镜像设置登录。该参数只对使用自定义镜像有效。当该值填写为true，默认InstancePassword参数无效。该参数与InstancePassword必须填写一个。
true/false，默认值为false
        :type PathPrefix: Boolean
        :param KeyId: 秘钥ID，非必填项，无默认值，若填写则默认InstancePassword参数无效，当用户选择other-linux镜像时，不支持该登录方式。若使用的自定义镜像，KeepImageLogin 为true时，默认keyId和InstancePassword参数无效。
        :type PathPrefix: String
        :param ChargeType: 计费类型，调用时需要明确指定，无默认值。
Monthly(包年包月）、Daily（按量付费（按日月结）)、 HourlyInstantSettlement（按量付费）、Spot（竞价型实例）
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，单位月。
当计费类型为Monthly（包年包月）时，有效值1-36；其他计费类型时，强制要求参数值为0。
        :type PathPrefix: Int
        :param SecurityGroupId: 实例绑定的安全组，目前仅支持绑定一个安全组。
标准UUID格式，形如`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
        :type PathPrefix: String
        :param PrivateIpAddress: 私有IP地址，指定子网IP地址范围内的任意有效值，代表实例的主IP地址，只能选择一个，绑定到主网卡；如果未指定该参数，系统自动从有效地址池中随机选取一个。
标准IP地址格式
        :type PathPrefix: String
        :param InstanceName: 实例名称，如果未指定，则自动生成，形如`KSC-IN-[A-Z0-9]{10}`。
最短2字符，最长64字符，支持中英文
        :type PathPrefix: String
        :param InstanceNameSuffix: 实例名称后缀，InstanceName参数如果缺省，此参数不生效；当大于1台的批量创建主机，后缀编号自动+1，例如后缀输入5，主机名输入"host"，批量3台，则生成的三台主机名分别为：“host-5”、“host-6”、“host-7”。
0到9999,默认值为空
        :type PathPrefix: String
        :param SriovNetSupport: 联网增强属性<br>该参数需要满足以下两个条件：<br>1.IO优化型I1，计算优化型C1，IO优化型I2的8C以上套餐<br>2.使用的是金山云提高的标准镜像或者通过金山云标准镜像开机的实例再制作的自定义镜像
        :type PathPrefix: String
        :param ProjectId: 实例所属项目ID
账户有权限的项目ID，0为默认项目,默认值为默认项目
        :type PathPrefix: Int
        :param DataGuardId: 容灾分组ID
        :type PathPrefix: String
        :param AddressBandWidth: 弹性IP的带宽
        :type PathPrefix: Int
        :param LineId: 弹性IP的链路类型的ID
        :type PathPrefix: String
        :param AddressChargeType: 弹性IP的计费类型
**Monthly**：包年包月，有到期时间，只能升带宽<br>**Peak**：按量付费（月峰值），无到期时间，可升降带宽<br>**Daily**：按量付费（按日月结），无到期时间，可升降带宽<br>**TrafficMonthly**：按量付费（流量月结），无到期时间，可升降带宽<br>**DailyPaidByTransfer**：按量付费（流量），无到期时间，可升降带宽<br>**HourlyInstantSettlement**：按量付费，无到期时间，可升降带宽
        :type PathPrefix: String
        :param AddressPurchaseTime: 弹性IP的购买时长，只有购买包年包月弹性IP时不可缺省。
        :type PathPrefix: Int
        :param AddressProjectId: 弹性IP项目的ID
        :type PathPrefix: String
        :param ModelName: 实例启动模版名称，不允许重复
ModelTest001
        :type PathPrefix: String
        :param SystemDisk.DiskType: 不能给默认值，不传默认按价格体系配置systemDisk属性中第一个创建
        :type PathPrefix: String
        :param SystemDisk.ResizeType: 扩容 offline 离线扩容| online 在线扩容
        :type PathPrefix: String
        :param VersionDetail: 模板描述
        :type PathPrefix: String
        :param FailureAutoDelete: 开机失败是否自动删除，默认值是false
        :type PathPrefix: Boolean
        """
        self.ImageId = None
        self.InstanceType = None
        self.SystemDisk.DiskSize = None
        self.DataDiskGb = None
        self.SubnetId = None
        self.DataDisk = None
        self.KeepImageLogin = None
        self.KeyId = None
        self.ChargeType = None
        self.PurchaseTime = None
        self.SecurityGroupId = None
        self.PrivateIpAddress = None
        self.InstanceName = None
        self.InstanceNameSuffix = None
        self.SriovNetSupport = None
        self.ProjectId = None
        self.DataGuardId = None
        self.AddressBandWidth = None
        self.LineId = None
        self.AddressChargeType = None
        self.AddressPurchaseTime = None
        self.AddressProjectId = None
        self.ModelName = None
        self.SystemDisk.DiskType = None
        self.SystemDisk.ResizeType = None
        self.VersionDetail = None
        self.FailureAutoDelete = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk.DiskSize"):
            self.SystemDisk.DiskSize = params.get("SystemDisk.DiskSize")
        if params.get("DataDiskGb"):
            self.DataDiskGb = params.get("DataDiskGb")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("DataDisk"):
            self.DataDisk = params.get("DataDisk")
        if params.get("KeepImageLogin"):
            self.KeepImageLogin = params.get("KeepImageLogin")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("PrivateIpAddress"):
            self.PrivateIpAddress = params.get("PrivateIpAddress")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstanceNameSuffix"):
            self.InstanceNameSuffix = params.get("InstanceNameSuffix")
        if params.get("SriovNetSupport"):
            self.SriovNetSupport = params.get("SriovNetSupport")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("DataGuardId"):
            self.DataGuardId = params.get("DataGuardId")
        if params.get("AddressBandWidth"):
            self.AddressBandWidth = params.get("AddressBandWidth")
        if params.get("LineId"):
            self.LineId = params.get("LineId")
        if params.get("AddressChargeType"):
            self.AddressChargeType = params.get("AddressChargeType")
        if params.get("AddressPurchaseTime"):
            self.AddressPurchaseTime = params.get("AddressPurchaseTime")
        if params.get("AddressProjectId"):
            self.AddressProjectId = params.get("AddressProjectId")
        if params.get("ModelName"):
            self.ModelName = params.get("ModelName")
        if params.get("SystemDisk.DiskType"):
            self.SystemDisk.DiskType = params.get("SystemDisk.DiskType")
        if params.get("SystemDisk.ResizeType"):
            self.SystemDisk.ResizeType = params.get("SystemDisk.ResizeType")
        if params.get("VersionDetail"):
            self.VersionDetail = params.get("VersionDetail")
        if params.get("FailureAutoDelete"):
            self.FailureAutoDelete = params.get("FailureAutoDelete")


class TerminateModelsRequest(AbstractModel):
    """TerminateModels请求参数结构体
    """

    def __init__(self):
        r"""删除实例启动模版
        :param ModelId: 只传ModelId删除模板以及模板下对应的版本
        :type PathPrefix: String
        :param ModelVersion: 传ModelId和ModelVersion，删除某个模板下的版本
        :type PathPrefix: Int
        """
        self.ModelId = None
        self.ModelVersion = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("ModelVersion"):
            self.ModelVersion = params.get("ModelVersion")


class DescribeModelsRequest(AbstractModel):
    """DescribeModels请求参数结构体
    """

    def __init__(self):
        r"""查询实例启动模版
        :param ModelId: 预查看的实例启动模板ID
        :type PathPrefix: Filter
        :param MaxResults: 单次调用所返回的最大实例数目，默认值为10。
        :type PathPrefix: Int
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: Int
        """
        self.ModelId = None
        self.MaxResults = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("ModelId"):
            self.ModelId = params.get("ModelId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class DescribeDedicatedClusterRequest(AbstractModel):
    """DescribeDedicatedCluster请求参数结构体
    """

    def __init__(self):
        r"""描述专属集群信息
        :param DedicatedClusterId: 专属集群id
        :type PathPrefix: Filter
        """
        self.DedicatedClusterId = None

    def _deserialize(self, params):
        if params.get("DedicatedClusterId"):
            self.DedicatedClusterId = params.get("DedicatedClusterId")


class CreateDedicatedClusterRequest(AbstractModel):
    """CreateDedicatedCluster请求参数结构体
    """

    def __init__(self):
        r"""创建集群
        :param DedicatedClusterName: 集群名称
        :type PathPrefix: String
        :param Model: 集群类型
        :type PathPrefix: String
        :param AvailabilityZone: 类型：String
        :type PathPrefix: String
        """
        self.DedicatedClusterName = None
        self.Model = None
        self.AvailabilityZone = None

    def _deserialize(self, params):
        if params.get("DedicatedClusterName"):
            self.DedicatedClusterName = params.get("DedicatedClusterName")
        if params.get("Model"):
            self.Model = params.get("Model")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")


class DeleteDedicatedClusterRequest(AbstractModel):
    """DeleteDedicatedCluster请求参数结构体
    """

    def __init__(self):
        r"""删除集群
        :param DedicatedClusterId: 专属集群id列表
        :type PathPrefix: Filter
        """
        self.DedicatedClusterId = None

    def _deserialize(self, params):
        if params.get("DedicatedClusterId"):
            self.DedicatedClusterId = params.get("DedicatedClusterId")


class SetvCPURequest(AbstractModel):
    """SetvCPU请求参数结构体
    """

    def __init__(self):
        r"""专属宿主机设置虚拟核数
        :param DedicatedHostId: 专属集群id
        :type PathPrefix: Filter
        :param VCPU: 虚拟核数
        :type PathPrefix: Int
        """
        self.DedicatedHostId = None
        self.VCPU = None

    def _deserialize(self, params):
        if params.get("DedicatedHostId"):
            self.DedicatedHostId = params.get("DedicatedHostId")
        if params.get("VCPU"):
            self.VCPU = params.get("VCPU")


class DedicatedHostMigrateRequest(AbstractModel):
    """DedicatedHostMigrate请求参数结构体
    """

    def __init__(self):
        r"""宿主机迁移集群
        :param DedicatedClusterId: 集群Id
        :type PathPrefix: String
        :param DedicatedHostId: 专属宿主机Id
        :type PathPrefix: Filter
        """
        self.DedicatedClusterId = None
        self.DedicatedHostId = None

    def _deserialize(self, params):
        if params.get("DedicatedClusterId"):
            self.DedicatedClusterId = params.get("DedicatedClusterId")
        if params.get("DedicatedHostId"):
            self.DedicatedHostId = params.get("DedicatedHostId")


class ModifyDedicatedClusterNameRequest(AbstractModel):
    """ModifyDedicatedClusterName请求参数结构体
    """

    def __init__(self):
        r"""修改专属集群名称
        :param DedicatedClusterId: 专属集群id
        :type PathPrefix: String
        :param DedicatedClusterName: 集群名称
        :type PathPrefix: String
        """
        self.DedicatedClusterId = None
        self.DedicatedClusterName = None

    def _deserialize(self, params):
        if params.get("DedicatedClusterId"):
            self.DedicatedClusterId = params.get("DedicatedClusterId")
        if params.get("DedicatedClusterName"):
            self.DedicatedClusterName = params.get("DedicatedClusterName")


class InstanceMigrateRequest(AbstractModel):
    """InstanceMigrate请求参数结构体
    """

    def __init__(self):
        r"""专属虚机迁移
        :param DedicatedHostId: 专属宿主机id
        :type PathPrefix: String
        :param InstanceId: 虚拟机ID
        :type PathPrefix: String
        :param InstanceType: 套餐类型
        :type PathPrefix: String
        :param DataDisk: 数据盘id
        :type PathPrefix: Filter
        """
        self.DedicatedHostId = None
        self.InstanceId = None
        self.InstanceType = None
        self.DataDisk = None

    def _deserialize(self, params):
        if params.get("DedicatedHostId"):
            self.DedicatedHostId = params.get("DedicatedHostId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("DataDisk"):
            self.DataDisk = params.get("DataDisk")


class ModifyInstanceAutoDeleteTimeRequest(AbstractModel):
    """ModifyInstanceAutoDeleteTime请求参数结构体
    """

    def __init__(self):
        r"""实例定时删除
        :param InstanceId: 待重启实例ID列表，N的范围为1-100
        :type PathPrefix: Filter
        :param AutoDeleteTime: 自动删除时间
        :type PathPrefix: String
        :param AutoDeleteEip: 随主机定时删除绑定的弹性IP，包年包月的弹性IP只解绑，不删除；只有AutoDeleteTime有效值生效时，该参数才生效
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.AutoDeleteTime = None
        self.AutoDeleteEip = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AutoDeleteTime"):
            self.AutoDeleteTime = params.get("AutoDeleteTime")
        if params.get("AutoDeleteEip"):
            self.AutoDeleteEip = params.get("AutoDeleteEip")


class ModifyScalingConfigurationRequest(AbstractModel):
    """ModifyScalingConfiguration请求参数结构体
    """

    def __init__(self):
        r"""修改启动配置
        :param ScalingConfigurationId: 启动配置ID 
 
        :type PathPrefix: String
        :param ScalingConfigurationName: 启动配置名称 
 
        :type PathPrefix: String
        :param ImageId: 镜像ID 
 
        :type PathPrefix: String
        :param Password: 实例密码 
 
        :type PathPrefix: String
        :param InstanceType: 选择云主机类型 
 
        :type PathPrefix: String
        :param ChargeType: 选择云主机计费方式 
 
        :type PathPrefix: String
        :param DataDiskGb: 数据盘容量 
 
        :type PathPrefix: Int
        :param ProjectId: 数据盘容量 
 
        :type PathPrefix: Int
        :param KeepImageLogin: 保留镜像设置 
 
        :type PathPrefix: Boolean
        :param KeyId: 密钥对 
 
        :type PathPrefix: Filter
        :param DataDisk: 云盘数据盘类型 
 
        :type PathPrefix: Filter
        :param SystemDisk.DiskSize: 系统盘大小，最小值为0，最大值为500
 
        :type PathPrefix: Int
        :param AddressBandWidth: 弹性IP的带宽 
 
        :type PathPrefix: Int
        :param BandWidthShareId: 弹性IP指定的共享带宽ID 
 
        :type PathPrefix: String
        :param LineId: 弹性IP的链路类型的ID 
 
        :type PathPrefix: String
        :param AddressProjectId: 弹性IP项目的ID 
 
        :type PathPrefix: Int
        :param InstanceName: 实例名称 
 
        :type PathPrefix: String
        :param InstanceNameSuffix: 实例名称后缀 
 
        :type PathPrefix: String
        :param UserData: 用户自定义数据 
 
        :type PathPrefix: String
        :param InstanceNameTimeSuffix: 实例名称时间戳后缀，true/false 
 
        :type PathPrefix: Boolean
        :param Tag: 启动配置创建的ECS实例的标签键 
 支持1-128个字符，仅支持中英文字符、数字及±=._/@:
        :type PathPrefix: Filter
        :param LoginSetAfter: 
        :type PathPrefix: Boolean
        :param IpBindAfter: 
        :type PathPrefix: Boolean
        :param InstanceNameRandom: 实例名称随机生成
        :type PathPrefix: Boolean
        :param SystemDisk.DiskType: 不能给默认值，不传默认按价格体系配置systemDisk属性中第一个创建
        :type PathPrefix: String
        :param SystemDisk.ResizeType: 扩容 offline 离线扩容| online 在线扩容
        :type PathPrefix: String
        """
        self.ScalingConfigurationId = None
        self.ScalingConfigurationName = None
        self.ImageId = None
        self.Password = None
        self.InstanceType = None
        self.ChargeType = None
        self.DataDiskGb = None
        self.ProjectId = None
        self.KeepImageLogin = None
        self.KeyId = None
        self.DataDisk = None
        self.SystemDisk.DiskSize = None
        self.AddressBandWidth = None
        self.BandWidthShareId = None
        self.LineId = None
        self.AddressProjectId = None
        self.InstanceName = None
        self.InstanceNameSuffix = None
        self.UserData = None
        self.InstanceNameTimeSuffix = None
        self.Tag = None
        self.LoginSetAfter = None
        self.IpBindAfter = None
        self.InstanceNameRandom = None
        self.SystemDisk.DiskType = None
        self.SystemDisk.ResizeType = None

    def _deserialize(self, params):
        if params.get("ScalingConfigurationId"):
            self.ScalingConfigurationId = params.get("ScalingConfigurationId")
        if params.get("ScalingConfigurationName"):
            self.ScalingConfigurationName = params.get("ScalingConfigurationName")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("DataDiskGb"):
            self.DataDiskGb = params.get("DataDiskGb")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("KeepImageLogin"):
            self.KeepImageLogin = params.get("KeepImageLogin")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("DataDisk"):
            self.DataDisk = params.get("DataDisk")
        if params.get("SystemDisk.DiskSize"):
            self.SystemDisk.DiskSize = params.get("SystemDisk.DiskSize")
        if params.get("AddressBandWidth"):
            self.AddressBandWidth = params.get("AddressBandWidth")
        if params.get("BandWidthShareId"):
            self.BandWidthShareId = params.get("BandWidthShareId")
        if params.get("LineId"):
            self.LineId = params.get("LineId")
        if params.get("AddressProjectId"):
            self.AddressProjectId = params.get("AddressProjectId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstanceNameSuffix"):
            self.InstanceNameSuffix = params.get("InstanceNameSuffix")
        if params.get("UserData"):
            self.UserData = params.get("UserData")
        if params.get("InstanceNameTimeSuffix"):
            self.InstanceNameTimeSuffix = params.get("InstanceNameTimeSuffix")
        if params.get("Tag"):
            self.Tag = params.get("Tag")
        if params.get("LoginSetAfter"):
            self.LoginSetAfter = params.get("LoginSetAfter")
        if params.get("IpBindAfter"):
            self.IpBindAfter = params.get("IpBindAfter")
        if params.get("InstanceNameRandom"):
            self.InstanceNameRandom = params.get("InstanceNameRandom")
        if params.get("SystemDisk.DiskType"):
            self.SystemDisk.DiskType = params.get("SystemDisk.DiskType")
        if params.get("SystemDisk.ResizeType"):
            self.SystemDisk.ResizeType = params.get("SystemDisk.ResizeType")


class DescribeSpotPriceHistoryRequest(AbstractModel):
    """DescribeSpotPriceHistory请求参数结构体
    """

    def __init__(self):
        r"""DescribeSpotPriceHistory
        :param InstanceType: 实例套餐规格，支持机型E1，N2，N3
        :type PathPrefix: String
        :param AvailabilityZone: 可用区信息
        :type PathPrefix: String
        :param StartTime: 查询竞价实例历史价格的起始时间。按照ISO8601标准表示，并使用UTC +8时间，格式为yyyy-MM-ddTHH:mm:ssZ。默认值：空，空代表结束时间前3小时，最大值不得超过指定的结束时间3天。
        :type PathPrefix: String
        :param EndTime: 查询抢占式实例历史价格的结束时间。按照ISO8601标准表示，并使用UTC +8时间，格式为yyyy-MM-ddTHH:mm:ssZ。默认值：空，空表示当前时间。（endtime不进行强校验）。
        :type PathPrefix: String
        """
        self.InstanceType = None
        self.AvailabilityZone = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class DescribePriceRequest(AbstractModel):
    """DescribePrice请求参数结构体
    """

    def __init__(self):
        r"""查询价格
        :param InstanceType: 实例套餐类型，如果调用时未指定实例套餐类型，默认值为I1.1A
        :type PathPrefix: String
        :param SystemDisk.DiskSize: 云主机系统盘配置参数。若不指定该参数，则按照系统默认值进行分配。
        :type PathPrefix: String
        :param ImageId: 镜像ID。
        :type PathPrefix: String
        :param ChargeType: 计费类型，调用时需要明确指定，无默认值。
        :type PathPrefix: String
        :param PurchaseTime: 购买时长，单位月
        :type PathPrefix: Int
        :param DataDiskGb: 数据卷容量，单位GB，容量限制依据 实例套餐类型定义 变化，如果调用时未指定，则为相应实例套餐类型最小值。InstanceType为通用型主机N1、N2、N3或者为本地NVMe机型I4时，此参数不生效。。
        :type PathPrefix: Int
        :param DataDisk: 数据盘（云盘）的类型，数据盘n的类型，n 的取值范围为 [1, 8]。只支持I2、I2联网增强、E1、N1、N2、N3、S3、I3、C3。DataDisk.n.Type与DataDisk.n.Size必须都填写才有效。
        :type PathPrefix: Filter
        :param MaxCount: 最大实例数。
        :type PathPrefix: Int
        :param SystemDisk.DiskType: 不能给默认值，不传默认按价格体系配置systemDisk属性中第一个创建
        :type PathPrefix: String
        """
        self.InstanceType = None
        self.SystemDisk.DiskSize = None
        self.ImageId = None
        self.ChargeType = None
        self.PurchaseTime = None
        self.DataDiskGb = None
        self.DataDisk = None
        self.MaxCount = None
        self.SystemDisk.DiskType = None

    def _deserialize(self, params):
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk.DiskSize"):
            self.SystemDisk.DiskSize = params.get("SystemDisk.DiskSize")
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("DataDiskGb"):
            self.DataDiskGb = params.get("DataDiskGb")
        if params.get("DataDisk"):
            self.DataDisk = params.get("DataDisk")
        if params.get("MaxCount"):
            self.MaxCount = params.get("MaxCount")
        if params.get("SystemDisk.DiskType"):
            self.SystemDisk.DiskType = params.get("SystemDisk.DiskType")


class EnableImageCachingRequest(AbstractModel):
    """EnableImageCaching请求参数结构体
    """

    def __init__(self):
        r"""自定义镜像预热
        :param ImageId: 预热的镜像ID。
——
        :type PathPrefix: Filter
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class DisableImageCachingRequest(AbstractModel):
    """DisableImageCaching请求参数结构体
    """

    def __init__(self):
        r"""取消自定义镜像预热
        :param ImageId: 预热的镜像ID。
——
        :type PathPrefix: Filter
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class ModifyLoadBalancersRequest(AbstractModel):
    """ModifyLoadBalancers请求参数结构体
    """

    def __init__(self):
        r"""ModifyLoadBalancers
        :param ScalingGroupId: 待修改负载均衡的伸缩组ID
        :type PathPrefix: String
        """
        self.ScalingGroupId = None

    def _deserialize(self, params):
        if params.get("ScalingGroupId"):
            self.ScalingGroupId = params.get("ScalingGroupId")


class AttachInstancesIamRoleRequest(AbstractModel):
    """AttachInstancesIamRole请求参数结构体
    """

    def __init__(self):
        r"""实例绑定IAM角色
        :param InstanceId: 待绑定IAM角色实例ID列表，N的范围为1-100
        :type PathPrefix: Filter
        :param IamRoleName: 实例待绑定的IAM角色名称
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.IamRoleName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("IamRoleName"):
            self.IamRoleName = params.get("IamRoleName")


class DetachInstancesIamRoleRequest(AbstractModel):
    """DetachInstancesIamRole请求参数结构体
    """

    def __init__(self):
        r"""实例解除绑定IAM角色
        :param InstanceId: 待解绑IAM角色实例ID列表，N的范围为1-100
        :type PathPrefix: Filter
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CopySnapshotRequest(AbstractModel):
    """CopySnapshot请求参数结构体
    """

    def __init__(self):
        r"""本地盘快照跨region复制
        :param SnapshotId: CopySnapshot
        :type PathPrefix: Filter
        :param DestinationRegion: 目标省区
        :type PathPrefix: Filter
        :param DestinationSnapshotName: 快照名称
        :type PathPrefix: String
        :param DestinationSnapshotDesc: 快照描述
        :type PathPrefix: String
        """
        self.SnapshotId = None
        self.DestinationRegion = None
        self.DestinationSnapshotName = None
        self.DestinationSnapshotDesc = None

    def _deserialize(self, params):
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")
        if params.get("DestinationRegion"):
            self.DestinationRegion = params.get("DestinationRegion")
        if params.get("DestinationSnapshotName"):
            self.DestinationSnapshotName = params.get("DestinationSnapshotName")
        if params.get("DestinationSnapshotDesc"):
            self.DestinationSnapshotDesc = params.get("DestinationSnapshotDesc")


class PreMigrateInstanceRequest(AbstractModel):
    """PreMigrateInstance请求参数结构体
    """

    def __init__(self):
        r"""创建预迁移
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param InstanceType: 目标实例类型
        :type PathPrefix: String
        :param SystemDiskType: 云盘系统盘的类型。

有效值：SSD3.0，EHDD
        :type PathPrefix: String
        :param DataDiskType: 云盘数据盘的类型。

有效值：SSD3.0，EHDD
        :type PathPrefix: String
        :param InstantAccess: 支持快速开盘/快速变更，该参数仅对本地盘/本地盘机型/本地盘快照生效
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.InstanceType = None
        self.SystemDiskType = None
        self.DataDiskType = None
        self.InstantAccess = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("SystemDiskType"):
            self.SystemDiskType = params.get("SystemDiskType")
        if params.get("DataDiskType"):
            self.DataDiskType = params.get("DataDiskType")
        if params.get("InstantAccess"):
            self.InstantAccess = params.get("InstantAccess")


class CancelPreMigrateInstanceRequest(AbstractModel):
    """CancelPreMigrateInstance请求参数结构体
    """

    def __init__(self):
        r"""取消预迁移
        :param InstanceId: 实例id
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class GetVNCAddressRequest(AbstractModel):
    """GetVNCAddress请求参数结构体
    """

    def __init__(self):
        r"""OpenAPI获取浏览器可用的VNC地址
        :param InstanceId: 实例ID
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


