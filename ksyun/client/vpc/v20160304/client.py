import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class VpcClient(AbstractClient):
    _apiVersion = '2016-03-04'
    _endpoint = 'vpc.api.ksyun.com'
    _service = 'vpc'
    def CreateVpc(self, request):
        """创建Vpc
        :param request: Request instance for CreateVpc.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateVpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateVpc", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteVpc(self, request):
        """删除Vpc
        :param request: Request instance for DeleteVpc.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteVpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteVpc", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeVpcs(self, request):
        """描述Vpc
        :param request: Request instance for DescribeVpcs.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeVpcsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVpcs", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateSubnet(self, request):
        """创建子网
        :param request: Request instance for CreateSubnet.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateSubnetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSubnet", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteSubnet(self, request):
        """删除子网
        :param request: Request instance for DeleteSubnet.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteSubnetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSubnet", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeSubnets(self, request):
        """描述子网
        :param request: Request instance for DescribeSubnets.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeSubnetsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSubnets", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def AssociateNetworkAcl(self, request):
        """关联ACL
        :param request: Request instance for AssociateNetworkAcl.
        :type request: :class:`ksyun.client.vpc.v20160304.models.AssociateNetworkAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateNetworkAcl", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DisassociateNetworkAcl(self, request):
        """解绑ACL
        :param request: Request instance for DisassociateNetworkAcl.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DisassociateNetworkAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisassociateNetworkAcl", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateRoute(self, request):
        """创建路由
        :param request: Request instance for CreateRoute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateRouteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateRoute", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteRoute(self, request):
        """删除路由
        :param request: Request instance for DeleteRoute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteRouteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteRoute", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeRoutes(self, request):
        """描述路由
        :param request: Request instance for DescribeRoutes.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeRoutesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeRoutes", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateNetworkAcl(self, request):
        """创建ACL
        :param request: Request instance for CreateNetworkAcl.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateNetworkAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateNetworkAcl", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteNetworkAcl(self, request):
        """删除ACL
        :param request: Request instance for DeleteNetworkAcl.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteNetworkAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteNetworkAcl", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateNetworkAclEntry(self, request):
        """创建ACL规则
        :param request: Request instance for CreateNetworkAclEntry.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateNetworkAclEntryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateNetworkAclEntry", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteNetworkAclEntry(self, request):
        """删除ACLl规则
        :param request: Request instance for DeleteNetworkAclEntry.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteNetworkAclEntryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteNetworkAclEntry", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeNetworkAcls(self, request):
        """描述ACL
        :param request: Request instance for DescribeNetworkAcls.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeNetworkAclsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNetworkAcls", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateSecurityGroup(self, request):
        """创建安全组
        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateSecurityGroup", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteSecurityGroup(self, request):
        """删除安全组
        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteSecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecurityGroup", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def AuthorizeSecurityGroupEntry(self, request):
        """创建安全组规则
        :param request: Request instance for AuthorizeSecurityGroupEntry.
        :type request: :class:`ksyun.client.vpc.v20160304.models.AuthorizeSecurityGroupEntryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AuthorizeSecurityGroupEntry", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def RevokeSecurityGroupEntry(self, request):
        """删除安全组规则
        :param request: Request instance for RevokeSecurityGroupEntry.
        :type request: :class:`ksyun.client.vpc.v20160304.models.RevokeSecurityGroupEntryRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RevokeSecurityGroupEntry", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeSecurityGroups(self, request):
        """描述安全组
        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeSecurityGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSecurityGroups", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateNat(self, request):
        """创建Nat
        :param request: Request instance for CreateNat.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateNatRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateNat", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteNat(self, request):
        """删除Nat
        :param request: Request instance for DeleteNat.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteNatRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteNat", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeNats(self, request):
        """描述Nat
        :param request: Request instance for DescribeNats.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeNatsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNats", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def AssociateNat(self, request):
        """Nat关联子网
        :param request: Request instance for AssociateNat.
        :type request: :class:`ksyun.client.vpc.v20160304.models.AssociateNatRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateNat", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DisassociateNat(self, request):
        """Nat解绑子网
        :param request: Request instance for DisassociateNat.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DisassociateNatRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DisassociateNat", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeInternetGateways(self, request):
        """描述InternetGateway
        :param request: Request instance for DescribeInternetGateways.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeInternetGatewaysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeInternetGateways", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateVpcPeeringConnection(self, request):
        """创建对等连接
        :param request: Request instance for CreateVpcPeeringConnection.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateVpcPeeringConnectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateVpcPeeringConnection", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteVpcPeeringConnection(self, request):
        """删除对等连接
        :param request: Request instance for DeleteVpcPeeringConnection.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteVpcPeeringConnectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteVpcPeeringConnection", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeVpcPeeringConnections(self, request):
        """描述对等连接
        :param request: Request instance for DescribeVpcPeeringConnections.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeVpcPeeringConnectionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVpcPeeringConnections", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyNetworkAcl(self, request):
        """修改ACL
        :param request: Request instance for ModifyNetworkAcl.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyNetworkAclRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNetworkAcl", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifySecurityGroup(self, request):
        """更改安全组信息
        :param request: Request instance for ModifySecurityGroup.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifySecurityGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySecurityGroup", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifySubnet(self, request):
        """修改子网
        :param request: Request instance for ModifySubnet.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifySubnetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifySubnet", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyNat(self, request):
        """更新NAT信息
        :param request: Request instance for ModifyNat.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyNatRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNat", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeNetworkInterfaces(self, request):
        """描述弹性网卡
        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeNetworkInterfacesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeNetworkInterfaces", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeSubnetAvailableAddresses(self, request):
        """描述子网可用IP信息
        :param request: Request instance for DescribeSubnetAvailableAddresses.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeSubnetAvailableAddressesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSubnetAvailableAddresses", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyVpc(self, request):
        """修改Vpc
        :param request: Request instance for ModifyVpc.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyVpcRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyVpc", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def AcceptVpcPeeringConnection(self, request):
        """接受对等连接
        :param request: Request instance for AcceptVpcPeeringConnection.
        :type request: :class:`ksyun.client.vpc.v20160304.models.AcceptVpcPeeringConnectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AcceptVpcPeeringConnection", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def RejectVpcPeeringConnection(self, request):
        """拒绝对等连接
        :param request: Request instance for RejectVpcPeeringConnection.
        :type request: :class:`ksyun.client.vpc.v20160304.models.RejectVpcPeeringConnectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("RejectVpcPeeringConnection", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyVpcPeeringConnection(self, request):
        """修改对等连接
        :param request: Request instance for ModifyVpcPeeringConnection.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyVpcPeeringConnectionRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyVpcPeeringConnection", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeAvailabilityZones(self, request):
        """描述可用区信息
        :param request: Request instance for DescribeAvailabilityZones.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeAvailabilityZonesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeAvailabilityZones", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeDirectConnects(self, request):
        """描述物理端口
        :param request: Request instance for DescribeDirectConnects.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeDirectConnectsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDirectConnects", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateDirectConnectInterface(self, request):
        """创建连接通道
        :param request: Request instance for CreateDirectConnectInterface.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateDirectConnectInterfaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDirectConnectInterface", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteDirectConnectInterface(self, request):
        """删除连接通道
        :param request: Request instance for DeleteDirectConnectInterface.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteDirectConnectInterfaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDirectConnectInterface", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeDirectConnectInterfaces(self, request):
        """描述连接通道
        :param request: Request instance for DescribeDirectConnectInterfaces.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeDirectConnectInterfacesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDirectConnectInterfaces", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateDirectConnectGateway(self, request):
        """创建边界网关
        :param request: Request instance for CreateDirectConnectGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateDirectConnectGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateDirectConnectGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteDirectConnectGateway(self, request):
        """删除边界网关
        :param request: Request instance for DeleteDirectConnectGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteDirectConnectGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDirectConnectGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeDirectConnectGateways(self, request):
        """描述边界网关
        :param request: Request instance for DescribeDirectConnectGateways.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeDirectConnectGatewaysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDirectConnectGateways", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def AttachDirectConnectGateway(self, request):
        """绑定边界网关
        :param request: Request instance for AttachDirectConnectGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.AttachDirectConnectGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AttachDirectConnectGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DetachDirectConnectGateway(self, request):
        """解绑边界网关
        :param request: Request instance for DetachDirectConnectGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DetachDirectConnectGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachDirectConnectGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyDirectConnectInterface(self, request):
        """修改连接通道
        :param request: Request instance for ModifyDirectConnectInterface.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyDirectConnectInterfaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDirectConnectInterface", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyDirectConnectGateway(self, request):
        """修改边界网关
        :param request: Request instance for ModifyDirectConnectGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyDirectConnectGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDirectConnectGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateVpnGateway(self, request):
        """创建VPN网关
        :param request: Request instance for CreateVpnGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateVpnGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateVpnGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyVpnGateway(self, request):
        """修改VPN网关
        :param request: Request instance for ModifyVpnGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyVpnGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyVpnGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteVpnGateway(self, request):
        """删除VPN网关
        :param request: Request instance for DeleteVpnGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteVpnGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteVpnGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeVpnGateways(self, request):
        """描述VPN网关
        :param request: Request instance for DescribeVpnGateways.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeVpnGatewaysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVpnGateways", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateVpnTunnel(self, request):
        """创建VPN通道
        :param request: Request instance for CreateVpnTunnel.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateVpnTunnelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateVpnTunnel", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyVpnTunnel(self, request):
        """修改VPN通道
        :param request: Request instance for ModifyVpnTunnel.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyVpnTunnelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyVpnTunnel", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteVpnTunnel(self, request):
        """删除VPN通道
        :param request: Request instance for DeleteVpnTunnel.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteVpnTunnelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteVpnTunnel", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeVpnTunnels(self, request):
        """描述VPN通道
        :param request: Request instance for DescribeVpnTunnels.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeVpnTunnelsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVpnTunnels", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateCustomerGateway(self, request):
        """创建客户网关
        :param request: Request instance for CreateCustomerGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateCustomerGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCustomerGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyCustomerGateway(self, request):
        """修改客户网关信息
        :param request: Request instance for ModifyCustomerGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyCustomerGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyCustomerGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteCustomerGateway(self, request):
        """删除客户网关
        :param request: Request instance for DeleteCustomerGateway.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteCustomerGatewayRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteCustomerGateway", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyDirectConnect(self, request):
        """修改物理端口
        :param request: Request instance for ModifyDirectConnect.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyDirectConnectRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyDirectConnect", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeCustomerGateways(self, request):
        """描述客户网关
        :param request: Request instance for DescribeCustomerGateways.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeCustomerGatewaysRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeCustomerGateways", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeSubnetAllocatedIpAddresses(self, request):
        """描述子网已用IP信息
        :param request: Request instance for DescribeSubnetAllocatedIpAddresses.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeSubnetAllocatedIpAddressesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeSubnetAllocatedIpAddresses", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyPrivateIpAddressAttribute(self, request):
        """修改内网IP属性
        :param request: Request instance for ModifyPrivateIpAddressAttribute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyPrivateIpAddressAttributeRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyPrivateIpAddressAttribute", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteNetworkInterface(self, request):
        """删除弹性网卡
        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteNetworkInterfaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteNetworkInterface", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateNetworkInterface(self, request):
        """创建弹性网卡
        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateNetworkInterfaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateNetworkInterface", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyNetworkInterface(self, request):
        """修改弹性网卡名称
        :param request: Request instance for ModifyNetworkInterface.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyNetworkInterfaceRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNetworkInterface", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateHaVip(self, request):
        """创建HaVip
        :param request: Request instance for CreateHaVip.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateHaVipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateHaVip", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteHaVip(self, request):
        """删除HaVip
        :param request: Request instance for DeleteHaVip.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteHaVipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteHaVip", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def AssociateHaVip(self, request):
        """绑定HaVip
        :param request: Request instance for AssociateHaVip.
        :type request: :class:`ksyun.client.vpc.v20160304.models.AssociateHaVipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssociateHaVip", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def UnAssociateHaVip(self, request):
        """解绑HaVip
        :param request: Request instance for UnAssociateHaVip.
        :type request: :class:`ksyun.client.vpc.v20160304.models.UnAssociateHaVipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnAssociateHaVip", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeHaVip(self, request):
        """查询HaVip
        :param request: Request instance for DescribeHaVip.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeHaVipRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeHaVip", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteDirectConnectGatewayRoute(self, request):
        """删除边界网关路由
        :param request: Request instance for DeleteDirectConnectGatewayRoute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteDirectConnectGatewayRouteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteDirectConnectGatewayRoute", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeDirectConnectGatewayRoute(self, request):
        """查询边界网关路由
        :param request: Request instance for DescribeDirectConnectGatewayRoute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeDirectConnectGatewayRouteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeDirectConnectGatewayRoute", params, "application/json")
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
                raise KsyunSDKException(e.message, e.message)


    def PublishDirectConnectRoute(self, request):
        """发布边界网关路由到BGP
        :param request: Request instance for PublishDirectConnectRoute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.PublishDirectConnectRouteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("PublishDirectConnectRoute", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def UnpublishDirectConnectRoute(self, request):
        """从BGP取消发布边界网关路由
        :param request: Request instance for UnpublishDirectConnectRoute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.UnpublishDirectConnectRouteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnpublishDirectConnectRoute", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def AddSecondaryCidrBlock(self, request):
        """为VPC添加附加IPv4网段
        :param request: Request instance for AddSecondaryCidrBlock.
        :type request: :class:`ksyun.client.vpc.v20160304.models.AddSecondaryCidrBlockRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AddSecondaryCidrBlock", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteSecondaryCidrBlock(self, request):
        """删除VPC附加IPv4网段
        :param request: Request instance for DeleteSecondaryCidrBlock.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteSecondaryCidrBlockRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteSecondaryCidrBlock", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def AssignPrivateIpAddress(self, request):
        """AssignPrivateIpAddress
        :param request: Request instance for AssignPrivateIpAddress.
        :type request: :class:`ksyun.client.vpc.v20160304.models.AssignPrivateIpAddressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("AssignPrivateIpAddress", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def UnassignPrivateIpAddress(self, request):
        """弹性网卡取消分配辅助私网ip
        :param request: Request instance for UnassignPrivateIpAddress.
        :type request: :class:`ksyun.client.vpc.v20160304.models.UnassignPrivateIpAddressRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UnassignPrivateIpAddress", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeVpnGatewayRoutes(self, request):
        """查询VPN网关路由
        :param request: Request instance for DescribeVpnGatewayRoutes.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeVpnGatewayRoutesRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVpnGatewayRoutes", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def CreateVpnGatewayRoute(self, request):
        """创建VPN网关下的路由
        :param request: Request instance for CreateVpnGatewayRoute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.CreateVpnGatewayRouteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateVpnGatewayRoute", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DeleteVpnGatewayRoute(self, request):
        """删除VPN网关下的路由
        :param request: Request instance for DeleteVpnGatewayRoute.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DeleteVpnGatewayRouteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteVpnGatewayRoute", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def DescribeVpnTunnelIpsecStatus(self, request):
        """查询VPN通道ipsec status状态
        :param request: Request instance for DescribeVpnTunnelIpsecStatus.
        :type request: :class:`ksyun.client.vpc.v20160304.models.DescribeVpnTunnelIpsecStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DescribeVpnTunnelIpsecStatus", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def QueryNatTopVifMonitor(self, request):
        """查询NAT下流量排名的TOP 50的网卡
        :param request: Request instance for QueryNatTopVifMonitor.
        :type request: :class:`ksyun.client.vpc.v20160304.models.QueryNatTopVifMonitorRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryNatTopVifMonitor", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


    def ModifyNatIpStatus(self, request):
        """修改NatIp的禁用/启用
        :param request: Request instance for ModifyNatIpStatus.
        :type request: :class:`ksyun.client.vpc.v20160304.models.ModifyNatIpStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ModifyNatIpStatus", params, "application/x-www-form-urlencoded")
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
                raise KsyunSDKException(e.message, e.message)


