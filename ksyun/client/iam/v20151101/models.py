from ksyun.common.abstract_model import AbstractModel

class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体
    """

    def __init__(self):
        r"""新建IAM子用户
        :param UserName: 待创建的IAM用户的用户名
        :type PathPrefix: String
        :param RealName: 待创建的IAM用户的真实姓名
        :type PathPrefix: String
        :param Phone: 手机号码
        :type PathPrefix: String
        :param Email: 邮箱
        :type PathPrefix: String
        :param Remark: 备注
        :type PathPrefix: String
        :param Password: 用户密码
        :type PathPrefix: String
        :param PasswordResetRequired: 登录是否重置密码
        :type PathPrefix: Int
        :param OpenLoginProtection: 是否开启登录保护
        :type PathPrefix: Int
        :param OpenSecurityProtection: 是否开启操作保护
        :type PathPrefix: Int
        :param ViewAllProject: 子用户查看所有项目
        :type PathPrefix: Int
        :param AddProjectId: 项目ID，默认项目传0
        :type PathPrefix: Int
        """
        self.UserName = None
        self.RealName = None
        self.Phone = None
        self.Email = None
        self.Remark = None
        self.Password = None
        self.PasswordResetRequired = None
        self.OpenLoginProtection = None
        self.OpenSecurityProtection = None
        self.ViewAllProject = None
        self.AddProjectId = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("RealName"):
            self.RealName = params.get("RealName")
        if params.get("Phone"):
            self.Phone = params.get("Phone")
        if params.get("Email"):
            self.Email = params.get("Email")
        if params.get("Remark"):
            self.Remark = params.get("Remark")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("PasswordResetRequired"):
            self.PasswordResetRequired = params.get("PasswordResetRequired")
        if params.get("OpenLoginProtection"):
            self.OpenLoginProtection = params.get("OpenLoginProtection")
        if params.get("OpenSecurityProtection"):
            self.OpenSecurityProtection = params.get("OpenSecurityProtection")
        if params.get("ViewAllProject"):
            self.ViewAllProject = params.get("ViewAllProject")
        if params.get("AddProjectId"):
            self.AddProjectId = params.get("AddProjectId")


class ListUsersRequest(AbstractModel):
    """ListUsers请求参数结构体
    """

    def __init__(self):
        r"""查询所有子用户的详细信息
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询用户操作的起始点

取值范围：1-320
        :type PathPrefix: String
        :param MaxItems: 
用于限制本次查询结果返回的用户数量，如果仍有额外用户未显示，则返回元素中的IsTruncated的值会被设置为true，同时返回下次查询的起始点Marker值

取值范围：1 ~ 100。默认值：100。
        :type PathPrefix: Int
        :param AccessKey: 用户ak
        :type PathPrefix: String
        """
        self.Marker = None
        self.MaxItems = None
        self.AccessKey = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")
        if params.get("AccessKey"):
            self.AccessKey = params.get("AccessKey")


class UpdateUserRequest(AbstractModel):
    """UpdateUser请求参数结构体
    """

    def __init__(self):
        r"""更新用户基本信息
        :param UserName: 需要修改的IAM子用户名
        :type PathPrefix: String
        :param NewUserName: 新的IAM用户名，如果未传入则说明不改变
        :type PathPrefix: String
        :param NewRealName: 新的IAM用户真实姓名，如果未传入则说明不改变
        :type PathPrefix: String
        :param NewEmail: 新的IAM用户Email，如果未传入则说明不改变
        :type PathPrefix: String
        :param NewPhone: 新的IAM用户手机，如果未传入则说明不改变
        :type PathPrefix: String
        :param IsInternational: 
        :type PathPrefix: Int
        :param NewRemark: 
        :type PathPrefix: String
        """
        self.UserName = None
        self.NewUserName = None
        self.NewRealName = None
        self.NewEmail = None
        self.NewPhone = None
        self.IsInternational = None
        self.NewRemark = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("NewUserName"):
            self.NewUserName = params.get("NewUserName")
        if params.get("NewRealName"):
            self.NewRealName = params.get("NewRealName")
        if params.get("NewEmail"):
            self.NewEmail = params.get("NewEmail")
        if params.get("NewPhone"):
            self.NewPhone = params.get("NewPhone")
        if params.get("IsInternational"):
            self.IsInternational = params.get("IsInternational")
        if params.get("NewRemark"):
            self.NewRemark = params.get("NewRemark")


class GetUserRequest(AbstractModel):
    """GetUser请求参数结构体
    """

    def __init__(self):
        r"""查询子用户基本信息
        :param UserName: UserName
        :type PathPrefix: String
        """
        self.UserName = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体
    """

    def __init__(self):
        r"""删除子用户
        :param UserName: UserName
        :type PathPrefix: String
        """
        self.UserName = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy请求参数结构体
    """

    def __init__(self):
        r"""解绑IAM用户策略
        :param PolicyKrn: 需要解绑的策略的krn标识
