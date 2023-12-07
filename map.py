from dis33 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from database_option import *

class Ui_MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())

    def setupUi(self, KevaCoin):
        KevaCoin.setObjectName("KevaCoin")
        KevaCoin.resize(1196, 796)
        KevaCoin.setStyleSheet("background-image: url(./picture/R-C.jpg);")  #设置背景
        KevaCoin.setWindowIcon(QIcon('./picture/maps.ico'))            #设置图标
        
        self.listWidget = QtWidgets.QListWidget(KevaCoin)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 381, 811))               #设置左侧的半透明
        self.listWidget.setStyleSheet("background-image: url(./picture/changeR-C.jpg);")
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
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")


        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(KevaCoin)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(0, 320, 361, 71))
        self.commandLinkButton_4.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 16pt \"幼圆\";")
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        
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
        self.textEdit.setStyleSheet("background-image: url(./picture/changeR-C.jpg);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(KevaCoin)
        QtCore.QMetaObject.connectSlotsByName(KevaCoin)


#######修改按钮图标
        self.commandLinkButton.setIcon(QIcon('./picture/user.png'))
        self.commandLinkButton_3.setIcon(QIcon('./picture/administrator_lock_open.ico'))
        self.commandLinkButton_4.setIcon(QIcon('./picture/user_full_add_32.ico'))

    


  #修改ui的细节
    def retranslateUi(self, KevaCoin):
        _translate = QtCore.QCoreApplication.translate
        KevaCoin.setWindowTitle(_translate("KevaCoin", "校园地图"))
        self.commandLinkButton.setText(_translate("KevaCoin", "用户"))
        self.commandLinkButton_3.setText(_translate("KevaCoin", "管理员"))
        self.commandLinkButton_4.setText(_translate("KevaCoin", "注册"))
        self.textEdit.setHtml(_translate("KevaCoin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#164350;\">用户您好！</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">在当下，</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">手机地图</span><span style=\" font-size:11pt;\">，已经成为了人们出行必备的app之一，但有的时候</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">地图</span><span style=\" font-size:11pt;\">发挥的功能却差强人意</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">此软件当用户发现校园内由施工或道路修改问题，可让用户记录下修改后的地理位置并上传至</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">管理员</span><span style=\" font-size:11pt;\">，当管理员收到消息后会第一时间核实内容真实性，并</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">实行修改</span><span style=\" font-size:11pt;\">并上传</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">实现实时更新地图操作，可让用户自行投稿最新地图路线，并让管理员审核，</span><span style=\" font-size:11pt; font-weight:600; color:#5555ff;\">解决校园道路经常变换</span><span style=\" font-size:11pt;\">的问题</span></p></body></html>"))



class Login_user(QtWidgets.QMainWindow):
    mySignal = pyqtSignal(object)
    def __init__(self):
        super(Login_user,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())


    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 300)
        Login.setStyleSheet("background-image: url(./picture/未标题-1.jpg);")  #设置背景
        Login.setWindowIcon(QIcon('./picture/maps.ico')) 


#####获取内容



#设置标签

        self.lab_l = QtWidgets.QLabel(Login)
        self.lab_p = QtWidgets.QLabel(Login)
        self.lab_l.setGeometry(QtCore.QRect(90, 60, 50, 50))  
        self.lab_p.setGeometry(QtCore.QRect(90, 120, 50, 50))
        self.lab_l.setObjectName("lab_l")
        self.lab_p.setObjectName("lab_p")  
#设置录入框
        self.Lin_l=QtWidgets.QLineEdit(Login)
        self.Lin_p=QtWidgets.QLineEdit(Login)
        self.Lin_l.setGeometry(QtCore.QRect(150, 70, 250, 30))  
        self.Lin_p.setGeometry(QtCore.QRect(150, 120, 250, 30))
        self.Lin_l.setObjectName("Lin_l") 
        self.Lin_p.setObjectName("Lin_p") 
        self.Lin_p.setEchoMode(QLineEdit.Password)
