from ksyun.common.abstract_model import AbstractModel


class GetDwsuMetricRequest(AbstractModel):
    """GetDwsuMetric请求参数结构体
    """

    def __init__(self):
        r"""获取实例监控数据
        :param DwsuId: Dwsu ID，即实例ID
        :type PathPrefix: String
        :param Timestamp: 秒级 Unix 时间戳，如果不提供则默认表示当时间
        :type PathPrefix: Int
        """
        self.DwsuId = None
        self.Timestamp = None

    def _deserialize(self, params):
        if params.get("DwsuId"):
            self.DwsuId = params.get("DwsuId")
        if params.get("Timestamp"):
            self.Timestamp = params.get("Timestamp")
