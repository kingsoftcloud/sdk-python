from ksyun.common.abstract_model import AbstractModel

class ListStreamDurationsRequest(AbstractModel):
    """ListStreamDurations请求参数结构体
    """

    def __init__(self):
        r"""查询主播流时长接口
        :param UniqueName: 域名空间
        :type PathPrefix: String
        :param App: 频道
        :type PathPrefix: String
        :param Pubdomain: 推流域名
        :type PathPrefix: String
        :param Stream: 流名，如果携带则返回单条流的推流时长；否则返回整个App下所有流的推流时长
        :type PathPrefix: String
        :param StartUnixTime: 查询开始时间，UTC时间戳，以当天00:00点为开始时间
        :type PathPrefix: Int
        :param EndUnixTime: 查询结束时间，UTC时间戳，以当天00:00点为结束时间
        :type PathPrefix: Int
        """
        self.UniqueName = None
        self.App = None
        self.Pubdomain = None
        self.Stream = None
        self.StartUnixTime = None
        self.EndUnixTime = None

    def _deserialize(self, params):
        if params.get("UniqueName"):
            self.UniqueName = params.get("UniqueName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Pubdomain"):
            self.Pubdomain = params.get("Pubdomain")
        if params.get("Stream"):
            self.Stream = params.get("Stream")
        if params.get("StartUnixTime"):
            self.StartUnixTime = params.get("StartUnixTime")
        if params.get("EndUnixTime"):
            self.EndUnixTime = params.get("EndUnixTime")


class ListHistoryPubStreamsErrInfoRequest(AbstractModel):
    """ListHistoryPubStreamsErrInfo请求参数结构体
    """

    def __init__(self):
        r"""查询流历史流错误信息
        :param UniqueName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param Pubdomain: 推流域名
        :type PathPrefix: String
        :param Stream: 流名
        :type PathPrefix: String
        :param OrderTime: 排序类型（0：按推流开始的时间降序排列，1：按推流开始的时间升序排列），默认为0
        :type PathPrefix: Int
        :param Marker: 起始游标，默认为0。0代表第1页的数据，以此类推
        :type PathPrefix: Int
        :param Limit: 每页返回的记录数，默认1000。单页最多返回5000条数据
        :type PathPrefix: Int
        :param StartUnixTime: 开始时间，UTC时间戳；默认5天前的0点，开始和结束时间间隔不能超过5天，支持查28天内的数据
        :type PathPrefix: Int
        :param EndUnixTime: 结束时间，UTC时间戳；默认当前时间，开始和结束时间间隔不能超过5天，支持查28天内的数据
        :type PathPrefix: Int
        """
        self.UniqueName = None
        self.App = None
        self.Pubdomain = None
        self.Stream = None
        self.OrderTime = None
        self.Marker = None
        self.Limit = None
        self.StartUnixTime = None
        self.EndUnixTime = None

    def _deserialize(self, params):
        if params.get("UniqueName"):
            self.UniqueName = params.get("UniqueName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Pubdomain"):
            self.Pubdomain = params.get("Pubdomain")
        if params.get("Stream"):
            self.Stream = params.get("Stream")
        if params.get("OrderTime"):
            self.OrderTime = params.get("OrderTime")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("StartUnixTime"):
            self.StartUnixTime = params.get("StartUnixTime")
        if params.get("EndUnixTime"):
            self.EndUnixTime = params.get("EndUnixTime")


class ListHistoryPubStreamsInfoRequest(AbstractModel):
    """ListHistoryPubStreamsInfo请求参数结构体
    """

    def __init__(self):
        r"""查询流历史信息接口
        :param UniqueName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param Pubdomain: 推流域名
        :type PathPrefix: String
        :param Stream: 流名
        :type PathPrefix: String
        :param OrderTime: 排序类型（0：按推流开始的时间降序排列，1：按推流开始的时间升序排列），默认为0
        :type PathPrefix: Int
        :param Marker: 起始游标，默认为0。0代表第1页的数据，以此类推
        :type PathPrefix: Int
        :param Limit: 每页返回的记录数，默认1000。单页最多返回5000条数据
        :type PathPrefix: Int
        :param StartUnixTime: UTC时间戳；默认5天前的0点，开始和结束时间间隔不能超过5天，支持查28天之内的数据
        :type PathPrefix: Int
        :param EndUnixTime: UTC时间戳；默认当前时间，开始和结束时间间隔不能超过5天，支持查28天之内的数据
        :type PathPrefix: Int
        """
        self.UniqueName = None
        self.App = None
        self.Pubdomain = None
        self.Stream = None
        self.OrderTime = None
        self.Marker = None
        self.Limit = None
        self.StartUnixTime = None
        self.EndUnixTime = None

    def _deserialize(self, params):
        if params.get("UniqueName"):
            self.UniqueName = params.get("UniqueName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Pubdomain"):
            self.Pubdomain = params.get("Pubdomain")
        if params.get("Stream"):
            self.Stream = params.get("Stream")
        if params.get("OrderTime"):
            self.OrderTime = params.get("OrderTime")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("StartUnixTime"):
            self.StartUnixTime = params.get("StartUnixTime")
        if params.get("EndUnixTime"):
            self.EndUnixTime = params.get("EndUnixTime")


