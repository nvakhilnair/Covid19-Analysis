##### Libraries imported #######
from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import pandas as pd

######## Required files import ##########
from India_Current_Status import india_Current_Status
from India_Daily_Status import india_Daily_Status
from India_Test_Positvity import india_Test_Positivity
from State_Current_Status import state_Current_Status
from State_Daily_Status import state_Daily_Status
from State_Test_Positivity import state_Test_Positivity
from State_Comparison import state_Compare
from District_Current_Status import district_Current_Status
from District_Daily_Status import district_Daily_Status



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_Covid_Analysis(QWidget):
    def setupUi(self, Covid_Analysis):
        Covid_Analysis.setObjectName(_fromUtf8("Covid_Analysis"))
        Covid_Analysis.resize(700, 530)
        Covid_Analysis.setAutoFillBackground(False)
        Covid_Analysis.setStyleSheet(
            "QWidget#Covid_Analysis {background-image: url('data/logo.png');background-repeat: no-repeat; background-position: center;}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("data\icon.ico")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Covid_Analysis.setWindowIcon(icon)
        self.line = QtWidgets.QFrame(Covid_Analysis)
        self.line.setGeometry(QtCore.QRect(0, 130, 701, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtWidgets.QFrame(Covid_Analysis)
        self.line_2.setGeometry(QtCore.QRect(0, 400, 701, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_India = QtWidgets.QLabel(Covid_Analysis)
        self.label_India.setGeometry(QtCore.QRect(270, 70, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_India.setFont(font)
        self.label_India.setObjectName(_fromUtf8("label_India"))
        self.label_State = QtWidgets.QLabel(Covid_Analysis)
        self.label_State.setGeometry(QtCore.QRect(270, 150, 191, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_State.setFont(font)
        self.label_State.setObjectName(_fromUtf8("label_State"))
        self.label_District = QtWidgets.QLabel(Covid_Analysis)
        self.label_District.setGeometry(QtCore.QRect(270, 420, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_District.setFont(font)
        self.label_District.setObjectName(_fromUtf8("label_District"))
        self.progressBar = QtWidgets.QProgressBar(Covid_Analysis)
        self.progressBar.setGeometry(QtCore.QRect(100, 30, 151, 21))
        self.progressBar.setMinimum(0)
        self.progressBar.setRange(0, 100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.Button_GetData = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_GetData.setGeometry(QtCore.QRect(300, 30, 111, 23))
        self.Button_GetData.setObjectName(_fromUtf8("Button_GetData"))
        self.Button_GetData.clicked.connect(self.get_Required_Data)
        self.Button_IndiaCurrent = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_IndiaCurrent.setGeometry(QtCore.QRect(60, 100, 111, 23))
        self.Button_IndiaCurrent.setObjectName(_fromUtf8("Button_IndiaCurrent"))
        self.Button_IndiaCurrent.setEnabled(False)
        self.Button_IndiaCurrent.clicked.connect(self.India_Current_Status)
        self.Button_IndiaDaily = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_IndiaDaily.setGeometry(QtCore.QRect(270, 100, 125, 23))
        self.Button_IndiaDaily.setObjectName(_fromUtf8("Button_IndiaDaily"))
        self.Button_IndiaDaily.setEnabled(False)
        self.Button_IndiaDaily.clicked.connect(self.India_Daily_Status)
        self.Button_IndiaPositivity = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_IndiaPositivity.setGeometry(QtCore.QRect(480, 100, 200, 23))
        self.Button_IndiaPositivity.setObjectName(_fromUtf8("Button_IndiaPositivity"))
        self.Button_IndiaPositivity.setEnabled(False)
        self.Button_IndiaPositivity.clicked.connect(self.India_Test_Positivity)
        self.Button_StateCurrent = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_StateCurrent.setGeometry(QtCore.QRect(200, 200, 101, 23))
        self.Button_StateCurrent.setObjectName(_fromUtf8("Button_StateCurrent"))
        self.Button_StateCurrent.setEnabled(False)
        self.Button_StateCurrent.clicked.connect(self.State_Current_Status)
        self.Button_StateDaily = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_StateDaily.setGeometry(QtCore.QRect(330, 200, 121, 23))
        self.Button_StateDaily.setObjectName(_fromUtf8("Button_StateDaily"))
        self.Button_StateDaily.setEnabled(False)
        self.Button_StateDaily.clicked.connect(self.State_Daily_Status)
        self.Button_StatePositivity = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_StatePositivity.setGeometry(QtCore.QRect(480, 200, 201, 23))
        self.Button_StatePositivity.setObjectName(_fromUtf8("Button_StatePositivity"))
        self.Button_StatePositivity.setEnabled(False)
        self.Button_StatePositivity.clicked.connect(self.State_Test_Positivity)
        self.Button_Compare = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_Compare.setGeometry(QtCore.QRect(500, 310, 180, 23))
        self.Button_Compare.setObjectName(_fromUtf8("Button_Compare"))
        self.Button_Compare.setEnabled(False)
        self.Button_Compare.clicked.connect(self.State_Comparision)
        self.Button_DistrictStatus = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_DistrictStatus.setGeometry(QtCore.QRect(150, 460, 120, 23))
        self.Button_DistrictStatus.setObjectName(_fromUtf8("Button_DistrictStatus"))
        self.Button_DistrictStatus.setEnabled(False)
        self.Button_DistrictStatus.clicked.connect(self.District_Current_Status)
        self.Button_DistrictDaily = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_DistrictDaily.setGeometry(QtCore.QRect(290, 460, 120, 23))
        self.Button_DistrictDaily.setObjectName(_fromUtf8("Button_DistrictDaily"))
        self.Button_DistrictDaily.setEnabled(False)
        self.Button_DistrictDaily.clicked.connect(self.District_Daily_Status)
        self.comboBox_State = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_State.setGeometry(QtCore.QRect(20, 200, 121, 22))
        self.comboBox_State.setEditable(False)
        self.comboBox_State.setMaxVisibleItems(13)
        self.comboBox_State.setObjectName(_fromUtf8("comboBox_State"))
        self.comboBox_State.addItem(_fromUtf8(""))
        self.comboBox_Compare_1 = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_Compare_1.setGeometry(QtCore.QRect(18, 310, 121, 22))
        self.comboBox_Compare_1.setObjectName(_fromUtf8("comboBox_Compare_1"))
        self.comboBox_Compare_1.addItem(_fromUtf8(""))
        self.comboBox_Compare_2 = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_Compare_2.setGeometry(QtCore.QRect(180, 310, 121, 22))
        self.comboBox_Compare_2.setObjectName(_fromUtf8("comboBox_Compare_2"))
        self.comboBox_Compare_2.addItem(_fromUtf8(""))
        self.comboBox_Compare_3 = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_Compare_3.setGeometry(QtCore.QRect(330, 310, 141, 22))
        self.comboBox_Compare_3.setObjectName(_fromUtf8("comboBox_Compare_3"))
        self.comboBox_Compare_3.addItem(_fromUtf8(""))
        self.comboBox_District = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_District.setGeometry(QtCore.QRect(6, 460, 131, 22))
        self.comboBox_District.setObjectName(_fromUtf8("comboBox_District"))
        self.comboBox_District.addItem(_fromUtf8(""))
        self.label_Discription = QtWidgets.QLabel(Covid_Analysis)
        self.label_Discription.setGeometry(QtCore.QRect(510, 420, 180, 71))
        self.label_Discription.setObjectName(_fromUtf8("label_Discription"))
        self.retranslateUi(Covid_Analysis)
        self.comboBox_State.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Covid_Analysis)

    def get_Required_Data(self):
        global state_wise
        global case_time_series
        global tested_number_icmr_data
        global state_wise_daily
        global statewise_tested_number_data
        global district_wise
        global districts

        ########## Reading the Data ##########################
        try:
            state_wise = pd.read_csv(
                "https://api.covid19india.org/csv/latest/state_wise.csv")
            self.progressBar.setValue(10)

            case_time_series = pd.read_csv(
                "https://api.covid19india.org/csv/latest/case_time_series.csv")
            self.progressBar.setValue(20)

            tested_number_icmr_data = pd.read_csv(
                "https://api.covid19india.org/csv/latest/tested_numbers_icmr_data.csv")
            self.progressBar.setValue(30)

            state_wise_daily = pd.read_csv(
                'https://api.covid19india.org/csv/latest/state_wise_daily.csv')
            self.progressBar.setValue(40)

            statewise_tested_number_data = pd.read_csv(
                'https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv')
            self.progressBar.setValue(60)

            district_wise = pd.read_csv(
                'https://api.covid19india.org/csv/latest/district_wise.csv')
            self.progressBar.setValue(80)

            districts = pd.read_csv('https://api.covid19india.org/csv/latest/districts.csv')
            self.progressBar.setValue(100)
            self.progressBar.setFormat('Completed')

        except:
            application = QtWidgets.QApplication(sys.argv)
            QMessageBox.information(None, 'Error', 'No Network Connection',
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)
            sys.exit(0)
        
        ######################## Enabling the buttons ##################
        self.Button_IndiaCurrent.setEnabled(True)
        self.Button_IndiaDaily.setEnabled(True)
        self.Button_IndiaPositivity.setEnabled(True)
        self.Button_StateCurrent.setEnabled(True)
        self.Button_StateDaily.setEnabled(True)
        self.Button_StatePositivity.setEnabled(True)
        self.Button_Compare.setEnabled(True)
        self.Button_DistrictStatus.setEnabled(True)
        self.Button_DistrictDaily.setEnabled(True)

        ########################## Assigning values to combobox ############
        data = state_wise.copy()
        state_names = list(data.State.iloc[1:,].unique())
        data = district_wise.copy()
        district_name = list(data.District.iloc[1:,].unique())
        del_list = ['Other State','Other Region','Unknown']
        district_name = [i for i in district_name if i not in del_list]
        for i in range(0, len(state_names)):
            self.comboBox_State.insertItem(i, _translate(
                "Covid_Analysis", state_names[i], None))
            self.comboBox_Compare_1.insertItem(
                i, _translate("Covid_Analysis", state_names[i], None))
            self.comboBox_Compare_2.insertItem(
                i, _translate("Covid_Analysis", state_names[i], None))
            self.comboBox_Compare_3.insertItem(
                i, _translate("Covid_Analysis", state_names[i], None))
        for i in range(0, len(district_name)):
            self.comboBox_District.insertItem(i, _translate(
                "Covid_Analysis", district_name[i], None))
        self.comboBox_State.setCurrentIndex(state_names.index('Kerala'))
        self.comboBox_Compare_1.setCurrentIndex(state_names.index('Kerala'))
        self.comboBox_Compare_2.setCurrentIndex(state_names.index('Gujarat'))
        self.comboBox_Compare_3.setCurrentIndex(state_names.index('Karnataka'))
        self.comboBox_District.setCurrentIndex(district_name.index('Kannur'))


    def India_Current_Status(self):
        india_Current_Status(state_wise)

    def India_Daily_Status(self):
        india_Daily_Status(case_time_series)

    def India_Test_Positivity(self):
        india_Test_Positivity(tested_number_icmr_data,case_time_series)

    def State_Current_Status(self):
        state = self.comboBox_State.currentText()
        state_Current_Status(state,state_wise)
        
    def State_Daily_Status(self):
        try:
            state = self.comboBox_State.currentText()
            state_Daily_Status(state,state_wise,state_wise_daily)
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected state")

    def State_Test_Positivity(self):
        try:
           state = self.comboBox_State.currentText()
           state_Test_Positivity(state,statewise_tested_number_data,state_wise,state_wise_daily)
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected state")

    def State_Comparision(self):
        try:
            state_1 = self.comboBox_Compare_1.currentText()
            state_2 = self.comboBox_Compare_2.currentText()
            state_3 = self.comboBox_Compare_3.currentText()
            state_Compare(state_1,state_2,state_3,state_wise,state_wise_daily,statewise_tested_number_data)
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the any 1 or more selected state")

    def District_Current_Status(self):
        district = self.comboBox_District.currentText()
        district_Current_Status(district,district_wise)
    
    def District_Daily_Status(self):
        try:
            district = self.comboBox_District.currentText()
            district_Daily_Status(district,districts)
            
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected district")

            
    def retranslateUi(self, Covid_Analysis):
        Covid_Analysis.setWindowTitle(_translate("Covid_Analysis", "Covid-19 Analysis", None))
        self.label_India.setText(_translate(
            "Covid_Analysis", "Covid-19: India Analysis", None))
        self.label_State.setText(_translate(
            "Covid_Analysis", "Covid-19: State Analysis", None))
        self.label_District.setText(_translate(
            "Covid_Analysis", "Covid-19: District Analysis", None))
        self.Button_IndiaCurrent.setText(_translate("Covid_Analysis", "Current Status", None))
        self.Button_IndiaDaily.setText(_translate(
            "Covid_Analysis", "15 Days Daily Status", None))
        self.Button_IndiaPositivity.setText(_translate(
            "Covid_Analysis", "15 Days Daily Test Positivity", None))
        self.Button_StateCurrent.setText(_translate("Covid_Analysis", "Current Status", None))
        self.Button_StateDaily.setText(_translate(
            "Covid_Analysis", "15 Days Daily Status", None))
        self.Button_StatePositivity.setText(_translate(
            "Covid_Analysis", "15 Days Daily Test Positivity", None))
        self.Button_Compare.setText(_translate(
            "Covid_Analysis", "Compare", None))
        self.Button_DistrictStatus.setText(_translate(
            "Covid_Analysis", "Current Status", None))
        self.Button_DistrictDaily.setText(_translate(
            "Covid_Analysis", "15 Days Daily Status", None))
        self.Button_GetData.setText(_translate(
            "Covid_Analysis", "Get Data", None))
        self.label_Discription.setText(_translate("Covid_Analysis", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Developed</span><span style=\" font-weight:600;\">: Akhil</span></p><p><span style=\" font-weight:600;\">MadeWithPY009@gmail.com</span></p><p><span style=\" font-weight:600; text-decoration: underline;\">Data</span><span style=\" font-weight:600;\">: </span><a href=\"https://api.covid19india.org/\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">api.covid19india.org</span></a></p></body></html>", None))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Covid_Analysis = QtWidgets.QDialog()
    ui = Ui_Covid_Analysis()
    ui.setupUi(Covid_Analysis)
    Covid_Analysis.show()
    sys.exit(app.exec_())


