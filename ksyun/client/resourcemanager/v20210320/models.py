from ksyun.common.abstract_model import AbstractModel


class CreateFolderRequest(AbstractModel):
    """CreateFolder请求参数结构体
    """

    def __init__(self):
        r"""创建资源夹
        :param ParentId: 父级资源夹ID
        :type PathPrefix: String
        :param Name: 资源夹名称	
        :type PathPrefix: String
        :param Desc: 备注
        :type PathPrefix: String
        """
        self.ParentId = None
        self.Name = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("ParentId"):
            self.ParentId = params.get("ParentId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class DeleteFolderRequest(AbstractModel):
    """DeleteFolder请求参数结构体
    """

    def __init__(self):
        r"""删除资源夹
        :param FolderId: 资源夹ID
        :type PathPrefix: String
        """
        self.FolderId = None

    def _deserialize(self, params):
        if params.get("FolderId"):
            self.FolderId = params.get("FolderId")


class UpdateFolderRequest(AbstractModel):
    """UpdateFolder请求参数结构体
    """

    def __init__(self):
        r"""更新资源夹
        :param FolderId: 资源夹ID
        :type PathPrefix: String
        :param ParentId: 父级资源夹ID
        :type PathPrefix: String
        :param Name: 新的资源夹名称
        :type PathPrefix: String
        :param Desc: 新的备注
        :type PathPrefix: String
        """
        self.FolderId = None
        self.ParentId = None
        self.Name = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("FolderId"):
            self.FolderId = params.get("FolderId")
        if params.get("ParentId"):
            self.ParentId = params.get("ParentId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class ListAccountsForParentRequest(AbstractModel):
    """ListAccountsForParent请求参数结构体
    """

    def __init__(self):
        r"""某资源夹下所有用户
        :param FolderId: 资源夹ID
        :type PathPrefix: String
        :param Search: 搜索成员名称/账号ID/用户名
        :type PathPrefix: String
        :param Page: 页码
        :type PathPrefix: Int
        :param PageSize: 每页显示条数
        :type PathPrefix: Int
        """
        self.FolderId = None
        self.Search = None
        self.Page = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("FolderId"):
            self.FolderId = params.get("FolderId")
        if params.get("Search"):
            self.Search = params.get("Search")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class MoveAccountRequest(AbstractModel):
    """MoveAccount请求参数结构体
    """

    def __init__(self):
        r"""移动成员到其他资源夹
        :param Ids: 成员uid，多个英文逗号分隔
        :type PathPrefix: String
        :param FromFolderId: 当前所在资源夹ID
        :type PathPrefix: String
        :param ToFolderId: 移动目标资源夹ID
        :type PathPrefix: String
        """
        self.Ids = None
        self.FromFolderId = None
        self.ToFolderId = None

    def _deserialize(self, params):
        if params.get("Ids"):
            self.Ids = params.get("Ids")
        if params.get("FromFolderId"):
            self.FromFolderId = params.get("FromFolderId")
        if params.get("ToFolderId"):
            self.ToFolderId = params.get("ToFolderId")


class UpdateAccountRequest(AbstractModel):
    """UpdateAccount请求参数结构体
    """

    def __init__(self):
        r"""更新成员
        :param MemberId: 成员UID
        :type PathPrefix: Int
        :param NewDisplayName: 修改的展示名称
        :type PathPrefix: String
        :param FolderId: 修改的资源夹id
        :type PathPrefix: String
        """
        self.MemberId = None
        self.NewDisplayName = None
        self.FolderId = None

    def _deserialize(self, params):
        if params.get("MemberId"):
            self.MemberId = params.get("MemberId")
        if params.get("NewDisplayName"):
            self.NewDisplayName = params.get("NewDisplayName")
        if params.get("FolderId"):
            self.FolderId = params.get("FolderId")


class ListAccountsRequest(AbstractModel):
    """ListAccounts请求参数结构体
    """

    def __init__(self):
        r"""查看整个资源目录下的所有成员信息
        :param PageNumber: 页码，默认第一页
        :type PathPrefix: Int
        :param PageSize: 每页展示多少条，默认10条
        :type PathPrefix: Int
        :param IsAll: 是否查询所有成员账号，1-是 0否；
如传1，PageNumber和PageSize无效
        :type PathPrefix: Int
        """
        self.PageNumber = None
        self.PageSize = None
        self.IsAll = None

    def _deserialize(self, params):
        if params.get("PageNumber"):
            self.PageNumber = params.get("PageNumber")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("IsAll"):
            self.IsAll = params.get("IsAll")


class ListFoldersRequest(AbstractModel):
    """ListFolders请求参数结构体
    """

    def __init__(self):
        r"""资源夹列表
        """

    def _deserialize(self, params):
        return
