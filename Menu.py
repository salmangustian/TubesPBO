# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import Peminjaman
import Pengembalian
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(800, 600)
        Menu.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 70, 681, 441))
        self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(250, 40, 181, 81))
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

        self.Pinjam = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Pinjam.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Pinjam.setObjectName("Pinjam")
        self.verticalLayout.addWidget(self.Pinjam)

        self.BalikinBarang = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BalikinBarang.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.BalikinBarang.setObjectName("BalikinBarang")
        self.verticalLayout.addWidget(self.BalikinBarang)

        self.Lihat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Lihat.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Lihat.setObjectName("Lihat")
        self.verticalLayout.addWidget(self.Lihat)

        self.BackIcon = QtWidgets.QLabel(self.groupBox)
        self.BackIcon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.BackIcon.setText("")
        self.BackIcon.setPixmap(QtGui.QPixmap("icon/LogOut.png"))
        self.BackIcon.setScaledContents(True)
        self.BackIcon.setObjectName("BackIcon")

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
        Menu.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)

        #code here
        print(self.username)

        #Pinjam
        self.Pinjam.clicked.connect(lambda: self.GotoPinjam(Menu))

        #Balikin
        self.BalikinBarang.clicked.connect(lambda: self.GotoBalikin(Menu))

        #Lihat
        self.Lihat.clicked.connect(lambda: self.GotoLihat(Menu))


        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.label.setText(_translate("Menu", "Menu"))
        self.Pinjam.setText(_translate("Menu", "Pinjam Barang"))
        self.BalikinBarang.setText(_translate("Menu", "Kembalikan Barang pinjaman"))
        self.Lihat.setText(_translate("Menu", "Lihat Data Barang Pinjaman"))

    def getMeAName(self,username):
        self.username=username

    def GotoPinjam(self,Menu):
        print("Pinjam")
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = Peminjaman.Ui_Minjam()
        self.ui.getMeAName(self.username)
        self.ui.setupUi(self.SubMenu)
        self.SubMenu.show()
        Menu.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Muncullah(Menu))

    def GotoBalikin(self,Menu):
        print("Balikin")
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = Pengembalian.Ui_Balikin()
        self.ui.getMeAName(self.username)
        self.ui.setupUi(self.SubMenu)
        self.SubMenu.show()
        Menu.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Muncullah(Menu))

    def GotoLihat(self,Menu):
        print("Lihat")
        pass

    def Muncullah(self,Menu):
        self.SubMenu.hide()
        Menu.show()

    # def Muncullah(self):
    #     CallMenu()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.getMeAName("Don")
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
