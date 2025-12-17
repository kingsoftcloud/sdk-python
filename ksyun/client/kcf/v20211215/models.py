from ksyun.common.abstract_model import AbstractModel

class GetLogDateRequest(AbstractModel):
    """GetLogDate请求参数结构体
    """

    def __init__(self):
        r"""查询云函数日志信息
        :param id: 
        :type PathPrefix: Int
        """
        self.id = None

    def _deserialize(self, params):
        if params.get("id"):
            self.id = params.get("id")


class CreateFunctionRequest(AbstractModel):
    """CreateFunction请求参数结构体
    """

    def __init__(self):
        r"""创建云函数
        :param Id: 函数ID
        :type PathPrefix: String
        :param Name: 函数名称
        :type PathPrefix: String
        :param Namespace: 命名空间
        :type PathPrefix: String
        :param Runtime: 运行时环境，支持的值：Java8、Java11、Java17、Go1、Nodejs16、Nodejs14、Nodejs12、Nodejs10、Python3.10
        :type PathPrefix: String
        :param CaPort: 应用端口  1 ≤ CaPort ≤ 65535
        :type PathPrefix: Int
        :param StartupCommand: 启动命令，如 ["./start.sh", "-c", "config.yaml"]， [ "python","python-test.py"]， [ "node","nodejs-test.js"], [ "java","-jar","demo.jar"]
        :type PathPrefix: Array
        :param Description: 函数描述 最多 32 个 Unicode 字符
        :type PathPrefix: String
        :param Timeout: 函数超时时间，单位：秒，默认180秒 。若指定，需满足1 ≤ Timeout ≤ 86400
        :type PathPrefix: Int
        :param MemorySize: 函数内存大小，单位：MB，默认512MB。若指定，若指定，必须满足 MemorySize ≤ 3072 且 MemorySize % 64 == 0
        :type PathPrefix: Int
        :param SingleInstanceConcurrency: 单实例并发数，默认1  1 ≤ SingleInstanceConcurrency ≤ 100；
        :type PathPrefix: Int
        :param InternetAccess: 是否允许访问公网，默认false
        :type PathPrefix: Boolean
        :param Code: 
        :type PathPrefix: Object
        :param Environment: 环境变量配置
        :type PathPrefix: Object
        :param VpcConfig: VPC配置信息
        :type PathPrefix: Object
        :param LogConfig: 日志配置信息
        :type PathPrefix: Object
        :param LivenessProbeConfig: 存活探针配置
        :type PathPrefix: Object
        :param ReadinessProbeConfig: 就绪探针配置
        :type PathPrefix: Object
        :param Layers: Layer列表，格式为“name#version”，如 “layer#1”
        :type PathPrefix: Array
        """
        self.Id = None
        self.Name = None
        self.Namespace = None
        self.Runtime = None
        self.CaPort = None
        self.StartupCommand = None
        self.Description = None
        self.Timeout = None
        self.MemorySize = None
        self.SingleInstanceConcurrency = None
        self.InternetAccess = None
        self.Code = None
        self.Environment = None
        self.VpcConfig = None
        self.LogConfig = None
        self.LivenessProbeConfig = None
        self.ReadinessProbeConfig = None
        self.Layers = None

    def _deserialize(self, params):
        if params.get("Id"):
            self.Id = params.get("Id")
        if params.get("Name"):
            self.Name = params.get("Name")
        if params.get("Namespace"):
            self.Namespace = params.get("Namespace")
        if params.get("Runtime"):
            self.Runtime = params.get("Runtime")
        if params.get("CaPort"):
            self.CaPort = params.get("CaPort")
        if params.get("StartupCommand"):
            self.StartupCommand = params.get("StartupCommand")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("MemorySize"):
            self.MemorySize = params.get("MemorySize")
        if params.get("SingleInstanceConcurrency"):
            self.SingleInstanceConcurrency = params.get("SingleInstanceConcurrency")
        if params.get("InternetAccess"):
            self.InternetAccess = params.get("InternetAccess")
        if params.get("Code"):
            self.Code = params.get("Code")
        if params.get("Environment"):
            self.Environment = params.get("Environment")
        if params.get("VpcConfig"):
            self.VpcConfig = params.get("VpcConfig")
        if params.get("LogConfig"):
            self.LogConfig = params.get("LogConfig")
        if params.get("LivenessProbeConfig"):
            self.LivenessProbeConfig = params.get("LivenessProbeConfig")
        if params.get("ReadinessProbeConfig"):
            self.ReadinessProbeConfig = params.get("ReadinessProbeConfig")
        if params.get("Layers"):
            self.Layers = params.get("Layers")


class CheckFunctionServiceRequest(AbstractModel):
    """CheckFunctionService请求参数结构体
    """

    def __init__(self):
        r"""检测用户是否开通函数服务
        """

    def _deserialize(self, params):
        return