#设置按钮
        self.Pu_l = QtWidgets.QPushButton(Login) 
        self.Pu_l.setGeometry(QtCore.QRect(180, 170, 361, 71))
        self.Pu_l.setStyleSheet("border-style:none;\n""padding:11px;\n""border-radius:3px;\n""background:transparent;\n""font: 13pt \"幼圆\";")
        self.Pu_l.setIcon(QIcon('./picture/icons8-left-click-48.png'))
        self.Pu_l.setObjectName("Pu_l")
        self.Pu_l.clicked.connect(self.Login)


    def Login(self):
        id_now = self.Lin_l.text()
        key_now = self.Lin_p.text()
        x=check_user_name(self.Lin_l.text())

      
        content = self.Lin_l.text()

        #发送用户id
        
        if x==0:
            self.Lin_l.setText("")
            self.Lin_p.setText("")
            msgBox3 = QMessageBox(QMessageBox.NoIcon, '失败','帐户录入错误！')
            msgBox3.setIconPixmap(QPixmap("./picture/云警告.png"))
            msgBox3.exec()
        elif x==1:
                self.cont = search_user_pass(id_now,key_now)
                self.psw=self.cont[0]
                self.name=self.cont[1]
                if (id_now==self.name and key_now==self.psw):
                        self.mySignal.emit(content)
                        msgBox2 = QMessageBox(QMessageBox.NoIcon, '成功','登陆成功')
                        msgBox2.setIconPixmap(QPixmap("./picture/云成功success(3).png"))
                        msgBox2.exec()
                        Login_user_.close()
                        Main_Window.close()
                        user_.show()

                elif(id_now==self.name and key_now!=self.psw):
                        self.Lin_p.setText("")
                        msgBox3 = QMessageBox(QMessageBox.NoIcon, '失败','密码录入错误!')
                        msgBox3.setIconPixmap(QPixmap("./picture/云警告.png"))
                        msgBox3.exec()







    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "用户登录界面"))
        self.Pu_l.setText(_translate("Login", "登录"))
        self.lab_l.setText(_translate("Login", "账户:"))
        self.lab_p.setText(_translate("Login", "密码:"))

class Login_Administrators(QtWidgets.QMainWindow):

    def __init__(self):
        super(Login_Administrators,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())
        self.Password='12345678'
        self.UserName="abc"
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 300)
        Login.setStyleSheet("background-image: url(./picture/未标题-1.jpg);")  #设置背景
        Login.setWindowIcon(QIcon('./picture/maps.ico')) 


#设置标签

        self.lab_l = QtWidgets.QLabel(Login)
        self.lab_p = QtWidgets.QLabel(Login)
        self.lab_l.setGeometry(QtCore.QRect(90, 60, 50, 50))  
        self.lab_p.setGeometry(QtCore.QRect(90, 120, 50, 50))
        self.lab_l.setObjectName("lab_l")
        self.lab_p.setObjectName("lab_p")  
#设置录入框
        self.Lin_l=QtWidgets.QLineEdit(Login)
        self.Lin_p=QtWidgets.QLineEdit(Login)
        self.Lin_l.setGeometry(QtCore.QRect(150, 70, 250, 30))  
        self.Lin_p.setGeometry(QtCore.QRect(150, 120, 250, 30))
        self.Lin_l.setObjectName("Lin_l") 
        self.Lin_p.setObjectName("Lin_p") 
        self.Lin_p.setEchoMode(QLineEdit.Password)
