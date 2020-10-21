from PyQt5 import QtWidgets
from start import Ui_MainWindow as Form1
from registr import Ui_MainWindow as Form2
from end import Ui_MainWindow as Form3

from sqlalchemy import create_engine
import sys

db_connect = create_engine('postgres://postgres:postgres@localhost:53457/registr')
print(db_connect)
connection = db_connect.connect()


class Starter(QtWidgets.QMainWindow):
    def __init__(self):
        super(Starter, self).__init__()
        self.ui = Form1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)

    def start(self):
        self.ui.hide()
        self.ui = Form2()
        self.ui.show()


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Form2()
        self.ui.setupUi(self)
        self.ui.pushButton2.clicked.connect(self.reg)
        self.ui.pushButton1.clicked.connect(self.close)

    def reg(self):
        name = self.ui.textEdit2.text()
        password = self.ui.textEdit3.text()
        connection.execute(f""" INSERT INTO login (name,password) VALUES ('{name}','{password}')""")
        self.hide()
        self.ui = Form1()
        self.ui.show()

    def quit(self):
        quit()


class End(QtWidgets.QMainWindow):
    def __init__(self):
        super(End, self).__init__()
        self.ui = Form3()
        self.ui.setupUi(self)
        self.ui.pushButton3.clicked.connect(self.quit)

    def quit(self):
        quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Starter()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
