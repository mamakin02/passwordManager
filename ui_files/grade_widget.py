# Form implementation generated from reading ui file 'password_grade.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PasswordGrade(object):
    def setupUi(self, PasswordGrade):
        PasswordGrade.setObjectName("PasswordGrade")
        PasswordGrade.resize(584, 472)
        self.EditGrade = QtWidgets.QLineEdit(parent=PasswordGrade)
        self.EditGrade.setGeometry(QtCore.QRect(150, 130, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EditGrade.setFont(font)
        self.EditGrade.setText("")
        self.EditGrade.setObjectName("EditGrade")
        self.labelgrade = QtWidgets.QLabel(parent=PasswordGrade)
        self.labelgrade.setGeometry(QtCore.QRect(190, 280, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelgrade.setFont(font)
        self.labelgrade.setText("")
        self.labelgrade.setObjectName("labelgrade")
        self.btnGrade = QtWidgets.QPushButton(parent=PasswordGrade)
        self.btnGrade.setGeometry(QtCore.QRect(240, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnGrade.setFont(font)
        self.btnGrade.setObjectName("btnGrade")
        self.passwordLabel = QtWidgets.QLabel(parent=PasswordGrade)
        self.passwordLabel.setGeometry(QtCore.QRect(70, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.btnBack = QtWidgets.QPushButton(parent=PasswordGrade)
        self.btnBack.setGeometry(QtCore.QRect(0, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")

        self.retranslateUi(PasswordGrade)
        QtCore.QMetaObject.connectSlotsByName(PasswordGrade)

    def retranslateUi(self, PasswordGrade):
        _translate = QtCore.QCoreApplication.translate
        PasswordGrade.setWindowTitle(_translate("PasswordGrade", "Оценка Пароля"))
        self.btnGrade.setText(_translate("PasswordGrade", "Запуск"))
        self.passwordLabel.setText(_translate("PasswordGrade", "Пароль:"))
        self.btnBack.setText(_translate("PasswordGrade", "<-"))