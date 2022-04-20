# -*- coding: utf-8 -*-
# Copyright 2022 Ksyun Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    # py3
    import configparser
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    # py2
    import ConfigParser as configparser
    from urllib import urlencode
    from urllib import urlopen

from ksyun.common.exception.ksyun_sdk_exception import KsyunSDKException


class Credential(object):
    def __init__(self, secret_id, secret_key, token=None):
        """Ksyun Credentials.
        :param secret_id: The secret id of your credential.
        :type secret_id: str
        :param secret_key: The secret key of your credential.
        :type secret_key: str
        :param token: The federation token of your credential, if this field
                      is specified, secret_id and secret_key should be set
        """
        if secret_id is None or secret_id.strip() == "":
            raise KsyunSDKException("InvalidCredential", "secret id should not be none or empty")
        if secret_id.strip() != secret_id:
            raise KsyunSDKException("InvalidCredential", "secret id should not contain spaces")
        self.secret_id = secret_id

        if secret_key is None or secret_key.strip() == "":
            raise KsyunSDKException("InvalidCredential", "secret key should not be none or empty")
        if secret_key.strip() != secret_key:
            raise KsyunSDKException("InvalidCredential", "secret key should not contain spaces")
        self.secret_key = secret_key

        self.token = token

    @property
    def secretId(self):
        return self.secret_id

    @property
    def secretKey(self):
        return self.secret_key
