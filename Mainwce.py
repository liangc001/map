##


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sys,os
import time
import io,binascii,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from kevacoin_lib import *
from kevacoin_tools import *



class Ui_MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())

    def setupUi(self, KevaCoin):
        KevaCoin.setObjectName("KevaCoin")
        KevaCoin.resize(1196, 796)
        KevaCoin.setStyleSheet("background-image: url(./GUI---PYQT5/p/R-C.jpg);")  #设置背景
        KevaCoin.setWindowIcon(QIcon('./GUI---PYQT5/p/rainbow.ico'))            #设置图标
        
        self.listWidget = QtWidgets.QListWidget(KevaCoin)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 381, 811))               #设置左侧的半透明
        self.listWidget.setStyleSheet("background-image: url(./GUI---PYQT5/p/changeR-C.jpg);")
        self.listWidget.setObjectName("listWidget")

###########设置三个菜单按钮
        self.commandLinkButton = QtWidgets.QCommandLinkButton(KevaCoin) 
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 120, 361, 71))
        self.commandLinkButton.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 16pt \"幼圆\";")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(KevaCoin)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(0, 220, 361, 71))
        self.commandLinkButton_3.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 16pt \"幼圆\";")
#         self.commandLinkButton_3.setObjectName("commandLinkButton_3")
#         self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(KevaCoin)
#         self.commandLinkButton_4.setGeometry(QtCore.QRect(0, 320, 361, 71))
#         self.commandLinkButton_4.setStyleSheet("border-style:none;\n"
# "padding:11px;\n"
# "border-radius:3px;\n"
# "background:transparent;\n"
# "font: 16pt \"幼圆\";")
#         self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        
############设置三条分割线
        self.line_4 = QtWidgets.QFrame(KevaCoin)
        self.line_4.setGeometry(QtCore.QRect(10, 200, 118, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(KevaCoin)
        self.line_5.setGeometry(QtCore.QRect(10, 300, 118, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

##############设置小tips文本框
        self.textEdit = QtWidgets.QTextEdit(KevaCoin)
        self.textEdit.setGeometry(QtCore.QRect(420, 50, 741, 301))
        self.textEdit.setStyleSheet("background-image: url(./GUI---PYQT5/p/changeR-C.jpg);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(KevaCoin)
        QtCore.QMetaObject.connectSlotsByName(KevaCoin)


#######修改按钮图标
        self.commandLinkButton.setIcon(QIcon('./GUI---PYQT5/p/icons8-kakashi-hatake-48.png'))
        self.commandLinkButton_3.setIcon(QIcon('./GUI---PYQT5/p/icons8-opened-folder-48.png'))
        #self.commandLinkButton_4.setIcon(QIcon('./GUI---PYQT5/p/icons8-connect-48.png'))

    


  #修改ui的细节
    def retranslateUi(self, KevaCoin):
        _translate = QtCore.QCoreApplication.translate
        KevaCoin.setWindowTitle(_translate("KevaCoin", "Kevacoin Storage"))
        self.commandLinkButton.setText(_translate("KevaCoin", "命名空间"))
        self.commandLinkButton_3.setText(_translate("KevaCoin", "你的文件"))
        #self.commandLinkButton_4.setText(_translate("KevaCoin", "帮助及关于我们"))
        self.textEdit.setHtml(_translate("KevaCoin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#164350;\">小Tips：</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">此软件基于</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">区块链技术</span><span style=\" font-size:11pt;\">，用于</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">永久储存</span><span style=\" font-size:11pt;\">小型文件（比较重要的word，excel，ppt文件）</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">此软件改良了</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">账号密码机制</span><span style=\" font-size:11pt;\">，只需要创建自己想要的</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">命名空间</span><span style=\" font-size:11pt;\">（相当于账号）即可使用</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">如有软件的使用问题请在每个窗口中点击</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">'帮助'</span><span style=\" font-size:11pt;\">即可</span></p></body></html>"))


class user(QtWidgets.QMainWindow):
    mySignal = pyqtSignal(object)
    def __init__(self):
        super(user,self).__init__()
        
        self.qlist=[]
        
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setFixedSize(self.width(), self.height())
        

##########创建UI界面
    def setupUi(self, Form):

        #self.layout=QFormLayout()

        Form.setStyleSheet("background-image: url(./GUI---PYQT5/p/changeR-C.jpg);")  #设置背景
        Form.setWindowIcon(QIcon('./GUI---PYQT5/p/rainbow.ico'))  
        Form.setObjectName("Form")
        Form.resize(1197, 799)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)



########设置按钮
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 30, 361, 71))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 16pt \"幼圆\";")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(10, 330, 361, 71))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton_2.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")

        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(10, 400, 361, 71))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton_3.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")

