from ksyun.common.abstract_model import AbstractModel

class DescribeKnowledgeBaseModelsRequest(AbstractModel):
    """DescribeKnowledgeBaseModels请求参数结构体
    """

    def __init__(self):
        r"""查询模型列表
        :param ModelType: 模型类型：llm|text-embedding|rerank
        :type PathPrefix: String
        """
        self.ModelType = None

    def _deserialize(self, params):
        if params.get("ModelType"):
            self.ModelType = params.get("ModelType")


class ActivateKnowledgeBaseServiceRequest(AbstractModel):
    """ActivateKnowledgeBaseService请求参数结构体
    """

    def __init__(self):
        r"""开通知识库服务
        """

    def _deserialize(self, params):
        return


class RetrieveKnowledgeRequest(AbstractModel):
    """RetrieveKnowledge请求参数结构体
    """

    def __init__(self):
        r"""知识库检索
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param Query: 检索关键词
        :type PathPrefix: String
        :param RetrievalModel: 检索模型配置
        :type PathPrefix: Object
        """
        self.DatasetId = None
        self.Query = None
        self.RetrievalModel = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("Query"):
            self.Query = params.get("Query")
        if params.get("RetrievalModel"):
            self.RetrievalModel = params.get("RetrievalModel")


class DescribeChunkRequest(AbstractModel):
    """DescribeChunk请求参数结构体
    """

    def __init__(self):
        r"""获取切片详情
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param DocumentId: 文档 ID
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.DocumentId = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("DocumentId"):
            self.DocumentId = params.get("DocumentId")


class BatchDisplayStatusRequest(AbstractModel):
    """BatchDisplayStatus请求参数结构体
    """

    def __init__(self):
        r"""批量获取文档索引状态
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param DocumentIds: 文档 ID 列表（上限 100）
        :type PathPrefix: Array
        """
        self.DatasetId = None
        self.DocumentIds = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("DocumentIds"):
            self.DocumentIds = params.get("DocumentIds")


class DisplayStatusRequest(AbstractModel):
    """DisplayStatus请求参数结构体
    """

    def __init__(self):
        r"""获取文档索引状态
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param DocumentId: 文档 ID
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.DocumentId = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("DocumentId"):
            self.DocumentId = params.get("DocumentId")


class IndexingStatusRequest(AbstractModel):
    """IndexingStatus请求参数结构体
    """

    def __init__(self):
        r"""获取文档嵌入状态
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param Batch: 上传批次号
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.Batch = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("Batch"):
            self.Batch = params.get("Batch")


class DeleteDocumentRequest(AbstractModel):
    """DeleteDocument请求参数结构体
    """

    def __init__(self):
        r"""删除知识库文档
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param DocumentId: 文档 ID
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.DocumentId = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("DocumentId"):
            self.DocumentId = params.get("DocumentId")


