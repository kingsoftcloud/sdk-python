from ksyun.common.abstract_model import AbstractModel

class DescribeClusterRequest(AbstractModel):
    """DescribeCluster请求参数结构体
    """

    def __init__(self):
        r"""DescribeCluster
        :param ClusterId: 集群id，如不输入，则默认查询该地域下的所有集群。
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大实例数目，默认10， 范围(0-20]。
        :type PathPrefix: String
        :param Search: 模糊匹配，可匹配如下字段：<br>集群名称(ClusterName)。
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


class DescribeClusterInstanceRequest(AbstractModel):
    """DescribeClusterInstance请求参数结构体
    """

    def __init__(self):
        r"""DescribeClusterInstance
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认10,最大50。
        :type PathPrefix: Int
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: Int
        :param Filter: 
        :type PathPrefix: Filter
        :param Search: 模糊匹配，可以匹配如下字段：<br>主网卡私有IP（PrivateIpAddress）。
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.MaxResults = None
        self.Marker = None
        self.Filter = None
        self.Search = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("Search"):
            self.Search = params.get("Search")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体
    """

    def __init__(self):
        r"""DeleteCluster
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param InstanceDeleteMode: 节点的删除模式。</br>有效值：</br>Terminate（默认值）-销毁实例（仅针对于按量付费的云服务器，对于包年包月的云服务器和裸金属服务器不生效）</br>Remove-仅把节点移除集群，实例本身不销毁
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.InstanceDeleteMode = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceDeleteMode"):
            self.InstanceDeleteMode = params.get("InstanceDeleteMode")


class DownloadClusterConfigRequest(AbstractModel):
    """DownloadClusterConfig请求参数结构体
    """

    def __init__(self):
        r"""DownloadClusterConfig
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param IsPublic: 获取的config类型<br>true：公网访问config文件<br>false：VPC内网config文件<br>默认值：true
        :type PathPrefix: Boolean
        """
        self.ClusterId = None
        self.IsPublic = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("IsPublic"):
            self.IsPublic = params.get("IsPublic")


class ModifyClusterInfoRequest(AbstractModel):
    """ModifyClusterInfo请求参数结构体
    """

    def __init__(self):
        r"""ModifyClusterInfo
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param ClusterName: 集群名称
        :type PathPrefix: String
        :param ClusterDesc: 集群描述信息
        :type PathPrefix: String
        :param EnableKMSE: 是否支持微服务

true：支持

false：不支持
        :type PathPrefix: Boolean
        :param ControlPlaneLog: 支持对托管集群控制面日志采集配置进行全量更新
        :type PathPrefix: Object
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.EnableKMSE = None
        self.ControlPlaneLog = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("ClusterDesc"):
            self.ClusterDesc = params.get("ClusterDesc")
        if params.get("EnableKMSE"):
            self.EnableKMSE = params.get("EnableKMSE")
        if params.get("ControlPlaneLog"):
            self.ControlPlaneLog = params.get("ControlPlaneLog")


class DescribeInstanceImageRequest(AbstractModel):
    """DescribeInstanceImage请求参数结构体
    """

    def __init__(self):
        r"""DescribeInstanceImage
        :param ImageId: 镜像id
        :type PathPrefix: Filter
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


class AddClusterInstancesRequest(AbstractModel):
    """AddClusterInstances请求参数结构体
    """

    def __init__(self):
        r"""AddClusterInstances
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param InstanceSet: 节点配置信息<br>NodeRole只能是Worker。
        :type PathPrefix: Filter
        """
        self.ClusterId = None
        self.InstanceSet = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceSet"):
            self.InstanceSet = params.get("InstanceSet")


