import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KedClient(AbstractClient):
    _apiVersion = 'V1'
    _endpoint = 'ked.api.ksyun.com'
    _service = 'ked'
    def CloudDeskreinstall(self, request):
        """云电脑重装系统
        :param request: Request instance for CloudDeskreinstall.
        :type request: :class:`ksyun.client.ked.v20250501.models.CloudDeskreinstallRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloudDeskreinstall", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CloudDeskmanage(self, request):
        """云电脑开机/关机/重启
        :param request: Request instance for CloudDeskmanage.
        :type request: :class:`ksyun.client.ked.v20250501.models.CloudDeskmanageRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloudDeskmanage", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CloudDeskedit(self, request):
        """云电脑列表编辑
        :param request: Request instance for CloudDeskedit.
        :type request: :class:`ksyun.client.ked.v20250501.models.CloudDeskeditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloudDeskedit", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CloudDeskcreate(self, request):
        """云电脑创建
        :param request: Request instance for CloudDeskcreate.
        :type request: :class:`ksyun.client.ked.v20250501.models.CloudDeskcreateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloudDeskcreate", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def CloudDesklist(self, request):
        """云电脑列表管理
        :param request: Request instance for CloudDesklist.
        :type request: :class:`ksyun.client.ked.v20250501.models.CloudDesklistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloudDesklist", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Strategyruleedit(self, request):
        """修改策略组API
        :param request: Request instance for Strategyruleedit.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategyruleeditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategyruleedit", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Strategyrulecreate(self, request):
        """新建策略组规则API
        :param request: Request instance for Strategyrulecreate.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategyrulecreateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategyrulecreate", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Strategyunbound(self, request):
        """策略安全组解绑云电脑API
        :param request: Request instance for Strategyunbound.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategyunboundRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategyunbound", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Strategybound(self, request):
        """策略安全组绑定云电脑API
        :param request: Request instance for Strategybound.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategyboundRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategybound", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Strategydelete(self, request):
        """策略安全组删除API
        :param request: Request instance for Strategydelete.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategydeleteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategydelete", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Strategyedit(self, request):
        """策略安全组修改API
        :param request: Request instance for Strategyedit.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategyeditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategyedit", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Strategycreate(self, request):
        """策略安全组创建API
        :param request: Request instance for Strategycreate.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategycreateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategycreate", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Strategylist(self, request):
        """策略安全组列表API
        :param request: Request instance for Strategylist.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategylistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategylist", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Rolesdelete(self, request):
        """角色删除API
        :param request: Request instance for Rolesdelete.
        :type request: :class:`ksyun.client.ked.v20250501.models.RolesdeleteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Rolesdelete", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Rolesedit(self, request):
        """角色修改API
        :param request: Request instance for Rolesedit.
        :type request: :class:`ksyun.client.ked.v20250501.models.RoleseditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Rolesedit", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Rolescreate(self, request):
        """角色创建API
        :param request: Request instance for Rolescreate.
        :type request: :class:`ksyun.client.ked.v20250501.models.RolescreateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Rolescreate", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Roleslist(self, request):
        """角色管理列表API
        :param request: Request instance for Roleslist.
        :type request: :class:`ksyun.client.ked.v20250501.models.RoleslistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Roleslist", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Imagedelete(self, request):
        """镜像删除API
        :param request: Request instance for Imagedelete.
        :type request: :class:`ksyun.client.ked.v20250501.models.ImagedeleteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Imagedelete", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Imageedit(self, request):
        """镜像修改API
        :param request: Request instance for Imageedit.
        :type request: :class:`ksyun.client.ked.v20250501.models.ImageeditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Imageedit", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Imagecreate(self, request):
        """镜像创建API
        :param request: Request instance for Imagecreate.
        :type request: :class:`ksyun.client.ked.v20250501.models.ImagecreateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Imagecreate", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Imagelist(self, request):
        """镜像管理列表API
        :param request: Request instance for Imagelist.
        :type request: :class:`ksyun.client.ked.v20250501.models.ImagelistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Imagelist", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def StrategyrulebatchEdit(self, request):
        """批量配置策略组规则API
        :param request: Request instance for StrategyrulebatchEdit.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategyrulebatchEditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("StrategyrulebatchEdit", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Monitorregions(self, request):
        """区域列表API
        :param request: Request instance for Monitorregions.
        :type request: :class:`ksyun.client.ked.v20250501.models.MonitorregionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Monitorregions", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Usersinstancebind(self, request):
        """用户绑定云电脑
        :param request: Request instance for Usersinstancebind.
        :type request: :class:`ksyun.client.ked.v20250501.models.UsersinstancebindRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Usersinstancebind", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Userspasswordreset(self, request):
        """用户重置密码API
        :param request: Request instance for Userspasswordreset.
        :type request: :class:`ksyun.client.ked.v20250501.models.UserspasswordresetRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Userspasswordreset", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Usersdelete(self, request):
        """用户删除API
        :param request: Request instance for Usersdelete.
        :type request: :class:`ksyun.client.ked.v20250501.models.UsersdeleteRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Usersdelete", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Usersedit(self, request):
        """用户修改API
        :param request: Request instance for Usersedit.
        :type request: :class:`ksyun.client.ked.v20250501.models.UserseditRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Usersedit", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Userscreate(self, request):
        """用户创建API
        :param request: Request instance for Userscreate.
        :type request: :class:`ksyun.client.ked.v20250501.models.UserscreateRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Userscreate", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


    def Userslist(self, request):
        """用户列表API
        :param request: Request instance for Userslist.
        :type request: :class:`ksyun.client.ked.v20250501.models.UserslistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Userslist", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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