格式：krn:ksc:iam::account-id:policy/policy-name
        :type PathPrefix: String
        :param UserName: 需要解绑的策略的目标用户名
        :type PathPrefix: String
        """
        self.PolicyKrn = None
        self.UserName = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies请求参数结构体
    """

    def __init__(self):
        r"""查询用户附加策略列表
        :param UserName: 待查询策略列表的目标用户名
        :type PathPrefix: String
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询策略信息列表操作的起始点
最短1,最长320
        :type PathPrefix: String
        :param MaxItems: 用于限制本次查询结果返回的策略数量，如果仍有额外策略未显示，则返回元素中的IsTruncated的值会被设置为true，同时返回下次查询的起始点Marker值
最小值1，最大值1000，默认100
        :type PathPrefix: String
        """
        self.UserName = None
        self.Marker = None
        self.MaxItems = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")


class ListPolicyVersionsRequest(AbstractModel):
    """ListPolicyVersions请求参数结构体
    """

    def __init__(self):
        r"""查询策略版本列表
        :param PolicyKrn: 待查询策略版本列表的策略的唯一标识

格式：krn:ksc:iam::account-id:policy/policy-name	
        :type PathPrefix: String
        """
        self.PolicyKrn = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")


class SetDefaultPolicyVersionRequest(AbstractModel):
    """SetDefaultPolicyVersion请求参数结构体
    """

    def __init__(self):
        r"""设定默认策略版本
        :param PolicyKrn: 待设定默认策略版本的策略标识
格式：krn:ksc:iam::account-id:policy/policy-name
        :type PathPrefix: String
        :param VersionId: 待设定为默认版本的策略版本Id
        :type PathPrefix: String
        """
        self.PolicyKrn = None
        self.VersionId = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")
        if params.get("VersionId"):
            self.VersionId = params.get("VersionId")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy请求参数结构体
    """

    def __init__(self):
        r"""附加用户策略
        :param PolicyKrn: 待附加的策略标识
格式：krn:ksc:iam::account-id:policy/policy-name
        :type PathPrefix: String
        :param UserName: 策略的附加目标用户名
        :type PathPrefix: String
        """
        self.PolicyKrn = None
        self.UserName = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class DeletePolicyVersionRequest(AbstractModel):
    """DeletePolicyVersion请求参数结构体
    """

    def __init__(self):
        r"""删除策略版本内容
        :param PolicyKrn: 待删除策略版本的策略的唯一标识
格式：krn:ksc:iam::account-id:policy/policy-name	
        :type PathPrefix: String
        :param VersionId: 待删除的策略版本Id
        :type PathPrefix: String
        """
        self.PolicyKrn = None
        self.VersionId = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")
        if params.get("VersionId"):
            self.VersionId = params.get("VersionId")


class GetPolicyVersionRequest(AbstractModel):
    """GetPolicyVersion请求参数结构体
    """

    def __init__(self):
        r"""查询策略版本内容
        :param PolicyKrn: 待查询的策略的唯一标识
格式：krn:ksc:iam::account-id:policy/policy-name
        :type PathPrefix: String
        :param VersionId: 待查询的策略版本Id
        :type PathPrefix: String
        """
        self.PolicyKrn = None
        self.VersionId = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")
        if params.get("VersionId"):
            self.VersionId = params.get("VersionId")


class CreatePolicyVersionRequest(AbstractModel):
    """CreatePolicyVersion请求参数结构体
    """

    def __init__(self):
        r"""新建策略版本内容
        :param PolicyKrn: 待创建新版本的策略的唯一标识
格式：krn:ksc:iam::account-id:policy/policy-name
        :type PathPrefix: String
        :param PolicyDocument: 待创建新策略版本的策略文档内容
        :type PathPrefix: String
        :param SetAsDefault: 可选参数，用于设置是否将新创建的策略版本指定为默认策略版本
        :type PathPrefix: String
        :param PolicyStruct: 
        :type PathPrefix: String
        """
        self.PolicyKrn = None
        self.PolicyDocument = None
        self.SetAsDefault = None
        self.PolicyStruct = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")
        if params.get("PolicyDocument"):
            self.PolicyDocument = params.get("PolicyDocument")
        if params.get("SetAsDefault"):
            self.SetAsDefault = params.get("SetAsDefault")
        if params.get("PolicyStruct"):
            self.PolicyStruct = params.get("PolicyStruct")


class ListPoliciesRequest(AbstractModel):
    """ListPolicies请求参数结构体
    """

    def __init__(self):
        r"""查询策略信息列表
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询策略信息列表操作的起始点

