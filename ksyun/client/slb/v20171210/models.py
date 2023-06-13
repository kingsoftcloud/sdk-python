from ksyun.common.abstract_model import AbstractModel

class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体
    """

    def __init__(self):
        r"""获取应用型负载均衡
        :param LoadBalancerId: 负载均衡的ID
        :type PathPrefix: Filter
        :param State: 负载均衡的状态，已绑定，未绑定
        :type PathPrefix: String
        :param ProjectId: 负载均衡所属项目的ID
        :type PathPrefix: Filter
        :param Filter: vpc-id，VPC的ID
        :type PathPrefix: Filter
        """
        self.LoadBalancerId = None
        self.State = None
        self.ProjectId = None
        self.Filter = None

    def _deserialize(self, params):
        if params.get("LoadBalancerId"):
            self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("State"):
            self.State = params.get("State")
        if params.get("ProjectId"):
            self.ProjectId = params.get("ProjectId")
        if params.get("Filter"):
            self.Filter = params.get("Filter")