class OpenFunctionServiceRequest(AbstractModel):
    """OpenFunctionService请求参数结构体
    """

    def __init__(self):
        r"""开通函数服务
        """

    def _deserialize(self, params):
        return


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction请求参数结构体
    """

    def __init__(self):
        r"""删除云函数
        :param Id: 函数ID
        :type PathPrefix: String
        """
        self.Id = None

    def _deserialize(self, params):
        if params.get("Id"):
            self.Id = params.get("Id")


class CreateTriggerRequest(AbstractModel):
    """CreateTrigger请求参数结构体
    """

    def __init__(self):
        r"""创建触发器
        :param FunctionId: 函数ID
        :type PathPrefix: String
        :param TriggerName: 触发器名称，在函数内唯一
        :type PathPrefix: String
        :param Type: 触发器类型，http/ks3
        :type PathPrefix: String
        :param Enable: 触发器启用状态，true表示启用，false表示禁用。默认为true。并且仅在Type为ks3时有效
        :type PathPrefix: Boolean
        :param TriggerDesc: 触发器配置
        :type PathPrefix: Object
        """
        self.FunctionId = None
        self.TriggerName = None
        self.Type = None
        self.Enable = None
        self.TriggerDesc = None

    def _deserialize(self, params):
        if params.get("FunctionId"):
            self.FunctionId = params.get("FunctionId")
        if params.get("TriggerName"):
            self.TriggerName = params.get("TriggerName")
        if params.get("Type"):
            self.Type = params.get("Type")
        if params.get("Enable"):
            self.Enable = params.get("Enable")
        if params.get("TriggerDesc"):
            self.TriggerDesc = params.get("TriggerDesc")


class DeleteTriggerRequest(AbstractModel):
    """DeleteTrigger请求参数结构体
    """

    def __init__(self):
        r"""删除触发器
        :param Id: 触发器ID
        :type PathPrefix: String
        """
        self.Id = None

    def _deserialize(self, params):
        if params.get("Id"):
            self.Id = params.get("Id")


class ModifyFunctionRequest(AbstractModel):
    """ModifyFunction请求参数结构体
    """

    def __init__(self):
        r"""更新函数配置
        :param Id: 函数ID
        :type PathPrefix: String
        :param Runtime: 运行时环境，支持的值：Java8、Java11、Java17、Go1、Nodejs16、Nodejs14、Nodejs12、Nodejs10、Python3.10
        :type PathPrefix: String
        :param CaPort: 容器应用端口  1 ≤ CaPort ≤ 65535
        :type PathPrefix: Int
        :param StartupCommand: 启动命令，如 ["./start.sh", "-c", "config.yaml"]
        :type PathPrefix: Array
        :param Timeout: 函数超时时间，单位：秒，默认180秒 。若指定，需满足1 ≤ Timeout ≤ 86400
        :type PathPrefix: Int
        :param MemorySize: 函数内存大小，单位：MB，默认512MB。若指定，必须满足 MemorySize ≤ 3072 且 MemorySize % 64 == 0
        :type PathPrefix: Int
        :param SingleInstanceConcurrency: 单实例并发数，默认1  1 ≤ SingleInstanceConcurrency ≤ 100；
        :type PathPrefix: Int
        :param InternetAccess: 是否允许访问公网，默认false
        :type PathPrefix: Boolean
        :param Code: 函数代码配置
        :type PathPrefix: Object
        :param Environment: 环境变量配置
        :type PathPrefix: Object
        :param VpcConfig: VPC配置信息
        :type PathPrefix: Object
        :param LogConfig: 日志配置信息
        :type PathPrefix: Object
        :param LivenessProbeConfig: 存活探针配置
        :type PathPrefix: Object
        :param ReadinessProbeConfig: 就绪探针配置
        :type PathPrefix: Object
        :param Layers: Layer列表，格式为“name#version”，如 “layer#1”
        :type PathPrefix: Array
        """
        self.Id = None
        self.Runtime = None
        self.CaPort = None
        self.StartupCommand = None
        self.Timeout = None
        self.MemorySize = None
        self.SingleInstanceConcurrency = None
        self.InternetAccess = None
        self.Code = None
        self.Environment = None
        self.VpcConfig = None
        self.LogConfig = None
        self.LivenessProbeConfig = None
        self.ReadinessProbeConfig = None
        self.Layers = None

    def _deserialize(self, params):
        if params.get("Id"):
            self.Id = params.get("Id")
        if params.get("Runtime"):
            self.Runtime = params.get("Runtime")
        if params.get("CaPort"):
            self.CaPort = params.get("CaPort")
        if params.get("StartupCommand"):
            self.StartupCommand = params.get("StartupCommand")
        if params.get("Timeout"):
            self.Timeout = params.get("Timeout")
        if params.get("MemorySize"):
            self.MemorySize = params.get("MemorySize")
        if params.get("SingleInstanceConcurrency"):
            self.SingleInstanceConcurrency = params.get("SingleInstanceConcurrency")
        if params.get("InternetAccess"):
            self.InternetAccess = params.get("InternetAccess")
        if params.get("Code"):
            self.Code = params.get("Code")
        if params.get("Environment"):
            self.Environment = params.get("Environment")
        if params.get("VpcConfig"):
            self.VpcConfig = params.get("VpcConfig")
        if params.get("LogConfig"):
            self.LogConfig = params.get("LogConfig")
        if params.get("LivenessProbeConfig"):
            self.LivenessProbeConfig = params.get("LivenessProbeConfig")
        if params.get("ReadinessProbeConfig"):
            self.ReadinessProbeConfig = params.get("ReadinessProbeConfig")
        if params.get("Layers"):
            self.Layers = params.get("Layers")


class DescribeTriggersRequest(AbstractModel):
    """DescribeTriggers请求参数结构体
    """

    def __init__(self):
        r"""获取触发器列表
        :param FunctionId: 函数Id
        :type PathPrefix: String
        """
        self.FunctionId = None

    def _deserialize(self, params):
        if params.get("FunctionId"):
            self.FunctionId = params.get("FunctionId")


