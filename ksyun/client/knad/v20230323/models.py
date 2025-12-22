from ksyun.common.abstract_model import AbstractModel

class CreateKnadRequest(AbstractModel):
    """CreateKnad请求参数结构体
    """

    def __init__(self):
        r"""创建原生高防
        :param ServiceId: 原生高防套餐，即保底防护带宽
        :type PathPrefix: String
        :param KnadName: 原生高防实例名称
        :type PathPrefix: String
        :param Duration: 购买时长，单位月
示例值：当计费类型为包年包月时，有效值1-36；其他计费类型时，强制要求参数值为0
        :type PathPrefix: Int
        :param ProjectId: 实例所属项目ID
示例值：账户有权限的项目ID，0为默认项目
        :type PathPrefix: String
        :param Band: 基础防护能力，与套餐的大小保持一致
示例值：套餐为KNAD_2000G，band值为：2000
        :type PathPrefix: Int
        :param MaxBand: 弹性防护上限，攻击峰值超过保底防护的最大防护能力，取值为：
套餐KNAD_2000G：2000
套餐KNAD_1000G：1000、2000
套餐KNAD_300G：300-1000以100阶梯取值、2000
套餐KNAD_100G：100-1000以100阶梯取值
套餐KNAD_30G：30-100以10阶梯取值、100-600以100阶梯取值
        :type PathPrefix: Int
        :param IpCount: 可防护ip数，取值范围：10-100
        :type PathPrefix: Int
        :param BillType: 计费方式：1 (包年包月)；5(按量付费（按日月结)）
        :type PathPrefix: Int
        :param IdcBand: 清洗后正常业务带宽大小，取值范围：100-15000
        :type PathPrefix: Int
        """
        self.ServiceId = None
        self.KnadName = None
        self.Duration = None
        self.ProjectId = None
        self.Band = None
        self.MaxBand = None
        self.IpCount = None
        self.BillType = None
        self.IdcBand = None

    def _deserialize(self, params):
        if params.get("ServiceId"):
            self.ServiceId = params.get("ServiceId")
        if params.get("KnadName"):
            self.KnadName = params.get("KnadName")
        if params.get("Duration"):
            self.Duration = params.get("Duration")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Band"):
            self.Band = params.get("Band")
        if params.get("MaxBand"):
            self.MaxBand = params.get("MaxBand")
        if params.get("IpCount"):
            self.IpCount = params.get("IpCount")
        if params.get("BillType"):
            self.BillType = params.get("BillType")
        if params.get("IdcBand"):
            self.IdcBand = params.get("IdcBand")


class ModifyKnadRequest(AbstractModel):
    """ModifyKnad请求参数结构体
    """

    def __init__(self):
        r"""调整防护能力
        :param KnadId: 待调整防护能力的实例ID
        :type PathPrefix: String
        :param ServiceId: 目标原生高防套餐，即保底防护带宽
        :type PathPrefix: String
        :param IpCount: 目标可防护ip数，取值范围：10-100
        :type PathPrefix: Int
        :param Band: 基础防护能力，与套餐的大小保持一致
示例值：套餐为KNAD_2000G，band值为：2000
        :type PathPrefix: Int
        :param MaxBand: 弹性防护上限，攻击峰值超过保底防护的最大防护能力（Band不为空时候必传）
取值为：
套餐KNAD_2000G：2000
套餐KNAD_1000G：1000、2000
套餐KNAD_300G：300-1000以100阶梯取值、2000
套餐KNAD_100G：100-1000以100阶梯取值
套餐KNAD_30G：30-100以10阶梯取值、100-600以100阶梯取值
        :type PathPrefix: Int
        :param IdcBand: 清洗后正常业务带宽大小，取值范围：100-15000
        :type PathPrefix: Int
        """
        self.KnadId = None
        self.ServiceId = None
        self.IpCount = None
        self.Band = None
        self.MaxBand = None
        self.IdcBand = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("ServiceId"):
            self.ServiceId = params.get("ServiceId")
        if params.get("IpCount"):
            self.IpCount = params.get("IpCount")
        if params.get("Band"):
            self.Band = params.get("Band")
        if params.get("MaxBand"):
            self.MaxBand = params.get("MaxBand")
        if params.get("IdcBand"):
            self.IdcBand = params.get("IdcBand")


