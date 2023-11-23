from qt_gui.plugin import Plugin
from .calibration_widget import *

class CalibrateAndino(Plugin):
    def __init__(self, context):
        super(CalibrateAndino, self).__init__(context)
        self.setObjectName('CalibrateAndino')

        self._context = context
        self._node = context.node

        self._widget = CalibrationWidget(self._node)
        context.add_widget(self._widget)
