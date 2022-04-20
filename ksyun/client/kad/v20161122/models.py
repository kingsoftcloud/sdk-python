from ksyun.common.abstract_model import AbstractModel

class CreateForwardConfRequest(AbstractModel):
    """CreateForwardConf请求参数结构体
    """

    def __init__(self):
        r"""创建四层转发配置
        :param KadId: 高防服务实例ID
        :type PathPrefix: String
        :param Protocol: 转发协议类型，有效值可选TCP或UDP

        :type PathPrefix: String
        :param ServicePort: 服务端口，有效值范围10~65535
        :type PathPrefix: Int
        """
        self.KadId = None
        self.Protocol = None
        self.ServicePort = None

    def _deserialize(self, params):
        if params.get("KadId"):
            self.KadId = params.get("KadId")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("ServicePort"):
            self.ServicePort = params.get("ServicePort")


class DeleteForwardConfRequest(AbstractModel):
    """DeleteForwardConf请求参数结构体
    """

    def __init__(self):
        r"""删除四层转发配置
        :param ForwardConfId: 四层转发配置ID
        :type PathPrefix: String
        """
        self.ForwardConfId = None

    def _deserialize(self, params):
        if params.get("ForwardConfId"):
            self.ForwardConfId = params.get("ForwardConfId")


class DescribeForwardConfRequest(AbstractModel):
    """DescribeForwardConf请求参数结构体
    """

    def __init__(self):
        r"""描述四层转发记录
        :param KadId: 高防服务的实例ID
        :type PathPrefix: String
        :param ForwardConfId: 一个或多个四层转发配置的ID
        :type PathPrefix: Filter
        """
        self.KadId = None
        self.ForwardConfId = None

    def _deserialize(self, params):
        if params.get("KadId"):
            self.KadId = params.get("KadId")
        if params.get("ForwardConfId"):
            self.ForwardConfId = params.get("ForwardConfId")


class CreateForwardSourceRequest(AbstractModel):
    """CreateForwardSource请求参数结构体
    """

    def __init__(self):
        r"""创建四层转发回源配置
        :param ForwardConfId: 四层转发配置的ID
        :type PathPrefix: String
        :param SourceIp: 源站IP
        :type PathPrefix: String
        :param SourcePort: 源站端口
        :type PathPrefix: String
        """
        self.ForwardConfId = None
        self.SourceIp = None
        self.SourcePort = None

    def _deserialize(self, params):
        if params.get("ForwardConfId"):
            self.ForwardConfId = params.get("ForwardConfId")
        if params.get("SourceIp"):
            self.SourceIp = params.get("SourceIp")
        if params.get("SourcePort"):
            self.SourcePort = params.get("SourcePort")


class DeleteForwardSourceRequest(AbstractModel):
    """DeleteForwardSource请求参数结构体
    """

    def __init__(self):
        r"""删除四层转发回源配置
        :param ForwardSourceId: 四层转发源站配置的ID
        :type PathPrefix: String
        """
        self.ForwardSourceId = None

    def _deserialize(self, params):
        if params.get("ForwardSourceId"):
            self.ForwardSourceId = params.get("ForwardSourceId")


class DescribeForwardSourceRequest(AbstractModel):
    """DescribeForwardSource请求参数结构体
    """

    def __init__(self):
        r"""描述四层转发回源配置
        :param ForwardConfId: 四层转发配置ID
        :type PathPrefix: String
        :param ForwardSourceId: 一个或多个四层转发源站配置的ID
        :type PathPrefix: Filter
        """
        self.ForwardConfId = None
        self.ForwardSourceId = None

    def _deserialize(self, params):
        if params.get("ForwardConfId"):
            self.ForwardConfId = params.get("ForwardConfId")
        if params.get("ForwardSourceId"):
            self.ForwardSourceId = params.get("ForwardSourceId")


