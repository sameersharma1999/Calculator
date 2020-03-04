from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
import math


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 564)
        MainWindow.setMinimumSize(QtCore.QSize(339, 564))
        MainWindow.setMaximumSize(QtCore.QSize(339, 564))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 1))
        MainWindow.setToolTipDuration(-1)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 341, 531))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_buttons = QtWidgets.QFrame(self.frame)
        self.frame_buttons.setGeometry(QtCore.QRect(10, 120, 321, 421))
        self.frame_buttons.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.point = QtWidgets.QPushButton(self.frame_buttons)
        self.point.setGeometry(QtCore.QRect(140, 350, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.point.setFont(font)
        self.point.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.point.setObjectName("point")
        self.three = QtWidgets.QPushButton(self.frame_buttons)
        self.three.setGeometry(QtCore.QRect(140, 280, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.three.setFont(font)
        self.three.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.three.setObjectName("three")
        self.zero = QtWidgets.QPushButton(self.frame_buttons)
        self.zero.setGeometry(QtCore.QRect(70, 350, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.zero.setFont(font)
        self.zero.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.zero.setObjectName("zero")
        self.two = QtWidgets.QPushButton(self.frame_buttons)
        self.two.setGeometry(QtCore.QRect(70, 280, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.two.setFont(font)
        self.two.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.two.setObjectName("two")
        self.eight = QtWidgets.QPushButton(self.frame_buttons)
        self.eight.setGeometry(QtCore.QRect(70, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eight.setFont(font)
        self.eight.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.eight.setObjectName("eight")
        self.back = QtWidgets.QPushButton(self.frame_buttons)
        self.back.setGeometry(QtCore.QRect(210, 0, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(227, 131, 13);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.back.setObjectName("back")
        self.five = QtWidgets.QPushButton(self.frame_buttons)
        self.five.setGeometry(QtCore.QRect(70, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.five.setFont(font)
        self.five.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.five.setObjectName("five")
        self.seven = QtWidgets.QPushButton(self.frame_buttons)
        self.seven.setGeometry(QtCore.QRect(0, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.seven.setFont(font)
        self.seven.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.seven.setObjectName("seven")
        self.plus_minus = QtWidgets.QPushButton(self.frame_buttons)
        self.plus_minus.setGeometry(QtCore.QRect(0, 350, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plus_minus.setFont(font)
        self.plus_minus.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.plus_minus.setObjectName("plus_minus")
        self.multiply = QtWidgets.QPushButton(self.frame_buttons)
        self.multiply.setGeometry(QtCore.QRect(210, 140, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("background-color: rgb(227, 131, 13);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.multiply.setObjectName("multiply")
        self.x_square = QtWidgets.QPushButton(self.frame_buttons)
        self.x_square.setGeometry(QtCore.QRect(70, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.x_square.setFont(font)
        self.x_square.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.x_square.setObjectName("x_square")
        self.divide = QtWidgets.QPushButton(self.frame_buttons)
        self.divide.setGeometry(QtCore.QRect(210, 70, 111, 61))
        self.divide.setMinimumSize(QtCore.QSize(111, 61))
        self.divide.setMaximumSize(QtCore.QSize(111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.divide.setFont(font)
        self.divide.setStyleSheet("background-color: rgb(227, 131, 13);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.divide.setObjectName("divide")
        self.root = QtWidgets.QPushButton(self.frame_buttons)
        self.root.setGeometry(QtCore.QRect(140, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.root.setFont(font)
        self.root.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.root.setObjectName("root")
        self.per = QtWidgets.QPushButton(self.frame_buttons)
        self.per.setGeometry(QtCore.QRect(0, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.per.setFont(font)
        self.per.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"border-radius: 30px;")
        self.per.setObjectName("per")
        self.six = QtWidgets.QPushButton(self.frame_buttons)
        self.six.setGeometry(QtCore.QRect(140, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.six.setFont(font)
        self.six.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.six.setObjectName("six")
        self.four = QtWidgets.QPushButton(self.frame_buttons)
        self.four.setGeometry(QtCore.QRect(0, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.four.setFont(font)
        self.four.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.four.setObjectName("four")
        self.plus = QtWidgets.QPushButton(self.frame_buttons)
        self.plus.setGeometry(QtCore.QRect(210, 280, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plus.setFont(font)
        self.plus.setStyleSheet("background-color: rgb(227, 131, 13);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.plus.setObjectName("plus")
        self.equal = QtWidgets.QPushButton(self.frame_buttons)
        self.equal.setGeometry(QtCore.QRect(210, 350, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.equal.setFont(font)
        self.equal.setStyleSheet("background-color: rgb(227, 131, 13);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.equal.setObjectName("equal")
        self.one_by_x = QtWidgets.QPushButton(self.frame_buttons)
        self.one_by_x.setGeometry(QtCore.QRect(0, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.one_by_x.setFont(font)
        self.one_by_x.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.one_by_x.setObjectName("one_by_x")
        self.nine = QtWidgets.QPushButton(self.frame_buttons)
        self.nine.setGeometry(QtCore.QRect(140, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nine.setFont(font)
        self.nine.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.nine.setObjectName("nine")
        self.minus = QtWidgets.QPushButton(self.frame_buttons)
        self.minus.setGeometry(QtCore.QRect(210, 210, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.minus.setFont(font)
        self.minus.setStyleSheet("background-color: rgb(227, 131, 13);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.minus.setObjectName("minus")
        self.one = QtWidgets.QPushButton(self.frame_buttons)
        self.one.setGeometry(QtCore.QRect(0, 280, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.one.setFont(font)
        self.one.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);border-radius: 30px;")
        self.one.setObjectName("one")
        self.clear = QtWidgets.QPushButton(self.frame_buttons)
        self.clear.setGeometry(QtCore.QRect(140, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"border-radius: 30px;")
        self.clear.setObjectName("clear")
        self.ce = QtWidgets.QPushButton(self.frame_buttons)
        self.ce.setGeometry(QtCore.QRect(70, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ce.setFont(font)
        self.ce.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"border-radius: 30px;")
        self.ce.setObjectName("ce")
        self.frame_calculations_display = QtWidgets.QFrame(self.frame)
        self.frame_calculations_display.setGeometry(QtCore.QRect(10, 40, 321, 71))
        self.frame_calculations_display.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_calculations_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_calculations_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calculations_display.setObjectName("frame_calculations_display")
        self.label_2 = QtWidgets.QLabel(self.frame_calculations_display)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_calculations_display)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 311, 20))
        self.label_3.setMaximumSize(QtCore.QSize(100000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.zero.clicked.connect(lambda: self.get('0'))
        self.one.clicked.connect(lambda: self.get('1'))
        self.two.clicked.connect(lambda: self.get('2'))
        self.three.clicked.connect(lambda: self.get('3'))
        self.four.clicked.connect(lambda: self.get('4'))
        self.five.clicked.connect(lambda: self.get('5'))
        self.six.clicked.connect(lambda: self.get('6'))
        self.seven.clicked.connect(lambda: self.get('7'))
        self.eight.clicked.connect(lambda: self.get('8'))
        self.nine.clicked.connect(lambda: self.get('9'))
        self.plus.clicked.connect(lambda: self.get('+'))
        self.minus.clicked.connect(lambda: self.get('-'))
        self.multiply.clicked.connect(lambda: self.get('*'))
        self.divide.clicked.connect(lambda: self.get('/'))
        self.plus_minus.clicked.connect(lambda: self.get('+_-'))
        self.per.clicked.connect(lambda: self.get('%'))
        self.one_by_x.clicked.connect(lambda: self.get('1/x'))
        self.x_square.clicked.connect(lambda: self.get('x_square'))
        self.root.clicked.connect(lambda: self.get('SquareRoot'))
        self.back.clicked.connect(lambda: self.get('<'))
        self.ce.clicked.connect(lambda: self.get('CE'))
        self.clear.clicked.connect(lambda: self.get('C'))
        self.equal.clicked.connect(lambda: self.get('='))
        self.point.clicked.connect(lambda: self.get('.'))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get(self, data):
        if self.label_2.text() == '0' and data not in ['+', '-', '*', '/', '=', '<', '.', 'C', 'CE', '%', '1/x', 'SquareRoot', 'x_square', '+_-']:
            self.label_2.setText(data)
        elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.label_2.text() == 'Error':
                self.label_2.clear()
            self.label_2.setText(self.label_2.text() + data)
        elif data in ['+', '-', '*', '/']:
            if self.label_3.text() == '':
                self.label_3.setText(self.label_2.text() + data)
                self.label_2.clear()
            elif self.label_2.text() != '' and list(self.label_3.text()).pop() not in ['+', '-', '*', '/']:
                self.label_3.setText(self.label_2.text() + data)
            else:
                check_operator2 = list(self.label_3.text()).pop()
                if self.label_2.text() != '' and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    self.label_3.setText(self.label_3.text() + self.label_2.text() + data)
                elif check_operator2 != data and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    self.label_3.setText(self.label_3.text()[:-1] + data)  # change operator
                elif check_operator2 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    self.label_3.setText(self.label_3.text() + data + self.label_2.text())
            self.label_2.clear()
        elif data == '<':
            if self.label_2.text() == '0':
                pass
            elif self.label_2.text() in ['-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']:
                self.label_2.setText('0')
            elif len(self.label_2.text()) == 1:
                self.label_2.setText('0')
            elif len(self.label_2.text()) > 0:
                changed_data = list(self.label_2.text())
                changed_data.pop()
                sums = ''
                for i in changed_data:
                    sums += i
                self.label_2.setText(sums)
            else:
                pass
        elif data == '=':
            if self.label_3.text() == '':
                self.label_2.setText(self.label_2.text())
            elif self.label_3.text() != '':
                if list(self.label_3.text()).pop() in ['+', '-', '*', '/'] and self.label_2.text() == '':
                    string_without_sign = list(self.label_3.text())
                    string_without_sign.pop()
                    string_sum = ''
                    for i in string_without_sign:
                        string_sum += i
                    result = self.calculations(string_sum)
                    self.label_2.setText(str(result))
                elif list(self.label_3.text()).pop() in ['+', '-', '*', '/']:
                    new_str = self.label_3.text() + self.label_2.text()
                    self.label_3.setText(new_str)
                    result = self.calculations(new_str)
                    self.label_2.setText(str(result))
                elif self.label_3.text() != '' and self.label_2.text() == '':
                    result = self.calculations(self.label_3.text())
                    self.label_2.setText(str(result))
            self.label_3.clear()
        elif data == '.':
            if '.' in self.label_2.text():
                pass
            elif self.label_2.text() == '0' or self.label_2.text() == '':
                self.label_2.setText('0' + data)
            else:
                self.label_2.setText(self.label_2.text() + data)
        elif data == '%':
            if self.label_2.text() != '':
                new_str = self.label_2.text() + '/' + '100'
                result = self.calculations(new_str)
                self.label_2.setText(str(result))
        elif data == '1/x':
            if self.label_2.text() != '':
                new_str = '1' + '/' + self.label_2.text()
                result = self.calculations(new_str)
                self.label_2.setText(str(result))
        elif data == 'x_square':
            if self.label_2.text() != '':
                new_str = self.label_2.text() + '**' + '2'
                result = self.calculations(new_str)
                self.label_2.setText(str(result))
        elif data == 'SquareRoot':
            if self.label_2.text() == '':
                pass
            else:    
                try:
                    self.label_2.setText(str(round(math.sqrt(eval(self.label_2.text())), 4)))
                except ValueError as e:
                    self.label_3.clear()
                    self.disable()
                    self.label_2.setText('Error')
        elif data == '+_-':
            if self.label_2.text() != '':
                if self.label_2.text() not in ['0', '0.0']:
                    first_letter = list(self.label_2.text())[0]
                    minus = '-'
                    if first_letter != minus:
                        self.label_2.setText(minus + self.label_2.text())
                    elif first_letter == minus:
                        self.label_2.setText(self.label_2.text()[1:])
                else:
                    pass        
        elif data == 'C':
            self.label_2.clear()
            self.label_3.clear()
            self.label_2.setText('0')
            self.enable()
        elif data == 'CE':
            self.label_3.clear()
            self.label_2.clear()
            self.label_2.setText('0')
            self.enable()

    def enable(self):
        self.plus.setEnabled(True)
        self.minus.setEnabled(True)
        self.multiply.setEnabled(True)
        self.divide.setEnabled(True)
        self.point.setEnabled(True)
        self.plus_minus.setEnabled(True)
        self.per.setEnabled(True)
        self.back.setEnabled(True)
        self.one_by_x.setEnabled(True)
        self.x_square.setEnabled(True)
        self.root.setEnabled(True)

    def disable(self):
        self.plus.setEnabled(False)
        self.minus.setEnabled(False)
        self.multiply.setEnabled(False)
        self.divide.setEnabled(False)
        self.point.setEnabled(False)
        self.plus_minus.setEnabled(False)
        self.per.setEnabled(False)
        self.back.setEnabled(False)
        self.one_by_x.setEnabled(False)
        self.x_square.setEnabled(False)
        self.root.setEnabled(False)

    def calculations(self, value):
        try:
            get = eval(value)
            if type(get) == type(1.1):
                count = 0
                for i in list(str(get)):
                    count += 1
                    if i == '.':
                        count = 0
                if count > 4:
                    return round(get, 4)
                else:
                    return get             
            else:
                return get 
        except ZeroDivisionError as e:
            self.label_3.clear()
            self.disable()
            return 'Error'
        except Exception as e:
            return 'Error'



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.point.setText(_translate("MainWindow", "."))
        self.three.setText(_translate("MainWindow", "3"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.two.setText(_translate("MainWindow", "2"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.back.setToolTip(_translate("MainWindow", "Remove/Back"))
        self.back.setText(_translate("MainWindow", "<"))
        self.five.setText(_translate("MainWindow", "5"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.plus_minus.setText(_translate("MainWindow", "+/-"))
        self.multiply.setToolTip(_translate("MainWindow", "Multiply"))
        self.multiply.setText(_translate("MainWindow", "X"))
        self.x_square.setToolTip(_translate("MainWindow", "Square"))
        self.x_square.setText(_translate("MainWindow", "x²"))
        self.divide.setToolTip(_translate("MainWindow", "Divide"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.root.setToolTip(_translate("MainWindow", "Square root"))
        self.root.setText(_translate("MainWindow", "²√x"))
        self.per.setText(_translate("MainWindow", "%"))
        self.six.setText(_translate("MainWindow", "6"))
        self.four.setText(_translate("MainWindow", "4"))
        self.plus.setToolTip(_translate("MainWindow", "Plus"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.equal.setText(_translate("MainWindow", "="))
        self.one_by_x.setToolTip(_translate("MainWindow", "one by x"))
        self.one_by_x.setText(_translate("MainWindow", "1/x"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.minus.setToolTip(_translate("MainWindow", "Subtract"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.one.setText(_translate("MainWindow", "1"))
        self.clear.setToolTip(_translate("MainWindow", "Clear"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.ce.setToolTip(_translate("MainWindow", "Clear recent calculation"))
        self.ce.setText(_translate("MainWindow", "CE"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Standard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
