from ksyun.common.abstract_model import AbstractModel

class CloudDeskreinstallRequest(AbstractModel):
    """CloudDeskreinstall请求参数结构体
    """

    def __init__(self):
        r"""云电脑重装系统
        :param instanceId: 云电脑 id
        :type PathPrefix: String
        :param imageId: 镜像 id
        :type PathPrefix: String
        """
        self.instanceId = None
        self.imageId = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")
        if params.get("imageId"):
            self.imageId = params.get("imageId")


class CloudDeskmanageRequest(AbstractModel):
    """CloudDeskmanage请求参数结构体
    """

    def __init__(self):
        r"""云电脑开机/关机/重启
        :param instanceIds: 云电脑 id 列表

        :type PathPrefix: String
        :param action1: start 开机
stop 关机
reboot 重启
forcedUnbind
        :type PathPrefix: String
        """
        self.instanceIds = None
        self.action1 = None

    def _deserialize(self, params):
        if params.get("instanceIds"):
            self.instanceIds = params.get("instanceIds")
        if params.get("action1"):
            self.action1 = params.get("action1")


class CloudDeskeditRequest(AbstractModel):
    """CloudDeskedit请求参数结构体
    """

    def __init__(self):
        r"""云电脑列表编辑
        :param instanceId: 云电脑id
        :type PathPrefix: String
        :param name: 自定义云电脑名称
        :type PathPrefix: String
        :param id: 
        :type PathPrefix: Int
        """
        self.instanceId = None
        self.name = None
        self.id = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")
        if params.get("name"):
            self.name = params.get("name")
        if params.get("id"):
            self.id = params.get("id")


class CloudDeskcreateRequest(AbstractModel):
    """CloudDeskcreate请求参数结构体
    """

    def __init__(self):
        r"""云电脑创建
        :param instanceName: 云电脑名称
        :type PathPrefix: String
        :param instanceType: 云电脑类型
4C8G
4C8G_1G
8C16G
8C16G_1G
8C16G_2G
16C16G_2G
16C32G
16C32G_2G
8C16G3060
16C32G3060
16C64G3060
        :type PathPrefix: String
        :param imageId: 镜像ID
        :type PathPrefix: String
        :param edgeNodeId: 区域 id, 通过区域列表接口获取
        :type PathPrefix: String
        :param systemDisk: 系统盘大小，单位 GB
        :type PathPrefix: Int
        :param dataDisk: 如果不需数据盘，传输 0 即可
        :type PathPrefix: Int
        :param billType: 计费模式
1: 包年包月
87: 按量付费
5：按量付费（按日月结）
        :type PathPrefix: Int
        :param duration: 单位:月， 仅 billType 为包年包月时填写

        :type PathPrefix: Int
        :param securityGroupId: 策略 id

        :type PathPrefix: String
        :param gpu: gpu类型：0,FPGA,vGPU 1G,vGPU 2G,3060 12G独显,2080Ti 2G
默认是套餐编码对应的gpu
        :type PathPrefix: String
        :param quantity: 默认1，创建实例台数
        :type PathPrefix: Int
        :param uniqueSuffix: 是否为HostName和InstanceName添加有序后缀。有序后缀从001开始递增，最大不能超过999。例如：LocalHost001，LocalHost002和MyInstance001，MyInstance002。
        :type PathPrefix: Boolean
        """
        self.instanceName = None
        self.instanceType = None
        self.imageId = None
        self.edgeNodeId = None
        self.systemDisk = None
        self.dataDisk = None
        self.billType = None
        self.duration = None
        self.securityGroupId = None
        self.gpu = None
        self.quantity = None
        self.uniqueSuffix = None

    def _deserialize(self, params):
        if params.get("instanceName"):
            self.instanceName = params.get("instanceName")
        if params.get("instanceType"):
            self.instanceType = params.get("instanceType")
        if params.get("imageId"):
            self.imageId = params.get("imageId")
        if params.get("edgeNodeId"):
            self.edgeNodeId = params.get("edgeNodeId")
        if params.get("systemDisk"):
            self.systemDisk = params.get("systemDisk")
        if params.get("dataDisk"):
            self.dataDisk = params.get("dataDisk")
        if params.get("billType"):
            self.billType = params.get("billType")
        if params.get("duration"):
            self.duration = params.get("duration")
        if params.get("securityGroupId"):
            self.securityGroupId = params.get("securityGroupId")
        if params.get("gpu"):
            self.gpu = params.get("gpu")
        if params.get("quantity"):
            self.quantity = params.get("quantity")
        if params.get("uniqueSuffix"):
            self.uniqueSuffix = params.get("uniqueSuffix")


