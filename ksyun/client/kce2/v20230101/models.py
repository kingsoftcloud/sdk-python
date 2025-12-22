from ksyun.common.abstract_model import AbstractModel

class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体
    """

    def __init__(self):
        r"""创建容器集群
        :param ClusterName: 集群名称
有效值：2-64个字符，支持中文，英文，数字，以及特殊字符-_

        :type PathPrefix: String
        :param ClusterDesc: 集群描述，255个字符以内。
        :type PathPrefix: String
        :param ClusterManageMode: 集群部署方式
INDEPENDENT_CLUSTER:独立部署集群MANAGED_CLUSTER: 托管集群
        :type PathPrefix: String
        :param ProjectId: 所属项目ID
        :type PathPrefix: String
        :param KubernetesVersion: K8S版本：v1.26.11，v1.28.7,v1.30.6

        :type PathPrefix: String
        :param Network: 集群网络信息
        :type PathPrefix: Object
        :param NodeInstanceSet: 节点相关配置
        :type PathPrefix: Array
        :param Addons: addon插件配置
        :type PathPrefix: Array
        """
        self.ClusterName = None
        self.ClusterDesc = None
        self.ClusterManageMode = None
        self.ProjectId = None
        self.KubernetesVersion = None
        self.Network = None
        self.NodeInstanceSet = None
        self.Addons = None

    def _deserialize(self, params):
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("ClusterDesc"):
            self.ClusterDesc = params.get("ClusterDesc")
        if params.get("ClusterManageMode"):
            self.ClusterManageMode = params.get("ClusterManageMode")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("KubernetesVersion"):
            self.KubernetesVersion = params.get("KubernetesVersion")
        if params.get("Network"):
            self.Network = params.get("Network")
        if params.get("NodeInstanceSet"):
            self.NodeInstanceSet = params.get("NodeInstanceSet")
        if params.get("Addons"):
            self.Addons = params.get("Addons")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体
    """

    def __init__(self):
        r"""查询集群列表
        :param ClusterIds: 集群ID
        :type PathPrefix: Array
        :param MaxResults: 值范围0-50
默认值：10
        :type PathPrefix: Int
        :param Marker: 分页参数
游标起始位置，每次查询返回
        :type PathPrefix: Int
        """
        self.ClusterIds = None
        self.MaxResults = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("ClusterIds"):
            self.ClusterIds = params.get("ClusterIds")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体
    """

    def __init__(self):
        r"""删除容器集群
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param InstanceDelete: 是否删除主机
        :type PathPrefix: Boolean
        :param SecurityGroupDelete: 默认为fasle
为ture时会尝试删除集群安全组
为false时不会尝试删除集群安全组
        :type PathPrefix: Boolean
        :param PrivateLbDelete: 是否删除私网负载均衡实例（如果是alb且为公私网合一，则只需要删除私网负载均衡即可）
        :type PathPrefix: Boolean
        :param PublicLbDelete: 是否删除公网负载均衡实例
        :type PathPrefix: Boolean
        """
        self.ClusterId = None
        self.InstanceDelete = None
        self.SecurityGroupDelete = None
        self.PrivateLbDelete = None
        self.PublicLbDelete = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceDelete"):
            self.InstanceDelete = params.get("InstanceDelete")
        if params.get("SecurityGroupDelete"):
            self.SecurityGroupDelete = params.get("SecurityGroupDelete")
        if params.get("PrivateLbDelete"):
            self.PrivateLbDelete = params.get("PrivateLbDelete")
        if params.get("PublicLbDelete"):
            self.PublicLbDelete = params.get("PublicLbDelete")


class ModifyClusterRequest(AbstractModel):
    """ModifyCluster请求参数结构体
    """

    def __init__(self):
        r"""修改集群配置
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param ClusterDesc: 集群新描述信息
        :type PathPrefix: String
        :param SANs: 更新SANs(覆盖更新)
        :type PathPrefix: Array
        :param PublicApiServer: 是否开启apiserver，开启则需要填enable 字段为true，如果关闭，则enable字段为false，不修改，这不填该字段
        :type PathPrefix: Object
        :param VpcCNI: 是否开启VpcCNI，开启enable字段为ture，关闭则enable字段为false，不修改则不填

        :type PathPrefix: Object
        """
        self.ClusterId = None
        self.ClusterDesc = None
        self.SANs = None
        self.PublicApiServer = None
        self.VpcCNI = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ClusterDesc"):
            self.ClusterDesc = params.get("ClusterDesc")
        if params.get("SANs"):
            self.SANs = params.get("SANs")
        if params.get("PublicApiServer"):
            self.PublicApiServer = params.get("PublicApiServer")
        if params.get("VpcCNI"):
            self.VpcCNI = params.get("VpcCNI")


class DescribeNodesRequest(AbstractModel):
    """DescribeNodes请求参数结构体
    """

    def __init__(self):
        r"""查询集群节点列表
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param KceNodeIds: 节点id，与InstanceIds 二选一填即可，如果两者均为空，则查询集群下所有的节点

        :type PathPrefix: Array
        :param Marker: 游标起始位置
