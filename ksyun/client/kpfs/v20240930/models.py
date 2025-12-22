from ksyun.common.abstract_model import AbstractModel

class UpdatePerformanceOnePosixAclRequest(AbstractModel):
    """UpdatePerformanceOnePosixAcl请求参数结构体
    """

    def __init__(self):
        r"""修改访问授权
        :param PosixAclId: 
        :type PathPrefix: String
        :param FileSystemList: 
        :type PathPrefix: Array
        :param Ips: 
        :type PathPrefix: Array
        :param AutoMount: 
        :type PathPrefix: Boolean
        :param Desc: 
        :type PathPrefix: String
        """
        self.PosixAclId = None
        self.FileSystemList = None
        self.Ips = None
        self.AutoMount = None
        self.Desc = None

    def _deserialize(self, params):
        if params.get("PosixAclId"):
            self.PosixAclId = params.get("PosixAclId")
        if params.get("FileSystemList"):
            self.FileSystemList = params.get("FileSystemList")
        if params.get("Ips"):
            self.Ips = params.get("Ips")
        if params.get("AutoMount"):
            self.AutoMount = params.get("AutoMount")
        if params.get("Desc"):
            self.Desc = params.get("Desc")


class DescribePerformanceOnePosixAclListRequest(AbstractModel):
    """DescribePerformanceOnePosixAclList请求参数结构体
    """

    def __init__(self):
        r"""查询访问授权列表
        :param PosixAclId: 
        :type PathPrefix: String
        :param FileSystemId: 
        :type PathPrefix: String
        :param FileSystemName: 
        :type PathPrefix: String
        :param Ip: 
        :type PathPrefix: String
        :param PageNum: 
        :type PathPrefix: Int
        :param PageSize: 
        :type PathPrefix: Int
        """
        self.PosixAclId = None
        self.FileSystemId = None
        self.FileSystemName = None
        self.Ip = None
        self.PageNum = None
        self.PageSize = None

    def _deserialize(self, params):
        if params.get("PosixAclId"):
            self.PosixAclId = params.get("PosixAclId")
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")
        if params.get("FileSystemName"):
            self.FileSystemName = params.get("FileSystemName")
        if params.get("Ip"):
            self.Ip = params.get("Ip")
        if params.get("PageNum"):
            self.PageNum = params.get("PageNum")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")


class ManageDataFlowTaskRequest(AbstractModel):
    """ManageDataFlowTask请求参数结构体
    """

    def __init__(self):
        r"""变更数据流动任务
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class CreateDataFlowStrategyRequest(AbstractModel):
    """CreateDataFlowStrategy请求参数结构体
    """

    def __init__(self):
        r"""创建数据流动策略
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class ModifyDataFlowTaskRequest(AbstractModel):
    """ModifyDataFlowTask请求参数结构体
    """

    def __init__(self):
        r"""变更数据流动任务
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class DescribeDataFlowTaskListRequest(AbstractModel):
    """DescribeDataFlowTaskList请求参数结构体
    """

    def __init__(self):
        r"""创建数据流动策略
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class ActivateDataFlowTaskRequest(AbstractModel):
    """ActivateDataFlowTask请求参数结构体
    """

    def __init__(self):
        r"""启动数据流动导入任务
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class DeleteDataFlowStrategyRequest(AbstractModel):
    """DeleteDataFlowStrategy请求参数结构体
    """

    def __init__(self):
        r"""删除数据流动策略
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


class DescribeDataFlowStrategyListRequest(AbstractModel):
    """DescribeDataFlowStrategyList请求参数结构体
    """

    def __init__(self):
        r"""创建数据流动列表
        :param FileSystemId: 
        :type PathPrefix: String
        """
        self.FileSystemId = None

    def _deserialize(self, params):
        if params.get("FileSystemId"):
            self.FileSystemId = params.get("FileSystemId")