class CloudDesklistRequest(AbstractModel):
    """CloudDesklist请求参数结构体
    """

    def __init__(self):
        r"""云电脑列表管理
        :param page: 
        :type PathPrefix: Int
        :param size: 
        :type PathPrefix: Int
        :param connected: on
off
        :type PathPrefix: String
        """
        self.page = None
        self.size = None
        self.connected = None

    def _deserialize(self, params):
        if params.get("page"):
            self.page = params.get("page")
        if params.get("size"):
            self.size = params.get("size")
        if params.get("connected"):
            self.connected = params.get("connected")


class StrategyruleeditRequest(AbstractModel):
    """Strategyruleedit请求参数结构体
    """

    def __init__(self):
        r"""修改策略组API
        :param policies: 安全组出站规则
        :type PathPrefix: Object
        :param securityGroupId: 策略组 id

        :type PathPrefix: String
        """
        self.policies = None
        self.securityGroupId = None

    def _deserialize(self, params):
        if params.get("policies"):
            self.policies = params.get("policies")
        if params.get("securityGroupId"):
            self.securityGroupId = params.get("securityGroupId")


class StrategyrulecreateRequest(AbstractModel):
    """Strategyrulecreate请求参数结构体
    """

    def __init__(self):
        r"""新建策略组规则API
        :param name: 规则名
        :type PathPrefix: String
        :param description: 规则描述
        :type PathPrefix: String
        :param policies: 安全组出站规则
        :type PathPrefix: Array
        """
        self.name = None
        self.description = None
        self.policies = None

    def _deserialize(self, params):
        if params.get("name"):
            self.name = params.get("name")
        if params.get("description"):
            self.description = params.get("description")
        if params.get("policies"):
            self.policies = params.get("policies")


class StrategyunboundRequest(AbstractModel):
    """Strategyunbound请求参数结构体
    """

    def __init__(self):
        r"""策略安全组解绑云电脑API
        :param securityGroupId: 策略组id
        :type PathPrefix: String
        :param instanceId: 云电脑id
        :type PathPrefix: String
        """
        self.securityGroupId = None
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("securityGroupId"):
            self.securityGroupId = params.get("securityGroupId")
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class StrategyboundRequest(AbstractModel):
    """Strategybound请求参数结构体
    """

    def __init__(self):
        r"""策略安全组绑定云电脑API
        :param securityGroupId: 策略组 id 

        :type PathPrefix: String
        :param instanceId: 云电脑 id
        :type PathPrefix: String
        """
        self.securityGroupId = None
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("securityGroupId"):
            self.securityGroupId = params.get("securityGroupId")
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class StrategydeleteRequest(AbstractModel):
    """Strategydelete请求参数结构体
    """

    def __init__(self):
        r"""策略安全组删除API
        :param id: 策略组 id 列表

        :type PathPrefix: Int
        """
        self.id = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")


class StrategyeditRequest(AbstractModel):
    """Strategyedit请求参数结构体
    """

    def __init__(self):
        r"""策略安全组修改API
        :param securityGroupId: 策略组唯一 id

        :type PathPrefix: String
        :param name: 策略组名称
        :type PathPrefix: String
        :param description: 描述信息

        :type PathPrefix: String
        """
        self.securityGroupId = None
        self.name = None
        self.description = None

    def _deserialize(self, params):
        if params.get("securityGroupId"):
            self.securityGroupId = params.get("securityGroupId")
        if params.get("name"):
            self.name = params.get("name")
        if params.get("description"):
            self.description = params.get("description")


class StrategycreateRequest(AbstractModel):
    """Strategycreate请求参数结构体
    """

    def __init__(self):
        r"""策略安全组创建API
        :param name: 策略组名称
        :type PathPrefix: String
        :param description: 描述信息
        :type PathPrefix: String
        """
        self.name = None
        self.description = None

    def _deserialize(self, params):
        if params.get("name"):
            self.name = params.get("name")
        if params.get("description"):
            self.description = params.get("description")


class StrategylistRequest(AbstractModel):
    """Strategylist请求参数结构体
    """

    def __init__(self):
        r"""策略安全组列表API
        :param size: 每页条数
        :type PathPrefix: Int
        :param page: 页码数
        :type PathPrefix: Int
        :param name: 根据名称模糊查询
        :type PathPrefix: String
        """
        self.size = None
        self.page = None
        self.name = None

    def _deserialize(self, params):
        if params.get("size"):
            self.size = params.get("size")
        if params.get("page"):
            self.page = params.get("page")
        if params.get("name"):
            self.name = params.get("name")


