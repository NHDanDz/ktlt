# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from ListPeople import ListPeople
from People import People
import csv
List = ListPeople()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 70, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 140, 701, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.EmCode = QtWidgets.QLineEdit(parent=self.groupBox)
        self.EmCode.setGeometry(QtCore.QRect(200, 40, 371, 22))
        self.EmCode.setObjectName("EmCode")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.label_3.setObjectName("label_3")
        self.Name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.Name.setGeometry(QtCore.QRect(200, 100, 371, 22))
        self.Name.setObjectName("Name")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 55, 16))
        self.label_4.setObjectName("label_4")
        self.Date = QtWidgets.QLineEdit(parent=self.groupBox)
        self.Date.setGeometry(QtCore.QRect(200, 160, 371, 22))
        self.Date.setObjectName("Date")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 220, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 55, 16))
        self.label_6.setObjectName("label_6")
        self.Pos = QtWidgets.QLineEdit(parent=self.groupBox)
        self.Pos.setGeometry(QtCore.QRect(200, 220, 371, 22))
        self.Pos.setObjectName("Pos")
        self.Sal = QtWidgets.QLineEdit(parent=self.groupBox)
        self.Sal.setGeometry(QtCore.QRect(200, 280, 371, 22))
        self.Sal.setObjectName("Sal")
        self.Home = QtWidgets.QPushButton(parent=self.groupBox)
        self.Home.setGeometry(QtCore.QRect(310, 330, 93, 28))
        self.Home.setObjectName("Home")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Page1"))
        self.label.setText(_translate("MainWindow", "Add a profile"))
        self.groupBox.setTitle(_translate("MainWindow", "Information"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Employee code"))
        self.label_4.setText(_translate("MainWindow", "Date"))
        self.label_5.setText(_translate("MainWindow", "Position"))
        self.label_6.setText(_translate("MainWindow", "Salary"))
        self.Home.setText(_translate("MainWindow", "Enter"))
    def get_Info(self):
        global List  # Sử dụng biến toàn cục List
        # Lấy thông tin từ các trường dữ liệu và thêm vào biến toàn cục List
        NewOne = People(str(self.EmCode.text()), str(self.Name.text()), str(self.Date.text()), str(self.Pos.text()), str(self.Sal.text()))  
        NewList = NewOne.to_list()
        print(NewList)
        file = open('my.csv', 'a', newline = '', encoding='utf-8')
        writer = csv.writer(file)
        writer.writerows([NewList])
        file.close()
        List.List_People.append(NewOne) 
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