#设置按钮
        self.Pu_l = QtWidgets.QPushButton(Login) 
        self.Pu_l.setGeometry(QtCore.QRect(180, 170, 361, 71))
        self.Pu_l.setStyleSheet("border-style:none;\n""padding:11px;\n""border-radius:3px;\n""background:transparent;\n""font: 13pt \"幼圆\";")
        self.Pu_l.setIcon(QIcon('./picture/icons8-left-click-48.png'))
        self.Pu_l.setObjectName("Pu_l")
        self.Pu_l.clicked.connect(self.Login)


    def Login(self):
        if (self.Lin_l.text()==self.UserName and self.Lin_p.text()==self.Password):
            msgBox2 = QMessageBox(QMessageBox.NoIcon, '成功','登陆成功')
            msgBox2.setIconPixmap(QPixmap("./picture/云成功success(3).png"))
            msgBox2.exec()
            Main_Window.close()
            Login_Administrators_.close()
            administrator.show()
            #print("登陆成功!!")
        elif(self.Lin_l.text()!=self.UserName):
            self.Lin_l.setText("")
            self.Lin_p.setText("")
            msgBox3 = QMessageBox(QMessageBox.NoIcon, '失败','帐户录入错误！')
            msgBox3.setIconPixmap(QPixmap("./picture/云警告.png"))
            msgBox3.exec()
            #print("帐户录入错误!!")
        elif(self.Lin_p.text()!=self.Password):
            self.Lin_p.setText("")
            msgBox3 = QMessageBox(QMessageBox.NoIcon, '失败','密码录入错误!')
            msgBox3.setIconPixmap(QPixmap("./picture/云警告.png"))
            msgBox3.exec()
            #print("密码录入错误!!")

        #self.commandLinkButton_4.setText(_translate("KevaCoin", "帮助及关于我们"))
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "管理员登录界面"))
        self.Pu_l.setText(_translate("Login", "登录"))
        self.lab_l.setText(_translate("Login", "账户:"))
        self.lab_p.setText(_translate("Login", "密码:"))
class register(QtWidgets.QMainWindow):
    def __init__(self):
        super(register,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())
        self.Password="12345678"
        self.UserName="123"
    def setupUi(self, register_):
        register_.setObjectName("Login")
        register_.resize(500, 300)
        register_.setStyleSheet("background-image: url(./picture/未标题-1.jpg);")  #设置背景
        register_.setWindowIcon(QIcon('./picture/maps.ico')) 


#设置标签

        self.lab_l = QtWidgets.QLabel(register_)
        self.lab_p = QtWidgets.QLabel(register_)
        self.lab_l.setGeometry(QtCore.QRect(90, 60, 50, 50))  
        self.lab_p.setGeometry(QtCore.QRect(90, 120, 50, 50))
        self.lab_l.setObjectName("lab_l")
        self.lab_p.setObjectName("lab_p")  
#设置录入框
        self.Lin_l=QtWidgets.QLineEdit(register_)
        self.Lin_p=QtWidgets.QLineEdit(register_)
        self.Lin_l.setGeometry(QtCore.QRect(150, 70, 250, 30))  
        self.Lin_p.setGeometry(QtCore.QRect(150, 120, 250, 30))
        self.Lin_l.setObjectName("Lin_l") 
        self.Lin_p.setObjectName("Lin_p") 
        self.Lin_p.setEchoMode(QLineEdit.Password)
#设置按钮
        self.Pu_l = QtWidgets.QPushButton(register_) 
        self.Pu_l.setGeometry(QtCore.QRect(180, 170, 361, 71))
        self.Pu_l.setStyleSheet("border-style:none;\n""padding:11px;\n""border-radius:3px;\n""background:transparent;\n""font: 13pt \"幼圆\";")
        self.Pu_l.setIcon(QIcon('./picture/icons8-left-click-48.png'))
        self.Pu_l.setObjectName("Pu_l")
        self.Pu_l.clicked.connect(self.Login)


    def Login(self):
        x=save_data_user(self.Lin_l.text(),self.Lin_p.text())
        
        if x!=0:
            msgBox2 = QMessageBox(QMessageBox.NoIcon, '成功','注册成功'+'您的密码是:'+self.Lin_p.text())
            msgBox2.setIconPixmap(QPixmap("./picture/云成功success(3).png"))
            msgBox2.exec()

            #print("登陆成功!!")
        elif x==0:
            self.Lin_l.setText("")
            self.Lin_p.setText("")
            msgBox3 = QMessageBox(QMessageBox.NoIcon, '失败','此账户已被注册')
            msgBox3.setIconPixmap(QPixmap("./picture/云警告.png"))
            msgBox3.exec()
            #print("帐户录入错误!!")

    def retranslateUi(self, register_):
        _translate = QtCore.QCoreApplication.translate
        register_.setWindowTitle(_translate("register_", "用户注册界面"))
        self.Pu_l.setText(_translate("register_", "注册"))
        self.lab_l.setText(_translate("register_", "账户:"))
        self.lab_p.setText(_translate("register_", "密码:"))

class user(QtWidgets.QMainWindow):
    
    #mySignal = pyqtSignal(object)
    def __init__(self):
        super(user,self).__init__()
        
        self.qlist=[]
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setFixedSize(self.width(), self.height())
        

