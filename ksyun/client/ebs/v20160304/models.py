from ksyun.common.abstract_model import AbstractModel


class CreateVolumeRequest(AbstractModel):
    """CreateVolume请求参数结构体
    """

    def __init__(self):
        r"""CreateVolume
        :param VolumeName: 硬盘名称
长度2-50个字符，包括字母、数字、-、_
不传自动生成
        :type PathPrefix: String
        :param VolumeType: 硬盘类型，SSD3.0/EHDD/ESSD_PL0/ESSD_PL1/ESSD_PL2/ESSD_PL3
        :type PathPrefix: String
        :param VolumeDesc: 硬盘描述信息
长度1-128字符
磁盘描述会展示在控制台
不能以 http:// 和 https:// 开头
        :type PathPrefix: String
        :param Size: 磁盘容量大小，单位GB
SSD3.0取值范围：【10，32000】，步长：1GB
EHDD取值范围：【10，32000】，步长：1GB
ESSD_PL0取值范围：【40，32768】，步长：1GB
ESSD_PL1取值范围：【40，32768】，步长：1GB
ESSD_PL2取值范围：【461，32768】，步长：1GB
ESSD_PL3取值范围：【1761，32768】，步长：1GB

        :type PathPrefix: Int
        :param AvailabilityZone: 购买云硬盘所处的可用区
如 cn-beijing-6a，cn-shanghai-2a
        :type PathPrefix: String
        :param ChargeType: 计费类型
- Monthly（预付费，包年包月）
- HourlyInstantSettlement（后付费，按小时实时结算）
- Daily（后付费，按日月结）
        :type PathPrefix: String
        :param PurchaseTime: 预付费计费类型必填字段；有效值为1-36，单位月
        :type PathPrefix: Int
        :param ProjectId: 硬盘项目组id，不传该参数将使用默认项目组id
        :type PathPrefix: String
        :param SubOrderId: 子订单ID（内部使用）
        :type PathPrefix: String
        """
        self.VolumeName = None
        self.VolumeType = None
        self.VolumeDesc = None
        self.Size = None
        self.AvailabilityZone = None
        self.ChargeType = None
        self.PurchaseTime = None
        self.ProjectId = None
        self.SubOrderId = None

    def _deserialize(self, params):
        if params.get("VolumeName"):
            self.VolumeName = params.get("VolumeName")
        if params.get("VolumeType"):
            self.VolumeType = params.get("VolumeType")
        if params.get("VolumeDesc"):
            self.VolumeDesc = params.get("VolumeDesc")
        if params.get("Size"):
            self.Size = params.get("Size")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("SubOrderId"):
            self.SubOrderId = params.get("SubOrderId")


class AttachVolumeRequest(AbstractModel):
    """AttachVolume请求参数结构体
    """

    def __init__(self):
        r"""AttachVolume
        :param VolumeId: 待挂载的云硬盘ID，云硬盘和云主机必须在同一可用区。长度36个字符，包括字母、数字、-、_-
        :type PathPrefix: String
        :param InstanceId: 待挂载的云主机实例ID
        :type PathPrefix: String
        :param DeleteWithInstance: 待挂载的云硬盘是否随云主机删除，默认值为false。取值范围：
true：删除云主机时，该云硬盘随云主机一起删除
false：删除云主机时，保留该云硬盘，仅卸载，不随云主机一起释放
        :type PathPrefix: String
        """
        self.VolumeId = None
        self.InstanceId = None
        self.DeleteWithInstance = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DeleteWithInstance"):
            self.DeleteWithInstance = params.get("DeleteWithInstance")


class DetachVolumeRequest(AbstractModel):
    """DetachVolume请求参数结构体
    """

    def __init__(self):
        r"""DetachVolume
        :param InstanceId: 待卸载的云主机实例ID
如果未传, 则获取当前硬盘挂载的主机ID
        :type PathPrefix: String
        :param VolumeId: 待卸载的云硬盘ID，云硬盘和云主机必须在同一可用区。长度36个字符，包括字母、数字、-、_
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.VolumeId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")


class DeleteVolumeRequest(AbstractModel):
    """DeleteVolume请求参数结构体
    """

    def __init__(self):
        r"""DeleteVolume
        :param VolumeId: 硬盘ID
