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
        :param IndexingTechnique: 索引方式（选填）：intelligence_fast
        :type PathPrefix: String
        :param EmbeddingModelProvider: 嵌入模型提供商（选填）
        :type PathPrefix: String
        :param EmbeddingModel: 嵌入模型（选填）
        :type PathPrefix: String
        :param RetrievalModel: 检索模型（选填）
        :type PathPrefix: Object
        :param ComputeUnit: 计算资源数
        :type PathPrefix: Int
        """
        self.DatasetId = None
        self.Name = None
        self.IndexingTechnique = None
        self.EmbeddingModelProvider = None
        self.EmbeddingModel = None
        self.RetrievalModel = None
        self.ComputeUnit = None

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
        if params.get("ComputeUnit"):
            self.ComputeUnit = params.get("ComputeUnit")


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
        :param IndexingTechnique: 索引方式：intelligence_fast
        :type PathPrefix: String
        :param RetrievalModel: 检索模型配置
        :type PathPrefix: Object
        :param ComputeUnit: 计算资源数
        :type PathPrefix: Int
        :param ProjectId: 项目ID
        :type PathPrefix: String
        :param ChargeType: 计费方式
        :type PathPrefix: String
        """
        self.Name = None
        self.IndexingTechnique = None
        self.RetrievalModel = None
        self.ComputeUnit = None
        self.ProjectId = None
        self.ChargeType = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("IndexingTechnique"):
            self.IndexingTechnique = params.get("IndexingTechnique")
        if params.get("RetrievalModel"):
            self.RetrievalModel = params.get("RetrievalModel")
        if params.get("ComputeUnit"):
            self.ComputeUnit = params.get("ComputeUnit")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")


class CreateMemorySdkRequest(AbstractModel):
    """CreateMemorySdk请求参数结构体
    """

    def __init__(self):
        r"""向指定记忆库写入记忆
        :param AgentId: 运行时Agent id，标签
        :type PathPrefix: String
        :param SessionId: 对话ID，区分多个对话
        :type PathPrefix: String
        :param SceneId: 场景ID，用来区分各个场景，提供精细化记忆提取策略
可选：
"_sys_work_assistant"、"_sys_travel_assistant"、"_sys_ai_chat_assistant"、"_sys_coding_assistant"、 "_sys_general"
        :type PathPrefix: String
        :param DataType: input对应的数据类型
        :type PathPrefix: String
        :param Data: 原始数据内容
        :type PathPrefix: Object
        :param AgentUserId: 与Agent交互的用户唯一标识
        :type PathPrefix: String
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        :param Flush: 强制提取记忆
> true: 强制当前seesion下的原始对话切分并提取记忆，false: 走默认流程
        :type PathPrefix: Boolean
        """
        self.AgentId = None
        self.SessionId = None
        self.SceneId = None
        self.DataType = None
        self.Data = None
        self.AgentUserId = None
        self.MemoryCollectionId = None
        self.Flush = None

    def _deserialize(self, params):
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
        if params.get("AgentUserId"):
            self.AgentUserId = params.get("AgentUserId")
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("Flush"):
            self.Flush = params.get("Flush")


class QueryMemorySdkRequest(AbstractModel):
    """QueryMemorySdk请求参数结构体
    """

    def __init__(self):
        r"""从记忆库检索记忆
        :param Query: 查询文本

        :type PathPrefix: String
        :param SceneId: 场景ID，用来区分各个场景，提供精细化记忆提取策略
可选：
"_sys_work_assistant"、"_sys_travel_assistant"、"_sys_ai_chat_assistant"、"_sys_coding_assistant"、 "_sys_general"
        :type PathPrefix: String
        :param OccurredAfter: 记忆事实发生时间（毫秒），左边界
        :type PathPrefix: Long
        :param OccurredBefore: 记忆事实发生时间（毫秒），右边界
        :type PathPrefix: Long
        :param Mode: 检索方式：default（默认，性能型）、agentic（效果型）
        :type PathPrefix: String
        :param ReturnCitations: 是否返回记忆关联的原始数据
        :type PathPrefix: Boolean
        :param Limit: 返回数量限制
        :type PathPrefix: Int
        :param SceneIds: 场景ID列表
        :type PathPrefix: Array
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        :param AgentUserId: 与Agent交互的用户唯一标识
        :type PathPrefix: String
        """
        self.Query = None
        self.SceneId = None
        self.OccurredAfter = None
        self.OccurredBefore = None
        self.Mode = None
        self.ReturnCitations = None
        self.Limit = None
        self.SceneIds = None
        self.MemoryCollectionId = None
        self.AgentUserId = None

    def _deserialize(self, params):
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
        if params.get("SceneIds"):
            self.SceneIds = params.get("SceneIds")
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("AgentUserId"):
            self.AgentUserId = params.get("AgentUserId")


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
        :param LongTermConfiguration: 
        :type PathPrefix: Object
        :param MemoryType: 记忆库类型：1-基础版，2-专业版，3-企业版
        :type PathPrefix: String
        :param ProjectId: 项目ID
        :type PathPrefix: String
        :param ChargeType: 计费方式
        :type PathPrefix: String
        """
        self.Name = None
        self.Description = None
        self.LongTermConfiguration = None
        self.MemoryType = None
        self.ProjectId = None
        self.ChargeType = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("LongTermConfiguration"):
            self.LongTermConfiguration = params.get("LongTermConfiguration")
        if params.get("MemoryType"):
            self.MemoryType = params.get("MemoryType")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ChargeType"):
            self.ChargeType = params.get("ChargeType")


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
        :param LongTermConfiguration: 
        :type PathPrefix: Object
        """
        self.MemoryCollectionId = None
        self.Description = None
        self.Name = None
        self.LongTermConfiguration = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("LongTermConfiguration"):
            self.LongTermConfiguration = params.get("LongTermConfiguration")


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


