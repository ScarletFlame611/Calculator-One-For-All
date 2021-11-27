# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'number_systems.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NumberSystems(object):
    def setupUi(self, NumberSystems):
        NumberSystems.setObjectName("NumberSystems")
        NumberSystems.resize(1050, 798)
        NumberSystems.setStyleSheet("#centralwidget { \n"
"            background-image:url(\"pic1.jpg\"); background-position: center;}")
        self.centralwidget = QtWidgets.QWidget(NumberSystems)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.first_number = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_number.sizePolicy().hasHeightForWidth())
        self.first_number.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.first_number.setFont(font)
        self.first_number.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 10px;")
        self.first_number.setText("")
        self.first_number.setObjectName("first_number")
        self.horizontalLayout.addWidget(self.first_number)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.group1 = QtWidgets.QButtonGroup(NumberSystems)
        self.group1.setObjectName("group1")
        self.group1.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.group1.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.group1.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.group1.addButton(self.radioButton_4)
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.group1.addButton(self.radioButton_5)
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.group1.addButton(self.radioButton_6)
        self.verticalLayout.addWidget(self.radioButton_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.other1 = QtWidgets.QLineEdit(self.centralwidget)
        self.other1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.other1.setFont(font)
        self.other1.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 10px;")
        self.other1.setText("")
        self.other1.setObjectName("other1")
        self.verticalLayout.addWidget(self.other1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.group2 = QtWidgets.QButtonGroup(NumberSystems)
        self.group2.setObjectName("group2")
        self.group2.addButton(self.radioButton_7)
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.group2.addButton(self.radioButton_8)
        self.verticalLayout_2.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setObjectName("radioButton_9")
        self.group2.addButton(self.radioButton_9)
        self.verticalLayout_2.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setObjectName("radioButton_10")
        self.group2.addButton(self.radioButton_10)
        self.verticalLayout_2.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setObjectName("radioButton_11")
        self.group2.addButton(self.radioButton_11)
        self.verticalLayout_2.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")
        self.group2.addButton(self.radioButton_12)
        self.verticalLayout_2.addWidget(self.radioButton_12)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.other2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.other2.setFont(font)
        self.other2.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 10px;")
        self.other2.setObjectName("other2")
        self.verticalLayout_2.addWidget(self.other2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.result_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.result_btn.setFont(font)
        self.result_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.result_btn.setAutoFillBackground(False)
        self.result_btn.setStyleSheet("min-width:  196px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(124, 16, 255, 255), stop:1 rgba(205, 6, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"    max-width:  196px;\n"
"    min-height: 50px;\n"
"    max-height: 50px;\n"
"    border-radius: 24px;\n"
"border: 4px groove rgb(170, 0, 255);")
        self.result_btn.setAutoDefault(False)
        self.result_btn.setDefault(False)
        self.result_btn.setFlat(False)
        self.result_btn.setObjectName("result_btn")
        self.verticalLayout_5.addWidget(self.result_btn, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.result_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_line.sizePolicy().hasHeightForWidth())
        self.result_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.result_line.setFont(font)
        self.result_line.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 10px;")
        self.result_line.setObjectName("result_line")
        self.horizontalLayout_2.addWidget(self.result_line)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.csv_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.csv_btn.setFont(font)
        self.csv_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.csv_btn.setStyleSheet("border: 4px groove rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(124, 16, 255, 255), stop:1 rgba(205, 6, 255, 255));\n"
" min-height: 40px;\n"
" min-width: 40px;")
        self.csv_btn.setObjectName("csv_btn")
        self.gridLayout.addWidget(self.csv_btn, 0, 3, 1, 1, QtCore.Qt.AlignTop)
        NumberSystems.setCentralWidget(self.centralwidget)

        self.retranslateUi(NumberSystems)
        QtCore.QMetaObject.connectSlotsByName(NumberSystems)

    def retranslateUi(self, NumberSystems):
        _translate = QtCore.QCoreApplication.translate
        NumberSystems.setWindowTitle(_translate("NumberSystems", "Системы счисления"))
        self.label.setText(_translate("NumberSystems", "Введите число:"))
        self.label_2.setText(_translate("NumberSystems", "Система счисления:"))
        self.radioButton.setText(_translate("NumberSystems", "Двоичная"))
        self.radioButton_2.setText(_translate("NumberSystems", "Троичная"))
        self.radioButton_3.setText(_translate("NumberSystems", "Восьмеричная"))
        self.radioButton_4.setText(_translate("NumberSystems", "Десятичная"))
        self.radioButton_5.setText(_translate("NumberSystems", "Шестнадцатеричная"))
        self.radioButton_6.setText(_translate("NumberSystems", "Другая"))
        self.label_3.setText(_translate("NumberSystems", "Перевести в:"))
        self.radioButton_7.setText(_translate("NumberSystems", "Двоичная"))
        self.radioButton_8.setText(_translate("NumberSystems", "Троичная"))
        self.radioButton_9.setText(_translate("NumberSystems", "Восьмеричная"))
        self.radioButton_10.setText(_translate("NumberSystems", "Десятичная"))
        self.radioButton_11.setText(_translate("NumberSystems", "Шестнадцатеричная"))
        self.radioButton_12.setText(_translate("NumberSystems", "Другая"))
        self.result_btn.setText(_translate("NumberSystems", "Перевести"))
        self.label_4.setText(_translate("NumberSystems", "    Результат:    "))
        self.csv_btn.setText(_translate("NumberSystems", "CSV"))