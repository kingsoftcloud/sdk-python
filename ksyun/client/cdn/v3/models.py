from ksyun.common.abstract_model import AbstractModel

class GetDomainLogsRequest(AbstractModel):
    """GetDomainLogs请求参数结构体
    """

    def __init__(self):
        r"""获取日志下载URL
        :param DomainId: 
        :type PathPrefix: String
        """
        self.DomainId = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")


class GetClientRequestDataRequest(AbstractModel):
    """GetClientRequestData请求参数结构体
    """

    def __init__(self):
        r"""访问数据查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800


        :type PathPrefix: String
        :param Metric: 指定查询指标，支持的类型有：flow：流量，单位为 byte；bandwidth：带宽，单位为 bps；request：请求数，单位为 次；qps：平均每秒请求次数，单位：次，支持批量数据查询，多个类型用逗号（半角）分隔，默认为全部类型
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为 5：5分钟粒度；60：1小时粒度；1440：1天粒度；
5分钟及以上粒度的带宽值均取该粒度时间段内的5分钟粒度的峰值点,流量、请求数取值为求和值。
缺省为5分钟粒度。
5分钟粒度查询范围最大跨度为31天，其余粒度查询范围最大跨度为90天
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件；支持多个查询，多个类型用逗号分隔
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param Areas: 网民分布区域简称，具体见【使用须知】，支持多区域查询，多个区域用逗号（半角）分隔，缺省为全部区域
        :type PathPrefix: String
        :param Provinces: 省份区域名称， 枚举类型表见【使用须知】；支持省份批量查询，多个省份用逗号（半角）分隔，缺省为全部省份（当Areas选项有且仅有中国大陆选项时，此类型生效，且支持数据展开），具体Provinces见下附录说明
        :type PathPrefix: String
        :param Isps: 运营商名称，枚举类型表见【使用须知】；只允许输入一种类型，缺省为全部运营商，（当Areas选项有且仅有中国大陆选项时，此类型生效，且支持数据展开），具体ISP见下附录说明
        :type PathPrefix: String
        :param IpType: IP类型，取值为ipv4:ipv4类型数据;ipv6:ipv类型数据；单选，缺省为全部IP类型
        :type PathPrefix: String
        :param Schema: 协议类型， 取值为http:http协议数据; https:https协议数据；quic：quic协议数据，单选，缺省为全部协议类型
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，支持不展开和展开，缺省为 不展开（unexpand）数据展开支持全部展开（expand）和按照指定查询维度展开，包含：域名（domain）、区域、省份（province）、运营商（isp）、IP类型（ip）、协议类型（schema） 支持多个条件组合展开，多个条件之间用半角逗号区分开来 —— PS:此处一共有31种组合数据包含关系如下：域名 > 省份 > 运营商 > IP 类型 > 协议类型
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Interval = None
        self.CdnType = None
        self.Domains = None
        self.Areas = None
        self.Provinces = None
        self.Isps = None
        self.IpType = None
        self.Schema = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Metric"):
            self.Metric = params.get("Metric")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("Areas"):
            self.Areas = params.get("Areas")
        if params.get("Provinces"):
            self.Provinces = params.get("Provinces")
        if params.get("Isps"):
            self.Isps = params.get("Isps")
        if params.get("IpType"):
            self.IpType = params.get("IpType")
        if params.get("Schema"):
            self.Schema = params.get("Schema")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetCdnDomainsRequest(AbstractModel):
    """GetCdnDomains请求参数结构体
    """

    def __init__(self):
        r"""根据用户查询域名信息列表-V3版本
        :param PageSize: 分页大小，默认20，最大500，取值1～500间整数
        :type PathPrefix: Int
        :param PageNumber: 取第几页。默认为1，取值1～10000
        :type PathPrefix: Int
        :param DomainName: 按域名过滤，默认为空，为空时代表当前用户下所有域名，域名长度最大255，不支持多个域名同时查询
        :type PathPrefix: String
        :param ProjectId: 查询指定项目下的域名。默认为空，为空时查询当前用户下所有域名ProjectId可至金山云控制台-资源管理-项目管理查询
        :type PathPrefix: Int
        :param DomainStatus: 按域名状态过滤。默认为空，为空时查询当前用户下所有域名的全部状态，取值为：online：正在运行；offline：已停止；configuring：配置中；configure_failed：配置失败 ；icp_checking：审核中；icp_check_failed：审核失败；locked：已封禁；locking：封禁中
        :type PathPrefix: String
        :param CdnType: 产品类型：file：大文件下载，video：音视频点播，page：图片小文件，wcdn：全站加速，默认为空，代表当前用户下全部产品类型（包括wcdn产品，不支持live：流媒体直播），支持同时查询多个产品类型，两个类型之间用英文逗号（半角）隔开
        :type PathPrefix: String
        :param FuzzyMatch: 域名过滤是否使用模糊匹配，取值为on：开启，off：关闭，默认为onon
        :type PathPrefix: String
        """
        self.PageSize = None
        self.PageNumber = None
        self.DomainName = None
        self.ProjectId = None
        self.DomainStatus = None
        self.CdnType = None
        self.FuzzyMatch = None

    def _deserialize(self, params):
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("DomainName"):
            self.DomainName = params.get("DomainName")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("DomainStatus"):
            self.DomainStatus = params.get("DomainStatus")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("FuzzyMatch"):
            self.FuzzyMatch = params.get("FuzzyMatch")


class DeleteCdnDomainRequest(AbstractModel):
    """DeleteCdnDomain请求参数结构体
    """

    def __init__(self):
        r"""删除加速域名
        :param DomainId: DomainId
        :type PathPrefix: String
        """
        self.DomainId = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")


class GetCdnDomainBasicInfoRequest(AbstractModel):
    """GetCdnDomainBasicInfo请求参数结构体
    """

    def __init__(self):
        r"""获取指定加速域名配置的基本信息
        :param DomainId: DomainId
        :type PathPrefix: String
        """
        self.DomainId = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")


class ModifyCdnDomainBasicInfoRequest(AbstractModel):
    """ModifyCdnDomainBasicInfo请求参数结构体
    """

    def __init__(self):
        r"""修改域名基本信息
        :param DomainId: DomainId
        :type PathPrefix: String
        :param Regions: Regions
        :type PathPrefix: String
        :param OriginType: OriginType
        :type PathPrefix: String
        :param OriginProtocol: OriginProtocol
        :type PathPrefix: String
        :param Origin: Origin
        :type PathPrefix: String
        """
        self.DomainId = None
        self.Regions = None
        self.OriginType = None
        self.OriginProtocol = None
        self.Origin = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("Regions"):
            self.Regions = params.get("Regions")
        if params.get("OriginType"):
            self.OriginType = params.get("OriginType")
        if params.get("OriginProtocol"):
            self.OriginProtocol = params.get("OriginProtocol")
        if params.get("Origin"):
            self.Origin = params.get("Origin")


class AddCdnDomainRequest(AbstractModel):
    """AddCdnDomain请求参数结构体
    """

    def __init__(self):
        r"""添加加速域名
        :param DomainName: 需要接入CDN的域名
        :type PathPrefix: String
        :param CdnType: 加速域名的产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件，live：流媒体直播，暂不支持直播域名添加
        :type PathPrefix: String
        :param ProjectId: 加速域名所属的项目，非必填项，默认归属为【默认项目】，若输入项目ID，可指定域名归属为已经创建好的项目ID下面
        :type PathPrefix: String
        :param CdnProtocol: 客户访问服务节点的协议。默认http，流媒体直播必须填写：http＋flv，hls，rtmp。当产品类型为大文件下载、音视频点播、图片小文件时，访问协议为http；当产品类型为流媒体直播时，访问协议为http＋flv，hls，rtmp
        :type PathPrefix: String
        :param Regions: 加速区域，支持CN：【中国大陆】；OverSea：【全球（除中国大陆）】；Global：【全球】，缺省为 CN
        :type PathPrefix: String
        :param OriginType: 源站类型 取值：ipaddr、 domain、KS3、ksvideo分别表示：IP源站、域名源站、KS3为源站、金山云视频云源站。当产品类型为下载时，源站类型为ipaddr、 domain、KS3；当产品类型为直播时，源站类型为ipaddr、 domain、ksvideo；当源站类型为KS3时，需添加以ksyun.com结尾的域名
        :type PathPrefix: String
        :param OriginProtocol: 回源协议，取值：http，https，follow，rtmp，hls，当产品类型为大文件下载、音视频点播时，回源协议为http，https，follow（协议跟随）；当产品类型为流媒体直播时，回源协议为rtmp，hls（注：访问协议为hls时，回源协议必须为hls；访问协议为http+flv和rtmp时，回源协议必须为rtmp）
        :type PathPrefix: String
        :param Origin: 回源地址，可以是IP或域名；IP支持最多20个，以逗号区分，域名只能输入一个。IP与域名不能同时输入。当源站类型选择ipaddr时，仅可输入IP地址，当源站类型选择 domain、KS3、ksvideo时，仅可输入域名
        :type PathPrefix: String
        """
        self.DomainName = None
        self.CdnType = None
        self.ProjectId = None
        self.CdnProtocol = None
        self.Regions = None
        self.OriginType = None
        self.OriginProtocol = None
        self.Origin = None

    def _deserialize(self, params):
        if params.get("DomainName"):
            self.DomainName = params.get("DomainName")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("CdnProtocol"):
            self.CdnProtocol = params.get("CdnProtocol")
        if params.get("Regions"):
            self.Regions = params.get("Regions")
        if params.get("OriginType"):
            self.OriginType = params.get("OriginType")
        if params.get("OriginProtocol"):
            self.OriginProtocol = params.get("OriginProtocol")
        if params.get("Origin"):
            self.Origin = params.get("Origin")


class GetDomainConfigsRequest(AbstractModel):
    """GetDomainConfigs请求参数结构体
    """

    def __init__(self):
        r"""查询域名详细配置信息
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param ConfigList: 需要查询的配置，多个配置用逗号（半角）分隔。不填代表查询所有，具体参数说明见下表
        :type PathPrefix: String
        """
        self.DomainId = None
        self.ConfigList = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("ConfigList"):
            self.ConfigList = params.get("ConfigList")


class StartStopCdnDomainRequest(AbstractModel):
    """StartStopCdnDomain请求参数结构体
    """

    def __init__(self):
        r"""启用或停用域名根据域名id
        :param DomainId: 需要启用或停用CDN服务的域名ID，只允许输入一个域名ID
        :type PathPrefix: String
        :param ActionType: 操作接口名，取值：start：启用；stop：停用
        :type PathPrefix: String
        """
        self.DomainId = None
        self.ActionType = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("ActionType"):
            self.ActionType = params.get("ActionType")


class SetCacheRuleConfigRequest(AbstractModel):
    """SetCacheRuleConfig请求参数结构体
    """

    def __init__(self):
        r"""设置缓存策略
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param CacheRules: 由CacheRule组成的数组，表示缓存规则列表。注意：该数组是有序的，优先级按照数组的输入顺序排序，即第一个输入的数组则为最高优先级。
        :type PathPrefix: Array
        """
        self.DomainId = None
        self.CacheRules = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("CacheRules"):
            self.CacheRules = params.get("CacheRules")


class SetBackOriginHostConfigRequest(AbstractModel):
    """SetBackOriginHostConfig请求参数结构体
    """

    def __init__(self):
        r"""设置回源host功能
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param FollowReqDomain: 回源host是否跟随请求域名，取值为true：是，false：否，默认为false
        :type PathPrefix: String
        :param BackOriginHost: 自定义回源域名，默认为空，表示不需要修改回源Host；当FollowReqDomain 为 false时，本参数为必填；FollowReqDomain 为 true时，本参数为非必填，若BackOriginHost传值，将被置空
        :type PathPrefix: String
        """
        self.DomainId = None
        self.FollowReqDomain = None
        self.BackOriginHost = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("FollowReqDomain"):
            self.FollowReqDomain = params.get("FollowReqDomain")
        if params.get("BackOriginHost"):
            self.BackOriginHost = params.get("BackOriginHost")


class GetValidDomainListRequest(AbstractModel):
    """GetValidDomainList请求参数结构体
    """

    def __init__(self):
        r"""获取有效域名
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，取值为file：大文件下载，video：音视频点播，page：小文件下载，live：流媒体直播；all：全部类型，即用户维度
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")


