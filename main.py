import sys

from pycalc import PyCalcUi, evaluateExpression
from pycalcctrl import PyCalcCtrl
from PyQt5.QtWidgets import QApplication


def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
