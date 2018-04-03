import os, sys, io, time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from toolspjp import Ui_MainWindow
from lxml import etree

class mainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self) :
		QMainWindow.__init__(self)
		self.setupUi(self)
		
		self.btOpen.clicked.connect(self.openXml)
		self.btSave.clicked.connect(self.saveChange)
		

		self.cbPJP.addItem("")
		self.cbPJP.addItem("0017")
		self.cbPJP.addItem("0021")
		self.cbPJP.addItem("0023")
		self.cbPJP.addItem("0033")

		self.cbSales.addItem("")
		self.cbSales.addItem("17")
		self.cbSales.addItem("21")
		self.cbSales.addItem("23")
		self.cbSales.addItem("33")

	def openXml(self):
		fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","XML Files (*.xml)")
		if fileName:
			print(fileName)
			x = QUrl.fromLocalFile(fileName).fileName()
			self.edFile.setText(x)

	def saveChange(self):
		path = self.edFile.text()
		if len(path) == 0:
			QMessageBox.warning(self, "Warning", "You Must Select File First!", QMessageBox.Ok)
		else:
			print(path)
			codePJP = self.cbPJP.currentText()
			print(codePJP)
			codeSales = self.cbSales.currentText()
			print(codeSales)
			tree = etree.parse(path)
			# root = tree.getroot()
			if len(codePJP) > 0:
				tree.find('.//RouteCode').text = codePJP
				if len(codeSales) > 0:
					tree.find('.//SalesmanCode').text = codeSales
				else:
					QMessageBox.warning(self, "Warning", "Salesman Code Must Be Selected!", QMessageBox.Ok)
			else:
				QMessageBox.warning(self, "Warning", "PJP Code Must Be Selected!", QMessageBox.Ok)
			if len(codePJP) > 0 and len(codeSales) > 0:
				tree.write(path, xml_declaration=True, encoding='utf-8', method="xml")
				QMessageBox.information(self, "Information", "Success!", QMessageBox.Ok)

		


if __name__ == '__main__' :
    app = QApplication(sys.argv)

    window = mainWindow()
    window.show()

    sys.exit(app.exec_())