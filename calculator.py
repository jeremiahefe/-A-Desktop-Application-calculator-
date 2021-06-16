# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalApp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(320, 400)
        Calculator.setMinimumSize(QtCore.QSize(320, 400))
        Calculator.setMaximumSize(QtCore.QSize(320, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("jerry project/python/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculator.setWindowIcon(icon)
        Calculator.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label = QtWidgets.QLabel(Calculator)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 61))
        self.label.setMaximumSize(QtCore.QSize(2000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:3px solid;\n"
"border-color: rgb(0, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")
        self.btn_percentage = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("%"))
        self.btn_percentage.setGeometry(QtCore.QRect(20, 100, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_percentage.setFont(font)
        self.btn_percentage.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_percentage.setObjectName("btn_percentage")
        self.btn_m_add = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it(""))
        self.btn_m_add.setGeometry(QtCore.QRect(100, 100, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_m_add.setFont(font)
        self.btn_m_add.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_m_add.setObjectName("btn_m_add")
        self.btn_del = QtWidgets.QPushButton(Calculator, clicked = lambda:self.remove_it())
        self.btn_del.setGeometry(QtCore.QRect(170, 100, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_del.setFont(font)
        self.btn_del.setStyleSheet("")
        self.btn_del.setObjectName("btn_del")
        self.btn_clear = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("C"))
        self.btn_clear.setGeometry(QtCore.QRect(250, 100, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_9 = QtWidgets.QPushButton(Calculator,clicked = lambda:self.tap_it("7"))
        self.btn_9.setGeometry(QtCore.QRect(20, 160, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_9.setObjectName("btn_9")
        self.btn_add = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("+"))
        self.btn_add.setGeometry(QtCore.QRect(250, 160, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_add.setObjectName("btn_add")
        self.btn_8 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("8"))
        self.btn_8.setGeometry(QtCore.QRect(100, 160, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_8.setObjectName("btn_8")
        self.btn_10 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("9"))
        self.btn_10.setGeometry(QtCore.QRect(170, 160, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_10.setFont(font)
        self.btn_10.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_10.setObjectName("btn_10")
        self.btn_4 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("4"))
        self.btn_4.setGeometry(QtCore.QRect(20, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_4.setObjectName("btn_4")
        self.btn_sub = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("-"))
        self.btn_sub.setGeometry(QtCore.QRect(250, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sub.setFont(font)
        self.btn_sub.setStyleSheet("\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_sub.setObjectName("btn_sub")
        self.btn_5 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("5"))
        self.btn_5.setGeometry(QtCore.QRect(100, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("6"))
        self.btn_6.setGeometry(QtCore.QRect(170, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_6.setObjectName("btn_6")
        self.btn_1 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("1"))
        self.btn_1.setGeometry(QtCore.QRect(20, 280, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_1.setObjectName("btn_1")
        self.btn_mul = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("*"))
        self.btn_mul.setGeometry(QtCore.QRect(250, 280, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mul.setFont(font)
        self.btn_mul.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_mul.setObjectName("btn_mul")
        self.btn_2 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("2"))
        self.btn_2.setGeometry(QtCore.QRect(100, 280, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("3"))
        self.btn_3.setGeometry(QtCore.QRect(170, 280, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_3.setObjectName("btn_3")
        self.btn_0 = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("0"))
        self.btn_0.setGeometry(QtCore.QRect(20, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_0.setObjectName("btn_0")
        self.btn_div = QtWidgets.QPushButton(Calculator, clicked = lambda:self.tap_it("/"))
        self.btn_div.setGeometry(QtCore.QRect(250, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_div.setObjectName("btn_div")
        self.btn_piont = QtWidgets.QPushButton(Calculator, clicked = lambda:self.dot_it())
        self.btn_piont.setGeometry(QtCore.QRect(100, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_piont.setFont(font)
        self.btn_piont.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_piont.setObjectName("btn_piont")
        self.btn_eual = QtWidgets.QPushButton(Calculator, clicked = lambda:self.solve_it())
        self.btn_eual.setGeometry(QtCore.QRect(170, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_eual.setFont(font)
        self.btn_eual.setStyleSheet("background-color:white;\n"
"border:3px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.btn_eual.setObjectName("btn_eual")

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
        
    def plus_minus_it(self):
        # Grab what's on the screen already
        screen = self.label.text()
        if "-" in screen:
            self.Label.setText(screen.replace("-", ""))
        else:
            self.label.setText(f'-{screen}')

    def remove_it(self):
        # Grab what's on the screen already
        screen = self.label.text()
        # Remove last item in list/string
        screen = screen[:-1]
        # Output back to the screen
        self.label.setText(screen)   
        
    def tap_it(self,pressed): 
        if pressed == "C":
            self.label.setText("0")
        else:
            if self.label.text() == "0":
                self.label.setText("")
            #Else concatenate button text
            self.label.setText(f'{self.label.text()}{pressed}')     
        
        
    def dot_it(self):
        # Grab what's on the screen already
        screen = self.label.text()

        if screen [-1] == ".":
            pass
        else:
            self.label.setText(f'{screen}.')    
        
    def solve_it(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            # Output error to the screen
            self.label.setText("ERROR")    

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", " CALCULATOR APP"))
        self.label.setText(_translate("Calculator", ""))
        self.btn_percentage.setText(_translate("Calculator", "%"))
        self.btn_m_add.setText(_translate("Calculator", "M+"))
        self.btn_del.setText(_translate("Calculator", "<<"))
        self.btn_clear.setText(_translate("Calculator", "C"))
        self.btn_9.setText(_translate("Calculator", "7"))
        self.btn_add.setText(_translate("Calculator", "+"))
        self.btn_8.setText(_translate("Calculator", "8"))
        self.btn_10.setText(_translate("Calculator", "9"))
        self.btn_4.setText(_translate("Calculator", "4"))
        self.btn_sub.setText(_translate("Calculator", "-"))
        self.btn_5.setText(_translate("Calculator", "5"))
        self.btn_6.setText(_translate("Calculator", "6"))
        self.btn_1.setText(_translate("Calculator", "1"))
        self.btn_mul.setText(_translate("Calculator", "*"))
        self.btn_2.setText(_translate("Calculator", "2"))
        self.btn_3.setText(_translate("Calculator", "3"))
        self.btn_0.setText(_translate("Calculator", "0"))
        self.btn_div.setText(_translate("Calculator", "/"))
        self.btn_piont.setText(_translate("Calculator", "."))
        self.btn_eual.setText(_translate("Calculator", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())

