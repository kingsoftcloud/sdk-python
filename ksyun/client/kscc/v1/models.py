from ksyun.common.abstract_model import AbstractModel

class UpdateUserQuotaRequest(AbstractModel):
    """UpdateUserQuota请求参数结构体
    """

    def __init__(self):
        r"""更新用户月度配额；QuotaAmount不传或为空时清除该用户单独配额。
        :param UserName: 用户邮箱前缀，比如：zhangsan3
        :type PathPrefix: String
        :param QuotaAmount: 用户月度配额；为空表示清除用户单独配额
        :type PathPrefix: Double
        """
        self.UserName = None
        self.QuotaAmount = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("QuotaAmount"):
            self.QuotaAmount = params.get("QuotaAmount")


class DescribeUserCostSummaryRequest(AbstractModel):
    """DescribeUserCostSummary请求参数结构体
    """

    def __init__(self):
        r"""查询指定用户在某月份的配额和已使用金额。
        :param UserName: 用户邮箱前缀，比如：zhangsan3
        :type PathPrefix: String
        :param Month: 月份，格式：yyyyMM；不传默认当前月
        :type PathPrefix: String
        """
        self.UserName = None
        self.Month = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("Month"):
            self.Month = params.get("Month")


class DescribeAiLogDetailByIdsRequest(AbstractModel):
    """DescribeAiLogDetailByIds请求参数结构体
    """

    def __init__(self):
        r"""根据消息ID查询消息详情。
        :param MessageIds: 消息ID，多个用逗号分隔
        :type PathPrefix: String
        """
        self.MessageIds = None

    def _deserialize(self, params):
        if params.get("MessageIds"):
            self.MessageIds = params.get("MessageIds")


class DescribeAiLogDetailRequest(AbstractModel):
    """DescribeAiLogDetail请求参数结构体
    """

    def __init__(self):
        r"""根据时间、用户、模型等条件分页查询日志记录。
        :param StartTime: 日志开始时间，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param EndTime: 日志结束时间，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param UserName: 用户邮箱前缀
        :type PathPrefix: String
        :param ModelList: 模型列表，多个用逗号分隔
        :type PathPrefix: String
        :param Page: 页码，默认1
        :type PathPrefix: Int
        :param Size: 每页条数，默认10
        :type PathPrefix: Int
        """
        self.StartTime = None
        self.EndTime = None
        self.UserName = None
        self.ModelList = None
        self.Page = None
        self.Size = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("ModelList"):
            self.ModelList = params.get("ModelList")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("Size"):
            self.Size = params.get("Size")


class DescribeOrganizationTreeRequest(AbstractModel):
    """DescribeOrganizationTree请求参数结构体
    """

    def __init__(self):
        r"""查询企业部门组织树，包含父子部门关系和AI启用状态。
        """

    def _deserialize(self, params):
        return


