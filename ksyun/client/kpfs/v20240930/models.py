from ksyun.common.abstract_model import AbstractModel

class DescribeFileSystemListRequest(AbstractModel):
    """DescribeFileSystemList请求参数结构体
    """

    def __init__(self):
        r"""查询文件系统列表
        :param FileSystemName: 文件系统名称前缀，模糊查询。
        :type PathPrefix: String
        :param FileSystemIds: 文件系统的实例ID清单，支持批量查询，FileSystemId 以逗号分隔。
        :type PathPrefix: String
        :param StoreClasses: 文件系统的存储类型。
        :type PathPrefix: String
        :param ProjectId: 项目制。子账号查询：若不传则返回子账号下有权限项目的文件系统列表。主账号查询：若不传则返回所有项目的文件系统列表。
        :type PathPrefix: String
        :param PageNum: 页码。默认为1。
        :type PathPrefix: Int
        :param PageSize: 分页大小。默认为10。
        :type PathPrefix: Int
        """
        self.FileSystemName = None
        self.FileSystemIds = None
        self.StoreClasses = None
        self.ProjectId = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("FileSystemIds"):
            self.FileSystemIds = params.get("FileSystemIds")
        if params.get("StoreClasses"):
            self.StoreClasses = params.get("StoreClasses")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class GetTotalSizeRequest(AbstractModel):
    """GetTotalSize请求参数结构体
    """

    def __init__(self):
        r"""当前文件系统中的容量使用数量
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/。


仅设置了目录配额的目录支持查询目录使用量及已用Inodes数量随时间变化趋势
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.DirPath = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")


class GetInodeCountRequest(AbstractModel):
    """GetInodeCount请求参数结构体
    """

    def __init__(self):
        r"""当前文件系统中的inode数量
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/。


仅设置了目录配额的目录支持查询目录使用量及已用Inodes数量随时间变化趋势
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.DirPath = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")


class DescribeFileSystemClientInfoRequest(AbstractModel):
    """DescribeFileSystemClientInfo请求参数结构体
    """

    def __init__(self):
        r"""查询文件系统POSIX客户端信息
        :param FileSystemId: 文件系统实例ID
        :type PathPrefix: String
        :param CacheGroup: 客户端所在缓存组，仅容量Ⅰ型、容量Ⅱ型、标准型支持，精确匹配。
        :type PathPrefix: String
        :param CacheGroupRole: 客户端所在缓存组中的角色，仅容量Ⅰ型、容量Ⅱ型、标准型支持，精确匹配。

consumer：代表消费者，即缓存组中的--no-sharing节点

provider：代表提供者
        :type PathPrefix: String
        :param HostNamePrefix: 客户端对应的主机名称前缀。
        :type PathPrefix: String
        :param PageSize: 页码。默认为1。
        :type PathPrefix: Int
        :param PageNum: 分页大小。默认为10。
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.CacheGroup = None
        self.CacheGroupRole = None
        self.HostNamePrefix = None
        self.PageSize = None
        self.PageNum = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("CacheGroup"):
            self.CacheGroup = params.get("CacheGroup")
        if params.get("CacheGroupRole"):
            self.CacheGroupRole = params.get("CacheGroupRole")
        if params.get("HostNamePrefix"):
            self.HostNamePrefix = params.get("HostNamePrefix")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")


class DescribeFileSystemFileListRequest(AbstractModel):
    """DescribeFileSystemFileList请求参数结构体
    """

    def __init__(self):
        r"""查询文件系统文件列表
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param Dir: 需要以/开头，且/需要做encode。默认搜索根目录。
        :type PathPrefix: String
        :param FileName: 当前目录下需要搜索的文件前缀。
        :type PathPrefix: String
        :param PageNum: 页码。默认为1。
        :type PathPrefix: Long
        :param PageSize: 分页。默认为10。
        :type PathPrefix: Long
        """
        self.FileSystemId = None
        self.Dir = None
        self.FileName = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("Dir"):
            self.Dir = params.get("Dir")
        if params.get("FileName"):
            self.FileName = params.get("FileName")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class RenewFileSystemRequest(AbstractModel):
    """RenewFileSystem请求参数结构体
    """

    def __init__(self):
        r"""文件系统续费
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param PurchaseTime: 购买时长。有效值：1~60，单位：月。
        :type PathPrefix: Long
        """
        self.FileSystemId = None
        self.PurchaseTime = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")


class UpgradeFileSystemRequest(AbstractModel):
    """UpgradeFileSystem请求参数结构体
    """

    def __init__(self):
        r"""文件系统扩容
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param Capacity: 文件系统扩容后容量，单位：TiB。
        :type PathPrefix: Long
        """
        self.FileSystemId = None
        self.Capacity = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("Capacity"):
            self.Capacity = params.get("Capacity")


class CreateFileSystemRequest(AbstractModel):
    """CreateFileSystem请求参数结构体
    """

    def __init__(self):
        r"""文件系统创建
        :param FileSystemName: 文件系统名称。容量Ⅰ型/容量Ⅱ型/标准型限制：小写字母开头，仅可包含小写字母、数字与连线符'-'，长度3-40个字符，不可以连线符'-'结尾。性能Ⅰ型/性能Ⅱ型限制：小写字母开头，仅可包含小写字母、数字与连线符'_'，长度3-40个字符，不可以下划线'_'结尾。
        :type PathPrefix: String
        :param Region: 文件系统所在地域。
        :type PathPrefix: String
        :param AvailZone: 文件系统所在可用区，需与Region参数配合使用。
        :type PathPrefix: String
        :param ChargeType: 文件系统计费类型。monthly（预付费，包年包月）、dailySettlement（后付费，按量付费）。
        :type PathPrefix: String
        :param PurchaseTime: 文件系统购买时长，仅购买包年包月时需填写。有效值：1~60，单位：月。
        :type PathPrefix: Long
        :param StoreClass: 文件系统存储类型。KPFS-capacity（容量Ⅰ型）、KPFS-capacity2（容量Ⅱ型）、KPFS-standard（标准型）、KPFS-P-S01（性能Ⅰ型）、KPFS-P-S02（性能Ⅱ型）。
        :type PathPrefix: String
        :param Capacity: 文件系统购买容量。单位TiB。有效值：容量Ⅰ型 20~102400；容量Ⅱ型 20~102400；标准型 10~102400；性能Ⅰ型 10~102400；性能Ⅱ型 10~102400。
        :type PathPrefix: Long
        :param ChunkSize: 条带块大小，仅性能Ⅰ型、性能Ⅱ型需填写。单位：Byte。枚举值：4096（4KB，小文件友好型）、32768（32KB，均衡型）、65536（64KB，大文件友好型）。
        :type PathPrefix: Long
        :param ClusterCode: 存储池Code，为集群的唯一标识，仅性能Ⅰ型、性能Ⅱ型需填写。
        :type PathPrefix: String
        """
        self.FileSystemName = None
        self.Region = None
        self.AvailZone = None
        self.ChargeType = None
        self.PurchaseTime = None
        self.StoreClass = None
        self.Capacity = None
        self.ChunkSize = None
        self.ClusterCode = None

    def _deserialize(self, params):
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("Region"):
            self.Region = params.get("Region")
        if params.get("AvailZone"):
            self.AvailZone = params.get("AvailZone")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("Capacity"):
            self.Capacity = params.get("Capacity")
        if params.get("ChunkSize"):
            self.ChunkSize = params.get("ChunkSize")
        if params.get("ClusterCode"):
            self.ClusterCode = params.get("ClusterCode")


class GetCapacityAvailableRequest(AbstractModel):
    """GetCapacityAvailable请求参数结构体
    """

    def __init__(self):
        r"""文件系统可用容量
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")


class GetCapacityTotalRequest(AbstractModel):
    """GetCapacityTotal请求参数结构体
    """

    def __init__(self):
        r"""文件系统总容量
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")


class GetLatencyWriteRequest(AbstractModel):
    """GetLatencyWrite请求参数结构体
    """

    def __init__(self):
        r"""客户端级写延迟
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param ClientNm: POSIX客户端的挂载信息。拼接规则为：Ip:ClientId，如：10.0.0.1:1000018。请参见查询文件系统POSIX客户端信息。
        :type PathPrefix: String
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。


该参数仅支持专属集群以及西北1（庆阳）公共集群，且白名单开放。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.ClientNm = None
        self.VpcIp = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")
        if params.get("VpcIp"):
            self.VpcIp = params.get("VpcIp")


class GetLatencyReadRequest(AbstractModel):
    """GetLatencyRead请求参数结构体
    """

    def __init__(self):
        r"""性能型客户端级读延迟
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param ClientNm: POSIX客户端的挂载信息。拼接规则为：Ip:ClientId，如：10.0.0.1:1000018。请参见查询文件系统POSIX客户端信息。
        :type PathPrefix: String
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。


该参数仅支持专属集群以及西北1（庆阳）公共集群，且白名单开放。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.ClientNm = None
        self.VpcIp = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")
        if params.get("VpcIp"):
            self.VpcIp = params.get("VpcIp")


class GetIopsWriteRequest(AbstractModel):
    """GetIopsWrite请求参数结构体
    """

    def __init__(self):
        r"""写IOPS
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param ClientNm: POSIX客户端的挂载信息。拼接规则为：Ip:ClientId，如：10.0.0.1:1000018。请参见查询文件系统POSIX客户端信息。
        :type PathPrefix: String
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。