最短1,最长320
        :type PathPrefix: String
        :param MaxItems: 用于限制本次查询结果返回的策略数量，如果仍有额外策略未显示，则返回元素中的IsTruncated的值会被设置为true，同时返回下次查询的起始点Marker值
最小值1，最大值1000，默认100
        :type PathPrefix: String
        :param OnlyAttached: 可选参数，用于过滤策略列表，如果设置则只返回已经附加到实体上策略
        :type PathPrefix: Boolean
        :param Scope: 用于过滤显示策略范围，ALL为全部，KSC是系统策略、Local是自定义策略
        :type PathPrefix: String
        """
        self.Marker = None
        self.MaxItems = None
        self.OnlyAttached = None
        self.Scope = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")
        if params.get("OnlyAttached"):
            self.OnlyAttached = params.get("OnlyAttached")
        if params.get("Scope"):
            self.Scope = params.get("Scope")


class GetPolicyRequest(AbstractModel):
    """GetPolicy请求参数结构体
    """

    def __init__(self):
        r"""查询策略元数据信息
        :param PolicyKrn: 
        :type PathPrefix: String
        """
        self.PolicyKrn = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")


class DeletePolicyRequest(AbstractModel):
    """DeletePolicy请求参数结构体
    """

    def __init__(self):
        r"""删除策略
        :param PolicyKrn: 待删除策略的唯一标识
格式：krn:ksc:iam::account-id:policy/policy-name
        :type PathPrefix: String
        """
        self.PolicyKrn = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")


class CreatePolicyRequest(AbstractModel):
    """CreatePolicy请求参数结构体
    """

    def __init__(self):
        r"""新建策略
        :param PolicyName: 待创建策略的策略名称
最短1,最长128
        :type PathPrefix: String
        :param Description: 策略描述
        :type PathPrefix: String
        :param PolicyDocument: 待创建的自定义策略的策略文档内容
最短1,最长5K
        :type PathPrefix: String
        :param PolicyStruct: 
        :type PathPrefix: String
        :param CreateMode: 
        :type PathPrefix: String
        """
        self.PolicyName = None
        self.Description = None
        self.PolicyDocument = None
        self.PolicyStruct = None
        self.CreateMode = None

    def _deserialize(self, params):
        if params.get("PolicyName"):
            self.PolicyName = params.get("PolicyName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("PolicyDocument"):
            self.PolicyDocument = params.get("PolicyDocument")
        if params.get("PolicyStruct"):
            self.PolicyStruct = params.get("PolicyStruct")
        if params.get("CreateMode"):
            self.CreateMode = params.get("CreateMode")


class ChangePasswordRequest(AbstractModel):
    """ChangePassword请求参数结构体
    """

    def __init__(self):
        r"""子用户修改密码
        :param OldPassword: 用户的旧登录密码
        :type PathPrefix: String
        :param NewPassword: 用户的新登录密码
        :type PathPrefix: String
        """
        self.OldPassword = None
        self.NewPassword = None

    def _deserialize(self, params):
        if params.get("OldPassword"):
            self.OldPassword = params.get("OldPassword")
        if params.get("NewPassword"):
            self.NewPassword = params.get("NewPassword")


class UpdateLoginProfileRequest(AbstractModel):
    """UpdateLoginProfile请求参数结构体
    """

    def __init__(self):
        r"""更新子用户登录配置
        :param UserName: 待更新登录配置的IAM用户名
        :type PathPrefix: String
        :param Password: 新密码，可选参数，注：
