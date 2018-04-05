import os, sys, io, time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from toolspjp import Ui_MainWindow
from lxml import etree
import pyodbc

class mainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self) :
		QMainWindow.__init__(self)
		self.setupUi(self)

		server = 'den1.mssql4.gear.host'
		database = 'sqlsrv'
		username = 'sqlsrv'
		password = 'terserah!'

		try:
			cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password, timeout=2)

			cnxn.setencoding(encoding='utf-8', ctype=pyodbc.SQL_CHAR)
			cursor = cnxn.cursor()
		except pyodbc.Error as err :
			QMessageBox.critical(self, "Error", "Can't connect to server.", QMessageBox.Abort)
			raise SystemExit(0)

		cursor.execute("SELECT PJP, DSR, LDESC FROM PJP_HEAD")
		row = cursor.fetchall()
		print(row)

		for rSales in row:
			self.cbSales.addItem(rSales[2], rSales[1])

		for rPJP in row:
			x = "{:0>4}".format(rPJP[0])
			self.cbPJP.addItem(x)

		self.btOpen.clicked.connect(self.openXml)
		self.btSave.clicked.connect(self.saveChange)


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
			codeSales = str(self.cbSales.itemData(self.cbSales.currentIndex()))
			print(codeSales)
			tree = etree.parse(path)
			# root = tree.getroot()
			if len(codePJP) > 0:
				suffix = "ORD"

				tree.find('.//RouteCode').text = codePJP

				for node in tree.xpath(".//DocumentPrefix"):
					node.text = codePJP + suffix

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