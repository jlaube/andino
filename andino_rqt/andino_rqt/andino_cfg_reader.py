
import rclpy
from rcl_interfaces.srv import GetParameters
from rcl_interfaces.msg import Parameter

class AndinoConfigReader:
  def __init__(self, node):
    self.wheel_radius_param = 'wheel_radius'
    self.parameter_server = 'diff_controller'
    self.node = node
    self.client = node.create_client(GetParameters, '/' + self.parameter_server + '/get_parameters')

    while not self.client.wait_for_service(timeout_sec=1.0):
        self.node.get_logger().info('service not available, waiting again...')
    self.req = GetParameters.Request()

  def __del__(self):
     self.node.destroy_client(self.client)


  def readWheelRadius(self):
    self.req.names = [self.wheel_radius_param]

    try:
        response = self.client.call(self.req)
        self.node.get_logger().info(str(response.values))
        return str(response.values[0].double_value)
    except Exception as e:
        self.node.get_logger().info("DOH!!!!!! " + str(e))
    return "0.00"