class GetDomainAuthContentRequest(AbstractModel):
    """GetDomainAuthContent请求参数结构体
    """

    def __init__(self):
        r"""获取域名归属校验内容
        :param DomainName: 本次需要验证的域名，只支持单个域名，如test.com。
        :type PathPrefix: String
        """
        self.DomainName = None

    def _deserialize(self, params):
        if params.get("DomainName"):
            self.DomainName = params.get("DomainName")


class SetVideoSeekConfigRequest(AbstractModel):
    """SetVideoSeekConfig请求参数结构体
    """

    def __init__(self):
        r"""设置拖拽播放功能
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param Enable: 配置是否开启或关闭 取值：on、off，默认值为off关闭。
        :type PathPrefix: String
        """
        self.DomainId = None
        self.Enable = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("Enable"):
            self.Enable = params.get("Enable")


class SetPageCompressConfigRequest(AbstractModel):
    """SetPageCompressConfig请求参数结构体
    """

    def __init__(self):
        r"""设置智能压缩接口
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param Enable: 配置智能压缩的开启或关闭 取值：on、off ，默认为off
        :type PathPrefix: String
        :param CompressType: 压缩方式类型，取值：GZIP：GZIP压缩； 默认为GZIP
        :type PathPrefix: String
        :param FileType: Content-Type值；支持传入多个，多个取值间用,分割； 默认为所有支持的18个Content-Type值
        :type PathPrefix: String
        :param FileSize: 压缩文件大小范围，单位Byte，输入格式实例：1024-2048； 默认为1024-31457280
底层参数限制：最小长度：1024 byte，最大长度：31457280 byte
        :type PathPrefix: String
        """
        self.DomainId = None
        self.Enable = None
        self.CompressType = None
        self.FileType = None
        self.FileSize = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("Enable"):
            self.Enable = params.get("Enable")
        if params.get("CompressType"):
            self.CompressType = params.get("CompressType")
        if params.get("FileType"):
            self.FileType = params.get("FileType")
        if params.get("FileSize"):
            self.FileSize = params.get("FileSize")


