from ksyun.common.abstract_model import AbstractModel

class CreateAlarmPolicyRequest(AbstractModel):
    """CreateAlarmPolicy请求参数结构体
    """

    def __init__(self):
        r"""创建告警策略
        """

    def _deserialize(self, params):
        return


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
