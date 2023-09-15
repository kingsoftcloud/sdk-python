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
            body = self.call_judge("CreateUser", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListUsers", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("UpdateUser", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetUser", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeleteUser", params, "application/x-www-form-urlencoded")
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


    def DetachUserPolicy(self, request):
        """解绑IAM用户策略
        :param request: Request instance for DetachUserPolicy.
        :type request: :class:`ksyun.client.iam.v20151101.models.DetachUserPolicyRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DetachUserPolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListAttachedUserPolicies", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListPolicyVersions", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("SetDefaultPolicyVersion", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("AttachUserPolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeletePolicyVersion", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetPolicyVersion", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("CreatePolicyVersion", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListPolicies", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetPolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeletePolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("CreatePolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ChangePassword", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("UpdateLoginProfile", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetLoginProfile", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("CreateAccessKey", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListAccessKeys", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("UpdateAccessKey", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeleteAccessKey", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListVirtualMFADevices", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("EnableMFADevice", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeactivateMFADevice", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetVirtualMFADevice", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("CreateRole", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeleteRole", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetRole", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListRoles", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("AttachRolePolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DetachRolePolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListAttachedRolePolicies", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("UpdateRoleTrustAccounts", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("CreateProject", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetAccountAllProjectList", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetProjectInstanceList", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("UpdateInstanceProjectId", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListEntitiesForPolicy", params, "application/json")
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
            body = self.call_judge("ListProjectMember", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeleteProjectMember", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("AddProjectMember", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("UpdateRole", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("UpdatePolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("CreateGroup", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DeleteGroup", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("DetachGroupPolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("AttachGroupPolicy", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListGroupPolicies", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("AddUserToGroup", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("GetGroup", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListGroupsForUser", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListGroups", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("RemoveUserFromGroup", params, "application/x-www-form-urlencoded")
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
            body = self.call_judge("ListAllUserAccessKeys", params, "application/x-www-form-urlencoded")
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


    def InsertInstanceToES(self, request):
        """非标实例插入es
        :param request: Request instance for InsertInstanceToES.
        :type request: :class:`ksyun.client.iam.v20151101.models.InsertInstanceToESRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("InsertInstanceToES", params, "application/x-www-form-urlencoded")
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


    def DelInstanceFromES(self, request):
        """删除非标实例
        :param request: Request instance for DelInstanceFromES.
        :type request: :class:`ksyun.client.iam.v20151101.models.DelInstanceFromESRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DelInstanceFromES", params, "application/x-www-form-urlencoded")
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