class DescribeDocumentRequest(AbstractModel):
    """DescribeDocument请求参数结构体
    """

    def __init__(self):
        r"""获取文档详情
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param DocumentId: 文档 ID
        :type PathPrefix: String
        :param Metadata: 返回内容粒度：all / only / without（默认 all）
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.DocumentId = None
        self.Metadata = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("DocumentId"):
            self.DocumentId = params.get("DocumentId")
        if params.get("Metadata"):
            self.Metadata = params.get("Metadata")


class DescribeDocumentsRequest(AbstractModel):
    """DescribeDocuments请求参数结构体
    """

    def __init__(self):
        r"""查看知识库文档列表
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param Keyword: 搜索关键词（目前仅支持文档名称模糊搜）
        :type PathPrefix: String
        :param Page: 页码（从 1 开始，默认 1）
        :type PathPrefix: Int
        :param Limit: 每页条数（1-100，默认 20）
        :type PathPrefix: Int
        """
        self.DatasetId = None
        self.Keyword = None
        self.Page = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class ImportDocumentsRequest(AbstractModel):
    """ImportDocuments请求参数结构体
    """

    def __init__(self):
        r"""创建知识库文档
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param Data: 文档解析与索引配置
        :type PathPrefix: Object
        :param AddType: 上传方式：ks3
        :type PathPrefix: String
        :param Ks3Path: 文件路径（AddType=ks3 时必填）
        :type PathPrefix: Array
        """
        self.DatasetId = None
        self.Data = None
        self.AddType = None
        self.Ks3Path = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("Data"):
            self.Data = params.get("Data")
        if params.get("AddType"):
            self.AddType = params.get("AddType")
        if params.get("Ks3Path"):
            self.Ks3Path = params.get("Ks3Path")


class DeleteKnowledgeBaseRequest(AbstractModel):
    """DeleteKnowledgeBase请求参数结构体
    """

    def __init__(self):
        r"""删除知识库
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        """
        self.DatasetId = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")


class ModifyKnowledgeBaseRequest(AbstractModel):
    """ModifyKnowledgeBase请求参数结构体
    """

    def __init__(self):
        r"""修改知识库配置
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param Name: 知识库名称（选填）
        :type PathPrefix: String
        :param IndexingTechnique: 索引方式（选填）
        :type PathPrefix: String
        :param EmbeddingModelProvider: 嵌入模型提供商（选填）
        :type PathPrefix: String
        :param EmbeddingModel: 嵌入模型（选填）
        :type PathPrefix: String
        :param RetrievalModel: 检索模型（选填）
        :type PathPrefix: Object
        """
        self.DatasetId = None
        self.Name = None
        self.IndexingTechnique = None
        self.EmbeddingModelProvider = None
        self.EmbeddingModel = None
        self.RetrievalModel = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("IndexingTechnique"):
            self.IndexingTechnique = params.get("IndexingTechnique")
        if params.get("EmbeddingModelProvider"):
            self.EmbeddingModelProvider = params.get("EmbeddingModelProvider")
        if params.get("EmbeddingModel"):
            self.EmbeddingModel = params.get("EmbeddingModel")
        if params.get("RetrievalModel"):
            self.RetrievalModel = params.get("RetrievalModel")


class DescribeKnowledgeBaseRequest(AbstractModel):
    """DescribeKnowledgeBase请求参数结构体
    """

    def __init__(self):
        r"""查看知识库详情
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        """
        self.DatasetId = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")


class DescribeKnowledgeBasesRequest(AbstractModel):
    """DescribeKnowledgeBases请求参数结构体
    """

    def __init__(self):
        r"""查看知识库列表
        :param Page: 页码（从 1 开始，默认 1）
        :type PathPrefix: Int
        :param Limit: 每页条数（1-100，默认 20）
        :type PathPrefix: Int
        :param Keyword: 搜索关键词（目前仅支持文档名称模糊搜）
        :type PathPrefix: String
        """
        self.Page = None
        self.Limit = None
        self.Keyword = None

    def _deserialize(self, params):
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")


class CreateKnowledgeBaseRequest(AbstractModel):
    """CreateKnowledgeBase请求参数结构体
    """

    def __init__(self):
        r"""创建知识库
        :param Name: 知识库名称（1-40 字符，不可重名）
        :type PathPrefix: String
        :param IndexingTechnique: 索引方式：intelligence / intelligence_fast / high_quality / economy
        :type PathPrefix: String
        :param RetrievalModel: 检索模型配置
        :type PathPrefix: Object
        """
        self.Name = None
        self.IndexingTechnique = None
        self.RetrievalModel = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("IndexingTechnique"):
            self.IndexingTechnique = params.get("IndexingTechnique")
        if params.get("RetrievalModel"):
            self.RetrievalModel = params.get("RetrievalModel")


class CreateMemorySdkRequest(AbstractModel):
    """CreateMemorySdk请求参数结构体
    """

    def __init__(self):
        r"""向指定记忆库写入记忆
        :param Namespace: 
        :type PathPrefix: String
        :param UserId: 
        :type PathPrefix: String
        :param AgentId: 
        :type PathPrefix: String
        :param SessionId: 
        :type PathPrefix: String
        :param SceneId: 
        :type PathPrefix: String
        :param DataType: 
        :type PathPrefix: String
        :param Data: 
        :type PathPrefix: Object
        """
        self.Namespace = None
        self.UserId = None
        self.AgentId = None
        self.SessionId = None
        self.SceneId = None
        self.DataType = None
        self.Data = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("UserId"):
            self.UserId = params.get("UserId")
        if params.get("AgentId"):
            self.AgentId = params.get("AgentId")
        if params.get("SessionId"):
            self.SessionId = params.get("SessionId")
        if params.get("SceneId"):
            self.SceneId = params.get("SceneId")
        if params.get("DataType"):
            self.DataType = params.get("DataType")
        if params.get("Data"):
            self.Data = params.get("Data")


class QueryMemorySdkRequest(AbstractModel):
    """QueryMemorySdk请求参数结构体
    """

    def __init__(self):
        r"""从记忆库检索记忆
        :param Namespace: 
        :type PathPrefix: String
        :param UserId: 
        :type PathPrefix: String
        :param Query: 
        :type PathPrefix: String
        :param SceneId: 
        :type PathPrefix: String
        :param OccurredAfter: 
        :type PathPrefix: Long
        :param OccurredBefore: 
        :type PathPrefix: Long
        :param Mode: 
        :type PathPrefix: String
        :param ReturnCitations: 
        :type PathPrefix: Boolean
        :param Limit: 
        :type PathPrefix: Int
        """
        self.Namespace = None
        self.UserId = None
        self.Query = None
        self.SceneId = None
        self.OccurredAfter = None
        self.OccurredBefore = None
        self.Mode = None
        self.ReturnCitations = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("UserId"):
            self.UserId = params.get("UserId")
        if params.get("Query"):
            self.Query = params.get("Query")
        if params.get("SceneId"):
            self.SceneId = params.get("SceneId")
        if params.get("OccurredAfter"):
            self.OccurredAfter = params.get("OccurredAfter")
        if params.get("OccurredBefore"):
            self.OccurredBefore = params.get("OccurredBefore")
        if params.get("Mode"):
            self.Mode = params.get("Mode")
        if params.get("ReturnCitations"):
            self.ReturnCitations = params.get("ReturnCitations")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class CreateMemoryCollectionRequest(AbstractModel):
    """CreateMemoryCollection请求参数结构体
    """

    def __init__(self):
        r"""创建记忆库
        :param Name: 记忆库名称；