class ListSessionsRequest(AbstractModel):
    """ListSessions请求参数结构体
    """

    def __init__(self):
        r"""查询会话列表
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        :param AgentUserId: 与Agent交互的用户唯一标识
        :type PathPrefix: String
        :param Query: 查询会话内容
        :type PathPrefix: String
        :param Page: 起始页码
        :type PathPrefix: Int
        :param PageSize: 页大小
        :type PathPrefix: Int
        :param CreatedAfter: 毫秒级时间戳
        :type PathPrefix: Int
        :param CreatedBefore: 毫秒级时间戳
        :type PathPrefix: Int
        """
        self.MemoryCollectionId = None
        self.AgentUserId = None
        self.Query = None
        self.Page = None
        self.PageSize = None
        self.CreatedAfter = None
        self.CreatedBefore = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("AgentUserId"):
            self.AgentUserId = params.get("AgentUserId")
        if params.get("Query"):
            self.Query = params.get("Query")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("CreatedAfter"):
            self.CreatedAfter = params.get("CreatedAfter")
        if params.get("CreatedBefore"):
            self.CreatedBefore = params.get("CreatedBefore")


class AddSessionRequest(AbstractModel):
    """AddSession请求参数结构体
    """

    def __init__(self):
        r"""创建记忆会话
        """

    def _deserialize(self, params):
        return


class QueryMemoryCollectionMetricsRequest(AbstractModel):
    """QueryMemoryCollectionMetrics请求参数结构体
    """

    def __init__(self):
        r"""查询指定记忆库的监控指标时间序列数据
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        :param StartTime: 开始时间，unix秒级时间戳
        :type PathPrefix: Long
        :param EndTime: 结束时间，unix秒级时间戳
        :type PathPrefix: Long
        """
        self.MemoryCollectionId = None
        self.StartTime = None
        self.EndTime = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")


class QuerySessionMemoriesRequest(AbstractModel):
    """QuerySessionMemories请求参数结构体
    """

    def __init__(self):
        r"""查询会话记忆
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        :param SessionId: 对话ID，区分多个对话
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None
        self.SessionId = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("SessionId"):
            self.SessionId = params.get("SessionId")


class RetrieveHistoriesRequest(AbstractModel):
    """RetrieveHistories请求参数结构体
    """

    def __init__(self):
        r"""知识库检索历史记录
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param Page: 页码（1-1000，默认 1）
        :type PathPrefix: Int
        :param Limit: 每页条数（1-100，默认 20）
        :type PathPrefix: Int
        """
        self.DatasetId = None
        self.Page = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class ReindexDocumentsRequest(AbstractModel):
    """ReindexDocuments请求参数结构体
    """

    def __init__(self):
        r"""重索引知识库文档
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param DocumentIds: 文档 ID 列表
        :type PathPrefix: Array
        """
        self.DatasetId = None
        self.DocumentIds = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("DocumentIds"):
            self.DocumentIds = params.get("DocumentIds")


class ModifyDocumentStatusRequest(AbstractModel):
    """ModifyDocumentStatus请求参数结构体
    """

    def __init__(self):
        r"""修改知识库文档状态
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param DocumentId: 文档 ID
        :type PathPrefix: String
        :param Status: 文档状态：enable（启用）/ disable（禁用）
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.DocumentId = None
        self.Status = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("DocumentId"):
            self.DocumentId = params.get("DocumentId")
        if params.get("Status"):
            self.Status = params.get("Status")


