from ksyun.common.abstract_model import AbstractModel


class CreateCacheClusterRequest(AbstractModel):
    """CreateCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""创建缓存服务
        :param Name: 缓存服务名称             	 支持6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线和中划线
        :type PathPrefix: String
        :param Capacity: 缓存容量大小，以GB为单位 	 缓存资源为单主从模式时，可选值为：{1, 2, 4, 8, 16, 32, 64}；
        :type PathPrefix: String
        :param SlaveNum: 从节点个数据             	 范围是 0~7个， 默认值为0
        :type PathPrefix: String
        :param NetType: 网络类型                 	 固定值2， 目前只支持创建VPC实例。
        :type PathPrefix: String
        :param VpcId: 虚拟专用网络             	 VPC网络ID，可在网络控制台获取。
        :type PathPrefix: String
        :param VnetId: 终端子网id               	 终端子网ID，可在网络控制台获取（注意类型必须为终端子网）。
        :type PathPrefix: String
        :param BillType: 计费方式：默认为1        	 1:包年包月 5:按天先结
        :type PathPrefix: String
        :param Duration: 时长，默认值：1(单位:月) 	 billType=1(包年包月)则必填，最大支持范围是(1 ~36月)，开发自定
        :type PathPrefix: String
        :param DurationUnit: 时长单位                 	 默认值：月
        :type PathPrefix: String
        :param PassWord: 密码                     	 规则：(?=.*[A-Z]+.*)(?=.*[a-z]+.*)(?=.*[\d]+.*)([A-Za-z\d!@#$%^&*()_+=-]{8,30})
        :type PathPrefix: String
        :param IamProjectId: 项目ID                   	 默认为0：默认项目
        :type PathPrefix: String
        :param Engine: 缓存服务引擎             	 取固定值：memcached
        :type PathPrefix: String
        """
        self.Name = None
        self.Capacity = None
        self.SlaveNum = None
        self.NetType = None
        self.VpcId = None
        self.VnetId = None
        self.BillType = None
        self.Duration = None
        self.DurationUnit = None
        self.PassWord = None
        self.IamProjectId = None
        self.Engine = None

    def _deserialize(self, params):
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Capacity"):
            self.Capacity = params.get("Capacity")
        if params.get("SlaveNum"):
            self.SlaveNum = params.get("SlaveNum")
        if params.get("NetType"):
            self.NetType = params.get("NetType")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("DurationUnit"):
            self.DurationUnit = params.get("DurationUnit")
        if params.get("PassWord"):
            self.PassWord = params.get("PassWord")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")
        if params.get("Engine"):
            self.Engine = params.get("Engine")


class DeleteCacheClusterRequest(AbstractModel):
    """DeleteCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""删除缓存服务
        """

    def _deserialize(self, params):
        return


class ResizeCacheClusterRequest(AbstractModel):
    """ResizeCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""更配缓存服务
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param Capacity: 更配目标大小，以GB为单位 	 缓存资源为单主从模式时，可选值为：{1, 2, 4, 8, 16, 32, 64}；
        :type PathPrefix: String
        :param Engine: 缓存服务引擎             	 取固定值：memcached
        :type PathPrefix: String
        """
        self.CacheId = None
        self.Capacity = None
        self.Engine = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Capacity"):
            self.Capacity = params.get("Capacity")
        if params.get("Engine"):
            self.Engine = params.get("Engine")


class DescribeCacheClustersRequest(AbstractModel):
    """DescribeCacheClusters请求参数结构体
    """

    def __init__(self):
        r"""查询缓存服务列表
        :param Engine: 服务引擎                              	 取固定值memcached
        :type PathPrefix: String
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param Name: 缓存服务名称
        :type PathPrefix: String
        :param Vip: 缓存服务IP地址
        :type PathPrefix: String
        :param VpcId: 虚拟专用网络ID                         	 只适用于VPC网络下的缓存服务
        :type PathPrefix: String
        :param VnetId: 虚拟专用网路EndpointID，或vpclbID      	 只适用于VPC网络下的缓存服务
        :type PathPrefix: String
        :param Offset: 查询数据的起始位置                     	 默认为0
        :type PathPrefix: String
        :param Limit: 需要从起始位置开始查询的缓存服务的个数 	 取值范围为[1~100]，默认为10
        :type PathPrefix: String
        :param OrderBy: 排序字段                               	 可传值为{name,asc，name,desc，created,asc，created,desc}，默认按照创建时间降序，只有排序字段时，默认按照升序排列
        :type PathPrefix: String
        :param IamProjectId: 项目ID                                 	 默认是0(默认项目),如果查询全部项目，需要传入所有的项目ID，‘,’隔开
        :type PathPrefix: String
        """
        self.Engine = None
        self.CacheId = None
        self.Name = None
        self.Vip = None
        self.VpcId = None
        self.VnetId = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.IamProjectId = None

    def _deserialize(self, params):
        if params.get("Engine"):
            self.Engine = params.get("Engine")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Vip"):
            self.Vip = params.get("Vip")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("OrderBy"):
            self.OrderBy = params.get("OrderBy")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")


class DescribeCacheClusterRequest(AbstractModel):
    """DescribeCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""查询缓存服务详情
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param Engine: 缓存服务引擎 	 取固定值： memcached
        :type PathPrefix: String
        """
        self.CacheId = None
        self.Engine = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Engine"):
            self.Engine = params.get("Engine")


class FlushCacheClusterRequest(AbstractModel):
    """FlushCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""清空缓存服务
        """

    def _deserialize(self, params):
        return


class RenameCacheClusterRequest(AbstractModel):
    """RenameCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""重命名缓存服务
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param Name: 缓存服务名称
        :type PathPrefix: String
        :param Engine: 缓存服务引擎 	 取固定值：memcached
        :type PathPrefix: String
        """
        self.CacheId = None
        self.Name = None
        self.Engine = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Engine"):
            self.Engine = params.get("Engine")


class UpdatePasswordRequest(AbstractModel):
    """UpdatePassword请求参数结构体
    """

    def __init__(self):
        r"""修改缓存服务密码
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param Password: 缓存服务密码 	 密码规则：(?=.*[A-Z]+.*)(?=.*[a-z]+.*)(?=.*[\\d]+.*)([A-Za-z\\d!@#$%^&*()_+=-]{8,30})，不传则设置为没有密码
        :type PathPrefix: String
        :param Engine: 缓存服务引擎 	 取固定值：memcached
        :type PathPrefix: String
        """
        self.CacheId = None
        self.Password = None
        self.Engine = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("Engine"):
            self.Engine = params.get("Engine")


class DescribeCacheSecurityRulesRequest(AbstractModel):
    """DescribeCacheSecurityRules请求参数结构体
    """

    def __init__(self):
        r"""缓存服务白名单(安全规则信息)
        """

    def _deserialize(self, params):
        return


class DeleteCacheSecurityRuleRequest(AbstractModel):
    """DeleteCacheSecurityRule请求参数结构体
    """

    def __init__(self):
        r"""缓存服务删除安全规则
        """

    def _deserialize(self, params):
        return


class SetCacheSecurityRulesRequest(AbstractModel):
    """SetCacheSecurityRules请求参数结构体
    """

    def __init__(self):
        r"""缓存服务设置安全规则
        """

    def _deserialize(self, params):
        return


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体
    """

    def __init__(self):
        r"""查询机房
        """

    def _deserialize(self, params):
        return


class DescribeAvailabilityZonesRequest(AbstractModel):
    """DescribeAvailabilityZones请求参数结构体
    """

    def __init__(self):
        r"""查询可用区
        """

    def _deserialize(self, params):
        return