class UnbindIpListRequest(AbstractModel):
    """UnbindIpList请求参数结构体
    """

    def __init__(self):
        r"""设置防护对象-可选eip列表
        """

    def _deserialize(self, params):
        return


class AssociateIpRequest(AbstractModel):
    """AssociateIp请求参数结构体
    """

    def __init__(self):
        r"""绑定eip
        :param KnadId: 
        :type PathPrefix: String
        :param Ip: 高防实例绑定的全量eip列表(注：覆盖式更新！！在请求中提交需要绑定的完整eip列表参数)
        :type PathPrefix: Array
        """
        self.KnadId = None
        self.Ip = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("Ip"):
            self.Ip = params.get("Ip")


class DisassociateIpRequest(AbstractModel):
    """DisassociateIp请求参数结构体
    """

    def __init__(self):
        r"""解绑eip
        :param Ip: 要解绑的ip
        :type PathPrefix: Array
        """
        self.Ip = None

    def _deserialize(self, params):
        if params.get("Ip"):
            self.Ip = params.get("Ip")


class DescribeKnadIpRequest(AbstractModel):
    """DescribeKnadIp请求参数结构体
    """

    def __init__(self):
        r"""已绑定eip列表
        :param IpSort: 防护ip排序规则。
asc:升序；desc：降序

        :type PathPrefix: String
        :param IpStatusSort: 状态排序规则。
asc:升序；desc：降序
        :type PathPrefix: String
        :param BandSort: 防护能力排序规则。
 asc:升序；desc：降序
        :type PathPrefix: String
        :param Ip: 单个eip address
        :type PathPrefix: String
        :param KnadId: 高防实例id
        :type PathPrefix: String
        :param ProjectId: 项目制id
        :type PathPrefix: Array
        :param PageSize: 每页条数
        :type PathPrefix: Int
        :param OffSet: 开始条数
        :type PathPrefix: Int
        """
        self.IpSort = None
        self.IpStatusSort = None
        self.BandSort = None
        self.Ip = None
        self.KnadId = None
        self.ProjectId = None
        self.PageSize = None
        self.OffSet = None

    def _deserialize(self, params):
        if params.get("IpSort"):
            self.IpSort = params.get("IpSort")
        if params.get("IpStatusSort"):
            self.IpStatusSort = params.get("IpStatusSort")
        if params.get("BandSort"):
            self.BandSort = params.get("BandSort")
        if params.get("Ip"):
            self.Ip = params.get("Ip")
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("OffSet"):
            self.OffSet = params.get("OffSet")


class DeleteKnadRequest(AbstractModel):
    """DeleteKnad请求参数结构体
    """

    def __init__(self):
        r"""退订高防实例(已绑弹性IP的高防实例无法退订)
        :param KnadId: 
        :type PathPrefix: String
        """
        self.KnadId = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")


class DescribeKnadRequest(AbstractModel):
    """DescribeKnad请求参数结构体
    """

    def __init__(self):
        r"""高防包列表
        :param ProjectId: 项目制id
        :type PathPrefix: Filter
        :param KnadId: 
        :type PathPrefix: Filter
        """
        self.ProjectId = None
        self.KnadId = None

    def _deserialize(self, params):
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")


class GetBWIpListRequest(AbstractModel):
    """GetBWIpList请求参数结构体
    """

    def __init__(self):
        r"""获取实例的黑白名单列表
        :param KnadId: 
        :type PathPrefix: String
        :param type: 策略类型（1: black, 2: white）
        :type PathPrefix: Int
        :param Ip: 要搜索的ip
        :type PathPrefix: String
        :param PageSize: 每页条数
        :type PathPrefix: Int
        :param OffSet: 开始条数
        :type PathPrefix: Int
        """
        self.KnadId = None
        self.type = None
        self.Ip = None
        self.PageSize = None
        self.OffSet = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("type"):
            self.type = params.get("type")
        if params.get("Ip"):
            self.Ip = params.get("Ip")
        if params.get("PageSize"):
            self.PageSize = params.get("PageSize")
        if params.get("OffSet"):
            self.OffSet = params.get("OffSet")


