from ksyun.common.abstract_model import AbstractModel

class CreateAlarmPolicyRequest(AbstractModel):
    """CreateAlarmPolicy请求参数结构体
    """

    def __init__(self):
        r"""创建告警策略
        :param PolicyName: 策略名称	
        :type PathPrefix: String
        :param ProductType: 云服务类别，详见 [云服务类别](云服务类别)
        :type PathPrefix: Int
        :param PolicyType: 策略类型。取值：
- 0：普通策略 
- 1：默认策略	
        :type PathPrefix: Int
        :param ResourceBindType: 策略所关联资源，绑定方式。取值： 
- 1：全部实例
- 2：按照项目组维度
- 3：自选实例
        :type PathPrefix: Int
        :param ProjectId: 项目组ID。 

> **注意**：有且当 ResourceBindType=2时，该字段必填


        :type PathPrefix: Int
        :param InstanceIds: 实例ID。

> **注意：** 有且当 ResourceBindType=3时，该字段必填	
        :type PathPrefix: Array
        :param TriggerRules: 配置触发告警的规则列表
        :type PathPrefix: Array
        :param UserNotice: 绑定告警联系人/联系组列表
        :type PathPrefix: Array
        :param URLNotice: 告警回调Webhook地址。
> **注意：** 最多可添加5个回调地址。
        :type PathPrefix: Array
        """
        self.PolicyName = None
        self.ProductType = None
        self.PolicyType = None
        self.ResourceBindType = None
        self.ProjectId = None
        self.InstanceIds = None
        self.TriggerRules = None
        self.UserNotice = None
        self.URLNotice = None

    def _deserialize(self, params):
        if params.get("PolicyName"):
            self.PolicyName = params.get("PolicyName")
        if params.get("ProductType"):
            self.ProductType = params.get("ProductType")
        if params.get("PolicyType"):
            self.PolicyType = params.get("PolicyType")
        if params.get("ResourceBindType"):
            self.ResourceBindType = params.get("ResourceBindType")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("TriggerRules"):
            self.TriggerRules = params.get("TriggerRules")
        if params.get("UserNotice"):
            self.UserNotice = params.get("UserNotice")
        if params.get("URLNotice"):
            self.URLNotice = params.get("URLNotice")


class DeleteAlarmPolicyRequest(AbstractModel):
    """DeleteAlarmPolicy请求参数结构体
    """

    def __init__(self):
        r"""删除告警策略
        :param PolicyIds: 告警策略ID。

> **说明：** 支持同时删除多个策略。
        :type PathPrefix: Array
        """
        self.PolicyIds = None

    def _deserialize(self, params):
        if params.get("PolicyIds"):
            self.PolicyIds = params.get("PolicyIds")


