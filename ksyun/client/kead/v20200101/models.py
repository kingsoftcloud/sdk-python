from ksyun.common.abstract_model import AbstractModel

class DescribeBlockIpRequest(AbstractModel):
    """DescribeBlockIp请求参数结构体
    """

    def __init__(self):
        r"""查询封禁IP
        :param SearchStr: 单个IP或所属实例名称
        :type PathPrefix: String
        :param Status: 封禁状态，有效值

- block 封禁中
- unblock 已解封
        :type PathPrefix: String
        :param InstanceType: 资源类型，有效值

- vpc_vm 云服务器
- lb 负载均衡
- other 其他
        :type PathPrefix: String
        :param RegionCode: 数据中心代码，可选值

- cn-beijing-6 华北1（北京）
- cn-shanghai-2 华东1（上海）
- cn-guangzhou-1 华南1（广州）
- cn-hongkong-2 香港  
- ap-singapore-1 新加坡
        :type PathPrefix: String
        :param StartTime: 查询起始时间，示例：2021-08-01 11:21:51
        :type PathPrefix: String
        :param endTime: 查询结束时间，示例：2021-08-01 11:21:51
        :type PathPrefix: String
        """
        self.SearchStr = None
        self.Status = None
        self.InstanceType = None
        self.RegionCode = None
        self.StartTime = None
        self.endTime = None

    def _deserialize(self, params):
        if params.get("SearchStr"):
            self.SearchStr = params.get("SearchStr")
        if params.get("Status"):
            self.Status = params.get("Status")
        if params.get("InstanceType"):
            self.InstanceType = params.get("InstanceType")
        if params.get("RegionCode"):
            self.RegionCode = params.get("RegionCode")
        if params.get("StartTime"):
            self.StartTime = params.get("StartTime")
        if params.get("endTime"):
            self.endTime = params.get("endTime")