class RolesdeleteRequest(AbstractModel):
    """Rolesdelete请求参数结构体
    """

    def __init__(self):
        r"""角色删除API
        :param id: 角色主键 id
        :type PathPrefix: Int
        """
        self.id = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")


class RoleseditRequest(AbstractModel):
    """Rolesedit请求参数结构体
    """

    def __init__(self):
        r"""角色修改API
        :param id: 主键 id
        :type PathPrefix: Int
        :param name: 角色名称
        :type PathPrefix: String
        :param description: 描述信息
        :type PathPrefix: String
        :param fileTransfer: 远程文件
0: 禁用
1：启用

        :type PathPrefix: Int
        :param clipboard: 共享剪贴板
0: 禁用
1：启用
        :type PathPrefix: Int
        :param disk: 硬盘挂载
0: 禁用
1：启用

        :type PathPrefix: Int
        :param usb: usb 挂载
0: 禁用
1：启用
        :type PathPrefix: Int
        """
        self.id = None
        self.name = None
        self.description = None
        self.fileTransfer = None
        self.clipboard = None
        self.disk = None
        self.usb = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")
        if params.get("name"):
            self.name = params.get("name")
        if params.get("description"):
            self.description = params.get("description")
        if params.get("fileTransfer"):
            self.fileTransfer = params.get("fileTransfer")
        if params.get("clipboard"):
            self.clipboard = params.get("clipboard")
        if params.get("disk"):
            self.disk = params.get("disk")
        if params.get("usb"):
            self.usb = params.get("usb")


class RolescreateRequest(AbstractModel):
    """Rolescreate请求参数结构体
    """

    def __init__(self):
        r"""角色创建API
        :param name: 角色名称
        :type PathPrefix: String
        :param description: 描述信息
        :type PathPrefix: String
        :param fileTransfer: 远程文件
0: 禁用
1：启用
        :type PathPrefix: Int
        :param clipboard: 共享剪贴板
0: 禁用
1：启用
        :type PathPrefix: Int
        :param disk: 硬盘挂载
0: 禁用
1：启用

        :type PathPrefix: Int
        :param usb: usb 挂载
0: 禁用
1：启用
        :type PathPrefix: Int
        """
        self.name = None
        self.description = None
        self.fileTransfer = None
        self.clipboard = None
        self.disk = None
        self.usb = None

    def _deserialize(self, params):
        if params.get("name"):
            self.name = params.get("name")
        if params.get("description"):
            self.description = params.get("description")
        if params.get("fileTransfer"):
            self.fileTransfer = params.get("fileTransfer")
        if params.get("clipboard"):
            self.clipboard = params.get("clipboard")
        if params.get("disk"):
            self.disk = params.get("disk")
        if params.get("usb"):
            self.usb = params.get("usb")


class RoleslistRequest(AbstractModel):
    """Roleslist请求参数结构体
    """

    def __init__(self):
        r"""角色管理列表API
        :param size: 每页条数
        :type PathPrefix: Int
        :param page: 页码数

        :type PathPrefix: Int
        :param name: 根据名称模糊查询
        :type PathPrefix: String
        """
        self.size = None
        self.page = None
        self.name = None

    def _deserialize(self, params):
        if params.get("size"):
            self.size = params.get("size")
        if params.get("page"):
            self.page = params.get("page")
        if params.get("name"):
            self.name = params.get("name")


class ImagedeleteRequest(AbstractModel):
    """Imagedelete请求参数结构体
    """

    def __init__(self):
        r"""镜像删除API
        :param imageId: 镜像 id
        :type PathPrefix: String
        """
        self.imageId = None

    def _deserialize(self, params):
        if params.get("imageId"):
            self.imageId = params.get("imageId")


class ImageeditRequest(AbstractModel):
    """Imageedit请求参数结构体
    """

    def __init__(self):
        r"""镜像修改API
        :param id: 镜像主键 id
        :type PathPrefix: Int
        :param imageId: 镜像 id

        :type PathPrefix: String
        :param imageName: 镜像名称
        :type PathPrefix: String
        """
        self.id = None
        self.imageId = None
        self.imageName = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")
        if params.get("imageId"):
            self.imageId = params.get("imageId")
        if params.get("imageName"):
            self.imageName = params.get("imageName")


