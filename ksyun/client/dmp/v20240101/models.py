from ksyun.common.abstract_model import AbstractModel

class DescribeDefaultMonitorItemsRequest(AbstractModel):
    """DescribeDefaultMonitorItems请求参数结构体
    """

    def __init__(self):
        r"""查询支持的监控项
        :param PanelType: 监控大盘类型。可选值为：MySQL，Redis（严格区分大小写）。
        :type PathPrefix: String
        """
        self.PanelType = None

    def _deserialize(self, params):
        if params.get("PanelType"):
            self.PanelType = params.get("PanelType")


class DeleteMonitorPanelRequest(AbstractModel):
    """DeleteMonitorPanel请求参数结构体
    """

    def __init__(self):
        r"""删除监控大盘
        :param PanelId: 监控大盘ID。
        :type PathPrefix: String
        """
        self.PanelId = None

    def _deserialize(self, params):
        if params.get("PanelId"):
            self.PanelId = params.get("PanelId")


class OperateMonitorPanelRequest(AbstractModel):
    """OperateMonitorPanel请求参数结构体
    """

    def __init__(self):
        r"""更新监控大盘
        :param AddInstanceIds: 待加入监控大盘的实例ID列表。
        :type PathPrefix: Array
        :param RemoveInstanceIds: 待从监控大盘删除的实例ID列表。
        :type PathPrefix: Array
        :param AddMonitorItems: 待加入监控大盘的监控项列表。
        :type PathPrefix: Array
        :param RemoveMonitorItems: 待从监控大盘移除的监控项列表。
        :type PathPrefix: Array
        :param PanelId: 监控大盘ID。
        :type PathPrefix: String
        """
        self.AddInstanceIds = None
        self.RemoveInstanceIds = None
        self.AddMonitorItems = None
        self.RemoveMonitorItems = None
        self.PanelId = None

    def _deserialize(self, params):
        if params.get("AddInstanceIds"):
            self.AddInstanceIds = params.get("AddInstanceIds")
        if params.get("RemoveInstanceIds"):
            self.RemoveInstanceIds = params.get("RemoveInstanceIds")
        if params.get("AddMonitorItems"):
            self.AddMonitorItems = params.get("AddMonitorItems")
        if params.get("RemoveMonitorItems"):
            self.RemoveMonitorItems = params.get("RemoveMonitorItems")
        if params.get("PanelId"):
            self.PanelId = params.get("PanelId")


class DescribeMonitorPanelRequest(AbstractModel):
    """DescribeMonitorPanel请求参数结构体
    """

    def __init__(self):
        r"""查询监控大盘详情
        :param PanelId: 监控大盘ID。
        :type PathPrefix: String
        """
        self.PanelId = None

    def _deserialize(self, params):
        if params.get("PanelId"):
            self.PanelId = params.get("PanelId")


class ModifyMonitorPanelInfoRequest(AbstractModel):
    """ModifyMonitorPanelInfo请求参数结构体
    """

    def __init__(self):
        r"""修改监控大盘信息
        :param PanelId: 监控大盘ID。
        :type PathPrefix: String
        :param PanelName: 监控大盘名称。
        :type PathPrefix: String
        """
        self.PanelId = None
        self.PanelName = None

    def _deserialize(self, params):
        if params.get("PanelId"):
            self.PanelId = params.get("PanelId")
        if params.get("PanelName"):
            self.PanelName = params.get("PanelName")


class CreateMonitorPanelRequest(AbstractModel):
    """CreateMonitorPanel请求参数结构体
    """

    def __init__(self):
        r"""创建监控大盘
        :param PanelName: 监控大盘名称。
        :type PathPrefix: String
        :param PanelType: 监控大盘类型。
        :type PathPrefix: String
        """
        self.PanelName = None
        self.PanelType = None

    def _deserialize(self, params):
        if params.get("PanelName"):
            self.PanelName = params.get("PanelName")
        if params.get("PanelType"):
            self.PanelType = params.get("PanelType")