长度36个字符，包括字母、数字、-
        :type PathPrefix: String
        :param ForceDelete: true直接彻底删除，false进入回收站，回收中云盘传true会从回收站删除；默认为false
        :type PathPrefix: Boolean
        """
        self.VolumeId = None
        self.ForceDelete = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("ForceDelete"):
            self.ForceDelete = params.get("ForceDelete")


class ResizeVolumeRequest(AbstractModel):
    """ResizeVolume请求参数结构体
    """

    def __init__(self):
        r"""ResizeVolume
        :param VolumeId: 待扩容的云硬盘ID，云硬盘和云主机必须在同一可用区。长度36个字符，包括字母、数字、-、_
        :type PathPrefix: String
        :param Size: 云硬盘扩容后的大小，单位GB。区间必须比原云盘容量大，单盘容量不可大于32TB。
        :type PathPrefix: String
        :param OnlineResize: 云硬盘扩容的方式：
● false（默认）：离线扩容；扩容后，必须经过控制台重启或者调用API重启实例使操作生效
● true：在线扩容（仅部分操作系统支持），无需重启实例即可完成扩容
        :type PathPrefix: Boolean
        :param SubOrderId: 子订单ID
        :type PathPrefix: String
        """
        self.VolumeId = None
        self.Size = None
        self.OnlineResize = None
        self.SubOrderId = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("Size"):
            self.Size = params.get("Size")
        if params.get("OnlineResize"):
            self.OnlineResize = params.get("OnlineResize")
        if params.get("SubOrderId"):
            self.SubOrderId = params.get("SubOrderId")


class DescribeVolumesRequest(AbstractModel):
    """DescribeVolumes请求参数结构体
    """

    def __init__(self):
        r"""DescribeVolumes
        :param VolumeId: 云硬盘ID，传参方式请参照示例；长度36个字符，包括字母、数字、-不传此参数，则查询该用户下所有硬盘信息。最多传入100个，N为1~100
        :type PathPrefix: Filter
        :param VolumeCategory: 云硬盘分类，两种，有效值是系统盘（system）或者数据盘（data）

        :type PathPrefix: String
        :param VolumeStatus: 云硬盘状态，八种creating、available、attaching、inuse、detaching、extending、deleting、error
        :type PathPrefix: String
        :param VolumeType: 云硬盘类型，SSD3.0/EHDD/ESSD_PL0/ESSD_PL1/ESSD_PL2/ESSD_PL3
        :type PathPrefix: String
        :param VolumeCreateDate: 云硬盘创建日期，格式：yyyy-MM-dd，可查出当日创建硬盘信息
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大实例数目，取值为10~1000，超过1000记为1000
最大值：1000
默认值：10
        :type PathPrefix: Int
        """
        self.VolumeId = None
        self.VolumeCategory = None
        self.VolumeStatus = None
        self.VolumeType = None
        self.VolumeCreateDate = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("VolumeCategory"):
            self.VolumeCategory = params.get("VolumeCategory")
        if params.get("VolumeStatus"):
            self.VolumeStatus = params.get("VolumeStatus")
        if params.get("VolumeType"):
            self.VolumeType = params.get("VolumeType")
        if params.get("VolumeCreateDate"):
            self.VolumeCreateDate = params.get("VolumeCreateDate")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class ModifyVolumeRequest(AbstractModel):
    """ModifyVolume请求参数结构体
    """

    def __init__(self):
        r"""ModifyVolume
        :param VolumeId: 待修改属性信息的云硬盘ID，云硬盘和云主机必须在同一可用区。长度36个字符，包括字母、数字、-、_
        :type PathPrefix: String
        :param VolumeName: 硬盘名称长度2-50个字符，包括字母、数字、-、_
        :type PathPrefix: String
        :param VolumeDesc: 硬盘描述信息长度0-128字符
        :type PathPrefix: String
        :param DeleteWithInstance: 待挂载的云硬盘是否随云主机删除。取值范围：
