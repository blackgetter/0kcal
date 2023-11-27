# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FoodInfoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel
import time


class Ui_FoodInfoDialog(object):
    def __init__(self, pic=None, mat=None, foodList=None):
        super().__init__()
        if pic is None:
            print("empty in food info..")
        if pic is not None:
            self.tmpPicInDialog = pic
        if mat is not None:
            self.tmpMatInDialog = mat
        self.btnToStore = QPushButton("store")
        self.btnToCancel = QPushButton("cancel")

#        self.tmpPicInDialog = None
        self.tmpMatInDialog = None
        self.timeList = None
        self.currentTime = None
        self.timeList = self.getTime()
        self.timeStr_ = [str(i) for i in self.timeList]
        self.timeStr = [str(i) for i in self.timeList[1:]]
        self.tmp_button_index = 1

        self.count = 1
        self.total_nut = [0, 0, 0, 0, 0, 0]

        self.chgDatabase(foodList)
        self.local_db = [[] for _ in range(self.count)]

    def chgDatabase(self, foodList):
        self.count = len(foodList)

        self.database = []
        for i, elem in enumerate(foodList):
            tmpList = []
            tmpList.append(str(elem['food_name']))
            tmpList.append(str(i+1))
            tmpList.append(elem['calorie'])
            tmpList.append(elem['carbo'])
            tmpList.append(elem['protein'])
            tmpList.append(elem['fat'])
            tmpList.append(elem['sugar'])
            tmpList.append(elem['sodium'])
            tmpList.append(0)  # chk For select Clicked
            print("FOODINFODIALOG tmpList :", tmpList)
            self.database.append(tmpList)

        # self.database = for elem in foodList

    def setImageLabel(self, pic):
        return self.label.setPixmap(pic)

    def getTime(self) -> time:
        tm = time.localtime(time.time())
        returnList = [tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min]
        return returnList

    def getPicAndMatData(self, pic, mat):
        self.tmpMatInDialog = mat

    def selectButtonTo(self, x):
        _translate = QtCore.QCoreApplication.translate
        vol_change = [0.5, 1, 1.5]
        self.local_db[x][1] = vol_change[self.volumn_list[x].currentIndex()]
        for i in range(6):
            # chg index 8th to 1 if clicked
            self.database[x][1] = vol_change[self.volumn_list[x].currentIndex()]
            self.database[x][8] = 1
            self.local_db[x][i+2] = float(self.database[x][i+2]) * vol_change[self.volumn_list[x].currentIndex()]
            self.local_db[x][i+2] = round(self.local_db[x][i+2], 3)
            self.total_nut[i] -= float(self.database[x][i+2]) * vol_change[self.tmp_button_index]
            self.total_nut[i] += self.local_db[x][i+2]
        print("FOODINFO selected database", str(self.database[x]))
        print("FOODINFO selected local_db", str(self.local_db[x]))
        print("FOODINFO timelist", self.timeList)
        print("FOODINFO time_str", self.timeStr)

        self.tmp_button_index = self.volumn_list[x].currentIndex()
        item = self.nutrition_table.item(0, 0)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[0])))
        item = self.nutrition_table.item(0, 1)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[1])))
        item = self.nutrition_table.item(0, 2)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[2])))
        item = self.nutrition_table2.item(0, 0)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[3])))
        item = self.nutrition_table2.item(0, 1)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[4])))
        item = self.nutrition_table2.item(0, 2)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[5])))
        print(self.local_db)
        print(self.total_nut)

    def setFoodFrame(self, x):
        food_frame = QtWidgets.QFrame(self.frame)
        food_frame.setGeometry(QtCore.QRect(10, x, 240, 95))
        food_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        food_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        food_frame.setObjectName("food_frame")
        title_food_name = QtWidgets.QLineEdit(food_frame)
        title_food_name.setGeometry(QtCore.QRect(10, 10, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        title_food_name.setFont(font)
        title_food_name.setFrame(False)
        title_food_name.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        title_food_name.setDragEnabled(False)
        title_food_name.setReadOnly(True)
        title_food_name.setObjectName("title_food_name")
        title_volumn = QtWidgets.QLineEdit(food_frame)
        title_volumn.setGeometry(QtCore.QRect(10, 40, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        title_volumn.setFont(font)
        title_volumn.setFrame(False)
        title_volumn.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        title_volumn.setDragEnabled(False)
        title_volumn.setReadOnly(True)
        title_volumn.setObjectName("title_volumn")
        food_name = QtWidgets.QLineEdit(food_frame)
        food_name.setGeometry(QtCore.QRect(110, 10, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        food_name.setFont(font)
        food_name.setFrame(False)
        food_name.setObjectName("food_name")

        volumn = QtWidgets.QComboBox(food_frame)
        volumn.setGeometry(QtCore.QRect(110, 40, 111, 20))
        volumn.setObjectName("volumn")
        volumn.addItem("")
        volumn.addItem("")
        volumn.addItem("")
        volumn.setCurrentIndex(1)

        select_button = QtWidgets.QPushButton(food_frame)
        select_button.setGeometry(QtCore.QRect(178, 68, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        select_button.setFont(font)
        select_button.setStyleSheet("background-color:rgb(200,200,200);\n"
        "border-radius:5px")
        select_button.setObjectName("select_button")

        _translate = QtCore.QCoreApplication.translate
        title_food_name.setText(_translate("FoodInfoDialog", "Food Name"))
        title_volumn.setText(_translate("FoodInfoDialog", "Volumn"))

        self.food_name_list.append(food_name)
        self.volumn_list.append(volumn)
        self.select_button_list.append(select_button)

    def setupUi(self, FoodInfoDialog):
        FoodInfoDialog.setObjectName("FoodInfoDialog")
        FoodInfoDialog.resize(720, 540)
        self.currentTime = QLabel(' '.join(self.timeStr_))

        self.picture = QtWidgets.QLabel(FoodInfoDialog)
        self.picture.setGeometry(QtCore.QRect(40, 30, 362, 320))
        self.picture.setText("")
        self.picture.setTextFormat(QtCore.Qt.PlainText)
        self.picture.setObjectName("picture")

        self.nutrition_frame = QtWidgets.QFrame(FoodInfoDialog)
        self.nutrition_frame.setGeometry(QtCore.QRect(40, 390, 362, 100))
        self.nutrition_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nutrition_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nutrition_frame.setObjectName("nutrition_frame")

        self.nutrition_table = QtWidgets.QTableWidget(self.nutrition_frame)
        self.nutrition_table.setGeometry(QtCore.QRect(0, 0, 362, 50))
        self.nutrition_table.setStyleSheet("background-color:rgb(100, 150, 255);")
        self.nutrition_table.setGridStyle(QtCore.Qt.NoPen)
        self.nutrition_table.setWordWrap(True)
        self.nutrition_table.setRowCount(1)
        self.nutrition_table.setColumnCount(3)
        self.nutrition_table.setObjectName("meal_info")
        item = QtWidgets.QTableWidgetItem()
        self.nutrition_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.nutrition_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.nutrition_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.nutrition_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.nutrition_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.nutrition_table.setItem(0, 2, item)
        self.nutrition_table.horizontalHeader().setVisible(True)
        self.nutrition_table.horizontalHeader().setDefaultSectionSize(120)
        self.nutrition_table.horizontalHeader().setMinimumSectionSize(60)
        self.nutrition_table.verticalHeader().setVisible(False)
        self.nutrition_table.verticalHeader().setDefaultSectionSize(31)
        self.nutrition_table.verticalHeader().setHighlightSections(True)
        self.nutrition_table.verticalHeader().setMinimumSectionSize(20)
        self.nutrition_table2 = QtWidgets.QTableWidget(self.nutrition_frame)
        self.nutrition_table2.setGeometry(QtCore.QRect(0, 50, 362, 50))
        self.nutrition_table2.setStyleSheet("background-color:rgb(100, 150, 255);")
        self.nutrition_table2.setGridStyle(QtCore.Qt.NoPen)
        self.nutrition_table2.setWordWrap(True)
        self.nutrition_table2.setRowCount(1)
        self.nutrition_table2.setColumnCount(3)
        self.nutrition_table2.setObjectName("meal_info")
        item = QtWidgets.QTableWidgetItem()
        self.nutrition_table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.nutrition_table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.nutrition_table2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.nutrition_table2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.nutrition_table2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.nutrition_table2.setItem(0, 2, item)
        self.nutrition_table2.horizontalHeader().setVisible(True)
        self.nutrition_table2.horizontalHeader().setDefaultSectionSize(120)
        self.nutrition_table2.horizontalHeader().setMinimumSectionSize(60)
        self.nutrition_table2.verticalHeader().setVisible(False)
        self.nutrition_table2.verticalHeader().setDefaultSectionSize(31)
        self.nutrition_table2.verticalHeader().setHighlightSections(True)
        self.nutrition_table2.verticalHeader().setMinimumSectionSize(20)
        self.nutrition = QtWidgets.QLineEdit(FoodInfoDialog)
        self.nutrition.setGeometry(QtCore.QRect(40, 360, 251, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.nutrition.setFont(font)
        self.nutrition.setFrame(False)
        self.nutrition.setObjectName("nutrition")

        self.btnToStore = QtWidgets.QPushButton(FoodInfoDialog)
        self.btnToStore.setGeometry(QtCore.QRect(560, 500, 60, 20))
        self.btnToStore.setObjectName("btnToStore")
        self.btnToCancel = QtWidgets.QPushButton(FoodInfoDialog)
        self.btnToCancel.setGeometry(QtCore.QRect(625, 500, 60, 20))
        self.btnToCancel.setObjectName("btnToCancel")

        self.scrollArea = QtWidgets.QScrollArea(FoodInfoDialog)
        self.scrollArea.setGeometry(QtCore.QRect(410, 40, 275, 450))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 3000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 3000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.date = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.date.setGeometry(QtCore.QRect(10, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date.setFont(font)
        self.date.setFrame(False)
        self.date.setObjectName("date")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, 30, 261, 3000))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.food_name_list = []
        self.volumn_list = []
        self.select_button_list = []

        j = 10
        for i in range(self.count):
            self.setFoodFrame(j)
            j += 100

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(FoodInfoDialog)
        QtCore.QMetaObject.connectSlotsByName(FoodInfoDialog)

    def retranslateUi(self, FoodInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        FoodInfoDialog.setWindowTitle(_translate("FoodInfoDialog", "Dialog"))
        item = self.nutrition_table.horizontalHeaderItem(0)
        item.setText(_translate("FoodInfoDialog", "Calories[kcal]"))
        item = self.nutrition_table.horizontalHeaderItem(1)
        item.setText(_translate("FoodInfoDialog", "Carbo[g]"))
        item = self.nutrition_table.horizontalHeaderItem(2)
        item.setText(_translate("FoodInfoDialog", "Protein[g]"))
        item = self.nutrition_table2.horizontalHeaderItem(0)
        item.setText(_translate("FoodInfoDialog", "Fat[g]"))
        item = self.nutrition_table2.horizontalHeaderItem(1)
        item.setText(_translate("FoodInfoDialog", "Sugar[g]"))
        item = self.nutrition_table2.horizontalHeaderItem(2)
        item.setText(_translate("FoodInfoDialog", "Sodium[mg]"))

        self.nutrition.setText(_translate("FoodInfoDialog", "Nutritional Information"))
        self.date.setText(_translate("FoodInfoDialog", "2023/11/24   12:08"))

        for i in range(self.count):
            self.food_name_list[i].setText(
                _translate("FoodInfoDialog", self.database[i][0])
            )
            self.local_db[i].append(self.database[i][0])
            self.local_db[i].append("1")
            vol_change = [0.5, 1, 1.5]
            for j in range(6):
                self.local_db[i].append(float(self.database[i][j+2])*vol_change[self.volumn_list[i].currentIndex()])
                self.total_nut[j] += float(self.database[i][j+2])*vol_change[self.volumn_list[i].currentIndex()]
            self.volumn_list[i].setItemText(0, _translate("FoodInfoDialog", "0.5 serving"))
            self.volumn_list[i].setItemText(1, _translate("FoodInfoDialog", "1 serving"))
            self.volumn_list[i].setItemText(2, _translate("FoodInfoDialog", "1.5 serving"))
            self.select_button_list[i].setText(_translate("FoodInfoDialog", "Select"))

        item = self.nutrition_table.item(0, 0)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[0])))
        item = self.nutrition_table.item(0, 1)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[1])))
        item = self.nutrition_table.item(0, 2)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[2])))
        item = self.nutrition_table2.item(0, 0)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[3])))
        item = self.nutrition_table2.item(0, 1)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[4])))
        item = self.nutrition_table2.item(0, 2)
        item.setText(_translate("FoodInfoDialog", str(self.total_nut[5])))

        self.btnToStore.setText(_translate("FoodInfoDialog", "Store"))
        self.btnToCancel.setText(_translate("FoodInfoDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FoodInfoDialog = QtWidgets.QDialog()
    ui = Ui_FoodInfoDialog()
    ui.setupUi(FoodInfoDialog)
    FoodInfoDialog.show()
    sys.exit(app.exec_())
