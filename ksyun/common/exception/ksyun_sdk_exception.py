# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys


class KsyunSDKException(Exception):
    """ksyun sdk 异常类"""

    def __init__(self, code=None, message=None, requestId=None):
        self.code = code
        self.message = message or str(code)
        self.requestId = requestId
        # Python 2/3 compatible super() call
        if sys.version_info[0] >= 3:
            super().__init__(self.message)
        else:
            super(KsyunSDKException, self).__init__(self.message)

    def __str__(self):
        return "[KsyunSDKException] code:%s message:%s requestId:%s" % (
            self.code, self.message, self.requestId
        )

    # 保证与旧版本代码兼容，保留原有方法名
    def get_code(self):
        return self.code

    def get_message(self):
        return self.message

    def get_request_id(self):
        return self.requestId