true：删除云主机时，该云硬盘随云主机一起删除
false：删除云主机时，保留该云硬盘，仅卸载，不随云主机一起释放
        :type PathPrefix: String
        """
        self.VolumeId = None
        self.VolumeName = None
        self.VolumeDesc = None
        self.DeleteWithInstance = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("VolumeName"):
            self.VolumeName = params.get("VolumeName")
        if params.get("VolumeDesc"):
            self.VolumeDesc = params.get("VolumeDesc")
        if params.get("DeleteWithInstance"):
            self.DeleteWithInstance = params.get("DeleteWithInstance")


class DescribeEbsInstancesRequest(AbstractModel):
    """DescribeEbsInstances请求参数结构体
    """

    def __init__(self):
        r"""DescribeEbsInstances
        :param AvailabilityZone: 指定获取某个AZ的可用主机
        :type PathPrefix: String
        :param VolumeType: 硬盘类型，SSD3.0/EHDD/ESSD_PL0/ESSD_PL1/ESSD_PL2/ESSD_PL3
        :type PathPrefix: String
        """
        self.AvailabilityZone = None
        self.VolumeType = None

    def _deserialize(self, params):
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("VolumeType"):
            self.VolumeType = params.get("VolumeType")


class DescribeInstanceVolumesRequest(AbstractModel):
    """DescribeInstanceVolumes请求参数结构体
    """

    def __init__(self):
        r"""DescribeInstanceVolumes
        :param InstanceId: 待查询的主机实例ID，现只支持单个查询长度36个字符，包括字母、数字、-
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class RenewVolumeRequest(AbstractModel):
    """RenewVolume请求参数结构体
    """

    def __init__(self):
        r"""RenewVolume
        :param VolumeId: 待续费的云硬盘ID，云硬盘和云主机必须在同一可用区。长度36个字符，包括字母、数字、-、_
        :type PathPrefix: String
        :param PurchaseTime: 需要续费的月数
        :type PathPrefix: Int
        """
        self.VolumeId = None
        self.PurchaseTime = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")


class UpdateVolumeProjectRequest(AbstractModel):
    """UpdateVolumeProject请求参数结构体
    """

    def __init__(self):
        r"""UpdateVolumeProject
        :param VolumeId: 硬盘ID，传参方式请参照示例.长度36个字符，包括字母、数字、-.PS:最多传入100个.N为1~100,硬盘状态必须为待挂载（available）
        :type PathPrefix: Filter
        :param ProjectId: 目标项目组id，项目组状态必须为可用
        :type PathPrefix: String
        """
        self.VolumeId = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots请求参数结构体
    """

    def __init__(self):
        r"""DescribeSnapshots
        :param VolumeId: 云盘ID，传入该参数可获取指定硬盘的所有快照数据，此时其他参数无效
        :type PathPrefix: String
        :param VolumeCategory: 硬盘分类，system（系统盘）或data（数据盘），传入该参数可获取指定类型的快照列表
        :type PathPrefix: String
        :param SnapshotId: 快照ID，传入该参数可获取指定快照的信息，此时其他参数无效
        :type PathPrefix: String
        :param AvailabilityZone: 可用区，传入该参数可获取指定可用区的快照信息
        :type PathPrefix: String
        :param SnapshotName: 快照名称，传入可进行快照名称的查询
        :type PathPrefix: String
        :param PageNumber: 页码，默认1，范围1-intMax
        :type PathPrefix: Int
        :param PageSize: 每页大小，默认10，范围1-intMax
        :type PathPrefix: Int
        """
        self.VolumeId = None
        self.VolumeCategory = None
        self.SnapshotId = None
        self.AvailabilityZone = None
        self.SnapshotName = None
        self.PageNumber = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("VolumeCategory"):
            self.VolumeCategory = params.get("VolumeCategory")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("SnapshotName"):
            self.SnapshotName = params.get("SnapshotName")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class CreateSnapshotRequest(AbstractModel):
    """CreateSnapshot请求参数结构体
    """

    def __init__(self):
        r"""CreateSnapshot
        :param VolumeId: 云硬盘创建快照时需为使用中或待挂载状态，使用中时主机状态为运行中或停止。长度36个字符，包括字母、数字、-、_
        :type PathPrefix: String
        :param SnapshotName: 快照名称，长度2-50个字符，包括字母、数字、“-”、“_”。不传自动生成，不能以auto开头
        :type PathPrefix: String
        :param SnapshotDesc: 快照描述，长度0-128字符
        :type PathPrefix: String
        :param SnapshotType: 快照类型支持极速可用快照（LocalSnapShot）、普通快照（CommonSnapShot），默认CommonSnapShot
        :type PathPrefix: String
        """
        self.VolumeId = None
        self.SnapshotName = None
        self.SnapshotDesc = None
        self.SnapshotType = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("SnapshotName"):
            self.SnapshotName = params.get("SnapshotName")
        if params.get("SnapshotDesc"):
            self.SnapshotDesc = params.get("SnapshotDesc")
        if params.get("SnapshotType"):
            self.SnapshotType = params.get("SnapshotType")


class DeleteSnapshotRequest(AbstractModel):
    """DeleteSnapshot请求参数结构体
    """

    def __init__(self):
        r"""DeleteSnapshot
        :param SnapshotId: 快照ID
