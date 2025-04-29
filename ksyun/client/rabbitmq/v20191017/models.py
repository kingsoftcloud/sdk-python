from ksyun.common.abstract_model import AbstractModel


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体
    """

    def __init__(self):
        r"""创建实例
        :param ProjectId: 所属项目Id。
        :type PathPrefix: String
        :param InstanceName: RabbitMQ实例名称,
校验规则：6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线及中划线
        :type PathPrefix: String
        :param InstancePassword: 实例密码。
        :type PathPrefix: String
        :param VpcId: VPC网络ID。
        :type PathPrefix: String
        :param SubnetId: 终端子网ID。
        :type PathPrefix: String
        :param EngineVersion: 实例版本。
        :type PathPrefix: String
        :param BillType: 计费类型
        :type PathPrefix: Int
        :param Duration: 计费区间(供包年包月计费方式使用)
        :type PathPrefix: Int
        :param Mode: 实例模式。
        :type PathPrefix: String
        :param InstanceType: 实例套餐。
        :type PathPrefix: String
        :param SsdDisk: 实例硬盘。
        :type PathPrefix: Int
        :param NodeNum: 实例节点数量。默认为3。
        :type PathPrefix: Int
        """
        self.ProjectId = None
        self.InstanceName = None
        self.InstancePassword = None
        self.VpcId = None
        self.SubnetId = None
        self.EngineVersion = None
        self.BillType = None
        self.Duration = None
        self.Mode = None
        self.InstanceType = None
        self.SsdDisk = None
        self.NodeNum = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("Mode"):
            self.Mode = params.get("Mode")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("SsdDisk"):
            self.SsdDisk = params.get("SsdDisk")
        if params.get("NodeNum"):
            self.NodeNum = params.get("NodeNum")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体
    """

    def __init__(self):
        r"""删除实例
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体
    """

    def __init__(self):
        r"""实例列表
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        :param InstanceName: 实例名称。
        :type PathPrefix: String
        :param VpcId: VPC网络ID。
        :type PathPrefix: String
        :param SubnetId: 终端子网ID。
        :type PathPrefix: String
        :param Offset: 位移量（查询数据的开始位置，默认为0）
        :type PathPrefix: Int
        :param Limit: 每页记录大小, 最小值是1， 最大值100， 默认值是10
        :type PathPrefix: Int
        :param OrderBy: 排序字段：InstanceId,InstanceName,VpcId,SubnetId,CreateDate

默认为依照实例新建时间由新到旧依次排列，即按创建时间倒序。
OrderBy只为排序字段时，默认按升序排列
可按“实例名称“进行升降排序
传值为如下：
instanceName,asc
instanceName,desc
可按“创建时间”进行升降排序
传值如下：
createTime,asc
createTime,desc
        :type PathPrefix: String
        :param ProjectId: 项目Id,多项目id使用‘,’ 分隔。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VpcId = None
        self.SubnetId = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体
    """

    def __init__(self):
        r"""实例明细
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeInstanceNodesRequest(AbstractModel):
    """DescribeInstanceNodes请求参数结构体
    """

    def __init__(self):
        r"""实例节点列表
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeValidRegionRequest(AbstractModel):
    """DescribeValidRegion请求参数结构体
    """

    def __init__(self):
        r"""控制台有效机房列表
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体
    """

    def __init__(self):
        r"""客户获取机房列表信息
        :param Action: Action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class DescribeSecurityGroupRulesRequest(AbstractModel):
    """DescribeSecurityGroupRules请求参数结构体
    """

    def __init__(self):
        r"""实例白名单列表
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class AddSecurityGroupRuleRequest(AbstractModel):
    """AddSecurityGroupRule请求参数结构体
    """

    def __init__(self):
        r"""添加实例白名单
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        :param Cidrs: IP地址段。如：0.0.0.0/16,0.0.0.0/24。多个","分隔
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Cidrs = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Cidrs"):
            self.Cidrs = params.get("Cidrs")


class DeleteSecurityGroupRulesRequest(AbstractModel):
    """DeleteSecurityGroupRules请求参数结构体
    """

    def __init__(self):
        r"""删除实例白名单
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        :param Cidrs: Ip地址段，如：0.0.0.0/16,0.0.0.0/24。多个以","分隔
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.Cidrs = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Cidrs"):
            self.Cidrs = params.get("Cidrs")


class ResetPasswordRequest(AbstractModel):
    """ResetPassword请求参数结构体
    """

    def __init__(self):
        r"""实例重置密码
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        :param InstancePassword: 实例新密码。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstancePassword = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstancePassword"):
            self.InstancePassword = params.get("InstancePassword")


class RenameRequest(AbstractModel):
    """Rename请求参数结构体
    """

    def __init__(self):
        r"""实例修改名称
        :param InstanceId: 实例Id。
        :type PathPrefix: String
        :param InstanceName: 实例新名称。
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstanceName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
