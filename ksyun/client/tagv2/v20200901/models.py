from ksyun.common.abstract_model import AbstractModel


class CreateTagRequest(AbstractModel):
    """CreateTag请求参数结构体
    """

    def __init__(self):
        r"""创建标签
        :param Key: Key 最多128字符，仅支持中英文字符 数字 + - = . _ : / @，不能以ksc开头
        :type PathPrefix: String
        :param Value: Value最多256字符，仅支持中英文字符 数字 + - = . _ : / @ () {}，不能以ksc开头,多个以","隔开
        :type PathPrefix: String
        """
        self.Key = None
        self.Value = None

    def _deserialize(self, params):
        if params.get("Key"):
            self.Key = params.get("Key")
        if params.get("Value"):
            self.Value = params.get("Value")


class DeleteTagRequest(AbstractModel):
    """DeleteTag请求参数结构体
    """

    def __init__(self):
        r"""删除标签
        :param Tags: Tags
        :type PathPrefix: Array
        """
        self.Tags = None

    def _deserialize(self, params):
        if params.get("Tags"):
            self.Tags = params.get("Tags")


class ListTagsRequest(AbstractModel):
    """ListTags请求参数结构体
    """

    def __init__(self):
        r"""获取标签列表
        :param Page: Page
        :type PathPrefix: Int
        :param PageSize: PageSize
        :type PathPrefix: Int
        :param Key: key
        :type PathPrefix: String
        :param Value: Value
        :type PathPrefix: String
        """
        self.Page = None
        self.PageSize = None
        self.Key = None
        self.Value = None

    def _deserialize(self, params):
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("Key"):
            self.Key = params.get("Key")
        if params.get("Value"):
            self.Value = params.get("Value")


class ListTagKeysRequest(AbstractModel):
    """ListTagKeys请求参数结构体
    """

    def __init__(self):
        r"""获取标签键列表
        :param TagKey: 标签键名称
        :type PathPrefix: String
        :param Page: 页码
        :type PathPrefix: Int
        :param PageSize: 每页数据量
        :type PathPrefix: Int
        """
        self.TagKey = None
        self.Page = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("TagKey"):
            self.TagKey = params.get("TagKey")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class ListTagValuesRequest(AbstractModel):
    """ListTagValues请求参数结构体
    """

    def __init__(self):
        r"""获取标签值列表
        :param TagKeys: 标签键名称，多个用逗号连接
        :type PathPrefix: String
        :param Page: 页码
        :type PathPrefix: Int
        :param PageSize: 页面限制
        :type PathPrefix: Int
        """
        self.TagKeys = None
        self.Page = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("TagKeys"):
            self.TagKeys = params.get("TagKeys")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class ListResourcesRequest(AbstractModel):
    """ListResources请求参数结构体
    """

    def __init__(self):
        r"""获取用户资源列表
        :param ResourceType: 资源类型英文简称
        :type PathPrefix: String
        :param ProjectIds: 项目ID，多个用逗号连接
        :type PathPrefix: String
        :param RegionCodes: regioncode，多个用逗号连接
        :type PathPrefix: String
        :param ResourceUuids: 资源ID，多个用逗号连接
        :type PathPrefix: String
        :param ResourceName: 资源类型名称，详见 [各产品线资源类型名称](https://docs.ksyun.com/documents/43391)
        :type PathPrefix: String
        :param TagFilters: 
        :type PathPrefix: Array
        :param Page: 页码
        :type PathPrefix: Int
        :param PageSize: 分页数
        :type PathPrefix: Int
        """
        self.ResourceType = None
        self.ProjectIds = None
        self.RegionCodes = None
        self.ResourceUuids = None
        self.ResourceName = None
        self.TagFilters = None
        self.Page = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("ResourceType"):
            self.ResourceType = params.get("ResourceType")
        if params.get("ProjectIds"):
            self.ProjectIds = params.get("ProjectIds")
        if params.get("RegionCodes"):
            self.RegionCodes = params.get("RegionCodes")
        if params.get("ResourceUuids"):
            self.ResourceUuids = params.get("ResourceUuids")
        if params.get("ResourceName"):
            self.ResourceName = params.get("ResourceName")
        if params.get("TagFilters"):
            self.TagFilters = params.get("TagFilters")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class ListTagsByResourceIdsRequest(AbstractModel):
    """ListTagsByResourceIds请求参数结构体
    """

    def __init__(self):
        r"""根据资源ID获取资源标签
        :param ResourceType: 资源类型英文简写
        :type PathPrefix: String
        :param ResourceUuids: 资源ID，多个用逗号连接
        :type PathPrefix: String
        """
        self.ResourceType = None
        self.ResourceUuids = None

    def _deserialize(self, params):
        if params.get("ResourceType"):
            self.ResourceType = params.get("ResourceType")
        if params.get("ResourceUuids"):
            self.ResourceUuids = params.get("ResourceUuids")


class ReplaceResourcesTagsRequest(AbstractModel):
    """ReplaceResourcesTags请求参数结构体
    """

    def __init__(self):
        r"""批量替换资源的全部标签
        :param ResourceType: 资源类型英文简写
        :type PathPrefix: String
        :param ReplaceTags: 
        :type PathPrefix: Array
        """
        self.ResourceType = None
        self.ReplaceTags = None

    def _deserialize(self, params):
        if params.get("ResourceType"):
            self.ResourceType = params.get("ResourceType")
        if params.get("ReplaceTags"):
            self.ReplaceTags = params.get("ReplaceTags")


class DetachResourceTagsRequest(AbstractModel):
    """DetachResourceTags请求参数结构体
    """

    def __init__(self):
        r"""解绑资源标签
        :param ResourceType: 资源类型英文简写
        :type PathPrefix: String
        :param ResourceUuid: 资源ID
        :type PathPrefix: String
        :param TagIds: 标签值ID，多个用逗号连接
        :type PathPrefix: String
        """
        self.ResourceType = None
        self.ResourceUuid = None
        self.TagIds = None

    def _deserialize(self, params):
        if params.get("ResourceType"):
            self.ResourceType = params.get("ResourceType")
        if params.get("ResourceUuid"):
            self.ResourceUuid = params.get("ResourceUuid")
        if params.get("TagIds"):
            self.TagIds = params.get("TagIds")