长度36个字符，包括字母、数字、-
        :type PathPrefix: String
        """
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class RollbackSnapshotRequest(AbstractModel):
    """RollbackSnapshot请求参数结构体
    """

    def __init__(self):
        r"""RollbackSnapshot
        :param VolumeId: 云盘ID，长度36个字符，包括字母、数字、-
        :type PathPrefix: String
        :param SnapshotId: 快照ID
        :type PathPrefix: String
        """
        self.VolumeId = None
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class ModifySnapshotRequest(AbstractModel):
    """ModifySnapshot请求参数结构体
    """

    def __init__(self):
        r"""ModifySnapshot
        :param SnapshotId: 快照ID，长度36个字符，包括字母、数字、-
        :type PathPrefix: String
        :param SnapshotName: 快照名称，长度2-50个字符，包括字母、数字、“-”、“_”，不能以auto开头
        :type PathPrefix: String
        :param SnapshotDesc: 快照描述，长度0-128字符
        :type PathPrefix: String
        """
        self.SnapshotId = None
        self.SnapshotName = None
        self.SnapshotDesc = None

    def _deserialize(self, params):
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")
        if params.get("SnapshotName"):
            self.SnapshotName = params.get("SnapshotName")
        if params.get("SnapshotDesc"):
            self.SnapshotDesc = params.get("SnapshotDesc")


class RecoveryVolumeRequest(AbstractModel):
    """RecoveryVolume请求参数结构体
    """

    def __init__(self):
        r"""RecoveryVolume
        :param VolumeId: 硬盘ID
长度36个字符，包括字母、数字、-
        :type PathPrefix: String
        """
        self.VolumeId = None

    def _deserialize(self, params):
        if params.get("VolumeId"):
            self.VolumeId = params.get("VolumeId")


class ValidateAttachInstanceRequest(AbstractModel):
    """ValidateAttachInstance请求参数结构体
    """

    def __init__(self):
        r"""ValidateAttachInstance
        :param VolumeType: 硬盘类型，有效值SSD3.0/EHDD/ESSD_PL0/ESSD_PL1/ESSD_PL2/ESSD_PL3
        :type PathPrefix: String
        :param InstanceId: 需要校验的主机实例ID，长度为36个字符，包括字母，数字，-
        :type PathPrefix: String
        """
        self.VolumeType = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("VolumeType"):
            self.VolumeType = params.get("VolumeType")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeCreateVolumePriceRequest(AbstractModel):
    """DescribeCreateVolumePrice请求参数结构体
    """

    def __init__(self):
        r"""查询云盘新建时的价格
        :param VolumeType: 云盘类型，ESSD_PL0/ESSD_PL1/ESSD_PL2/ESSD_PL3/SSD3.0/EHDD
        :type PathPrefix: String
        :param Size: 磁盘容量大小，单位GB，步长：1GB
        :type PathPrefix: Int
        :param AvailabilityZone: 购买云硬盘所处的可用区
        :type PathPrefix: String
        :param ChargeType: 计费类型
Monthly（预付费，包年包月）
HourlyInstantSettlement（后付费，按小时实时结算）
Daily（后付费，按日月结）
        :type PathPrefix: String
        :param PurchaseTime: 预付费计费类型必填字段；有效值为1-36，单位月
        :type PathPrefix: Int
        """
        self.VolumeType = None
        self.Size = None
        self.AvailabilityZone = None
        self.ChargeType = None
        self.PurchaseTime = None

    def _deserialize(self, params):
        if params.get("VolumeType"):
            self.VolumeType = params.get("VolumeType")
        if params.get("Size"):
            self.Size = params.get("Size")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
