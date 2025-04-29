from ksyun.common.abstract_model import AbstractModel


class CloudDeskreinstallRequest(AbstractModel):
    """CloudDeskreinstall请求参数结构体
    """

    def __init__(self):
        r"""允许用户对一个或多个云电脑实例执行系统重装操作。
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
        r"""提供对云电脑进行开机、关机、重启、删除、锁定和解锁的操作功能。
        :param instanceIds: 云电脑 id 列表

        :type PathPrefix: Array
        :param action1: start 开机
stop 关机
reboot 重启
forcedUnbind 强制解绑用户
delete 删除
lock 锁定
unlock 解锁
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
        r"""修改云电脑实例的名称
        :param instanceId: 云电脑id
        :type PathPrefix: String
        :param name: 自定义云电脑名称
        :type PathPrefix: String
        """
        self.instanceId = None
        self.name = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")
        if params.get("name"):
            self.name = params.get("name")


class CloudDeskcreateRequest(AbstractModel):
    """CloudDeskcreate请求参数结构体
    """

    def __init__(self):
        r"""此接口允许用户通过提供必要的参数（如实例名称、类型、镜像ID等）来创建新的云电脑实例。
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
        r"""该接口用于获取用户所拥有的所有云电脑实例的列表，支持分页查询，并能根据连接状态过滤结果。
        :param page: 
        :type PathPrefix: Int
        :param size: 
        :type PathPrefix: Int
        :param connected: 连接状态 on off
        :type PathPrefix: String
        :param labelIds: 云电脑已绑定的标签id,多个id使用英文逗号分隔
        :type PathPrefix: String
        :param name: 云电脑名称或实例id
        :type PathPrefix: String
        :param userName: 云电脑已绑定的用户名
        :type PathPrefix: String
        """
        self.page = None
        self.size = None
        self.connected = None
        self.labelIds = None
        self.name = None
        self.userName = None

    def _deserialize(self, params):
        if params.get("page"):
            self.page = params.get("page")
        if params.get("size"):
            self.size = params.get("size")
        if params.get("connected"):
            self.connected = params.get("connected")
        if params.get("labelIds"):
            self.labelIds = params.get("labelIds")
        if params.get("name"):
            self.name = params.get("name")
        if params.get("userName"):
            self.userName = params.get("userName")


class StrategyruleeditRequest(AbstractModel):
    """Strategyruleedit请求参数结构体
    """

    def __init__(self):
        r"""修改已有的策略安全组规则。
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
        r"""创建一个新的策略安全组规则。
        :param name: 策略名称
        :type PathPrefix: String
        :param description: 策略描述
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
        r"""解除当前云电脑与安全组的绑定关系。
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
        r"""将指定云电脑与策略安全组绑定。
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
        r"""删除指定的策略安全组。
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
        r"""修改现有策略安全组的信息。
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
        r"""创建一个新的策略安全组。
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
        r"""获取特定云电脑的安全组列表。
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
        r"""删除指定角色。
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
        r"""更新角色属性。
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
        r"""创建新角色，支持配置相应权限。
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
        r"""显示所有角色列表及其详细信息。
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
        r"""删除指定的镜像。
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
        r"""编辑已有镜像的信息。
        :param id: 镜像主键 id
        :type PathPrefix: Int
        :param imageId: 镜像 id

        :type PathPrefix: String
        :param imageName: 镜像名称
        :type PathPrefix: String
        :param description: 镜像描述信息
        :type PathPrefix: String
        """
        self.id = None
        self.imageId = None
        self.imageName = None
        self.description = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")
        if params.get("imageId"):
            self.imageId = params.get("imageId")
        if params.get("imageName"):
            self.imageName = params.get("imageName")
        if params.get("description"):
            self.description = params.get("description")


class ImagecreateRequest(AbstractModel):
    """Imagecreate请求参数结构体
    """

    def __init__(self):
        r"""创建自定义镜像。
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
        r"""列出所有可用的镜像资源列表。
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
        r"""批量删除策略安全组规则。
        :param securityGroupId: 安全组id
        :type PathPrefix: Array
        """
        self.securityGroupId = None

    def _deserialize(self, params):
        if params.get("securityGroupId"):
            self.securityGroupId = params.get("securityGroupId")


