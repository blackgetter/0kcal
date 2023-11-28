# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TodayDiet.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import cv2

class Ui_DietWidget(object):
    def __init__(self):
        self.count = 0
        self.total_nut = [0,0,0,0,0,0]
        self.database = []
        self.food_img = []

    def setData(self, foodInfo: list, foodImg: list):
        # foodInfo : list of list(
        # day(eg.11271618) food_name serving calcorie carbo protein fat sugar sodium imgsize emptyspace) total 11
        # foodImg : list of Mat img
        self.count = len(foodInfo)
        self.database = []
        self.food_img = []
        for i in range(len(foodInfo)):
            self.temp = []
            self.food_img.append(foodImg[i])
            for j in range(len(foodInfo[i])-2):
                if 3 <= j and j <= 8:
                    self.total_nut[j-3] += float(foodInfo[i][j])
                self.temp.append(foodInfo[i][j])
            self.database.append(self.temp)


    def setMealFrame(self, addr, x, y):
        meal = QtWidgets.QFrame(self.frame)
        meal.setGeometry(QtCore.QRect(x, y, 671, 211))
        meal.setFrameShadow(QtWidgets.QFrame.Raised)
        meal.setObjectName("meal")
        meal.setStyleSheet( "background-color:white;\n"
        "border-radius:5px;\n")
        meal_pic = QtWidgets.QLabel(meal)
        meal_pic.setGeometry(QtCore.QRect(20, 10, 241, 191))
        meal_pic.setText("")

        height, width, channel = addr.shape
        bytes_per_line = 3 * width
        addr = cv2.cvtColor(addr, cv2.COLOR_BGR2RGB)
        q_image = QImage(addr.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        new_pixmap = pixmap.scaled(241,191)
        meal_pic.setPixmap(QtGui.QPixmap(new_pixmap))
        meal_pic.setObjectName("meal_pic")

        meal_name = QtWidgets.QLineEdit(meal)
        meal_name.setGeometry(QtCore.QRect(290, 45, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        meal_name.setFont(font)
        meal_name.setStyleSheet("font-size:18px;")
        meal_name.setFrame(False)
        meal_name.setObjectName("meal_name")
        meal_info = QtWidgets.QTableWidget(meal)
        meal_info.setGeometry(QtCore.QRect(290, 100, 362, 51))
        meal_info.setStyleSheet("background-color:rgb(50,150,150);"
        "border-radius:1px;\n"
        "color:white;")
        meal_info.setGridStyle(QtCore.Qt.NoPen)
        meal_info.setWordWrap(True)
        meal_info.setRowCount(1)
        meal_info.setColumnCount(3)
        meal_info.setObjectName("meal_info")
        item = QtWidgets.QTableWidgetItem()
        meal_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        meal_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        meal_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        meal_info.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        meal_info.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        meal_info.setItem(0, 2, item)
        meal_info.horizontalHeader().setVisible(True)
        meal_info.horizontalHeader().setDefaultSectionSize(120)
        meal_info.horizontalHeader().setMinimumSectionSize(60)
        meal_info.verticalHeader().setVisible(False)
        meal_info.verticalHeader().setDefaultSectionSize(31)
        meal_info.verticalHeader().setHighlightSections(True)
        meal_info.verticalHeader().setMinimumSectionSize(20)
        meal_info2 = QtWidgets.QTableWidget(meal)
        meal_info2.setGeometry(QtCore.QRect(290, 150, 362, 51))
        meal_info2.setStyleSheet("background-color:rgb(50,150,150);"
        "border-radius:1px;\n"
        "color:white;")
        meal_info2.setGridStyle(QtCore.Qt.NoPen)
        meal_info2.setWordWrap(True)
        meal_info2.setRowCount(1)
        meal_info2.setColumnCount(3)
        meal_info2.setObjectName("meal_info")
        item = QtWidgets.QTableWidgetItem()
        meal_info2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        meal_info2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        meal_info2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        meal_info2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        meal_info2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        meal_info2.setItem(0, 2, item)
        meal_info2.horizontalHeader().setVisible(True)
        meal_info2.horizontalHeader().setDefaultSectionSize(120)
        meal_info2.horizontalHeader().setMinimumSectionSize(60)
        meal_info2.verticalHeader().setVisible(False)
        meal_info2.verticalHeader().setDefaultSectionSize(31)
        meal_info2.verticalHeader().setHighlightSections(True)
        meal_info2.verticalHeader().setMinimumSectionSize(20)
        meal_vol = QtWidgets.QLineEdit(meal)
        meal_vol.setGeometry(QtCore.QRect(290, 71, 101, 20))
        font = QtGui.QFont()
        font.setBold(False)
        meal_vol.setFont(font)
        meal_vol.setFrame(False)
        meal_vol.setObjectName("meal_vol")
        meal_time = QtWidgets.QLineEdit(meal)
        meal_time.setGeometry(QtCore.QRect(290, 14, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        meal_time.setFont(font)
        meal_time.setStyleSheet("font-size:12px;")
        meal_time.setFrame(False)
        meal_time.setObjectName("meal_time")

        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)

        self.meals_pic.append(meal_pic)
        self.meals_name.append(meal_name)
        self.meals_time.append(meal_time)
        self.meals_vol.append(meal_vol)
        self.meals_info.append(meal_info)
        self.meals_info2.append(meal_info2)

    def setupUi(self, TodayDietWindow):
        TodayDietWindow.setObjectName("TodayDietWindow")
        TodayDietWindow.resize(870, 770)
        self.centralwidget = QtWidgets.QWidget(TodayDietWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(80, 80, 700, 500))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setSizeIncrement(QtCore.QSize(0, 390))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color:rgb(225,230,230);\n")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -2, 696, 500))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 2000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 2000))
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.meals = []
        self.meals_pic = []
        self.meals_is = []
        self.meals_name = []
        self.meals_time = []
        self.meals_vol = []
        self.meals_info = []
        self.meals_info2 = []

        x = 10
        for i in range(self.count):
            if len(self.food_img) == self.count:
                self.setMealFrame(self.food_img[i], 10, x)
                x += 220

        self.total_info = QtWidgets.QTableWidget(self.centralwidget)
        self.total_info.setGeometry(QtCore.QRect(68, 600, 722, 50))
        self.total_info.setStyleSheet("background-color:rgb(200,200,200);\n")
        self.total_info.setGridStyle(QtCore.Qt.NoPen)
        self.total_info.setWordWrap(True)
        self.total_info.setRowCount(1)
        self.total_info.setColumnCount(6)
        self.total_info.setObjectName("total_info")

        item = QtWidgets.QTableWidgetItem()
        self.total_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_info.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_info.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.total_info.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.total_info.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.total_info.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.total_info.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.total_info.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.total_info.setItem(0, 5, item)
        self.total_info.horizontalHeader().setVisible(True)
        self.total_info.horizontalHeader().setDefaultSectionSize(120)
        self.total_info.horizontalHeader().setMinimumSectionSize(60)
        self.total_info.verticalHeader().setVisible(False)
        self.total_info.verticalHeader().setCascadingSectionResizes(False)
        self.total_info.verticalHeader().setDefaultSectionSize(10)
        self.total_info.verticalHeader().setHighlightSections(True)
        self.total_info.verticalHeader().setMinimumSectionSize(20)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 50, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.total_info.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(TodayDietWindow)
        QtCore.QMetaObject.connectSlotsByName(TodayDietWindow)

    def retranslateUi(self, TodayDietWindow):
        _translate = QtCore.QCoreApplication.translate
        TodayDietWindow.setWindowTitle(_translate("TodayDietWindow", "MainWindow"))
        item = self.total_info.horizontalHeaderItem(0)
        item.setText(_translate("TodayDietWindow", "Calories[kcal]"))
        item = self.total_info.horizontalHeaderItem(1)
        item.setText(_translate("TodayDietWindow", "Carbo[g]"))
        item = self.total_info.horizontalHeaderItem(2)
        item.setText(_translate("TodayDietWindow", "Protein[g]"))
        item = self.total_info.horizontalHeaderItem(3)
        item.setText(_translate("TodayDietWindow", "Fat[g]"))
        item = self.total_info.horizontalHeaderItem(4)
        item.setText(_translate("TodayDietWindow", "Sugar[g]"))
        item = self.total_info.horizontalHeaderItem(5)
        item.setText(_translate("TodayDietWindow", "Sodium[g]"))
        __sortingEnabled = self.total_info.isSortingEnabled()
        self.total_info.setSortingEnabled(False)
        item = self.total_info.item(0, 0)
        item.setText(_translate("TodayDietWindow", str(self.total_nut[0])))
        item = self.total_info.item(0, 1)
        item.setText(_translate("TodayDietWindow", str(self.total_nut[1])))
        item = self.total_info.item(0, 2)
        item.setText(_translate("TodayDietWindow", str(self.total_nut[2])))
        item = self.total_info.item(0, 3)
        item.setText(_translate("TodayDietWindow", str(self.total_nut[3])))
        item = self.total_info.item(0, 4)
        item.setText(_translate("TodayDietWindow", str(self.total_nut[4])))
        item = self.total_info.item(0, 5)
        item.setText(_translate("TodayDietWindow", str(self.total_nut[5])))
        self.total_info.setSortingEnabled(__sortingEnabled)

        if self.count == len(self.database):
            for i in range(self.count):
                self.meals_time[i].setText(_translate("TodayDietWindow", self.database[i][0][0:2]+" / "\
                +self.database[i][0][2:4]+"   "+self.database[i][0][4:6]+":"+self.database[i][0][6:8]))
                self.meals_name[i].setText(_translate("TodayDietWindow", self.database[i][1]))
                self.meals_vol[i].setText(_translate("TodayDietWindow", self.database[i][2]+" serving"))
                item = self.meals_info[i].horizontalHeaderItem(0)
                item.setText(_translate("TodayDietWindow", "Carbo[g]"))
                item = self.meals_info[i].horizontalHeaderItem(1)
                item.setText(_translate("TodayDietWindow", "Protein[g]"))
                item = self.meals_info[i].horizontalHeaderItem(2)
                item.setText(_translate("TodayDietWindow", "Fat[g]"))
                __sortingEnabled = self.meals_info[0].isSortingEnabled()
                self.meals_info[i].setSortingEnabled(False)
                item = self.meals_info[i].item(0, 0)
                item.setText(_translate("TodayDietWindow", self.database[i][3]))
                item = self.meals_info[i].item(0, 1)
                item.setText(_translate("TodayDietWindow", self.database[i][4]))
                item = self.meals_info[i].item(0, 2)
                item.setText(_translate("TodayDietWindow", self.database[i][5]))

                self.meals_info2[i].setSortingEnabled(__sortingEnabled)
                item = self.meals_info2[i].horizontalHeaderItem(0)
                item.setText(_translate("TodayDietWindow", "Calories[kcal]"))
                item = self.meals_info2[i].horizontalHeaderItem(1)
                item.setText(_translate("TodayDietWindow", "Sugar[g]"))
                item = self.meals_info2[i].horizontalHeaderItem(2)
                item.setText(_translate("TodayDietWindow", "Sodium[g]"))
                __sortingEnabled = self.meals_info2[0].isSortingEnabled()
                self.meals_info2[i].setSortingEnabled(False)
                item = self.meals_info2[i].item(0, 0)
                item.setText(_translate("TodayDietWindow", self.database[i][6]))
                item = self.meals_info2[i].item(0, 1)
                item.setText(_translate("TodayDietWindow", self.database[i][7]))
                item = self.meals_info2[i].item(0, 2)
                item.setText(_translate("TodayDietWindow", self.database[i][7]))
                self.meals_info2[i].setSortingEnabled(__sortingEnabled)

        self.lineEdit.setText(_translate("TodayDietWindow", "Today\'s Diet"))
