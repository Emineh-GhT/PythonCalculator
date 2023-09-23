from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import * 
from PySide6.QtUiTools import QUiLoader

from math import *



class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()
        self.ui = self.loader.load('design.ui' , None)
        self.ui.show()
        self.result = 0
        self.operation = ''
        self.ui.b0.clicked.connect(self.zero)
        self.ui.b1.clicked.connect(self.one)
        self.ui.b2.clicked.connect(self.two)
        self.ui.b3.clicked.connect(self.three)
        self.ui.b4.clicked.connect(self.four)
        self.ui.b5.clicked.connect(self.five)
        self.ui.b6.clicked.connect(self.six)
        self.ui.b7.clicked.connect(self.seven)
        self.ui.b8.clicked.connect(self.eight)
        self.ui.b9.clicked.connect(self.nine)
        self.ui.b_equal.clicked.connect(self.equal)
        self.ui.b_sum.clicked.connect(self.sum)
        self.ui.b_sub.clicked.connect(self.sub)
        self.ui.b_m.clicked.connect(self.mul)
        self.ui.b_d.clicked.connect(self.div)
        self.ui.b_dot.clicked.connect(self.dot)
        self.ui.b_ac.clicked.connect(self.reset)
        self.ui.b_pm.clicked.connect(self.plus_minus)
        self.ui.b_p.clicked.connect(self.percentage)
        self.ui.b_sin.clicked.connect(self.sin_t)
        self.ui.b_cos.clicked.connect(self.cos_t)
        self.ui.b_tan.clicked.connect(self.tan_t)
        self.ui.b_cot.clicked.connect(self.cot_t)
        self.ui.b_log.clicked.connect(self.log_n)
        self.ui.b_sqrt.clicked.connect(self.sqrt_n)
    

    def zero(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "0")
    def one(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "1")
    def two(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "2")
    def three(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "3")
    def four(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "4")
    def five(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "5")
    def six(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "6")
    def seven(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "7")
    def eight(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "8")
    def nine(self):
        self.ui.text_box.setText(self.ui.text_box.text() + "9")

    def sum(self):
        try:
            self.result=float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.opration="+"
        except:
            self.ui.text_box.setText("Enter a number")
            self.result = 0
        
    def sub(self):
        try:
            self.result=float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.opration="-"
        except:
            self.ui.text_box.setText("Enter a number")
            self.result = 0
       
    def mul(self):
        try:
            self.result=float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.opration="*"
        except:
            self.ui.text_box.setText("Enter a number")
            self.result = 0
        
    def div(self):
        try:
            self.result=float(self.ui.text_box.text())
            self.ui.text_box.setText("")
            self.opration="/"
        except:
            self.ui.text_box.setText("Enter a number")
            self.result = 0
        
    def sin_t(self):
        try:
            self.result = float(self.ui.text_box.text())
            self.result = self.result/360 *2 * pi
            self.result = round(sin(self.result),5)
            self.ui.text_box.setText(str(self.result))
            self.oparation = 'sin'
        except:
            self.ui.text_box.setText("Enter an angle")
            self.result = 0

    def cos_t(self):
        try:
            self.result = float(self.ui.text_box.text())
            self.result = self.result/360 *2 * pi
            self.result = round(cos(self.result),5)
            self.ui.text_box.setText(str(self.result))
            self.oparation = 'cos'
        except:
            self.ui.text_box.setText("Enter an angle")
            self.result = 0

    def tan_t(self):
        try:
            self.result = float(self.ui.text_box.text())
            self.result = self.result/360 *2 * pi
            self.result = round(tan(self.result),5)
            self.ui.text_box.setText(str(self.result))
            self.oparation = 'tan'
        except:
            self.ui.text_box.setText("Enter an angle")
            self.result = 0
           
    def cot_t(self):
        try:
            self.result=float(self.ui.text_box.text())
            self.result=self.result/360 *2 * pi
            self.result=round(atan(self.result),5)
            self.ui.text_box.setText(str(self.result))
            self.oparation = 'cot'
        except:
            self.ui.text_box.setText("Enter an angle")
            self.result = 0
        
    def log_n(self):
        try:
            self.ui.text_box.setText(str(log10(float(self.ui.text_box.text()))))
        except:
            self.ui.text_box.setText("Enter a number")
            self.result = 0

    def sqrt_n(self):
        try:
            self.ui.text_box.setText(str(sqrt(float(self.ui.text_box.text()))))
        except:
            self.ui.text_box.setText("Enter a number")
            self.result = 0

    def dot(self):
        
        if '.' not in self.ui.text_box.text():
            self.ui.text_box.setText(self.ui.text_box.text() + '.')

    def plus_minus(self):
        try:
            self.num2=float(self.ui.text_box.text())
            self.num2 *=-1
            self.ui.text_box.setText(str(self.num2))
        except:
            self.ui.text_box.setText("Enter a number")
            self.result = 0

    def percentage(self):
        try:
            self.ui.text_box.setText(str(float(self.ui.text_box.text())/100))
        except:
            self.ui.text_box.setText("Enter a number")
            self.result = 0

    def equal(self):
        self.num2 = float(self.ui.text_box.text())
        if self.opration == "+":
            self.result +=self.num2
            self.ui.text_box.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "-":
            self.result -=self.num2
            self.ui.text_box.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "*":
            self.result *= self.num2
            self.ui.text_box.setText(str(self.result))
            self.opration= ""
            self.result=0
        elif self.opration == "/":
            try:
                self.result /= self.num2
                self.ui.text_box.setText(str(self.result))
                self.opration= ""
                self.result=0
            except:
                self.ui.text_box.setText("")
                self.opration= ""
                self.result=0
        else:
            self.result = self.num2

    def reset(self):
       self.ui.text_box.setText("")
       self.result=0
       self.opration=""




app = QApplication([]) #yek aplication mitone chand window dashte bashe
window = Calculator()
app.exec() #baz baqi mondan