class SetBrCompressConfigRequest(AbstractModel):
    """SetBrCompressConfig请求参数结构体
    """

    def __init__(self):
        r"""设置BR类型智能压缩接口
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param Enable: 配置智能压缩的开启或关闭 取值：on、off ，默认为off
        :type PathPrefix: String
        :param CompressType: 压缩方式类型，取值：BR：BR压缩； 默认为BR
        :type PathPrefix: String
        :param FileType: Content-Type值；支持传入多个，多个取值间用,分割； 默认为所有支持的18个Content-Type值
        :type PathPrefix: String
        :param FileSize: 压缩文件大小范围，单位Byte，输入格式实例：1024-2048； 默认为1024-31457280
底层参数限制：最小长度：1024 byte，最大长度：31457280 byte
        :type PathPrefix: String
        """
        self.DomainId = None
        self.Enable = None
        self.CompressType = None
        self.FileType = None
        self.FileSize = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("Enable"):
            self.Enable = params.get("Enable")
        if params.get("CompressType"):
            self.CompressType = params.get("CompressType")
        if params.get("FileType"):
            self.FileType = params.get("FileType")
        if params.get("FileSize"):
            self.FileSize = params.get("FileSize")


class SetIgnoreQueryStringConfigRequest(AbstractModel):
    """SetIgnoreQueryStringConfig请求参数结构体
    """

    def __init__(self):
        r"""设置过滤参数功能
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param Enable: 配置过滤参数的开启或关闭 取值：on、off ，默认为on 。
        :type PathPrefix: String
        :param HashKeyArgs: 保留参数，多个用逗号（英文、半角）分隔。
        :type PathPrefix: String
        :param Type: 过滤参数类型
取值：block：删除部分参数；allow：保留部分参数；
当type参数填写是，hashkeyargs必填，否则报错
        :type PathPrefix: String
        """
        self.DomainId = None
        self.Enable = None
        self.HashKeyArgs = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("Enable"):
            self.Enable = params.get("Enable")
        if params.get("HashKeyArgs"):
            self.HashKeyArgs = params.get("HashKeyArgs")
        if params.get("Type"):
            self.Type = params.get("Type")


