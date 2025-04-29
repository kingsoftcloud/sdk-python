import json

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException
from ksyun.common.abstract_client import AbstractClient


class KedClient(AbstractClient):
    _apiVersion = 'V1'
    _endpoint = 'ked.api.ksyun.com'
    _service = 'ked'

    def CloudDeskreinstall(self, request):
        """允许用户对一个或多个云电脑实例执行系统重装操作。
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
        """提供对云电脑进行开机、关机、重启、删除、锁定和解锁的操作功能。
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
        """修改云电脑实例的名称
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
        """此接口允许用户通过提供必要的参数（如实例名称、类型、镜像ID等）来创建新的云电脑实例。
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
        """该接口用于获取用户所拥有的所有云电脑实例的列表，支持分页查询，并能根据连接状态过滤结果。
        :param request: Request instance for CloudDesklist.
        :type request: :class:`ksyun.client.ked.v20250501.models.CloudDesklistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloudDesklist", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """修改已有的策略安全组规则。
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
        """创建一个新的策略安全组规则。
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
        """解除当前云电脑与安全组的绑定关系。
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
        """将指定云电脑与策略安全组绑定。
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
        """删除指定的策略安全组。
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
        """修改现有策略安全组的信息。
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
        """创建一个新的策略安全组。
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
        """获取特定云电脑的安全组列表。
        :param request: Request instance for Strategylist.
        :type request: :class:`ksyun.client.ked.v20250501.models.StrategylistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Strategylist", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """删除指定角色。
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
        """更新角色属性。
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
        """创建新角色，支持配置相应权限。
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
        """显示所有角色列表及其详细信息。
        :param request: Request instance for Roleslist.
        :type request: :class:`ksyun.client.ked.v20250501.models.RoleslistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Roleslist", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """删除指定的镜像。
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
        """编辑已有镜像的信息。
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
        """创建自定义镜像。
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
        """列出所有可用的镜像资源列表。
        :param request: Request instance for Imagelist.
        :type request: :class:`ksyun.client.ked.v20250501.models.ImagelistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Imagelist", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """批量删除策略安全组规则。
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
        """返回系统支持的所有地理区域的列表，包括其显示名称和对应的值。
        :param request: Request instance for Monitorregions.
        :type request: :class:`ksyun.client.ked.v20250501.models.MonitorregionsRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Monitorregions", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
        """将云电脑分配给指定用户。
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
        """重新设置用户密码。
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
        """删除指定用户账户。
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
        """更改相关用户资料。
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
        """注册新用户。
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
        """查看所有用户的概览信息。
        :param request: Request instance for Userslist.
        :type request: :class:`ksyun.client.ked.v20250501.models.UserslistRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("Userslist", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def CloudDeskgetDesktopUrl(self, request):
        """根据授权toen生成一个可以直接进入云电脑的URL
        :param request: Request instance for CloudDeskgetDesktopUrl.
        :type request: :class:`ksyun.client.ked.v20250501.models.CloudDeskgetDesktopUrlRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CloudDeskgetDesktopUrl", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def QueryCloudDesksubmitShell(self, request):
        """提交一个可执行的脚本，支持ps1,bat脚本,请注意脚本的后缀,".ps1"的后缀会使用powershell 执行
        :param request: Request instance for QueryCloudDesksubmitShell.
        :type request: :class:`ksyun.client.ked.v20250501.models.QueryCloudDesksubmitShellRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryCloudDesksubmitShell", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def CreateCloudDeskgetToken(self, request):
        """KOP鉴权通过之后，使用此接口可生成一个token用于快速登录云电脑
        :param request: Request instance for CreateCloudDeskgetToken.
        :type request: :class:`ksyun.client.ked.v20250501.models.CreateCloudDeskgetTokenRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateCloudDeskgetToken", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def QueryShellStatus(self, request):
        """查询下发的脚本运行状态
        :param request: Request instance for QueryShellStatus.
        :type request: :class:`ksyun.client.ked.v20250501.models.QueryShellStatusRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryShellStatus", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def SetProxyIp(self, request):
        """支持在云电脑里配置出口代理
        :param request: Request instance for SetProxyIp.
        :type request: :class:`ksyun.client.ked.v20250501.models.SetProxyIpRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("SetProxyIp", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def GetProxyConfig(self, request):
        """查询出口代理ip
        :param request: Request instance for GetProxyConfig.
        :type request: :class:`ksyun.client.ked.v20250501.models.GetProxyConfigRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetProxyConfig", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def QueryRuledetail(self, request):
        """根据策略组id查询策略规则详情
        :param request: Request instance for QueryRuledetail.
        :type request: :class:`ksyun.client.ked.v20250501.models.QueryRuledetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryRuledetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def QueryUsersinfo(self, request):
        """查询注册时的用户账号信息，不支持模糊查询
        :param request: Request instance for QueryUsersinfo.
        :type request: :class:`ksyun.client.ked.v20250501.models.QueryUsersinfoRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("QueryUsersinfo", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def GetDetail(self, request):
        """查询云电脑实例详情信息
        :param request: Request instance for GetDetail.
        :type request: :class:`ksyun.client.ked.v20250501.models.GetDetailRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("GetDetail", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def ListLabel(self, request):
        """查询所有标签
        :param request: Request instance for ListLabel.
        :type request: :class:`ksyun.client.ked.v20250501.models.ListLabelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("ListLabel", params, "application/x-www-form-urlencoded")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def CancelInstanceLabel(self, request):
        """解绑云电脑已绑定的标签
        :param request: Request instance for CancelInstanceLabel.
        :type request: :class:`ksyun.client.ked.v20250501.models.CancelInstanceLabelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CancelInstanceLabel", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def UpdateInstanceLabel(self, request):
        """绑定标签到云电脑
        :param request: Request instance for UpdateInstanceLabel.
        :type request: :class:`ksyun.client.ked.v20250501.models.UpdateInstanceLabelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateInstanceLabel", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def DeleteLabel(self, request):
        """删除一个或多个标签，删除标签后，已绑定过此标签的云桌面上的标签都将被删除
        :param request: Request instance for DeleteLabel.
        :type request: :class:`ksyun.client.ked.v20250501.models.DeleteLabelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("DeleteLabel", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def UpdateLabel(self, request):
        """修改标签名
        :param request: Request instance for UpdateLabel.
        :type request: :class:`ksyun.client.ked.v20250501.models.UpdateLabelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("UpdateLabel", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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

    def CreateLabel(self, request):
        """创建一个标签，用于分类管理云桌面
        :param request: Request instance for CreateLabel.
        :type request: :class:`ksyun.client.ked.v20250501.models.CreateLabelRequest`
        """
        try:
            params = request._serialize()
            body = self.call_judge("CreateLabel", params, "application/json")
            response = json.loads(body)
            if "Error" not in response:
                return body
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
