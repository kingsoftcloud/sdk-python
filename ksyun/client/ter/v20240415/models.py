from ksyun.common.abstract_model import AbstractModel

class DescribeStackOutputsRequest(AbstractModel):
    """DescribeStackOutputs请求参数结构体
    """

    def __init__(self):
        r"""查询资源栈输出
        :param StackId: 资源栈ID
        :type PathPrefix: String
        """
        self.StackId = None

    def _deserialize(self, params):
        if params.get("StackId"):
            self.StackId = params.get("StackId")


class DescribeStackEventsRequest(AbstractModel):
    """DescribeStackEvents请求参数结构体
    """

    def __init__(self):
        r"""查询资源栈事件
        :param StackId: 资源栈ID
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大资源栈数目，取值范围5-1000
        :type PathPrefix: Int
        :param Offset: 页码数 从1开始
        :type PathPrefix: Int
        """
        self.StackId = None
        self.MaxResults = None
        self.Offset = None

    def _deserialize(self, params):
        if params.get("StackId"):
            self.StackId = params.get("StackId")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Offset"):
            self.Offset = params.get("Offset")


class DeleteTemplateRequest(AbstractModel):
    """DeleteTemplate请求参数结构体
    """

    def __init__(self):
        r"""删除模板
        :param TemplateId: 
        :type PathPrefix: String
        """
        self.TemplateId = None

    def _deserialize(self, params):
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")


class DescribeTemplateVersionsRequest(AbstractModel):
    """DescribeTemplateVersions请求参数结构体
    """

    def __init__(self):
        r"""查询模板版本
        :param TemplateId: 模板ID
仅支持我的模板ID
        :type PathPrefix: String
        """
        self.TemplateId = None

    def _deserialize(self, params):
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")


class DescribeTemplatesRequest(AbstractModel):
    """DescribeTemplates请求参数结构体
    """

    def __init__(self):
        r"""查询模板
        :param MaxResults: 单次调用所返回的最大模板数目，取值范围5-1000

        :type PathPrefix: Int
        :param TemplateId: 模板Id
        :type PathPrefix: Filter
        :param Offset: 偏移量
        :type PathPrefix: Int
        :param TemplateName: 模板名称
        :type PathPrefix: Filter
        :param TemplateType: 有效值：sample、custom
default：custom
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.TemplateId = None
        self.Offset = None
        self.TemplateName = None
        self.TemplateType = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("TemplateName"):
            self.TemplateName = params.get("TemplateName")
        if params.get("TemplateType"):
            self.TemplateType = params.get("TemplateType")


