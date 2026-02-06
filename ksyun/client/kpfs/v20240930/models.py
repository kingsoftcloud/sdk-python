from ksyun.common.abstract_model import AbstractModel

class DescribeFileSystemListRequest(AbstractModel):
    """DescribeFileSystemList请求参数结构体
    """

    def __init__(self):
        r"""文件系统列表查询
        :param Region: 文件系统所在地域，不传则返回所有地域下文件系统。
        :type PathPrefix: String
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
        self.Region = None
        self.FileSystemName = None
        self.FileSystemIds = None
        self.StoreClasses = None
        self.ProjectId = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("Region"):
            self.Region = params.get("Region")
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
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。该参数仅支持华北3（呼和浩特）地域，且仅支持专属集群。
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
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。该参数仅支持华北3（呼和浩特）地域，且仅支持专属集群。
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
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。该参数仅支持华北3（呼和浩特）地域，且仅支持专属集群。
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
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。该参数仅支持华北3（呼和浩特）地域，且仅支持专属集群。
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
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。该参数仅支持华北3（呼和浩特）地域，且仅支持专属集群。
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
        :param VpcIp: NFS客户端的VpcIp。若您需要查询NFS客户端级的统计项，可根据VpcIp筛选。支持Ipv4，如：10.0.0.1。请参见查询文件系统NFS客户端信息。该参数仅支持华北3（呼和浩特）地域，且仅支持专属集群。
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


class DescribeDirQuotaListRequest(AbstractModel):
    """DescribeDirQuotaList请求参数结构体
    """

    def __init__(self):
        r"""查询目录配额列表
        :param FileSystemId: 文件系统的实例ID。性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：1.通过文件系统ID(FileSystemId)；2.输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：1.通过文件系统ID(FileSystemId)；2.输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型，取值：KPFS-capacity（容量Ⅰ型）、KPFS-capacity2（容量Ⅱ型）、KPFS-standard（标准型）、KPFS-P-S01（性能Ⅰ型）、KPFS-P-S02（性能Ⅱ型）。
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录路径模糊查询关键字，支持中间路径的模糊匹配，比如，存在目录配额/dir/subdir，查询关键字为subdir，那么会返回/dir/subdir的目录配额信息。注意：若不传入该参数，则返回文件系统下的目录配额列表。
        :type PathPrefix: String
        :param FuzzySearch: 是否模糊查询，默认 true；精确查询时，格式：dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/。
        :type PathPrefix: Boolean
        :param PageSize: 分页大小。默认为10。
        :type PathPrefix: Int
        :param PageNum: 页码。默认为1。
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
        :param FileSystemId: 文件系统的实例ID。性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：1. 通过文件系统ID(FileSystemId)；2. 输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：1. 通过文件系统ID(FileSystemId)；2. 输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/
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
        :param FileSystemId: 文件系统的实例ID。性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：1. 通过文件系统ID(FileSystemId)；2. 输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：1. 通过文件系统ID(FileSystemId)；2. 输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/。注意：1. 性能Ⅰ型/性能Ⅱ型存储池、文件系统名称、目录完整路径不允许修改，必须与原目录相同；2. 容量Ⅰ型/容量Ⅱ型/标准型，必须与原目录相同；3. 已设置目录配额的目录，才允许修改目录配额。
        :type PathPrefix: String
        :param LogicalHardThreshold: 容量硬阈值，不可超过文件系统容量配额，单位：Bytes
        :type PathPrefix: Long
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None
        self.LogicalHardThreshold = None

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
        if params.get("LogicalHardThreshold"):
            self.LogicalHardThreshold = params.get("LogicalHardThreshold")


class CreateDirQuotaRequest(AbstractModel):
    """CreateDirQuota请求参数结构体
    """

    def __init__(self):
        r"""新建目录配额
        :param FileSystemId: 文件系统的实例ID。性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：1.通过文件系统ID(FileSystemId)；2.输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：1.通过文件系统ID(FileSystemId)；2.输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型，取值：KPFS-capacity（容量Ⅰ型）、KPFS-capacity2（容量Ⅱ型）、KPFS-standard（标准型）、KPFS-P-S01（性能Ⅰ型）、KPFS-P-S02（性能Ⅱ型）。
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/。注意：1.性能Ⅰ型/性能Ⅱ型存储池、文件系统名称、目录完整路径不允许修改，必须与原目录相同；2.容量Ⅰ型/容量Ⅱ型/标准型，若目录不存在，接口会自动创建新目录；3.性能Ⅰ型/性能Ⅱ型，不支持为非空目录新增配额；4.无法为文件系统根目录设置配额，仅支持子目录；5.支持为各级目录设置配额，并且嵌套配额均取最小值作为该目录的阈值。比如：设置/dir配额为1MB，设置/dir/subdir配额为10MB，那么实际使用时会递归地向上查询，确保当前目录用量满足每一级目录的配额设置。
        :type PathPrefix: String
        :param LogicalHardThreshold: 容量硬阈值，不可超过文件系统容量配额。单位：Bytes。
        :type PathPrefix: Long
        """
        self.FileSystemId = None
        self.StoreClass = None
        self.ClusterName = None
        self.FileSystemName = None
        self.DirPath = None
        self.LogicalHardThreshold = None

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
        if params.get("LogicalHardThreshold"):
            self.LogicalHardThreshold = params.get("LogicalHardThreshold")