class DeleteClusterInstancesRequest(AbstractModel):
    """DeleteClusterInstances请求参数结构体
    """

    def __init__(self):
        r"""DeleteClusterInstances
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param InstanceId: 需要移除的节点id列表，只允许移除Worker节点（N的范围为1-50）。
        :type PathPrefix: Filter
        :param InstanceDeleteMode: 节点的删除模式，有效值:<br/>- **Terminate**（默认值）：销毁实例（仅针对于按量付费的云服务器，对于包年包月的云服务器和裸金属服务器不生效）<br/>- **Remove**：仅把节点移除集群，实例本身不销毁。
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.InstanceId = None
        self.InstanceDeleteMode = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceDeleteMode"):
            self.InstanceDeleteMode = params.get("InstanceDeleteMode")


class DescribeEpcForClusterRequest(AbstractModel):
    """DescribeEpcForCluster请求参数结构体
    """

    def __init__(self):
        r"""DescribeEpcForCluster
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param InstanceId: 裸金属服务器实例id
        :type PathPrefix: Filter
        :param Filter: 
        :type PathPrefix: Filter
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大实例数目，默认20， 范围(0-50]。
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.InstanceId = None
        self.Filter = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class AddClusterEpcInstancesRequest(AbstractModel):
    """AddClusterEpcInstances请求参数结构体
    """

    def __init__(self):
        r"""AddClusterEpcInstances
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param InstanceId: 移入集群的裸金属服务器实例id <br>注：参数InstanceId.N和EpcPara.N必须填写一个
        :type PathPrefix: Filter
        :param EpcPara: 裸金属服务器产品重新安装操作系统的透传参数，json化字符串格式，详见[重装租赁裸金属服务器](https://docs.ksyun.com/documents/631)。<br>注：已兼容InstanceId.N参数，若填写此参数，则InstanceId.N参数无效
        :type PathPrefix: Filter
        :param AdvancedSetting: 节点高级设置
        :type PathPrefix: Object
        """
        self.ClusterId = None
        self.InstanceId = None
        self.EpcPara = None
        self.AdvancedSetting = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("EpcPara"):
            self.EpcPara = params.get("EpcPara")
        if params.get("AdvancedSetting"):
            self.AdvancedSetting = params.get("AdvancedSetting")


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances请求参数结构体
    """

    def __init__(self):
        r"""获取KEC实例列表
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param InstanceId: 云服务器id
        :type PathPrefix: Filter
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大实例数目，默认10， 范围(0-50]。
        :type PathPrefix: String
        :param Filter: 
        :type PathPrefix: Filter
        :param Search: 模糊匹配，可匹配如下字段：<br>服务器名称(InstanceName)、主网卡私有IP（PrivateIpAddress）。
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.InstanceId = None
        self.Marker = None
        self.MaxResults = None
        self.Filter = None
        self.Search = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("Search"):
            self.Search = params.get("Search")


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances请求参数结构体
    """

    def __init__(self):
        r"""添加KEC节点到集群
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param ExistedInstanceKecSet: 选择已有的虚拟机（包含专属云主机）作为集群的Worker节点，其中NodeRole只能是Worker。<br>N：1-99
        :type PathPrefix: Filter
        """
        self.ClusterId = None
        self.ExistedInstanceKecSet = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ExistedInstanceKecSet"):
            self.ExistedInstanceKecSet = params.get("ExistedInstanceKecSet")


class ForceRemoveClusterInstanceRequest(AbstractModel):
    """ForceRemoveClusterInstance请求参数结构体
    """

    def __init__(self):
        r"""强制删除集群节点
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param InstanceId: 需要强制移除的节点id列表
        :type PathPrefix: Filter
        """
        self.ClusterId = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateNodePoolRequest(AbstractModel):
    """CreateNodePool请求参数结构体
    """

    def __init__(self):
        r"""创建节点池
        :param NodePoolName: 节点池名称<br>校验规则：2-64个字符，支持中文，英文，数字，以及特殊字符-,.!$^*()%#&+/:;<=>[]_`{
        :type PathPrefix: String
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param EnableAutoScale: 是否开启弹性伸缩，有效值：<br>True：开启弹性伸缩<br>False：关闭弹性伸缩<br>默认值：False<br>注：默认未开启自动缩容，若您想开启弹性缩容，后续可在参数ScaleDownEnabled中进行配置开启
        :type PathPrefix: Boolean
        :param NodeTemplate: 节点模板信息
        :type PathPrefix: Object
        :param Label: 节点标签
        :type PathPrefix: Filter
        :param Taint: 节点污点
        :type PathPrefix: Filter
        :param MinSize: 最小节点数量，即为最小能缩容的实例数量，范围[0-50]，不大于maxSize
        :type PathPrefix: Int
        :param MaxSize: 最大节点数量，即为最大能扩容的实例数量，范围[0-50]，不小于minSize
        :type PathPrefix: Int
        :param DesiredCapacity: 期望节点数量，即节点池刚创建时的实例数量，必须在最小节点数量与最大节点数量之间
        :type PathPrefix: Int
        """
        self.NodePoolName = None
        self.ClusterId = None
        self.EnableAutoScale = None
        self.NodeTemplate = None
        self.Label = None
        self.Taint = None
        self.MinSize = None
        self.MaxSize = None
        self.DesiredCapacity = None

    def _deserialize(self, params):
        if params.get("NodePoolName"):
            self.NodePoolName = params.get("NodePoolName")
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("EnableAutoScale"):
            self.EnableAutoScale = params.get("EnableAutoScale")
        if params.get("NodeTemplate"):
            self.NodeTemplate = params.get("NodeTemplate")
        if params.get("Label"):
            self.Label = params.get("Label")
        if params.get("Taint"):
            self.Taint = params.get("Taint")
        if params.get("MinSize"):
            self.MinSize = params.get("MinSize")
        if params.get("MaxSize"):
            self.MaxSize = params.get("MaxSize")
        if params.get("DesiredCapacity"):
            self.DesiredCapacity = params.get("DesiredCapacity")


class DescribeNodePoolRequest(AbstractModel):
    """DescribeNodePool请求参数结构体
    """

    def __init__(self):
        r"""查询节点池详细信息
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodePoolId: 节点池id
        :type PathPrefix: Filter
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0
        :type PathPrefix: Int
        :param MaxResults: 单次调用所返回的最大实例数目，默认10， 范围(0-50]
        :type PathPrefix: Int
        :param NodePoolName: 节点池名称
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.Marker = None
        self.MaxResults = None
        self.NodePoolName = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodePoolId"):
            self.NodePoolId = params.get("NodePoolId")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NodePoolName"):
            self.NodePoolName = params.get("NodePoolName")


