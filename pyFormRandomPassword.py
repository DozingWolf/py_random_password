from Ui_pyRP_UI import Ui_Form

from PySide6.QtWidgets import QApplication,QWidget,QSlider
from PySide6.QtGui import QShortcut,QKeySequence
from random import choice
from pyperclip import copy
from datetime import datetime

appVersion = '0.0.4'
appAuth = 'Edmond.Chen'

class PasswdWinForm(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.horizontalSlider.setValue(8)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
        self.label_7.setText(''.join(['生成','{:0>2d}'.format(self.horizontalSlider.value()),'位']))
        self.label_auth.setText(appAuth)
        self.label_ver.setText(appVersion)
        self.levelDict = {'l1':['0','1','2','3','4','5','6','7','8','9'],
                          'l2':['0','1','2','3','4','5','6','7','8','9',
                                'a','b','c','d','e','f','g','h','i','j',
                                'k','l','m','n','o','p','q','r','s','t',
                                'u','v','w','x','y','z'],
                          'l3':['0','1','2','3','4','5','6','7','8','9',
                                'a','b','c','d','e','f','g','h','i','j',
                                'k','l','m','n','o','p','q','r','s','t',
                                'u','v','w','x','y','z',
                                'A','B','C','D','E','F','G','H','I','J',
                                'K','L','M','N','O','P','Q','R','S','T',
                                'U','V','W','X','Y','Z'],
                          'l4':['0','1','2','3','4','5','6','7','8','9',
                                'a','b','c','d','e','f','g','h','i','j',
                                'k','l','m','n','o','p','q','r','s','t',
                                'u','v','w','x','y','z',
                                'A','B','C','D','E','F','G','H','I','J',
                                'K','L','M','N','O','P','Q','R','S','T',
                                'U','V','W','X','Y','Z',
                                '!','$','%','&','_','=','+'],
                          'l5':[['!','$','%','&','_','=','+'],
                                ['a','b','c','d','e','f','g','h','i','j',
                                 'k','l','m','n','o','p','q','r','s','t',
                                 'u','v','w','x','y','z',
                                 'A','B','C','D','E','F','G','H','I','J',
                                 'K','L','M','N','O','P','Q','R','S','T',
                                 'U','V','W','X','Y','Z'],
                                 ['0','1','2','3','4','5','6','7','8','9']]}
        self.levelDesc = {'l1':'可以生成仅包含数字的密码',
                          'l2':'可以生成包含数字和小写字母的密码',
                          'l3':'可以生成包含数字和大小写字母的密码',
                          'l4':'可以生成包含数字、大小写字母和特殊字符的密码，但呈随机出现',
                          'l5':'可以生成包含数字、大小写字母和特殊字符的密码，特殊字符必定出现'}
        self.textBrowser.setText(self.levelDesc['l1'])
        self.comboBox.addItems(self.levelDict.keys())
        self.scEnter = QShortcut(QKeySequence('Enter'),self)
        self.scEnter.activated.connect(self.createPassword)
        self.bind()

    def bind(self):
        self.horizontalSlider.valueChanged.connect(self.flushNum)
        self.comboBox.currentIndexChanged.connect(self.flushDescLabel)
        self.pushButton.clicked.connect(self.createPassword)

    def flushNum(self):
        self.label_7.setText(''.join(['生成','{:0>2d}'.format(self.horizontalSlider.value()),'位']))

    def flushDescLabel(self):
        self.textBrowser.setText(self.levelDesc[self.comboBox.currentText()])

    def createPassword(self):
        self.__passwordLen = self.horizontalSlider.value()
        self.__passwordList = []
        for letnum in range(0,self.__passwordLen):
            if self.comboBox.currentText() == 'l1':
                self.__passwordList.append(choice(self.levelDict['l1']))
            elif self.comboBox.currentText() == 'l2':
                self.__passwordList.append(choice(self.levelDict['l2']))
            elif self.comboBox.currentText() == 'l3':
                self.__passwordList.append(choice(self.levelDict['l3']))
            elif self.comboBox.currentText() == 'l4':
                self.__passwordList.append(choice(self.levelDict['l4']))
            elif self.comboBox.currentText() == 'l5':
                if letnum%3 == 0:
                    self.__passwordList.append(choice(self.levelDict['l5'][1]))
                if letnum%3 == 1:
                    self.__passwordList.append(choice(self.levelDict['l5'][2]))
                if letnum%3 == 2:
                    self.__passwordList.append(choice(self.levelDict['l5'][0]))
        self.__passwordString = ''.join(self.__passwordList)
        self.lineEdit.setText(self.__passwordString)
        copy(self.__passwordString)
        self.wrightDownPassword(passwd = self.__passwordString)

    def wrightDownPassword(self,passwd):
        self.__fileData = open(file='./history/hisPasswd',mode='a')
        self.__fileData.write('{"time":%r , "passwd":%r},\n'%(datetime.now().strftime('%Y-%m-%d  %H:%M:%S'),passwd))
        self.__fileData.close()

if __name__ == '__main__':
    from qt_material import apply_stylesheet
    app = QApplication([])
    win = PasswdWinForm()
    apply_stylesheet(app=app, theme='dark_teal.xml')
    win.show()
    app.exec()