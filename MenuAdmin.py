# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import Perolehan
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuAdmin(object):
    def setupUi(self, MenuAdmin):
        MenuAdmin.setObjectName("MenuAdmin")
        MenuAdmin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MenuAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 70, 681, 441))
        self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(150, 40, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 150, 581, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Lihat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Lihat.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Lihat.setObjectName("Lihat")
        self.verticalLayout.addWidget(self.Lihat)

        self.PerolehanBarang = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PerolehanBarang.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.PerolehanBarang.setObjectName("PerolehanBarang")
        self.verticalLayout.addWidget(self.PerolehanBarang)

        self.Expert = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Expert.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Expert.setObjectName("Expert")
        self.verticalLayout.addWidget(self.Expert)

        self.BackButton = QtWidgets.QPushButton(self.groupBox)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setKerning(False)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.BackButton.setMouseTracking(False)
        self.BackButton.setAutoFillBackground(False)
        self.BackButton.setStyleSheet("color: rgb(170, 255, 255);\n"
"background-color: transparent;\n"
"")
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")

        self.BackIcon = QtWidgets.QLabel(self.groupBox)
        self.BackIcon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.BackIcon.setText("")
        self.BackIcon.setPixmap(QtGui.QPixmap("icon/LogOut.png"))
        self.BackIcon.setScaledContents(True)
        self.BackIcon.setObjectName("BackIcon")
        self.label.raise_()

        self.verticalLayoutWidget.raise_()
        self.BackIcon.raise_()
        self.BackButton.raise_()
        MenuAdmin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MenuAdmin)
        self.statusbar.setObjectName("statusbar")
        MenuAdmin.setStatusBar(self.statusbar)

        #code here
        print(self.username)
        #Lihat
        self.Lihat.clicked.connect(self.lihatingedung)
        #perolehan
        self.PerolehanBarang.clicked.connect(lambda: self.gotoPerolehan(MenuAdmin))
        #ExpertMode
        self.Expert.clicked.connect(self.gotoExpert)

        self.retranslateUi(MenuAdmin)
        QtCore.QMetaObject.connectSlotsByName(MenuAdmin)

    def retranslateUi(self, MenuAdmin):
        _translate = QtCore.QCoreApplication.translate
        MenuAdmin.setWindowTitle(_translate("MenuAdmin", "MenuAdmin"))
        self.label.setText(_translate("MenuAdmin", "Menu Admin"))
        self.Lihat.setText(_translate("MenuAdmin", "Lihat Data Inventaris Gedung"))
        self.PerolehanBarang.setText(_translate("MenuAdmin", "Terima Inventaris"))
        self.Expert.setText(_translate("MenuAdmin", "Mode Expert"))

    def getMeAName(self,username):
        self.username=username

    def lihatingedung(self):
        print("Program ngelihatin inventaris gedung")
        pass

    def gotoPerolehan(self,MenuAdmin):
        print("Program akan menerima barang")
        pass
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = Perolehan.Ui_Perolehan()
        self.ui.getMeAName(self.username)
        self.ui.setupUi(self.SubMenu)
        self.SubMenu.show()
        MenuAdmin.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Muncullah(MenuAdmin))

    def gotoExpert(self):
        print("Program akan menampilkan mode expert")
        pass

    def Muncullah(self,MenuAdmin):
        self.SubMenu.hide()
        MenuAdmin.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuAdmin = QtWidgets.QMainWindow()
    ui = Ui_MenuAdmin()
    ui.getMeAName("admin")
    ui.setupUi(MenuAdmin)
    MenuAdmin.show()
    sys.exit(app.exec_())