- 当传参且值为空字符串时，关闭子用户控制台登录；
- 当传参不为空字符串时，启用子用户控制台登录，并设置新密码；
- 当不传参时，沿用原设置；
        :type PathPrefix: String
        :param PasswordResetRequired: 可选参数，标识用户下次成功登录后是否需要设置新密码,带参数调用即为true，否则不带参数为false
        :type PathPrefix: Boolean
        :param OpenLoginProtection: 可选参数，开启登录操作保护，不带参数不处理，带参数 为true开启，false关闭
        :type PathPrefix: Boolean
        :param OpenSecurityProtection: 可选参数，开启敏感操作保护，不带参数不处理，带参数 为true开启，false关闭
        :type PathPrefix: Boolean
        :param ViewAllProject: 可选参数，标识用户是否可以查看全部项目,带参数调用即为true，否则不带参数为false
        :type PathPrefix: Boolean
        """
        self.UserName = None
        self.Password = None
        self.PasswordResetRequired = None
        self.OpenLoginProtection = None
        self.OpenSecurityProtection = None
        self.ViewAllProject = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("PasswordResetRequired"):
            self.PasswordResetRequired = params.get("PasswordResetRequired")
        if params.get("OpenLoginProtection"):
            self.OpenLoginProtection = params.get("OpenLoginProtection")
        if params.get("OpenSecurityProtection"):
            self.OpenSecurityProtection = params.get("OpenSecurityProtection")
        if params.get("ViewAllProject"):
            self.ViewAllProject = params.get("ViewAllProject")


class GetLoginProfileRequest(AbstractModel):
    """GetLoginProfile请求参数结构体
    """

    def __init__(self):
        r"""查询登录配置信息
        :param UserName: 要查询的IAM子用户名称
        :type PathPrefix: String
        :param NotCheckPassword: 该字段默认是0，0的情况查询未开启控制台访问的账号会抛出异常"LoginProfileNoSuchEntity"，传1则都可以查看，可通过出参"ConsoleLogin"来判断是否开启了控制台访问和编程API访问。
        :type PathPrefix: Int
        """
        self.UserName = None
        self.NotCheckPassword = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("NotCheckPassword"):
            self.NotCheckPassword = params.get("NotCheckPassword")


class CreateAccessKeyRequest(AbstractModel):
    """CreateAccessKey请求参数结构体
    """

    def __init__(self):
        r"""生成访问密钥
        :param UserName: IAM子用户名
        :type PathPrefix: String
        """
        self.UserName = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class ListAccessKeysRequest(AbstractModel):
    """ListAccessKeys请求参数结构体
    """

    def __init__(self):
        r"""查询访问密钥列表
        :param UserName: IAM子用户名
        :type PathPrefix: String
        """
        self.UserName = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class UpdateAccessKeyRequest(AbstractModel):
    """UpdateAccessKey请求参数结构体
    """

    def __init__(self):
        r"""更新访问密钥
        :param AccessKeyId: 访问密钥ID
        :type PathPrefix: String
        :param UserName: IAM子用户的用户名
        :type PathPrefix: String
        :param Status: 修改后的访问密钥的状态，Active为可用，Inactive为不可用
        :type PathPrefix: String
        """
        self.AccessKeyId = None
        self.UserName = None
        self.Status = None

    def _deserialize(self, params):
        if params.get("AccessKeyId"):
            self.AccessKeyId = params.get("AccessKeyId")
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("Status"):
            self.Status = params.get("Status")


class DeleteAccessKeyRequest(AbstractModel):
    """DeleteAccessKey请求参数结构体
    """

    def __init__(self):
        r"""删除访问密钥
        :param UserName: IAM子用户的用户名
        :type PathPrefix: String
        :param AccessKeyId: 访问密钥ID
        :type PathPrefix: String
        """
        self.UserName = None
        self.AccessKeyId = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("AccessKeyId"):
            self.AccessKeyId = params.get("AccessKeyId")


class ListVirtualMFADevicesRequest(AbstractModel):
    """ListVirtualMFADevices请求参数结构体
    """

    def __init__(self):
        r"""查询虚拟设备列表
        :param AssignmentStatus: AssignmentStatus
        :type PathPrefix: String
        :param Marker: Marker
        :type PathPrefix: String
        :param MaxItems: MaxItems
        :type PathPrefix: Int
        """
        self.AssignmentStatus = None
        self.Marker = None
        self.MaxItems = None

    def _deserialize(self, params):
        if params.get("AssignmentStatus"):
            self.AssignmentStatus = params.get("AssignmentStatus")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")


class EnableMFADeviceRequest(AbstractModel):
    """EnableMFADevice请求参数结构体
    """

    def __init__(self):
        r"""激活虚拟设备
        :param AuthenticationCode1: AuthenticationCode1
        :type PathPrefix: String
        :param AuthenticationCode2: AuthenticationCode2
        :type PathPrefix: String
        :param SerialNumber: SerialNumber
        :type PathPrefix: String
        :param UserName: UserName
        :type PathPrefix: String
        """
        self.AuthenticationCode1 = None
        self.AuthenticationCode2 = None
        self.SerialNumber = None
        self.UserName = None

    def _deserialize(self, params):
        if params.get("AuthenticationCode1"):
            self.AuthenticationCode1 = params.get("AuthenticationCode1")
        if params.get("AuthenticationCode2"):
            self.AuthenticationCode2 = params.get("AuthenticationCode2")
        if params.get("SerialNumber"):
            self.SerialNumber = params.get("SerialNumber")
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class DeactivateMFADeviceRequest(AbstractModel):
    """DeactivateMFADevice请求参数结构体
    """

    def __init__(self):
        r"""解绑虚拟设备
        :param SerialNumber: krn
        :type PathPrefix: String
        :param UserName: UserName
        :type PathPrefix: String
        """
        self.SerialNumber = None
        self.UserName = None

    def _deserialize(self, params):
        if params.get("SerialNumber"):
            self.SerialNumber = params.get("SerialNumber")
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class GetVirtualMFADeviceRequest(AbstractModel):
    """GetVirtualMFADevice请求参数结构体
    """

    def __init__(self):
        r"""获取虚拟设备
        :param UserName: UserName
        :type PathPrefix: String
        """
        self.UserName = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class CreateRoleRequest(AbstractModel):
    """CreateRole请求参数结构体
    """

    def __init__(self):
        r"""创建角色
        :param RoleName: 角色名称
        :type PathPrefix: String
        :param TrustAccounts: 信任账号列表(多个账号之间使用半角逗号(,)分隔，最多可以有20个账号)
        :type PathPrefix: String
        :param Description: 角色描述
        :type PathPrefix: String
        """
        self.RoleName = None
        self.TrustAccounts = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("RoleName"):
            self.RoleName = params.get("RoleName")
        if params.get("TrustAccounts"):
            self.TrustAccounts = params.get("TrustAccounts")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteRoleRequest(AbstractModel):
    """DeleteRole请求参数结构体
    """

    def __init__(self):
        r"""删除角色
        :param RoleName: 要删除的角色名称
        :type PathPrefix: String
        """
        self.RoleName = None

    def _deserialize(self, params):
        if params.get("RoleName"):
            self.RoleName = params.get("RoleName")


class GetRoleRequest(AbstractModel):
    """GetRole请求参数结构体
    """

    def __init__(self):
        r"""查询角色基本信息
        :param RoleName: 要查询的角色名称
        :type PathPrefix: String
        """
        self.RoleName = None

    def _deserialize(self, params):
        if params.get("RoleName"):
            self.RoleName = params.get("RoleName")


class ListRolesRequest(AbstractModel):
    """ListRoles请求参数结构体
    """

    def __init__(self):
        r"""查询账号的角色列表
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询操作的起始点，Marker值不会过期
        :type PathPrefix: String
        :param MaxItems: 用于限制本次查询结果返回的数量，如果仍有额外元素未显示，则返回元素中的IsTruncated的值会被设置为true，同时返回下次查询的起始点Marker值
        :type PathPrefix: Int
        """
        self.Marker = None
        self.MaxItems = None

    def _deserialize(self, params):
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")


class AttachRolePolicyRequest(AbstractModel):
    """AttachRolePolicy请求参数结构体
    """

    def __init__(self):
        r"""附加角色的访问策略
        :param RoleName: 角色名称
        :type PathPrefix: String
        :param PolicyKrn: 需要附加给角色的策略的krn
        :type PathPrefix: String
        """
        self.RoleName = None
        self.PolicyKrn = None

    def _deserialize(self, params):
        if params.get("RoleName"):
            self.RoleName = params.get("RoleName")
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")


class DetachRolePolicyRequest(AbstractModel):
    """DetachRolePolicy请求参数结构体
    """

    def __init__(self):
        r"""分离角色的访问策略
        :param RoleName: 角色名称
        :type PathPrefix: String
        :param PolicyKrn: 待分离的策略krn标识
        :type PathPrefix: String
        """
        self.RoleName = None
        self.PolicyKrn = None

    def _deserialize(self, params):
        if params.get("RoleName"):
            self.RoleName = params.get("RoleName")
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")


class ListAttachedRolePoliciesRequest(AbstractModel):
    """ListAttachedRolePolicies请求参数结构体
    """

    def __init__(self):
        r"""查询角色附加的策略列表
        :param RoleName: 角色名称
        :type PathPrefix: String
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询操作的起始点，Marker值不会过期
        :type PathPrefix: String
        :param MaxItems: 用于限制本次查询结果返回的数量，如果仍有额外元素未显示，则返回元素中的IsTruncated的值会被设置为true，同时返回下次查询的起始点Marker值
        :type PathPrefix: Int
        """
        self.RoleName = None
        self.Marker = None
        self.MaxItems = None

    def _deserialize(self, params):
        if params.get("RoleName"):
            self.RoleName = params.get("RoleName")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")


class UpdateRoleTrustAccountsRequest(AbstractModel):
    """UpdateRoleTrustAccounts请求参数结构体
    """

    def __init__(self):
        r"""更新角色的信任关系
        :param RoleName: 角色名称
        :type PathPrefix: String
        :param NewTrustAccounts: 信任账号列表(多个账号之间使用半角逗号(,)分隔，最多可以有20个账号)
        :type PathPrefix: String
        """
        self.RoleName = None
        self.NewTrustAccounts = None

    def _deserialize(self, params):
        if params.get("RoleName"):
            self.RoleName = params.get("RoleName")
        if params.get("NewTrustAccounts"):
            self.NewTrustAccounts = params.get("NewTrustAccounts")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体
    """

    def __init__(self):
        r"""创建项目
        :param ProjectName: 项目名称，64个字符以内
        :type PathPrefix: String
        :param ProjectDesc: 项目描述
        :type PathPrefix: String
        """
        self.ProjectName = None
        self.ProjectDesc = None

    def _deserialize(self, params):
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("ProjectDesc"):
            self.ProjectDesc = params.get("ProjectDesc")