##########创建UI界面
    def setupUi(self, Form):
        
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 1197, 799))               #设置左侧的半透明
        self.listWidget.setStyleSheet("background-image: url(./picture/changeR-C.jpg);")
        self.listWidget.setObjectName("listWidget")
        #self.layout=QFormLayout()

        Form.setStyleSheet("background-image: url(./picture/未标题-1.jpg);")  #设置背景
        Form.setWindowIcon(QIcon('./picture/maps.ico'))  
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
        self.commandLinkButton_3.setObjectName("commandLinkButton_4")

        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(10, 260, 361, 71))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton_4.setFont(font)
        self.commandLinkButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton_4.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")

        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(10, 190, 361, 71))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton_5.setFont(font)
        self.commandLinkButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton_5.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")



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
        self.lab_l = QtWidgets.QLabel(Form)
        self.lab_l.setGeometry(QtCore.QRect(390, 195, 700, 50))
        self.lab_l.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")
        self.lab_2 = QtWidgets.QLabel(Form)
        self.lab_2.setGeometry(QtCore.QRect(390, 70, 700, 50))
        self.lab_2.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")
        self.lab_3 = QtWidgets.QLabel(Form)
        self.lab_3.setGeometry(QtCore.QRect(680, 70, 700, 50))
        self.lab_3.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 14pt \"幼圆\";")


        self.listView = QtWidgets.QListView(Form)
        #self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stringlistmodel2 = QStringListModel()  # 创建stringlistmodel对象

        self.stringlistmodel2.setStringList(self.qlist)# 把数据赋值到 model 上
        
        self.listView.setModel(self.stringlistmodel2)  # 把 view 和 model 关联


        #self.listView.clicked.connect(self.clickedlist) ###出发事件


        self.listView.setGeometry(QtCore.QRect(480, 200, 690, 500))
        self.listView.setStyleSheet("background-image: url(./picture/未标题-1.jpg)")
        self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn) 
 
        self.listView.setObjectName("listView")


