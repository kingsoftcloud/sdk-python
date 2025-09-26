from ksyun.common.abstract_model import AbstractModel

class GetDomainLogsRequest(AbstractModel):
    """GetDomainLogs请求参数结构体
    """

    def __init__(self):
        r"""获取日志下载URL
        """

    def _deserialize(self, params):
        return


class GetRefreshOrPreloadTaskRequest(AbstractModel):
    """GetRefreshOrPreloadTask请求参数结构体
    """

    def __init__(self):
        r"""刷新预热进度查询接口
        :param DomainIds: DomainIds
        :type PathPrefix: String
        """
        self.DomainIds = None

    def _deserialize(self, params):
        if params.get("DomainIds"):
            self.DomainIds = params.get("DomainIds")


class RefreshCachesRequest(AbstractModel):
    """RefreshCaches请求参数结构体
    """

    def __init__(self):
        r"""刷新缓存接口
        :param Files: Files
        :type PathPrefix: String
        :param Dirs: Dirs
        :type PathPrefix: String
        """
        self.Files = None
        self.Dirs = None

    def _deserialize(self, params):
        if params.get("Files"):
            self.Files = params.get("Files")
        if params.get("Dirs"):
            self.Dirs = params.get("Dirs")


class GetDomainPidDimensionUsageDataRequest(AbstractModel):
    """GetDomainPidDimensionUsageData请求参数结构体
    """

    def __init__(self):
        r"""查询pid维度-计费用量数据
        """

    def _deserialize(self, params):
        return


