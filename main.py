"""
import sys

from pycalc import PyCalcUi
from pycalcctrl import PyCalcCtrl
from PyQt5.QtWidgets import QApplication


def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    PyCalcCtrl(view=view)
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
"""