###########加入选择框
        x=read_manager_road()
        t=read_node(x)
        tt=t[0]
        country=list(tt.values())
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(480, 80, 190, 31))
        self.comboBox.addItems(country)
        # self.comboBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        self.comboBox.setStyleSheet("QComboBox {"
                                    "combobox-popup: 0;\n"  # 滚动条设置必需
                                    "border-style:none; "
                                    "padding-left:50px;  "   # 字体距离左边的距离
                                    "width:48px; "
                                    "height:24px; "
                                    "font-size:24px; "
                                    "font-family:PingFangSC-Regular,PingFang SC; "
                                    "font-weight:400; "
                                    #"color:rgba(93,169,255,1);\n"
                                    "line-height:24px; }\n"
                                    
                                    "QComboBox:drop-down {"  # 选择箭头样式
                                    "width:40px;  "
                                    "height:50px; "
                                    "border: none;  "
                                    "subcontrol-position: right center; "  # 位置
                                    "subcontrol-origin: padding;}\n"  # 对齐方式

                                    "QComboBox:down-arrow {"  # 选择箭头，继承drop-down
                                    "border: none; "
                                    "background: transparent; "
                                    "image: url(\"./ui/image/down.png\");}\n"

                                    "QComboBox:down-arrow:pressed { image: url(\"./ui/image/up.png\"); }\n"  # 选择箭头

                                    "QComboBox QAbstractItemView {"  # 下拉选项样式
                                    "color:black; "
                                    "background: transparent; "
                                    "selection-color:rgba(93,169,255,1);"
                                    "selection-background-color: rgba(255,255,255,1);"
                                    "}\n"

                                    "QComboBox QAbstractScrollArea QScrollBar:vertical {"  # 滚动条样式
                                    "width: 6px;\n"
                                    "height: 100px;"
                                    "background-color: transparent;  }\n"

                                    "QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"  # 滚动条样式
                                    "border-radius: 3px;   "
                                    "background: rgba(0,0,0,0.1);}\n"

                                    # "QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"  # 划过滚动条，变化
                                    # "background: rgb(90, 91, 93);}\n"

                                    "QComboBox QScrollBar::add-line::vertical{"  # 滚动条上箭头
                                    "border:none;}"
                                    "QComboBox QScrollBar::sub-line::vertical{"  # 滚动条下箭头
                                    "border:none;}"
                                    "")
        self.comboBox.setMaxVisibleItems(3)
        # self.comboBox.setMaxCount(24456232)
        self.comboBox.setObjectName("comboBox")




        self.comboBox2 = QtWidgets.QComboBox(Form)
        self.comboBox2.setGeometry(QtCore.QRect(774, 80, 190, 31))
        self.comboBox2.addItems(country)
        # self.comboBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        self.comboBox2.setStyleSheet("QComboBox {"
                                    "combobox-popup: 0;\n"  # 滚动条设置必需
                                    "border-style:none; "
                                    "padding-left:50px;  "   # 字体距离左边的距离
                                    "width:48px; "
                                    "height:24px; "
                                    "font-size:24px; "
                                    "font-family:PingFangSC-Regular,PingFang SC; "
                                    "font-weight:400; "
                                    #"color:rgba(93,169,255,1);\n"
                                    "line-height:24px; }\n"
                                    
                                    "QComboBox:drop-down {"  # 选择箭头样式
                                    "width:40px;  "
                                    "height:50px; "
                                    "border: none;  "
                                    "subcontrol-position: right center; "  # 位置
                                    "subcontrol-origin: padding;}\n"  # 对齐方式

                                    "QComboBox:down-arrow {"  # 选择箭头，继承drop-down
                                    "border: none; "
                                    "background: transparent; "
                                    "image: url(\"./ui/image/down.png\");}\n"

                                    "QComboBox:down-arrow:pressed { image: url(\"./ui/image/up.png\"); }\n"  # 选择箭头

                                    "QComboBox QAbstractItemView {"  # 下拉选项样式
                                    "color:black; "
                                    "background: transparent; "
                                    "selection-color:rgba(93,169,255,1);"
                                    "selection-background-color: rgba(255,255,255,1);"
                                    "}\n"

                                    "QComboBox QAbstractScrollArea QScrollBar:vertical {"  # 滚动条样式
                                    "width: 6px;\n"
                                    "height: 100px;"
                                    "background-color: transparent;  }\n"

                                    "QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"  # 滚动条样式
                                    "border-radius: 3px;   "
                                    "background: rgba(0,0,0,0.1);}\n"

                                    # "QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"  # 划过滚动条，变化
                                    # "background: rgb(90, 91, 93);}\n"

                                    "QComboBox QScrollBar::add-line::vertical{"  # 滚动条上箭头
                                    "border:none;}"
                                    "QComboBox QScrollBar::sub-line::vertical{"  # 滚动条下箭头
                                    "border:none;}"
                                    "")
        self.comboBox2.setMaxVisibleItems(3)
        # self.comboBox.setMaxCount(24456232)
        self.comboBox2.setObjectName("comboBox2")





###########显示所有命名空间



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

###########修改按钮图标
        self.commandLinkButton.setIcon(QIcon('./picture/icons8-back-to-48.png'))
        self.commandLinkButton_2.setIcon(QIcon('./picture/edit.ico'))
        self.commandLinkButton_3.setIcon(QIcon('./picture/network_up.ico'))
        self.commandLinkButton_4.setIcon(QIcon('./picture/icons8-search-64.png'))
        self.commandLinkButton_5.setIcon(QIcon('./picture/icons8-refresh-30.png'))
###########按钮的实现
        #self.commandLinkButton_2.clicked.connect(self.change_password)
        self.commandLinkButton_2.clicked.connect(self.change_password)
        self.commandLinkButton_4.clicked.connect(self.search)
        self.commandLinkButton_3.clicked.connect(self.upload)
        self.commandLinkButton_5.clicked.connect(self.refresh)
    def refresh(self):
        try:
                xxx=read_manager_road()
                ttt=read_node(xxx)
                tttt=ttt[0]
                country2=list(tttt.values())
                self.comboBox.addItems(country2)
                self.comboBox2.addItems(country2)
        except:
                print('错误')
    def gett(self,id):
        self.id_=id


    def search(self):
        try:
                self.plist=[]
                self.stringlistmodel2.setStringList(self.plist)
                self.listView.setModel(self.stringlistmodel2)  
                data=read_manager_road()

                start=self.comboBox.currentText()
                end=self.comboBox2.currentText()
                road=query_path(data,start,end)
                for i in range(len(road)):
                        kw=road[i]
                        row=self.stringlistmodel2.rowCount()
                        self.stringlistmodel2.insertRow(row)
                        self.stringlistmodel2.setData(self.stringlistmodel2.index(row),kw)
        except:
                pass


        

