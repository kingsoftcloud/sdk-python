from ksyun.common.abstract_model import AbstractModel

class DescribeAlertingResourcesRequest(AbstractModel):
    """DescribeAlertingResources请求参数结构体
    """

    def __init__(self):
        r"""正在告警资源列表
        :param Namespace: 指定命名空间。
        :type PathPrefix: String
        :param StartTime: 起始时间。

> 时间格式：`Unix` 时间戳

> **注意：** StartTime 时间戳要小于30天，目前只能支持查30以内的数据。
        :type PathPrefix: Int
        :param EndTime: 结束时间。

> 时间格式：`Unix` 时间戳
        :type PathPrefix: Int
        """
        self.Namespace = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class DescribeSystemEventAttributesRequest(AbstractModel):
    """DescribeSystemEventAttributes请求参数结构体
    """

    def __init__(self):
        r"""查询系统事件详情
        :param StartTime: 开始时间。

> **Tips：** 请注意时间格式为Unix时间戳（毫秒），从1970年1月1日开始所经过的毫秒数。
        :type PathPrefix: Int
        :param EndTime: 结束时间。

> **Tips：** 请注意时间格式为Unix时间戳（毫秒），从1970年1月1日开始所经过的毫秒数。
        :type PathPrefix: Int
        :param Namespace: 表示一类云产品，指定命名空间。
        :type PathPrefix: String
        :param EventType: 事件类型。

> **说明：**
> 关于事件类型的取值，可参考：[云产品事件列表](https://docs.ksyun.com/directories/3753?type=1)
        :type PathPrefix: String
        :param EventName: 事件名称。

> **说明：**
> 关于事件类型的取值，可参考：[云产品事件列表](https://docs.ksyun.com/directories/3753?type=1)


> **Tips：** 支持同时查询多个事件，多个事件之间用逗号分隔，最多可查询10个事件。
        :type PathPrefix: String
        :param Level: 事件级别。

有效值：
- Critical：严重
- Warn(Warning)：警告
- Info：信息

        :type PathPrefix: String
        :param Status: 事件状态。

> **说明：**
> 关于事件类型的取值，可参考：[云产品事件列表](https://docs.ksyun.com/directories/3753?type=1)
        :type PathPrefix: String
        :param SearchKeywords: 搜索事件内容包含的关键字。

取值：
- 如果您待搜索事件的内容中包括 a 和 b，可以搜索a and b。
- 如果您待搜索事件的内容中包括 a 或 b，可以搜索a or b。
        :type PathPrefix: String
        :param PageIndex: 页码。

取值范围：1~10000。
        :type PathPrefix: Int
        :param PageSize: 每页显示记录条数。

取值范围：1~100。
        :type PathPrefix: Int
        """
        self.StartTime = None
        self.EndTime = None
        self.Namespace = None
        self.EventType = None
        self.EventName = None
        self.Level = None
        self.Status = None
        self.SearchKeywords = None
        self.PageIndex = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("EventType"):
            self.EventType = params.get("EventType")
        if params.get("EventName"):
            self.EventName = params.get("EventName")
        if params.get("Level"):
            self.Level = params.get("Level")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("SearchKeywords"):
            self.SearchKeywords = params.get("SearchKeywords")
        if params.get("PageIndex"):
            self.PageIndex = params.get("PageIndex")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
