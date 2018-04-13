import os, sys, io, time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from toolssales import Ui_PJPChanger
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

        # Set database result as global variabel
        self.rowData = self.getData()

        for rSales in self.rowData:
            self.cbSales.addItem(rSales[2], rSales[1])

        # for rPJP in row:
        #     x = "{:0>4}".format(rPJP[0])
        #     self.cbPJP.addItem(x)
        # end of Getting Data Section

        self.lbPath.hide()
        self.btOpen.clicked.connect(self.openXml)
        self.btSave.clicked.connect(self.saveChange)
        self.edFile.textChanged.connect(self.setItem)

    def getData(self):
        # Getting Data Section
        server = 'localhost\SQLEXPRESS'
        database = 'Centegy_SnDPro_UID'
        username = 'sa'
        password = 'unilever1'

        try:
            cnxn = pyodbc.connect(driver='{ODBC Driver 13 for SQL Server}',
                                  server=server,
                                  database=database,
                                  uid=username,
                                  pwd=password,
                                  timeout=5)

            cnxn.setencoding(encoding='utf-8', ctype=pyodbc.SQL_CHAR)
            cursor = cnxn.cursor()
        except pyodbc.Error as err :
            self.hide()
            QMessageBox.critical(self, "Error", "Can't connect to database server.", QMessageBox.Abort)
            raise SystemExit(0)

        cursor.execute("SELECT PJP, DSR, LDESC FROM PJP_HEAD")

        results = cursor.fetchall()

        return results


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
            # self.cbPJP.setCurrentIndex(0)
            self.cbSales.setCurrentIndex(0)
        else:
            tree = etree.parse(path)
            vPJP = tree.find('.//RouteCode').text
            vSales = tree.find('.//SalesmanCode').text

            # get text of combobox, set it with same value of XML file
            # indexPJP = self.cbPJP.findText(vPJP)
            # if indexPJP >= 0:
            #     self.cbPJP.setCurrentIndex(indexPJP)

            # get value of combobox, set it with same value of XML file
            indexSales = self.cbSales.findData(vSales)
            if indexSales >= 0:
                self.cbSales.setCurrentIndex(indexSales)
        # End of def setItem.


    def saveChange(self):
        # Get Path from hidden label
        path = self.lbPath.text()

        if len(path) == 0:
            QMessageBox.warning(self, "Warning", "You Must Select File First!", QMessageBox.Ok)
        else:
            # Put Value in variable
            # codePJP = self.cbPJP.currentText()
            codeSales = str(self.cbSales.itemData(self.cbSales.currentIndex()))
            nameSales = str(self.cbSales.currentText())

            # Parsing file xml
            tree = etree.parse(path)

            # Validating the value before make any change
            if len(codeSales) > 0:
                suffix = "ORD"

                arrayRowData = np.array(self.rowData)
                rowFilter = np.where(arrayRowData[:,2] == nameSales)
                resultFilter = arrayRowData[rowFilter]
                tmp = resultFilter[:,0]
                # format 4 Digit
                codePJP = "{:0>4}".format(tmp[0])

                # RouteCode
                tree.find('.//RouteCode').text = codePJP

                # BillToCustomer
                tree.find('.//BillToCustomer').text = codePJP

                # DocumentPrefix
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