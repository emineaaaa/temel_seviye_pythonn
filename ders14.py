import sys
from PyQt6 import QtWidgets

uygulama=QtWidgets.QApplication(sys.argv)

pencere=QtWidgets.QtWidget()

pencere.setWindowTitle("BTK Python Kursu")

pencere.show()

sys.exit(uygulama.exec())



