from ksyun.common.abstract_model import AbstractModel


class DescribeClusterRequest(AbstractModel):
    """DescribeCluster请求参数结构体
    """

    def __init__(self):
        r"""查询集群列表，只加载集群基本信息，不会加载组件详情等信息
        :param ClusterId: 
        :type PathPrefix: String
        :param Marker: 
        :type PathPrefix: Int
        :param MaxResults: 值范围0-20
        :type PathPrefix: Int
        :param Search: 集群名称模糊匹配
        :type PathPrefix: String
        :param Filter: 
        :type PathPrefix: Filter
        """
        self.ClusterId = None
        self.Marker = None
        self.MaxResults = None
        self.Search = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Search"):
            self.Search = params.get("Search")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
