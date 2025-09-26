from ksyun.common.abstract_model import AbstractModel


class QueryUnPayOrdersRequest(AbstractModel):
    """QueryUnPayOrders请求参数结构体
    """

    def __init__(self):
        r"""查询主账号待支付的订单列表
        :param page: 页码，从1开始
        :type PathPrefix: Int
        :param size: 每页大小
        :type PathPrefix: Int
        """
        self.page = None
        self.size = None

    def _deserialize(self, params):
        if params.get("page"):
            self.page = params.get("page")
        if params.get("size"):
            self.size = params.get("size")


class QueryOrderInfoRequest(AbstractModel):
    """QueryOrderInfo请求参数结构体
    """

    def __init__(self):
        r"""根据订单ID查询订单信息
        :param orderId: 订单ID
        :type PathPrefix: String
        """
        self.orderId = None

    def _deserialize(self, params):
        if params.get("orderId"):
            self.orderId = params.get("orderId")


class CancelOrderRequest(AbstractModel):
    """CancelOrder请求参数结构体
    """

    def __init__(self):
        r"""取消还未支付的订单，取消后不能再支付
        :param orderId: 订单ID
        :type PathPrefix: String
        """
        self.orderId = None

    def _deserialize(self, params):
        if params.get("orderId"):
            self.orderId = params.get("orderId")


class LaunchPayOrderRequest(AbstractModel):
    """LaunchPayOrder请求参数结构体
    """

    def __init__(self):
        r"""通过订单ID支付订单，会自动扣余额的金额
        :param OrderId: 订单ID
        :type PathPrefix: String
        """
        self.OrderId = None

    def _deserialize(self, params):
        if params.get("OrderId"):
            self.OrderId = params.get("OrderId")
