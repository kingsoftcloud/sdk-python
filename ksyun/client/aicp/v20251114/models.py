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


