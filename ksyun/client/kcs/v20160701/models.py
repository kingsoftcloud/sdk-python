from ksyun.common.abstract_model import AbstractModel


class CreateCacheClusterRequest(AbstractModel):
    """CreateCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""创建实例
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param Name: 缓存服务名称 	 支持6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线和中划线
        :type PathPrefix: String
        :param PassWord: 缓存服务密码。可不填（无密码）或者密码须符合以下规则：含大写字母、小写字母、数字、特殊字符（!@#$%^&*()_+=-）4中字符中的3种以上，且长度为8-30个字符。
        :type PathPrefix: String
        :param Mode: 缓存服务的模式。 	 默认：2，取值范围：2：单主从；3：自定义集群。
        :type PathPrefix: Int
        :param Vip: 缓存服务IP       	 默认为：自动分配，填写则为指定IP
        :type PathPrefix: String
        :param Capacity: 缓存服务容量。主从实例（mode为2）默认1G，集群必填。 	 缓存服务内存大小，以GB为单位，参照请见－[缓存服务容量](https://docs.ksyun.com/documents/38475)
        :type PathPrefix: Int
        :param VpcId: 虚拟专用网络 	 VPC网络ID，可在网络控制台获取
        :type PathPrefix: String
        :param VnetId: 终端子网ID   	 终端子网ID，可在网络控制台获取（注意类型必须为终端子网）
        :type PathPrefix: String
        :param BillType: 计费方式     	 默认：1。范围：1包年包月，5按量付费（按日月结），87按量付费。 参照请见－[计费方式](https://docs.ksyun.com/documents/38477)
        :type PathPrefix: Int
        :param Duration: 时长         	 默认：1，BillType=1(包年包月)必填，最大支持范围是(1 ~36月)
        :type PathPrefix: Int
        :param IamProjectId: 项目ID       	 默认为0：默认项目
        :type PathPrefix: String
        :param Protocol: 缓存服务版本 	 集群默认：4.0、单主从默认：4.0，参照请见－[缓存服务版本](https://docs.ksyun.com/documents/38472)
        :type PathPrefix: String
        :param BackupTimezone: 自动备份时间 	 不设置参数代表不开启自动备份，参照请见－[自动备份时间格式](https://docs.ksyun.com/documents/38478)
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID     	 安全组ID，可通过安全组模块的列表查询获取到具体的安全组ID  参见 [查询安全组列表](https://docs.ksyun.com/documents/38503) 。此接口为20年10月新增参数
        :type PathPrefix: String
        :param SlaveNum: 主从实例的只读节点数量 	 默认：0，取值范围：0~7（注意当缓存服务方式：2.单主从时生效）
        :type PathPrefix: Int
        :param SlaveVip: 主从实例的只读节点IP。    	 默认为：自动分配，填写则为指定IP。
（注意当缓存服务mode：2.单主从时生效）
        :type PathPrefix: String
        :param PrepareAzName: 主从实例从节点可用区az。 （注意当缓存服务mode：2.单主从时，且当前Region支持多az生效）
        :type PathPrefix: String
        :param RrAzName: 主从只读实例可用区az。（注意当缓存服务mode：2.单主从时，且当前Region支持多az生效）
        :type PathPrefix: String
        :param ShardNum: 集群分片数量。（注意当缓存服务mode：1. 集群时必填）。
        :type PathPrefix: Int
        :param ShardSize: 集群每个分片内存大小。（注意当缓存服务mode：1. 集群时必填）。
        :type PathPrefix: Int
        :param Separation: 是否开启读写分离。可选范围：0（关闭），1（开启）。默认为0。请注意，目前仅集群实例支持。
        :type PathPrefix: Int
        """
        self.AvailableZone = None
        self.Name = None
        self.PassWord = None
        self.Mode = None
        self.Vip = None
        self.Capacity = None
        self.VpcId = None
        self.VnetId = None
        self.BillType = None
        self.Duration = None
        self.IamProjectId = None
        self.Protocol = None
        self.BackupTimezone = None
        self.SecurityGroupId = None
        self.SlaveNum = None
        self.SlaveVip = None
        self.PrepareAzName = None
        self.RrAzName = None
        self.ShardNum = None
        self.ShardSize = None
        self.Separation = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("PassWord"):
            self.PassWord = params.get("PassWord")
        if params.get("Mode"):
            self.Mode = params.get("Mode")
        if params.get("Vip"):
            self.Vip = params.get("Vip")
        if params.get("Capacity"):
            self.Capacity = params.get("Capacity")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")
        if params.get("VnetId"):
            self.VnetId = params.get("VnetId")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("IamProjectId"):
            self.IamProjectId = params.get("IamProjectId")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("BackupTimezone"):
            self.BackupTimezone = params.get("BackupTimezone")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SlaveNum"):
            self.SlaveNum = params.get("SlaveNum")
        if params.get("SlaveVip"):
            self.SlaveVip = params.get("SlaveVip")
        if params.get("PrepareAzName"):
            self.PrepareAzName = params.get("PrepareAzName")
        if params.get("RrAzName"):
            self.RrAzName = params.get("RrAzName")
        if params.get("ShardNum"):
            self.ShardNum = params.get("ShardNum")
        if params.get("ShardSize"):
            self.ShardSize = params.get("ShardSize")
        if params.get("Separation"):
            self.Separation = params.get("Separation")


