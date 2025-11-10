from ksyun.common.abstract_model import AbstractModel

class DescribeClusterRequest(AbstractModel):
    """DescribeCluster请求参数结构体
    """

    def __init__(self):
        r"""查询集群详情V2
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class ListClustersRequest(AbstractModel):
    """ListClusters请求参数结构体
    """

    def __init__(self):
        r"""查看集群列表V2
        :param Marker: 分页信息：
limit:指定返回的记录数
offset：指定查询起始位置
示例值：
limit=2&offset=0
        :type PathPrefix: String
        """
        self.Marker = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName请求参数结构体
    """

    def __init__(self):
        r"""修改集群名称V2
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


class LaunchClusterRequest(AbstractModel):
    """LaunchCluster请求参数结构体
    """

    def __init__(self):
        r"""创建集群V2
        :param ClusterName: 集群名称（1-25个字符，支持数字、大小写字母、减号、下划线）
        :type PathPrefix: String
        :param MainVersion: ES版本
有效值：

7.10.0
7.4.2
6.8.4
5.6.16
        :type PathPrefix: String
        :param Scenario: 场景化配置模板
有效值:
General
Analysis
Log
Search
        :type PathPrefix: String
        :param AvailabilityZone: 集群数据中心及可用区
有效值：
cn-beijing-6a: 华北1（北京）,
cn-beijing-6b: 华北1（北京）,
cn-beijing-6c: 华北1（北京）,
cn-beijing-6d: 华北1（北京）,
cn-beijing-6e: 华北1（北京）,
cn-shanghai-2a: 华东1（上海）,
cn-shanghai-2b: 华东1（上海）,
cn-shanghai-3a: 华东2（上海),
cn-shanghai-3b: 华东2（上海),
cn-qingyangtest-1a: 华南1（广州）,
cn-qingyangtest-1b: 华南1（广州）,
ap-singapore-1a: 新加坡,
ap-singapore-1b: 新加坡,
eu-east-1a: 俄罗斯（莫斯科）,
eu-east-1b: 俄罗斯（莫斯科）,
cn-taipei-1a: 台北,
cn-beijing-fin-a: 华北金融1（北京）,
cn-northwest-1a: 西北1区（庆阳）,
cn-northwest-4a: 西北4区（海东）,
cn-northwest-3a: 西北3区（宁夏）,
        :type PathPrefix: String
        :param ChargeType: 计费方式
有效值：
Monthly：包年包月
Minutely：按量付费
Daily：按量付费按日月结
        :type PathPrefix: String
        :param PurchaseTime: 包年包月购买时长,计费类型为Monthly时必填
        :type PathPrefix: Int
        :param ProjectId: 项目ID
        :type PathPrefix: Int
        :param VpcDomainId: 账号下同数据中心可用VPC网络ID
        :type PathPrefix: String
        :param VpcSubnetId: 账号下同数据中心同可用区可用云服务器子网ID
节点资源有KEC资源则必填
        :type PathPrefix: String
        :param VpcEpcSubnetId: 账号下同数据中心同可用区可用裸金属服务器子网ID
节点资源有裸金属资源则必填
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param InstanceGroups: 节点组信息
        :type PathPrefix: Array
        """
        self.ClusterName = None
        self.MainVersion = None
        self.Scenario = None
        self.AvailabilityZone = None
        self.ChargeType = None
        self.PurchaseTime = None
        self.ProjectId = None
        self.VpcDomainId = None
        self.VpcSubnetId = None
        self.VpcEpcSubnetId = None
        self.SecurityGroupId = None
        self.InstanceGroups = None

    def _deserialize(self, params):
        if params.get("ClusterName"):
            self.ClusterName = params.get("ClusterName")
        if params.get("MainVersion"):
            self.MainVersion = params.get("MainVersion")
        if params.get("Scenario"):
            self.Scenario = params.get("Scenario")
        if params.get("AvailabilityZone"):
            self.AvailabilityZone = params.get("AvailabilityZone")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")
        if params.get("PurchaseTime"):
            self.PurchaseTime = params.get("PurchaseTime")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("VpcDomainId"):
            self.VpcDomainId = params.get("VpcDomainId")
        if params.get("VpcSubnetId"):
            self.VpcSubnetId = params.get("VpcSubnetId")
        if params.get("VpcEpcSubnetId"):
            self.VpcEpcSubnetId = params.get("VpcEpcSubnetId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("InstanceGroups"):
            self.InstanceGroups = params.get("InstanceGroups")


class ListInstanceGroupsRequest(AbstractModel):
    """ListInstanceGroups请求参数结构体
    """

    def __init__(self):
        r"""查询节点组详情V2
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class ServiceControlRequest(AbstractModel):
    """ServiceControl请求参数结构体
    """

    def __init__(self):
        r"""重启集群V2
        :param ClusterId: 集群ID
        :type PathPrefix: String
        :param ControlType: 操作类型：
restart：重启
        :type PathPrefix: String
        :param Rolling: 重启方式：
True（默认）:滚动重启
False：强制重启
        :type PathPrefix: String
        """
        self.ClusterId = None
        self.ControlType = None
        self.Rolling = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")
        if params.get("ControlType"):
            self.ControlType = params.get("ControlType")
        if params.get("Rolling"):
            self.Rolling = params.get("Rolling")


class ClusterHealthStatisticRequest(AbstractModel):
    """ClusterHealthStatistic请求参数结构体
    """

    def __init__(self):
        r"""查看诊断报告V2
        :param ClusterId: 集群ID
        :type PathPrefix: String
        """
        self.ClusterId = None

    def _deserialize(self, params):
        if params.get("ClusterId"):
            self.ClusterId = params.get("ClusterId")


class CheckClusterHealthRequest(AbstractModel):
    """CheckClusterHealth请求参数结构体
    """

    def __init__(self):
        r"""立即诊断V2
        :param cluster_id: 集群ID
        :type PathPrefix: String
        :param check_list: 检查范围:
目前仅支持对集群所有节点组进行诊断，请填写：all

        :type PathPrefix: Array
        """
        self.cluster_id = None
        self.check_list = None

    def _deserialize(self, params):
        if params.get("cluster_id"):
            self.cluster_id = params.get("cluster_id")
        if params.get("check_list"):
            self.check_list = params.get("check_list")


