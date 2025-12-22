from ksyun.common.abstract_model import AbstractModel

class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体
    """

    def __init__(self):
        r"""创建实例
        :param ProjectId: 项目id
        :type PathPrefix: String
        :param InstanceName: 
        :type PathPrefix: String
        :param ProductType: 366 标准版
504 集群版
        :type PathPrefix: String
        :param EngineVersion: 目前仅支持1.8.0
        :type PathPrefix: String
        :param InstanceType: 
        :type PathPrefix: String
        :param EbsType: 默认值是SSD3.0，目前仅支持SSD3.0
        :type PathPrefix: String
        :param EbsSize: 云盘大小，单位是GB
        :type PathPrefix: Int
        :param VpcId: VPC网络ID，可在网络控制台获取
        :type PathPrefix: String
        :param SubnetId: 终端子网ID，可在网络控制台获取（注意类型必须为终端子网）
        :type PathPrefix: String
        :param BillType: 默认是5，5按日配置月结
        :type PathPrefix: Int
        """
        self.ProjectId = None
        self.InstanceName = None
        self.ProductType = None
        self.EngineVersion = None
        self.InstanceType = None
        self.EbsType = None
        self.EbsSize = None
        self.VpcId = None
        self.SubnetId = None
        self.BillType = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("EbsType"):
            self.EbsType = params.get("EbsType")
        if params.get("EbsSize"):
            self.EbsSize = params.get("EbsSize")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("BillType"):
            self.BillType = params.get("BillType")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体
    """

    def __init__(self):
        r"""删除实例
        :param InstanceIds: 
        :type PathPrefix: String
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体
    """

    def __init__(self):
        r"""查看实例详情
        :param InstanceId: 
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
        r"""查看实例列表
        :param InstanceId: 
        :type PathPrefix: String
        :param InstanceName: 
        :type PathPrefix: String
        :param Vip: 
        :type PathPrefix: String
        :param VpcId: 
        :type PathPrefix: String
        :param FuzzySearch: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.VpcId = None
        self.FuzzySearch = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("Vip"):
            self.Vip = params.get("Vip")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")


class DescribeInstanceNodeRequest(AbstractModel):
    """DescribeInstanceNode请求参数结构体
    """

    def __init__(self):
        r"""查看实例节点
        :param InstanceId: 
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance请求参数结构体
    """

    def __init__(self):
        r"""重命名实例
        :param InstanceId: 
        :type PathPrefix: String
        :param InstanceName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.InstanceName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")


class DescribeValidRegionsRequest(AbstractModel):
    """DescribeValidRegions请求参数结构体
    """

    def __init__(self):
        r"""查看有效机房及可用区
        :param Action: action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查看安全组
        :param InstanceId: 
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateSecurityRuleRequest(AbstractModel):
    """CreateSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""创建安全规则
        :param InstanceId: 
        :type PathPrefix: String
        :param SecurityRuleCidrs: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.SecurityRuleCidrs = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("SecurityRuleCidrs"):
            self.SecurityRuleCidrs = params.get("SecurityRuleCidrs")


class DeleteSecurityRuleRequest(AbstractModel):
    """DeleteSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""删除安全规则
        :param InstanceId: 
        :type PathPrefix: String
        :param SecurityRuleIds: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.SecurityRuleIds = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("SecurityRuleIds"):
            self.SecurityRuleIds = params.get("SecurityRuleIds")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体
    """

    def __init__(self):
        r"""查看数据库列表
        :param InstanceId: 
        :type PathPrefix: String
        :param Offset: 
        :type PathPrefix: Int
        :param Limit: 
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class CreateDatabaseRequest(AbstractModel):
    """CreateDatabase请求参数结构体
    """

    def __init__(self):
        r"""创建数据库
        :param InstanceId: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DatabaseName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")


class DeleteDatabaseRequest(AbstractModel):
    """DeleteDatabase请求参数结构体
    """

    def __init__(self):
        r"""删除数据库
        :param InstanceId: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DatabaseName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")


