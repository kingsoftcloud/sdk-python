from ksyun.common.abstract_model import AbstractModel

class DescribeCacheByRoleRequest(AbstractModel):
    """DescribeCacheByRole请求参数结构体
    """

    def __init__(self):
        r"""缓存服务查询角色节点列表
        :param CacheId: 
        :type PathPrefix: String
        :param Role: 节点角色。默认为“ALL”查询全部角色。可选：MASTER、SLAVE、PROXY、ALL.
        :type PathPrefix: String
        """
        self.CacheId = None
        self.Role = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Role"):
            self.Role = params.get("Role")