该参数仅支持专属集群以及西北1（庆阳）公共集群，且白名单开放。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.ClientNm = None
        self.VpcIp = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")
        if params.get("VpcIp"):
            self.VpcIp = params.get("VpcIp")


class GetIopsReadRequest(AbstractModel):
    """GetIopsRead请求参数结构体
    """

    def __init__(self):
        r"""读IOPS
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param ClientNm: POSIX客户端的挂载信息。拼接规则为：Ip:ClientId，如：10.0.0.1:1000018。请参见查询文件系统POSIX客户端信息。
        :type PathPrefix: String
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。


该参数仅支持专属集群以及西北1（庆阳）公共集群，且白名单开放。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.ClientNm = None
        self.VpcIp = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")
        if params.get("VpcIp"):
            self.VpcIp = params.get("VpcIp")


class GetBandwidthWriteRequest(AbstractModel):
    """GetBandwidthWrite请求参数结构体
    """

    def __init__(self):
        r"""文件系统统计查询_性能型写带宽
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param ClientNm: POSIX客户端的挂载信息。拼接规则为：Ip:ClientId，如：10.0.0.1:1000018。请参见查询文件系统POSIX客户端信息。
        :type PathPrefix: String
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。


该参数仅支持专属集群以及西北1（庆阳）公共集群，且白名单开放。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.ClientNm = None
        self.VpcIp = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")
        if params.get("VpcIp"):
            self.VpcIp = params.get("VpcIp")


class GetBandwidthReadRequest(AbstractModel):
    """GetBandwidthRead请求参数结构体
    """

    def __init__(self):
        r"""文件系统统计查询_性能型读带宽
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d；（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param ClientNm: POSIX客户端的挂载信息。拼接规则为：Ip:ClientId，如：10.0.0.1:1000018。请参见查询文件系统POSIX客户端信息。
        :type PathPrefix: String
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。


该参数仅支持专属集群以及西北1（庆阳）公共集群，且白名单开放。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.ClientNm = None
        self.VpcIp = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")
        if params.get("VpcIp"):
            self.VpcIp = params.get("VpcIp")


class DeletePerformanceOnePosixAclRequest(AbstractModel):
    """DeletePerformanceOnePosixAcl请求参数结构体
    """

    def __init__(self):
        r"""删除POSIX协议访问授权
        :param PosixAclId: 待删除POSIX访问授权规则ID
        :type PathPrefix: String
        """
        self.PosixAclId = None

    def _deserialize(self, params):
        if params.get("PosixAclId"):
            self.PosixAclId = params.get("PosixAclId")


class UpdatePerformanceOnePosixAclRequest(AbstractModel):
    """UpdatePerformanceOnePosixAcl请求参数结构体
    """

    def __init__(self):
        r"""修改POSIX协议访问授权
        :param PosixAclId: POSIX访问授权规则ID
        :type PathPrefix: String
        :param FileSystemList: 文件系统数组，支持批量绑定文件系统
        :type PathPrefix: Array
        :param AutoMount: 是否自动挂载；true自动挂载，false手动挂载
        :type PathPrefix: Boolean
        :param Ips: 允许访问的客户端IP列表，授权白名单
        :type PathPrefix: Array
        :param Desc: 该POSIX授权规则自定义描述
        :type PathPrefix: String
        """
        self.PosixAclId = None
        self.FileSystemList = None
        self.AutoMount = None
        self.Ips = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("PosixAclId"):
            self.PosixAclId = params.get("PosixAclId")
        if params.get("FileSystemList"):
            self.FileSystemList = params.get("FileSystemList")
        if params.get("AutoMount"):
            self.AutoMount = params.get("AutoMount")
        if params.get("Ips"):
            self.Ips = params.get("Ips")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class DescribePerformanceOnePosixAclListRequest(AbstractModel):
    """DescribePerformanceOnePosixAclList请求参数结构体
    """

    def __init__(self):
        r"""查询POSIX协议访问授权列表
        :param FileSystemId: 文件系统实例ID，筛选条件，非必填
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，筛选条件，非必填
        :type PathPrefix: String
        :param Ip: 授权IP，模糊筛选条件，非必填
        :type PathPrefix: String
        :param PageNum: 分页页码，默认1
        :type PathPrefix: Int
        :param PageSize: 分页每页条数，默认10
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.FileSystemName = None
        self.Ip = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("Ip"):
            self.Ip = params.get("Ip")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class SetPerformanceOnePosixAclRequest(AbstractModel):
    """SetPerformanceOnePosixAcl请求参数结构体
    """

    def __init__(self):
        r"""新建POSIX协议访问授权
        :param FileSystemList: 文件系统数组，支持批量绑定文件系统
        :type PathPrefix: Array
        :param AutoMount: 是否自动挂载；true自动挂载，false手动挂载
        :type PathPrefix: Boolean
        :param Ips: 允许访问的客户端IP列表，授权白名单
        :type PathPrefix: Array
        :param Desc: 该POSIX授权规则自定义描述
        :type PathPrefix: String
        """
        self.FileSystemList = None
        self.AutoMount = None
        self.Ips = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("FileSystemList"):
            self.FileSystemList = params.get("FileSystemList")
        if params.get("AutoMount"):
            self.AutoMount = params.get("AutoMount")
        if params.get("Ips"):
            self.Ips = params.get("Ips")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class DescribeDirQuotaListRequest(AbstractModel):
    """DescribeDirQuotaList请求参数结构体
    """

    def __init__(self):
        r"""查询目录配额列表
        :param FileSystemId: 文件系统的实例ID

性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。

容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型，取值：

KPFS-capacity（容量Ⅰ型）

KPFS-capacity2（容量Ⅱ型）

KPFS-standard（标准型）

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型）
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录路径模糊查询关键字，支持中间路径的模糊匹配，比如，存在目录配额/dir/subdir，查询关键字为subdir，那么会返回/dir/subdir的目录配额信息。

注意：若不传入该参数，则返回文件系统下的目录配额列表。
        :type PathPrefix: String
        :param FuzzySearch: 是否模糊查询，默认 true；精确查询时，格式：dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/×××/。
        :type PathPrefix: Boolean
        :param PageSize: 页码。默认为1。
        :type PathPrefix: Int
        :param PageNum: 分页大小。默认为10。
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None
        self.FuzzySearch = None
        self.PageSize = None
        self.PageNum = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")


class DeleteDirQuotaRequest(AbstractModel):
    """DeleteDirQuota请求参数结构体
    """

    def __init__(self):
        r"""删除目录配额
        :param FileSystemId: 文件系统的实例ID

性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。

容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填
        :type PathPrefix: String
        :param StoreClass: 存储类型，取值：

KPFS-capacity（容量Ⅰ型）

KPFS-capacity2（容量Ⅱ型）

KPFS-standard（标准型）

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/

注意：

性能Ⅰ型/性能Ⅱ型存储池、文件系统名称、目录完整路径不允许修改，必须与原目录相同。

容量Ⅰ型/容量Ⅱ型/标准型，必须与原目录相同。

已设置目录配额的目录，才允许删除目录配额。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")


class UpdateDirQuotaRequest(AbstractModel):
    """UpdateDirQuota请求参数结构体
    """

    def __init__(self):
        r"""修改目录配额
        :param FileSystemId: 文件系统的实例ID

性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。

容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型，取值：

KPFS-capacity（容量Ⅰ型）

KPFS-capacity2（容量Ⅱ型）

KPFS-standard（标准型）

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型）
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/

注意：

性能Ⅰ型/性能Ⅱ型存储池、文件系统名称、目录完整路径不允许修改，必须与原目录相同。

容量Ⅰ型/容量Ⅱ型/标准型，必须与原目录相同。

为已设置目录配额的目录，才允许修改目录配额。
        :type PathPrefix: String
        :param LogicalCapacityType: 容量配额的设置方式，若不传，则默认为limit。参数取值：

none：无设置，该条目录配额不进行容量设置。仅KPFS性能型支持。

statistics：仅统计，设置后将统计该目录容量情况但不限制容量。仅KPFS性能型支持。

limit：限制类型，设置后将统计该目录容量情况且限制容量。KPFS容量型、标准型、性能型均支持。
        :type PathPrefix: String
        :param LogicalHardThreshold: 容量硬阈值，正整数，不可超过文件系统容量配额，仅LogicalCapacityType取值为limit时支持设置该参数。

单位：Bytes。
        :type PathPrefix: Long
        :param LogicalInodesType: Inodes配额的设置方式，若不传，则默认为none，仅KPFS性能型支持。参数取值：

none：无设置

statistics：仅统计，设置后将统计该目录Inodes情况但不限制Inodes。

limit：限制类型，设置后将统计该目录Inodes情况且限制Inodes。
        :type PathPrefix: String
        :param LogicalHardInodes: Inodes硬阈值，正整数。仅LogicalInodesTypee取值为limit时支持设置该参数。仅KPFS性能型支持。

单位：个
        :type PathPrefix: Long
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None
        self.LogicalCapacityType = None
        self.LogicalHardThreshold = None
        self.LogicalInodesType = None
        self.LogicalHardInodes = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("LogicalCapacityType"):
            self.LogicalCapacityType = params.get("LogicalCapacityType")
        if params.get("LogicalHardThreshold"):
            self.LogicalHardThreshold = params.get("LogicalHardThreshold")
        if params.get("LogicalInodesType"):
            self.LogicalInodesType = params.get("LogicalInodesType")
        if params.get("LogicalHardInodes"):
            self.LogicalHardInodes = params.get("LogicalHardInodes")


class CreateDirQuotaRequest(AbstractModel):
    """CreateDirQuota请求参数结构体
    """

    def __init__(self):
        r"""新建目录配额
        :param FileSystemId: 文件系统的实例ID