class DeleteNodePoolRequest(AbstractModel):
    """DeleteNodePool请求参数结构体
    """

    def __init__(self):
        r"""删除节点池
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodePoolId: 节点池id
        :type PathPrefix: Filter
        :param InstanceDeleteMode: 节点的删除模式，有效值:<br>- **Terminate**：销毁实例<br>- **Remove**：仅把节点移出集群，实例本身不销毁<br>默认值：Terminate
        :type PathPrefix: Boolean
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceDeleteMode = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodePoolId"):
            self.NodePoolId = params.get("NodePoolId")
        if params.get("InstanceDeleteMode"):
            self.InstanceDeleteMode = params.get("InstanceDeleteMode")


class ModifyNodePoolRequest(AbstractModel):
    """ModifyNodePool请求参数结构体
    """

    def __init__(self):
        r"""修改节点池
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodePoolId: 节点池id
        :type PathPrefix: String
        :param NodePoolName: 节点池名称
        :type PathPrefix: String
        :param EnableAutoScale: 是否开启弹性伸缩，有效值：<br>- **False**：关闭弹性伸缩
        :type PathPrefix: Boolean
        :param MinSize: 最小节点数量，即为最小能缩容的实例数量，范围[0-50]，不大于maxSize
        :type PathPrefix: Int
        :param MaxSize: 最大节点数量，即为最大能扩容的实例数量，范围[0-50]，不小于minSize
        :type PathPrefix: Int
        :param DesiredCapacity: 期望节点数量，必须在最小节点数量与最大节点数量之间<br>注：若EnableAutoScale参数为True，不可修改该参数
        :type PathPrefix: Int
        :param Label: 节点标签
        :type PathPrefix: Filter
        :param Taint: 节点污点
        :type PathPrefix: Filter
        :param UpdateExistingNodes: Label、Taints更新是否对节点池内所有已有节点生效，有效值：<br>- **True**：对节点池内已有节点以及扩容出来的节点生效<br>- **False**：只对扩容出来的节点生效<br>默认值：False
        :type PathPrefix: Boolean
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.NodePoolName = None
        self.EnableAutoScale = None
        self.MinSize = None
        self.MaxSize = None
        self.DesiredCapacity = None
        self.Label = None
        self.Taint = None
        self.UpdateExistingNodes = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodePoolId"):
            self.NodePoolId = params.get("NodePoolId")
        if params.get("NodePoolName"):
            self.NodePoolName = params.get("NodePoolName")
        if params.get("EnableAutoScale"):
            self.EnableAutoScale = params.get("EnableAutoScale")
        if params.get("MinSize"):
            self.MinSize = params.get("MinSize")
        if params.get("MaxSize"):
            self.MaxSize = params.get("MaxSize")
        if params.get("DesiredCapacity"):
            self.DesiredCapacity = params.get("DesiredCapacity")
        if params.get("Label"):
            self.Label = params.get("Label")
        if params.get("Taint"):
            self.Taint = params.get("Taint")
        if params.get("UpdateExistingNodes"):
            self.UpdateExistingNodes = params.get("UpdateExistingNodes")


class ModifyNodeTemplateRequest(AbstractModel):
    """ModifyNodeTemplate请求参数结构体
    """

    def __init__(self):
        r"""修改节点池模板
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodePoolId: 节点池id
        :type PathPrefix: String
        :param NodeTemplate: 节点模板信息<br>注：不可修改计费方式、节点池所在vpc
        :type PathPrefix: Object
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.NodeTemplate = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodePoolId"):
            self.NodePoolId = params.get("NodePoolId")
        if params.get("NodeTemplate"):
            self.NodeTemplate = params.get("NodeTemplate")


class ModifyNodePoolScaleUpPolicyRequest(AbstractModel):
    """ModifyNodePoolScaleUpPolicy请求参数结构体
    """

    def __init__(self):
        r"""修改节点池扩容策略
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param ScaleUpPolicy: 扩容算法，有效值：<br>- **random**<br>- **most-pods**<br>- **least-waste**<br>注：仅对开启弹性伸缩的节点池生效
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.ScaleUpPolicy = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ScaleUpPolicy"):
            self.ScaleUpPolicy = params.get("ScaleUpPolicy")