class UpdateProjectInfoRequest(AbstractModel):
    """UpdateProjectInfo请求参数结构体
    """

    def __init__(self):
        r"""更新项目信息
        :param ProjectId: ProjectId
        :type PathPrefix: Int
        :param ProjectName: 项目名称，最多64个字符
        :type PathPrefix: String
        :param ProjectDesc: 项目描述，最多64个字符
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ProjectName"):
            self.ProjectName = params.get("ProjectName")
        if params.get("ProjectDesc"):
            self.ProjectDesc = params.get("ProjectDesc")


class GetAccountAllProjectListRequest(AbstractModel):
    """GetAccountAllProjectList请求参数结构体
    """

    def __init__(self):
        r"""获取主/子用户项目列表
        """

    def _deserialize(self, params):
        return


class UpdateInstanceProjectIdRequest(AbstractModel):
    """UpdateInstanceProjectId请求参数结构体
    """

    def __init__(self):
        r"""更新实例项目
        :param ProjectId: ProjectId
        :type PathPrefix: Int
        :param InstanceId: 实例id
        :type PathPrefix: String
        :param Action: Action
        :type PathPrefix: String
        :param Version: Version
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.InstanceId = None
        self.Action = None
        self.Version = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("Action"):
            self.Action = params.get("Action")
        if params.get("Version"):
            self.Version = params.get("Version")


