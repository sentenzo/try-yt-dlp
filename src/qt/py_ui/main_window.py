# Form implementation generated from reading ui file './src/qt/ui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(345, 86)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_download_all = QtWidgets.QPushButton(self.centralwidget)
        self.pb_download_all.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pb_download_all.setObjectName("pb_download_all")
        self.gridLayout.addWidget(self.pb_download_all, 2, 0, 1, 1)
        self.le_youtube_link = QtWidgets.QLineEdit(self.centralwidget)
        self.le_youtube_link.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.le_youtube_link.setText("")
        self.le_youtube_link.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.le_youtube_link.setReadOnly(False)
        self.le_youtube_link.setObjectName("le_youtube_link")
        self.gridLayout.addWidget(self.le_youtube_link, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "yt-dpl-qt6"))
        self.pb_download_all.setText(_translate("MainWindow", "Download video"))
        self.le_youtube_link.setPlaceholderText(_translate("MainWindow", "https://www.youtube.com/watch?v=..."))
        self.label.setText(_translate("MainWindow", "Copy-paste the youtube link:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
