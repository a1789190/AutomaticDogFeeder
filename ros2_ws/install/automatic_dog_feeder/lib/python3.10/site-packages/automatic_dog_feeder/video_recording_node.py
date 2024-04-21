import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from sensor_msgs.msg import Range
import cv2

class VideoRecordingNode(Node):
    def __init__(self):
        super().__init__('video_recording_node')
        self.pir_subscriber = self.create_subscription(Range, '/pir_sensor', self.pir_callback, 10)
        self.recording = False
        self.video_writer = None

    def pir_callback(self, msg):
        if msg.range == 1.0:
            self.get_logger().info('Motion detected!')
        else:
            self.get_logger().info('No motion detected.')

    def start_recording(self):
        # OpenCV code to initialize video recording device
        # Here, we're assuming a webcam at index 0.
        self.video_capture = cv2.VideoCapture(0)
        
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        
        self.get_logger().info('Starting video recording...')
        self.recording = True

    def stop_recording(self):

        if self.video_writer is not None:
            self.video_writer.release()
        if self.video_capture is not None:
            self.video_capture.release()

        self.get_logger().info('Stopping video recording...')
        self.recording = False

def main(args=None):
    rclpy.init(args=args)
    video_recording_node = VideoRecordingNode()
    rclpy.spin(video_recording_node)
    video_recording_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
