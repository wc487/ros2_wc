#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")

    def call_add_two_ints(self, a, b):
        # 等待服务端上线
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Add Two Ints server...")

        # 构造请求数据
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        # 发送异步请求
        future = self.client_.call_async(request)
        # 注册回调函数：当收到响应时，自动执行 callback_call_add_two_ints
        future.add_done_callback(partial
                                 (self.callback_call_add_two_ints,request=request))

    def callback_call_add_two_ints(self, future,request):
        # 从 future 中提取结果并打印
        response = future.result()
        self.get_logger().info(str(request.a) + " + " +
                                  str(request.b) + " = " + str(response.sum))


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    node.call_add_two_ints(2, 7)
    node.call_add_two_ints(1, 4)
    node.call_add_two_ints(100, 200)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()