##########设置输入框
        #self.lineEdit1=QLineEdit()

###########设置线条
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 90, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(120, 90, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")



##########设置竖线
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(380, 0, 3, 800))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")



#########设置显示钱包空间栏

        self.listView = QtWidgets.QListView(Form)
        #self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stringlistmodel2 = QStringListModel()  # 创建stringlistmodel对象

        self.stringlistmodel2.setStringList(self.qlist)# 把数据赋值到 model 上
        
        self.listView.setModel(self.stringlistmodel2)  # 把 view 和 model 关联


        self.listView.clicked.connect(self.clickedlist) ###出发事件


        self.listView.setGeometry(QtCore.QRect(450, 50, 700, 700))
        self.listView.setStyleSheet("background-image: url(./GUI---PYQT5/p/未标题-1.jpg)")
        self.listView.setObjectName("listView")

###########显示所有命名空间
        for _ in list_namespace():
                self.qlist.append(_.split(':')[-1])
        for _ in range(len(self.qlist)):
                row2 = self.stringlistmodel2.rowCount()
                pw=list_namespace()
                self.stringlistmodel2.insertRow(row2)
                self.stringlistmodel2.setData(self.stringlistmodel2.index(row2), pw[_])


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

###########修改按钮图标
        self.commandLinkButton.setIcon(QIcon('./GUI---PYQT5/p/icons8-back-to-48.png'))
        self.commandLinkButton_2.setIcon(QIcon('./GUI---PYQT5/p/icons8-add-user-male-48.png'))
        self.commandLinkButton_3.setIcon(QIcon('./GUI---PYQT5/p/icons8-connect-48.png'))

###########按钮的实现
        self.commandLinkButton_2.clicked.connect(self.bulid_kw)
        self.commandLinkButton_3.clicked.connect(self.message)

    def message(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, '提示','温馨提示:用户(短号)创建需要2~3分钟,请耐心等待')
        msgBox.setWindowIcon(QIcon('./GUI---PYQT5/p/rainbow.ico'))
        msgBox.setIconPixmap(QPixmap("./GUI---PYQT5/p/icons8-connect-48.png"))
        msgBox.exec()
############创建账户
    def bulid_kw(self):
        """
        把 编辑栏 line_edit 中的 字符添加到 listmodel 中
        :return:
        """
        text,ok=QInputDialog.getText(self,'创建','提示:ID名小于等于4个字')
        if ok and text: 
                namespace=create_namespace(text)
                row = self.stringlistmodel2.rowCount()
                kw = f'命名空间名称:{text}，短号:正在生成中，命名空间ID:{namespace}'
                self.qlist.append(namespace)
                self.stringlistmodel2.insertRow(row)
                self.stringlistmodel2.setData(self.stringlistmodel2.index(row), kw)

############添加账户

    def add_kw(self):
        
        pass

#############创建listview事件
    
    def clickedlist(self, qModelIndex):
        
        content = self.qlist[qModelIndex.row()]
        self.mySignal.emit(content)
        #print(content)
        user_Window.close()

        file_Window.show()





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kevacoin Storage"))
        self.commandLinkButton.setText(_translate("Form", "返回首页"))
        self.commandLinkButton_3.setText(_translate("Form", "帮助提示"))

        self.commandLinkButton_2.setText(_translate("Form", "创建账户"))



class File(Ui_MainWindow,user):
    mySignal1 = pyqtSignal(object)
    def __init__(self):
        #super(File,self).__init__()
        user.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.cwd = os.getcwd()

##########创建UI界面
    def setupUi(self, File1):

        #self.layout=QFormLayout()

        File1.setStyleSheet("background-image: url(./GUI---PYQT5/p/changeR-C.jpg);")  #设置背景
        File1.setWindowIcon(QIcon('./GUI---PYQT5/p/rainbow.ico'))  
        File1.setObjectName("File1")
        File1.resize(1197, 799)
        File1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)