class SetSetOriginAdvancedConfigRequest(AbstractModel):
    """SetSetOriginAdvancedConfig请求参数结构体
    """

    def __init__(self):
        r"""设置高级回源策略
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param Enable: 设置高级回源配置的开启或关闭 取值: on、off。注意：开启后会关闭掉基础配置中的的回源配置。默认值关闭。开启时，下述必须项为必填项；关闭时，只更改此标识，忽略后面的项目。
        :type PathPrefix: String
        :param OriginType: 主源站类型 取值：ipaddr、 domain分别表示：IP源站、域名源站。 主源站的信息也是在创建加速域名时所设置的源站信息。关闭高级回源配置后，则沿用创建加速域名时的回源配置
        :type PathPrefix: String
        :param Origin: 回源地址，可以是IP或域名；IP支持最多20个，以逗号区分，域名只能输入一个。IP与域名不能同时输入。
        :type PathPrefix: String
        :param BackupOriginType: 热备源站类型，取值：ipaddr、 domain分别表示：IP源站、域名源站。热备源站类型和主源站类型可以不一致。
        :type PathPrefix: String
        :param BackupOrigin: 热备源站回源地址，可以是IP或域名；IP支持最多20个，以逗号区分，域名只能输入一个。IP与域名不能同时输入。
        :type PathPrefix: String
        :param OriginPolicy: rr: 轮询； quality: 按质量最优的topN来轮询回源
        :type PathPrefix: String
        :param OriginPolicyBestCount: 取值1-10的整数。当OriginPolicy是quality时，该项必填。
        :type PathPrefix: String
        """
        self.DomainId = None
        self.Enable = None
        self.OriginType = None
        self.Origin = None
        self.BackupOriginType = None
        self.BackupOrigin = None
        self.OriginPolicy = None
        self.OriginPolicyBestCount = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("Enable"):
            self.Enable = params.get("Enable")
        if params.get("OriginType"):
            self.OriginType = params.get("OriginType")
        if params.get("Origin"):
            self.Origin = params.get("Origin")
        if params.get("BackupOriginType"):
            self.BackupOriginType = params.get("BackupOriginType")
        if params.get("BackupOrigin"):
            self.BackupOrigin = params.get("BackupOrigin")
        if params.get("OriginPolicy"):
            self.OriginPolicy = params.get("OriginPolicy")
        if params.get("OriginPolicyBestCount"):
            self.OriginPolicyBestCount = params.get("OriginPolicyBestCount")


