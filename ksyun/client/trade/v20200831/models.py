from ksyun.common.abstract_model import AbstractModel

class SetRenewalRequest(AbstractModel):
    """SetRenewal请求参数结构体
    """

    def __init__(self):
        r"""批量设置实例续费策略
        :param InstanceIds: 实例id, 多个英文逗号隔开
        :type PathPrefix: String
        :param RenewStrategy: 续费策略， 0 手动续费 1 自动续费
        :type PathPrefix: Int
        :param RenewDuration: 续费时长（月）
当renewStrategy为0时，非必填，当renewStrategy为1时，必填。
        :type PathPrefix: Int
        """
        self.InstanceIds = None
        self.RenewStrategy = None
        self.RenewDuration = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")
        if params.get("RenewStrategy"):
            self.RenewStrategy = params.get("RenewStrategy")
        if params.get("RenewDuration"):
            self.RenewDuration = params.get("RenewDuration")


