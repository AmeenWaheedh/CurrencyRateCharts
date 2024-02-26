import sys
from PySide6 import QtWidgets
from widget import Widget
import pandas as pd
app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.show()

app.exec()

