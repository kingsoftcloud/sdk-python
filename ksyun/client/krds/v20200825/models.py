from ksyun.common.abstract_model import AbstractModel

class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""创建安全组(GET)
        :param SecurityGroupName: 安全组名称	不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述	不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param SecurityGroupType: 安全组类型	取值范围：IPV4 / IPV6（默认：IPV4）
        :type PathPrefix: String
        :param DBInstanceIdentifier: 安全组绑定实例列表	UUID格式，可填写未绑定过安全组的实例ID。查看数据库实例
        :type PathPrefix: Filter
        :param SecurityGroupRule.SecurityGroupRuleName.N: 安全组规则描述	不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param SecurityGroupRule.SecurityGroupRuleCidr.N: 
        :type PathPrefix: String
        """
        self.SecurityGroupName = None
        self.SecurityGroupDescription = None
        self.SecurityGroupType = None
        self.DBInstanceIdentifier = None
        self.SecurityGroupRule_SecurityGroupRuleName_N = None
        self.SecurityGroupRule_SecurityGroupRuleCidr_N = None

    def _deserialize(self, params):
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("SecurityGroupDescription"):
            self.SecurityGroupDescription = params.get("SecurityGroupDescription")
        if params.get("SecurityGroupType"):
            self.SecurityGroupType = params.get("SecurityGroupType")
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")
        if params.get("SecurityGroupRule.SecurityGroupRuleName.N"):
            self.SecurityGroupRule_SecurityGroupRuleName_N = params.get("SecurityGroupRule.SecurityGroupRuleName.N")
        if params.get("SecurityGroupRule.SecurityGroupRuleCidr.N"):
            self.SecurityGroupRule_SecurityGroupRuleCidr_N = params.get("SecurityGroupRule.SecurityGroupRuleCidr.N")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查询安全组列表/详情
        :param SecurityGroupId: 安全组ID列表，不传的时候返回列表，传值展示指定ID的安全组信息。支持批量查询。
        :type PathPrefix: Filter
        :param SecurityGroupType: 取值范围：IPV4 / IPV6 （默认IPV4）
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupType = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupType"):
            self.SecurityGroupType = params.get("SecurityGroupType")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""删除安全组
        :param SecurityGroupIds: 删除实例安全组，支持批量删除。

注意：

1.已绑定实例的安全组不支持删除，需要手动解除绑定。

2.若删除失败可使用Version: 2016-07-01尝试，创建/删除需使用相同API版本号。

3.返回值为删除后剩余的安全组列表
        :type PathPrefix: String
        """
        self.SecurityGroupIds = None

    def _deserialize(self, params):
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")


class ModifySecurityGroupRequest(AbstractModel):
    """ModifySecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""修改安全组
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupName: 安全组名称
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDescription = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("SecurityGroupDescription"):
            self.SecurityGroupDescription = params.get("SecurityGroupDescription")


class CloneSecurityGroupRequest(AbstractModel):
    """CloneSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""克隆安全组(仅含CIDR规则)
        :param SecurityGroupId: 被克隆安全组ID
        :type PathPrefix: String
        :param SecurityGroupName: 安全组名称.		不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        :param SecurityGroupDescription: 安全组描述	不超过256个字节，仅支持中文、大小写字母、数字、减号和下划线
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDescription = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupName"):
            self.SecurityGroupName = params.get("SecurityGroupName")
        if params.get("SecurityGroupDescription"):
            self.SecurityGroupDescription = params.get("SecurityGroupDescription")


class ModifySecurityGroupRuleRequest(AbstractModel):
    """ModifySecurityGroupRule请求参数结构体
    """

    def __init__(self):
        r"""修改安全组规则
        :param SecurityGroupRuleAction: 对安全组规则列表的操作。		取值范围：Attach|Delete|Cover
Attach: 将传入的规则列表（SecurityGroupRuleName，SecurityGroupRuleProtocol）追加到安全组规则列表内。所有绑定了此安全组的实例都会发生变化。
Delete：从安全组中删除传入的规则列表（SecurityGroupRuleId）。所有绑定了此安全组的实例都会发生变化。
Cover：用传入的规则列表（SecurityGroupRuleName，SecurityGroupRuleProtocol）覆盖安全组规则列表。所有绑定了此安全组的实例都会发生变化。
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupRule.SecurityGroupRuleId: 规则id列表
        :type PathPrefix: Filter
        :param SecurityGroupRule.SecurityGroupRuleName: 规则名称列表
        :type PathPrefix: Filter
        :param SecurityGroupRule.SecurityGroupRuleCidr: 规则协议列表
        :type PathPrefix: Filter
        """
        self.SecurityGroupRuleAction = None
        self.SecurityGroupId = None
        self.SecurityGroupRule_SecurityGroupRuleId = None
        self.SecurityGroupRule_SecurityGroupRuleName = None
        self.SecurityGroupRule_SecurityGroupRuleCidr = None

    def _deserialize(self, params):
        if params.get("SecurityGroupRuleAction"):
            self.SecurityGroupRuleAction = params.get("SecurityGroupRuleAction")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupRule.SecurityGroupRuleId"):
            self.SecurityGroupRule_SecurityGroupRuleId = params.get("SecurityGroupRule.SecurityGroupRuleId")
        if params.get("SecurityGroupRule.SecurityGroupRuleName"):
            self.SecurityGroupRule_SecurityGroupRuleName = params.get("SecurityGroupRule.SecurityGroupRuleName")
        if params.get("SecurityGroupRule.SecurityGroupRuleCidr"):
            self.SecurityGroupRule_SecurityGroupRuleCidr = params.get("SecurityGroupRule.SecurityGroupRuleCidr")


