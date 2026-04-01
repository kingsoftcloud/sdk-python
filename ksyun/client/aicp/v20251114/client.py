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


