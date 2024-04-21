#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

class PirSensorNode(Node):
    def __init__(self):
        super().__init__('pir_sensor_node')
        self.publisher_ = self.create_publisher(Range, '/pir_sensor', 10)
        self.timer = self.create_timer(1, self.publish_pir_data)

    def publish_pir_data(self):
        # In a real scenario, you'd read from the PIR sensor here

        pir_data = Range()
        pir_data.header.frame_id = 'pir_sensor_frame'
        pir_data.radiation_type = Range.INFRARED
        pir_data.field_of_view = 1.0  # Field of view of the sensor in radians
        pir_data.min_range = 0.0
        pir_data.max_range = 10.0
        pir_data.range = 1.0 if self.get_clock().now().nanoseconds % 4 == 0 else 0.0
        self.publisher_.publish(pir_data)
        self.get_logger().info('PIR data published')

def main(args=None):
    rclpy.init(args=args)
    pir_sensor_node = PirSensorNode()
    rclpy.spin(pir_sensor_node)
    pir_sensor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