class DeleteBWRequest(AbstractModel):
    """DeleteBW请求参数结构体
    """

    def __init__(self):
        r"""删除黑白名单
        :param KnadId: 
        :type PathPrefix: String
        :param IpId: 删除的IP的id
        :type PathPrefix: Array
        :param type: 策略类型（1: black, 2: white）
        :type PathPrefix: Int
        """
        self.KnadId = None
        self.IpId = None
        self.type = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("IpId"):
            self.IpId = params.get("IpId")
        if params.get("type"):
            self.type = params.get("type")


class AddBWIpListRequest(AbstractModel):
    """AddBWIpList请求参数结构体
    """

    def __init__(self):
        r"""添加黑白名单
        :param KnadId: 
        :type PathPrefix: String
        :param Ip: 添加的IP段
        :type PathPrefix: Array
        :param type: 策略类型（1: black, 2: white）
        :type PathPrefix: Int
        """
        self.KnadId = None
        self.Ip = None
        self.type = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("Ip"):
            self.Ip = params.get("Ip")
        if params.get("type"):
            self.type = params.get("type")


class GetZoneListRequest(AbstractModel):
    """GetZoneList请求参数结构体
    """

    def __init__(self):
        r"""获取地理位置列表
        """

    def _deserialize(self, params):
        return


class ModifyPolicyRequest(AbstractModel):
    """ModifyPolicy请求参数结构体
    """

    def __init__(self):
        r"""修改防护策略
        :param KnadId: 
        :type PathPrefix: String
        :param TemplateId: 防护模板ID（默认：1075）
        :type PathPrefix: Int
        :param UdpBlock: 是否封禁Udp（1：封禁 0：不封禁）
        :type PathPrefix: Int
        :param TcpBlock: 是否封禁Tcp（1：封禁 0：不封禁）
        :type PathPrefix: Int
        :param IcmpBlock: 是否封禁Icmp（1：封禁 0：不封禁）
        :type PathPrefix: Int
        """
        self.KnadId = None
        self.TemplateId = None
        self.UdpBlock = None
        self.TcpBlock = None
        self.IcmpBlock = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("TemplateId"):
            self.TemplateId = params.get("TemplateId")
        if params.get("UdpBlock"):
            self.UdpBlock = params.get("UdpBlock")
        if params.get("TcpBlock"):
            self.TcpBlock = params.get("TcpBlock")
        if params.get("IcmpBlock"):
            self.IcmpBlock = params.get("IcmpBlock")


class ModifyBlockLocationRequest(AbstractModel):
    """ModifyBlockLocation请求参数结构体
    """

    def __init__(self):
        r"""设置封禁地域
        :param KnadId: 
        :type PathPrefix: String
        :param LocationBlock: 是否开启封禁(1:封禁; 0:不封禁)
        :type PathPrefix: Int
        :param Location: 要封禁的位置（例：['BeiJing','Other']）
        :type PathPrefix: Array
        """
        self.KnadId = None
        self.LocationBlock = None
        self.Location = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("LocationBlock"):
            self.LocationBlock = params.get("LocationBlock")
        if params.get("Location"):
            self.Location = params.get("Location")


class GetBlockLocationsRequest(AbstractModel):
    """GetBlockLocations请求参数结构体
    """

    def __init__(self):
        r"""获取封禁区域
        :param KnadId: 
        :type PathPrefix: String
        """
        self.KnadId = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")


class GetKnadPolicyRequest(AbstractModel):
    """GetKnadPolicy请求参数结构体
    """

    def __init__(self):
        r"""获取实例的防护模板信息
        :param KnadId: 
        :type PathPrefix: String
        """
        self.KnadId = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")


class InsertEipsRequest(AbstractModel):
    """InsertEips请求参数结构体
    """

    def __init__(self):
        r"""增量绑定eip
        :param KnadId: 
        :type PathPrefix: String
        :param Ip: 高防实例绑定的eip列表
        :type PathPrefix: Array
        """
        self.KnadId = None
        self.Ip = None

    def _deserialize(self, params):
        if params.get("KnadId"):
            self.KnadId = params.get("KnadId")
        if params.get("Ip"):
            self.Ip = params.get("Ip")


