from ksyun.common.abstract_model import AbstractModel


class ListInstanceSupportBillTypesRequest(AbstractModel):
    """ListInstanceSupportBillTypes请求参数结构体
    """

    def __init__(self):
        r"""实例转正，支持重新指定正式实例的计费方式，实例获取支持的计费方式列表
        :param instanceId: 实例ID
        :type PathPrefix: String
        """
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class AddTrialToBuyTaskRequest(AbstractModel):
    """AddTrialToBuyTask请求参数结构体
    """

    def __init__(self):
        r"""添加定时转正的任务，支持到期转正和指定时间点转正。 可重复提交，最后一次提交会覆盖之前的提交，相当于更新。
        :param instanceId: 实例id
        :type PathPrefix: String
        :param billType: 计费方式。默认按照当前实例的计费方式进行转正。支持的计费方式列表通过ListInstanceSupportBillTypes接口获取
        :type PathPrefix: Int
        :param duration: 转正为包年包月时，必须填写正式实例购买时长，单位月
        :type PathPrefix: Int
        :param autoTrialToBuyDate: 指定转正日期，格式为yyyy-MM-dd HH:mm:ss。默认是到期时间点转正。
        :type PathPrefix: String
        """
        self.instanceId = None
        self.billType = None
        self.duration = None
        self.autoTrialToBuyDate = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")
        if params.get("billType"):
            self.billType = params.get("billType")
        if params.get("duration"):
            self.duration = params.get("duration")
        if params.get("autoTrialToBuyDate"):
            self.autoTrialToBuyDate = params.get("autoTrialToBuyDate")


class DeleteTrialToBuyTaskRequest(AbstractModel):
    """DeleteTrialToBuyTask请求参数结构体
    """

    def __init__(self):
        r"""取消已经提交的转正任务。
        :param instanceId: 实例id
        :type PathPrefix: String
        """
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class CreateTrialToBuyNowRequest(AbstractModel):
    """CreateTrialToBuyNow请求参数结构体
    """

    def __init__(self):
        r"""创建转正订单，立即将实例转成正式实例。
        :param instanceId: 实例ID
        :type PathPrefix: String
        :param billType: 计费方式。默认按照当前实例的计费方式进行转正。支持的计费方式列表通过ListInstanceSupportBillTypes接口获取
        :type PathPrefix: Int
        :param duration: 转正为包年包月时，必须填写正式实例购买时长，单位月
        :type PathPrefix: Int
        """
        self.instanceId = None
        self.billType = None
        self.duration = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")
        if params.get("billType"):
            self.billType = params.get("billType")
        if params.get("duration"):
            self.duration = params.get("duration")
