from ksyun.common.abstract_model import AbstractModel

class DescribeDefaultParamsRequest(AbstractModel):
    """DescribeDefaultParams请求参数结构体
    """

    def __init__(self):
        r"""查询默认参数模板
        :param DbVersion: 实例版本
        :type PathPrefix: Double
        """
        self.DbVersion = None

    def _deserialize(self, params):
        if params.get("DbVersion"):
            self.DbVersion = params.get("DbVersion")