性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。

容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型，取值：

KPFS-capacity（容量Ⅰ型）

KPFS-capacity2（容量Ⅱ型）

KPFS-standard（标准型）

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型）
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/

注意：

性能Ⅰ型/性能Ⅱ型存储池、文件系统名称、目录完整路径不允许修改，必须与原目录相同。

容量Ⅰ型/容量Ⅱ型/标准型，若目录不存在，接口会自动创建新目录。

性能Ⅰ型/性能Ⅱ型，不支持为非空目录新增配额。

无法为文件系统根目录设置配额，仅支持子目录。

支持为各级目录设置配额，并且嵌套配额均取最小值作为该目录的阈值。比如：设置/dir配额为1MB，设置/dir/subdir配额为10MB，那么实际使用时会递归地向上查询，确保当前目录用量满足每一级目录的配额设置
        :type PathPrefix: String
        :param LogicalCapacityType: 容量配额的设置方式，若不传，则默认为limit。参数取值：

none：无设置，该条目录配额不进行容量设置。仅KPFS性能型支持。

statistics：仅统计，设置后将统计该目录容量情况但不限制容量。仅KPFS性能型支持。

limit：限制类型，设置后将统计该目录容量情况且限制容量。KPFS容量型、标准型、性能型均支持。
        :type PathPrefix: String
        :param LogicalHardThreshold: 容量硬阈值，正整数，不可超过文件系统容量配额，仅LogicalCapacityType取值为limit时支持设置该参数。

单位：Bytes。
        :type PathPrefix: Long
        :param LogicalInodesType: Inodes配额的设置方式，若不传，则默认为none，仅KPFS性能型支持。参数取值：

none：无设置

statistics：仅统计，设置后将统计该目录Inodes情况但不限制Inodes。

limit：限制类型，设置后将统计该目录Inodes情况且限制Inodes。
        :type PathPrefix: String
        :param LogicalHardInodes: Inodes硬阈值，正整数。仅LogicalInodesTypee取值为limit时支持设置该参数。仅KPFS性能型支持。

单位：个。

        :type PathPrefix: Long
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None
        self.LogicalCapacityType = None
        self.LogicalHardThreshold = None
        self.LogicalInodesType = None
        self.LogicalHardInodes = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("LogicalCapacityType"):
            self.LogicalCapacityType = params.get("LogicalCapacityType")
        if params.get("LogicalHardThreshold"):
            self.LogicalHardThreshold = params.get("LogicalHardThreshold")
        if params.get("LogicalInodesType"):
            self.LogicalInodesType = params.get("LogicalInodesType")
        if params.get("LogicalHardInodes"):
            self.LogicalHardInodes = params.get("LogicalHardInodes")


class DescribeSubDirListRequest(AbstractModel):
    """DescribeSubDirList请求参数结构体
    """

    def __init__(self):
        r"""查询文件系统目录列表
        :param FileSystemId: 指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)。

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型 取值：

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型）
        :type PathPrefix: String
        :param ClusterName: 存储池名称，

从控制台>文件系统详情>资源池获取
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式 dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/

文件系统传入：/

目录传入路径：dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/

目录最大深度255层，根目录是第一层
        :type PathPrefix: String
        :param Name: 目录名称，支持模糊匹配。
        :type PathPrefix: String
        :param PageNum: 页码。默认为1。
        :type PathPrefix: Int
        :param PageSize: 分页大小。默认为1000，取值范围1-1000。
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None
        self.Name = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DeleteDirRequest(AbstractModel):
    """DeleteDir请求参数结构体
    """

    def __init__(self):
        r"""删除文件系统目录
        :param FileSystemId: 指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)。

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型 取值：

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型）
        :type PathPrefix: String
        :param ClusterName: 存储池名称，

从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式 dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/。

注意：

存储池、文件系统名称、目录完整路径不允许修改

必须与原目录相同。

若目录中有文件，无法删除。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")


class UpdateDirRequest(AbstractModel):
    """UpdateDir请求参数结构体
    """

    def __init__(self):
        r"""修改文件系统目录
        :param FileSystemId: 指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)。

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型 取值：

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型）
        :type PathPrefix: String
        :param ClusterName: 存储池名称，

从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式 dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/。

注意：

存储池、文件系统名称、目录完整路径不允许修改。

必须与原目录相同。
        :type PathPrefix: String
        :param FileSysPosixPermission: 文件读写权限，格式:十位二进制表示法。

备注：

默认为755 (-rwxr-xr-x)，拥有者有读、写、执行权限；而属组用户和其他用户只有读、执行权限。
        :type PathPrefix: Int
        :param FileSysOwnerUserId: 文件所属用户的id。

备注：

设置为0时，为root权限。

注意：

所属用户的id和所属用户的用户组id须同时修改。
        :type PathPrefix: Int
        :param FileSysOwnerGroupId: 文件所属用户的用户组id。

备注：

设置为0时，为root权限。

注意：

所属用户的id和所属用户的用户组id须同时修改。
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None
        self.FileSysPosixPermission = None
        self.FileSysOwnerUserId = None
        self.FileSysOwnerGroupId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("FileSysPosixPermission"):
            self.FileSysPosixPermission = params.get("FileSysPosixPermission")
        if params.get("FileSysOwnerUserId"):
            self.FileSysOwnerUserId = params.get("FileSysOwnerUserId")
        if params.get("FileSysOwnerGroupId"):
            self.FileSysOwnerGroupId = params.get("FileSysOwnerGroupId")


class CreateDirRequest(AbstractModel):
    """CreateDir请求参数结构体
    """

    def __init__(self):
        r"""新建文件系统目录
        :param FileSystemId: 指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)。

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型 取值：

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型）
        :type PathPrefix: String
        :param ClusterName: 存储池名称，

从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式 dir/xxx 或 /dir/××× 或 dir/×××/或/dir/×××/。

限制：

创建目录的上一层目录必须存在，系统不会自动创建，不存在则报错: $path dose not exist。

若目录中包含/，系统会自动用/将目录分层，报错信息同上。

补充说明：

针对目录名称的限制如下：

不能超过255字节（UTF8编码）。

不能创建/和隐藏目录。

针对完整路径(文件系统名:/dir)：最大4091字节（UTF8编码）。最大支持255层。
        :type PathPrefix: String
        :param FileSysOwnerUserId: 文件所属用户的id，不可设置负数。

有效值范围：0- （不校验范围）。

备注：

设置为0时，为root权限。

UID和GID必须同时配置，或皆不配置。否则会报错。
        :type PathPrefix: Int
        :param FileSysOwnerGroupId: 文件所属用户的用户组id，不可设置负数。

