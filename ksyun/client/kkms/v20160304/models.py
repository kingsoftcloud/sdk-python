from ksyun.common.abstract_model import AbstractModel


class CreateKeyRequest(AbstractModel):
    """CreateKey请求参数结构体
    """

    def __init__(self):
        r"""创建用户的主密钥
        :param KeyName: 客户主KEY的名称
        :type PathPrefix: String
        :param Description: 备注
        :type PathPrefix: String
        :param KeyUsage: 客户主KEY的用途，仅可用于对称加密和解密
        :type PathPrefix: String
        :param Origin: 客户的主KEY的来源
        :type PathPrefix: String
        :param ChargeType: KKMS的计费类型
        :type PathPrefix: String
        """
        self.KeyName = None
        self.Description = None
        self.KeyUsage = None
        self.Origin = None
        self.ChargeType = None

    def _deserialize(self, params):
        if params.get("KeyName"):
            self.KeyName = params.get("KeyName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("KeyUsage"):
            self.KeyUsage = params.get("KeyUsage")
        if params.get("Origin"):
            self.Origin = params.get("Origin")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")


class ModifyKeyRequest(AbstractModel):
    """ModifyKey请求参数结构体
    """

    def __init__(self):
        r"""修改用户主密钥
        :param KeyId: 客户主KEY的ID
        :type PathPrefix: String
        :param KeyName: 客户主KEY的名称
        :type PathPrefix: String
        :param Description: 备注
        :type PathPrefix: String
        """
        self.KeyId = None
        self.KeyName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("KeyName"):
            self.KeyName = params.get("KeyName")
        if params.get("Description"):
            self.Description = params.get("Description")


class ModifyKeyStateRequest(AbstractModel):
    """ModifyKeyState请求参数结构体
    """

    def __init__(self):
        r"""修改用户主密钥的状态
        :param KeyId: 客户主KEY的ID
        :type PathPrefix: String
        :param KeyState: KEY的状态
        :type PathPrefix: String
        """
        self.KeyId = None
        self.KeyState = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("KeyState"):
            self.KeyState = params.get("KeyState")


class DeleteKeyRequest(AbstractModel):
    """DeleteKey请求参数结构体
    """

    def __init__(self):
        r"""删除用户主密钥
        :param KeyId: 客户主KEY的ID
        :type PathPrefix: String
        """
        self.KeyId = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys请求参数结构体
    """

    def __init__(self):
        r"""查询用户主密钥信息
        :param KeyId: 客户主KEY的ID
        :type PathPrefix: Filter
        """
        self.KeyId = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")


class EncryptRequest(AbstractModel):
    """Encrypt请求参数结构体
    """

    def __init__(self):
        r"""加密明文数据
        :param KeyId: 客户主KEY的ID
        :type PathPrefix: String
        :param Plaintext: 明文数据，最多长度不超过4096
        :type PathPrefix: String
        """
        self.KeyId = None
        self.Plaintext = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("Plaintext"):
            self.Plaintext = params.get("Plaintext")


class DecryptRequest(AbstractModel):
    """Decrypt请求参数结构体
    """

    def __init__(self):
        r"""解密密文数据
        :param KeyId: 客户主KEY的ID
        :type PathPrefix: String
        :param CiphertextBlob: 密文数据
        :type PathPrefix: String
        """
        self.KeyId = None
        self.CiphertextBlob = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("CiphertextBlob"):
            self.CiphertextBlob = params.get("CiphertextBlob")


class GenerateDataKeyRequest(AbstractModel):
    """GenerateDataKey请求参数结构体
    """

    def __init__(self):
        r"""创建数据密钥
        :param KeyId: 客户主KEY的ID
        :type PathPrefix: String
        :param KeySpec: 数据加密密钥（DataKey）的长度。使用AES128生成128位对称密钥，或AES256生成256位对称密钥
        :type PathPrefix: String
        :param NumberOfBytes: DataKey的长度为字节。例如，使用值64生成512位。数据键（64字节为512位）。对于公共密钥长度（128位和256位对称密钥），我们建议您使用KEYSPEC字段，而不是使用此键字段。
        :type PathPrefix: Int
        """
        self.KeyId = None
        self.KeySpec = None
        self.NumberOfBytes = None

    def _deserialize(self, params):
        if params.get("KeyId"):
            self.KeyId = params.get("KeyId")
        if params.get("KeySpec"):
            self.KeySpec = params.get("KeySpec")
        if params.get("NumberOfBytes"):
            self.NumberOfBytes = params.get("NumberOfBytes")
