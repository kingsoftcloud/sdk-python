from ksyun.common.abstract_model import AbstractModel

class GetProjectInstanceListNewRequest(AbstractModel):
    """GetProjectInstanceListNew请求参数结构体
    """

    def __init__(self):
        r"""获取项目资源列表（新）
        :param ProjectId: 项目id，不传入该参数时将会查询所有ProjectId对应的数据
        :type PathPrefix: Int
        :param ProductLine: 资源类型标识
        :type PathPrefix: String
        :param Ps: 每页条数，默认10, 最大100条
        :type PathPrefix: Int
        :param Pn: 页码。默认1
        :type PathPrefix: Int
        """
        self.ProjectId = None
        self.ProductLine = None
        self.Ps = None
        self.Pn = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ProductLine"):
            self.ProductLine = params.get("ProductLine")
        if params.get("Ps"):
            self.Ps = params.get("Ps")
        if params.get("Pn"):
            self.Pn = params.get("Pn")