有效值范围：0- (不校验范围）。

备注：

设置为0时，为root权限。

UID和GID必须同时配置，或皆不配置。否则会报错。
        :type PathPrefix: Int
        :param FileSysPosixPermission: 文件读写权限，格式:十位二进制表示法。

备注：

默认为755 (-rwxr-xr-x)，拥有者有读、写、执行权限；而属组用户和其他用户只有读、执行权限。
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None
        self.FileSysOwnerUserId = None
        self.FileSysOwnerGroupId = None
        self.FileSysPosixPermission = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("FileSysOwnerUserId"):
            self.FileSysOwnerUserId = params.get("FileSysOwnerUserId")
        if params.get("FileSysOwnerGroupId"):
            self.FileSysOwnerGroupId = params.get("FileSysOwnerGroupId")
        if params.get("FileSysPosixPermission"):
            self.FileSysPosixPermission = params.get("FileSysPosixPermission")


class DescribeDirQuotaRequest(AbstractModel):
    """DescribeDirQuota请求参数结构体
    """

    def __init__(self):
        r"""查询指定目录配额
        :param FileSystemId: 文件系统的实例ID

性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，文件系统信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。

容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：

通过文件系统ID(FileSystemId)

输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型，取值：

KPFS-capacity（容量Ⅰ型）

KPFS-capacity2（容量Ⅱ型）

KPFS-standard（标准型）

KPFS-P-S01（性能Ⅰ型）

KPFS-P-S02（性能Ⅱ型）
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx或 /dir/xxx 或 dir/xxx/或/dir/×××/，匹配到 /dir/xxx/。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")


class DeleteFileSystemRequest(AbstractModel):
    """DeleteFileSystem请求参数结构体
    """

    def __init__(self):
        r"""删除文件系统
        :param FileSystemId: 文件系统实例ID
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class AddPerformanceOnePosixAclIpRequest(AbstractModel):
    """AddPerformanceOnePosixAclIp请求参数结构体
    """

    def __init__(self):
        r"""添加POSIX协议访问授权IP
        :param PosixAclId: POSIX访问授权规则ID
        :type PathPrefix: String
        :param Ip: 授权IP，支持单个/逗号分隔批量，单次最多100个IP
        :type PathPrefix: String
        """
        self.PosixAclId = None
        self.Ip = None

    def _deserialize(self, params):
        if params.get("PosixAclId"):
            self.PosixAclId = params.get("PosixAclId")
        if params.get("Ip"):
            self.Ip = params.get("Ip")


class RemovePerformanceOnePosixAclIpRequest(AbstractModel):
    """RemovePerformanceOnePosixAclIp请求参数结构体
    """

    def __init__(self):
        r"""移除POSIX协议访问授权IP
        :param PosixAclId: POSIX访问授权规则ID
        :type PathPrefix: String
        :param Ip: 待移除IP，支持单个/逗号分隔批量，单次最多100个IP；移除后无IP则自动删除授权规则
        :type PathPrefix: String
        """
        self.PosixAclId = None
        self.Ip = None

    def _deserialize(self, params):
        if params.get("PosixAclId"):
            self.PosixAclId = params.get("PosixAclId")
        if params.get("Ip"):
            self.Ip = params.get("Ip")


class GetDataMigrateTaskProgressRequest(AbstractModel):
    """GetDataMigrateTaskProgress请求参数结构体
    """

    def __init__(self):
        r"""获取数据流转任务进度
        :param TaskId: 数据流动任务ID
        :type PathPrefix: String
        """
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class DescribeDataMigrateTaskListRequest(AbstractModel):
    """DescribeDataMigrateTaskList请求参数结构体
    """

    def __init__(self):
        r"""获取数据流转任务列表
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param TaskIds: 数据流动任务ID清单，以逗号分隔，支持批量精确检索
        :type PathPrefix: String
        :param TaskName: 数据流动任务名称，模糊检索
        :type PathPrefix: String
        :param TaskType: 数据流动任务类型，有效值：export：导出
        :type PathPrefix: String
        :param DirPath: 目录路径，模糊检索 /aaa/bbb/
        :type PathPrefix: String
        :param Bucket: 存储桶名称，模糊检索
        :type PathPrefix: String
        :param BucketPrefix: 存储桶前缀，模糊检索/aaa/bbb/
        :type PathPrefix: String
        :param PageNum: 页码，默认为1
        :type PathPrefix: Int
        :param PageSize: 分页大小，默认为10
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.TaskIds = None
        self.TaskName = None
        self.TaskType = None
        self.DirPath = None
        self.Bucket = None
        self.BucketPrefix = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("TaskIds"):
            self.TaskIds = params.get("TaskIds")
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")
        if params.get("TaskType"):
            self.TaskType = params.get("TaskType")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("Bucket"):
            self.Bucket = params.get("Bucket")
        if params.get("BucketPrefix"):
            self.BucketPrefix = params.get("BucketPrefix")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class StartDataMigrateTaskRequest(AbstractModel):
    """StartDataMigrateTask请求参数结构体
    """

    def __init__(self):
        r"""启动数据流转任务
        :param TaskId: 数据流动任务ID
        :type PathPrefix: String
        """
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class StopDataMigrateTaskRequest(AbstractModel):
    """StopDataMigrateTask请求参数结构体
    """

    def __init__(self):
        r"""停止数据流转任务
        :param TaskId: 数据流动任务ID
        :type PathPrefix: String
        """
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class DeleteDataMigrateTaskRequest(AbstractModel):
    """DeleteDataMigrateTask请求参数结构体
    """

    def __init__(self):
        r"""删除数据流转任务
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param TaskIds: 数据流动任务ID清单，以逗号分隔，支持批量删除
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.TaskIds = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("TaskIds"):
            self.TaskIds = params.get("TaskIds")


class UpdateDataMigrateTaskRequest(AbstractModel):
    """UpdateDataMigrateTask请求参数结构体
    """

    def __init__(self):
        r"""修改数据流转任务
        :param TaskId: 数据流动任务ID
        :type PathPrefix: String
        :param TaskName: 数据流动任务名称，支持1-63字符，仅允许字母、数字和下划线 '_'，必须以字母开头。
        :type PathPrefix: String
        :param DirPath: 完整目录路径，1~950字节，格式：/dir/test/，目录必须存在
        :type PathPrefix: String
        :param Description: 数据流动策略描述
        :type PathPrefix: String
        :param BandWidthLimit: 带宽限制，单位MB/s，默认为0，不限制。有效值范围：0~{文件系统吞吐峰值}MB/s，0表示不限制
        :type PathPrefix: Int
        :param CleanSourceFile: 迁移完成后，是否删除源的数据。有效值：true，false（默认值）
        :type PathPrefix: Boolean
        :param ExportTaskPeriodEnabled: 数据流动任务状态，支持周期性任务立即或稍后启用，有效值：on：启用，off：禁用（默认值）
        :type PathPrefix: String
        :param ExportTaskPeriodConfig: 仅导出周期任务需要设置
        :type PathPrefix: Object
        """
        self.TaskId = None
        self.TaskName = None
        self.DirPath = None
        self.Description = None
        self.BandWidthLimit = None
        self.CleanSourceFile = None
        self.ExportTaskPeriodEnabled = None
        self.ExportTaskPeriodConfig = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("BandWidthLimit"):
            self.BandWidthLimit = params.get("BandWidthLimit")
        if params.get("CleanSourceFile"):
            self.CleanSourceFile = params.get("CleanSourceFile")
        if params.get("ExportTaskPeriodEnabled"):
            self.ExportTaskPeriodEnabled = params.get("ExportTaskPeriodEnabled")
        if params.get("ExportTaskPeriodConfig"):
            self.ExportTaskPeriodConfig = params.get("ExportTaskPeriodConfig")


class CreateDataMigrateTaskRequest(AbstractModel):
    """CreateDataMigrateTask请求参数结构体
    """

    def __init__(self):
        r"""创建数据流转任务
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param TaskName: 数据流动任务名称，支持1-63字符，仅允许字母、数字和下划线 '_'，必须以字母开头。
        :type PathPrefix: String
        :param TaskType: 数据流动任务类型，有效值：export：导出（从KPFS迁移数据到KS3）
        :type PathPrefix: String
        :param BucketConfig: 金山云对象存储KS3配置
        :type PathPrefix: Object
        :param DirPath: 完整目录路径，1~950字节，格式：/dir/test/，目录必须存在
        :type PathPrefix: String
        :param Description: 数据流动策略描述
        :type PathPrefix: String
        :param BandWidthLimit: 带宽限制，单位MB/s，默认为0，不限制。有效值范围：0~{文件系统吞吐峰值      }MB/s，0表示不限制
        :type PathPrefix: Int
        :param CleanSourceFile: 迁移完成后，是否删除源的数据。有效值：true，false（默认值）
        :type PathPrefix: Boolean
        :param ExportTaskPeriodEnabled: 数据流动任务状态，支持周期性任务立即或稍后启用，有效值：on：启用，off：禁用（默认值）
        :type PathPrefix: String
        :param ExportTaskPeriodConfig: 仅导出周期任务需要设置
        :type PathPrefix: Object
        """
        self.FileSystemId = None
        self.TaskName = None
        self.TaskType = None
        self.BucketConfig = None
        self.DirPath = None
        self.Description = None
        self.BandWidthLimit = None
        self.CleanSourceFile = None
        self.ExportTaskPeriodEnabled = None
        self.ExportTaskPeriodConfig = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")
        if params.get("TaskType"):
            self.TaskType = params.get("TaskType")
        if params.get("BucketConfig"):
            self.BucketConfig = params.get("BucketConfig")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("BandWidthLimit"):
            self.BandWidthLimit = params.get("BandWidthLimit")
        if params.get("CleanSourceFile"):
            self.CleanSourceFile = params.get("CleanSourceFile")
        if params.get("ExportTaskPeriodEnabled"):
            self.ExportTaskPeriodEnabled = params.get("ExportTaskPeriodEnabled")
        if params.get("ExportTaskPeriodConfig"):
            self.ExportTaskPeriodConfig = params.get("ExportTaskPeriodConfig")


class DescribeClientInstallInfoRequest(AbstractModel):
    """DescribeClientInstallInfo请求参数结构体
    """

    def __init__(self):
        r"""查询文件系统POSIX客户端安装包信息
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class ManageDataFlowTaskRequest(AbstractModel):
    """ManageDataFlowTask请求参数结构体
    """

    def __init__(self):
        r"""变更数据流动任务
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param StrategyId: 数据流动策略ID。
        :type PathPrefix: String
        :param TaskId: 数据流动任务ID。
        :type PathPrefix: String
        :param Operation: • 停止：pause，运行中状态的任务，支持停止，停止后变为暂停状态。
• 恢复：resume，暂停状态的任务，支持恢复，恢复后变为运行中状态
• 取消: cancel，运行中、暂停、等待状态的任务，支持取消，取消后变为完成状态
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StrategyId = None
        self.TaskId = None
        self.Operation = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("Operation"):
            self.Operation = params.get("Operation")


class CreateDataFlowStrategyRequest(AbstractModel):
    """CreateDataFlowStrategy请求参数结构体
    """

    def __init__(self):
        r"""创建数据流动策略
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param StrategyName: 数据流动策略名称，最大64字符。
        :type PathPrefix: String
        :param StrategyType: 数据流动策略类型
• 若为KPFS-P1存储池类型，有效值：import 导入。
• 若为KPFS-P2存储池类型，有效值：import 导入、export 导出。
        :type PathPrefix: String
        :param Bind: 数据流动是否启用绑定目录关系，启用绑定目录关系后文件侧的文件会和对象侧的文件进行关联，可以支持仅元数据加载、订阅模式。仅KPFS-P1存储池类型支持。
• false：默认值，表示禁用。
• true：启用绑定目录关系。
        :type PathPrefix: String
        :param DataLoadingMode: 数据导入加载模式，仅import导入策略可设置。
• 若为KPFS-P1存储池类型，有效值
    ◦ data_and_metadata - 元数据+数据加载。
    ◦ metadata_only - 仅元数据加载。仅当Bind为true时可支持。
• 若为KPFS-P2存储池类型，有效值
    ◦ demand - 按需加载（即仅元数据加载）。
    ◦ preload-预加载（即元数据+数据加载）。
        :type PathPrefix: String
        :param DirPath: 文件系统目录完整绝对路径，若不设置，则代表整个文件系统。
• 支持中英文字母、特殊字符不做限制，且不允许出现连续的/，必须以/开头和结尾。
• KPFS文件系统目录不能与其它导入策略存在重复。
• KPFS文件系统目录要求必须存在。
• 当Bind为true时，目录必须为空，且不能与其他导入策略的目录存在嵌套（如/dir/、/dir/subdir）。
        :type PathPrefix: String
        :param Bucket: KS3 Bucket名称，必须与KPFS实例在相同地域，3~63个字符，只能包含小写字母、数字和连字符（-），且不能以连字符（-）开头或结尾。
        :type PathPrefix: String
        :param BucketPrefix: KS3 Bucket前缀，若不设置，则代表整个存储桶。
• 1~1023个字符，不能包含"@"、“..”"@base@"和"@style@"。
• KS3存储桶前缀不能与其它任务存在重复。
        :type PathPrefix: String
        :param DuplicateProcess: 同名文件处理方式。仅KPFS-P1存储池类型支持。
• skip：跳过，默认值。
• overwrite：覆盖。
• diff：比较，保留最后修改时间最新的文件。
        :type PathPrefix: String
        :param Subscribe: 是否立即订阅。仅当Bind为true时可支持。仅KPFS-P1存储池类型支持。
• cancel：默认值，表示取消订阅。
• activate：表示开启订阅。
        :type PathPrefix: String
        :param CleanSourceFile: 导出完成后，是否删除源的数据，仅export导出策略可设置。仅KPFS-P2存储池类型支持。
• true：删除数据
• false：不删除，默认值。
        :type PathPrefix: Boolean
        :param BandWidthLimit: 导入/导出任务的执行速率，仅KPFS-P2存储池类型支持。
• low：业务优先，默认值。
• mid：均衡。
• high：导入优先。
        :type PathPrefix: String
        :param ArchiveRule: 数据流动导出策略的过滤规则，仅export导出策略可设置。仅KPFS-P2存储池类型支持。默认值0，有效值0-365。
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.StrategyName = None
        self.StrategyType = None
        self.Bind = None
        self.DataLoadingMode = None
        self.DirPath = None
        self.Bucket = None
        self.BucketPrefix = None
        self.DuplicateProcess = None
        self.Subscribe = None
        self.CleanSourceFile = None
        self.BandWidthLimit = None
        self.ArchiveRule = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyName"):
            self.StrategyName = params.get("StrategyName")
        if params.get("StrategyType"):
            self.StrategyType = params.get("StrategyType")
        if params.get("Bind"):
            self.Bind = params.get("Bind")
        if params.get("DataLoadingMode"):
            self.DataLoadingMode = params.get("DataLoadingMode")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("Bucket"):
            self.Bucket = params.get("Bucket")
        if params.get("BucketPrefix"):
            self.BucketPrefix = params.get("BucketPrefix")
        if params.get("DuplicateProcess"):
            self.DuplicateProcess = params.get("DuplicateProcess")
        if params.get("Subscribe"):
            self.Subscribe = params.get("Subscribe")
        if params.get("CleanSourceFile"):
            self.CleanSourceFile = params.get("CleanSourceFile")
        if params.get("BandWidthLimit"):
            self.BandWidthLimit = params.get("BandWidthLimit")
        if params.get("ArchiveRule"):
            self.ArchiveRule = params.get("ArchiveRule")


class DescribeDataFlowTaskListRequest(AbstractModel):
    """DescribeDataFlowTaskList请求参数结构体
    """

    def __init__(self):
        r"""查看数据流动任务
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param StrategyId: 数据流动策略ID。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StrategyId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")


class ActivateDataFlowTaskRequest(AbstractModel):
    """ActivateDataFlowTask请求参数结构体
    """

    def __init__(self):
        r"""启动数据流动导入任务
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param StrategyId: 数据流动策略ID。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StrategyId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")


class DeleteDataFlowStrategyRequest(AbstractModel):
    """DeleteDataFlowStrategy请求参数结构体
    """

    def __init__(self):
        r"""删除数据流动策略
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param StrategyId: 数据流动策略ID。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StrategyId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")


class DescribeDataFlowStrategyListRequest(AbstractModel):
    """DescribeDataFlowStrategyList请求参数结构体
    """

    def __init__(self):
        r"""创建数据流动列表
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param StrategyId: 数据流动策略ID
        :type PathPrefix: String
        :param PageNum: 页码。默认为1。
        :type PathPrefix: Int
        :param PageSize: 分页大小。默认为10。取值范围1-1000。
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.StrategyId = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class CleanRecycledFilesRequest(AbstractModel):
    """CleanRecycledFiles请求参数结构体
    """

    def __init__(self):
        r"""清空回收站数据
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class DeleteCleanRecycledFilesRequest(AbstractModel):
    """DeleteCleanRecycledFiles请求参数结构体
    """

    def __init__(self):
        r"""清空回收站文件
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class DeleteRecycleBinConfigRequest(AbstractModel):
    """DeleteRecycleBinConfig请求参数结构体
    """

    def __init__(self):
        r"""删除回收站配置
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class DeleteRecycledFileListRequest(AbstractModel):
    """DeleteRecycledFileList请求参数结构体
    """

    def __init__(self):
        r"""删除回收站配置
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class GetRecycleBinConfigRequest(AbstractModel):
    """GetRecycleBinConfig请求参数结构体
    """

    def __init__(self):
        r"""获取回收站配置
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class SetRecycleBinConfigRequest(AbstractModel):
    """SetRecycleBinConfig请求参数结构体
    """

    def __init__(self):
        r"""设置回收站配置
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param Enabled: 回收站状态
• on：启用回收站
• off：关闭回收站
        :type PathPrefix: String
        :param ExpireTime: 回收站中文件的保留时间。若启用回收站，则必传
• 容量型&标准型限制1-30天
• 性能型限制1-720小时
        :type PathPrefix: Int
        :param ExpireType: 过期时间类型
• DAY：天
• HOUR:小时（仅性能型支持）
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.Enabled = None
        self.ExpireTime = None
        self.ExpireType = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("Enabled"):
            self.Enabled = params.get("Enabled")
        if params.get("ExpireTime"):
            self.ExpireTime = params.get("ExpireTime")
        if params.get("ExpireType"):
            self.ExpireType = params.get("ExpireType")


class DescribeRecycledFileListRequest(AbstractModel):
    """DescribeRecycledFileList请求参数结构体
    """

    def __init__(self):
        r"""查看回收站中文件
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param RecycledPath: • 容量型/标准型：支持按路径关键字进行搜索
• 性能型：支持根据文件所在回收站目录搜索
        :type PathPrefix: String
        :param PageNum: 分页大小，默认1
        :type PathPrefix: Int
        :param PageSize: 分页起始位置，默认1000。取值范围：1-1000
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.RecycledPath = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("RecycledPath"):
            self.RecycledPath = params.get("RecycledPath")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DeleteRecycledFilesRequest(AbstractModel):
    """DeleteRecycledFiles请求参数结构体
    """

    def __init__(self):
        r"""删除回收站中文件
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param RecycledPath: 回收站的相对地址，仅性能型支持
        :type PathPrefix: String
        :param Files: 文件信息
        :type PathPrefix: Array
        :param Inodes: 文件Inode值数据，该参数与Position参数二选一，仅容量型/标准型支持
        :type PathPrefix: Array
        """
        self.FileSystemId = None
        self.RecycledPath = None
        self.Files = None
        self.Inodes = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("RecycledPath"):
            self.RecycledPath = params.get("RecycledPath")
        if params.get("Files"):
            self.Files = params.get("Files")
        if params.get("Inodes"):
            self.Inodes = params.get("Inodes")


class RestoreRecycledFilesRequest(AbstractModel):
    """RestoreRecycledFiles请求参数结构体
    """

    def __init__(self):
        r"""恢复回收站中文件
        :param FileSystemId: 文件系统ID
        :type PathPrefix: String
        :param RecycledPath: 回收站的相对地址，仅性能型支持
        :type PathPrefix: String
        :param Files: 文件信息
        :type PathPrefix: Array
        :param Inodes: 文件Inode值数据，该参数与Position参数二选一，仅容量型/标准型支持

        :type PathPrefix: Array
        """
        self.FileSystemId = None
        self.RecycledPath = None
        self.Files = None
        self.Inodes = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("RecycledPath"):
            self.RecycledPath = params.get("RecycledPath")
        if params.get("Files"):
            self.Files = params.get("Files")
        if params.get("Inodes"):
            self.Inodes = params.get("Inodes")


class DescribeClusterInfoRequest(AbstractModel):
    """DescribeClusterInfo请求参数结构体
    """

    def __init__(self):
        r"""查询可用存储集群信息
        :param Region: 查询对应地域下支持的存储池类型。
        :type PathPrefix: String
        :param AvailZone: 可用区，需与地域参数配合使用。
        :type PathPrefix: String
        :param StoreClass: 文件系统存储类型。
        :type PathPrefix: String
        :param SRoceCluster: 存储RoCE集群名称，仅性能Ⅰ型、性能Ⅱ型支持。传入后返回对应集群下的存储集群信息。
        :type PathPrefix: String
        :param StorePoolType: 存储池类型。
        :type PathPrefix: String
        """
        self.Region = None
        self.AvailZone = None
        self.StoreClass = None
        self.SRoceCluster = None
        self.StorePoolType = None

    def _deserialize(self, params):
        if params.get("Region"):
            self.Region = params.get("Region")
        if params.get("AvailZone"):
            self.AvailZone = params.get("AvailZone")
        if params.get("StoreClass"):
            self.StoreClass = params.get("StoreClass")
        if params.get("SRoceCluster"):
            self.SRoceCluster = params.get("SRoceCluster")
        if params.get("StorePoolType"):
            self.StorePoolType = params.get("StorePoolType")


class UpdatePerformanceNfsAclIpRequest(AbstractModel):
    """UpdatePerformanceNfsAclIp请求参数结构体
    """

    def __init__(self):
        r"""编辑NFS访问授权客户端
        :param NfsAclId: 访问授权ID。
        :type PathPrefix: String
        :param Ips: 授权IP列表，单次最多编辑20个。
        :type PathPrefix: Array
        """
        self.NfsAclId = None
        self.Ips = None

    def _deserialize(self, params):
        if params.get("NfsAclId"):
            self.NfsAclId = params.get("NfsAclId")
        if params.get("Ips"):
            self.Ips = params.get("Ips")


class RemovePerformanceNfsAclClientRequest(AbstractModel):
    """RemovePerformanceNfsAclClient请求参数结构体
    """

    def __init__(self):
        r"""删除NFS访问授权客户端
        :param NfsAclId: 访问授权ID。
        :type PathPrefix: String
        :param Ips: 授权IP列表，单次最多删除100个。支持IP和网段格式。
        :type PathPrefix: Array
        """
        self.NfsAclId = None
        self.Ips = None

    def _deserialize(self, params):
        if params.get("NfsAclId"):
            self.NfsAclId = params.get("NfsAclId")
        if params.get("Ips"):
            self.Ips = params.get("Ips")


class AddPerformanceNfsAclClientRequest(AbstractModel):
    """AddPerformanceNfsAclClient请求参数结构体
    """

    def __init__(self):
        r"""添加NFS访问授权客户端
        :param NfsAclId: 访问授权ID。
        :type PathPrefix: String
        :param Ips: 授权IP列表（计算节点私网IP，单次最多100个）。
        :type PathPrefix: Array
        """
        self.NfsAclId = None
        self.Ips = None

    def _deserialize(self, params):
        if params.get("NfsAclId"):
            self.NfsAclId = params.get("NfsAclId")
        if params.get("Ips"):
            self.Ips = params.get("Ips")


class DeletePerformanceOneNfsAclRequest(AbstractModel):
    """DeletePerformanceOneNfsAcl请求参数结构体
    """

    def __init__(self):
        r"""删除NFS协议访问授权
        :param NfsAclId: 规则ID。
        :type PathPrefix: String
        """
        self.NfsAclId = None

    def _deserialize(self, params):
        if params.get("NfsAclId"):
            self.NfsAclId = params.get("NfsAclId")


class SetPerformanceOneNfsAclRequest(AbstractModel):
    """SetPerformanceOneNfsAcl请求参数结构体
    """

    def __init__(self):
        r"""新建NFS协议访问授权
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param ExportPath: 共享目录路径。格式：整个文件系统不传或传/；子目录支持dir/xxx、/dir/xxx、dir/xxx/、/dir/xxx/。
        :type PathPrefix: String
        :param Ips: 授权IP列表（计算节点私网IP，单次最多100个）。
        :type PathPrefix: Array
        :param Desc: 规则描述信息，0-63字符。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.ExportPath = None
        self.Ips = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("ExportPath"):
            self.ExportPath = params.get("ExportPath")
        if params.get("Ips"):
            self.Ips = params.get("Ips")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class DescribePerformanceOneNfsAclListRequest(AbstractModel):
    """DescribePerformanceOneNfsAclList请求参数结构体
    """

    def __init__(self):
        r"""查询NFS协议访问授权
        :param FileSystemName: 文件系统名称。
        :type PathPrefix: String
        :param NfsAclId: 规则ID。
        :type PathPrefix: String
        :param PageNum: 页码。默认为1。
        :type PathPrefix: Long
        :param PageSize: 分页大小。默认为10。
        :type PathPrefix: Long
        """
        self.FileSystemName = None
        self.NfsAclId = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("NfsAclId"):
            self.NfsAclId = params.get("NfsAclId")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DescribeFileSystemNfsClientInfoRequest(AbstractModel):
    """DescribeFileSystemNfsClientInfo请求参数结构体
    """

    def __init__(self):
        r"""查询特定文件系统的NFS客户端信息
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param PageNum: 页码 默认值1
        :type PathPrefix: Int
        :param PageSize: 分页大小 默认值1000 可选1-1000
        :type PathPrefix: Int
        :param Action: 该参数为公共参数，本接口取值如下：DescribeFileSystemNfsClientInfo。
        :type PathPrefix: String
        :param Version: 该参数为公共参数，取值：2024-09-30。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.PageNum = None
        self.PageSize = None
        self.Action = None
        self.Version = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")


class SetFileSystemResourceProtectRequest(AbstractModel):
    """SetFileSystemResourceProtect请求参数结构体
    """

    def __init__(self):
        r"""设置文件系统删除保护
        :param FileSystemIds: 待修改实例保护的文件系统实例ID列表
        :type PathPrefix: Array
        :param IsProtection: 是否打开资源保护，默认不开启
• TRUE ：表示开启资源删除保护
• FALSE（默认）：表示不开启资源删除保护

        :type PathPrefix: Boolean
        """
        self.FileSystemIds = None
        self.IsProtection = None

    def _deserialize(self, params):
        if params.get("FileSystemIds"):
            self.FileSystemIds = params.get("FileSystemIds")
        if params.get("IsProtection"):
            self.IsProtection = params.get("IsProtection")


class DescribeFileDeletePolicyListRequest(AbstractModel):
    """DescribeFileDeletePolicyList请求参数结构体
    """

    def __init__(self):
        r"""查看列表-删除策略
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        :param DeletePolicyStatus: • 已生效：Enabled
• 已禁用：Disabled
• 已失效：Expired
        :type PathPrefix: String
        :param DirPath: 目录绝对路径
        :type PathPrefix: String
        :param FileDeletePolicyId: 文件删除策略ID，中间用“,”隔开，注意：URL参数中如果存在此类特殊符号，需要使用URLEncoder来进行编码
        :type PathPrefix: Array
        :param PageNum: 当前页码，默认值1
        :type PathPrefix: Int
        :param PageSize: 每页数量，值范围：1-1000，默认值：1000
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.DeletePolicyStatus = None
        self.DirPath = None
        self.FileDeletePolicyId = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("DeletePolicyStatus"):
            self.DeletePolicyStatus = params.get("DeletePolicyStatus")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("FileDeletePolicyId"):
            self.FileDeletePolicyId = params.get("FileDeletePolicyId")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class EnableFileDeletePolicyRequest(AbstractModel):
    """EnableFileDeletePolicy请求参数结构体
    """

    def __init__(self):
        r"""启用-删除策略
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        :param FileDeletePolicyId: 文件删除策略ID
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.FileDeletePolicyId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("FileDeletePolicyId"):
            self.FileDeletePolicyId = params.get("FileDeletePolicyId")


class DisableFileDeletePolicyRequest(AbstractModel):
    """DisableFileDeletePolicy请求参数结构体
    """

    def __init__(self):
        r"""禁用-删除策略
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        :param FileDeletePolicyId: 文件删除策略ID
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.FileDeletePolicyId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("FileDeletePolicyId"):
            self.FileDeletePolicyId = params.get("FileDeletePolicyId")


class DescribeFileDeletePolicyRequest(AbstractModel):
    """DescribeFileDeletePolicy请求参数结构体
    """

    def __init__(self):
        r"""查看-删除策略详情
        :param FileDeletePolicyId: 文件删除策略ID
        :type PathPrefix: String
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        """
        self.FileDeletePolicyId = None
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileDeletePolicyId"):
            self.FileDeletePolicyId = params.get("FileDeletePolicyId")
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class DeleteFileDeletePolicyRequest(AbstractModel):
    """DeleteFileDeletePolicy请求参数结构体
    """

    def __init__(self):
        r"""删除-删除策略
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        :param FileDeletePolicyId: 文件删除策略ID
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.FileDeletePolicyId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("FileDeletePolicyId"):
            self.FileDeletePolicyId = params.get("FileDeletePolicyId")


class UpdateFileDeletePolicyRequest(AbstractModel):
    """UpdateFileDeletePolicy请求参数结构体
    """

    def __init__(self):
        r"""修改删除策略
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        :param FileDeletePolicyId: 文件删除策略ID
        :type PathPrefix: String
        :param FileDeletePolicyName: 文件删除策略名称
格式要求：允许字符长度:1-63，允许包含一下字符:数字 字母 + = . @ _ -，不能以 . 字符开头
        :type PathPrefix: String
        :param ExecutionType: 执行类型
有效值：
• 周期执行：CycleExecution
• 立即执行：ImmediateExecution
• 默认：CycleExecution
        :type PathPrefix: String
        :param FrequencyUnit: 文件删除策略执行频率。
有效值：
• day：按天
• week：按周
• month：按月
        :type PathPrefix: String
        :param IndexOfFrequency: 文件删除策略执行日期。
• 按天不传
• 按周（必传） （1-7  可多选）
• 按月（必传）（1-30）[1，2，3，4，5]
        :type PathPrefix: Array
        :param FrequencyTimePoints: 文件删除策略定期执行时间点，只支持小时（整点）
        :type PathPrefix: Array
        :param FileNameRule: 文件名过滤规则
        :type PathPrefix: Object
        :param FileSizeRule: 文件大小过滤规则
        :type PathPrefix: Object
        :param TimeRuleParameters: 时间参数
        :type PathPrefix: Array
        :param Description: 文件删除策略备注信息
（限制）:允许字符长度:0-63，允许包含以下字符:数字 字母 中文 + = . @ _ -
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.FileDeletePolicyId = None
        self.FileDeletePolicyName = None
        self.ExecutionType = None
        self.FrequencyUnit = None
        self.IndexOfFrequency = None
        self.FrequencyTimePoints = None
        self.FileNameRule = None
        self.FileSizeRule = None
        self.TimeRuleParameters = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("FileDeletePolicyId"):
            self.FileDeletePolicyId = params.get("FileDeletePolicyId")
        if params.get("FileDeletePolicyName"):
            self.FileDeletePolicyName = params.get("FileDeletePolicyName")
        if params.get("ExecutionType"):
            self.ExecutionType = params.get("ExecutionType")
        if params.get("FrequencyUnit"):
            self.FrequencyUnit = params.get("FrequencyUnit")
        if params.get("IndexOfFrequency"):
            self.IndexOfFrequency = params.get("IndexOfFrequency")
        if params.get("FrequencyTimePoints"):
            self.FrequencyTimePoints = params.get("FrequencyTimePoints")
        if params.get("FileNameRule"):
            self.FileNameRule = params.get("FileNameRule")
        if params.get("FileSizeRule"):
            self.FileSizeRule = params.get("FileSizeRule")
        if params.get("TimeRuleParameters"):
            self.TimeRuleParameters = params.get("TimeRuleParameters")
        if params.get("Description"):
            self.Description = params.get("Description")


class CreateFileDeletePolicyRequest(AbstractModel):
    """CreateFileDeletePolicy请求参数结构体
    """

    def __init__(self):
        r"""新建-删除策略
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        :param FileDeletePolicyName: 文件删除策略名称
格式要求：允许字符长度:1-63，允许包含一下字符:数字 字母 + = . @ _ -，不能以 . 字符开头
        :type PathPrefix: String
        :param DirPath: 目录绝对路径
        :type PathPrefix: String
        :param ExecutionType: 执行类型
有效值：
• 周期执行：CycleExecution
• 立即执行：ImmediateExecution
• 默认：CycleExecution
        :type PathPrefix: String
        :param FrequencyUnit: 文件删除策略执行频率。
有效值：
• day：按天
• week：按周
• month：按月
        :type PathPrefix: String
        :param IndexOfFrequency: 文件删除策略执行日期。
• 按天不传
• 按周（必传） （1-7  可多选）
• 按月（必传）（1-30 可多选）
        :type PathPrefix: Array
        :param FrequencyTimePoints: 文件删除策略定期执行时间点，只支持小时（整点）
        :type PathPrefix: Array
        :param FileNameRule: 文件名过滤规则
        :type PathPrefix: Object
        :param FileSizeRule: 文件大小过滤规则
        :type PathPrefix: Object
        :param TimeRuleParameters: 时间参数
        :type PathPrefix: Array
        :param Description: 文件删除策略备注信息
（限制）:允许字符长度:0-63，允许包含以下字符:数字 字母 中文 + = . @ _ -
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.FileDeletePolicyName = None
        self.DirPath = None
        self.ExecutionType = None
        self.FrequencyUnit = None
        self.IndexOfFrequency = None
        self.FrequencyTimePoints = None
        self.FileNameRule = None
        self.FileSizeRule = None
        self.TimeRuleParameters = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("FileDeletePolicyName"):
            self.FileDeletePolicyName = params.get("FileDeletePolicyName")
        if params.get("DirPath"):
            self.DirPath = params.get("DirPath")
        if params.get("ExecutionType"):
            self.ExecutionType = params.get("ExecutionType")
        if params.get("FrequencyUnit"):
            self.FrequencyUnit = params.get("FrequencyUnit")
        if params.get("IndexOfFrequency"):
            self.IndexOfFrequency = params.get("IndexOfFrequency")
        if params.get("FrequencyTimePoints"):
            self.FrequencyTimePoints = params.get("FrequencyTimePoints")
        if params.get("FileNameRule"):
            self.FileNameRule = params.get("FileNameRule")
        if params.get("FileSizeRule"):
            self.FileSizeRule = params.get("FileSizeRule")
        if params.get("TimeRuleParameters"):
            self.TimeRuleParameters = params.get("TimeRuleParameters")
        if params.get("Description"):
            self.Description = params.get("Description")


class DescribeDataFlowStrategySubscribeRequest(AbstractModel):
    """DescribeDataFlowStrategySubscribe请求参数结构体
    """

    def __init__(self):
        r"""查看数据流动订阅记录
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param StrategyId: 数据流动策略ID。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StrategyId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")


class ManageDataFlowStrategySubscribeRequest(AbstractModel):
    """ManageDataFlowStrategySubscribe请求参数结构体
    """

    def __init__(self):
        r"""管理数据流动订阅
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param StrategyId: 数据流动策略ID。
        :type PathPrefix: String
        :param Operation: • activate：开启数据流动订阅，仅Subscribe为to_be_subscribed时支持
• cancel：取消数据流动订阅，仅Subscribe为subscribing时支持

        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StrategyId = None
        self.Operation = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")
        if params.get("Operation"):
            self.Operation = params.get("Operation")


class GetRemoteCachePutLatencyRequest(AbstractModel):
    """GetRemoteCachePutLatency请求参数结构体
    """

    def __init__(self):
        r"""分布式缓存组的分布式缓存发送数据延迟
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d。
（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param CacheGroup: 客户端所在缓存组。精确匹配。
        :type PathPrefix: String
        :param CacheGroupRole: 客户端所在缓存组中角色。精确匹配。
• consumer：代表消费者，即缓存组中的--no-sharing节点
• provider：代表提供者

        :type PathPrefix: String
        :param ClientNm: 客户端挂载信息。拼接规则为：HostName:MountPoint，如：vm10-0-0-116:/datapoint。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CacheGroup = None
        self.CacheGroupRole = None
        self.ClientNm = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CacheGroup"):
            self.CacheGroup = params.get("CacheGroup")
        if params.get("CacheGroupRole"):
            self.CacheGroupRole = params.get("CacheGroupRole")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")


class GetRemoteCacheGetLatencyRequest(AbstractModel):
    """GetRemoteCacheGetLatency请求参数结构体
    """

    def __init__(self):
        r"""分布式缓存组的分布式缓存读数据延迟
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d。
（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param CacheGroup: 客户端所在缓存组。精确匹配。
        :type PathPrefix: String
        :param CacheGroupRole: 客户端所在缓存组中角色。精确匹配。
• consumer：代表消费者，即缓存组中的--no-sharing节点
• provider：代表提供者

        :type PathPrefix: String
        :param ClientNm: 客户端挂载信息。拼接规则为：HostName:MountPoint，如：vm10-0-0-116:/datapoint。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CacheGroup = None
        self.CacheGroupRole = None
        self.ClientNm = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CacheGroup"):
            self.CacheGroup = params.get("CacheGroup")
        if params.get("CacheGroupRole"):
            self.CacheGroupRole = params.get("CacheGroupRole")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")


class GetRemoteCachePutThroughputRequest(AbstractModel):
    """GetRemoteCachePutThroughput请求参数结构体
    """

    def __init__(self):
        r"""分布式缓存组的分布式缓存发送数据吞吐
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d。
（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param CacheGroup: 客户端所在缓存组。精确匹配。
        :type PathPrefix: String
        :param CacheGroupRole: 客户端所在缓存组中角色。精确匹配。
• consumer：代表消费者，即缓存组中的--no-sharing节点
• provider：代表提供者

        :type PathPrefix: String
        :param ClientNm: 客户端挂载信息。拼接规则为：HostName:MountPoint，如：vm10-0-0-116:/datapoint。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CacheGroup = None
        self.CacheGroupRole = None
        self.ClientNm = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CacheGroup"):
            self.CacheGroup = params.get("CacheGroup")
        if params.get("CacheGroupRole"):
            self.CacheGroupRole = params.get("CacheGroupRole")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")


class GetRemoteCacheGetThroughputRequest(AbstractModel):
    """GetRemoteCacheGetThroughput请求参数结构体
    """

    def __init__(self):
        r"""分布式缓存组的分布式缓存读数据吞吐量
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d。
（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param CacheGroup: 客户端所在缓存组。精确匹配。
        :type PathPrefix: String
        :param CacheGroupRole: 客户端所在缓存组中角色。精确匹配。
• consumer：代表消费者，即缓存组中的--no-sharing节点
• provider：代表提供者
        :type PathPrefix: String
        :param ClientNm: 客户端挂载信息。拼接规则为：HostName:MountPoint，如：vm10-0-0-116:/datapoint。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CacheGroup = None
        self.CacheGroupRole = None
        self.ClientNm = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CacheGroup"):
            self.CacheGroup = params.get("CacheGroup")
        if params.get("CacheGroupRole"):
            self.CacheGroupRole = params.get("CacheGroupRole")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")


class GetRemoteCacheIOPSSendRequest(AbstractModel):
    """GetRemoteCacheIOPSSend请求参数结构体
    """

    def __init__(self):
        r"""分布式缓存组的分布式缓存发送数据请求数
        :param FileSystemId: 文件系统的实例ID。
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d。
（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param CacheGroup: 客户端所在缓存组。精确匹配。
        :type PathPrefix: String
        :param CacheGroupRole: 客户端所在缓存组中角色。精确匹配。
• consumer：代表消费者，即缓存组中的--no-sharing节点
• provider：代表提供者
        :type PathPrefix: String
        :param ClientNm: 客户端挂载信息。拼接规则为：HostName:MountPoint，如：vm10-0-0-116:/datapoint。
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CacheGroup = None
        self.CacheGroupRole = None
        self.ClientNm = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CacheGroup"):
            self.CacheGroup = params.get("CacheGroup")
        if params.get("CacheGroupRole"):
            self.CacheGroupRole = params.get("CacheGroupRole")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")


class GetRemoteCacheIOPSGetRequest(AbstractModel):
    """GetRemoteCacheIOPSGet请求参数结构体
    """

    def __init__(self):
        r"""分布式缓存组的分布式缓存读数据请求数
        :param FileSystemId: 文件系统的实例ID
        :type PathPrefix: String
        :param StartTime: 监控数据开始时间。格式为：时间戳，如：1732204800。
        :type PathPrefix: String
        :param EndTime: 监控数据截止时间。格式为：时间戳，如：1734797100。
        :type PathPrefix: String
        :param Interval: 监控数据统计颗粒度。有效值：1m、5m、10m、1h、1d。
（EndTime-StartTime）/ Interval 必须 ≤ 6000，否则接口会拦截报错。
        :type PathPrefix: String
        :param CacheGroup: 客户端所在缓存组。精确匹配。
        :type PathPrefix: String
        :param CacheGroupRole: 客户端所在缓存组中角色。精确匹配。
• consumer：代表消费者，即缓存组中的--no-sharing节点
• provider：代表提供者
        :type PathPrefix: String
        :param ClientNm: 客户端挂载信息。拼接规则为：HostName:MountPoint，如：vm10-0-0-116:/datapoin
        :type PathPrefix: String
        """
        self.FileSystemId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CacheGroup = None
        self.CacheGroupRole = None
        self.ClientNm = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CacheGroup"):
            self.CacheGroup = params.get("CacheGroup")
        if params.get("CacheGroupRole"):
            self.CacheGroupRole = params.get("CacheGroupRole")
        if params.get("ClientNm"):
            self.ClientNm = params.get("ClientNm")


class DescribeDataFlowStrategySubscribeFailedRequest(AbstractModel):
    """DescribeDataFlowStrategySubscribeFailed请求参数结构体
    """

    def __init__(self):
        r"""查看数据流动订阅失败事件
        :param FileSystemId: 文件系统ID。
        :type PathPrefix: String
        :param StrategyId: 数据流动策略ID。
        :type PathPrefix: String
        :param SubscribeId: 订阅ID。
        :type PathPrefix: String
        :param StartTime: 获取失败列表起始时间,取值：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param EndTime: 获取失败列表结束时间,取值：yyyy-MM-dd HH:mm:ss
查看最新的订阅失败，入参：endTime:--
        :type PathPrefix: String
        :param PageNum: 页码。默认为1。
        :type PathPrefix: Int
        :param PageSize: 分页大小。默认为10。取值范围1-1000。
        :type PathPrefix: Int
        """
        self.FileSystemId = None
        self.StrategyId = None
        self.SubscribeId = None
        self.StartTime = None
        self.EndTime = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("StrategyId"):
            self.StrategyId = params.get("StrategyId")
        if params.get("SubscribeId"):
            self.SubscribeId = params.get("SubscribeId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class ManageMigrateTaskRequest(AbstractModel):
    """ManageMigrateTask请求参数结构体
    """

    def __init__(self):
        r"""管理迁移任务
        :param TaskId: 数据迁移任务ID。
        :type PathPrefix: String
        :param Operation: 任务操作。pause：暂停任务（仅运行中支持）；resume：恢复任务（仅已暂停、异常中断支持）；close：关闭任务（仅运行中、异常中断支持）；delete：删除任务（仅已关闭、已完成、异常中断支持）；re_execute：重新执行任务（仅已完成支持）。
        :type PathPrefix: String
        """
        self.TaskId = None
        self.Operation = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("Operation"):
            self.Operation = params.get("Operation")


class DescribeMigrateTasksRequest(AbstractModel):
    """DescribeMigrateTasks请求参数结构体
    """

    def __init__(self):
        r"""查询迁移任务列表
        :param RuleId: 数据迁移规则ID。
        :type PathPrefix: String
        :param TaskId: 数据迁移任务ID。
        :type PathPrefix: String
        :param PageSize: 分页大小，默认为10。
        :type PathPrefix: Long
        :param PageNum: 页码，默认为1。
        :type PathPrefix: Long
        """
        self.RuleId = None
        self.TaskId = None
        self.PageSize = None
        self.PageNum = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")


class CreateMigrateTaskRequest(AbstractModel):
    """CreateMigrateTask请求参数结构体
    """

    def __init__(self):
        r"""创建迁移任务
        :param RuleId: 任务id（数据迁移规则ID）。
        :type PathPrefix: String
        :param SrcDirectory: 数据源存储下的相对路径（为数据迁移绑定关系中数据源存储目录或前缀下的相对路径）。若数据源存储为KS3，则限制为：1~1023个字符，不能包含"@"、".."、"@base@"和"@style@"，必须以/开头，不允许以/结尾。若数据源存储为KPFS，则必须以/开头，不允许以/结尾，且KPFS文件系统子目录要求必须存在。
        :type PathPrefix: String
        :param DstDirectory: 数据目标存储下的相对路径（为数据迁移绑定关系中数据目标存储目录或前缀下的相对路径）。若数据目标存储为KS3，则限制为：1~1023个字符，不能包含"@"、".."、"@base@"和"@style@"，必须以/开头，不允许以/结尾。若数据目标存储为KPFS，则必须以/开头，不允许以/结尾，且KPFS文件系统子目录要求必须存在。
        :type PathPrefix: String
        :param EntryList: 64KB，采用JSON格式。该参数仅数据源存储为KS3，数据目标存储为KPFS时支持。
若文件清单内存在源存储下不存在的文件，迁移时会忽略。
• 任务要同步的源数据为：BucketPrefix+SrcDirectory+EntryList
• 任务同步到目标的数据路径为：DirPath+DstDirectory+EntryList
        :type PathPrefix: Array
        """
        self.RuleId = None
        self.SrcDirectory = None
        self.DstDirectory = None
        self.EntryList = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("SrcDirectory"):
            self.SrcDirectory = params.get("SrcDirectory")
        if params.get("DstDirectory"):
            self.DstDirectory = params.get("DstDirectory")
        if params.get("EntryList"):
            self.EntryList = params.get("EntryList")


class DeleteMigrateRuleRequest(AbstractModel):
    """DeleteMigrateRule请求参数结构体
    """

    def __init__(self):
        r"""删除迁移规则
        :param RuleId: 数据迁移规则ID。
        :type PathPrefix: String
        """
        self.RuleId = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")


class DescribeMigrateRulesRequest(AbstractModel):
    """DescribeMigrateRules请求参数结构体
    """

    def __init__(self):
        r"""查询迁移规则列表
        :param RuleId: 数据迁移规则ID。
        :type PathPrefix: String
        :param Region: 地域信息。
        :type PathPrefix: String
        :param PageSize: 分页大小，默认为10。
        :type PathPrefix: Long
        :param PageNum: 页码，默认为1。
        :type PathPrefix: Long
        """
        self.RuleId = None
        self.Region = None
        self.PageSize = None
        self.PageNum = None

    def _deserialize(self, params):
        if params.get("RuleId"):
            self.RuleId = params.get("RuleId")
        if params.get("Region"):
            self.Region = params.get("Region")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")


class CreateMigrateRuleRequest(AbstractModel):
    """CreateMigrateRule请求参数结构体
    """

    def __init__(self):
        r"""创建迁移规则
        :param Name: 数据迁移名称，最大64字符。
        :type PathPrefix: String
        :param Region: 地域信息。
        :type PathPrefix: String
        :param SrcData: 数据源存储。数据源存储与数据目标存储必须在相同Region。
        :type PathPrefix: Object
        :param DstData: 数据目标存储。数据源存储与数据目标存储必须在相同Region。
        :type PathPrefix: Object
        """
        self.Name = None
        self.Region = None
        self.SrcData = None
        self.DstData = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Region"):
            self.Region = params.get("Region")
        if params.get("SrcData"):
            self.SrcData = params.get("SrcData")
        if params.get("DstData"):
            self.DstData = params.get("DstData")