class ListEntitiesForPolicyRequest(AbstractModel):
    """ListEntitiesForPolicy请求参数结构体
    """

    def __init__(self):
        r"""查询策略关联实体列表
        :param PolicyKrn: 待查询的策略krn
        :type PathPrefix: String
        :param MaxItems: 用于限制本次查询结果返回的关联实体数量，如果仍有额外关联实体未显示，则返回元素中的IsTruncated的值会被设置为true，同时返回下次查询的起始点Marker值
        :type PathPrefix: Int
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询关联实体操作的起始点
        :type PathPrefix: String
        """
        self.PolicyKrn = None
        self.MaxItems = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ListProjectMemberRequest(AbstractModel):
    """ListProjectMember请求参数结构体
    """

    def __init__(self):
        r"""查询项目成员列表
        :param ProjectId: 项目ID
        :type PathPrefix: Int
        """
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class DeleteProjectMemberRequest(AbstractModel):
    """DeleteProjectMember请求参数结构体
    """

    def __init__(self):
        r"""删除项目成员
        :param ProjectId: 项目id
        :type PathPrefix: Int
        :param MemberIds: 要移除的成员id
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.MemberIds = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("MemberIds"):
            self.MemberIds = params.get("MemberIds")


class AddProjectMemberRequest(AbstractModel):
    """AddProjectMember请求参数结构体
    """

    def __init__(self):
        r"""添加项目成员
        :param ProjectId: 项目ID
        :type PathPrefix: Int
        :param IdentityId: 如果成员类型是IAM子用户，传UserId
