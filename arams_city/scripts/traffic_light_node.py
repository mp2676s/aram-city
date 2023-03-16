#!/usr/bin/env python3

from arams_city_plugin_interfaces.srv import SetStopLightColor
import rclpy
import time
from rclpy.node import Node

BLACK = 0
RED = 1
YELLOW = 2
ORANGE = 3
GREEN = 4


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('traffig_lights_node')
        # y road traffic lights        
        self.tl475 = self.create_client(SetStopLightColor, 'switch_475/set_color')
        while not self.tl475.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl476 = self.create_client(SetStopLightColor, 'switch_476/set_color')
        while not self.tl476.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl477 = self.create_client(SetStopLightColor, 'switch_477/set_color')
        while not self.tl477.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl478 = self.create_client(SetStopLightColor, 'switch_478/set_color')        
        while not self.tl478.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl479 = self.create_client(SetStopLightColor, 'switch_479/set_color')
        while not self.tl479.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl480 = self.create_client(SetStopLightColor, 'switch_480/set_color')
        while not self.tl480.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl481 = self.create_client(SetStopLightColor, 'switch_481/set_color')
        while not self.tl481.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        # x road traffic lights
        self.tl482 = self.create_client(SetStopLightColor, 'switch_482/set_color')
        while not self.tl482.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl483 = self.create_client(SetStopLightColor, 'switch_483/set_color')
        while not self.tl483.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl484 = self.create_client(SetStopLightColor, 'switch_484/set_color')
        while not self.tl484.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl485 = self.create_client(SetStopLightColor, 'switch_485/set_color')
        while not self.tl485.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl486 = self.create_client(SetStopLightColor, 'switch_486/set_color')
        while not self.tl486.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.tl487 = self.create_client(SetStopLightColor, 'switch_487/set_color')
        while not self.tl487.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.req = SetStopLightColor.Request()

    def send_request_y_roads(self, state):
        self.req.color.data = state
        self.future = self.tl475.call_async(self.req)
        self.future = self.tl476.call_async(self.req)
        self.future = self.tl477.call_async(self.req)
        self.future = self.tl478.call_async(self.req)
        self.future = self.tl479.call_async(self.req)
        self.future = self.tl480.call_async(self.req)
        self.future = self.tl481.call_async(self.req)

    def send_request_x_roads(self, state):
        self.req.color.data = state
        self.future = self.tl482.call_async(self.req)
        self.future = self.tl483.call_async(self.req)
        self.future = self.tl484.call_async(self.req)
        self.future = self.tl485.call_async(self.req)
        self.future = self.tl486.call_async(self.req)
        self.future = self.tl487.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    traffic_light_service_client = MinimalClientAsync()

    while rclpy.ok():
        traffic_light_service_client.send_request_x_roads(RED)
        traffic_light_service_client.send_request_y_roads(GREEN)
        rclpy.spin_once(traffic_light_service_client)
        if traffic_light_service_client.future.done():
            try:
                response = traffic_light_service_client.future.result()
            except Exception as e:
                traffic_light_service_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                traffic_light_service_client.get_logger().info('Response: ' + str(response.success))
        time.sleep(8)
        traffic_light_service_client.send_request_x_roads(YELLOW)
        traffic_light_service_client.send_request_y_roads(YELLOW)
        rclpy.spin_once(traffic_light_service_client)
        if traffic_light_service_client.future.done():
            try:
                response = traffic_light_service_client.future.result()
            except Exception as e:
                traffic_light_service_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                traffic_light_service_client.get_logger().info('Response: ' + str(response.success))
        time.sleep(2)
        traffic_light_service_client.send_request_x_roads(GREEN)
        traffic_light_service_client.send_request_y_roads(RED)
        rclpy.spin_once(traffic_light_service_client)
        if traffic_light_service_client.future.done():
            try:
                response = traffic_light_service_client.future.result()
            except Exception as e:
                traffic_light_service_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                traffic_light_service_client.get_logger().info('Response: ' + str(response.success))
        time.sleep(8)
        traffic_light_service_client.send_request_x_roads(YELLOW)
        traffic_light_service_client.send_request_y_roads(YELLOW)
        rclpy.spin_once(traffic_light_service_client)
        if traffic_light_service_client.future.done():
            try:
                response = traffic_light_service_client.future.result()
            except Exception as e:
                traffic_light_service_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                traffic_light_service_client.get_logger().info('Response: ' + str(response.success))
        time.sleep(2)


    traffic_light_service_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()