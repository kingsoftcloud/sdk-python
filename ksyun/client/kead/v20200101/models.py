from ksyun.common.abstract_model import AbstractModel

class DescribeKeadRequest(AbstractModel):
    """DescribeKead请求参数结构体
    """

    def __init__(self):
        r"""高防包列表
        :param KeadId: 高防包ID
        :type PathPrefix: Filter
        :param ProjectId: 项目制id
        :type PathPrefix: Filter
        """
        self.KeadId = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("KeadId"):
            self.KeadId = params.get("KeadId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribeKeadIpRequest(AbstractModel):
    """DescribeKeadIp请求参数结构体
    """

    def __init__(self):
        r"""高防包IP列表
        :param Ip: 
        :type PathPrefix: String
        :param ProjectId: 项目制id
        :type PathPrefix: Filter
        :param PageSize: 每页条数
        :type PathPrefix: Int
        :param OffSet: 开始条数
        :type PathPrefix: Int
        """
        self.Ip = None
        self.ProjectId = None
        self.PageSize = None
        self.OffSet = None

    def _deserialize(self, params):
        if params.get("Ip"):
            self.Ip = params.get("Ip")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("OffSet"):
            self.OffSet = params.get("OffSet")


class DescribeBlockIpRequest(AbstractModel):
    """DescribeBlockIp请求参数结构体
    """

    def __init__(self):
        r"""查询封禁IP
        """

    def _deserialize(self, params):
        return