class ImagecreateRequest(AbstractModel):
    """Imagecreate请求参数结构体
    """

    def __init__(self):
        r"""镜像创建API
        :param imageName: 镜像名称

        :type PathPrefix: String
        :param description: 描述信息
        :type PathPrefix: String
        :param instanceId: 云电脑id
        :type PathPrefix: String
        """
        self.imageName = None
        self.description = None
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("imageName"):
            self.imageName = params.get("imageName")
        if params.get("description"):
            self.description = params.get("description")
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class ImagelistRequest(AbstractModel):
    """Imagelist请求参数结构体
    """

    def __init__(self):
        r"""镜像管理列表API
        :param size: 每条页数
        :type PathPrefix: Int
        :param page: 页码数
        :type PathPrefix: Int
        :param name: 根据名称模糊查询
        :type PathPrefix: String
        """
        self.size = None
        self.page = None
        self.name = None

    def _deserialize(self, params):
        if params.get("size"):
            self.size = params.get("size")
        if params.get("page"):
            self.page = params.get("page")
        if params.get("name"):
            self.name = params.get("name")


class StrategyrulebatchEditRequest(AbstractModel):
    """StrategyrulebatchEdit请求参数结构体
    """

    def __init__(self):
        r"""批量配置策略组规则API
        :param securityGroupId: 安全组id
        :type PathPrefix: String
        """
        self.securityGroupId = None

    def _deserialize(self, params):
        if params.get("securityGroupId"):
            self.securityGroupId = params.get("securityGroupId")


class MonitorregionsRequest(AbstractModel):
    """Monitorregions请求参数结构体
    """

    def __init__(self):
        r"""区域列表API
        """

    def _deserialize(self, params):
        return


class UsersinstancebindRequest(AbstractModel):
    """Usersinstancebind请求参数结构体
    """

    def __init__(self):
        r"""用户绑定云电脑
        :param id: 用户 id
        :type PathPrefix: Int
        :param instanceId: 云电脑 id
        :type PathPrefix: String
        """
        self.id = None
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class UserspasswordresetRequest(AbstractModel):
    """Userspasswordreset请求参数结构体
    """

    def __init__(self):
        r"""用户重置密码API
        :param id: 主键 id
        :type PathPrefix: Int
        :param password: base64 加密后的密码

        :type PathPrefix: String
        """
        self.id = None
        self.password = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")
        if params.get("password"):
            self.password = params.get("password")


class UsersdeleteRequest(AbstractModel):
    """Usersdelete请求参数结构体
    """

    def __init__(self):
        r"""用户删除API
        :param id: 用户主键 id
        :type PathPrefix: Int
        """
        self.id = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")


class UserseditRequest(AbstractModel):
    """Usersedit请求参数结构体
    """

    def __init__(self):
        r"""用户修改API
        :param id: 主键 id

        :type PathPrefix: Int
        :param name: 用户名
        :type PathPrefix: String
        :param phoneOrEmail: 电话或邮箱
        :type PathPrefix: String
        :param nickName: 昵称
        :type PathPrefix: String
        :param status: 1: 启用/0: 禁用
不传递或者传递 null 时不修改
        :type PathPrefix: Int
        """
        self.id = None
        self.name = None
        self.phoneOrEmail = None
        self.nickName = None
        self.status = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")
        if params.get("name"):
            self.name = params.get("name")
        if params.get("phoneOrEmail"):
            self.phoneOrEmail = params.get("phoneOrEmail")
        if params.get("nickName"):
            self.nickName = params.get("nickName")
        if params.get("status"):
            self.status = params.get("status")


class UserscreateRequest(AbstractModel):
    """Userscreate请求参数结构体
    """

    def __init__(self):
        r"""用户创建API
        :param name: 用户名
        :type PathPrefix: String
        :param password: 密码，请使用 base64 加密后传输
        :type PathPrefix: String
        :param phoneOrEmail: 手机号码或者邮箱
        :type PathPrefix: String
        :param roleId: 角色 id
        :type PathPrefix: Int
        """
        self.name = None
        self.password = None
        self.phoneOrEmail = None
        self.roleId = None

    def _deserialize(self, params):
        if params.get("name"):
            self.name = params.get("name")
        if params.get("password"):
            self.password = params.get("password")
        if params.get("phoneOrEmail"):
            self.phoneOrEmail = params.get("phoneOrEmail")
        if params.get("roleId"):
            self.roleId = params.get("roleId")


class UserslistRequest(AbstractModel):
    """Userslist请求参数结构体
    """

    def __init__(self):
        r"""用户列表API
        :param size: 每页条数

        :type PathPrefix: Int
        :param page: 页码数
        :type PathPrefix: Int
        """
        self.size = None
        self.page = None

    def _deserialize(self, params):
        if params.get("size"):
            self.size = params.get("size")
        if params.get("page"):
            self.page = params.get("page")