40位，允许字母、中文、数字、顿号、-、_、
.、\、/、(、)
        :type PathPrefix: String
        :param Description: 记忆库描述；
200位，允许字母、中文、数字、顿号、-、_、\、/、(、)、.、空格
        :type PathPrefix: String
        """
        self.Name = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")


class GetMemoryCollectionRequest(AbstractModel):
    """GetMemoryCollection请求参数结构体
    """

    def __init__(self):
        r"""查询记忆库详情
        :param MemoryCollectionId: 待查询的记忆库唯一 ID，不可为空
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")


class ListMemoryCollectionsRequest(AbstractModel):
    """ListMemoryCollections请求参数结构体
    """

    def __init__(self):
        r"""批量查询记忆库详情
        :param CreateTimeAfter: 秒级时间戳，筛选该时间后创建的记忆库
        :type PathPrefix: Long
        :param CreateTimeBefore: 秒级时间戳，筛选该时间前创建的记忆库
        :type PathPrefix: Long
        :param UpdateTimeAfter: 秒级时间戳，筛选该时间后更新的记忆库
        :type PathPrefix: Long
        :param UpdateTimeBefore: 秒级时间戳，筛选该时间前更新的记忆库
        :type PathPrefix: Long
        :param MemoryCollectionId: 记忆库唯一ID，精确查询
        :type PathPrefix: String
        :param Name: 记忆库名称，精确查询
        :type PathPrefix: String
        :param NameKeyword: 名称关键词，模糊查询
        :type PathPrefix: String
        :param Status: 状态，可选CreateFailed/Ready
        :type PathPrefix: String
        :param Marker: 
        :type PathPrefix: Long
        :param MaxResults: 
        :type PathPrefix: Long
        """
        self.CreateTimeAfter = None
        self.CreateTimeBefore = None
        self.UpdateTimeAfter = None
        self.UpdateTimeBefore = None
        self.MemoryCollectionId = None
        self.Name = None
        self.NameKeyword = None
        self.Status = None
        self.Marker = None
        self.MaxResults = None

    def _deserialize(self, params):
        if params.get("CreateTimeAfter"):
            self.CreateTimeAfter = params.get("CreateTimeAfter")
        if params.get("CreateTimeBefore"):
            self.CreateTimeBefore = params.get("CreateTimeBefore")
        if params.get("UpdateTimeAfter"):
            self.UpdateTimeAfter = params.get("UpdateTimeAfter")
        if params.get("UpdateTimeBefore"):
            self.UpdateTimeBefore = params.get("UpdateTimeBefore")
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("NameKeyword"):
            self.NameKeyword = params.get("NameKeyword")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")


