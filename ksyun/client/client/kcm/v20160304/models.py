from ksyun.common.abstract_model import AbstractModel

class ApplyCertificateRequest(AbstractModel):
    """ApplyCertificate请求参数结构体
    """

    def __init__(self):
        r"""申请证书
        :param MainDomain: 证书绑定主域名
        :type PathPrefix: String
        :param CertificateCode: 证书代码，详见[CertificateCode可选值](https://docs.ksyun.com/documents/37638)
        :type PathPrefix: String
        :param YearLength: 证书年限，默认值为1
        :type PathPrefix: Int
        :param DomainCount: 域名数量，最小值为1
        :type PathPrefix: Int
        :param WildcardCount: 通配符域名数量，最小值为0
        :type PathPrefix: Int
        :param ProductId: 生成订单时产生的商品ID
        :type PathPrefix: String
        :param SubOrderId: 产生的子订单ID
        :type PathPrefix: String
        :param ProjectId: 资源所属项目ID
        :type PathPrefix: Int
        """
        self.MainDomain = None
        self.CertificateCode = None
        self.YearLength = None
        self.DomainCount = None
        self.WildcardCount = None
        self.ProductId = None
        self.SubOrderId = None
        self.ProjectId = None

    def _deserialize(self, params):
        if params.get("MainDomain"):
            self.MainDomain = params.get("MainDomain")
        if params.get("CertificateCode"):
            self.CertificateCode = params.get("CertificateCode")
        if params.get("YearLength"):
            self.YearLength = params.get("YearLength")
        if params.get("DomainCount"):
            self.DomainCount = params.get("DomainCount")
        if params.get("WildcardCount"):
            self.WildcardCount = params.get("WildcardCount")
        if params.get("ProductId"):
            self.ProductId = params.get("ProductId")
        if params.get("SubOrderId"):
            self.SubOrderId = params.get("SubOrderId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")


class UpdateCertificateRequest(AbstractModel):
    """UpdateCertificate请求参数结构体
    """

    def __init__(self):
        r"""更新/补全证书信息
        :param CertificateId: 证书ID
        :type PathPrefix: String
        :param AuthMethod: 验证方式（除Sectigo外仅针对DV证书，Sectigo全部需要）
        :type PathPrefix: String
        :param CSR: 证书CSR字符串，当CsrSource为USER或缺省时，此值不可缺省
        :type PathPrefix: String
        :param CompanyName: 企业名称
        :type PathPrefix: String
        :param Department: 部门名称
        :type PathPrefix: String
        :param State: 省份
        :type PathPrefix: String
        :param City: 城市
        :type PathPrefix: String
        :param Address: 地址
        :type PathPrefix: String
        :param CompanyPhone: 公司电话,可为座机或者手机
        :type PathPrefix: String
        :param PostalCode: 邮编
        :type PathPrefix: String
        :param DcvEmail: 可从whois查询到的注册域名时填写的邮箱信息
        :type PathPrefix: String
        :param AdditionalDomains: 附加域名,多个域名以英文,分隔
        :type PathPrefix: String
        :param Wildcards: 通配符域名,多个通配符域名以英文,分隔
        :type PathPrefix: String
        :param Contact: 联系人,DV证书只需要技术联系人
        :type PathPrefix: String
        :param IsSubmit: 是否提交，提交后将把订单数据提交给第三方，可选值0 否|1 是

约束：
- 当值为0时：
可以用来修改Contact、CompanyName、State、City、Address、CompanyPhone、PostalCode、Department等信息；
- 当值为1时：
  - 必须保证Contact不为空
  - 且CompanyName、State、City、Address、CompanyPhone、PostalCode、Department不为空，或在IsSubmit为0时已经设置过
  - 对于DV证书，以上规则有两个例外
     - Department可为空
     - CompanyPhone可为空，但contact当中必须设置phone
        :type PathPrefix: String
        :param BusinessLicence: 企业营业执照图片文件，图片的base64值，图片大小不超过600K
        :type PathPrefix: String
        :param CsrSource: CSR字符串来源
- 约束
  - IsSubmit为0时，此参数可缺省
  - IsSubmit为1时
     - 当值为USER时，参数CSR不可缺省或此前在IsSubmit为0时设置过；
     - 当值为SYSTEM时，CSR参数或此前设置的CSR无效
        :type PathPrefix: String
        :param Algorithm: 编码算法类型，可选值

- ECC
- RSA 默认值
        :type PathPrefix: String
        """
        self.CertificateId = None
        self.AuthMethod = None
        self.CSR = None
        self.CompanyName = None
        self.Department = None
        self.State = None
        self.City = None
        self.Address = None
        self.CompanyPhone = None
        self.PostalCode = None
        self.DcvEmail = None
        self.AdditionalDomains = None
        self.Wildcards = None
        self.Contact = None
        self.IsSubmit = None
        self.BusinessLicence = None
        self.CsrSource = None
        self.Algorithm = None

    def _deserialize(self, params):
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("AuthMethod"):
            self.AuthMethod = params.get("AuthMethod")
        if params.get("CSR"):
            self.CSR = params.get("CSR")
        if params.get("CompanyName"):
            self.CompanyName = params.get("CompanyName")
        if params.get("Department"):
            self.Department = params.get("Department")
        if params.get("State"):
            self.State = params.get("State")
        if params.get("City"):
            self.City = params.get("City")
        if params.get("Address"):
            self.Address = params.get("Address")
        if params.get("CompanyPhone"):
            self.CompanyPhone = params.get("CompanyPhone")
        if params.get("PostalCode"):
            self.PostalCode = params.get("PostalCode")
        if params.get("DcvEmail"):
            self.DcvEmail = params.get("DcvEmail")
        if params.get("AdditionalDomains"):
            self.AdditionalDomains = params.get("AdditionalDomains")
        if params.get("Wildcards"):
            self.Wildcards = params.get("Wildcards")
        if params.get("Contact"):
            self.Contact = params.get("Contact")
        if params.get("IsSubmit"):
            self.IsSubmit = params.get("IsSubmit")
        if params.get("BusinessLicence"):
            self.BusinessLicence = params.get("BusinessLicence")
        if params.get("CsrSource"):
            self.CsrSource = params.get("CsrSource")
        if params.get("Algorithm"):
            self.Algorithm = params.get("Algorithm")


class ListCertificatesRequest(AbstractModel):
    """ListCertificates请求参数结构体
    """

    def __init__(self):
        r"""描述证书
        :param CertificateId: 一个或多个证书ID
        :type PathPrefix: Filter
        :param ProjectId: 一个或多个项目ID
        :type PathPrefix: Filter
        :param Filter: 主域名
        :type PathPrefix: Filter
        """
        self.CertificateId = None
        self.ProjectId = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


class GetCertificateDetailRequest(AbstractModel):
    """GetCertificateDetail请求参数结构体
    """

    def __init__(self):
        r"""获取证书详情
        :param CertificateId: 证书ID
        :type PathPrefix: String
        """
        self.CertificateId = None

    def _deserialize(self, params):
        if params.get("CertificateId"):
            self.CertificateId = params.get("CertificateId")