class MonitorregionsRequest(AbstractModel):
    """Monitorregions请求参数结构体
    """

    def __init__(self):
        r"""返回系统支持的所有地理区域的列表，包括其显示名称和对应的值。
        """

    def _deserialize(self, params):
        return


class UsersinstancebindRequest(AbstractModel):
    """Usersinstancebind请求参数结构体
    """

    def __init__(self):
        r"""将云电脑分配给指定用户。
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
        r"""重新设置用户密码。
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
        r"""删除指定用户账户。
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
        r"""更改相关用户资料。
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
        r"""注册新用户。
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
        r"""查看所有用户的概览信息。
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


class CloudDeskgetDesktopUrlRequest(AbstractModel):
    """CloudDeskgetDesktopUrl请求参数结构体
    """

    def __init__(self):
        r"""根据授权toen生成一个可以直接进入云电脑的URL
        :param token: 访问token
        :type PathPrefix: String
        :param instanceId: 实例id
        :type PathPrefix: String
        """
        self.token = None
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("token"):
            self.token = params.get("token")
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class QueryCloudDesksubmitShellRequest(AbstractModel):
    """QueryCloudDesksubmitShell请求参数结构体
    """

    def __init__(self):
        r"""提交一个可执行的脚本，支持ps1,bat脚本,请注意脚本的后缀,".ps1"的后缀会使用powershell 执行
        :param instanceIds: 
        :type PathPrefix: Array
        :param name: 
        :type PathPrefix: String
        :param shellContent: 脚本内容需要base64转下
        :type PathPrefix: String
        """
        self.instanceIds = None
        self.name = None
        self.shellContent = None

    def _deserialize(self, params):
        if params.get("instanceIds"):
            self.instanceIds = params.get("instanceIds")
        if params.get("name"):
            self.name = params.get("name")
        if params.get("shellContent"):
            self.shellContent = params.get("shellContent")


class CreateCloudDeskgetTokenRequest(AbstractModel):
    """CreateCloudDeskgetToken请求参数结构体
    """

    def __init__(self):
        r"""KOP鉴权通过之后，使用此接口可生成一个token用于快速登录云电脑
        :param username: 已分配的云电脑用户名
        :type PathPrefix: String
        :param password: 密码
        :type PathPrefix: String
        """
        self.username = None
        self.password = None

    def _deserialize(self, params):
        if params.get("username"):
            self.username = params.get("username")
        if params.get("password"):
            self.password = params.get("password")


class QueryShellStatusRequest(AbstractModel):
    """QueryShellStatus请求参数结构体
    """

    def __init__(self):
        r"""查询下发的脚本运行状态
        :param instanceIds: 云电脑 id,多个使用英文逗号分隔
        :type PathPrefix: String
        :param planId: 任务id
        :type PathPrefix: Int
        """
        self.instanceIds = None
        self.planId = None

    def _deserialize(self, params):
        if params.get("instanceIds"):
            self.instanceIds = params.get("instanceIds")
        if params.get("planId"):
            self.planId = params.get("planId")


class SetProxyIpRequest(AbstractModel):
    """SetProxyIp请求参数结构体
    """

    def __init__(self):
        r"""支持在云电脑里配置出口代理
        :param instanceIds: 云电脑id
        :type PathPrefix: Array
        :param province: 省份：湖北 湖南 江西 山东 江苏 安徽 浙江 福建 上海 广东 广西 海南 云南 贵州 西藏 重庆 宁夏 新疆 青海 陕西 甘肃 北京 天津 河北 山西 内蒙古 辽宁 吉林 黑龙江 四川 
        :type PathPrefix: String
        :param isp: 运营商：电信、联通、移动
        :type PathPrefix: String
        :param city: 城市
        :type PathPrefix: String
        """
        self.instanceIds = None
        self.province = None
        self.isp = None
        self.city = None

    def _deserialize(self, params):
        if params.get("instanceIds"):
            self.instanceIds = params.get("instanceIds")
        if params.get("province"):
            self.province = params.get("province")
        if params.get("isp"):
            self.isp = params.get("isp")
        if params.get("city"):
            self.city = params.get("city")


