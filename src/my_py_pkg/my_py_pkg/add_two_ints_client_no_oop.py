#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client_no_oop")

    client = node.create_client(AddTwoInts, "add_two_ints")
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for Add Two Ints server...")

    # 1. 构造请求对象并填入数据
    request = AddTwoInts.Request()
    request.a = 3
    request.b = 8

    # 2. 异步发送请求（返回一个 future 对象）
    future = client.call_async(request)

    # 3. 阻塞等待，直到服务端返回响应
    rclpy.spin_until_future_complete(node, future)

    # 4. 从 future 中提取结果并打印
    response = future.result()
    node.get_logger().info(str(request.a) + " + " +
                           str(request.b) + " = " + str(response.sum))

    rclpy.shutdown()


if __name__ == "__main__":
    main()