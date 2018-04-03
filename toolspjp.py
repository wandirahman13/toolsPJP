# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolspjp.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 276)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btOpen.setGeometry(QtCore.QRect(260, 10, 93, 28))
        self.btOpen.setObjectName("btOpen")
        self.edFile = QtWidgets.QLineEdit(self.centralwidget)
        self.edFile.setEnabled(False)
        self.edFile.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.edFile.setObjectName("edFile")
        self.gbPJP = QtWidgets.QGroupBox(self.centralwidget)
        self.gbPJP.setGeometry(QtCore.QRect(10, 50, 351, 71))
        self.gbPJP.setObjectName("gbPJP")
        self.cbPJP = QtWidgets.QComboBox(self.gbPJP)
        self.cbPJP.setGeometry(QtCore.QRect(30, 30, 281, 22))
        self.cbPJP.setCurrentText("")
        self.cbPJP.setObjectName("cbPJP")
        self.gbSales = QtWidgets.QGroupBox(self.centralwidget)
        self.gbSales.setGeometry(QtCore.QRect(10, 130, 351, 71))
        self.gbSales.setObjectName("gbSales")
        self.cbSales = QtWidgets.QComboBox(self.gbSales)
        self.cbSales.setGeometry(QtCore.QRect(30, 30, 281, 22))
        self.cbSales.setObjectName("cbSales")
        self.btSave = QtWidgets.QPushButton(self.centralwidget)
        self.btSave.setGeometry(QtCore.QRect(90, 220, 201, 31))
        self.btSave.setObjectName("btSave")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btOpen.setText(_translate("MainWindow", "Open"))
        self.gbPJP.setTitle(_translate("MainWindow", "PJP Code"))
        self.gbSales.setTitle(_translate("MainWindow", "Salesman Code"))
        self.btSave.setText(_translate("MainWindow", "Save Change"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

