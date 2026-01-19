from ksyun.common.abstract_model import AbstractModel

class CreateKeyRequest(AbstractModel):
    """CreateKey请求参数结构体
    """

    def __init__(self):
        r"""创建密钥对
        :param projectId: 项目制ID
        :type PathPrefix: String
        :param KeyName: 秘钥名称
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        """
        self.projectId = None
        self.KeyName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("projectId"):
            self.projectId = params.get("projectId")
        if params.get("KeyName"):
            self.KeyName = params.get("KeyName")
        if params.get("Description"):
            self.Description = params.get("Description")


class ImportKeyRequest(AbstractModel):
    """ImportKey请求参数结构体
    """

    def __init__(self):
        r"""导入密钥
        :param KeyName: 密钥名称
        :type PathPrefix: String
        :param PublicKey: 公钥信息
        :type PathPrefix: String
        :param Description: 描述
        :type PathPrefix: String
        :param IsCheck: 是否校验密钥合法性
true:校验
false:不校验
        :type PathPrefix: Boolean
        """
        self.KeyName = None
        self.PublicKey = None
        self.Description = None
        self.IsCheck = None

    def _deserialize(self, params):
        if params.get("KeyName"):
            self.KeyName = params.get("KeyName")
        if params.get("PublicKey"):
            self.PublicKey = params.get("PublicKey")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("IsCheck"):
            self.IsCheck = params.get("IsCheck")


class DeleteKeyRequest(AbstractModel):
    """DeleteKey请求参数结构体
    """

    def __init__(self):
        r"""删除密钥
        :param KeyId: 密钥Id
        :type PathPrefix: String
        """
        self.KeyId = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")


class ModifyKeyRequest(AbstractModel):
    """ModifyKey请求参数结构体
    """

    def __init__(self):
        r"""修改密钥信息
        :param KeyName: 密钥名称
        :type PathPrefix: String
        :param KeyId: 密钥Id
        :type PathPrefix: String
        """
        self.KeyName = None
        self.KeyId = None

    def _deserialize(self, params):
        if params.get("KeyName"):
            self.KeyName = params.get("KeyName")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys请求参数结构体
    """

    def __init__(self):
        r"""获取密钥列表信息
        :param MaxResults: 单次调用可返回的最大条目数量
        :type PathPrefix: Int
        :param NextToken: 获取另一页返回结果的 token.
        :type PathPrefix: String
        :param KeyId: 密钥ID
        :type PathPrefix: Filter
        :param Filter: 筛选Filter
        :type PathPrefix: Filter
        :param ProjectId: 项目制ID
        :type PathPrefix: Filter
        """
        self.MaxResults = None
        self.NextToken = None
        self.KeyId = None
        self.Filter = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("NextToken"):
            self.NextToken = params.get("NextToken")
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


