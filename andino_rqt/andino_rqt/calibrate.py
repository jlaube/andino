from qt_gui.plugin import Plugin
from .ui_andino_calibrate import *

class CalibrateAndino(Plugin):

    def __init__(self, context):
        super(CalibrateAndino, self).__init__(context)
        self.setObjectName('CalibrateAndino')

        self._context = context
        self._node = context.node

        self._widget = Ui_CalibrationUI()
        context.add_widget(self._widget)