class DescribeSubDirListRequest(AbstractModel):
    """DescribeSubDirList请求参数结构体
    """

    def __init__(self):
        r"""查询文件系统或特定目录的子目录列表
        :param FileSystemId: 指定文件系统支持2种方式，建议择一使用：1.通过文件系统ID(FileSystemId)；2.输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型 取值：KPFS-P-S01（性能Ⅰ型）KPFS-P-S02（性能Ⅱ型）。
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式 dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/；文件系统传入：/；目录传入路径：dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/；目录最大深度255层，根目录是第一层。
        :type PathPrefix: String
        :param Name: 目录名称
        :type PathPrefix: String
        :param PageNum: 当前页码，最小值1，无上限
        :type PathPrefix: Int
        :param PageSize: 每页数量，默认值1000，最小值1，最大值1000
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
        :param FileSystemId: 指定文件系统支持2种方式，建议择一使用：1.通过文件系统ID(FileSystemId)；2.输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型 取值：KPFS-P-S01（性能Ⅰ型）KPFS-P-S02（性能Ⅱ型）。
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式 dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/。注意：1.存储池、文件系统名称、目录完整路径不允许修改；2.必须与原目录相同；3.若目录中有文件，无法删除。
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
        :param FileSystemId: 指定文件系统支持2种方式，建议择一使用：1.通过文件系统ID(FileSystemId)；2.输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型 取值：KPFS-P-S01（性能Ⅰ型）KPFS-P-S02（性能Ⅱ型）。
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式 dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/。注意：1.存储池、文件系统名称、目录完整路径不允许修改；2.必须与原目录相同。
        :type PathPrefix: String
        :param FileSysPosixPermission: 文件读写权限，格式:十位二进制表示法。备注：默认为755 (-rwxr-xr-x)，拥有者有读、写、执行权限；而属组用户和其他用户只有读、执行权限。
        :type PathPrefix: Int
        :param FileSysOwnerUserId: 文件所属用户的id。备注：设置为0时，为root权限。注意：所属用户的id和所属用户的用户组id须同时修改。
        :type PathPrefix: Int
        :param FileSysOwnerGroupId: 文件所属用户的用户组id。备注：设置为0时，为root权限。注意：所属用户的id和所属用户的用户组id须同时修改。
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
        :param FileSystemId: 指定文件系统支持2种方式，建议择一使用：1.通过文件系统ID(FileSystemId)；2.输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型 取值：KPFS-P-S01（性能Ⅰ型）KPFS-P-S02（性能Ⅱ型）。
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取。
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节。
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式 dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/。限制：1.创建目录的上一层目录必须存在，系统不会自动创建，不存在则报错: $path dose not exist；2.若目录中包含/，系统会自动用/将目录分层，报错信息同上。补充说明：针对目录名称的限制如下：字节长度1-254字节；不允许使用 /；不能设置为.和..。针对完整路径(文件系统名:/dir)：最大1024字节。
        :type PathPrefix: String
        :param FileSysOwnerUserId: 文件所属用户的id，不可设置负数。有效值范围：0-（不校验范围）。备注：设置为0时，为root权限。UID和GID必须同时配置，或皆不配置。否则会报错。
        :type PathPrefix: Int
        :param FileSysOwnerGroupId: 文件所属用户的用户组id，不可设置负数。有效值范围：0- (不校验范围）。备注：设置为0时，为root权限。UID和GID必须同时配置，或皆不配置。否则会报错。
        :type PathPrefix: Int
        :param FileSysPosixPermission: 文件读写权限，格式:十位二进制表示法。备注：默认为755 (-rwxr-xr-x)，拥有者有读、写、执行权限；而属组用户和其他用户只有读、执行权限。
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
        :param FileSystemId: 文件系统的实例ID。性能Ⅰ型/性能Ⅱ型指定文件系统支持2种方式，建议择一使用：1. 通过文件系统ID(FileSystemId)；2. 输入文件系统完整信息，存储类型(StoreClass) + 存储池名称(ClusterName) + 文件系统名称(FileSystemName)同时必填。容量Ⅰ型/容量Ⅱ型/标准型支持2种方式，建议择一使用：1. 通过文件系统ID(FileSystemId)；2. 输入文件系统完整信息，存储类型(StoreClass) + 文件系统名称(FileSystemName)同时必填。
        :type PathPrefix: String
        :param StoreClass: 存储类型
        :type PathPrefix: String
        :param ClusterName: 存储池名称，从控制台>文件系统详情>资源池获取
        :type PathPrefix: String
        :param FileSystemName: 文件系统名称，名称最大长度63字节
        :type PathPrefix: String
        :param DirPath: 目录完整路径，格式：dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/
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


class UpdatePerformanceNfsAclIpRequest(AbstractModel):
    """UpdatePerformanceNfsAclIp请求参数结构体
    """

    def __init__(self):
        r"""编辑NFS访问授权客户端
        :param NfsAclId: 访问授权ID。
        :type PathPrefix: String
        :param Ips: 授权IP配置列表，单次最多编辑20个。
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
        :param Ips: 授权IP列表，为计算节点的私网IP，单次最多删除100个。支持IP（示例：10.0.0.1,10.0.0.2）和网段（示例：10.0.0.1/24）
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
        :param Ips: 授权IP列表，为计算节点的私网IP，单次最多添加100个。
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
        :param ExportPath: 共享目录路径。格式：整个文件系统：不传或传/；子目录：支持格式 dir/xxx 或 /dir/xxx 或 dir/xxx/ 或 /dir/xxx/。
        :type PathPrefix: String
        :param Ips: 授权IP列表，为计算节点的私网IP，单次最多添加100个。
        :type PathPrefix: Array
        :param Desc: 规则描述信息。0-63字符。
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
        :type PathPrefix: Int
        :param PageSize: 分页大小。默认为10。
        :type PathPrefix: Int
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