class DeleteMemoryCollectionRequest(AbstractModel):
    """DeleteMemoryCollection请求参数结构体
    """

    def __init__(self):
        r"""删除记忆库
        :param MemoryCollectionId: 待删除的记忆库唯一 ID，不可为空
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")


class GetMemoryBaseServiceRequest(AbstractModel):
    """GetMemoryBaseService请求参数结构体
    """

    def __init__(self):
        r"""查询记忆库服务状态
        """

    def _deserialize(self, params):
        return


class ActivateMemoryBaseServiceRequest(AbstractModel):
    """ActivateMemoryBaseService请求参数结构体
    """

    def __init__(self):
        r"""开通记忆库服务
        """

    def _deserialize(self, params):
        return


class UpdateMemoryCollectionRequest(AbstractModel):
    """UpdateMemoryCollection请求参数结构体
    """

    def __init__(self):
        r"""修改记忆库信息
        :param MemoryCollectionId: 待修改的记忆库唯一 ID，不可为空
        :type PathPrefix: String
        :param Description: 记忆库描述；
200位，允许字母、中文、数字、顿号、-、_、\、/、(、)、.、空格
不传则不修改原有描述
        :type PathPrefix: String
        :param Name: 记忆库名称；
40位，允许字母、中文、数字、顿号、-、_、
.、\、/、(、)
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None
        self.Description = None
        self.Name = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Name"):
            self.Name = params.get("Name")


class DeleteMcpServerRequest(AbstractModel):
    """DeleteMcpServer请求参数结构体
    """

    def __init__(self):
        r"""删除自定义MCP服务
        :param McpServerId: MCP服务ID（必填）
        :type PathPrefix: String
        """
        self.McpServerId = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")


class ModifyMcpServerRequest(AbstractModel):
    """ModifyMcpServer请求参数结构体
    """

    def __init__(self):
        r"""修改自定义MCP服务
        :param McpServerId: MCP服务ID（必填）
        :type PathPrefix: String
        :param McpServerName: MCP服务名称（1-64字符）
        :type PathPrefix: String
        :param Description: 描述（1-255字符）
        :type PathPrefix: String
        :param Introduction: 介绍
        :type PathPrefix: String
        :param OutboundAuthFieldValue: 后端服务出向认证字段值
        :type PathPrefix: String
        :param HttpApiConfig: HTTP API配置（McpType=HttpToMcp时必填，base64格式）
        :type PathPrefix: String
        :param HttpApiConfigUpdateType: HTTP API配置更新方式：Ignore / Replace（工具名称相同时，Ignore=忽略，Replace=替换更新）
        :type PathPrefix: String
        """
        self.McpServerId = None
        self.McpServerName = None
        self.Description = None
        self.Introduction = None
        self.OutboundAuthFieldValue = None
        self.HttpApiConfig = None
        self.HttpApiConfigUpdateType = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")
        if params.get("McpServerName"):
            self.McpServerName = params.get("McpServerName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Introduction"):
            self.Introduction = params.get("Introduction")
        if params.get("OutboundAuthFieldValue"):
            self.OutboundAuthFieldValue = params.get("OutboundAuthFieldValue")
        if params.get("HttpApiConfig"):
            self.HttpApiConfig = params.get("HttpApiConfig")
        if params.get("HttpApiConfigUpdateType"):
            self.HttpApiConfigUpdateType = params.get("HttpApiConfigUpdateType")


