#!/usr/bin/env python3

from arams_city_plugin_interfaces.srv import SetStopLightColor
import rclpy
from rclpy.node import Node

RED = 1

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('traffig_lights_node')
        self.cli = self.create_client(SetStopLightColor, 'switch_475/set_color')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SetStopLightColor.Request()

    def send_request(self, state):
        self.req.color.data = state
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)

    traffic_light_service_client = MinimalClientAsync()

    response = traffic_light_service_client.send_request(RED)
    traffic_light_service_client.get_logger().info('Response: ' + str(response.success))

    traffic_light_service_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()