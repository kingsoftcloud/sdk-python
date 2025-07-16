from ksyun.common.abstract_model import AbstractModel

class GetMetricStatisticsRequest(AbstractModel):
    """GetMetricStatistics请求参数结构体
    """

    def __init__(self):
        r"""获取监控数据
        :param Namespace: 表示一类云产品，指定命名空间。
        :type PathPrefix: String
        :param InstanceID: 监控实例的ID。

> **特别注意：** 需要额外关注部分产品线实例ID，具体如下：
> - KS3: 实例ID为 BucketName，并非 BucketID；
> - MongoDB：实例ID前添加`user` 前缀；
        :type PathPrefix: String
        :param MetricName: 监控项名称
        :type PathPrefix: String
        :param StartTime: 起始时间。

> **时间格式：** `2023-07-19T16:00:50Z`
        :type PathPrefix: String
        :param EndTime: 结束时间。

> **时间格式：** `2023-07-19T16:09:50Z`

> **特别注意：** 数据采集可能存在有2分钟左右的延迟，EndTime的值应当比当前时间延迟两分钟，
>
> 假设当前时间为：2023-07-19T16:11:50Z，那么 EndTime=2023-07-19T16:09:50Z。
        :type PathPrefix: String
        :param Aggregate: 数据聚合的方法。目前支持：

- Average
- Max
- Min

> **注意：** 如果查询的数据与控制台监控视图不一致，可能是由于该参数导致。
        :type PathPrefix: String
        :param Period: 统计粒度，单位为秒。

> **注意：** 该参数值应为60的整数倍，值的大小可能会导致数据与控制台展示不一致。
>
> 默认值为空时，将不对数据进行降采样，按产品线的推送频率进行展示。
        :type PathPrefix: String
        """
        self.Namespace = None
        self.InstanceID = None
        self.MetricName = None
        self.StartTime = None
        self.EndTime = None
        self.Aggregate = None
        self.Period = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("InstanceID"):
            self.InstanceID = params.get("InstanceID")
        if params.get("MetricName"):
            self.MetricName = params.get("MetricName")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Aggregate"):
            self.Aggregate = params.get("Aggregate")
        if params.get("Period"):
            self.Period = params.get("Period")


class ListMetricsRequest(AbstractModel):
    """ListMetrics请求参数结构体
    """

    def __init__(self):
        r"""查看实例对应的监控指标
        :param Namespace: 表示一类云产品，指定命名空间。
        :type PathPrefix: String
        :param InstanceID: 实例ID。
        :type PathPrefix: String
        :param MetricName: 监控项。
        :type PathPrefix: String
        :param PageIndex: 页号，起始值：1
        :type PathPrefix: Int
        :param PageSize: 分页时每页显示的数据行数。

> 默认值：获取实例下所有监控项
        :type PathPrefix: Int
        """
        self.Namespace = None
        self.InstanceID = None
        self.MetricName = None
        self.PageIndex = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("InstanceID"):
            self.InstanceID = params.get("InstanceID")
        if params.get("MetricName"):
            self.MetricName = params.get("MetricName")
        if params.get("PageIndex"):
            self.PageIndex = params.get("PageIndex")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
