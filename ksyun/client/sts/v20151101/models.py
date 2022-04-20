from ksyun.common.abstract_model import AbstractModel

class AssumeRoleRequest(AbstractModel):
    """AssumeRole请求参数结构体
    """

    def __init__(self):
        r"""获取角色的一个临时安全令牌
        :param RoleKrn: 要扮演的IAM角色的KRN，参考格式：krn:ksc:iam::account-id:role/role-name。

您可以通过IAM控制台访问对应角色详情页查询对应角色的KRN信息。
        :type PathPrefix: String
        :param RoleSessionName: 角色会话名称。
该参数为用户自定义参数。通常设置为调用该API的用户身份来区分实际不同的操作者。
        :type PathPrefix: String
        :param DurationSeconds: 过期时间。单位：秒。

过期时间最小值为900秒，最大值为要扮演角色的MaxSessionDuration时间。默认值为3600秒。
        :type PathPrefix: String
        :param Policy: 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下：
如果指定该权限策略，则STS Token最终的权限策略取IAM角色权限策略与该权限策略的交集。
如果不指定该权限策略，则STS Token最终的权限策略取IAM角色的权限策略。
长度为1~1024个字符。

格式：

{
“Version”: “2015-11-01”,
“Statement”: [
{
“Effect”: “Allow”,
“Action”: “",
“Resource”: "”
}
]
}

        :type PathPrefix: String
        """
        self.RoleKrn = None
        self.RoleSessionName = None
        self.DurationSeconds = None
        self.Policy = None

    def _deserialize(self, params):
        if params.get("RoleKrn"):
            self.RoleKrn = params.get("RoleKrn")
        if params.get("RoleSessionName"):
            self.RoleSessionName = params.get("RoleSessionName")
        if params.get("DurationSeconds"):
            self.DurationSeconds = params.get("DurationSeconds")
        if params.get("Policy"):
            self.Policy = params.get("Policy")


