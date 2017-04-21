import sys
from PyQt5 import QtWidgets
from anasayfa import Ui_Otomat


class Main(QtWidgets.QMainWindow, Ui_Otomat):
    def __init__(self):
        super(Main, self).__init__()
        self.move(300, 90)
        self.ui = Ui_Otomat()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())