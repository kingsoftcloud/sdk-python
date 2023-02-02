import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class IamClient(AbstractClient):
    _apiVersion = '2015-11-01'
    _endpoint = 'iam.api.ksyun.com'
    _service = 'iam'
    def CreateUser(self, request):
        """新建IAM子用户
        :param request: Request instance for CreateUser.
        :type request: :class:`ksyun.client.iam.v20151101.models.CreateUserRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateUser", params)
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


    def ListUsers(self, request):
        """查询所有子用户的详细信息
        :param request: Request instance for ListUsers.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListUsersRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListUsers", params)
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


    def UpdateUser(self, request):
        """更新用户基本信息
        :param request: Request instance for UpdateUser.
        :type request: :class:`ksyun.client.iam.v20151101.models.UpdateUserRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdateUser", params)
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


    def GetUser(self, request):
        """查询子用户基本信息
        :param request: Request instance for GetUser.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetUserRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetUser", params)
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


    def DeleteUser(self, request):
        """删除子用户
        :param request: Request instance for DeleteUser.
        :type request: :class:`ksyun.client.iam.v20151101.models.DeleteUserRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteUser", params)
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


    def ListAttachedUserPolicies(self, request):
        """查询用户附加策略列表
        :param request: Request instance for ListAttachedUserPolicies.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListAttachedUserPoliciesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedUserPolicies", params)
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


    def ListPolicyVersions(self, request):
        """查询策略版本列表
        :param request: Request instance for ListPolicyVersions.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListPolicyVersionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListPolicyVersions", params)
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


    def SetDefaultPolicyVersion(self, request):
        """设定默认策略版本
        :param request: Request instance for SetDefaultPolicyVersion.
        :type request: :class:`ksyun.client.iam.v20151101.models.SetDefaultPolicyVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call("SetDefaultPolicyVersion", params)
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


    def AttachUserPolicy(self, request):
        """附加用户策略
        :param request: Request instance for AttachUserPolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.AttachUserPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AttachUserPolicy", params)
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


    def DeletePolicyVersion(self, request):
        """删除策略版本内容
        :param request: Request instance for DeletePolicyVersion.
        :type request: :class:`ksyun.client.iam.v20151101.models.DeletePolicyVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicyVersion", params)
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


    def GetPolicyVersion(self, request):
        """查询策略版本内容
        :param request: Request instance for GetPolicyVersion.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetPolicyVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetPolicyVersion", params)
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


    def CreatePolicyVersion(self, request):
        """新建策略版本内容
        :param request: Request instance for CreatePolicyVersion.
        :type request: :class:`ksyun.client.iam.v20151101.models.CreatePolicyVersionRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicyVersion", params)
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


    def ListPolicies(self, request):
        """查询策略信息列表
        :param request: Request instance for ListPolicies.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListPoliciesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListPolicies", params)
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


    def GetPolicy(self, request):
        """查询策略元数据信息
        :param request: Request instance for GetPolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetPolicy", params)
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


    def DeletePolicy(self, request):
        """删除策略
        :param request: Request instance for DeletePolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.DeletePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicy", params)
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


    def CreatePolicy(self, request):
        """新建策略
        :param request: Request instance for CreatePolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.CreatePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicy", params)
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


    def ChangePassword(self, request):
        """子用户修改密码
        :param request: Request instance for ChangePassword.
        :type request: :class:`ksyun.client.iam.v20151101.models.ChangePasswordRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ChangePassword", params)
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


    def UpdateLoginProfile(self, request):
        """更新子用户登录配置
        :param request: Request instance for UpdateLoginProfile.
        :type request: :class:`ksyun.client.iam.v20151101.models.UpdateLoginProfileRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdateLoginProfile", params)
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


    def GetLoginProfile(self, request):
        """查询登录配置信息
        :param request: Request instance for GetLoginProfile.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetLoginProfileRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetLoginProfile", params)
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


    def CreateAccessKey(self, request):
        """生成访问密钥
        :param request: Request instance for CreateAccessKey.
        :type request: :class:`ksyun.client.iam.v20151101.models.CreateAccessKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateAccessKey", params)
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


    def ListAccessKeys(self, request):
        """查询访问密钥列表
        :param request: Request instance for ListAccessKeys.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListAccessKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListAccessKeys", params)
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


    def UpdateAccessKey(self, request):
        """更新访问密钥
        :param request: Request instance for UpdateAccessKey.
        :type request: :class:`ksyun.client.iam.v20151101.models.UpdateAccessKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdateAccessKey", params)
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


    def DeleteAccessKey(self, request):
        """删除访问密钥
        :param request: Request instance for DeleteAccessKey.
        :type request: :class:`ksyun.client.iam.v20151101.models.DeleteAccessKeyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccessKey", params)
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


    def ListVirtualMFADevices(self, request):
        """查询虚拟设备列表
        :param request: Request instance for ListVirtualMFADevices.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListVirtualMFADevicesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListVirtualMFADevices", params)
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


    def EnableMFADevice(self, request):
        """激活虚拟设备
        :param request: Request instance for EnableMFADevice.
        :type request: :class:`ksyun.client.iam.v20151101.models.EnableMFADeviceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("EnableMFADevice", params)
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


    def DeactivateMFADevice(self, request):
        """解绑虚拟设备
        :param request: Request instance for DeactivateMFADevice.
        :type request: :class:`ksyun.client.iam.v20151101.models.DeactivateMFADeviceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeactivateMFADevice", params)
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


    def GetVirtualMFADevice(self, request):
        """获取虚拟设备
        :param request: Request instance for GetVirtualMFADevice.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetVirtualMFADeviceRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetVirtualMFADevice", params)
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


    def CreateRole(self, request):
        """创建角色
        :param request: Request instance for CreateRole.
        :type request: :class:`ksyun.client.iam.v20151101.models.CreateRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateRole", params)
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


    def DeleteRole(self, request):
        """删除角色
        :param request: Request instance for DeleteRole.
        :type request: :class:`ksyun.client.iam.v20151101.models.DeleteRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteRole", params)
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


    def GetRole(self, request):
        """查询角色基本信息
        :param request: Request instance for GetRole.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetRole", params)
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


    def ListRoles(self, request):
        """查询账号的角色列表
        :param request: Request instance for ListRoles.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListRolesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListRoles", params)
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


    def AttachRolePolicy(self, request):
        """附加角色的访问策略
        :param request: Request instance for AttachRolePolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.AttachRolePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AttachRolePolicy", params)
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


    def DetachRolePolicy(self, request):
        """分离角色的访问策略
        :param request: Request instance for DetachRolePolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.DetachRolePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DetachRolePolicy", params)
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


    def ListAttachedRolePolicies(self, request):
        """查询角色附加的策略列表
        :param request: Request instance for ListAttachedRolePolicies.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListAttachedRolePoliciesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedRolePolicies", params)
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


    def UpdateRoleTrustAccounts(self, request):
        """更新角色的信任关系
        :param request: Request instance for UpdateRoleTrustAccounts.
        :type request: :class:`ksyun.client.iam.v20151101.models.UpdateRoleTrustAccountsRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdateRoleTrustAccounts", params)
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


    def CreateProject(self, request):
        """创建项目
        :param request: Request instance for CreateProject.
        :type request: :class:`ksyun.client.iam.v20151101.models.CreateProjectRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateProject", params)
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


    def GetAccountAllProjectList(self, request):
        """获取主/子用户项目列表
        :param request: Request instance for GetAccountAllProjectList.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetAccountAllProjectListRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetAccountAllProjectList", params)
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


    def GetProjectInstanceList(self, request):
        """获取项目资源列表
        :param request: Request instance for GetProjectInstanceList.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetProjectInstanceListRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetProjectInstanceList", params)
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


    def UpdateInstanceProjectId(self, request):
        """更新实例项目
        :param request: Request instance for UpdateInstanceProjectId.
        :type request: :class:`ksyun.client.iam.v20151101.models.UpdateInstanceProjectIdRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdateInstanceProjectId", params)
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


    def ListEntitiesForPolicy(self, request):
        """查询策略关联实体列表
        :param request: Request instance for ListEntitiesForPolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListEntitiesForPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListEntitiesForPolicy", params)
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


    def ListProjectMember(self, request):
        """查询项目成员列表
        :param request: Request instance for ListProjectMember.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListProjectMemberRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListProjectMember", params)
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


    def DeleteProjectMember(self, request):
        """删除项目成员
        :param request: Request instance for DeleteProjectMember.
        :type request: :class:`ksyun.client.iam.v20151101.models.DeleteProjectMemberRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteProjectMember", params)
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


    def AddProjectMember(self, request):
        """添加项目成员
        :param request: Request instance for AddProjectMember.
        :type request: :class:`ksyun.client.iam.v20151101.models.AddProjectMemberRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AddProjectMember", params)
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


    def UpdateRole(self, request):
        """更新角基本描述
        :param request: Request instance for UpdateRole.
        :type request: :class:`ksyun.client.iam.v20151101.models.UpdateRoleRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdateRole", params)
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


    def UpdatePolicy(self, request):
        """更新策略描述
        :param request: Request instance for UpdatePolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.UpdatePolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("UpdatePolicy", params)
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


    def CreateGroup(self, request):
        """创建用户组
        :param request: Request instance for CreateGroup.
        :type request: :class:`ksyun.client.iam.v20151101.models.CreateGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("CreateGroup", params)
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


    def DeleteGroup(self, request):
        """删除用户组
        :param request: Request instance for DeleteGroup.
        :type request: :class:`ksyun.client.iam.v20151101.models.DeleteGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DeleteGroup", params)
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


    def DetachGroupPolicy(self, request):
        """从用户组分离策略
        :param request: Request instance for DetachGroupPolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.DetachGroupPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("DetachGroupPolicy", params)
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


    def AttachGroupPolicy(self, request):
        """附加策略到用户组
        :param request: Request instance for AttachGroupPolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.AttachGroupPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AttachGroupPolicy", params)
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


    def ListGroupPolicies(self, request):
        """获取用户组权限列表
        :param request: Request instance for ListGroupPolicies.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListGroupPoliciesRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListGroupPolicies", params)
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


    def AddUserToGroup(self, request):
        """添加用户到用户组
        :param request: Request instance for AddUserToGroup.
        :type request: :class:`ksyun.client.iam.v20151101.models.AddUserToGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("AddUserToGroup", params)
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


    def GetGroup(self, request):
        """获取用户组基础信息
        :param request: Request instance for GetGroup.
        :type request: :class:`ksyun.client.iam.v20151101.models.GetGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("GetGroup", params)
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


    def ListGroupsForUser(self, request):
        """获取用户所属用户组列表
        :param request: Request instance for ListGroupsForUser.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListGroupsForUserRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListGroupsForUser", params)
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


    def ListGroups(self, request):
        """获取用户组列表
        :param request: Request instance for ListGroups.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListGroupsRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListGroups", params)
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


    def RemoveUserFromGroup(self, request):
        """从用户组删除用户
        :param request: Request instance for RemoveUserFromGroup.
        :type request: :class:`ksyun.client.iam.v20151101.models.RemoveUserFromGroupRequest`
        """
        try:
            params = request._serialize()
            body = self.call("RemoveUserFromGroup", params)
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


    def ListAllUserAccessKeys(self, request):
        """获取子用户ak最后使用时间
        :param request: Request instance for ListAllUserAccessKeys.
        :type request: :class:`ksyun.client.iam.v20151101.models.ListAllUserAccessKeysRequest`
        """
        try:
            params = request._serialize()
            body = self.call("ListAllUserAccessKeys", params)
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


