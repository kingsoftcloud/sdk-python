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
