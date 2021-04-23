"""
from functools import partial


class PyCalcCtrl:
    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
"""