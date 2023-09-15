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


