from ksyun.common.abstract_model import AbstractModel

class ListAlarmPolicyRequest(AbstractModel):
    """ListAlarmPolicy请求参数结构体
    """

    def __init__(self):
        r"""查询告警策略
        :param PageIndex: 页号，起始值：1
        :type PathPrefix: Int
        :param PageSize: 分页时每页显示的数据行数。

> 取值范围 1~100
        :type PathPrefix: Int
        """
        self.PageIndex = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("PageIndex"):
            self.PageIndex = params.get("PageIndex")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DescribeAlarmPolicyRequest(AbstractModel):
    """DescribeAlarmPolicy请求参数结构体
    """

    def __init__(self):
        r"""查询告警策略详细信息
        :param PolicyId: 告警策略ID，详见[查询告警策略](https://docs.ksyun.com/documents/40346)
        :type PathPrefix: Int
        """
        self.PolicyId = None

    def _deserialize(self, params):
        if params.get("PolicyId"):
            self.PolicyId = params.get("PolicyId")


class DescribePolicyObjectRequest(AbstractModel):
    """DescribePolicyObject请求参数结构体
    """

    def __init__(self):
        r"""查询告警策略关联实例明细
        :param PolicyId: 告警策略ID，详见[查询告警策略](https://docs.ksyun.com/documents/40346)
        :type PathPrefix: Int
        :param PageIndex: 页号，起始值：1
        :type PathPrefix: Int
        :param PageSize: 分页时每页显示的数据行数。

> 取值范围 1~100
        :type PathPrefix: Int
        """
        self.PolicyId = None
        self.PageIndex = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("PolicyId"):
            self.PolicyId = params.get("PolicyId")
        if params.get("PageIndex"):
            self.PageIndex = params.get("PageIndex")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DescribeAlarmReceivesRequest(AbstractModel):
    """DescribeAlarmReceives请求参数结构体
    """

    def __init__(self):
        r"""查询告警策略关联的接收人
        :param PolicyId: 告警策略ID，详见[查询告警策略](https://docs.ksyun.com/documents/40346)
        :type PathPrefix: Int
        """
        self.PolicyId = None

    def _deserialize(self, params):
        if params.get("PolicyId"):
            self.PolicyId = params.get("PolicyId")


class AddAlarmReceivesRequest(AbstractModel):
    """AddAlarmReceives请求参数结构体
    """

    def __init__(self):
        r"""添加告警策略关联的接收人
        :param PolicyId: 告警策略ID，详见[查询告警策略](https://docs.ksyun.com/documents/40346)
        :type PathPrefix: Int
        :param ContactFlag: 告警联系人类型。取值：
- 1: 联系组
- 2: 联系人
        :type PathPrefix: Int
        :param ContactWay: 告警通知方式。取值：
- 1: 发送邮件
- 2: 发送短信
- 3: 发送邮件和短信
        :type PathPrefix: Int
        :param ContactId: 告警联系人ID或告警联系组ID。

> **说明：** 参数支持多个联系人或联系组ID。
        :type PathPrefix: Array
        """
        self.PolicyId = None
        self.ContactFlag = None
        self.ContactWay = None
        self.ContactId = None

    def _deserialize(self, params):
        if params.get("PolicyId"):
            self.PolicyId = params.get("PolicyId")
        if params.get("ContactFlag"):
            self.ContactFlag = params.get("ContactFlag")
        if params.get("ContactWay"):
            self.ContactWay = params.get("ContactWay")
        if params.get("ContactId"):
            self.ContactId = params.get("ContactId")


class DeleteAlarmReceivesRequest(AbstractModel):
    """DeleteAlarmReceives请求参数结构体
    """

    def __init__(self):
        r"""删除告警策略关联的接收人
        :param PolicyId: 告警策略ID，详见[查询告警策略](https://docs.ksyun.com/documents/40346)
        :type PathPrefix: Int
        :param ContactFlag: 告警联系人类型。取值：
- 1: 联系组
- 2: 联系人
        :type PathPrefix: Int
        :param ContactId: 告警联系人ID或告警联系组ID。

> **说明：** 参数支持多个联系人或联系组ID。
        :type PathPrefix: Array
        """
        self.PolicyId = None
        self.ContactFlag = None
        self.ContactId = None

    def _deserialize(self, params):
        if params.get("PolicyId"):
            self.PolicyId = params.get("PolicyId")
        if params.get("ContactFlag"):
            self.ContactFlag = params.get("ContactFlag")
        if params.get("ContactId"):
            self.ContactId = params.get("ContactId")


class GetUserGroupRequest(AbstractModel):
    """GetUserGroup请求参数结构体
    """

    def __init__(self):
        r"""查询联系组
        """

    def _deserialize(self, params):
        return


class GetAlertUserRequest(AbstractModel):
    """GetAlertUser请求参数结构体
    """

    def __init__(self):
        r"""查询联系人
        :param UserGrpId: 联系组ID，详见 [获取联系组](获取联系组)。


> **说明：** 默认：表示全部；
> **示例：** `UserGrpId.1=100&UserGrpId.2=101`
(如果用户需要获取两个联系组的人员信息)
        :type PathPrefix: Filter
        """
        self.UserGrpId = None

    def _deserialize(self, params):
        if params.get("UserGrpId"):
            self.UserGrpId = params.get("UserGrpId")


class UpdateAlertUserStatusRequest(AbstractModel):
    """UpdateAlertUserStatus请求参数结构体
    """

    def __init__(self):
        r"""启用或禁用联系人
        :param UserId: 联系人ID，支持多个。
        :type PathPrefix: Array
        :param UserStatus: 告警联系人状态。取值：
- 1：启用
- 2：禁用
        :type PathPrefix: Int
        """
        self.UserId = None
        self.UserStatus = None

    def _deserialize(self, params):
        if params.get("UserId"):
            self.UserId = params.get("UserId")
        if params.get("UserStatus"):
            self.UserStatus = params.get("UserStatus")


class DescribeSysEventGroupListRequest(AbstractModel):
    """DescribeSysEventGroupList请求参数结构体
    """

    def __init__(self):
        r"""查询事件分组列表
        :param Namespace: 表示一类云产品，指定命名空间, 示例值：
- KEC: 云服务器
- KS3：对象存储
        :type PathPrefix: String
        :param StartTime: 起始时间。

> **Tips**：请注意时间格式为Unix时间戳（毫秒），从1970年1月1日开始所经过的毫秒数。
        :type PathPrefix: Int
        :param EndTime: 结束时间。
        :type PathPrefix: Int
        :param EventName: 指定事件名称，多个间以逗号分隔。
        :type PathPrefix: String
        :param InstanceId: 指定实例ID查询事件，多个间以逗号分隔，最多可查询20个实例
        :type PathPrefix: Array
        :param Order: 结果按照事件创建时间排序方式。
- 0：倒序 
- 1：正序
        :type PathPrefix: Boolean
        :param PageIndex: 页号
        :type PathPrefix: Int
        :param PageSize: 每页显示的数据行数
        :type PathPrefix: Int
        """
        self.Namespace = None
        self.StartTime = None
        self.EndTime = None
        self.EventName = None
        self.InstanceId = None
        self.Order = None
        self.PageIndex = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("EventName"):
            self.EventName = params.get("EventName")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Order"):
            self.Order = params.get("Order")
        if params.get("PageIndex"):
            self.PageIndex = params.get("PageIndex")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DescribeMonitorProductListRequest(AbstractModel):
    """DescribeMonitorProductList请求参数结构体
    """

    def __init__(self):
        r"""描述监控云服务类别，支持项目
        """

    def _deserialize(self, params):
        return