class SecurityGroupRelationRequest(AbstractModel):
    """SecurityGroupRelation请求参数结构体
    """

    def __init__(self):
        r"""修改安全组绑定关系
        :param RelationAction: Attach | Dettach Attach: 添加实例Id到安全组 Dettach：将实例Id从安全组解绑
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID

单独操作传递此值
        :type PathPrefix: String
        :param SecurityGroupIds: 安全组ID列表

若批量操作则传递此值
        :type PathPrefix: String
        :param DBInstanceIdentifier: 实例ID列表		例如：<br>方式1：DBInstanceIdentifier.0=aaa&DBInstanceIdentifier.1=bbb<br>方式2：DBInstanceIdentifier=aaa,bbb
        :type PathPrefix: String
        """
        self.RelationAction = None
        self.SecurityGroupId = None
        self.SecurityGroupIds = None
        self.DBInstanceIdentifier = None

    def _deserialize(self, params):
        if params.get("RelationAction"):
            self.RelationAction = params.get("RelationAction")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupIds"):
            self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("DBInstanceIdentifier"):
            self.DBInstanceIdentifier = params.get("DBInstanceIdentifier")


class ModifySecurityGroupRuleNameRequest(AbstractModel):
    """ModifySecurityGroupRuleName请求参数结构体
    """

    def __init__(self):
        r"""修改规则名称
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        :param SecurityGroupRuleId: 安全组规则ID
        :type PathPrefix: String
        :param SecurityGroupRuleName: 安区组规则备注
        :type PathPrefix: String
        """
        self.SecurityGroupId = None
        self.SecurityGroupRuleId = None
        self.SecurityGroupRuleName = None

    def _deserialize(self, params):
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupRuleId"):
            self.SecurityGroupRuleId = params.get("SecurityGroupRuleId")
        if params.get("SecurityGroupRuleName"):
            self.SecurityGroupRuleName = params.get("SecurityGroupRuleName")


class CreateDBParameterGroupRequest(AbstractModel):
    """CreateDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""创建参数组
        :param DBParameterGroupName: 参数组名称
        :type PathPrefix: String
        :param Engine: 数据库引擎名称 不同的数据库引擎，需要不同的数据库参数组
```json
Engine与EngineVersion的对应关系：
mysql 5.5、5.6、5.7、8.0
percona 5.6
consistent_mysql 5.7
ebs_mysql 5.6、5.7
```
        :type PathPrefix: String
        :param EngineVersion: 数据库引擎版本
        :type PathPrefix: String
        :param Description: 参数组描述
        :type PathPrefix: String
        :param Parameters: 参数值

```json
模拟请求入参：
{
    "Engine": "mysql",
    "EngineVersion": "5.7",
    "Parameters": {
        "delay_key_write": "ON",
        "table_open_cache_instances": 16
    },
    "DBParameterGroupName": "db-drds-openapi-2",
    "Description": "db-drds-openapi-2"
}
```
        :type PathPrefix: Object
        """
        self.DBParameterGroupName = None
        self.Engine = None
        self.EngineVersion = None
        self.Description = None
        self.Parameters = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupName"):
            self.DBParameterGroupName = params.get("DBParameterGroupName")
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("EngineVersion"):
            self.EngineVersion = params.get("EngineVersion")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Parameters"):
            self.Parameters = params.get("Parameters")


class ModifyDBParameterGroupRequest(AbstractModel):
    """ModifyDBParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""修改参数组
        :param DBParameterGroupId: 参数组ID


        :type PathPrefix: String
        :param DBParameterGroupName: 参数组名称 请勿修改实例唯一参数组；参数组名-参数值/参数组名称/参数组描述，至少填写一项


        :type PathPrefix: String
        :param Description: 参数组描述 请勿修改实例唯一参数组；参数组名-参数值/参数组名称/参数组描述，至少填写一项


        :type PathPrefix: String
        :param Parameters: 参数名 参数名与参数值同时填写；参数组名-参数值/参数组名称/参数组描述，至少填写一项


        :type PathPrefix: Object
        """
        self.DBParameterGroupId = None
        self.DBParameterGroupName = None
        self.Description = None
        self.Parameters = None

    def _deserialize(self, params):
        if params.get("DBParameterGroupId"):
            self.DBParameterGroupId = params.get("DBParameterGroupId")
        if params.get("DBParameterGroupName"):
            self.DBParameterGroupName = params.get("DBParameterGroupName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Parameters"):
            self.Parameters = params.get("Parameters")