如果成员类型是IAM角色，传RoleId
        :type PathPrefix: String
        :param IdentityType: 成员类型：1子用户，2角色
        :type PathPrefix: Int
        """
        self.ProjectId = None
        self.IdentityId = None
        self.IdentityType = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("IdentityId"):
            self.IdentityId = params.get("IdentityId")
        if params.get("IdentityType"):
            self.IdentityType = params.get("IdentityType")


class UpdateRoleRequest(AbstractModel):
    """UpdateRole请求参数结构体
    """

    def __init__(self):
        r"""更新角基本描述
        :param RoleName: 角色名称
        :type PathPrefix: String
        :param NewDescription: 新角色描述
        :type PathPrefix: String
        """
        self.RoleName = None
        self.NewDescription = None

    def _deserialize(self, params):
        if params.get("RoleName"):
            self.RoleName = params.get("RoleName")
        if params.get("NewDescription"):
            self.NewDescription = params.get("NewDescription")


class UpdatePolicyRequest(AbstractModel):
    """UpdatePolicy请求参数结构体
    """

    def __init__(self):
        r"""更新策略描述
        :param PolicyKrn: 策略krn
        :type PathPrefix: String
        :param NewDescription: 新策略描述
        :type PathPrefix: String
        :param NewPolicyName: 策略名称
        :type PathPrefix: String
        """
        self.PolicyKrn = None
        self.NewDescription = None
        self.NewPolicyName = None

    def _deserialize(self, params):
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")
        if params.get("NewDescription"):
            self.NewDescription = params.get("NewDescription")
        if params.get("NewPolicyName"):
            self.NewPolicyName = params.get("NewPolicyName")


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体
    """

    def __init__(self):
        r"""创建用户组
        :param GroupName: 用户组名称
1-64个字符，允许输入大小写英文字母，数字，' . '，' _ ' 或 ' - '


        :type PathPrefix: String
        :param Description: 用户组描述，1-64字符
        :type PathPrefix: String
        :param GroupRealName: 组别名
        :type PathPrefix: String
        """
        self.GroupName = None
        self.Description = None
        self.GroupRealName = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("GroupRealName"):
            self.GroupRealName = params.get("GroupRealName")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体
    """

    def __init__(self):
        r"""删除用户组
        :param GroupName: 用户组名称
        :type PathPrefix: String
        """
        self.GroupName = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")


class DetachGroupPolicyRequest(AbstractModel):
    """DetachGroupPolicy请求参数结构体
    """

    def __init__(self):
        r"""从用户组分离策略
        :param GroupName: 用户组名
        :type PathPrefix: String
        :param PolicyKrn: 要分离的策略krn

        :type PathPrefix: String
        """
        self.GroupName = None
        self.PolicyKrn = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")


class AttachGroupPolicyRequest(AbstractModel):
    """AttachGroupPolicy请求参数结构体
    """

    def __init__(self):
        r"""附加策略到用户组
        :param GroupName: 用户组名称
        :type PathPrefix: String
        :param PolicyKrn: 要附加的策略krn
        :type PathPrefix: String
        """
        self.GroupName = None
        self.PolicyKrn = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("PolicyKrn"):
            self.PolicyKrn = params.get("PolicyKrn")


class ListGroupPoliciesRequest(AbstractModel):
    """ListGroupPolicies请求参数结构体
    """

    def __init__(self):
        r"""获取用户组权限列表
        :param GroupName: 用户组名称
        :type PathPrefix: String
        :param MaxItems: 最大返回个数，默认值100
        :type PathPrefix: String
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询用户操作的起始点
        :type PathPrefix: String
        """
        self.GroupName = None
        self.MaxItems = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class AddUserToGroupRequest(AbstractModel):
    """AddUserToGroup请求参数结构体
    """

    def __init__(self):
        r"""添加用户到用户组
        :param GroupName: 用户组名称
        :type PathPrefix: String
        :param UserName: 要添加的IAM子用户名称
        :type PathPrefix: String
        """
        self.GroupName = None
        self.UserName = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class GetGroupRequest(AbstractModel):
    """GetGroup请求参数结构体
    """

    def __init__(self):
        r"""获取用户组基础信息
        :param GroupName: 用户组名称
        :type PathPrefix: String
        :param MaxItems: 最大返回个数，默认值100
        :type PathPrefix: String
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询用户操作的起始点
        :type PathPrefix: String
        """
        self.GroupName = None
        self.MaxItems = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ListGroupsForUserRequest(AbstractModel):
    """ListGroupsForUser请求参数结构体
    """

    def __init__(self):
        r"""获取用户所属用户组列表
        :param UserName: 要查询的IAM用户名称
        :type PathPrefix: String
        :param MaxItems: 最大返回个数，默认值100
        :type PathPrefix: String
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询用户操作的起始点
        :type PathPrefix: String
        """
        self.UserName = None
        self.MaxItems = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class ListGroupsRequest(AbstractModel):
    """ListGroups请求参数结构体
    """

    def __init__(self):
        r"""获取用户组列表
        :param MaxItems: 最大返回个数，默认值100
        :type PathPrefix: String
        :param Marker: 当返回结果被截断时，使用本次返回的Marker值用于标示下次调用查询用户操作的起始点
        :type PathPrefix: String
        """
        self.MaxItems = None
        self.Marker = None

    def _deserialize(self, params):
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")
        if params.get("Marker"):
            self.Marker = params.get("Marker")


class RemoveUserFromGroupRequest(AbstractModel):
    """RemoveUserFromGroup请求参数结构体
    """

    def __init__(self):
        r"""从用户组删除用户
        :param GroupName: 用户组名称
        :type PathPrefix: String
        :param UserName: 待移除的子用户名称
        :type PathPrefix: String
        """
        self.GroupName = None
        self.UserName = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("UserName"):
            self.UserName = params.get("UserName")


class UpdateGroupRequest(AbstractModel):
    """UpdateGroup请求参数结构体
    """

    def __init__(self):
        r"""更新用户组基本信息
        :param GroupName: 要更新的用户组名称
        :type PathPrefix: String
        :param Description: 新用户组描述
        :type PathPrefix: String
        :param GroupRealName: 新别名
        :type PathPrefix: String
        """
        self.GroupName = None
        self.Description = None
        self.GroupRealName = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("GroupRealName"):
            self.GroupRealName = params.get("GroupRealName")


class ListUsersForGroupRequest(AbstractModel):
    """ListUsersForGroup请求参数结构体
    """

    def __init__(self):
        r"""获取组成员列表
        :param GroupName: 组名
        :type PathPrefix: String
        :param MaxItems: 默认500条，最大1000条
        :type PathPrefix: Int
        :param Page: 页码
        :type PathPrefix: Int
        """
        self.GroupName = None
        self.MaxItems = None
        self.Page = None

    def _deserialize(self, params):
        if params.get("GroupName"):
            self.GroupName = params.get("GroupName")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")
        if params.get("Page"):
            self.Page = params.get("Page")


class ListAllUserAccessKeysRequest(AbstractModel):
    """ListAllUserAccessKeys请求参数结构体
    """

    def __init__(self):
        r"""获取子用户ak最后使用时间
        """

    def _deserialize(self, params):
        return


class InsertInstanceToESRequest(AbstractModel):
    """InsertInstanceToES请求参数结构体
    """

    def __init__(self):
        r"""非标实例插入es
        :param ProjectId: 
        :type PathPrefix: Int
        :param ProductLine: 
        :type PathPrefix: String
        :param ProductGroup: 
        :type PathPrefix: Int
        :param ResourceType: 
        :type PathPrefix: String
        :param InstanceId: 
        :type PathPrefix: String
        :param RegionEn: 
        :type PathPrefix: String
        :param InstanceName: 
        :type PathPrefix: String
        """
        self.ProjectId = None
        self.ProductLine = None
        self.ProductGroup = None
        self.ResourceType = None
        self.InstanceId = None
        self.RegionEn = None
        self.InstanceName = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("ProductLine"):
            self.ProductLine = params.get("ProductLine")
        if params.get("ProductGroup"):
            self.ProductGroup = params.get("ProductGroup")
        if params.get("ResourceType"):
            self.ResourceType = params.get("ResourceType")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("RegionEn"):
            self.RegionEn = params.get("RegionEn")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")


class DelInstanceFromESRequest(AbstractModel):
    """DelInstanceFromES请求参数结构体
    """

    def __init__(self):
        r"""删除非标实例
        :param ProductLine: 
        :type PathPrefix: String
        :param InstanceId: 
        :type PathPrefix: String
        """
        self.ProductLine = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("ProductLine"):
            self.ProductLine = params.get("ProductLine")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class GetAccountAllProjectsByParamsRequest(AbstractModel):
    """GetAccountAllProjectsByParams请求参数结构体
    """

    def __init__(self):
        r"""根据参数获取账户项目列表
        :param Ps: 每页显示条数
        :type PathPrefix: Int
        :param Pn: 页码
        :type PathPrefix: Int
        :param ParamUserName: 子账号用户名
        :type PathPrefix: String
        :param ParamAccessKey: 该主账号下任意一个子账号的AccessKey
        :type PathPrefix: String
        """
        self.Ps = None
        self.Pn = None
        self.ParamUserName = None
        self.ParamAccessKey = None

    def _deserialize(self, params):
        if params.get("Ps"):
            self.Ps = params.get("Ps")
        if params.get("Pn"):
            self.Pn = params.get("Pn")
        if params.get("ParamUserName"):
            self.ParamUserName = params.get("ParamUserName")
        if params.get("ParamAccessKey"):
            self.ParamAccessKey = params.get("ParamAccessKey")


class SetUserSsoSettingsRequest(AbstractModel):
    """SetUserSsoSettings请求参数结构体
    """

    def __init__(self):
        r"""设置用户SSO身份提供商信息
        :param Status: 是否开启用户 SSO
