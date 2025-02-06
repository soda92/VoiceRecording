import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView
from pathlib import Path

if __name__ == "__main__":
    app = QGuiApplication()
    view = QQuickView()
    view.engine().addImportPath(Path(__file__).resolve().parent)
    view.loadFromModule(".", "Copy")
    view.show()
    ex = app.exec()
    del view
    sys.exit(ex)