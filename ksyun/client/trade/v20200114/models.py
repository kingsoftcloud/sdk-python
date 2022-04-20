from ksyun.common.abstract_model import AbstractModel

class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体
    """

    def __init__(self):
        r"""实例信息描述
        :param InstanceIds: 实例Id（多个英文逗号隔开）
        :type PathPrefix: String
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


