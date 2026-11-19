#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ComputeRectangArea


class ComputeRectangAreaServerNode(Node):
    def __init__(self):
        super().__init__("compute_rectang_area_server")
        self.compute_rectang_area_server = self.create_service(ComputeRectangArea, "compute_area", self.callback_compute_area)
        self.get_logger().info("compute_area_server has been started.")


    def callback_compute_area(self, request: ComputeRectangArea.Request, response: ComputeRectangArea.Response):
        response.area = request.length * request.width
        self.get_logger().info(str(request.length) + "*" +
                               str(request.width) + " = " + str(response.area))
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ComputeRectangAreaServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()