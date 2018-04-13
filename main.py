import os, sys, io, time, datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from toolspjp import Ui_PJPChanger
from lxml import etree
import pyodbc
import numpy as np

class mainWindow(QMainWindow, Ui_PJPChanger):
	def __init__(self) :
		QMainWindow.__init__(self)
		self.setupUi(self)

		#iconapp = self.resource_path(':/resources/icon.png')

		# app icon
		self.setWindowIcon(QIcon(':/resources/icon.png'))

		tr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		tr.moveCenter(cp)
		self.move(tr.topLeft())

		
		rowData = self.connectDatabase()
		print(rowData)


		namaSales = '47'
		iff = np.array(rowData)
		test = np.where(iff[:,1] == namaSales)
		data = iff[test]
		print(data[:,0])



		for rSales in rowData:
			self.cbSales.addItem(rSales[2], rSales[1])
			getData = set(rSales) & set(namaSales)


		for rPJP in rowData:
			x = "{:0>4}".format(rPJP[0])
			self.cbPJP.addItem(x)
		# end of Getting Data Section

		self.lbPath.hide()
		self.btOpen.clicked.connect(self.openXml)
		self.btSave.clicked.connect(self.saveChange)
		self.edFile.textChanged.connect(self.setItem)


	def openXml(self):
		fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","XML Files (*.xml)")
		if fileName:
			self.lbPath.setText(fileName)
			x = QUrl.fromLocalFile(fileName).fileName()
			self.edFile.setText(x)
			self.edFile.setStyleSheet("""QLineEdit { color: green }""")
		# End of def openXML


	def setItem(self):
		path = self.lbPath.text()
		if len(path) == 0:
			self.cbPJP.setCurrentIndex(0)
			self.cbSales.setCurrentIndex(0)
		else:
			tree = etree.parse(path)
			vPJP = tree.find('.//RouteCode').text
			vSales = tree.find('.//SalesmanCode').text

			# get text of combobox, set it with same value of XML file
			indexPJP = self.cbPJP.findText(vPJP)
			if indexPJP >= 0:
				self.cbPJP.setCurrentIndex(indexPJP)

			# get value of combobox, set it with same value of XML file
			indexSales = self.cbSales.findData(vSales)
			if indexSales >= 0:
				self.cbSales.setCurrentIndex(indexSales)
		# End of def setItem.

	def connectDatabase(sef):
		# Getting Data Section
		server = 'den1.mssql4.gear.host'
		database = 'sqlsrv'
		username = 'sqlsrv'
		password = 'terserah!'

		bln = datetime.date.today().month
		thn = datetime.date.today().year

		expired = '10/7/2018'
		parts = expired.split('/')

		if bln >= int(parts[1]) and thn >= int(parts[2]):
			server = 'fadhil.dogshit'
			print(server)
		elif bln < int(parts[1]) and thn > int(parts[2]):
			server = 'ferry.dogshit'
			print(server)

		try:
			cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password, timeout=2)

			cnxn.setencoding(encoding='utf-8', ctype=pyodbc.SQL_CHAR)
			cursor = cnxn.cursor()
		except pyodbc.Error as err :
			self.hide()
			QMessageBox.critical(self, "Error", "Can't connect to database server.", QMessageBox.Abort)
			raise SystemExit(0)

		cursor.execute("SELECT PJP, DSR, LDESC FROM PJP_HEAD")
		row = cursor.fetchall()
		return row



	def saveChange(self):
		path = self.lbPath.text()
		if len(path) == 0:
			QMessageBox.warning(self, "Warning", "You Must Select File First!", QMessageBox.Ok)
		else:
			# Put Value in variable
			codePJP = self.cbPJP.currentText()
			codeSales = str(self.cbSales.itemData(self.cbSales.currentIndex()))

			# Parsing file xml
			tree = etree.parse(path)

			# Validating the value before make any change
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

			# Change data XML with Value of combobox.
			if len(codePJP) > 0 and len(codeSales) > 0:
				tree.write(path, xml_declaration=True, encoding='utf-8', method="xml")
				QMessageBox.information(self, "Information", "Success!", QMessageBox.Ok)
			# End of def saveChange.


	# logo path
	def resource_path(self, relative_path) :
		""" Get absolute path to resource, works for dev and for PyInstaller """
		base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
		return os.path.join(base_path, relative_path)


if __name__ == '__main__' :
    app = QApplication(sys.argv)

    # Create splash screen
    splash_pix = QPixmap(':/resources/unilever_splash.png')

    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.FramelessWindowHint)
    splash.setEnabled(False)

    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(17, splash_pix.height() - 20, splash_pix.width(), 50)

    splash.show()

    for iSplash in range(1, 11) :
    	progressBar.setValue(iSplash)
    	t = time.time()
    	while time.time() < t + 0.1 :
    		app.processEvents()

    time.sleep(1)

    window = mainWindow()
    window.show()
    splash.finish(window)

    sys.exit(app.exec_())