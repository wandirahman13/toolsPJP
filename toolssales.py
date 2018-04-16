# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolssales.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PJPChanger(object):
    def setupUi(self, PJPChanger):
        PJPChanger.setObjectName("PJPChanger")
        PJPChanger.resize(341, 161)
        PJPChanger.setMinimumSize(QtCore.QSize(341, 161))
        PJPChanger.setMaximumSize(QtCore.QSize(341, 233))
        self.centralwidget = QtWidgets.QWidget(PJPChanger)
        self.centralwidget.setObjectName("centralwidget")
        self.btOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btOpen.setGeometry(QtCore.QRect(250, 10, 81, 22))
        self.btOpen.setObjectName("btOpen")
        self.edFile = QtWidgets.QLineEdit(self.centralwidget)
        self.edFile.setEnabled(False)
        self.edFile.setGeometry(QtCore.QRect(10, 10, 231, 22))
        self.edFile.setFrame(True)
        self.edFile.setReadOnly(True)
        self.edFile.setObjectName("edFile")
        self.gbSales = QtWidgets.QGroupBox(self.centralwidget)
        self.gbSales.setGeometry(QtCore.QRect(10, 40, 321, 61))
        self.gbSales.setObjectName("gbSales")
        self.cbSales = QtWidgets.QComboBox(self.gbSales)
        self.cbSales.setGeometry(QtCore.QRect(20, 23, 281, 22))
        self.cbSales.setMaximumSize(QtCore.QSize(341, 233))
        self.cbSales.setObjectName("cbSales")
        self.btSave = QtWidgets.QPushButton(self.centralwidget)
        self.btSave.setGeometry(QtCore.QRect(85, 116, 181, 31))
        self.btSave.setObjectName("btSave")
        self.lbPath = QtWidgets.QLabel(self.centralwidget)
        self.lbPath.setGeometry(QtCore.QRect(20, 100, 55, 16))
        self.lbPath.setObjectName("lbPath")
        PJPChanger.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PJPChanger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.menubar.setObjectName("menubar")
        PJPChanger.setMenuBar(self.menubar)

        self.retranslateUi(PJPChanger)
        QtCore.QMetaObject.connectSlotsByName(PJPChanger)

    def retranslateUi(self, PJPChanger):
        _translate = QtCore.QCoreApplication.translate
        PJPChanger.setWindowTitle(_translate("PJPChanger", "PJP Changer"))
        self.btOpen.setText(_translate("PJPChanger", "Open"))
        self.gbSales.setTitle(_translate("PJPChanger", "Select Salesman"))
        self.btSave.setText(_translate("PJPChanger", "Save Changes"))
        self.lbPath.setText(_translate("PJPChanger", "TextLabel"))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PJPChanger = QtWidgets.QMainWindow()
    ui = Ui_PJPChanger()
    ui.setupUi(PJPChanger)
    PJPChanger.show()
    sys.exit(app.exec_())

