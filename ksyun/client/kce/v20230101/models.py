from ksyun.common.abstract_model import AbstractModel


class DescribeEventLogsRequest(AbstractModel):
    """DescribeEventLogs请求参数结构体
    """

    def __init__(self):
        r"""查询集群事件日志
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param ClusterName: 集群名称
        :type PathPrefix: String
        :param NodeId: 节点ID
        :type PathPrefix: String
        :param NodeName: 节点名称
        :type PathPrefix: String
        :param Inner: 是否查询内部事件
        :type PathPrefix: Boolean
        :param Marker: 分页参数 游标起始位置，
每次查询返回
        :type PathPrefix: Int
        :param MaxResults: 分页参数，每页最大数 

        :type PathPrefix: Int
        """
        self.ClusterId = None
        self.ClusterName = None
        self.NodeId = None
        self.NodeName = None
        self.Inner = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")
        if params.get("NodeName"):
            self.NodeName = params.get("NodeName")
        if params.get("Inner"):
            self.Inner = params.get("Inner")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class CreateAddonInstanceRequest(AbstractModel):
    """CreateAddonInstance请求参数结构体
    """

    def __init__(self):
        r"""创建插件实例
        """

    def _deserialize(self, params):
        return


class DeleteAddonInstanceRequest(AbstractModel):
    """DeleteAddonInstance请求参数结构体
    """

    def __init__(self):
        r"""删除插件实例
        :param ClusterName: 集群名称
        :type PathPrefix: String
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param AddonId: 插件ID
        :type PathPrefix: String
        :param InstanceId: 插件实例ID
        :type PathPrefix: String
        """
        self.ClusterName = None
        self.ClusterId = None
        self.AddonId = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("AddonId"):
            self.AddonId = params.get("AddonId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeAddonInstancesRequest(AbstractModel):
    """DescribeAddonInstances请求参数结构体
    """

    def __init__(self):
        r"""查询插件实例
        :param CulsterId: 集群ID
        :type PathPrefix: String
        :param ClusterName: 集群名称
        :type PathPrefix: String
        :param Name: 插件名称
        :type PathPrefix: String
        :param AddonIds: 插件ID
        :type PathPrefix: Array
        """
        self.CulsterId = None
        self.ClusterName = None
        self.Name = None
        self.AddonIds = None

    def _deserialize(self, params):
        if params.get("CulsterId"):
            self.CulsterId = params.get("CulsterId")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("AddonIds"):
            self.AddonIds = params.get("AddonIds")


class DescribeAddonListRequest(AbstractModel):
    """DescribeAddonList请求参数结构体
    """

    def __init__(self):
        r"""查询插件列表
        :param Name: 插件名称
        :type PathPrefix: String
        :param MaxResults: 分页参数，每页最大数
        :type PathPrefix: Int
        :param Marker: 游标起始位置
        :type PathPrefix: Int
        """
        self.Name = None
        self.MaxResults = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class DescribeComponentParamsRequest(AbstractModel):
    """DescribeComponentParams请求参数结构体
    """

    def __init__(self):
        r"""查询组件参数版本
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param Components: 组件查询条件
        :type PathPrefix: Array
        :param Marker: 游标起始位置
        :type PathPrefix: Int
        :param MaxResults: 分页参数，每页最大数
        :type PathPrefix: Int
        """
        self.ClusterId = None
        self.Components = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("Components"):
            self.Components = params.get("Components")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class DescribeNetworkRequest(AbstractModel):
    """DescribeNetwork请求参数结构体
    """

    def __init__(self):
        r"""查询集群网络
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param ClusterName: 集群名称
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.ClusterName = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")


class DescribeNodeComponentsRequest(AbstractModel):
    """DescribeNodeComponents请求参数结构体
    """

    def __init__(self):
        r"""查询节点组件列表
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param ClusterName: 集群名称
        :type PathPrefix: String
        :param NodeNames: 节点名称
        :type PathPrefix: Array
        :param NodeIds: 节点ID
        :type PathPrefix: String
        :param Marker: 游标起始位置
        :type PathPrefix: Int
        :param MaxResults: 分页参数，每页最大数
        :type PathPrefix: Int
        """
        self.ClusterId = None
        self.ClusterName = None
        self.NodeNames = None
        self.NodeIds = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("NodeNames"):
            self.NodeNames = params.get("NodeNames")
        if params.get("NodeIds"):
            self.NodeIds = params.get("NodeIds")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class DescribeComponentListRequest(AbstractModel):
    """DescribeComponentList请求参数结构体
    """

    def __init__(self):
        r"""查询可安装的组件列表
        :param K8sVersion: K8S 版本
        :type PathPrefix: String
        """
        self.K8sVersion = None

    def _deserialize(self, params):
        if params.get("K8sVersion"):
            self.K8sVersion = params.get("K8sVersion")
