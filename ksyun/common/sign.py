# -*- coding: utf-8 -*-

import hashlib
import hmac

try:
    from urllib.request import quote
except ImportError:
    from urllib import quote

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException


class Sign(object):

    @staticmethod
    # generate sign
    def sign(params, secret_key, sign_method):
        if sign_method == 'HMAC-SHA256':
            digestmod = hashlib.sha256
        elif sign_method == 'HMAC-SHA1':
            digestmod = hashlib.sha1
        else:
            raise KsyunSDKException("signMethod invalid", "signMethod only support (HMAC-SHA1, HMAC-SHA256)")

        # 加密
        str_encode = ''
        param_keys = sorted(params.keys())
        for key in param_keys:
            str_encode += quote(key, '~') + '=' + quote(str(params[key]), '~') + '&'
        str_encode = str_encode[:-1]
        # print(str_encode)
        return hmac.new(secret_key.encode('utf-8'), str_encode.encode('utf-8'), digestmod).hexdigest()
