import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.show()

hwnd = window.winId()

print(hwnd)

app.exec()