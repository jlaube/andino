import sys

from rqt_gui.main import Main
from andino_rqt.ui_andino_calibrate.Ui_CalibrationUI import Speedometer


def main():
    plugin = 'andino_rqt.calibrate.CalibrateAndino'
    main = Main(filename=plugin)
    sys.exit(main.main(sys.argv, standalone=plugin))

if __name__ == '__main__':
    main()