class DescribeRetentionPolicyListRequest(AbstractModel):
    """DescribeRetentionPolicyList请求参数结构体
    """

    def __init__(self):
        r"""查看数据保留策略列表
        :param InstanceId: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DatabaseName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")


class CreateRetentionPolicyRequest(AbstractModel):
    """CreateRetentionPolicy请求参数结构体
    """

    def __init__(self):
        r"""创建数据保留策略
        :param InstanceId: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        :param PolicyName: 
        :type PathPrefix: String
        :param Duration: 1d10h
        :type PathPrefix: String
        :param DefaultPolicy: 默认值：0, 支持0|1  0 否  1是
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DatabaseName = None
        self.PolicyName = None
        self.Duration = None
        self.DefaultPolicy = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")
        if params.get("PolicyName"):
            self.PolicyName = params.get("PolicyName")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("DefaultPolicy"):
            self.DefaultPolicy = params.get("DefaultPolicy")


class DeleteRetentionPolicyRequest(AbstractModel):
    """DeleteRetentionPolicy请求参数结构体
    """

    def __init__(self):
        r"""删除数据保留策略
        :param InstanceId: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        :param PolicyName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DatabaseName = None
        self.PolicyName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")
        if params.get("PolicyName"):
            self.PolicyName = params.get("PolicyName")


class ModifyRetentionPolicyRequest(AbstractModel):
    """ModifyRetentionPolicy请求参数结构体
    """

    def __init__(self):
        r"""修改数据保留策略
        :param InstanceId: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        :param PolicyName: 
        :type PathPrefix: String
        :param Duration: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DatabaseName = None
        self.PolicyName = None
        self.Duration = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")
        if params.get("PolicyName"):
            self.PolicyName = params.get("PolicyName")
        if params.get("Duration"):
            self.Duration = params.get("Duration")


class DescribeMeasurementsRequest(AbstractModel):
    """DescribeMeasurements请求参数结构体
    """

    def __init__(self):
        r"""查看measurement列表
        :param InstanceId: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DatabaseName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")


class DeleteMeasurementRequest(AbstractModel):
    """DeleteMeasurement请求参数结构体
    """

    def __init__(self):
        r"""删除measurement
        :param InstanceId: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        :param MeasurementName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.DatabaseName = None
        self.MeasurementName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")
        if params.get("MeasurementName"):
            self.MeasurementName = params.get("MeasurementName")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体
    """

    def __init__(self):
        r"""查看账户列表
        :param InstanceId: 
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体
    """

    def __init__(self):
        r"""创建账户
        :param InstanceId: 
        :type PathPrefix: String
        :param AccountName: 
        :type PathPrefix: String
        :param AccountPassword: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None
        self.AccountPassword = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")
        if params.get("AccountPassword"):
            self.AccountPassword = params.get("AccountPassword")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体
    """

    def __init__(self):
        r"""删除账户
        :param InstanceId: 
        :type PathPrefix: String
        :param AccountName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体
    """

    def __init__(self):
        r"""查看账户权限列表
        :param InstanceId: 
        :type PathPrefix: String
        :param AccountName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")


class GrantAccountPrivilegeRequest(AbstractModel):
    """GrantAccountPrivilege请求参数结构体
    """

    def __init__(self):
        r"""授予账户权限
        :param InstanceId: 
        :type PathPrefix: String
        :param AccountName: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        :param AccountPrivilege: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None
        self.DatabaseName = None
        self.AccountPrivilege = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")
        if params.get("AccountPrivilege"):
            self.AccountPrivilege = params.get("AccountPrivilege")


class RevokeAccountPrivilegeRequest(AbstractModel):
    """RevokeAccountPrivilege请求参数结构体
    """

    def __init__(self):
        r"""回收账户权限
        :param InstanceId: 
        :type PathPrefix: String
        :param AccountName: 
        :type PathPrefix: String
        :param DatabaseName: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None
        self.DatabaseName = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体
    """

    def __init__(self):
        r"""重置账户密码
        :param InstanceId: 
        :type PathPrefix: String
        :param AccountName: 
        :type PathPrefix: String
        :param AccountPassword: 
        :type PathPrefix: String
        """
        self.InstanceId = None
        self.AccountName = None
        self.AccountPassword = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("AccountName"):
            self.AccountName = params.get("AccountName")
        if params.get("AccountPassword"):
            self.AccountPassword = params.get("AccountPassword")


class DescribeAccountDetailListRequest(AbstractModel):
    """DescribeAccountDetailList请求参数结构体
    """

    def __init__(self):
        r"""查看账户详情列表
        :param Action: action
        :type PathPrefix: String
        """
        self.Action = None

    def _deserialize(self, params):
        if params.get("Action"):
            self.Action = params.get("Action")