class GetApiDetailRequest(AbstractModel):
    """GetApiDetail请求参数结构体
    """

    def __init__(self):
        r"""查询云产品OpenAPI详情
        :param ApiService: 服务名称（必填）
        :type PathPrefix: String
        :param ApiName: API名称（必填）
        :type PathPrefix: String
        :param ApiVersion: 版本号（必填）
        :type PathPrefix: String
        """
        self.ApiService = None
        self.ApiName = None
        self.ApiVersion = None

    def _deserialize(self, params):
        if params.get("ApiService"):
            self.ApiService = params.get("ApiService")
        if params.get("ApiName"):
            self.ApiName = params.get("ApiName")
        if params.get("ApiVersion"):
            self.ApiVersion = params.get("ApiVersion")


class GetApiOverviewRequest(AbstractModel):
    """GetApiOverview请求参数结构体
    """

    def __init__(self):
        r"""查询云产品OpenAPI概览列表
        :param ApiService: 服务名称（必填）
        :type PathPrefix: String
        :param ApiVersion: 版本号，不填则查询所有版本
        :type PathPrefix: String
        """
        self.ApiService = None
        self.ApiVersion = None

    def _deserialize(self, params):
        if params.get("ApiService"):
            self.ApiService = params.get("ApiService")
        if params.get("ApiVersion"):
            self.ApiVersion = params.get("ApiVersion")


class GetProductListRequest(AbstractModel):
    """GetProductList请求参数结构体
    """

    def __init__(self):
        r"""查询云产品列表
        """

    def _deserialize(self, params):
        return


class DescribeMcpRuntimeMetricsRequest(AbstractModel):
    """DescribeMcpRuntimeMetrics请求参数结构体
    """

    def __init__(self):
        r"""查询MCP运行监控（只有部署方式为代码方式部署的MCP才有）
        :param McpServerId: MCP服务ID
        :type PathPrefix: String
        :param StartTime: 开始时间（Unix时间戳，秒）
        :type PathPrefix: Long
        :param EndTime: 结束时间（Unix时间戳，秒）
        :type PathPrefix: Long
        :param Interval: 聚合周期（秒），不传由后端自动计算
        :type PathPrefix: Int
        """
        self.McpServerId = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")


class QueryMcpMetricsRequest(AbstractModel):
    """QueryMcpMetrics请求参数结构体
    """

    def __init__(self):
        r"""查询MCP服务调用监控信息
        :param StartTime: 开始时间（Unix时间戳，秒）
        :type PathPrefix: Long
        :param EndTime: 结束时间（Unix时间戳，秒）
        :type PathPrefix: Long
        :param Interval: 聚合步长（秒），允许值：30, 60, 300, 600, 1800, 3600
        :type PathPrefix: Int
        :param McpType: MCP类型：Official / Custom
        :type PathPrefix: String
        :param McpServerId: MCP服务ID
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.McpType = None
        self.McpServerId = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Interval"):
            self.Interval = params.get("Interval")
        if params.get("McpType"):
            self.McpType = params.get("McpType")
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")


class QueryMemoryCollectionSkillsRequest(AbstractModel):
    """QueryMemoryCollectionSkills请求参数结构体
    """

    def __init__(self):
        r"""查询记忆库匹配策略技能
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")


class DescribeKnowledgeTokenMonitorRequest(AbstractModel):
    """DescribeKnowledgeTokenMonitor请求参数结构体
    """

    def __init__(self):
        r"""查看知识库模型用量监控信息
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param StartTime: 开始时间戳（秒）
        :type PathPrefix: Long
        :param EndTime: 结束时间戳（秒）
        :type PathPrefix: Long
        :param Granularity: 聚合粒度：minute / hour / day
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Granularity"):
            self.Granularity = params.get("Granularity")


class DescribeKnowledgeStorageMonitorRequest(AbstractModel):
    """DescribeKnowledgeStorageMonitor请求参数结构体
    """

    def __init__(self):
        r"""查看知识库存储用量监控信息
        :param DatasetId: 知识库 ID
        :type PathPrefix: String
        :param StartTime: 开始时间戳（秒）
        :type PathPrefix: Long
        :param EndTime: 结束时间戳（秒）
        :type PathPrefix: Long
        :param Granularity: 聚合粒度：minute / hour / day
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Granularity"):
            self.Granularity = params.get("Granularity")