class DeleteCacheClusterRequest(AbstractModel):
    """DeleteCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""删除实例
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class DescribeCacheClusterRequest(AbstractModel):
    """DescribeCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""查询实例详情
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param AvailableZone: 默认：对应机房的a区
        :type PathPrefix: String
        """
        self.CacheId = None
        self.AvailableZone = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")


class DescribeCacheClustersRequest(AbstractModel):
    """DescribeCacheClusters请求参数结构体
    """

    def __init__(self):
        r"""查看实例列表
        :param AvailableZone: 实例所属az。AvailableZone不作为实例筛选条件。
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        :param Name: 缓存服务名称。
        :type PathPrefix: String
        :param Vip: 缓存服务IP。
        :type PathPrefix: String
        :param VpcId: 虚拟网络ID。   	 只适用于VPC网络下的缓存服务。
        :type PathPrefix: String
        :param VnetId: 终端子网ID 。  	 只适用于VPC网络下的缓存服务。
        :type PathPrefix: String
        :param Offset: 数据偏移量。   	 默认：0。
        :type PathPrefix: String
        :param Limit: 每页查询数量。     	 默认：10，取值范围为[1~100]。
        :type PathPrefix: String
        :param OrderBy: 排序字段。    	 传值为{name,asc，name,desc，created,asc，created,desc}，默认按照创建时间降序，只有排序字段时，默认按照升序排列。
        :type PathPrefix: String
        :param IamProjectId: 项目ID。       	 默认：查询全部项目。可传入多个的项目ID，以‘,’（逗号）隔开。
        :type PathPrefix: String
        :param FuzzySearch: 模糊条件查询。 	 如：可根据ID，IP，名称进行过滤。
        :type PathPrefix: String
        :param Protocol: 版本号。 	 默认：查询所有，可选版本号：4.0、5.0、6.0。
        :type PathPrefix: String
        :param TagKey: 标签的key，标签名。标签过滤查询（必须同标签值一同传入）。
        :type PathPrefix: String
        :param TagValue: 标签的value，标签值。标签过滤查询（必须同标签名一同传入）。
        :type PathPrefix: String
        :param Mode: 根据实例的部署方式进行筛选。可选：singledatanode（主从实例），cluster（集群实例），enterprise（企业版）。

        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.Name = None
        self.Vip = None
        self.VpcId = None
        self.VnetId = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.IamProjectId = None
        self.FuzzySearch = None
        self.Protocol = None
        self.TagKey = None
        self.TagValue = None
        self.Mode = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
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
        if params.get("FuzzySearch"):
            self.FuzzySearch = params.get("FuzzySearch")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("TagKey"):
            self.TagKey = params.get("TagKey")
        if params.get("TagValue"):
            self.TagValue = params.get("TagValue")
        if params.get("Mode"):
            self.Mode = params.get("Mode")


class FlushCacheClusterRequest(AbstractModel):
    """FlushCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""清空缓存
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        :param DatabaseNo: 指定清除的数据库。若指定多个数据库，用","(逗号)隔开，如：如：DatabaseNo=0,1,2,3,4,5,6,7,8,9,10

        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.DatabaseNo = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("DatabaseNo"):
            self.DatabaseNo = params.get("DatabaseNo")


class RenameCacheClusterRequest(AbstractModel):
    """RenameCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""修改实例名称
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        :param Name: 缓存服务名称。 	 支持6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线和中划线。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.Name = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Name"):
            self.Name = params.get("Name")


class ResizeCacheClusterRequest(AbstractModel):
    """ResizeCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""更配实例
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        :param Capacity: 更配目标容量。 	 缓存资源为单主从模式时，可选值为：{1, 2, 4, 8, 16, 32, 64}。
        :type PathPrefix: Int
        :param ShardSize: 仅集群实例使用。shardSize和shardNum不能同时更配，只能一次更配这两种参数中的一种。范围可参照创建实例的范围。自定义集群暂不支持降配。
        :type PathPrefix: Int
        :param ShardNum: 仅集群实例使用。shardSize和shardNum不能同时更配，只能一次更配这两种参数中的一种。范围可参照创建实例的范围。自定义集群暂不支持降配。
        :type PathPrefix: Int
        """
        self.AvailableZone = None
        self.CacheId = None
        self.Capacity = None
        self.ShardSize = None
        self.ShardNum = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Capacity"):
            self.Capacity = params.get("Capacity")
        if params.get("ShardSize"):
            self.ShardSize = params.get("ShardSize")
        if params.get("ShardNum"):
            self.ShardNum = params.get("ShardNum")