class ValidateDomainOwnerRequest(AbstractModel):
    """ValidateDomainOwner请求参数结构体
    """

    def __init__(self):
        r"""域名归属校验
        :param DomainName: 本次需要验证的域名，只支持单个域名，如test-cdn.com。
        :type PathPrefix: String
        :param AuthType: 验证方式，支持两种方式 DNS校验： dnsCheck；文件校验：fileCheck
        :type PathPrefix: String
        """
        self.DomainName = None
        self.AuthType = None

    def _deserialize(self, params):
        if params.get("DomainName"):
            self.DomainName = params.get("DomainName")
        if params.get("AuthType"):
            self.AuthType = params.get("AuthType")


class SetHttp2OptionConfigRequest(AbstractModel):
    """SetHttp2OptionConfig请求参数结构体
    """

    def __init__(self):
        r"""设置HTTP/2接口
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param Enable: 配置HTTP 2.0功能的开启或关闭 取值：on、off ，默认为off ；开启需保证域名已配置证书。
        :type PathPrefix: String
        """
        self.DomainId = None
        self.Enable = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("Enable"):
            self.Enable = params.get("Enable")


class SetReferProtectionConfigRequest(AbstractModel):
    """SetReferProtectionConfig请求参数结构体
    """

    def __init__(self):
        r"""设置加速域名的Refer防盗链功能
        :param DomainId: 域名ID
        :type PathPrefix: String
        :param Enable: 配置是否开启或关闭，取值：on、off，默认值为off；
开启时，参数ReferType和ReferList为必填项。
        :type PathPrefix: String
        :param ReferType: refer类型，取值：block：黑名单；allow：白名单，开启后必填
        :type PathPrefix: String
        :param ReferList: 逗号（半角）分隔的refer列表；
Enable为on时为必填项；
支持多条输入，一次最多输入一百条。
        :type PathPrefix: String
        :param AllowEmpty: 是否允许空refer访问，取值：on：允许；off：不允许；默认值：on。
        :type PathPrefix: String
        """
        self.DomainId = None
        self.Enable = None
        self.ReferType = None
        self.ReferList = None
        self.AllowEmpty = None

    def _deserialize(self, params):
        if params.get("DomainId"):
            self.DomainId = params.get("DomainId")
        if params.get("Enable"):
            self.Enable = params.get("Enable")
        if params.get("ReferType"):
            self.ReferType = params.get("ReferType")
        if params.get("ReferList"):
            self.ReferList = params.get("ReferList")
        if params.get("AllowEmpty"):
            self.AllowEmpty = params.get("AllowEmpty")


