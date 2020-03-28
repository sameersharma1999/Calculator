from PyQt5 import QtWidgets
from MyApp.Ui import Ui_MainWindow
from MyApp.light_theme import Ui_MainWindow2
import math


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow, Ui_MainWindow2):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi2(self)  # here we setup ui file of light mode (Initially)

        self.actionDark.triggered.connect(self.change_theme_to_dark)
        self.actionLight.triggered.connect(self.change_theme_to_light)

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

    def change_theme_to_light(self):
        self.setupUi2(self)  # here we setup ui file of light mode

        self.actionDark.triggered.connect(self.change_theme_to_dark)
        self.actionLight.triggered.connect(self.change_theme_to_light)

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

    def change_theme_to_dark(self):
        self.setupUi(self)  # here we setup ui file of dark mode

        self.actionDark.triggered.connect(self.change_theme_to_dark)
        self.actionLight.triggered.connect(self.change_theme_to_light)

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

    def get(self, data):
            if self.label_2.text() != 'Error':
                self.enable()
            if self.label_2.text() == '0' and data not in ['+', '-', '*', '/', '=', '<', '.', 'C', 'CE', '%', '1/x',
                                                           'SquareRoot', 'x_square', '+_-']:
                self.label_2.setText(data)
            elif data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.label_2.text() == 'Error':
                    self.label_2.clear()
                elif len(self.label_2.text()) == 12:
                    pass
                else:
                    self.label_2.setText(self.label_2.text() + data)
            elif data in ['+', '-', '*', '/']:
                if self.label_3.text() == '':
                    self.label_3.setText(self.label_2.text() + data)
                    self.label_2.clear()
                elif self.label_2.text() != '' and list(self.label_3.text()).pop() not in ['+', '-', '*', '/']:
                    self.label_3.setText(self.label_2.text() + data)
                else:
                    check_operator2 = list(self.label_3.text()).pop()
                    if self.label_2.text() != '' and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                                             '9']:
                        self.label_3.setText(self.label_3.text() + self.label_2.text() + data)
                    elif check_operator2 != data and check_operator2 not in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                                             '9']:
                        self.label_3.setText(self.label_3.text()[:-1] + data)  # change operator
                    elif check_operator2 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        self.label_3.setText(self.label_3.text() + data + self.label_2.text())
                self.label_2.clear()
            elif data == '<':
                if self.label_2.text() == 'E':
                    self.enable()
                if self.label_2.text() == '0':
                    self.enable()
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
            if type(1.1) == type(get):
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

    def keyPressEvent(self, event):
        if event.key() == 48:  # 0
            self.get('0')
        elif event.key() == 49:  # 1
            self.get('1')
        elif event.key() == 50:  # 2
            self.get('2')
        elif event.key() == 51:  # 3
            self.get('3')
        elif event.key() == 52:  # 4
            self.get('4')
        elif event.key() == 53:  # 5
            self.get('5')
        elif event.key() == 54:  # 6
            self.get('6')
        elif event.key() == 55:  # 7
            self.get('7')
        elif event.key() == 56:  # 8
            self.get('8')
        elif event.key() == 57:  # 9
            self.get('9')
        elif event.key() == 43:  # +
            self.get('+')
        elif event.key() == 45:  # -
            self.get('-')
        elif event.key() == 42:  # *
            self.get('*')
        elif event.key() == 47:  # /
            self.get('/')
        elif event.key() == 37:  # %
            self.get('%')
        elif event.key() == 16777219:  # Backspace
            self.get('<')
        elif event.key() == 16777220:  # enter (=)
            self.get('=')
        elif event.key() == 61:
            self.get('=')
        elif event.key() == 46:  # . (point)
            self.get('.')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MyMainWindow()
    win.show()
    app.exec_()
