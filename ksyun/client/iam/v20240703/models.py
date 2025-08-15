from ksyun.common.abstract_model import AbstractModel

class ProjectsInfoByInstanceIdsRequest(AbstractModel):
    """ProjectsInfoByInstanceIds请求参数结构体
    """

    def __init__(self):
        r"""根据实例ID查询所属项目
        :param InstanceIds: 实例ID，多个英文逗号分隔，min:1 max:100
        :type PathPrefix: String
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


