from ksyun.common.abstract_model import AbstractModel

class GetClientRequestDataRequest(AbstractModel):
    """GetClientRequestData请求参数结构体
    """

    def __init__(self):
        r"""访问数据查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param Metric: 指定查询指标，支持的类型有：**flow**：流量，单位为 byte；**bandwidth**：带宽，单位为 bps；**request**：请求数，单位为 次；**qps**：平均每秒请求次数，单位：次，支持批量数据查询，多个类型用逗号（半角）分隔，默认为全部类型
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为 5：5分钟粒度；60：1小时粒度；1440：1天粒度；<br>5分钟及以上粒度的带宽值均取该粒度时间段内的5分钟粒度的峰值点,流量、请求数取值为求和值。<br>缺省为5分钟粒度。<br>5分钟粒度查询范围最大跨度为31天，其余粒度查询范围最大跨度为90天
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件；支持多个查询，多个类型用逗号分隔
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param Areas: 网民分布区域简称，具体见【[使用须知](https://docs.ksyun.com/documents/196#39)】，支持多区域查询，多个区域用逗号（半角）分隔，缺省为全部区域
        :type PathPrefix: String
        :param Provinces: 省份区域名称， 枚举类型表见【[使用须知](https://docs.ksyun.com/documents/196#37)】；支持省份批量查询，多个省份用逗号（半角）分隔，缺省为全部省份（当Areas选项有且仅有中国大陆选项时，此类型生效，且支持数据展开），具体Provinces见下附录说明
        :type PathPrefix: String
        :param Isps: 运营商名称，枚举类型表见【[使用须知](https://docs.ksyun.com/documents/196#38)】；只允许输入一种类型，缺省为全部运营商，（当Areas选项有且仅有中国大陆选项时，此类型生效，且支持数据展开），具体ISP见下附录说明
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


class GetServerDataRequest(AbstractModel):
    """GetServerData请求参数结构体
    """

    def __init__(self):
        r"""服务数据查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param Metric: 指定查询指标，支持的类型有：**flow**：流量，单位为 byte；**bandwidth**：带宽，单位为 bps；**request**：请求数，单位为次；**qps**：平均每秒请求次数，单位：次，支持批量数据查询，多个类型用逗号（半角）分隔，默认为全部类型
        :type PathPrefix: String
        :param DataType: 数据类型，取值为edge：服务数据； origin：回源数据；一次查询只允许查询一个类型，缺省为 edge
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为5：5分钟粒度；60：1小时粒度；1440：1天粒度；</br>5分钟及以上粒度的带宽值均取该粒度时间段内的5分钟粒度的峰值点，缺省为5分钟粒度；</br>1分钟粒度查询范围最大跨度为24小时，5分钟粒度查询范围最大跨度为31天其余粒度查询范围最大跨度为90天
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param Regions: 区域简称，具体见【[使用须知](https://docs.ksyun.com/documents/196#36)】，支持多区域查询，多个区域用逗号（半角）分隔，缺省为全部区域
        :type PathPrefix: String
        :param Schema: 协议类型， 取值为http:http协议数据; https:https协议数据；quic：quic协议数据，单选，缺省为全部协议类型
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，支持不展开和展开，缺省为 不展开（unexpand）展开支持全部展开（expand）和按照某个查询维度展开，具体包含：区域（region）（回源不支持按照区域展开）、域名（domain）、协议类型（schema）
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.DataType = None
        self.Interval = None
        self.CdnType = None
        self.Domains = None
        self.Regions = None
        self.Schema = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Metric"):
            self.Metric = params.get("Metric")
        if params.get("DataType"):
            self.DataType = params.get("DataType")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("Regions"):
            self.Regions = params.get("Regions")
        if params.get("Schema"):
            self.Schema = params.get("Schema")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetDomainRankingListDataRequest(AbstractModel):
    """GetDomainRankingListData请求参数结构体
    """

    def __init__(self):
        r"""查询域名排行V2
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，取值为all：全部类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param SortBy: 排序方式，取值为bandwidth：带宽峰值，flow：流量，pv：请求数，缺省为flow
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None
        self.SortBy = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")


class GetAreaIspDataRequest(AbstractModel):
    """GetAreaIspData请求参数结构体
    """

    def __init__(self):
        r"""查询地区、运营商V2
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，取值为file：大文件下载，video：音视频点播，page：图片小文件；all：全部类型
        :type PathPrefix: String
        :param Domains: 域名，缺省为当前产品类型下的全部域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None
        self.Domains = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")


class GetTopReferDataRequest(AbstractModel):
    """GetTopReferData请求参数结构体
    """

    def __init__(self):
        r"""查询热门refererV2
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 域名，缺省为当前产品类型下的全部域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔
        :type PathPrefix: String
        :param LimitN: 热门Refer条数，取值为1-200，最大200，默认100
        :type PathPrefix: String
        :param SortBy: 排序方式，取值为flow：流量，pv：请求数，缺省为pv
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None
        self.Domains = None
        self.LimitN = None
        self.SortBy = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("LimitN"):
            self.LimitN = params.get("LimitN")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")


class GetTopUrlDataRequest(AbstractModel):
    """GetTopUrlData请求参数结构体
    """

    def __init__(self):
        r"""查询热门URLV2
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 域名，缺省为当前产品类型下的全部域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔
        :type PathPrefix: String
        :param LimitN: 热门Url条数，取值为1-200，最大200，默认100
        :type PathPrefix: String
        :param SortBy: 排序方式，取值为flow：流量，pv：请求数，缺省为pv
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None
        self.Domains = None
        self.LimitN = None
        self.SortBy = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("LimitN"):
            self.LimitN = params.get("LimitN")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")


class GetRealTimeHitRateDataRequest(AbstractModel):
    """GetRealTimeHitRateData请求参数结构体
    """

    def __init__(self):
        r"""命中率查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param HitRatetype: 命中率类型，取值为取值为flowhitrate:流量命中率;reqhitrate:请求数命中率，单选，缺省为流量命中率，
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件，当CdnType和Domains两个条件同时存在时，进行强校验。
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名，当CdnType和Domains两个条件同时存在时，进行强校验。
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，支持不展开（unexpand）、按域名（domain）维度展开共2种展开方式，缺省为 不展开（unexpand）
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.HitRatetype = None
        self.CdnType = None
        self.Domains = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("HitRatetype"):
            self.HitRatetype = params.get("HitRatetype")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetReqHitRateDataRequest(AbstractModel):
    """GetReqHitRateData请求参数结构体
    """

    def __init__(self):
        r"""请求命中率详情查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为 1：1分钟粒度；取值为 5：5分钟粒度；60：1小时粒度；1440：1天粒度；5分钟及以上粒度的值取该粒度时间段内的5分钟粒度的请求数值累加和的命中率，缺省为5分钟粒度。1分钟粒度查询范围最大跨度为24小时，5分钟粒度查询范围最大跨度为31天，其余粒度查询范围最大跨度为90天
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件，缺省为全部类型，当CdnType和Domains两个条件同时存在时，进行强校验。
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名，当CdnType和Domains两个条件同时存在时，进行强校验。
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，支持不展开（unexpand）、按域名（domain）维度展开共2种展开方式，缺省为 不展开（unexpand）
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CdnType = None
        self.Domains = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetFlowHitRateDataRequest(AbstractModel):
    """GetFlowHitRateData请求参数结构体
    """

    def __init__(self):
        r"""流量命中率详情查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为 1：1分钟粒度；取值为 5：5分钟粒度；60：1小时粒度；1440：1天粒度；5分钟及以上粒度的值取该粒度时间段内的5分钟粒度的流量值累加和，缺省为5分钟粒度。1分钟粒度查询范围最大跨度为24小时，5分钟粒度查询范围最大跨度为31天，其余粒度查询范围最大跨度为90天
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件，缺省为全部类型，当CdnType和Domains两个条件同时存在时，进行强校验。
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名，当CdnType和Domains两个条件同时存在时，进行强校验。
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，支持不展开（unexpand）、按域名（domain）维度展开共2种展开方式，缺省为 不展开（unexpand）
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CdnType = None
        self.Domains = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetDomainRequestPeriodRatioDataRequest(AbstractModel):
    """GetDomainRequestPeriodRatioData请求参数结构体
    """

    def __init__(self):
        r"""数据对比V2
        :param CurrentPeriodStartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param CurrentPeriodEndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param PriorPeriodStartTime: 获取数据起始时间点，不可与CurrentPeriodStartTime相同，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param PriorPeriodEndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param Metric: 指定查询指标，单选，支持的类型为：**flow**：流量，单位为 byte；**bandwidth**：带宽，单位为 bps；**request**：请求数，单位为 次；**qps**：平均每秒请求次数，单位：次
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件，live：流媒体直播
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为 1：1分钟粒度；取值为 5：5分钟粒度；60：1小时粒度；1440：1天粒度；5分钟及以上粒度的带宽值均取该粒度时间段内的5分钟粒度的峰值点。默认为5分钟粒度1分钟粒度查询范围最大跨度为24小时5分钟粒度查询范围最大跨度为31天其余粒度查询范围最大跨度为31天
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param Areas: 网民分布区域简称，枚举类型表见[使用须知](https://docs.ksyun.com/documents/196#39)，支持多区域查询，多个区域用逗号（半角）分隔，缺省为全部区域
        :type PathPrefix: String
        :param Provinces: 省份区域名称， 枚举类型表见[使用须知](https://docs.ksyun.com/documents/196#37)；支持省份批量查询，多个省份用逗号（半角）分隔，缺省为全部省份（当Areas选项有且仅有中国大陆选项时，此类型生效），具体Provinces见下附录说明
        :type PathPrefix: String
        :param Isps: 运营商名称，枚举类型表见[使用须知](https://docs.ksyun.com/documents/196#38)；只允许输入一种类型，缺省为全部运营商，（当Areas选项有且仅有中国大陆选项时，此类型生效），具体ISP见下附录说明
        :type PathPrefix: String
        :param IpType: IP类型，取值为ipv4:ipv4类型数据;ipv6:ipv6类型数据；单选，缺省为全部IP类型
        :type PathPrefix: String
        :param Schema: 协议类型， 取值为http:http协议数据; https:https协议数据；quic：quic协议数据，单选，缺省为全部协议类型
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，支持不展开和按一种维度展开，缺省为 不展开（unexpand）可展开维度包含：区域（area）、域名（domain）、省份（province）、运营商（isp）、IP类型（ip）、协议类型（schema）,
        :type PathPrefix: String
        """
        self.CurrentPeriodStartTime = None
        self.CurrentPeriodEndTime = None
        self.PriorPeriodStartTime = None
        self.PriorPeriodEndTime = None
        self.Metric = None
        self.CdnType = None
        self.Interval = None
        self.Domains = None
        self.Areas = None
        self.Provinces = None
        self.Isps = None
        self.IpType = None
        self.Schema = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("CurrentPeriodStartTime"):
            self.CurrentPeriodStartTime = params.get("CurrentPeriodStartTime")
        if params.get("CurrentPeriodEndTime"):
            self.CurrentPeriodEndTime = params.get("CurrentPeriodEndTime")
        if params.get("PriorPeriodStartTime"):
            self.PriorPeriodStartTime = params.get("PriorPeriodStartTime")
        if params.get("PriorPeriodEndTime"):
            self.PriorPeriodEndTime = params.get("PriorPeriodEndTime")
        if params.get("Metric"):
            self.Metric = params.get("Metric")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
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


class GetUvDataRequest(AbstractModel):
    """GetUvData请求参数结构体
    """

    def __init__(self):
        r"""查询独立IP数V2
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 域名，缺省为当前产品类型下的全部域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为 5（默认）：5分钟粒度；1440：1天粒度。<br>注：当选择粒度是 1440：1天粒度 时，  ResultType 必须是 expand ， StartTime 和 EndTime  都必须是 T00:00+0800 结尾，比如：StartTime 是2022-08-01T00:00+0800、EndTime  是2022-08-06T00:00+0800，表示查询2022-08-01 到 2022-08-05 的天粒度数据；可以是多天查询，最大支持31天的跨度查询。天粒度上线较晚，是在2022-07-05迭代上线，故最早可查询 2022-07-05的天粒度数据。
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，支持不展开（unexpand）和按照域名维度展开（expand），缺省为 不展开
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None
        self.Domains = None
        self.Interval = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetTopIpDataRequest(AbstractModel):
    """GetTopIpData请求参数结构体
    """

    def __init__(self):
        r"""查询TopIPV2
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param LimitN: 独立请求的IP数，取值为1-200，最大200，默认100
        :type PathPrefix: String
        :param SortBy: 排序方式，取值为flow：流量，pv：请求数，缺省为pv
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None
        self.Domains = None
        self.LimitN = None
        self.SortBy = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("LimitN"):
            self.LimitN = params.get("LimitN")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")


class GetSrcDomainHttpCodeDetailedDataRequest(AbstractModel):
    """GetSrcDomainHttpCodeDetailedData请求参数结构体
    """

    def __init__(self):
        r"""回源状态码详情查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param Interval: 统计粒度,取值为 1：1分钟粒度；取值为 5：5分钟粒度；60：1小时粒度；1440：1天粒度;5分钟以上粒度的值取该粒度时间段内的5分钟粒度的累加和,缺省为5分钟粒度.1分钟粒度查询范围最大跨度为24小时，5分钟粒度查询范围最大跨度为31天，其余粒度查询范围最大跨度为90天
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param Schema: 协议类型， 取值为http:http协议数据; https:https协议数据；quic：quic协议数据，单选，缺省为全部协议类型
        :type PathPrefix: String
        :param CodeType: 状态码分类，取值为：2xx/3xx/4xx/5xx，默认为全部状态码类型，多个状态码类型用逗号（半角）分隔
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，此处表示是否按照域名维度展开，支持不展开（unexpand）、按照具体域名维度展开（domain），按照具体状态码维度展开（code）、展开（expand）缺省为不展开（unexpand）方式
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CdnType = None
        self.Domains = None
        self.Schema = None
        self.CodeType = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("Schema"):
            self.Schema = params.get("Schema")
        if params.get("CodeType"):
            self.CodeType = params.get("CodeType")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetSrcDomainHttpCodeDataRequest(AbstractModel):
    """GetSrcDomainHttpCodeData请求参数结构体
    """

    def __init__(self):
        r"""回源状态码查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param Schema: 协议类型， 取值为http:http协议数据; https:https协议数据；quic：quic协议数据，单选，缺省为全部协议类型
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，此处表示是否按照域名维度展开，支持不展开（unexpand）、按照具体域名维度展开（domain），按照具体状态码维度展开（code）、展开（expand）缺省为不展开（unexpand）方式
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None
        self.Domains = None
        self.Schema = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("Schema"):
            self.Schema = params.get("Schema")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetDomainHttpCodeDetailedDataRequest(AbstractModel):
    """GetDomainHttpCodeDetailedData请求参数结构体
    """

    def __init__(self):
        r"""服务状态码详情查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为 1：1分钟粒度；取值为 5：5分钟粒度；60：1小时粒度；1440：1天粒度;<br>5分钟以上粒度的值取该粒度时间段内的5分钟粒度的累加和,缺省为5分钟粒度.<br>1分钟粒度查询范围最大跨度为24小时，5分钟粒度查询范围最大跨度为31天，其余粒度查询范围最大跨度为90天
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param Areas: 网民分布区域简称，具体见【[使用须知](https://docs.ksyun.com/documents/196#39)】，支持多区域查询，多个区域用逗号（半角）分隔，缺省为全部区域
        :type PathPrefix: String
        :param Provinces: 省份区域名称， 枚举类型表见【[使用须知](https://docs.ksyun.com/documents/196#37)】；支持省份批量查询，多个省份用逗号（半角）分隔，缺省为全部省份（当Areas选项有且仅有中国大陆选项时，此类型生效）
        :type PathPrefix: String
        :param Isps: 运营商名称，枚举类型表见【[使用须知](https://docs.ksyun.com/documents/196#38)】；只允许输入一种类型，缺省为全部运营商，（当Areas选项有且仅有中国大陆选项时，此类型生效）
        :type PathPrefix: String
        :param IpType: IP类型，取值为ipv4:ipv4类型数据;ipv6:ipv6类型数据；单选，缺省为全部IP类型
        :type PathPrefix: String
        :param Schema: 协议类型， 取值为http:http协议数据; https:https协议数据；quic：quic协议数据，单选，缺省为全部协议类型
        :type PathPrefix: String
        :param CodeType: 状态码分类，取值为：2xx/3xx/4xx/5xx，默认为全部状态码类型
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，此处表示是否按照域名维度展开，支持不展开（unexpand）、按照具体域名维度展开（domain），按照具体状态码维度展开（code）、展开（expand）缺省为不展开（unexpand）方式
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.CdnType = None
        self.Domains = None
        self.Areas = None
        self.Provinces = None
        self.Isps = None
        self.IpType = None
        self.Schema = None
        self.CodeType = None
        self.ResultType = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
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
        if params.get("CodeType"):
            self.CodeType = params.get("CodeType")
        if params.get("ResultType"):
            self.ResultType = params.get("ResultType")


class GetDomainHttpCodeDataRequest(AbstractModel):
    """GetDomainHttpCodeData请求参数结构体
    """

    def __init__(self):
        r"""服务状态码占比查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:10+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:15+0800
        :type PathPrefix: String
        :param CdnType: 产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名
        :type PathPrefix: String
        :param Areas: 网民分布区域简称，具体见【[使用须知](https://docs.ksyun.com/documents/196#39)】，支持多区域查询，多个区域用逗号（半角）分隔，缺省为全部区域
        :type PathPrefix: String
        :param Provinces: 省份区域名称， 枚举类型表见【[使用须知](https://docs.ksyun.com/documents/196#37)】；支持省份批量查询，多个省份用逗号（半角）分隔，缺省为全部省份（当Areas选项有且仅有中国大陆选项时，此类型生效）
        :type PathPrefix: String
        :param Isps: 运营商名称，枚举类型表见【[使用须知](https://docs.ksyun.com/documents/196#38)】；只允许输入一种类型，缺省为全部运营商，（当Areas选项有且仅有中国大陆选项时，此类型生效）
        :type PathPrefix: String
        :param IpType: IP类型，取值为ipv4:ipv4类型数据;ipv6:ipv6类型数据；单选，缺省为全部IP类型
        :type PathPrefix: String
        :param Schema: 协议类型， 取值为http:http协议数据; https:https协议数据；quic：quic协议数据，单选，缺省为全部协议类型
        :type PathPrefix: String
        :param ResultType: 统计结果数据展示方式，此处表示是否按照域名维度展开，支持不展开（unexpand）、按照具体域名维度展开（domain）、按照具体状态码维度展开（code）、展开（expand）缺省为不展开（unexpand）方式
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
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


class GetEntryRateDataRequest(AbstractModel):
    """GetEntryRateData请求参数结构体
    """

    def __init__(self):
        r"""ECN进入率查询接口
        :param Domains: 需要获取ECN进入率的域名，支持多域名，使用英文逗号(半角)分隔。最多30个
        :type PathPrefix: String
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
只能按5分钟粒度传，每次传一个时间点。例如：取10:00的数据，起止时间传10:00-10:05
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间。日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
只能按5分钟粒度传，每次传一个时间点。例如：取10:00的数据，起止时间传10:00-10:05
        :type PathPrefix: String
        :param Province: 网民ip解析出来的省份。可选值参考省份运营商表。单次请求传多个省份，使用英文逗号(半角)分隔，返回汇总值
        :type PathPrefix: String
        :param Isp: 网民ip解析出来的运营商。可选值参考省份运营商表。单次请求传多个运营商，使用英文逗号(半角)分隔，返回汇总值
        :type PathPrefix: String
        """
        self.Domains = None
        self.StartTime = None
        self.EndTime = None
        self.Province = None
        self.Isp = None

    def _deserialize(self, params):
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Province"):
            self.Province = params.get("Province")
        if params.get("Isp"):
            self.Isp = params.get("Isp")


