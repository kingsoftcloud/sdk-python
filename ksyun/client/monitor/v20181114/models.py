from ksyun.common.abstract_model import AbstractModel

class GetMetricStatisticsBatchRequest(AbstractModel):
    """GetMetricStatisticsBatch请求参数结构体
    """

    def __init__(self):
        r"""批量获取监控数据
        :param Namespace: 表示一类云产品，指定命名空间。
        :type PathPrefix: String
        :param StartTime: 起始时间。

> **时间格式：** `2023-07-19T16:09:50Z`
        :type PathPrefix: String
        :param EndTime: 结束时间。

> **时间格式：** `2023-07-19T16:09:50Z`

> **注意：** 数据采集可能存在有2分钟左右的延迟，`EndTime`的值应当比当前时间延迟两分钟，如果当前时间为：2023-07-19T16:11:50Z，那么 `EndTime`=2023-07-19T16:09:50Z。
        :type PathPrefix: String
        :param Aggregate: 数据聚合的方法。目前支持：

- Average
- Max
- Min
        :type PathPrefix: Array
        :param Period: 统计粒度，单位为秒。

> 注意：该参数值应为60的整数倍，值的大小可能会导致数据与控制台展示不一致。

> 默认值为空，将不对数据进行降采样，按产品线的推送频率进行展示。
        :type PathPrefix: Int
        :param Metrics: 指标名列表。


        :type PathPrefix: Array
        """
        self.Namespace = None
        self.StartTime = None
        self.EndTime = None
        self.Aggregate = None
        self.Period = None
        self.Metrics = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Aggregate"):
            self.Aggregate = params.get("Aggregate")
        if params.get("Period"):
            self.Period = params.get("Period")
        if params.get("Metrics"):
            self.Metrics = params.get("Metrics")


