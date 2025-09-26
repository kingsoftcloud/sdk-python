from ksyun.common.abstract_model import AbstractModel

class CreateUserUsageDataExportTaskRequest(AbstractModel):
    """CreateUserUsageDataExportTask请求参数结构体
    """

    def __init__(self):
        r"""创建用量导表任务
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DD，例如： 2016-08-01
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DD，例如： 2016-08-01
        :type PathPrefix: String
        :param CdnType: 当前产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件，
        :type PathPrefix: String
        :param TaskName: 任务名称，支持任意任务名称，最大长度256字节
        :type PathPrefix: String
        :param Language: 导出文件的语言。zh-cn（默认值）：简体中文。en-us：英文。
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.CdnType = None
        self.TaskName = None
        self.Language = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")
        if params.get("Language"):
            self.Language = params.get("Language")


class GetUserUsageDataExportTaskRequest(AbstractModel):
    """GetUserUsageDataExportTask请求参数结构体
    """

    def __init__(self):
        r"""获取用量导表任务
        :param PageSize: 分页大小。默认值：20；最大值：50。取值：1~50之间的任意整数。
        :type PathPrefix: String
        :param PageNumber: 取得第几页，取值范围：1~100000。
        :type PathPrefix: String
        """
        self.PageSize = None
        self.PageNumber = None

    def _deserialize(self, params):
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")


class DeleteUserUsageDataExportTaskRequest(AbstractModel):
    """DeleteUserUsageDataExportTask请求参数结构体
    """

    def __init__(self):
        r"""删除用量导表任务
        :param TaskID: 任务ID
        :type PathPrefix: String
        """
        self.TaskID = None

    def _deserialize(self, params):
        if params.get("TaskID"):
            self.TaskID = params.get("TaskID")


class GetDomainUsageDataRequest(AbstractModel):
    """GetDomainUsageData请求参数结构体
    """

    def __init__(self):
        r"""用量查询接口
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        :type PathPrefix: String
        :param Metric: 需要获取的用量类型，一次只允许查询一种类型bandwidth：带宽数据traffic：流量数据static-https：静态https请求数dynamic-http：动态http请求数dynamic-https：动态https请求数static-quic：静态quic请求数dynamic-quic：动态quic请求数 <br /><br />PS：Metric取值为bandwidth或者traffic的时候areas生效，请求数不区分区域
        :type PathPrefix: String
        :param CdnType: 当前产品类型，允许输入多种类型，多种类型用，分隔。取值为file：大文件下载，video：音视频点播，page：图片小文件
        :type PathPrefix: String
        :param Domains: 当前账户下选择时间段内正在运行状态的加速域名，可输入需要查询的域名，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名，若产品类型和域名同时存在，进行强校验处理
        :type PathPrefix: String
        :param Areas: 计费区域名称，只允许输入单区域查询。取值：中国大陆 - CN，亚太一区 - AP1，亚太二区 - AP2，亚太三区 - AP3，北美洲 - NA，欧洲 - EU，非洲 - AF，南美洲 - SA。<br /><br />PS：只有Metric取值为bandwidth或者traffic的时候生效，单次允许查询一个或多个区域，多个区域间逗号（半角）分隔，缺省为 CN；请求数不区分区域，当输入条件为请求数任意一种时，此处缺省为全部区域
        :type PathPrefix: String
        :param Interval: 统计粒度，取值为 5：5分钟粒度；60：1小时粒度；1440：1天粒度；缺省为5分钟粒度5分钟及以上粒度的带宽峰值均取该粒度时间段内的5分钟粒度的最高峰值点单次查询最多可获取最近 一年 内 31天 跨度的数据
        :type PathPrefix: String
        :param RequestId: 
        :type PathPrefix: String
        :param PeakTime: 
        :type PathPrefix: String
        :param Time: 
        :type PathPrefix: String
        :param Value: 
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.CdnType = None
        self.Domains = None
        self.Areas = None
        self.Interval = None
        self.RequestId = None
        self.PeakTime = None
        self.Time = None
        self.Value = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Metric"):
            self.Metric = params.get("Metric")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("Areas"):
            self.Areas = params.get("Areas")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("RequestId"):
            self.RequestId = params.get("RequestId")
        if params.get("PeakTime"):
            self.PeakTime = params.get("PeakTime")
        if params.get("Time"):
            self.Time = params.get("Time")
        if params.get("Value"):
            self.Value = params.get("Value")


class CreateUsageDetailDataExportTaskRequest(AbstractModel):
    """CreateUsageDetailDataExportTask请求参数结构体
    """

    def __init__(self):
        r"""创建明细导表任务
        :param StartTime: 获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DD，例如： 2016-08-01
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DD，例如： 2016-08-01，例如： 2016-08-01
        :type PathPrefix: String
        :param Type: 需要获取的用量类型flow：流量带宽数据request：请求数据
        :type PathPrefix: String
        :param CdnType: 当前产品类型，只允许输入一种类型，取值为file：大文件下载，video：音视频点播，page：图片小文件，缺省为全部类型如果该参数不为空，则忽略Domains字段
        :type PathPrefix: String
        :param Domains: 域名信息，支持批量域名查询，多个域名用逗号（半角）分隔，缺省为全部域名，若CdnType有值，则忽略此字段值
        :type PathPrefix: String
        :param TaskName: 任务名称，支持任意任务名称，最大长度256字节
        :type PathPrefix: String
        :param Language: 导出文件的语言。zh-cn（默认值）：简体中文。en-us：英文。
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.CdnType = None
        self.Domains = None
        self.TaskName = None
        self.Language = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("CdnType"):
            self.CdnType = params.get("CdnType")
        if params.get("Domains"):
            self.Domains = params.get("Domains")
        if params.get("TaskName"):
            self.TaskName = params.get("TaskName")
        if params.get("Language"):
            self.Language = params.get("Language")


class GetUsageDetailDataExportTaskRequest(AbstractModel):
    """GetUsageDetailDataExportTask请求参数结构体
    """

    def __init__(self):
        r"""获取明细导出任务
        :param PageSize: 分页大小。默认值：20；最大值：50。取值：1~50之间的任意整数。
        :type PathPrefix: String
        :param PageNumber: 取得第几页，取值范围：1~100000。
        :type PathPrefix: String
        """
        self.PageSize = None
        self.PageNumber = None

    def _deserialize(self, params):
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")


class DeleteUsageDetailDataExportTaskRequest(AbstractModel):
    """DeleteUsageDetailDataExportTask请求参数结构体
    """

    def __init__(self):
        r"""删除明细导表任务
        :param TaskID: 任务ID
        :type PathPrefix: String
        """
        self.TaskID = None

    def _deserialize(self, params):
        if params.get("TaskID"):
            self.TaskID = params.get("TaskID")