class CreateMcpServerRequest(AbstractModel):
    """CreateMcpServer请求参数结构体
    """

    def __init__(self):
        r"""创建自定义MCP服务
        :param McpServerName: MCP服务名称（必填，1-64字符）
        :type PathPrefix: String
        :param McpServerNameEn: MCP服务英文名称（必填，英文/数字/下划线/中划线，1-64字符）
        :type PathPrefix: String
        :param Description: 描述（1-255字符）
        :type PathPrefix: String
        :param Introduction: 介绍
        :type PathPrefix: String
        :param ServiceProtocol: 服务协议：SSE / StreamableHTTP
        :type PathPrefix: String
        :param BackendServiceUrl: 后端服务URL
        :type PathPrefix: String
        :param AllowCustomAuth: 是否允许自定义认证
        :type PathPrefix: Boolean
        :param ServiceCustomHeaders: 服务自定义请求头
        :type PathPrefix: String
        :param OutboundAuthLocation: 后端服务出向认证位置：Query / Header
        :type PathPrefix: String
        :param OutboundAuthFieldName: 后端服务出向认证字段名
        :type PathPrefix: String
        :param OutboundAuthFieldValue: 后端服务出向认证字段值
        :type PathPrefix: String
        :param McpRuntimeConfig: MCP运行时配置（McpType=ProxyRuntime时必填）
        :type PathPrefix: Object
        :param HttpApiConfig: HTTP API配置（McpType=HttpToMcp时必填，base64格式）
        :type PathPrefix: String
        :param McpType: MCP类型：Proxy / HttpToMcp / ProxyRuntime）
        :type PathPrefix: String
        """
        self.McpServerName = None
        self.McpServerNameEn = None
        self.Description = None
        self.Introduction = None
        self.ServiceProtocol = None
        self.BackendServiceUrl = None
        self.AllowCustomAuth = None
        self.ServiceCustomHeaders = None
        self.OutboundAuthLocation = None
        self.OutboundAuthFieldName = None
        self.OutboundAuthFieldValue = None
        self.McpRuntimeConfig = None
        self.HttpApiConfig = None
        self.McpType = None

    def _deserialize(self, params):
        if params.get("McpServerName"):
            self.McpServerName = params.get("McpServerName")
        if params.get("McpServerNameEn"):
            self.McpServerNameEn = params.get("McpServerNameEn")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Introduction"):
            self.Introduction = params.get("Introduction")
        if params.get("ServiceProtocol"):
            self.ServiceProtocol = params.get("ServiceProtocol")
        if params.get("BackendServiceUrl"):
            self.BackendServiceUrl = params.get("BackendServiceUrl")
        if params.get("AllowCustomAuth"):
            self.AllowCustomAuth = params.get("AllowCustomAuth")
        if params.get("ServiceCustomHeaders"):
            self.ServiceCustomHeaders = params.get("ServiceCustomHeaders")
        if params.get("OutboundAuthLocation"):
            self.OutboundAuthLocation = params.get("OutboundAuthLocation")
        if params.get("OutboundAuthFieldName"):
            self.OutboundAuthFieldName = params.get("OutboundAuthFieldName")
        if params.get("OutboundAuthFieldValue"):
            self.OutboundAuthFieldValue = params.get("OutboundAuthFieldValue")
        if params.get("McpRuntimeConfig"):
            self.McpRuntimeConfig = params.get("McpRuntimeConfig")
        if params.get("HttpApiConfig"):
            self.HttpApiConfig = params.get("HttpApiConfig")
        if params.get("McpType"):
            self.McpType = params.get("McpType")


