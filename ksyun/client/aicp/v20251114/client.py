import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class AicpClient(AbstractClient):
    _apiVersion = '2025-11-14'
    _endpoint = 'aicp.api.ksyun.com'
    _service = 'aicp'
    def DescribeKnowledgeBaseModels(self, request):
        """查询模型列表
        :param request: Request instance for DescribeKnowledgeBaseModels.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeKnowledgeBaseModelsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKnowledgeBaseModels", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ActivateKnowledgeBaseService(self, request):
        """开通知识库服务
        :param request: Request instance for ActivateKnowledgeBaseService.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ActivateKnowledgeBaseServiceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ActivateKnowledgeBaseService", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def RetrieveKnowledge(self, request):
        """知识库检索
        :param request: Request instance for RetrieveKnowledge.
        :type request: :class:`ksyun.client.aicp.v20251114.models.RetrieveKnowledgeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RetrieveKnowledge", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeChunk(self, request):
        """获取切片详情
        :param request: Request instance for DescribeChunk.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeChunkRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeChunk", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def BatchDisplayStatus(self, request):
        """批量获取文档索引状态
        :param request: Request instance for BatchDisplayStatus.
        :type request: :class:`ksyun.client.aicp.v20251114.models.BatchDisplayStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("BatchDisplayStatus", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DisplayStatus(self, request):
        """获取文档索引状态
        :param request: Request instance for DisplayStatus.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DisplayStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisplayStatus", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def IndexingStatus(self, request):
        """获取文档嵌入状态
        :param request: Request instance for IndexingStatus.
        :type request: :class:`ksyun.client.aicp.v20251114.models.IndexingStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("IndexingStatus", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DeleteDocument(self, request):
        """删除知识库文档
        :param request: Request instance for DeleteDocument.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DeleteDocumentRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDocument", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeDocument(self, request):
        """获取文档详情
        :param request: Request instance for DescribeDocument.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeDocumentRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDocument", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeDocuments(self, request):
        """查看知识库文档列表
        :param request: Request instance for DescribeDocuments.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeDocumentsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDocuments", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ImportDocuments(self, request):
        """创建知识库文档
        :param request: Request instance for ImportDocuments.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ImportDocumentsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ImportDocuments", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DeleteKnowledgeBase(self, request):
        """删除知识库
        :param request: Request instance for DeleteKnowledgeBase.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DeleteKnowledgeBaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteKnowledgeBase", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ModifyKnowledgeBase(self, request):
        """修改知识库配置
        :param request: Request instance for ModifyKnowledgeBase.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ModifyKnowledgeBaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyKnowledgeBase", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeKnowledgeBase(self, request):
        """查看知识库详情
        :param request: Request instance for DescribeKnowledgeBase.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeKnowledgeBaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKnowledgeBase", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeKnowledgeBases(self, request):
        """查看知识库列表
        :param request: Request instance for DescribeKnowledgeBases.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeKnowledgeBasesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKnowledgeBases", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def CreateKnowledgeBase(self, request):
        """创建知识库
        :param request: Request instance for CreateKnowledgeBase.
        :type request: :class:`ksyun.client.aicp.v20251114.models.CreateKnowledgeBaseRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateKnowledgeBase", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def CreateMemorySdk(self, request):
        """向指定记忆库写入记忆
        :param request: Request instance for CreateMemorySdk.
        :type request: :class:`ksyun.client.aicp.v20251114.models.CreateMemorySdkRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateMemorySdk", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def QueryMemorySdk(self, request):
        """从记忆库检索记忆
        :param request: Request instance for QueryMemorySdk.
        :type request: :class:`ksyun.client.aicp.v20251114.models.QueryMemorySdkRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryMemorySdk", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def CreateMemoryCollection(self, request):
        """创建记忆库
        :param request: Request instance for CreateMemoryCollection.
        :type request: :class:`ksyun.client.aicp.v20251114.models.CreateMemoryCollectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateMemoryCollection", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def GetMemoryCollection(self, request):
        """查询记忆库详情
        :param request: Request instance for GetMemoryCollection.
        :type request: :class:`ksyun.client.aicp.v20251114.models.GetMemoryCollectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMemoryCollection", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ListMemoryCollections(self, request):
        """批量查询记忆库详情
        :param request: Request instance for ListMemoryCollections.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ListMemoryCollectionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListMemoryCollections", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DeleteMemoryCollection(self, request):
        """删除记忆库
        :param request: Request instance for DeleteMemoryCollection.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DeleteMemoryCollectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteMemoryCollection", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def GetMemoryBaseService(self, request):
        """查询记忆库服务状态
        :param request: Request instance for GetMemoryBaseService.
        :type request: :class:`ksyun.client.aicp.v20251114.models.GetMemoryBaseServiceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMemoryBaseService", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ActivateMemoryBaseService(self, request):
        """开通记忆库服务
        :param request: Request instance for ActivateMemoryBaseService.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ActivateMemoryBaseServiceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ActivateMemoryBaseService", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def UpdateMemoryCollection(self, request):
        """修改记忆库信息
        :param request: Request instance for UpdateMemoryCollection.
        :type request: :class:`ksyun.client.aicp.v20251114.models.UpdateMemoryCollectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateMemoryCollection", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DeleteMcpServer(self, request):
        """删除自定义MCP服务
        :param request: Request instance for DeleteMcpServer.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DeleteMcpServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteMcpServer", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ModifyMcpServer(self, request):
        """修改自定义MCP服务
        :param request: Request instance for ModifyMcpServer.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ModifyMcpServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyMcpServer", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def CreateMcpServer(self, request):
        """创建自定义MCP服务
        :param request: Request instance for CreateMcpServer.
        :type request: :class:`ksyun.client.aicp.v20251114.models.CreateMcpServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateMcpServer", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeMcpServers(self, request):
        """查询自定义MCP服务
        :param request: Request instance for DescribeMcpServers.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeMcpServersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMcpServers", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeMcpOfficialServers(self, request):
        """查询MCP官方服务
        :param request: Request instance for DescribeMcpOfficialServers.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeMcpOfficialServersRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMcpOfficialServers", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DeactivateMcpOfficialServer(self, request):
        """取消MCP官方服务
        :param request: Request instance for DeactivateMcpOfficialServer.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DeactivateMcpOfficialServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeactivateMcpOfficialServer", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ActivateMcpOfficialServer(self, request):
        """激活MCP官方服务
        :param request: Request instance for ActivateMcpOfficialServer.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ActivateMcpOfficialServerRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ActivateMcpOfficialServer", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeMcpSquares(self, request):
        """查询MCP广场
        :param request: Request instance for DescribeMcpSquares.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeMcpSquaresRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMcpSquares", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def GetMcpOfficialServerDetail(self, request):
        """查询MCP官方服务详情
        :param request: Request instance for GetMcpOfficialServerDetail.
        :type request: :class:`ksyun.client.aicp.v20251114.models.GetMcpOfficialServerDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMcpOfficialServerDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def GetMcpServerDetail(self, request):
        """查询自定义MCP服务详情
        :param request: Request instance for GetMcpServerDetail.
        :type request: :class:`ksyun.client.aicp.v20251114.models.GetMcpServerDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMcpServerDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def GetMcpSquareDetail(self, request):
        """查询MCP广场详情
        :param request: Request instance for GetMcpSquareDetail.
        :type request: :class:`ksyun.client.aicp.v20251114.models.GetMcpSquareDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetMcpSquareDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ListSessions(self, request):
        """查询会话列表
        :param request: Request instance for ListSessions.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ListSessionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListSessions", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def AddSession(self, request):
        """创建记忆会话
        :param request: Request instance for AddSession.
        :type request: :class:`ksyun.client.aicp.v20251114.models.AddSessionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddSession", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def QueryMemoryCollectionMetrics(self, request):
        """查询指定记忆库的监控指标时间序列数据
        :param request: Request instance for QueryMemoryCollectionMetrics.
        :type request: :class:`ksyun.client.aicp.v20251114.models.QueryMemoryCollectionMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryMemoryCollectionMetrics", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def QuerySessionMemories(self, request):
        """查询会话记忆
        :param request: Request instance for QuerySessionMemories.
        :type request: :class:`ksyun.client.aicp.v20251114.models.QuerySessionMemoriesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QuerySessionMemories", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def RetrieveHistories(self, request):
        """知识库检索历史记录
        :param request: Request instance for RetrieveHistories.
        :type request: :class:`ksyun.client.aicp.v20251114.models.RetrieveHistoriesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RetrieveHistories", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ReindexDocuments(self, request):
        """重索引知识库文档
        :param request: Request instance for ReindexDocuments.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ReindexDocumentsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ReindexDocuments", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ModifyDocumentStatus(self, request):
        """修改知识库文档状态
        :param request: Request instance for ModifyDocumentStatus.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ModifyDocumentStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDocumentStatus", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def GetApiDetail(self, request):
        """查询云产品OpenAPI详情
        :param request: Request instance for GetApiDetail.
        :type request: :class:`ksyun.client.aicp.v20251114.models.GetApiDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetApiDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def GetApiOverview(self, request):
        """查询云产品OpenAPI概览列表
        :param request: Request instance for GetApiOverview.
        :type request: :class:`ksyun.client.aicp.v20251114.models.GetApiOverviewRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetApiOverview", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def GetProductList(self, request):
        """查询云产品列表
        :param request: Request instance for GetProductList.
        :type request: :class:`ksyun.client.aicp.v20251114.models.GetProductListRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetProductList", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeMcpRuntimeMetrics(self, request):
        """查询MCP运行监控（只有部署方式为代码方式部署的MCP才有）
        :param request: Request instance for DescribeMcpRuntimeMetrics.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeMcpRuntimeMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMcpRuntimeMetrics", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def QueryMcpMetrics(self, request):
        """查询MCP服务调用监控信息
        :param request: Request instance for QueryMcpMetrics.
        :type request: :class:`ksyun.client.aicp.v20251114.models.QueryMcpMetricsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryMcpMetrics", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeKnowledgeTokenMonitor(self, request):
        """查看知识库模型用量监控信息
        :param request: Request instance for DescribeKnowledgeTokenMonitor.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeKnowledgeTokenMonitorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKnowledgeTokenMonitor", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeKnowledgeStorageMonitor(self, request):
        """查看知识库存储用量监控信息
        :param request: Request instance for DescribeKnowledgeStorageMonitor.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeKnowledgeStorageMonitorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeKnowledgeStorageMonitor", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeMcpRuntimeLogs(self, request):
        """查看MCP运行时日志
        :param request: Request instance for DescribeMcpRuntimeLogs.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeMcpRuntimeLogsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMcpRuntimeLogs", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeMemoryTokenMonitor(self, request):
        """查看记忆库模型用量监控信息
        :param request: Request instance for DescribeMemoryTokenMonitor.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeMemoryTokenMonitorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMemoryTokenMonitor", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DescribeMemoryStorageMonitor(self, request):
        """查看记忆库存储用量监控信息
        :param request: Request instance for DescribeMemoryStorageMonitor.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DescribeMemoryStorageMonitorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeMemoryStorageMonitor", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ListMemories(self, request):
        """记忆列表信息
        :param request: Request instance for ListMemories.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ListMemoriesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListMemories", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def DeleteMemory(self, request):
        """根据记忆ID删除已有记忆
        :param request: Request instance for DeleteMemory.
        :type request: :class:`ksyun.client.aicp.v20251114.models.DeleteMemoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteMemory", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def UpdateMemory(self, request):
        """更新记忆信息
        :param request: Request instance for UpdateMemory.
        :type request: :class:`ksyun.client.aicp.v20251114.models.UpdateMemoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateMemory", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def QueryMemoryHistory(self, request):
        """查询记忆变更历史记录
        :param request: Request instance for QueryMemoryHistory.
        :type request: :class:`ksyun.client.aicp.v20251114.models.QueryMemoryHistoryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryMemoryHistory", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


    def ListTopics(self, request):
        """查询瀚海topic列表
        :param request: Request instance for ListTopics.
        :type request: :class:`ksyun.client.aicp.v20251114.models.ListTopicsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListTopics", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
            else:
                code = response["Error"]["Code"]
                message = response["Error"]["Message"]
                req_id = response["RequestId"]
                raise KsyunSDKException(code, message, req_id)
        except Exception as e:
            if isinstance(e, KsyunSDKException):
                raise
            else:
                raise KsyunSDKException(message=str(e))


