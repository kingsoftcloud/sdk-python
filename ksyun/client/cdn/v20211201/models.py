from ksyun.common.abstract_model import AbstractModel

class GetRefreshOrPreloadTaskRequest(AbstractModel):
    """GetRefreshOrPreloadTask请求参数结构体
    """

    def __init__(self):
        r"""刷新预热进度查询接口迭代
        :param StartTime: 获取数据起始时间点，不能超出可查询范围的起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2022-03-10T21:00+0800
        :type PathPrefix: String
        :param EndTime: 结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2022-03-10T21:10+0800
        :type PathPrefix: String
        :param TaskId: 支持按任务ID查询，只允许输入单个任务ID
        :type PathPrefix: String
        :param DomainName: 支持按域名查询，只允许输入单个域名
        :type PathPrefix: String
        :param Urls: Url组成的数组，支持按Url路径查询，准确匹配
        :type PathPrefix: Array
        :param Type: 支持按内容管理任务的类型查询，传参可取值：refresh、preload。其中，refresh表示刷新任务类型，preload表示预热任务类型，不传参表示查询所有类型。
        :type PathPrefix: String
        :param SubType: 支持按任务的细分类型查询，传参可取值：REFRESH_FILE、REFRESH_DIR。若Type取值refresh或者不传参，则该传参可生效，其中，REFRESH_FILE表示URL刷新，REFRESH_DIR表示目录刷新，不传参表示查询所有细分类型。若Type取值preload，则该参数为无效参数
        :type PathPrefix: String
        :param PageSize: 分页大小，取值为1-50，最大50，默认20
        :type PathPrefix: Long
        :param PageNumber: 取得第几页，取值为：1-100000，最大100000，默认1
        :type PathPrefix: Long
        """
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.DomainName = None
        self.Urls = None
        self.Type = None
        self.SubType = None
        self.PageSize = None
        self.PageNumber = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("DomainName"):
            self.DomainName = params.get("DomainName")
        if params.get("Urls"):
            self.Urls = params.get("Urls")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("SubType"):
            self.SubType = params.get("SubType")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")