class GetProxyConfigRequest(AbstractModel):
    """GetProxyConfig请求参数结构体
    """

    def __init__(self):
        r"""查询出口代理ip
        :param instanceId: 云电脑 id
        :type PathPrefix: String
        """
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class QueryRuledetailRequest(AbstractModel):
    """QueryRuledetail请求参数结构体
    """

    def __init__(self):
        r"""根据策略组id查询策略规则详情
        :param securityGroupId: 策略组 id
        :type PathPrefix: String
        """
        self.securityGroupId = None

    def _deserialize(self, params):
        if params.get("securityGroupId"):
            self.securityGroupId = params.get("securityGroupId")


class QueryUsersinfoRequest(AbstractModel):
    """QueryUsersinfo请求参数结构体
    """

    def __init__(self):
        r"""查询注册时的用户账号信息，不支持模糊查询
        :param username: 用户名
        :type PathPrefix: String
        :param phone: 手机号
        :type PathPrefix: String
        :param email: 邮箱
        :type PathPrefix: String
        """
        self.username = None
        self.phone = None
        self.email = None

    def _deserialize(self, params):
        if params.get("username"):
            self.username = params.get("username")
        if params.get("phone"):
            self.phone = params.get("phone")
        if params.get("email"):
            self.email = params.get("email")


class GetDetailRequest(AbstractModel):
    """GetDetail请求参数结构体
    """

    def __init__(self):
        r"""查询云电脑实例详情信息
        :param instanceId: 实例id
        :type PathPrefix: String
        """
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class ListLabelRequest(AbstractModel):
    """ListLabel请求参数结构体
    """

    def __init__(self):
        r"""查询所有标签
        :param name: 标签名
        :type PathPrefix: String
        """
        self.name = None

    def _deserialize(self, params):
        if params.get("name"):
            self.name = params.get("name")


class CancelInstanceLabelRequest(AbstractModel):
    """CancelInstanceLabel请求参数结构体
    """

    def __init__(self):
        r"""解绑云电脑已绑定的标签
        :param labelId: 标签id
        :type PathPrefix: Array
        :param instanceId: 实例id
        :type PathPrefix: String
        """
        self.labelId = None
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("labelId"):
            self.labelId = params.get("labelId")
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class UpdateInstanceLabelRequest(AbstractModel):
    """UpdateInstanceLabel请求参数结构体
    """

    def __init__(self):
        r"""绑定标签到云电脑
        :param labelId: 标签id
        :type PathPrefix: Array
        :param instanceId: 云桌面实例id
        :type PathPrefix: String
        """
        self.labelId = None
        self.instanceId = None

    def _deserialize(self, params):
        if params.get("labelId"):
            self.labelId = params.get("labelId")
        if params.get("instanceId"):
            self.instanceId = params.get("instanceId")


class DeleteLabelRequest(AbstractModel):
    """DeleteLabel请求参数结构体
    """

    def __init__(self):
        r"""删除一个或多个标签，删除标签后，已绑定过此标签的云桌面上的标签都将被删除
        :param id: 标签id
        :type PathPrefix: Array
        """
        self.id = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")


class UpdateLabelRequest(AbstractModel):
    """UpdateLabel请求参数结构体
    """

    def __init__(self):
        r"""修改标签名
        :param id: 标签id
        :type PathPrefix: Int
        :param name: 标签名
        :type PathPrefix: String
        """
        self.id = None
        self.name = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")
        if params.get("name"):
            self.name = params.get("name")


class CreateLabelRequest(AbstractModel):
    """CreateLabel请求参数结构体
    """

    def __init__(self):
        r"""创建一个标签，用于分类管理云桌面
        :param name: 标签名
        :type PathPrefix: String
        """
        self.name = None

    def _deserialize(self, params):
        if params.get("name"):
            self.name = params.get("name")
