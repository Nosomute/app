import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon 

# Agregar el directorio padre al path para importar módulos locales
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  

# Importación del módulo local
from assets.icon import icon_qrc  

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/ui/mainwindow.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