默认值：0

        :type PathPrefix: Int
        :param MaxResults: 分页参数，每页最大数
值范围0-50
默认值：10
        :type PathPrefix: Int
        :param InstanceIds: 实例id ，与KceNodeIds 二选一填即可，如果两者均为空，则查询集群下所有的节点
        :type PathPrefix: Array
        """
        self.ClusterId = None
        self.KceNodeIds = None
        self.Marker = None
        self.MaxResults = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("KceNodeIds"):
            self.KceNodeIds = params.get("KceNodeIds")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class DeleteNodeRequest(AbstractModel):
    """DeleteNode请求参数结构体
    """

    def __init__(self):
        r"""删除集群节点
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param NodeIds: 
        :type PathPrefix: Array
        :param InstanceDelete: 是否删除主机实例
        :type PathPrefix: Boolean
        :param KceNodeIds: 节点id集合，同实例 id集合必须二选一
        :type PathPrefix: String
        :param InstanceIds: 实例id 集合，同节点 id集合必须二选一
        :type PathPrefix: Array
        """
        self.ClusterId = None
        self.NodeIds = None
        self.InstanceDelete = None
        self.KceNodeIds = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodeIds"):
            self.NodeIds = params.get("NodeIds")
        if params.get("InstanceDelete"):
            self.InstanceDelete = params.get("InstanceDelete")
        if params.get("KceNodeIds"):
            self.KceNodeIds = params.get("KceNodeIds")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class ModifyNodeRequest(AbstractModel):
    """ModifyNode请求参数结构体
    """

    def __init__(self):
        r"""修改节点组件
        :param ClusteId: 集群ID
        :type PathPrefix: String
        :param KceNodeId: 节点id，同实例 id必须二选一
        :type PathPrefix: String
        :param InstanceId: 实例id ，同节点 id必须二选一
        :type PathPrefix: String
        :param Components: 组件列表
        :type PathPrefix: Array
        """
        self.ClusteId = None
        self.KceNodeId = None
        self.InstanceId = None
        self.Components = None

    def _deserialize(self, params):
        if params.get("ClusteId"):
            self.ClusteId = params.get("ClusteId")
        if params.get("KceNodeId"):
            self.KceNodeId = params.get("KceNodeId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Components"):
            self.Components = params.get("Components")


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


class DescribeClusterVersionListRequest(AbstractModel):
    """DescribeClusterVersionList请求参数结构体
    """

    def __init__(self):
        r"""查询集群版本信息
        :param K8sVersion: 
        :type PathPrefix: String
        """
        self.K8sVersion = None

    def _deserialize(self, params):
        if params.get("K8sVersion"):
            self.K8sVersion = params.get("K8sVersion")


class AddKecNodesRequest(AbstractModel):
    """AddKecNodes请求参数结构体
    """

    def __init__(self):
        r"""给集群添加新kec节点或已有kec节点
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodeInstanceSet: 节点信息
        :type PathPrefix: Object
        """
        self.ClusterId = None
        self.NodeInstanceSet = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodeInstanceSet"):
            self.NodeInstanceSet = params.get("NodeInstanceSet")


class AddEpcNodesRequest(AbstractModel):
    """AddEpcNodes请求参数结构体
    """

    def __init__(self):
        r"""给集群添加新Epc节点或已有Epc节点
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodeInstanceSet: 节点信息
        :type PathPrefix: Array
        """
        self.ClusterId = None
        self.NodeInstanceSet = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodeInstanceSet"):
            self.NodeInstanceSet = params.get("NodeInstanceSet")