0否 1是
        :type PathPrefix: Int
        :param Metadata: 	
元数据文档。经过 Base64 编码
        :type PathPrefix: String
        :param Domain: 域名 状态开启时必填
        :type PathPrefix: String
        """
        self.Status = None
        self.Metadata = None
        self.Domain = None

    def _deserialize(self, params):
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("Metadata"):
            self.Metadata = params.get("Metadata")
        if params.get("Domain"):
            self.Domain = params.get("Domain")


class GetUserSsoSettingsRequest(AbstractModel):
    """GetUserSsoSettings请求参数结构体
    """

    def __init__(self):
        r"""查询用户SSO身份提供商信息
        """

    def _deserialize(self, params):
        return


class GetEffectivePoliciesRequest(AbstractModel):
    """GetEffectivePolicies请求参数结构体
    """

    def __init__(self):
        r"""获取有效的策略信息
        :param PolicyName: 策略名称
        :type PathPrefix: String
        :param Page: 页码
        :type PathPrefix: Int
        :param MaxItems: 每页返回条数，最高500条
        :type PathPrefix: Int
        """
        self.PolicyName = None
        self.Page = None
        self.MaxItems = None

    def _deserialize(self, params):
        if params.get("PolicyName"):
            self.PolicyName = params.get("PolicyName")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("MaxItems"):
            self.MaxItems = params.get("MaxItems")


