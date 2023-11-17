from ksyun.common.abstract_model import AbstractModel

class GetMetricStatisticsRequest(AbstractModel):
    """GetMetricStatistics请求参数结构体
    """

    def __init__(self):
        r"""获取监控数据
        :param Namespace: 表示一类云产品，指定命名空间。
        :type PathPrefix: String
        :param InstanceID: 监控实例的ID
备注：MongoDB产品，请在相应监控实例ID前添加user前缀
        :type PathPrefix: String
        :param MetricName: 监控项名称
        :type PathPrefix: String
        :param StartTime: 本地时间，开始时间戳，如2017-02-28T17:00:00Z
        :type PathPrefix: String
        :param EndTime: 本地时间，结束时间戳，如2017-02-28T18:00:00Z, 数据采集有2分钟左右延迟，EndTime需比当前时间延迟两分钟
        :type PathPrefix: String
        :param Aggregate: 数据聚合的方法，Average,Max,Min ，如果和控制台不一致，会导致数据不一致
        :type PathPrefix: String
        :param Period: 采样周期，60的整数倍，单位为秒，如果和控制台不一致，会导致数据不一致。默认值为空，将不对数据进行降采样，按产品线的推送频率进行展示。
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


