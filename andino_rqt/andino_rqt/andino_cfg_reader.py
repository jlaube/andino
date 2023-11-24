import rospy


class AndinoConfigReader:
  def __init__(self):
    self.wheel_radius_param = '/param_wr'

  def readWheelRadius(self):
    return
    # return rospy.get_param(self.wheel_radius_param)