########修改密码

    def change_password(self):
        
        old_password,okPressed = QInputDialog.getText(self, "Get text","请输入原始和密码:", QLineEdit.Normal,"")
        if (okPressed and old_password != ''):
            new_password,okPressed = QInputDialog.getText(self, "Get text","请输入新密码", QLineEdit.Normal,"")
            if (okPressed and new_password != ''):
                xx=change_key(self.id_,old_password,new_password)
                if xx==1:
                        msgBox2 = QMessageBox(QMessageBox.NoIcon, '成功','修改成功')
                        msgBox2.setIconPixmap(QPixmap("./picture/云成功success(3).png"))
                        msgBox2.exec()
                elif xx==0:
                        msgBox3 = QMessageBox(QMessageBox.NoIcon, '失败','密码输入入错误!')
                        msgBox3.setIconPixmap(QPixmap("./picture/云警告.png"))
                        msgBox3.exec()


        




#############上传道路信息
    def upload(self):
        upload_.show()







    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户界面"))
        self.commandLinkButton.setText(_translate("Form", "返回首页"))
        self.commandLinkButton_3.setText(_translate("Form", "上传地图"))
        self.commandLinkButton_2.setText(_translate("Form", "修改密码"))
        self.commandLinkButton_4.setText(_translate("Form", "查询"))
        self.commandLinkButton_5.setText(_translate("Form", "刷新"))

        self.lab_l.setText(_translate("Form", "路线:"))
        self.lab_2.setText(_translate("Form", "起始:"))
        self.lab_3.setText(_translate("Form", "终点:"))
class administration(QtWidgets.QMainWindow):
    #mySignal = pyqtSignal(object)
    def __init__(self):
        super(administration,self).__init__()
        
 
        
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setFixedSize(self.width(), self.height())
        

##########创建UI界面
    def setupUi(self, ad):

        #self.layout=QFormLayout()

        ad.setStyleSheet("background-image: url(./picture/changeR-C.jpg);")  #设置背景
        ad.setWindowIcon(QIcon('./picture/maps.ico'))  
        ad.setObjectName("ad")
        ad.resize(1197, 799)
        ad.setContextMenuPolicy(QtCore.Qt.NoContextMenu)



########设置按钮
        self.commandLinkButton = QtWidgets.QCommandLinkButton(ad)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 30, 361, 71))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton.setStyleSheet("border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;\n"
"font: 16pt \"幼圆\";")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(ad)
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



