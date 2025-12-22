from ksyun.common.abstract_model import AbstractModel

class DeleteCacheSlaveNodeRequest(AbstractModel):
    """DeleteCacheSlaveNode请求参数结构体
    """

    def __init__(self):
        r"""社区版主从实例删除只读实例
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        :param NodeId: 只读节点ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.NodeId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("NodeId"):
            self.NodeId = params.get("NodeId")