class DescribeMcpServersRequest(AbstractModel):
    """DescribeMcpServers请求参数结构体
    """

    def __init__(self):
        r"""查询自定义MCP服务
        :param McpServerIds: MCP服务ID列表
        :type PathPrefix: Array
        :param NameKeyword: 名称关键词
        :type PathPrefix: String
        :param Region: 区域
        :type PathPrefix: String
        """
        self.McpServerIds = None
        self.NameKeyword = None
        self.Region = None

    def _deserialize(self, params):
        if params.get("McpServerIds"):
            self.McpServerIds = params.get("McpServerIds")
        if params.get("NameKeyword"):
            self.NameKeyword = params.get("NameKeyword")
        if params.get("Region"):
            self.Region = params.get("Region")


class DescribeMcpOfficialServersRequest(AbstractModel):
    """DescribeMcpOfficialServers请求参数结构体
    """

    def __init__(self):
        r"""查询MCP官方服务
        :param McpServerIds: MCP服务ID列表
        :type PathPrefix: Array
        :param NameKeyword: 名称关键词
        :type PathPrefix: String
        :param Region: 区域
        :type PathPrefix: String
        """
        self.McpServerIds = None
        self.NameKeyword = None
        self.Region = None

    def _deserialize(self, params):
        if params.get("McpServerIds"):
            self.McpServerIds = params.get("McpServerIds")
        if params.get("NameKeyword"):
            self.NameKeyword = params.get("NameKeyword")
        if params.get("Region"):
            self.Region = params.get("Region")


class DeactivateMcpOfficialServerRequest(AbstractModel):
    """DeactivateMcpOfficialServer请求参数结构体
    """

    def __init__(self):
        r"""取消MCP官方服务
        :param McpServerId: MCP服务ID
        :type PathPrefix: String
        """
        self.McpServerId = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")


class ActivateMcpOfficialServerRequest(AbstractModel):
    """ActivateMcpOfficialServer请求参数结构体
    """

    def __init__(self):
        r"""激活MCP官方服务
        :param McpServerId: MCP服务ID
        :type PathPrefix: String
        :param AuthFieldValue: 认证字段值
        :type PathPrefix: String
        """
        self.McpServerId = None
        self.AuthFieldValue = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")
        if params.get("AuthFieldValue"):
            self.AuthFieldValue = params.get("AuthFieldValue")


class DescribeMcpSquaresRequest(AbstractModel):
    """DescribeMcpSquares请求参数结构体
    """

    def __init__(self):
        r"""查询MCP广场
        :param McpServerIds: MCP服务ID列表
        :type PathPrefix: Array
        :param NameKeyword: 名称关键词
        :type PathPrefix: String
        """
        self.McpServerIds = None
        self.NameKeyword = None

    def _deserialize(self, params):
        if params.get("McpServerIds"):
            self.McpServerIds = params.get("McpServerIds")
        if params.get("NameKeyword"):
            self.NameKeyword = params.get("NameKeyword")


class GetMcpOfficialServerDetailRequest(AbstractModel):
    """GetMcpOfficialServerDetail请求参数结构体
    """

    def __init__(self):
        r"""查询MCP官方服务详情
        :param McpServerId: MCP服务ID
        :type PathPrefix: String
        """
        self.McpServerId = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")


class GetMcpServerDetailRequest(AbstractModel):
    """GetMcpServerDetail请求参数结构体
    """

    def __init__(self):
        r"""查询自定义MCP服务详情
        :param McpServerId: MCP服务ID
        :type PathPrefix: String
        """
        self.McpServerId = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")


class GetMcpSquareDetailRequest(AbstractModel):
    """GetMcpSquareDetail请求参数结构体
    """

    def __init__(self):
        r"""查询MCP广场详情
        :param McpServerId: MCP服务ID
        :type PathPrefix: String
        """
        self.McpServerId = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")