class DescribeModelMetricsRequest(AbstractModel):
    """DescribeModelMetrics请求参数结构体
    """

    def __init__(self):
        r"""查询模型维度的请求量、Token量、TPM和RPM监控数据。
        :param StartTime: 开始时间，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param EndTime: 结束时间，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param ModelName: 模型名称，不传则查询全部模型
        :type PathPrefix: String
        :param TimeInterval: 统计粒度：min、hour、day；不传时自动判断
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.ModelName = None
        self.TimeInterval = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("ModelName"):
            self.ModelName = params.get("ModelName")
        if params.get("TimeInterval"):
            self.TimeInterval = params.get("TimeInterval")


class DescribeUserTokenUsageRequest(AbstractModel):
    """DescribeUserTokenUsage请求参数结构体
    """

    def __init__(self):
        r"""按时间范围查询用户Token和配额金额消耗，可按用户或部门过滤。
        :param StartTime: 开始时间，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param EndTime: 结束时间，格式：yyyy-MM-dd HH:mm:ss
        :type PathPrefix: String
        :param UserName: 用户邮箱前缀，不传则不过滤用户
        :type PathPrefix: String
        :param Department: 部门全路径（需要带所有父部门，例如：xx公司/xx事业部/研发部），不传则不过滤部门
        :type PathPrefix: String
        """
        self.StartTime = None
        self.EndTime = None
        self.UserName = None
        self.Department = None

    def _deserialize(self, params):
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("EndTime"):
            self.EndTime = params.get("EndTime")
        if params.get("UserName"):
            self.UserName = params.get("UserName")
        if params.get("Department"):
            self.Department = params.get("Department")


class DescribeUserQuotaListRequest(AbstractModel):
    """DescribeUserQuotaList请求参数结构体
    """

    def __init__(self):
        r"""分页查询用户月度配额、已用金额和使用比例。
        :param Keyword: 用户姓名、账号或部门关键字
        :type PathPrefix: String
        :param PageNum: 页码，默认1
        :type PathPrefix: Int
        :param PageSize: 每页条数，默认10
        :type PathPrefix: Int
        :param Month: 月份，格式：yyyyMM
        :type PathPrefix: String
        :param SortKey: 排序字段，如UsageAmount、UsagePercent
        :type PathPrefix: String
        :param SortType: 排序方向：asc或desc
        :type PathPrefix: String
        """
        self.Keyword = None
        self.PageNum = None
        self.PageSize = None
        self.Month = None
        self.SortKey = None
        self.SortType = None

    def _deserialize(self, params):
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("Month"):
            self.Month = params.get("Month")
        if params.get("SortKey"):
            self.SortKey = params.get("SortKey")
        if params.get("SortType"):
            self.SortType = params.get("SortType")


class DescribeQuotaGlobalConfigRequest(AbstractModel):
    """DescribeQuotaGlobalConfig请求参数结构体
    """

    def __init__(self):
        r"""查询账号、部门、成员配额开关和通用配置。
        """

    def _deserialize(self, params):
        return


class UpdateQuotaGlobalConfigRequest(AbstractModel):
    """UpdateQuotaGlobalConfig请求参数结构体
    """

    def __init__(self):
        r"""更新配额预警、折扣、联系人和各级配额开关。
        :param WarnThreshold: 预警阈值百分比，例如80表示80%
        :type PathPrefix: Int
        :param Discount: 费用折扣，例如9表示9折
        :type PathPrefix: Double
        :param ContactsJson: 预警联系人JSON字符串
        :type PathPrefix: String
        :param AccountEnabled: 账号配额开关，1启用，0禁用
        :type PathPrefix: Int
        :param DeptEnabled: 部门配额开关，1启用，0禁用
        :type PathPrefix: Int
        :param MemberEnabled: 成员配额开关，1启用，0禁用
        :type PathPrefix: Int
        :param DefaultMemberQuota: 默认成员月度配额
        :type PathPrefix: Double
        """
        self.WarnThreshold = None
        self.Discount = None
        self.ContactsJson = None
        self.AccountEnabled = None
        self.DeptEnabled = None
        self.MemberEnabled = None
        self.DefaultMemberQuota = None

    def _deserialize(self, params):
        if params.get("WarnThreshold"):
            self.WarnThreshold = params.get("WarnThreshold")
        if params.get("Discount"):
            self.Discount = params.get("Discount")
        if params.get("ContactsJson"):
            self.ContactsJson = params.get("ContactsJson")
        if params.get("AccountEnabled"):
            self.AccountEnabled = params.get("AccountEnabled")
        if params.get("DeptEnabled"):
            self.DeptEnabled = params.get("DeptEnabled")
        if params.get("MemberEnabled"):
            self.MemberEnabled = params.get("MemberEnabled")
        if params.get("DefaultMemberQuota"):
            self.DefaultMemberQuota = params.get("DefaultMemberQuota")


class DescribeAccountQuotaRequest(AbstractModel):
    """DescribeAccountQuota请求参数结构体
    """

    def __init__(self):
        r"""查询账号级月度配额、已用金额和使用比例。
        """

    def _deserialize(self, params):
        return


class UpdateAccountQuotaRequest(AbstractModel):
    """UpdateAccountQuota请求参数结构体
    """

    def __init__(self):
        r"""设置账号级月度配额，并可同步设置默认成员配额。
        :param QuotaAmount: 账号月度配额
        :type PathPrefix: Double
        """
        self.QuotaAmount = None

    def _deserialize(self, params):
        if params.get("QuotaAmount"):
            self.QuotaAmount = params.get("QuotaAmount")


class DeleteAccountQuotaRequest(AbstractModel):
    """DeleteAccountQuota请求参数结构体
    """

    def __init__(self):
        r"""删除账号级月度配额限制。
        """

    def _deserialize(self, params):
        return


class UpdateDefaultMemberQuotaRequest(AbstractModel):
    """UpdateDefaultMemberQuota请求参数结构体
    """

    def __init__(self):
        r"""设置全员默认成员月度配额。
        :param DefaultMemberQuota: 默认成员月度配额
        :type PathPrefix: Double
        """
        self.DefaultMemberQuota = None

    def _deserialize(self, params):
        if params.get("DefaultMemberQuota"):
            self.DefaultMemberQuota = params.get("DefaultMemberQuota")


class DeleteDefaultMemberQuotaRequest(AbstractModel):
    """DeleteDefaultMemberQuota请求参数结构体
    """

    def __init__(self):
        r"""清空全员默认成员月度配额，返回值为0。
        """

    def _deserialize(self, params):
        return


class DescribeDeptQuotaListRequest(AbstractModel):
    """DescribeDeptQuotaList请求参数结构体
    """

    def __init__(self):
        r"""分页查询部门月度配额、已用金额和使用比例。
        :param Keyword: 部门ID或部门名称关键字
        :type PathPrefix: String
        :param PageNum: 页码，默认1
        :type PathPrefix: Int
        :param PageSize: 每页条数，默认10
        :type PathPrefix: Int
        :param SortKey: 排序字段，如UsageAmount、UsagePercent
        :type PathPrefix: String
        :param SortType: 排序方向：asc或desc
        :type PathPrefix: String
        """
        self.Keyword = None
        self.PageNum = None
        self.PageSize = None
        self.SortKey = None
        self.SortType = None

    def _deserialize(self, params):
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("SortKey"):
            self.SortKey = params.get("SortKey")
        if params.get("SortType"):
            self.SortType = params.get("SortType")


class UpdateDeptQuotaRequest(AbstractModel):
    """UpdateDeptQuota请求参数结构体
    """

    def __init__(self):
        r"""设置指定部门的月度配额。
        :param DeptId: 部门ID
        :type PathPrefix: String
        :param QuotaAmount: 部门月度配额
        :type PathPrefix: Double
        """
        self.DeptId = None
        self.QuotaAmount = None

    def _deserialize(self, params):
        if params.get("DeptId"):
            self.DeptId = params.get("DeptId")
        if params.get("QuotaAmount"):
            self.QuotaAmount = params.get("QuotaAmount")


class DeleteDeptQuotaRequest(AbstractModel):
    """DeleteDeptQuota请求参数结构体
    """

    def __init__(self):
        r"""删除指定部门的月度配额限制。
        :param DeptId: 部门ID
        :type PathPrefix: String
        """
        self.DeptId = None

    def _deserialize(self, params):
        if params.get("DeptId"):
            self.DeptId = params.get("DeptId")


class DeleteUserQuotaRequest(AbstractModel):
    """DeleteUserQuota请求参数结构体
    """

    def __init__(self):
        r"""删除指定用户的月度配额限制。
        :param UserName: 用户邮箱前缀，比如：zhangsan3
        :type PathPrefix: String
        """
        self.UserName = None

    def _deserialize(self, params):
        if params.get("UserName"):
            self.UserName = params.get("UserName")


