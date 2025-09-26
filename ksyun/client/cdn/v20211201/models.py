from ksyun.common.abstract_model import AbstractModel

class GetRefreshOrPreloadTaskRequest(AbstractModel):
    """GetRefreshOrPreloadTask请求参数结构体
    """

    def __init__(self):
        r"""刷新预热进度查询接口迭代
        :param Action: 
        :type PathPrefix: String
        :param Version: 
        :type PathPrefix: String
        """
        self.Action = None
        self.Version = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")


