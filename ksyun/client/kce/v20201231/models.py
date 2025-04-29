from ksyun.common.abstract_model import AbstractModel


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体
    """

    def __init__(self):
        r"""创建集群（新）
        :param ClusterName: 集群名称<br>有效值：2-64个字符，支持中文，英文，数字，以及特殊字符-,.!$^*()%#&+/:;<=>[]_`{}~
        :type PathPrefix: String
        :param ClusterType: 集群类型，默认值 VirtualMachine，该字段已无实际意义，可忽略

- VirtualMachine 云服务器
- BareMetal 裸金属

        :type PathPrefix: String
        :param ClusterManageMode: 集群管理模式，默认DedicatedCluster

- DedicatedCluster 独立部署集群
- ManagedCluster 托管集群
- ServerlessCluster serverless集群
        :type PathPrefix: String
        :param ClusterDesc: 集群描述
        :type PathPrefix: String
        :param VpcId: 集群所在的vpcid
        :type PathPrefix: String
        :param PodCidr: 集群pod的网段，如：10.0.0.0/16

- 不能与Service网段冲突
- 不能与VPC网段冲突
- 托管集群不支持33网段
        :type PathPrefix: String
        :param ServiceCidr: 集群Service的网段，如10.254.0.0/16

- 不能与Pod网段冲突
- 不能与Vpc网段冲突
        :type PathPrefix: String
        :param NetworkType: 集群的网络模型

- Flannel
- Canal
- Calico
        :type PathPrefix: String
        :param K8sVersion: 容器服务支持的k8s的集群版本号<br>有效值：v1.17.6、v1.19.3、v1.21.3
        :type PathPrefix: String
        :param ReserveSubnetId: 集群所在vpc终端子网id
        :type PathPrefix: String
        :param PublicApiServer: 是否将apiserver暴露到公网，仅针对独立部署集群生效。若不需要暴露，则不填写此选项；若选择暴露，则会创建公网SLB和EIP用于开启集群的Api Server公网访问。需要用户传递弹性EIP创建透传参数，json化字符串格，详见[创建弹性IP](https://docs.ksyun.com/documents/687)。
        :type PathPrefix: String
        :param ExposePublicApiServer: 托管集群或者Serverless集群是否将apiserver暴露到公网
        :type PathPrefix: Boolean
        :param MaxPodPerNode: 每个节点上运行的pod数量上限<br> 默认值：128 <br> 可选值：16，32，64，128，256
        :type PathPrefix: String
        :param MasterEtcdSeparate: 该字段仅针对于独立部署集群生效，托管集群不生效。集群Master和Etcd组件部署方式，有效值：
True：Master和Etcd组件独享节点部署
False：Master和Etcd组件共享节点部署
默认值：False
        :type PathPrefix: Boolean
        :param ManagedClusterMultiMaster: 当集群类型为托管集群时生效，为托管集群控制面进行子网和安全组配置，支持配置多个
        :type PathPrefix: Filter
        :param InstanceForNode: 新建节点创建集群，定义节点角色和配置，支持云服务器机和专属云服务器。
        :type PathPrefix: Filter
        :param ExistedInstanceForEpc: 使用已有的云物理机创建集群，定义节点角色和配置
        :type PathPrefix: Filter
        :param Component: 不推荐使用接口进行安装，集群会安装默认的组件，如需安装其它增强组件，请在集群创建完成后，在控制台选择安装。
        :type PathPrefix: Filter
        :param ControlPlaneLog: 控制面日志采集,当用户选择的是独立部署集群时，此选项填写无效；当选择是托管时，可选
        :type PathPrefix: Object
        """
        self.ClusterName = None
        self.ClusterType = None
        self.ClusterManageMode = None
        self.ClusterDesc = None
        self.VpcId = None
        self.PodCidr = None
        self.ServiceCidr = None
        self.NetworkType = None
        self.K8sVersion = None
        self.ReserveSubnetId = None
        self.PublicApiServer = None
        self.ExposePublicApiServer = None
        self.MaxPodPerNode = None
        self.MasterEtcdSeparate = None
        self.ManagedClusterMultiMaster = None
        self.InstanceForNode = None
        self.ExistedInstanceForEpc = None
        self.Component = None
        self.ControlPlaneLog = None

    def _deserialize(self, params):
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("ClusterType"):
            self.ClusterType = params.get("ClusterType")
        if params.get("ClusterManageMode"):
            self.ClusterManageMode = params.get("ClusterManageMode")
        if params.get("ClusterDesc"):
            self.ClusterDesc = params.get("ClusterDesc")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("PodCidr"):
            self.PodCidr = params.get("PodCidr")
        if params.get("ServiceCidr"):
            self.ServiceCidr = params.get("ServiceCidr")
        if params.get("NetworkType"):
            self.NetworkType = params.get("NetworkType")
        if params.get("K8sVersion"):
            self.K8sVersion = params.get("K8sVersion")
        if params.get("ReserveSubnetId"):
            self.ReserveSubnetId = params.get("ReserveSubnetId")
        if params.get("PublicApiServer"):
            self.PublicApiServer = params.get("PublicApiServer")
        if params.get("ExposePublicApiServer"):
            self.ExposePublicApiServer = params.get("ExposePublicApiServer")
        if params.get("MaxPodPerNode"):
            self.MaxPodPerNode = params.get("MaxPodPerNode")
        if params.get("MasterEtcdSeparate"):
            self.MasterEtcdSeparate = params.get("MasterEtcdSeparate")
        if params.get("ManagedClusterMultiMaster"):
            self.ManagedClusterMultiMaster = params.get("ManagedClusterMultiMaster")
        if params.get("InstanceForNode"):
            self.InstanceForNode = params.get("InstanceForNode")
        if params.get("ExistedInstanceForEpc"):
            self.ExistedInstanceForEpc = params.get("ExistedInstanceForEpc")
        if params.get("Component"):
            self.Component = params.get("Component")
        if params.get("ControlPlaneLog"):
            self.ControlPlaneLog = params.get("ControlPlaneLog")