###########设置线条
        self.line = QtWidgets.QFrame(ad)
        self.line.setGeometry(QtCore.QRect(0, 90, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(ad)
        self.line_2.setGeometry(QtCore.QRect(120, 90, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")



##########设置竖线
        self.line_3 = QtWidgets.QFrame(ad)
        self.line_3.setGeometry(QtCore.QRect(380, 0, 3, 800))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")



#########设置显示钱包空间栏
        self.listView = QtWidgets.QListView(ad)
        self.qlist=[]
        self.stringlistmodel_file = QStringListModel()  # 创建stringlistmodel对象

        self.stringlistmodel_file.setStringList(self.qlist)# 把数据赋值到 model 上
        
        self.listView.setModel(self.stringlistmodel_file)  # 把 view 和 model 关联


        self.listView.clicked.connect(self.clickedlist) ###出发事件




        self.listView.setGeometry(QtCore.QRect(450, 50, 700, 700))
        self.listView.setStyleSheet("background-image: url(./picture/未标题-1.jpg)")
        self.listView.setObjectName("listView")

###########显示所有命名空间



        self.retranslateUi(ad)
        QtCore.QMetaObject.connectSlotsByName(ad)

###########修改按钮图标
        self.commandLinkButton.setIcon(QIcon('./picture/icons8-back-to-48.png'))
        self.commandLinkButton_2.setIcon(QIcon('./picture/icons8-search-64.png'))
        #self.commandLinkButton_3.setIcon(QIcon('./picture/icons8-connect-48.png'))

###########按钮的实现
        self.commandLinkButton_2.clicked.connect(self.search)


############刷新
    def search(self):
        self.plist=[]
        self.stringlistmodel_file.setStringList(self.plist)
        self.listView.setModel(self.stringlistmodel_file)
        li=manager_check_user_road_mes()

        for _ in range(len(li)):
                kw=f'起始点:{li[_][0]} ，终点:{li[_][1]} ，方向:{li[_][2]} ，距离:{li[_][3]}米'
                self.plist.append(li[_])
                row=self.stringlistmodel_file.rowCount()
                self.stringlistmodel_file.insertRow(row)
                self.stringlistmodel_file.setData(self.stringlistmodel_file.index(row),kw)

############添加账户


#############创建listview事件
    
    def clickedlist(self, qModelIndex):
        text,ok=QInputDialog.getText(self,'添加道路信息','是否添加此条道路？是请填yes，否填no')
        if ok and text=='yes':
                content=[]
                content = self.plist[qModelIndex.row()]
                print(content)
                save_data_road_manager(content[0],content[1],content[2],content[3])
                index = self.listView.currentIndex()
                self.stringlistmodel_file.removeRow(index.row())
                pp=qModelIndex.row()
                self.plist.remove(self.plist[pp])
 
                msgBox = QMessageBox(QMessageBox.NoIcon, '成功','添加成功！')
                msgBox.setWindowIcon(QIcon('./picture/maps.ico'))
                msgBox.setIconPixmap(QPixmap("./picture/云成功success(3).png"))
                msgBox.exec()






    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kevacoin Storage"))
        self.commandLinkButton.setText(_translate("Form", "返回首页"))
        #self.commandLinkButton_3.setText(_translate("Form", "帮助提示"))

        self.commandLinkButton_2.setText(_translate("Form", "刷新"))

class Upload(QtWidgets.QMainWindow):
    def __init__(self):
        super(Upload,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())


    def setupUi(self, Upload_):

        Upload_.setObjectName("Login")
        Upload_.resize(500, 300)
        Upload_.setStyleSheet("background-image: url(./picture/未标题-1.jpg);")  #设置背景
        Upload_.setWindowIcon(QIcon('./picture/maps.ico')) 


#####获取内容



#设置标签

        self.be_now = QtWidgets.QLabel(Upload_)
        self.en_now = QtWidgets.QLabel(Upload_)
        self.dir_now = QtWidgets.QLabel(Upload_)
        self.dis_now = QtWidgets.QLabel(Upload_)
        self.be_now.setGeometry(QtCore.QRect(75, 20, 50, 50)) ###起始点 
        self.en_now.setGeometry(QtCore.QRect(75, 80, 50, 50)) ###终点
        self.dir_now.setGeometry(QtCore.QRect(75, 140, 50, 50)) ###方向
        self.dis_now.setGeometry(QtCore.QRect(75, 200, 70, 50)) ###距离
        self.be_now.setObjectName("be_now")
        self.en_now.setObjectName("en_now")  
        self.dir_now.setObjectName("dir_now")  
        self.dis_now.setObjectName("dis_now")  
#设置录入框
        self.Lin_be_now=QtWidgets.QLineEdit(Upload_)
        self.Lin_en_now=QtWidgets.QLineEdit(Upload_)
        self.Lin_be_now.setGeometry(QtCore.QRect(150, 30, 250, 30))  
        self.Lin_en_now.setGeometry(QtCore.QRect(150, 90, 250, 30))
        self.Lin_be_now.setObjectName("Lin_be_now") 
        self.Lin_en_now.setObjectName("Lin_en_now")
        self.Lin_be_now.setPlaceholderText("实例:图书馆")
        self.Lin_en_now.setPlaceholderText("实例:申一教室")





        self.Lin_dir_now=QtWidgets.QLineEdit(Upload_)
        self.Lin_dis_now=QtWidgets.QLineEdit(Upload_)
        self.Lin_dir_now.setGeometry(QtCore.QRect(150, 150, 250, 30))  
        self.Lin_dis_now.setGeometry(QtCore.QRect(150, 210, 250, 30))
        self.Lin_dir_now.setObjectName("Lin_dir_now") 
        self.Lin_dis_now.setObjectName("Lin_dis_now") 
        self.Lin_dir_now.setPlaceholderText("实例:南")
        self.Lin_dis_now.setPlaceholderText("实例:100")
#设置按钮
        self.Pu_l = QtWidgets.QPushButton(Upload_) 
        self.Pu_l.setGeometry(QtCore.QRect(180, 230, 361, 71))
        self.Pu_l.setStyleSheet("border-style:none;\n""padding:11px;\n""border-radius:3px;\n""background:transparent;\n""font: 13pt \"幼圆\";")
        self.Pu_l.setIcon(QIcon('./picture/icons8-left-click-48.png'))
        self.Pu_l.setObjectName("Pu_l")
        self.Pu_l.clicked.connect(self.Uploaded)


    def Uploaded(self):
        m=self.Lin_dis_now.text()
        try:
                save_data_road_user(self.Lin_be_now.text(),self.Lin_en_now.text(),self.Lin_dir_now.text(),int(m))
                tes_dic = ''
                if self.Lin_dir_now.text()=='东':
                        tes_dic = '西'
                if self.Lin_dir_now.text()=='西':
                        tes_dic = '东'
                if self.Lin_dir_now.text()=='南':
                        tes_dic = '北'
                if self.Lin_dir_now.text()=='北':
                        tes_dic = '南'
                if self.Lin_dir_now.text()=='东北':
                        tes_dic = '西南'
                if self.Lin_dir_now.text()=='西北':
                        tes_dic = '东南'
                if self.Lin_dir_now.text()=='西南':
                        tes_dic = '东北'
                if self.Lin_dir_now.text()=='东南':
                        tes_dic = '西北'
                save_data_road_user(self.Lin_en_now.text(),self.Lin_be_now.text(),tes_dic,int(m))
                msgBox = QMessageBox(QMessageBox.NoIcon, '成功','上传成功！')
                msgBox.setWindowIcon(QIcon('./picture/maps.ico'))
                msgBox.setIconPixmap(QPixmap("./picture/云成功success(3).png"))
                msgBox.exec()
                self.Lin_be_now.setText("")
                self.Lin_en_now.setText("")
                self.Lin_dir_now.setText("")
                self.Lin_dis_now.setText("")
        except:
                msgBox = QMessageBox(QMessageBox.NoIcon, '失败','请填写正确格式！')
                msgBox.setWindowIcon(QIcon('./picture/maps.ico'))
                msgBox.setIconPixmap(QPixmap("./picture/云警告.png"))
                msgBox.exec()






    def retranslateUi(self, Upload_):
        _translate = QtCore.QCoreApplication.translate
        Upload_.setWindowTitle(_translate("Login", "上传道路信息"))
        self.Pu_l.setText(_translate("Login", "上传"))
        self.be_now.setText(_translate("Login", "起点:"))
        self.en_now.setText(_translate("Login", "终点:"))
        self.dir_now.setText(_translate("Login", "方向:"))
        self.dis_now.setText(_translate("Login", "距离(m):"))



if __name__ == '__main__':
    create_table()
    app = QApplication(sys.argv)
    Main_Window=Ui_MainWindow()
    Login_user_=Login_user()
    Login_Administrators_=Login_Administrators()
    user_=user()
    administrator=administration()
    register_=register()
    upload_=Upload()


    Main_Window.show()
    Main_Window.commandLinkButton.clicked.connect(Login_user_.show)
    Main_Window.commandLinkButton_4.clicked.connect(register_.show)
    Main_Window.commandLinkButton_3.clicked.connect(Login_Administrators_.show)
    user_.commandLinkButton.clicked.connect(Main_Window.show)
    user_.commandLinkButton.clicked.connect(user_.close)

    administrator.commandLinkButton.clicked.connect(administrator.close)
    administrator.commandLinkButton.clicked.connect(Main_Window.show)
    Login_user_.mySignal.connect(user_.gett)
    data=read_manager_road()
    print(data)
    sys.exit(app.exec())