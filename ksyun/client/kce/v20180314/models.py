from ksyun.common.abstract_model import AbstractModel


class CreateRepoNamespaceRequest(AbstractModel):
    """CreateRepoNamespace请求参数结构体
    """

    def __init__(self):
        r"""创建命名空间
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        :param Public: 命名空间属性，决定其下的镜像仓库的属性。<br>true：公有；false：私有
        :type PathPrefix: String
        """
        self.Namespace = None
        self.Public = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("Public"):
            self.Public = params.get("Public")


class DescribeRepoNamespaceRequest(AbstractModel):
    """DescribeRepoNamespace请求参数结构体
    """

    def __init__(self):
        r"""查询命名空间
        :param Namespace: 命名空间名称，若不填写，则默认返回该用户所有命名空间。
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99。
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: String
        :param Filter: 
        :type PathPrefix: Filter
        """
        self.Namespace = None
        self.MaxResults = None
        self.Marker = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class ModifyRepoNamespaceTypeRequest(AbstractModel):
    """ModifyRepoNamespaceType请求参数结构体
    """

    def __init__(self):
        r"""修改命名空间属性
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        :param Public: 命名空间属性:<br>true：公共；false：私有
        :type PathPrefix: Boolean
        """
        self.Namespace = None
        self.Public = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("Public"):
            self.Public = params.get("Public")


class RepoNamespaceExistRequest(AbstractModel):
    """RepoNamespaceExist请求参数结构体
    """

    def __init__(self):
        r"""查询命名空间是否存在
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        """
        self.Namespace = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository请求参数结构体
    """

    def __init__(self):
        r"""创建镜像仓库
        :param RepoName: 镜像仓库名称，在这里我们定义reponame是命名空间/仓库，如我们要创建的仓库是nginx，所属命名空间是mynamespace，则reponame为mynamespace/nginx。
        :type PathPrefix: String
        :param Description: 镜像仓库描述信息
        :type PathPrefix: String
        """
        self.RepoName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("Description"):
            self.Description = params.get("Description")


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository请求参数结构体
    """

    def __init__(self):
        r"""删除镜像仓库
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        """
        self.RepoName = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")


class DescribeRepositoryRequest(AbstractModel):
    """DescribeRepository请求参数结构体
    """

    def __init__(self):
        r"""查询镜像仓库
        :param RepoName: 镜像仓库名称,若不输入，则默认查询该用户的所有镜像仓库。
        :type PathPrefix: Filter
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99。
        :type PathPrefix: Int
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: Int
        :param Filter: 
        :type PathPrefix: Filter
        """
        self.RepoName = None
        self.MaxResults = None
        self.Marker = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class DescribePublicRepositoryRequest(AbstractModel):
    """DescribePublicRepository请求参数结构体
    """

    def __init__(self):
        r"""查询ksyun公有镜像仓库列表
        :param RepoName: 镜像仓库名称
        :type PathPrefix: Filter
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99。
        :type PathPrefix: Int
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: Int
        :param Filter: 
        :type PathPrefix: Filter
        """
        self.RepoName = None
        self.MaxResults = None
        self.Marker = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class UpdateRepoDescRequest(AbstractModel):
    """UpdateRepoDesc请求参数结构体
    """

    def __init__(self):
        r"""更新仓库描述信息
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param Description: 镜像仓库描述内容
        :type PathPrefix: String
        """
        self.RepoName = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("Description"):
            self.Description = params.get("Description")


class DescribeTagRequest(AbstractModel):
    """DescribeTag请求参数结构体
    """

    def __init__(self):
        r"""查询镜像tag列表
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99。
        :type PathPrefix: String
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: String
        :param Filter: 
        :type PathPrefix: Filter
        """
        self.RepoName = None
        self.MaxResults = None
        self.Marker = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class DeleteTagsRequest(AbstractModel):
    """DeleteTags请求参数结构体
    """

    def __init__(self):
        r"""删除镜像tag
        :param RepoName: 镜像仓库名称
        :type PathPrefix: String
        :param Tag: 指定的镜像版本
        :type PathPrefix: Filter
        """
        self.RepoName = None
        self.Tag = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("Tag"):
            self.Tag = params.get("Tag")


class AddFavorRequest(AbstractModel):
    """AddFavor请求参数结构体
    """

    def __init__(self):
        r"""添加收藏
        :param RepoName: 命名空间/仓库名称，如“mynamespace/myrepo”
        :type PathPrefix: String
        :param RepoType: 收藏的镜像仓库类型，有效值：KSYUN HUB ：收藏的金山云镜像，DOCKER HUB：收藏的docker hub官方镜像
        :type PathPrefix: String
        """
        self.RepoName = None
        self.RepoType = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")
        if params.get("RepoType"):
            self.RepoType = params.get("RepoType")


class DeleteFavorRequest(AbstractModel):
    """DeleteFavor请求参数结构体
    """

    def __init__(self):
        r"""取消收藏
        :param RepoName: 命名空间/仓库名称，如“mynamespace/myrepo”
        :type PathPrefix: String
        """
        self.RepoName = None

    def _deserialize(self, params):
        if params.get("RepoName"):
            self.RepoName = params.get("RepoName")


class GetFavorRequest(AbstractModel):
    """GetFavor请求参数结构体
    """

    def __init__(self):
        r"""查询镜像收藏列表
        :param MaxResults: 单次调用所返回的最大实例数目，默认20，最大99。
        :type PathPrefix: Int
        :param Marker: 分页标识，单次调用未返回全部实例时，标记下次调用的返回值的起点，默认值是0。
        :type PathPrefix: Int
        :param Keyword: 查询关键字
        :type PathPrefix: String
        """
        self.MaxResults = None
        self.Marker = None
        self.Keyword = None

    def _deserialize(self, params):
        if params.get("MaxResults"):
            self.MaxResults = params.get("MaxResults")
        if params.get("Marker"):
            self.Marker = params.get("Marker")
        if params.get("Keyword"):
            self.Keyword = params.get("Keyword")


class RegisterRepositoryAccountRequest(AbstractModel):
    """RegisterRepositoryAccount请求参数结构体
    """

    def __init__(self):
        r"""注册镜像仓库
        :param Password: 镜像仓库密码，限制：8-32个字符，必须包含字母、数字和特殊字符中至少两项，支持英文特殊字符!$%()*+,-./:;<=>?@[]^_`{&#124;}~
        :type PathPrefix: String
        """
        self.Password = None

    def _deserialize(self, params):
        if params.get("Password"):
            self.Password = params.get("Password")


class ModifyPasswordRequest(AbstractModel):
    """ModifyPassword请求参数结构体
    """

    def __init__(self):
        r"""修改镜像仓库密码
        :param Password: 镜像仓库密码，限制：8-32个字符，必须包含字母、数字和特殊字符中至少两项，支持英文特殊字符!$%()*+,-./:;<=>?@[]^_`{
        :type PathPrefix: String
        """
        self.Password = None

    def _deserialize(self, params):
        if params.get("Password"):
            self.Password = params.get("Password")


class DeleteRepoNamespaceRequest(AbstractModel):
    """DeleteRepoNamespace请求参数结构体
    """

    def __init__(self):
        r"""删除命名空间
        :param Namespace: 命名空间名称
        :type PathPrefix: String
        """
        self.Namespace = None

    def _deserialize(self, params):
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
