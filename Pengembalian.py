# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pengembalian.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()


class Ui_Balikin(object):
    def setupUi(self, Balikin):
        Balikin.setObjectName("Balikin")
        Balikin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Balikin)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 70, 681, 441))
        self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(150, 20, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(50, 100, 581, 281))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.No_Surat = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.No_Surat.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.No_Surat.setText("")
        self.No_Surat.setClearButtonEnabled(False)
        self.No_Surat.setObjectName("No_Surat")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.No_Surat)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.NIP = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NIP.setEnabled(False)
        self.NIP.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.NIP.setInputMethodHints(QtCore.Qt.ImhTime)
        self.NIP.setText("")
        self.NIP.setClearButtonEnabled(False)
        self.NIP.setObjectName("NIP")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NIP)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.ID_Barang = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ID_Barang.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.ID_Barang.setText("")
        self.ID_Barang.setClearButtonEnabled(False)
        self.ID_Barang.setObjectName("ID_Barang")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ID_Barang)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Pilih_Gedung = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.Pilih_Gedung.setFont(font)
        self.Pilih_Gedung.setObjectName("Pilih_Gedung")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Pilih_Gedung)
        self.No_Ruangan = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.No_Ruangan.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.No_Ruangan.setText("")
        self.No_Ruangan.setClearButtonEnabled(False)
        self.No_Ruangan.setObjectName("No_Ruangan")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.No_Ruangan)
        self.Input = QtWidgets.QPushButton(self.frame)
        self.Input.setGeometry(QtCore.QRect(480, 240, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Input.setAutoDefault(False)
        self.Input.setDefault(False)
        self.Input.setFlat(False)
        self.Input.setObjectName("Input")
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
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("icon/BackIcon.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label.raise_()
        self.frame.raise_()
        self.label_9.raise_()
        self.BackButton.raise_()
        Balikin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Balikin)
        self.statusbar.setObjectName("statusbar")
        Balikin.setStatusBar(self.statusbar)

        self.retranslateUi(Balikin)
        QtCore.QMetaObject.connectSlotsByName(Balikin)

        #code here
        self.Input.clicked.connect(self.Inputin)

    def retranslateUi(self, Balikin):
        _translate = QtCore.QCoreApplication.translate
        Balikin.setWindowTitle(_translate("Balikin", "Pengembalian"))
        self.label.setText(_translate("Balikin", "Form Pengembalian"))
        self.label_2.setText(_translate("Balikin", "No. Surat"))
        self.No_Surat.setPlaceholderText(_translate("Balikin", "No. Surat Peminjaman"))
        self.label_3.setText(_translate("Balikin", "NIP"))
        self.NIP.setText(_translate("Minjam", f'{self.ID}'))
        self.NIP.setPlaceholderText(_translate("Balikin", "NIP"))
        self.label_4.setText(_translate("Balikin", "ID_Barang"))
        self.ID_Barang.setPlaceholderText(_translate("Balikin", "ID_Barang"))
        self.label_8.setText(_translate("Balikin", "Lokasi Barang"))
        self.Pilih_Gedung.setCurrentText(_translate("Balikin", "- Pilih Gedung -"))
        self.Pilih_Gedung.setItemText(0, _translate("Balikin", "- Pilih Gedung -"))
        self.Pilih_Gedung.setItemText(1, _translate("Balikin", "A"))
        self.Pilih_Gedung.setItemText(2, _translate("Balikin", "B"))
        self.Pilih_Gedung.setItemText(3, _translate("Balikin", "C"))
        self.Pilih_Gedung.setItemText(4, _translate("Balikin", "D"))
        self.Pilih_Gedung.setItemText(5, _translate("Balikin", "E"))
        self.Pilih_Gedung.setItemText(6, _translate("Balikin", "F"))
        self.Pilih_Gedung.setItemText(7, _translate("Balikin", "GKU"))
        self.Pilih_Gedung.setItemText(8, _translate("Balikin", "Labtek1"))
        self.Pilih_Gedung.setItemText(9, _translate("Balikin", "Labtek2"))
        self.Pilih_Gedung.setItemText(10, _translate("Balikin", "Labtek3"))
        self.No_Ruangan.setPlaceholderText(_translate("Balikin", "Nomor Ruang"))
        self.Input.setText(_translate("Balikin", "Input"))

    def getMeAName(self,username):
        self.username=username
        mycursor.execute("Select NIP from login_info where username  = '" + self.username + "\'")
        result = mycursor.fetchall()
        self.ID = (result[0])[0]
        print(self.ID)

    def Inputin(self):
        print("Bakal Nerima Data")
        #terima data
        self.No_Surat.text()
        self.NIP.text()
        self.ID_Barang.text()
        self.Pilih_Gedung.currentText()
        self.No_Ruangan.text()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Balikin = QtWidgets.QMainWindow()
    ui = Ui_Balikin()
    ui.getMeAName("Don")
    ui.setupUi(Balikin)
    Balikin.show()
    sys.exit(app.exec_())