class DescribeMcpRuntimeLogsRequest(AbstractModel):
    """DescribeMcpRuntimeLogs请求参数结构体
    """

    def __init__(self):
        r"""查看MCP运行时日志
        :param McpServerId: MCP服务ID
        :type PathPrefix: String
        :param StartTime: 开始时间（Unix时间戳，秒）
        :type PathPrefix: Long
        :param EndTime: 结束时间（Unix时间戳，秒）
        :type PathPrefix: Long
        :param Keyword: 关键词搜索
        :type PathPrefix: String
        :param Page: 页码，默认1
        :type PathPrefix: Int
        :param Limit: 每页条数，默认100，最大5000
        :type PathPrefix: Int
        """
        self.McpServerId = None
        self.StartTime = None
        self.EndTime = None
        self.Keyword = None
        self.Page = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("McpServerId"):
            self.McpServerId = params.get("McpServerId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class DescribeMemoryTokenMonitorRequest(AbstractModel):
    """DescribeMemoryTokenMonitor请求参数结构体
    """

    def __init__(self):
        r"""查看记忆库模型用量监控信息
        :param MemoryId: 记忆库 ID
        :type PathPrefix: String
        :param StartTime: 开始时间戳（秒）
        :type PathPrefix: Long
        :param EndTime: 结束时间戳（秒）
        :type PathPrefix: Long
        :param Granularity: 聚合粒度：minute / hour / day
        :type PathPrefix: String
        """
        self.MemoryId = None
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None

    def _deserialize(self, params):
        if params.get("MemoryId"):
            self.MemoryId = params.get("MemoryId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Granularity"):
            self.Granularity = params.get("Granularity")


class DescribeMemoryStorageMonitorRequest(AbstractModel):
    """DescribeMemoryStorageMonitor请求参数结构体
    """

    def __init__(self):
        r"""查看记忆库存储用量监控信息
        :param MemoryId: 记忆库 ID
        :type PathPrefix: String
        :param StartTime: 开始时间戳（秒）
        :type PathPrefix: Long
        :param EndTime: 结束时间戳（秒）
        :type PathPrefix: Long
        :param Granularity: 聚合粒度：minute / hour / day
        :type PathPrefix: String
        """
        self.MemoryId = None
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None

    def _deserialize(self, params):
        if params.get("MemoryId"):
            self.MemoryId = params.get("MemoryId")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("Granularity"):
            self.Granularity = params.get("Granularity")


class ListMemoriesRequest(AbstractModel):
    """ListMemories请求参数结构体
    """

    def __init__(self):
        r"""记忆列表信息
        :param MemoryCollectionId: 记忆库 ID
        :type PathPrefix: String
        :param AgentUserId: 查询的用户ID
        :type PathPrefix: String
        :param TopicId: 主题 ID
        :type PathPrefix: String
        :param Query: 查询关键字
        :type PathPrefix: String
        :param Page: 分页参数——页码  默认1
        :type PathPrefix: Long
        :param PageSize: 分页参数——每页条数，默认10
        :type PathPrefix: Long
        :param SortBy: 排序字段，默认 记忆创建时间
枚举值:
created_at  记忆创建时间
occurred_start  事件开始时间
occurred_end  事件结束时间
updated_at  记忆更新时间
        :type PathPrefix: String
        :param SortOrder: 排序方向，默认 desc
枚举值:
asc  升序
desc  降序
        :type PathPrefix: String
        :param CreatedAfter: 记忆创建时间下界（ms，闭区间）：仅返回创建时间 >= 该值的记忆，值须 >= 0
        :type PathPrefix: Long
        :param CreatedBefore: 记忆创建时间上界（ms，开区间）：仅返回创建时间 < 该值的记忆，值须 >= 0
        :type PathPrefix: Long
        :param OccurredAfter: 事件时间下界（ms，闭区间）：仅返回事件时间 >= 该值的记忆，值须 >= 0
        :type PathPrefix: Long
        :param OccurredBefore: 事件时间上界（ms，开区间）：仅返回事件时间 < 该值的记忆，值须 >= 0
        :type PathPrefix: Long
        """
        self.MemoryCollectionId = None
        self.AgentUserId = None
        self.TopicId = None
        self.Query = None
        self.Page = None
        self.PageSize = None
        self.SortBy = None
        self.SortOrder = None
        self.CreatedAfter = None
        self.CreatedBefore = None
        self.OccurredAfter = None
        self.OccurredBefore = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("AgentUserId"):
            self.AgentUserId = params.get("AgentUserId")
        if params.get("TopicId"):
            self.TopicId = params.get("TopicId")
        if params.get("Query"):
            self.Query = params.get("Query")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("SortBy"):
            self.SortBy = params.get("SortBy")
        if params.get("SortOrder"):
            self.SortOrder = params.get("SortOrder")
        if params.get("CreatedAfter"):
            self.CreatedAfter = params.get("CreatedAfter")
        if params.get("CreatedBefore"):
            self.CreatedBefore = params.get("CreatedBefore")
        if params.get("OccurredAfter"):
            self.OccurredAfter = params.get("OccurredAfter")
        if params.get("OccurredBefore"):
            self.OccurredBefore = params.get("OccurredBefore")


class DeleteMemoryRequest(AbstractModel):
    """DeleteMemory请求参数结构体
    """

    def __init__(self):
        r"""根据记忆ID删除已有记忆
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        :param MemoryId: 记忆ID
        :type PathPrefix: String
        :param AgentUserId: 用户ID
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None
        self.MemoryId = None
        self.AgentUserId = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("MemoryId"):
            self.MemoryId = params.get("MemoryId")
        if params.get("AgentUserId"):
            self.AgentUserId = params.get("AgentUserId")


class UpdateMemoryRequest(AbstractModel):
    """UpdateMemory请求参数结构体
    """

    def __init__(self):
        r"""更新记忆信息
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        :param MemoryId: 记忆ID
        :type PathPrefix: String
        :param Content: 记忆内容
        :type PathPrefix: String
        :param AgentUserId: 用户ID
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None
        self.MemoryId = None
        self.Content = None
        self.AgentUserId = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("MemoryId"):
            self.MemoryId = params.get("MemoryId")
        if params.get("Content"):
            self.Content = params.get("Content")
        if params.get("AgentUserId"):
            self.AgentUserId = params.get("AgentUserId")


class QueryMemoryHistoryRequest(AbstractModel):
    """QueryMemoryHistory请求参数结构体
    """

    def __init__(self):
        r"""查询记忆变更历史记录
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        :param MemoryId: 记忆ID
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None
        self.MemoryId = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")
        if params.get("MemoryId"):
            self.MemoryId = params.get("MemoryId")


class ListTopicsRequest(AbstractModel):
    """ListTopics请求参数结构体
    """

    def __init__(self):
        r"""查询topic列表
        :param MemoryCollectionId: 记忆库ID
        :type PathPrefix: String
        """
        self.MemoryCollectionId = None

    def _deserialize(self, params):
        if params.get("MemoryCollectionId"):
            self.MemoryCollectionId = params.get("MemoryCollectionId")


class UpdateDocumentMetadataRequest(AbstractModel):
    """UpdateDocumentMetadata请求参数结构体
    """

    def __init__(self):
        r"""更新文档元数据
        :param DatasetId: 知识库ID
        :type PathPrefix: String
        :param OperationData: 操作的文档元数据
        :type PathPrefix: Array
        """
        self.DatasetId = None
        self.OperationData = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("OperationData"):
            self.OperationData = params.get("OperationData")


class DeleteMetadataRequest(AbstractModel):
    """DeleteMetadata请求参数结构体
    """

    def __init__(self):
        r"""删除知识库元数据
        :param DatasetId: 知识库ID
        :type PathPrefix: String
        :param MetadataId: 元数据ID
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.MetadataId = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("MetadataId"):
            self.MetadataId = params.get("MetadataId")


class UpdateMetadataRequest(AbstractModel):
    """UpdateMetadata请求参数结构体
    """

    def __init__(self):
        r"""更新知识库元数据
        :param DatasetId: 知识库ID
        :type PathPrefix: String
        :param MetadataId: 元数据ID
        :type PathPrefix: String
        :param Name: 元数据名称
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.MetadataId = None
        self.Name = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("MetadataId"):
            self.MetadataId = params.get("MetadataId")
        if params.get("Name"):
            self.Name = params.get("Name")


class CreateMetadataRequest(AbstractModel):
    """CreateMetadata请求参数结构体
    """

    def __init__(self):
        r"""新建知识库元数据
        :param DatasetId: 知识库ID
        :type PathPrefix: String
        :param Name: 元数据名称
        :type PathPrefix: String
        :param Type: 元数据类型
string  number  time  array[number]  array[string]
        :type PathPrefix: String
        """
        self.DatasetId = None
        self.Name = None
        self.Type = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Type"):
            self.Type = params.get("Type")


class DescribeMetadataRequest(AbstractModel):
    """DescribeMetadata请求参数结构体
    """

    def __init__(self):
        r"""查询知识库元数据
        :param DatasetId: 知识库ID
        :type PathPrefix: String
        """
        self.DatasetId = None

    def _deserialize(self, params):
        if params.get("DatasetId"):
            self.DatasetId = params.get("DatasetId")