########设置按钮
        self.commandLinkButton = QtWidgets.QCommandLinkButton(File1)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 30, 361, 71))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 16pt \"幼圆\";")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(File1)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(10, 330, 371, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton_2.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")

        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(File1)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(1060, 90, 250, 50))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton_3.setStyleSheet("border-style:none;\n""padding:11px;\n""border-radius:3px;\n""background:transparent;\n""font: 14pt \"幼圆\";")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        #self.commandLinkButton_3.setToolTip('查询前请先点击清除~')

        self.commandLinkButton4 = QtWidgets.QPushButton(File1)
        self.commandLinkButton4.setGeometry(QtCore.QRect(325, 70, 371, 81))
        self.commandLinkButton4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton4.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 16pt \"幼圆\";")
        self.commandLinkButton4.setObjectName("commandLinkButton")

        self.commandLinkButton5 = QtWidgets.QCommandLinkButton(File1)
        self.commandLinkButton5.setGeometry(QtCore.QRect(930, 90, 95, 50))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton5.setFont(font)
        self.commandLinkButton5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton5.setStyleSheet("border-style:none;\n""padding:11px;\n""border-radius:3px;\n""background:transparent;\n""font: 14pt \"幼圆\";")
        self.commandLinkButton5.setObjectName("commandLinkButton_3")

        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(File1)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 400, 371, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton_6.setFont(font)
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton_6.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")



##########设置输入框
        self.lineEdit1=QLineEdit(File1)
        self.lineEdit1.setGeometry(QtCore.QRect(590,95,330,40))
        self.lineEdit1.setObjectName("lineEdit1")
        #self.lineEdit1.setText(str(user.qlist))

