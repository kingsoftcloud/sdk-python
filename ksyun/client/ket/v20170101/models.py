from ksyun.common.abstract_model import AbstractModel

class PresetRequest(AbstractModel):
    """Preset请求参数结构体
    """

    def __init__(self):
        r"""add preset
        :param UniqName: 
        :type PathPrefix: String
        :param App: 
        :type PathPrefix: String
        :param Preset: 
        :type PathPrefix: String
        :param Description: 
        :type PathPrefix: String
        :param Output: 
        :type PathPrefix: String
        :param Video: 
        :type PathPrefix: String
        """
        self.UniqName = None
        self.App = None
        self.Preset = None
        self.Description = None
        self.Output = None
        self.Video = None

    def _deserialize(self, params):
        if params.get("UniqName"):
            self.UniqName = params.get("UniqName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Preset"):
            self.Preset = params.get("Preset")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Output"):
            self.Output = params.get("Output")
        if params.get("Video"):
            self.Video = params.get("Video")


class UpdatePresetRequest(AbstractModel):
    """UpdatePreset请求参数结构体
    """

    def __init__(self):
        r"""update preset
        :param UniqName: 客户的域名标识
        :type PathPrefix: String
        :param App: 客户的频道名
        :type PathPrefix: String
        :param Preset: 模板名
        :type PathPrefix: String
        :param Description: 模板描述
        :type PathPrefix: String
        :param Output: 转码输出参数集
        :type PathPrefix: String
        :param Video: 转码输出视频补充参数集
        :type PathPrefix: String
        """
        self.UniqName = None
        self.App = None
        self.Preset = None
        self.Description = None
        self.Output = None
        self.Video = None

    def _deserialize(self, params):
        if params.get("UniqName"):
            self.UniqName = params.get("UniqName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Preset"):
            self.Preset = params.get("Preset")
        if params.get("Description"):
            self.Description = params.get("Description")
        if params.get("Output"):
            self.Output = params.get("Output")
        if params.get("Video"):
            self.Video = params.get("Video")


class DelPresetRequest(AbstractModel):
    """DelPreset请求参数结构体
    """

    def __init__(self):
        r"""delete preset
        :param UniqName: 客户的域名标识
        :type PathPrefix: String
        :param App: 客户的频道名
        :type PathPrefix: String
        :param Preset: 模板名
        :type PathPrefix: String
        """
        self.UniqName = None
        self.App = None
        self.Preset = None

    def _deserialize(self, params):
        if params.get("UniqName"):
            self.UniqName = params.get("UniqName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Preset"):
            self.Preset = params.get("Preset")


class GetPresetListRequest(AbstractModel):
    """GetPresetList请求参数结构体
    """

    def __init__(self):
        r"""get preset list
        :param UniqName: 客户的域名标识
        :type PathPrefix: String
        :param App: 客户的频道名
        :type PathPrefix: String
        """
        self.UniqName = None
        self.App = None

    def _deserialize(self, params):
        if params.get("UniqName"):
            self.UniqName = params.get("UniqName")
        if params.get("App"):
            self.App = params.get("App")


class GetPresetDetailRequest(AbstractModel):
    """GetPresetDetail请求参数结构体
    """

    def __init__(self):
        r"""get preset detail
        :param UniqName: 客户的域名标识
        :type PathPrefix: String
        :param App: 客户的频道名
        :type PathPrefix: String
        :param Preset: 模板名称
        :type PathPrefix: String
        """
        self.UniqName = None
        self.App = None
        self.Preset = None

    def _deserialize(self, params):
        if params.get("UniqName"):
            self.UniqName = params.get("UniqName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Preset"):
            self.Preset = params.get("Preset")


class GetStreamTranListRequest(AbstractModel):
    """GetStreamTranList请求参数结构体
    """

    def __init__(self):
        r"""get stream tran list
        :param UniqName: 客户的域名标识
        :type PathPrefix: String
        :param App: 客户的频道名
        :type PathPrefix: String
        :param StreamID: 流名称
        :type PathPrefix: String
        """
        self.UniqName = None
        self.App = None
        self.StreamID = None

    def _deserialize(self, params):
        if params.get("UniqName"):
            self.UniqName = params.get("UniqName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("StreamID"):
            self.StreamID = params.get("StreamID")


class StartLoopRequest(AbstractModel):
    """StartLoop请求参数结构体
    """

    def __init__(self):
        r"""start loop tran
        :param UniqName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param Preset: 模板名称，支持配置：视频帧率、视频码率、音频码率、视频分辨率
        :type PathPrefix: String
        :param StreamID: 轮播流名
        :type PathPrefix: String
        :param SrcInfo: 轮播源文件信息，数组，每项包括文件路径（金山云KS3内网URL）和顺序参数。发起轮播前请先确认轮播源文件是否存在。最多可以支持100个轮播任务。
        :type PathPrefix: Array
        :param PubDomain: 用来轮播的推流域名
        :type PathPrefix: String
        :param TaskStartTime: 任务开始时间戳，指定轮播流启动播放时间，精确到秒，不填默认下发后立即开始轮播。只能填当前时间1分钟之后的时间。
        :type PathPrefix: String
        :param TaskStopTime: 任务结束时间戳，指定轮播流结束播放时间，精确到秒，不填默认结束时间为开始时间之后20天。TaskStopTime-TaskStartTime必须>30s。
        :type PathPrefix: String
        :param LoopTimes: 文件轮播次数，与TaskStopTime冲突时，以TaskStopTime为准，如果需要以轮播次数为准，TaskStopTime不填。
        :type PathPrefix: Int
        """
        self.UniqName = None
        self.App = None
        self.Preset = None
        self.StreamID = None
        self.SrcInfo = None
        self.PubDomain = None
        self.TaskStartTime = None
        self.TaskStopTime = None
        self.LoopTimes = None

    def _deserialize(self, params):
        if params.get("UniqName"):
            self.UniqName = params.get("UniqName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("Preset"):
            self.Preset = params.get("Preset")
        if params.get("StreamID"):
            self.StreamID = params.get("StreamID")
        if params.get("SrcInfo"):
            self.SrcInfo = params.get("SrcInfo")
        if params.get("PubDomain"):
            self.PubDomain = params.get("PubDomain")
        if params.get("TaskStartTime"):
            self.TaskStartTime = params.get("TaskStartTime")
        if params.get("TaskStopTime"):
            self.TaskStopTime = params.get("TaskStopTime")
        if params.get("LoopTimes"):
            self.LoopTimes = params.get("LoopTimes")


class StopLoopRequest(AbstractModel):
    """StopLoop请求参数结构体
    """

    def __init__(self):
        r"""stop loop tran
        :param UniqName: 域名空间
        :type PathPrefix: String
        :param App: 应用名
        :type PathPrefix: String
        :param StreamID: 轮播流名
        :type PathPrefix: String
        """
        self.UniqName = None
        self.App = None
        self.StreamID = None

    def _deserialize(self, params):
        if params.get("UniqName"):
            self.UniqName = params.get("UniqName")
        if params.get("App"):
            self.App = params.get("App")
        if params.get("StreamID"):
            self.StreamID = params.get("StreamID")