class DeleteBatchInstancesRequest(AbstractModel):
    """DeleteBatchInstances请求参数结构体
    """

    def __init__(self):
        r"""批量删除实例
        :param InstanceIds: 待从KDMP中删除的实例ID列表。
注意：实例从KDMP中删除并不影响实例本身运行。
        :type PathPrefix: Array
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        if params.get("InstanceIds"):
            self.InstanceIds = params.get("InstanceIds")


class InstanceStatisticsRequest(AbstractModel):
    """InstanceStatistics请求参数结构体
    """

    def __init__(self):
        r"""实例资产统计
        """

    def _deserialize(self, params):
        return


class DescribeMonitorPanelListRequest(AbstractModel):
    """DescribeMonitorPanelList请求参数结构体
    """

    def __init__(self):
        r"""查询监控大盘列表
        :param PanelIds: 指定监控大盘ID进行筛选。多个监控大盘ID用“,”隔开。
        :type PathPrefix: String
        :param PanelType: 指定监控大盘类型进行筛选。
        :type PathPrefix: String
        :param Page: 页数，从1开始，默认为1。
        :type PathPrefix: Int
        :param PageSize: 每页最多返回数据条目数。默认为10。
        :type PathPrefix: Int
        """
        self.PanelIds = None
        self.PanelType = None
        self.Page = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("PanelIds"):
            self.PanelIds = params.get("PanelIds")
        if params.get("PanelType"):
            self.PanelType = params.get("PanelType")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体
    """

    def __init__(self):
        r"""查询实例列表
        :param InstanceId: 指定实例ID查询。
        :type PathPrefix: String
        :param DatabaseType: 指定数据库类型进行筛选。
        :type PathPrefix: String
        :param InstanceRegion: 指定实例机房进行筛选。
        :type PathPrefix: String
        :param InstanceName: 指定监控大盘类型查找。
        :type PathPrefix: String
        :param Ip: 指定实例Ip进行查找。
        :type PathPrefix: String
        :param Search: 支持按实例ID，实例名称，Ip地址模糊查找。
        :type PathPrefix: String
        :param Page: 页数，从1开始，默认为1。
        :type PathPrefix: Int
        :param PageSize: 每页返回数据条目数。默认为10。
        :type PathPrefix: Int
        """
        self.InstanceId = None
        self.DatabaseType = None
        self.InstanceRegion = None
        self.InstanceName = None
        self.Ip = None
        self.Search = None
        self.Page = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseType"):
            self.DatabaseType = params.get("DatabaseType")
        if params.get("InstanceRegion"):
            self.InstanceRegion = params.get("InstanceRegion")
        if params.get("InstanceName"):
            self.InstanceName = params.get("InstanceName")
        if params.get("Ip"):
            self.Ip = params.get("Ip")
        if params.get("Search"):
            self.Search = params.get("Search")
        if params.get("Page"):
            self.Page = params.get("Page")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class ImportInstanceToDmpRequest(AbstractModel):
    """ImportInstanceToDmp请求参数结构体
    """

    def __init__(self):
        r"""导入实例至KDMP
        :param InstanceRegion: 
        :type PathPrefix: String
        :param DatabaseType: 
        :type PathPrefix: String
        :param InstanceId: 
        :type PathPrefix: String
        """
        self.InstanceRegion = None
        self.DatabaseType = None
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceRegion"):
            self.InstanceRegion = params.get("InstanceRegion")
        if params.get("DatabaseType"):
            self.DatabaseType = params.get("DatabaseType")
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class DescribeDedicatedClustersRequest(AbstractModel):
    """DescribeDedicatedClusters请求参数结构体
    """

    def __init__(self):
        r"""查询专属集群列表
        """

    def _deserialize(self, params):
        return


class DescribeDedicatedHostsRequest(AbstractModel):
    """DescribeDedicatedHosts请求参数结构体
    """

    def __init__(self):
        r"""查询专属集群主机列表
        """

    def _deserialize(self, params):
        return


class DescribeDatabaseSchemaRequest(AbstractModel):
    """DescribeDatabaseSchema请求参数结构体
    """

    def __init__(self):
        r"""查询数据库模式
        :param DatabaseId: 数据库Id
        :type PathPrefix: Int
        """
        self.DatabaseId = None

    def _deserialize(self, params):
        if params.get("DatabaseId"):
            self.DatabaseId = params.get("DatabaseId")


class DescribeDatabaseListRequest(AbstractModel):
    """DescribeDatabaseList请求参数结构体
    """

    def __init__(self):
        r"""查询数据库列表
        """

    def _deserialize(self, params):
        return


class DescribeHistorySQLRequest(AbstractModel):
    """DescribeHistorySQL请求参数结构体
    """

    def __init__(self):
        r"""查询执行历史SQL
        """

    def _deserialize(self, params):
        return


class StartExecuteSQLRequest(AbstractModel):
    """StartExecuteSQL请求参数结构体
    """

    def __init__(self):
        r"""开始执行sql
        :param DatabaseName: 数据库名称
        :type PathPrefix: String
        :param Statement: SQL语句
        :type PathPrefix: String
        """
        self.DatabaseName = None
        self.Statement = None

    def _deserialize(self, params):
        if params.get("DatabaseName"):
            self.DatabaseName = params.get("DatabaseName")
        if params.get("Statement"):
            self.Statement = params.get("Statement")


class UpdateInstanceDatabaseRequest(AbstractModel):
    """UpdateInstanceDatabase请求参数结构体
    """

    def __init__(self):
        r"""刷新实例数据库信息
        :param InstanceId: 实例Id.
        :type PathPrefix: String
        """
        self.InstanceId = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")


class UpdateDatabaseTableRequest(AbstractModel):
    """UpdateDatabaseTable请求参数结构体
    """

    def __init__(self):
        r"""更新数据库表信息
        :param DatabaseId: 
        :type PathPrefix: String
        """
        self.DatabaseId = None

    def _deserialize(self, params):
        if params.get("DatabaseId"):
            self.DatabaseId = params.get("DatabaseId")


class TestInstanceConnectionRequest(AbstractModel):
    """TestInstanceConnection请求参数结构体
    """

    def __init__(self):
        r"""测试实例连通性
        :param InstanceId: 实例Id.
        :type PathPrefix: String
        :param DatabaseType: 数据库类型
        :type PathPrefix: String
        :param DatabaseVersion: 数据库版本
        :type PathPrefix: String
        :param Username: 用户名
        :type PathPrefix: String
        :param Password: 用户名密码
        :type PathPrefix: String
        :param UseSourceUser: 是否使用加入dmp时的用户名和密码
        :type PathPrefix: Boolean
        """
        self.InstanceId = None
        self.DatabaseType = None
        self.DatabaseVersion = None
        self.Username = None
        self.Password = None
        self.UseSourceUser = None

    def _deserialize(self, params):
        if params.get("InstanceId"):
            self.InstanceId = params.get("InstanceId")
        if params.get("DatabaseType"):
            self.DatabaseType = params.get("DatabaseType")
        if params.get("DatabaseVersion"):
            self.DatabaseVersion = params.get("DatabaseVersion")
        if params.get("Username"):
            self.Username = params.get("Username")
        if params.get("Password"):
            self.Password = params.get("Password")
        if params.get("UseSourceUser"):
            self.UseSourceUser = params.get("UseSourceUser")