class ModifyNodePoolScaleDownPolicyRequest(AbstractModel):
    """ModifyNodePoolScaleDownPolicy请求参数结构体
    """

    def __init__(self):
        r"""修改节点池缩容策略
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param MaxEmptyBulkDelete: 缩容最大并发数，默认值10
        :type PathPrefix: Int
        :param ScaleDownDelayAfterAdd: 集群扩容后多少分钟开始考虑缩容条件，默认值10
        :type PathPrefix: Int
        :param ScaleDownEnabled: 是否启用自动缩容，有效值：<br>- **True**：开启自动缩容<br>- **False**：关闭自动缩容
        :type PathPrefix: Boolean
        :param ScaleDownUnneededTime: 节点满足缩容条件多少分钟后开始启动缩容，默认值10
        :type PathPrefix: Int
        :param ScaleDownUtilizationThreshold: 缩容阈值百分比。Node已分配资源/node可分配资源小于多少（百分比）时，开始判断缩容条件，默认值50
        :type PathPrefix: Int
        """
        self.ClusterId = None
        self.MaxEmptyBulkDelete = None
        self.ScaleDownDelayAfterAdd = None
        self.ScaleDownEnabled = None
        self.ScaleDownUnneededTime = None
        self.ScaleDownUtilizationThreshold = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("MaxEmptyBulkDelete"):
            self.MaxEmptyBulkDelete = params.get("MaxEmptyBulkDelete")
        if params.get("ScaleDownDelayAfterAdd"):
            self.ScaleDownDelayAfterAdd = params.get("ScaleDownDelayAfterAdd")
        if params.get("ScaleDownEnabled"):
            self.ScaleDownEnabled = params.get("ScaleDownEnabled")
        if params.get("ScaleDownUnneededTime"):
            self.ScaleDownUnneededTime = params.get("ScaleDownUnneededTime")
        if params.get("ScaleDownUtilizationThreshold"):
            self.ScaleDownUtilizationThreshold = params.get("ScaleDownUtilizationThreshold")


class AddClusterInstanceToNodePoolRequest(AbstractModel):
    """AddClusterInstanceToNodePool请求参数结构体
    """

    def __init__(self):
        r"""将集群内节点移入节点池
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodePoolId: 节点池id
        :type PathPrefix: String
        :param InstanceIds: 节点id
        :type PathPrefix: Filter
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodePoolId"):
            self.NodePoolId = params.get("NodePoolId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class ProtectedFromScaleDownRequest(AbstractModel):
    """ProtectedFromScaleDown请求参数结构体
    """

    def __init__(self):
        r"""节点池节点设置缩容保护
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodePoolId: 节点池id
        :type PathPrefix: String
        :param InstanceIds: 节点id
        :type PathPrefix: Filter
        :param ProtectedFromScaleDown: 节点是否开启缩容保护，有效值：<br>- **True**：开启缩容保护<br>- **False**：关闭缩容保护<br>
        :type PathPrefix: Boolean
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None
        self.ProtectedFromScaleDown = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodePoolId"):
            self.NodePoolId = params.get("NodePoolId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("ProtectedFromScaleDown"):
            self.ProtectedFromScaleDown = params.get("ProtectedFromScaleDown")


class DeleteClusterInstancesFromNodePoolRequest(AbstractModel):
    """DeleteClusterInstancesFromNodePool请求参数结构体
    """

    def __init__(self):
        r"""移出节点池节点
        :param ClusterId: 集群id
        :type PathPrefix: String
        :param NodePoolId: 节点池id
        :type PathPrefix: String
        :param InstanceIds: 节点id
        :type PathPrefix: Filter
        :param InstanceDeleteMode: 节点的删除模式，有效值:<br>- **Terminate**：销毁实例<br>- **Remove**：仅把节点移出集群，实例本身不销毁<br>默认值：Terminate
        :type PathPrefix: Boolean
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None
        self.InstanceDeleteMode = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("NodePoolId"):
            self.NodePoolId = params.get("NodePoolId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceDeleteMode"):
            self.InstanceDeleteMode = params.get("InstanceDeleteMode")


class DescribeEpcImageRequest(AbstractModel):
    """DescribeEpcImage请求参数结构体
    """

    def __init__(self):
        r"""查询EPC镜像
        :param ImageId: 镜像id
        :type PathPrefix: Filter
        """
        self.ImageId = None

    def _deserialize(self, params):
        if params.get("ImageId"):
            self.ImageId = params.get("ImageId")


