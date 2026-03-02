from ksyun.common.abstract_model import AbstractModel

class QueryAnswerRequest(AbstractModel):
    """QueryAnswer请求参数结构体
    """

    def __init__(self):
        r"""获取安全代答内容
        :param AppId: 防护应用ID
        :type PathPrefix: String
        :param MsgId: 消息ID
        :type PathPrefix: String
        :param UseStream: 是否返回流式结果：0-非流式，1-流式
        :type PathPrefix: Int
        """
        self.AppId = None
        self.MsgId = None
        self.UseStream = None

    def _deserialize(self, params):
        if params.get("AppId"):
            self.AppId = params.get("AppId")
        if params.get("MsgId"):
            self.MsgId = params.get("MsgId")
        if params.get("UseStream"):
            self.UseStream = params.get("UseStream")


class CheckModerateRequest(AbstractModel):
    """CheckModerate请求参数结构体
    """

    def __init__(self):
        r"""检测模型输入和输出内容
        :param AppId: 防护应用ID
        :type PathPrefix: String
        :param MsgId: 消息ID，用于流式检测场景
        :type PathPrefix: String
        :param UseStream: 流式状态：0-非流式，1-流式，2-流式结束
        :type PathPrefix: Int
        :param Message: 
        :type PathPrefix: Object
        :param History: 
        :type PathPrefix: Array
        """
        self.AppId = None
        self.MsgId = None
        self.UseStream = None
        self.Message = None
        self.History = None

    def _deserialize(self, params):
        if params.get("AppId"):
            self.AppId = params.get("AppId")
        if params.get("MsgId"):
            self.MsgId = params.get("MsgId")
        if params.get("UseStream"):
            self.UseStream = params.get("UseStream")
        if params.get("Message"):
            self.Message = params.get("Message")
        if params.get("History"):
            self.History = params.get("History")


