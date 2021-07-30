from mhyt import yt_download
from PyQt5 import QtCore, QtGui, QtWidgets
import img


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 531, 521))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 191, 41))
        self.label_3.setObjectName("label_3")
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(60, 40, 421, 20))
        self.txt_link.setObjectName("txt_link")
        self.txt_file = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_file.setGeometry(QtCore.QRect(60, 70, 421, 20))
        self.txt_file.setObjectName("txt_file")
        self.rd_mp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_mp3.setGeometry(QtCore.QRect(390, 110, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rd_mp3.setFont(font)
        self.rd_mp3.setChecked(True)
        self.rd_mp3.setObjectName("rd_mp3")
        self.rd_mp4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_mp4.setGeometry(QtCore.QRect(390, 140, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rd_mp4.setFont(font)
        self.rd_mp4.setObjectName("rd_mp4")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(170, 110, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_download.setFont(font)
        self.bt_download.setObjectName("bt_download")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(70, 170, 411, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 191, 20))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.progressBar.setValue(0)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bt_download.clicked.connect(self.download)


    def download(self):
        self.progressBar.setValue(0)
        url = self.txt_link.text()
        file = self.txt_file.text()
        if self.rd_mp4.isChecked() == True:
            file= file + ".mp4"
            yt_download(url,file)   
        else:
            file= file +".mp3"
            try:
                yt_download(url, file, ismusic=True, codec = "mp3")
            except:
                pass
        self.progressBar.setValue(100)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/3f44b992553a77e027404c7a97575148.jpg\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Link:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">File:</span></p></body></html>"))
        self.rd_mp3.setText(_translate("MainWindow", "MP3"))
        self.rd_mp4.setText(_translate("MainWindow", "MP4"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Free Download YouTube</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