###########设置线条
        self.line = QtWidgets.QFrame(File1)
        self.line.setGeometry(QtCore.QRect(0, 90, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(File1)
        self.line_2.setGeometry(QtCore.QRect(120, 90, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")



##########设置竖线
        self.line_3 = QtWidgets.QFrame(File1)
        self.line_3.setGeometry(QtCore.QRect(380, 0, 3, 800))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")



#########设置显示钱包空间栏

        self.listView = QtWidgets.QListView(File1)
        #self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.plist=[]
        self.stringlistmodel_file = QStringListModel()  # 创建stringlistmodel对象

        self.stringlistmodel_file.setStringList(self.plist)# 把数据赋值到 model 上
        
        self.listView.setModel(self.stringlistmodel_file)  # 把 view 和 model 关联

        self.listView.clicked.connect(self.clickedlist) ###出发事件


        self.listView.setGeometry(QtCore.QRect(450, 150, 700, 600))
        self.listView.setStyleSheet("background-image: url(./GUI---PYQT5/p/未标题-1.jpg)")
        self.listView.setObjectName("listView")


        self.retranslateUi(File1)
        QtCore.QMetaObject.connectSlotsByName(File1)

###########修改按钮图标
        self.commandLinkButton.setIcon(QIcon('./GUI---PYQT5/p/icons8-back-to-48.png'))
        self.commandLinkButton_2.setIcon(QIcon('./GUI---PYQT5/p/icons8-upload-to-cloud-32.png'))
        self.commandLinkButton_3.setIcon(QIcon('./GUI---PYQT5/p/icons8-search-64.png'))
        self.commandLinkButton5.setIcon(QIcon('./GUI---PYQT5/p/icons8-delete-30.png'))
        self.commandLinkButton_6.setIcon(QIcon('./GUI---PYQT5/p/icons8-connect-48.png'))
        

###########按钮的实现
        self.commandLinkButton_2.clicked.connect(self.open_file)
        self.commandLinkButton_3.clicked.connect(self.search)
        self.commandLinkButton5.clicked.connect(self.delete_kw)
        self.commandLinkButton_6.clicked.connect(self.message)


########弹出帮助对话框
    def message(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, '提示','下载请单击右边文件~ ')
        msgBox.setWindowIcon(QIcon('./GUI---PYQT5/p/rainbow.ico'))
        msgBox.setIconPixmap(QPixmap("./GUI---PYQT5/p/icons8-connect-48.png"))
        msgBox.exec()



#########接受信号
    def gett(self,msg):
        #print(msg+'12333333333')
        self.lineEdit1.setText(msg)


############上传文件
    def open_file(self):
        namespace=self.lineEdit1.text()
        self.mySignal1.emit(namespace)
        example1.show()


        
        
        #if fileName_choose == "":
         #   print("\n取消选择")
          #  return

        #print("\n你选择的文件为:")
        #print(fileName_choose[0])



############搜寻
    def search(self):
        #size=self.listView.size()
        #row0=self.stringlistmodel_file.rowCount()

        self.plist=[]
        self.stringlistmodel_file.setStringList(self.plist)
        self.listView.setModel(self.stringlistmodel_file)

        #print(size)
        if self.lineEdit1.text()!='':
                try:
                        if self.lineEdit1.text()[0]!='N':#当输入短号的情况下，需要转成ID
                                self.lineEdit1.setText(convert_shortcode_to_namespaceid(self.lineEdit1.text()))
                        li=list(show_content_of_namespace(self.lineEdit1.text()).values())
                        for i in range(len(li)):
                                kw=li[i]
                                row=self.stringlistmodel_file.rowCount()
                                self.stringlistmodel_file.insertRow(row)
                                self.stringlistmodel_file.setData(self.stringlistmodel_file.index(row),kw)
                except Exception as e:
                        msgBox = QMessageBox(QMessageBox.NoIcon, '错误',str(e))
                        msgBox.setIconPixmap(QPixmap("./GUI---PYQT5/p/云警告.png"))
                        msgBox.exec()
        else:
                msgBox = QMessageBox(QMessageBox.NoIcon, '提示','请输入命名空间!')
                msgBox.setIconPixmap(QPixmap("./GUI---PYQT5/p/云警告.png"))
                msgBox.exec()


#############删除
    def delete_kw(self):
        """删除 listmodel 中选中的项"""
        self.lineEdit1.setText('')

        # index = self.listView.currentIndex()
        # #print(index.row())
        # self.stringlistmodel_file.removeRow(index.row())

        # selected=self.listView.selectedIndexes()
        # selectindex = self.listView.currentIndex()
        # li=list(show_content_of_namespace(self.lineEdit1.text()).values())
        # for i in range(len(li)):
        #         row=self.stringlistmodel_file.rowCount()
        #         self.stringlistmodel_file.removeRow(i.row())

        # kw2='下载请单击下列文件,但别单击这一行~'
        # row3=self.stringlistmodel_file.rowCount()
        # self.stringlistmodel_file.insertRow(row3)
        # self.stringlistmodel_file.setData(self.stringlistmodel_file.index(row3),kw2)







#############创建listview事件(下载)

    def clickedlist(self, qModelIndex):
        hash=list(show_content_of_namespace(self.lineEdit1.text()).keys())
        qModelIndex.row()-1####索引
        # print(hash)
        # print(qModelIndex.row()-1)
        # print(hash[ qModelIndex.row()-1])
        if has_password(self.lineEdit1.text(),hash[qModelIndex.row()]):
                psw2,ok=QInputDialog.getText(self,'输入密码','输入密码？ok/cancel')
                if psw2 and ok:
                        psw2=psw2
        else:
                psw2=None




        
        file_name = QtWidgets.QFileDialog.getExistingDirectory(None, "Select File Directory to Save File", "")
        code=download(file_name,self.lineEdit1.text(),hash[qModelIndex.row()],password=psw2)
        if (code)!=0:
                msgBox2 = QMessageBox(QMessageBox.NoIcon, '失败','下载失败')
                msgBox2.setIconPixmap(QPixmap("./GUI---PYQT5/p/云警告.png"))
                msgBox2.exec()
                #print('Error!Code is:',code)
        elif code == 0 and file_name!='':
                msgBox2 = QMessageBox(QMessageBox.NoIcon, '成功','下载成功')
                msgBox2.setIconPixmap(QPixmap("./GUI---PYQT5/p/云成功success(3).png"))
                msgBox2.exec()



    def retranslateUi(self, File1):
        _translate = QtCore.QCoreApplication.translate
        File1.setWindowTitle(_translate("File1", "Kevacoin Storage"))
        self.commandLinkButton.setText(_translate("File1", "返回首页"))
        self.commandLinkButton_2.setText(_translate("File1", "上传文件"))
        self.commandLinkButton_3.setText(_translate("File1", "查询"))
        self.commandLinkButton4.setText(_translate("File1", "命名空间:"))
        self.commandLinkButton5.setText(_translate("File1", "清除"))
        self.commandLinkButton_6.setText(_translate("File1", "帮助"))



class Example(QtWidgets.QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cwd = os.getcwd()
        self.retranslateUi(self)
  
    # method for creating widgets
    def setupUi(self, File2):

        #self.layout=QFormLayout()

        File2.setStyleSheet("background-image: url(./GUI---PYQT5/p/changeR-C.jpg);")  #设置背景
        File2.setWindowIcon(QIcon('./GUI---PYQT5/p/rainbow.ico'))  
        File2.setObjectName("File2")
        File2.resize(400, 150)
        File2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)


        self.btn = QtWidgets.QPushButton(File2)
        self.btn.setGeometry(QtCore.QRect(89, 90, 100, 25))
        self.btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.btn.clicked.connect(self.doAction)
        self.lab = QLabel("进度:", File2)
        self.lab.setGeometry(30,40,50,25)    

        self.pbar = QProgressBar(File2)
        self.pbar.setGeometry(88, 40, 300, 25)




        



    def gett(self,namespace1):
            self.namespac=namespace1   

  


  
    # when button is pressed this method is being called
    def doAction(self):
        namespace=self.namespac
        psw,ok=QInputDialog.getText(self,'设置密码','是否加密码？ok/cancel')
        if psw and ok:
            psw=psw
        else:
            psw=None

        file_describe,ok=QInputDialog.getText(self,'添加文件描述','是否添加文件描述？ok/cancel')
        if file_describe and ok:
            file_describe=file_describe
        else:
            file_describe=''

        file_path_1= QFileDialog.getOpenFileName(self,  "选取文件",  self.cwd)  # 设置文件扩展名过滤,用双分号间隔
        
        file_path=file_path_1[0]
        if file_path!='':
            try:
                file_to_upload,file_name,size,compress_flag = compress_7z(file_path,psw)  # 压缩后文件地址以及上传文件的文件名
                strlist = convert_bytes_to_strlist(file_to_upload.getvalue())
                crc32_hash = hex(binascii.crc32(file_to_upload.getvalue()))[2:]  # 要上传的文件的哈希值
                #print(f"共计{len(strlist)}个交易待上传（从0开始）")
                self.pbar.setMaximum(len(strlist))
                for index, part_file in enumerate(strlist):
                    key = f"{str(index)}|{crc32_hash}|{compress_flag}|{size}|{file_name}|{file_describe}"
                    try:
                        write_namespace(namespace, key, part_file)
                        #print(f'第{index+1}个交易上传成功')
                        self.pbar.setValue((index+1))
                    except:
                        #print(f'第{index+1}个交易上传失败，等待1s')
                        time.sleep(1)
                        generate()
                        #print(f'创建新区块，等待3s')
                        time.sleep(3)
                        write_namespace(namespace, key, part_file)
                        #print(f'上传第{index+1}个交易')
                        self.pbar.setValue((index+1))
                file_to_upload.close()
            except Exception as e:
                    pass
        elif file_path=='':
                msgBox2 = QMessageBox(QMessageBox.NoIcon, '错误','请选择上传文件')
                msgBox2.setIconPixmap(QPixmap("./GUI---PYQT5/p/云警告.png"))
                msgBox2.exec()
                
    def retranslateUi(self, File2):
        _translate = QtCore.QCoreApplication.translate
        File2.setWindowTitle(_translate("File2", "上传文件"))
        self.btn.setText(_translate("File2", "上传"))

"""
主函数部分：
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main_Window=Ui_MainWindow()
    user_Window=user()
    file_Window=File()
    example1=Example()

#######显示主页面
    Main_Window.show()

#####页面的切换
    Main_Window.commandLinkButton.clicked.connect(user_Window.show)
    Main_Window.commandLinkButton.clicked.connect(Main_Window.close)
    Main_Window.commandLinkButton_3.clicked.connect(file_Window.show)
    Main_Window.commandLinkButton_3.clicked.connect(Main_Window.close)

    user_Window.commandLinkButton.clicked.connect(Main_Window.show)
    user_Window.commandLinkButton.clicked.connect(user_Window.close)

    file_Window.commandLinkButton.clicked.connect(file_Window.close)
    file_Window.commandLinkButton.clicked.connect(Main_Window.show)


    user_Window.mySignal.connect(file_Window.gett)
    file_Window.mySignal1.connect(example1.gett)


    sys.exit(app.exec())