class ForbidStreamRequest(AbstractModel):
    """ForbidStream请求参数结构体
    """

    def __init__(self):
        r"""禁止单路直播流推送
        :param UniqueName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param Pubdomain: 推流域名
        :type PathPrefix: String
        :param Stream: 流名
        :type PathPrefix: String
        :param ForbidTillUnixTime: 流恢复的时间，Unix秒级时间戳<br/> 注意：默认禁播90天，且最长支持禁播90天<br/>传1，立即断开直播流 <br/>传-1，立即断开直播流并禁播90天
        :type PathPrefix: Int
        """
        self.UniqueName = None
        self.App = None
        self.Pubdomain = None
        self.Stream = None
        self.ForbidTillUnixTime = None

    def _deserialize(self, params):
        if params.get("UniqueName"):
            self.UniqueName = params.get("UniqueName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Pubdomain"):
            self.Pubdomain = params.get("Pubdomain")
        if params.get("Stream"):
            self.Stream = params.get("Stream")
        if params.get("ForbidTillUnixTime"):
            self.ForbidTillUnixTime = params.get("ForbidTillUnixTime")


class ResumeStreamRequest(AbstractModel):
    """ResumeStream请求参数结构体
    """

    def __init__(self):
        r"""恢复单路直播流推送
        :param UniqueName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param Pubdomain: 推流域名
        :type PathPrefix: String
        :param Stream: 流名
        :type PathPrefix: String
        """
        self.UniqueName = None
        self.App = None
        self.Pubdomain = None
        self.Stream = None

    def _deserialize(self, params):
        if params.get("UniqueName"):
            self.UniqueName = params.get("UniqueName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Pubdomain"):
            self.Pubdomain = params.get("Pubdomain")
        if params.get("Stream"):
            self.Stream = params.get("Stream")


class GetBlacklistRequest(AbstractModel):
    """GetBlacklist请求参数结构体
    """

    def __init__(self):
        r"""查询黑名单列表
        :param UniqueName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param Pubdomain: 推流域名
        :type PathPrefix: String
        """
        self.UniqueName = None
        self.App = None
        self.Pubdomain = None

    def _deserialize(self, params):
        if params.get("UniqueName"):
            self.UniqueName = params.get("UniqueName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Pubdomain"):
            self.Pubdomain = params.get("Pubdomain")


class CheckBlacklistRequest(AbstractModel):
    """CheckBlacklist请求参数结构体
    """

    def __init__(self):
        r"""检查流是否在黑名单内
        :param UniqueName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param Pubdomain: 推流域名
        :type PathPrefix: String
        :param Stream: 流名
        :type PathPrefix: String
        """
        self.UniqueName = None
        self.App = None
        self.Pubdomain = None
        self.Stream = None

    def _deserialize(self, params):
        if params.get("UniqueName"):
            self.UniqueName = params.get("UniqueName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Pubdomain"):
            self.Pubdomain = params.get("Pubdomain")
        if params.get("Stream"):
            self.Stream = params.get("Stream")


class ListRealtimeStreamsInfoRequest(AbstractModel):
    """ListRealtimeStreamsInfo请求参数结构体
    """

    def __init__(self):
        r"""获取流实时信息
        :param UniqueName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param Stream: 流名，只支持输入单个流名
        :type PathPrefix: String
        :param DomainIds: 拉流域名ID，缺省为UniqueName下全部拉流域名，可输入需要查询的拉流域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        :type PathPrefix: String
        :param PullProtocol: 返回拉流信息协议类型，**默认http+flv**，http flv协议在线人数和带宽；**rtmp**，rtmp协议在线人数和带宽；**hls**：返回hls协议在线人数和带宽
        :type PathPrefix: String
        :param Type: 返回信息类型， 缺省：返回推拉流信息的交集，push，只返回推流信息，pull：只返回拉流信息
        :type PathPrefix: String
        """
        self.UniqueName = None
        self.App = None
        self.Stream = None
        self.DomainIds = None
        self.PullProtocol = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("UniqueName"):
            self.UniqueName = params.get("UniqueName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Stream"):
            self.Stream = params.get("Stream")
        if params.get("DomainIds"):
            self.DomainIds = params.get("DomainIds")
        if params.get("PullProtocol"):
            self.PullProtocol = params.get("PullProtocol")
        if params.get("Type"):
            self.Type = params.get("Type")