class DescribeCacheParametersRequest(AbstractModel):
    """DescribeCacheParameters请求参数结构体
    """

    def __init__(self):
        r"""查询缓存服务参数
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class SetCacheParametersRequest(AbstractModel):
    """SetCacheParameters请求参数结构体
    """

    def __init__(self):
        r"""设置缓存服务参数
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID 	 缓存服务ID
        :type PathPrefix: String
        :param Protocol: 参数组版本 	 参数组版本，版本号：4.0，5.0
        :type PathPrefix: String
        :param Parameters.ParameterName: 参数名称   	 N：表示数字，示例（Parameters.ParameterName.1=xx&Parameters.ParameterName.2=yy）参考请见：[参数组参数](https://docs.ksyun.com/documents/38470)(默认不修改)
        :type PathPrefix: Filter
        :param Parameters.ParameterValue: 参数值 N：表示数字，示例（Parameters.ParameterValue.1=xx&Parameters.ParameterValue.2=yy）参考请见：参数组参数(默认不修改)
        :type PathPrefix: Filter
        :param ResetAllParameters: 是否为重置参数 	 默认：false；重置实例参数时修改为true，参数值/参数名不传
        :type PathPrefix: Boolean
        """
        self.AvailableZone = None
        self.CacheId = None
        self.Protocol = None
        self.Parameters.ParameterName = None
        self.Parameters.ParameterValue = None
        self.ResetAllParameters = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Protocol"):
            self.Protocol = params.get("Protocol")
        if params.get("Parameters.ParameterName"):
            self.Parameters.ParameterName = params.get("Parameters.ParameterName")
        if params.get("Parameters.ParameterValue"):
            self.Parameters.ParameterValue = params.get("Parameters.ParameterValue")
        if params.get("ResetAllParameters"):
            self.ResetAllParameters = params.get("ResetAllParameters")


class DescribeCacheDefaultParametersRequest(AbstractModel):
    """DescribeCacheDefaultParameters请求参数结构体
    """

    def __init__(self):
        r"""DescribeCacheDefaultParameters
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param ParamVersion: 参数组版本 ，默认是2.8版本。 可选2.8，3.0，4.0，5.0，6.0
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.ParamVersion = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("ParamVersion"):
            self.ParamVersion = params.get("ParamVersion")


class SetCacheParameterGroupRequest(AbstractModel):
    """SetCacheParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""应用参数组，将参数组中所有的参数的当前值应用到指定的缓存服务对应参数上
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheParameterGroupId: 参数组ID。
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheParameterGroupId = None
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheParameterGroupId"):
            self.CacheParameterGroupId = params.get("CacheParameterGroupId")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class CreateCacheParameterGroupRequest(AbstractModel):
    """CreateCacheParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""创建参数组
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param Name: 参数组名称。 	 支持1-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线和中划线。
        :type PathPrefix: String
        :param Description: 参数组描述。
        :type PathPrefix: String
        :param ParamVersion: 参数组版本。
        :type PathPrefix: String
        :param Parameters: 参数名称   	 N：表示数字，示例（Parameters.ParameterName.1=xx&Parameters.ParameterName.2=yy）参考请见-[参数组参数](https://docs.ksyun.com/documents/38470)
        :type PathPrefix: Filter
        """
        self.AvailableZone = None
        self.Name = None
        self.Description = None
        self.ParamVersion = None
        self.Parameters = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ParamVersion"):
            self.ParamVersion = params.get("ParamVersion")
        if params.get("Parameters"):
            self.Parameters = params.get("Parameters")


class DeleteCacheParameterGroupRequest(AbstractModel):
    """DeleteCacheParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""删除参数组
        :param AvailableZone: 可用区   	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheParameterGroupId: 参数组ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheParameterGroupId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheParameterGroupId"):
            self.CacheParameterGroupId = params.get("CacheParameterGroupId")


class ModifyCacheParameterGroupRequest(AbstractModel):
    """ModifyCacheParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""修改参数组
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param Name: 参数组名称 	 支持1-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线和中划线
        :type PathPrefix: String
        :param Description: 参数组描述 	 参数组描述
        :type PathPrefix: String
        :param ParamVersion: 参数组版本。 必须和修改前保持一致
        :type PathPrefix: String
        :param CacheParameterGroupId: 参数组ID   	 参数组ID
        :type PathPrefix: String
        :param Parameters: 参数名称   	 N：表示数字，示例（Parameters.ParameterName.1=xx&Parameters.ParameterName.2=yy）参考请见 - [参数组参数](https://docs.ksyun.com/documents/38470)
        :type PathPrefix: Filter
        """
        self.AvailableZone = None
        self.Name = None
        self.Description = None
        self.ParamVersion = None
        self.CacheParameterGroupId = None
        self.Parameters = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("ParamVersion"):
            self.ParamVersion = params.get("ParamVersion")
        if params.get("CacheParameterGroupId"):
            self.CacheParameterGroupId = params.get("CacheParameterGroupId")
        if params.get("Parameters"):
            self.Parameters = params.get("Parameters")


class DescribeCacheParameterGroupsRequest(AbstractModel):
    """DescribeCacheParameterGroups请求参数结构体
    """

    def __init__(self):
        r"""根据参数组的名称以及ID进行参数组查询
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param Name: 参数组名称
        :type PathPrefix: String
        :param CacheParameterGroupId: 参数组ID 	 参数组ID
        :type PathPrefix: String
        :param ParamVersion: 参数组版本 	 参数组版本
        :type PathPrefix: String
        :param Offset: 数据偏移量 	 默认：0
        :type PathPrefix: String
        :param Limit: 每页数量   	 默认：10，取值范围为[1~10000]
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.Name = None
        self.CacheParameterGroupId = None
        self.ParamVersion = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("CacheParameterGroupId"):
            self.CacheParameterGroupId = params.get("CacheParameterGroupId")
        if params.get("ParamVersion"):
            self.ParamVersion = params.get("ParamVersion")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class DescribeCacheParameterGroupRequest(AbstractModel):
    """DescribeCacheParameterGroup请求参数结构体
    """

    def __init__(self):
        r"""查询参数组详情
        :param AvailableZone: 可用区   	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheParameterGroupId: 参数组ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheParameterGroupId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheParameterGroupId"):
            self.CacheParameterGroupId = params.get("CacheParameterGroupId")


class SetTimingSnapshotRequest(AbstractModel):
    """SetTimingSnapshot请求参数结构体
    """

    def __init__(self):
        r"""设置备份时间
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param TimingSwitch: 备份开关   	 On/Off：开/关
        :type PathPrefix: String
        :param CacheId: 缓存服务ID 	 缓存服务ID
        :type PathPrefix: String
        :param Timezone: 时段       	 TimingSwitch=On时，该项必填，参照请见－[自动备份的时间格式](https://docs.ksyun.com/documents/38478)
        :type PathPrefix: String
        :param Bigkey: 是否进行大key分析，默认false
        :type PathPrefix: Boolean
        """
        self.AvailableZone = None
        self.TimingSwitch = None
        self.CacheId = None
        self.Timezone = None
        self.Bigkey = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("TimingSwitch"):
            self.TimingSwitch = params.get("TimingSwitch")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Timezone"):
            self.Timezone = params.get("Timezone")
        if params.get("Bigkey"):
            self.Bigkey = params.get("Bigkey")


class DeleteSnapshotRequest(AbstractModel):
    """DeleteSnapshot请求参数结构体
    """

    def __init__(self):
        r"""删除备份
        :param AvailableZone: 可用区   	 默认：对应机房的a区
        :type PathPrefix: String
        :param SnapshotId: 备份ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class RenameSnapshotRequest(AbstractModel):
    """RenameSnapshot请求参数结构体
    """

    def __init__(self):
        r"""重命名备份
        :param AvailableZone: 可用区   	 默认：对应机房的a区
        :type PathPrefix: String
        :param Name: 备份名称。 	 支持6-64个中文或者英文字符，包括汉字，大小写字母，数字，下划线和中划线。
        :type PathPrefix: String
        :param SnapshotId: 备份ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.Name = None
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class RestoreSnapshotRequest(AbstractModel):
    """RestoreSnapshot请求参数结构体
    """

    def __init__(self):
        r"""恢复备份
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param Cacheld: 缓存服务ID。
        :type PathPrefix: String
        :param Type: 备份类型     	 Default / BaseKS3
        :type PathPrefix: String
        :param SnapshotId: 备份ID。       	 Type值为Default时，必选项。
        :type PathPrefix: String
        :param BucketName: 存储空间名称。 	 Type值为BaseKS3时，必选项。
        :type PathPrefix: String
        :param ObjectName: 文件名称。     	 Type值为BaseKS3时，必选项
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.Cacheld = None
        self.Type = None
        self.SnapshotId = None
        self.BucketName = None
        self.ObjectName = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Cacheld"):
            self.Cacheld = params.get("Cacheld")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")
        if params.get("BucketName"):
            self.BucketName = params.get("BucketName")
        if params.get("ObjectName"):
            self.ObjectName = params.get("ObjectName")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots请求参数结构体
    """

    def __init__(self):
        r"""获取备份列表
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class DownloadSnapshotRequest(AbstractModel):
    """DownloadSnapshot请求参数结构体
    """

    def __init__(self):
        r"""下载备份
        :param AvailableZone: 可用区   	 默认：对应机房的a区
        :type PathPrefix: String
        :param SnapshotId: 备份ID 
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class ExportSnapshotRequest(AbstractModel):
    """ExportSnapshot请求参数结构体
    """

    def __init__(self):
        r"""ExportSnapshot
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param SnapshotId: 备份ID 
        :type PathPrefix: String
        :param BucketName: 存储空间名称 
        :type PathPrefix: String
        :param ObjectName: 文件名称 
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.SnapshotId = None
        self.BucketName = None
        self.ObjectName = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")
        if params.get("BucketName"):
            self.BucketName = params.get("BucketName")
        if params.get("ObjectName"):
            self.ObjectName = params.get("ObjectName")


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


class DescribeCacheByRoleRequest(AbstractModel):
    """DescribeCacheByRole请求参数结构体
    """

    def __init__(self):
        r"""通过角色查询缓存服务列表接口
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID 
        :type PathPrefix: String
        :param Proxy: 节点角色。默认查询全部。可选：MASTER、SLAVE、READONLY、PROXY
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.Proxy = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Proxy"):
            self.Proxy = params.get("Proxy")


class StatisticDBInstancesRequest(AbstractModel):
    """StatisticDBInstances请求参数结构体
    """

    def __init__(self):
        r"""概览页统计查询
        """

    def _deserialize(self, params):
        return


class UpdatePasswordRequest(AbstractModel):
    """UpdatePassword请求参数结构体
    """

    def __init__(self):
        r"""修改缓存服务密码
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param Password: 缓存服务密码。可不填（无密码）或者密码须符合以下规则：含大写字母、小写字母、数字、特殊字符（!@#$%^&*()_+=-）4中字符中的3种以上，且长度为8-30个字符。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.Password = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Password"):
            self.Password = params.get("Password")


class RestartCacheClusterRequest(AbstractModel):
    """RestartCacheCluster请求参数结构体
    """

    def __init__(self):
        r"""实例重启
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID 
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class AllocateEipRequest(AbstractModel):
    """AllocateEip请求参数结构体
    """

    def __init__(self):
        r"""申请EIP
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        :param InsType: 实例类型。 	 1:master 仅给主实例上绑定</br>    2:readonly 仅给只读上绑定</br>3:all 给两者上绑定</br>注释：集群版本不需要该参数，主从版需要该参数。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.InsType = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("InsType"):
            self.InsType = params.get("InsType")


class DeallocateEipRequest(AbstractModel):
    """DeallocateEip请求参数结构体
    """

    def __init__(self):
        r"""释放EIP
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID 	 缓存服务ID
        :type PathPrefix: String
        :param InsType: 实例类型   	 1:master 仅给主节点解绑</br>2:readonly 仅给只读节点解绑</br>3:all 给两者都解绑</br>注释：集群版本不需要该参数，主从版需要该参数
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.InsType = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("InsType"):
            self.InsType = params.get("InsType")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体
    """

    def __init__(self):
        r"""安全组-查询实例信息
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param SecurityGroupId: 安全组id
        :type PathPrefix: String
        :param Offset: 数据偏移量 	 默认：0，数据偏移量,
        :type PathPrefix: Int
        :param Limit: 返回结果数量限制
        :type PathPrefix: Int
        :param FilterCache: 参考值：true|false。
<br>FilterCache：true 查询绑定指定安全组的缓存服务列表标识；
<br>FilterCache：false 查询未绑定指定安全组的缓存服务列表标识；
        :type PathPrefix: Boolean
        :param SearchKey: 模糊查找。根据缓存服务名称或者IP进行筛选。

        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.SecurityGroupId = None
        self.Offset = None
        self.Limit = None
        self.FilterCache = None
        self.SearchKey = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("FilterCache"):
            self.FilterCache = params.get("FilterCache")
        if params.get("SearchKey"):
            self.SearchKey = params.get("SearchKey")


class DeleteSecurityGroupRuleRequest(AbstractModel):
    """DeleteSecurityGroupRule请求参数结构体
    """

    def __init__(self):
        r"""删除安全组规则
        :param AvailableZone: 可用区			默认：对应机房的a区
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID	安全组ID
        :type PathPrefix: String
        :param SecurityGroupRuleId: 安全组规则ID		N：代表数字，示例（SecurityGroupRuleId.1=xxx&SecurityGroupRuleId.2=yyy）
        :type PathPrefix: Filter
        """
        self.AvailableZone = None
        self.SecurityGroupId = None
        self.SecurityGroupRuleId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupRuleId"):
            self.SecurityGroupRuleId = params.get("SecurityGroupRuleId")


class CreateSecurityGroupRuleRequest(AbstractModel):
    """CreateSecurityGroupRule请求参数结构体
    """

    def __init__(self):
        r"""创建安全组规则
        :param AvailableZone: 可用区   	 默认：对应机房的a区
        :type PathPrefix: String
        :param Cidrs: IP规则   	 N：代表数字，示例（Cidrs.1=127.0.0.1/32&Cidrs.2=0.0.0.0/32）
        :type PathPrefix: Filter
        :param SecurityGroupId: 安全组ID 
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.Cidrs = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Cidrs"):
            self.Cidrs = params.get("Cidrs")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class DeallocateSecurityGroupRequest(AbstractModel):
    """DeallocateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""解绑安全组
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID 	 N：代表数字，示例（CacheId.1=xxx&CacheId.2=yyy）
        :type PathPrefix: Filter
        :param SecurityGroupId: 安全组ID   	 安全组ID
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class AllocateSecurityGroupRequest(AbstractModel):
    """AllocateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""绑定安全组
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID 	 N：代表数字，示例（CacheId.1=xxxx&CacheId.2=yyyy），每个缓存服务都会绑定SecurityGroupId.N
        :type PathPrefix: Filter
        :param SecurityGroupId: 安全组ID   	 N：代表数字，示例（SecurityGroupId.1=xxxx&SecurityGroupId.2=yyyy）
        :type PathPrefix: Filter
        """
        self.AvailableZone = None
        self.CacheId = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""查询安全组明细
        :param AvailableZone: 可用区			默认：对应机房的a区
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID	安全组规则ID
        :type PathPrefix: String
        :param SearchKey: 查询条件		根据IP进行过滤
        :type PathPrefix: String
        :param Offset: 数据偏移量	默认：0
        :type PathPrefix: String
        :param Limit: 每页最大数量		默认：1000，最大值1000
        :type PathPrefix: Int
        """
        self.AvailableZone = None
        self.SecurityGroupId = None
        self.SearchKey = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SearchKey"):
            self.SearchKey = params.get("SearchKey")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups请求参数结构体
    """

    def __init__(self):
        r"""查询安全组列表
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param Offset: 数据偏移量 	 默认：0，数据偏移量,
        :type PathPrefix: String
        :param Limit: 每页数据量
        :type PathPrefix: Int
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param FilterCache: 参考值：true|false

如果传入CacheId
FilterCache：true 查询包含缓存服务ID的安全规则；
FilterCache：false 查询不包含缓存服务ID的安全规则；

如果CacheId为空
FilterCache参数无效
        :type PathPrefix: Boolean
        :param SearchKey: 根据名称或者备注进行筛选
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.Offset = None
        self.Limit = None
        self.CacheId = None
        self.FilterCache = None
        self.SearchKey = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("FilterCache"):
            self.FilterCache = params.get("FilterCache")
        if params.get("SearchKey"):
            self.SearchKey = params.get("SearchKey")


class ModifySecurityGroupRequest(AbstractModel):
    """ModifySecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""修改安全组
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param Name: 安全组名称 	 安全组名称支持1-64个字符，中文，字母，数字，中划线，下划线；
        :type PathPrefix: String
        :param Description: 安全组描述 	 安全组描述支持1-64个字符，中文，字母，数字，中划线，下划线；
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.Name = None
        self.Description = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""删除安全组
        :param AvailableZone: 可用区   	 默认：对应机房的a区
        :type PathPrefix: String
        :param SecurityGroupId: 安全组ID 	 N：代表数字，示例(SecurityGroupId.1=xxxx&SecurityGroupId.2=yyyyy)
        :type PathPrefix: Filter
        """
        self.AvailableZone = None
        self.SecurityGroupId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("SecurityGroupId"):
            self.SecurityGroupId = params.get("SecurityGroupId")


class CloneSecurityGroupRequest(AbstractModel):
    """CloneSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""克隆安全组
        :param AvailableZone: 可用区。     	 默认：对应机房的a区</br>注意：未指定和源安全组相同可用区，则默认克隆至机房a区。
        :type PathPrefix: String
        :param Name: 安全组名称。 	 安全组名称支持1-64个字符，中文，字母，数字，中划线，下划线。
        :type PathPrefix: String
        :param Description: 安全组描述。	 安全组描述支持1-64个字符，中文，字母，数字，中划线，下划线。
        :type PathPrefix: String
        :param SrcSecurityGroupId: 源安全组ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.Name = None
        self.Description = None
        self.SrcSecurityGroupId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("SrcSecurityGroupId"):
            self.SrcSecurityGroupId = params.get("SrcSecurityGroupId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体
    """

    def __init__(self):
        r"""创建安全组
        :param AvailableZone: 可用区     	 默认：对应机房的a区
        :type PathPrefix: String
        :param Name: 安全组名称。 	 安全组名称支持1-64个字符，中文，字母，数字，中划线，下划线。
        :type PathPrefix: String
        :param Description: 安全组描述。 	 安全组描述支持1-64个字符，中文，字母，数字，中划线，下划线。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.Name = None
        self.Description = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Description"):
            self.Description = params.get("Description")


class DescribeHotKeysRequest(AbstractModel):
    """DescribeHotKeys请求参数结构体
    """

    def __init__(self):
        r"""查询热key列表
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID   	 缓存服务ID
        :type PathPrefix: String
        :param Limit: 偏移量       	 默认：10
        :type PathPrefix: Int
        :param Offset: 每页数量     	 默认：0
        :type PathPrefix: Int
        :param SortKey: 排序字段名		 count
        :type PathPrefix: String
        :param SortDir: 排序方式		 asc,desc
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.Limit = None
        self.Offset = None
        self.SortKey = None
        self.SortDir = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("Limit"):
            self.Limit = params.get("Limit")
        if params.get("Offset"):
            self.Offset = params.get("Offset")
        if params.get("SortKey"):
            self.SortKey = params.get("SortKey")
        if params.get("SortDir"):
            self.SortDir = params.get("SortDir")


class AnalyzeHotKeysRequest(AbstractModel):
    """AnalyzeHotKeys请求参数结构体
    """

    def __init__(self):
        r"""热key分析按钮
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class CloseDirectAccessToClusterRequest(AbstractModel):
    """CloseDirectAccessToCluster请求参数结构体
    """

    def __init__(self):
        r"""cluster关闭直连
        :param AvailableZone: 可用区       	 默认：对应机房的a区
        :type PathPrefix: String
        :param CacheId: 缓存服务ID。
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class OpenDirectAccessToClusterRequest(AbstractModel):
    """OpenDirectAccessToCluster请求参数结构体
    """

    def __init__(self):
        r"""cluster开启直连
        :param AvailableZone: 可用区。默认为当前region的a区。
        :type PathPrefix: String
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param SubnetId: 终端网络id
        :type PathPrefix: String
        :param VpcId: 虚拟网络VPC id
        :type PathPrefix: String
        """
        self.AvailableZone = None
        self.CacheId = None
        self.SubnetId = None
        self.VpcId = None

    def _deserialize(self, params):
        if params.get("AvailableZone"):
            self.AvailableZone = params.get("AvailableZone")
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("SubnetId"):
            self.SubnetId = params.get("SubnetId")
        if params.get("VpcId"):
            self.VpcId = params.get("VpcId")


class DescribeParentBackUpsSnapshotsRequest(AbstractModel):
    """DescribeParentBackUpsSnapshots请求参数结构体
    """

    def __init__(self):
        r"""redis集群备份数据父列表数据
        :param CacheId: 缓存服务ID		缓存服务ID
        :type PathPrefix: String
        """
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class DescribeBackUpsSnapshotsDetailRequest(AbstractModel):
    """DescribeBackUpsSnapshotsDetail请求参数结构体
    """

    def __init__(self):
        r"""redis集群备份数据子列表数据
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param SnapshotId: 备份ID
        :type PathPrefix: String
        """
        self.CacheId = None
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class DeleteLevelSnapshotsRequest(AbstractModel):
    """DeleteLevelSnapshots请求参数结构体
    """

    def __init__(self):
        r"""redis集群层级备份数据删除
        :param CacheId: 缓存服务ID		缓存服务ID
        :type PathPrefix: String
        :param SnapshotId: 备份ID		备份ID
        :type PathPrefix: String
        """
        self.CacheId = None
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class DownloadLevelSnapshotRequest(AbstractModel):
    """DownloadLevelSnapshot请求参数结构体
    """

    def __init__(self):
        r"""redis集群层次备份数据下载
        :param CacheId: 缓存服务ID
        :type PathPrefix: String
        :param SnapshotId: 备份ID
        :type PathPrefix: String
        """
        self.CacheId = None
        self.SnapshotId = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("SnapshotId"):
            self.SnapshotId = params.get("SnapshotId")


class DescribeBigKeysRequest(AbstractModel):
    """DescribeBigKeys请求参数结构体
    """

    def __init__(self):
        r"""获取大key分析的任务结果列表
        :param CacheId: 缓存服务ID(实例ID)
        :type PathPrefix: String
        """
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class DeleteBigKeysAnalyseResultRequest(AbstractModel):
    """DeleteBigKeysAnalyseResult请求参数结构体
    """

    def __init__(self):
        r"""删除大key分析任务列表数据
        :param CacheId: 缓存服务ID(实例ID)
        :type PathPrefix: String
        :param TaskId: 大key任务ID
        :type PathPrefix: String
        """
        self.CacheId = None
        self.TaskId = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")


class AnalyzeBigKeysRequest(AbstractModel):
    """AnalyzeBigKeys请求参数结构体
    """

    def __init__(self):
        r"""获取大key分析的结果
        :param TaskId: 任务ID	 大key分析任务id
        :type PathPrefix: String
        :param QueryType: 操作类型	 范围（1，2，3，4），1-缓存分析-结果-基础信息；2-缓存分析-结果-top大key占比图；3-缓存分析-结果-详情；4-缓存分析-结果-详情下载
        :type PathPrefix: Int
        """
        self.TaskId = None
        self.QueryType = None

    def _deserialize(self, params):
        if params.get("TaskId"):
            self.TaskId = params.get("TaskId")
        if params.get("QueryType"):
            self.QueryType = params.get("QueryType")


class DescribeCreateSnapshotStatusRequest(AbstractModel):
    """DescribeCreateSnapshotStatus请求参数结构体
    """

    def __init__(self):
        r"""创建备份前的备份状态和大key分析状态查询
        :param CacheId: 缓存服务ID(实例ID)
        :type PathPrefix: String
        """
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class GetDailyAnalyzeSwitchStateRequest(AbstractModel):
    """GetDailyAnalyzeSwitchState请求参数结构体
    """

    def __init__(self):
        r"""慢日志和运行日志分析开关
        :param CacheId: 缓存服务ID（实例ID）
        :type PathPrefix: String
        """
        self.CacheId = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")


class AnalyzeDailyRequest(AbstractModel):
    """AnalyzeDaily请求参数结构体
    """

    def __init__(self):
        r"""运行日志分析
        :param CacheId: 缓存服务ID（实例ID）
        :type PathPrefix: String
        :param StartQueryTime: 运行日志采集开始时间      	 yyyy-MM-dd HH:mm:ss格式
        :type PathPrefix: String
        :param EndQueryTime: 运行日志采集结束时间      	 yyyy-MM-dd HH:mm:ss格式
        :type PathPrefix: String
        :param PageNum: 记录开始偏移量  	 位移量（查询数据的开始位置，默认为1）
        :type PathPrefix: String
        :param PageSize: 每页记录大小     	 每页记录大小, 默认10
        :type PathPrefix: String
        :param ShardId: 实例节点ID   	 实例为集群架构可选填写，加上查询实例下节点的日志，不传默认查询全部
        :type PathPrefix: String
        :param OperationType: 操作类型   	 筛选不同操作类型的日志数据，如LATENCY GET STATS ALL 等
        :type PathPrefix: String
        """
        self.CacheId = None
        self.StartQueryTime = None
        self.EndQueryTime = None
        self.PageNum = None
        self.PageSize = None
        self.ShardId = None
        self.OperationType = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("StartQueryTime"):
            self.StartQueryTime = params.get("StartQueryTime")
        if params.get("EndQueryTime"):
            self.EndQueryTime = params.get("EndQueryTime")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("ShardId"):
            self.ShardId = params.get("ShardId")
        if params.get("OperationType"):
            self.OperationType = params.get("OperationType")


class AnalyzeSlowDailyRequest(AbstractModel):
    """AnalyzeSlowDaily请求参数结构体
    """

    def __init__(self):
        r"""慢日志分析
        :param CacheId: 缓存服务ID（实例ID）
        :type PathPrefix: String
        :param StartQueryTime: 慢日志采集开始时间      	 yyyy-MM-dd HH:mm:ss格式
        :type PathPrefix: String
        :param EndQueryTime: 慢日志采集结束时间      	 yyyy-MM-dd HH:mm:ss格式
        :type PathPrefix: String
        :param PageNum: 记录开始偏移量  	 位移量（查询数据的开始位置，默认为1）
        :type PathPrefix: Int
        :param PageSize: 每页记录大小     	 每页记录大小, 默认10
        :type PathPrefix: Int
        :param ShardId: 实例节点ID   	 实例为集群架构可选填写，加上查询实例下节点的日志，不传默认查询全部。若isProxy为true,则选择Proxy的node
        :type PathPrefix: String
        :param IsProxy: 是否是proxy查询   	 取值：true;false。默认false
        :type PathPrefix: Boolean
        :param OperationType: 操作类型   	 筛选不同操作类型的日志数据，如LATENCY GET STATS ALL 等
        :type PathPrefix: String
        """
        self.CacheId = None
        self.StartQueryTime = None
        self.EndQueryTime = None
        self.PageNum = None
        self.PageSize = None
        self.ShardId = None
        self.IsProxy = None
        self.OperationType = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("StartQueryTime"):
            self.StartQueryTime = params.get("StartQueryTime")
        if params.get("EndQueryTime"):
            self.EndQueryTime = params.get("EndQueryTime")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("ShardId"):
            self.ShardId = params.get("ShardId")
        if params.get("IsProxy"):
            self.IsProxy = params.get("IsProxy")
        if params.get("OperationType"):
            self.OperationType = params.get("OperationType")


class AnalyzeDailySwitchRequest(AbstractModel):
    """AnalyzeDailySwitch请求参数结构体
    """

    def __init__(self):
        r"""AnalyzeDailySwitch
        :param CacheId: 缓存服务ID	 实例ID
        :type PathPrefix: String
        :param ServiceLog: 运行日志开关	 true表示开启，false表示关闭，null保持当前状态不变 默认传null
        :type PathPrefix: Boolean
        :param SlowLog: 慢日志开关	 true表示开启，false表示关闭，null保持当前状态不变 默认传null
        :type PathPrefix: Boolean
        """
        self.CacheId = None
        self.ServiceLog = None
        self.SlowLog = None

    def _deserialize(self, params):
        if params.get("CacheId"):
            self.CacheId = params.get("CacheId")
        if params.get("ServiceLog"):
            self.ServiceLog = params.get("ServiceLog")
        if params.get("SlowLog"):
            self.SlowLog = params.get("SlowLog")
