from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot,Qt

#메인 윈도우 생성,관리

class Ui_MainWindow(QWidget): #메인 UI 세팅 클래스
    def setupUi(self, MainWindow):#메인 UI 정의 함수
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("")
        MainWindow.resize(1000, 900)
        MainWindow.setStyleSheet("background-color: #ffffff")
        MainWindow.setMaximumSize(QtCore.QSize(1000,900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tool_life_box = QtWidgets.QGroupBox(self.centralwidget)
        self.tool_life_box.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.tool_life_box.setFont(font)
        self.tool_life_box.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_life_box.setObjectName("tool_life_box")
        self.tool_life_box.setMinimumSize(QtCore.QSize(150, 360))
        self.tool_img = QtWidgets.QLabel(self.tool_life_box)
        self.tool_img.setGeometry(QtCore.QRect(94, 20, 360, 360))
        self.tool_img.setMinimumSize(QtCore.QSize(0, 0))
        self.tool_img.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.tool_img.setFont(font)
        self.tool_img.setText("")
        self.tool_img.setObjectName("tool_img")
        self.cut_num = QtWidgets.QLabel(self.tool_life_box)
        self.cut_num.setGeometry(QtCore.QRect(233, 170, 51, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.cut_num.setFont(font)
        self.cut_num.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cut_num.setObjectName("cut_num")
        self.wear = QtWidgets.QLabel(self.tool_life_box)
        self.wear.setGeometry(QtCore.QRect(232, 245, 53, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.wear.setFont(font)
        self.wear.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.wear.setObjectName("wear")
        self.label = QtWidgets.QLabel(self.tool_life_box)
        self.label.setGeometry(QtCore.QRect(200, 130, 140, 41))
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.tool_life_box)
        self.label_2.setGeometry(QtCore.QRect(220, 205, 101, 41))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)

        self.gridLayout_5.addWidget(self.tool_life_box, 0, 0, 1, 1)
        self.info_box = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_box.setFont(font)
        font.setPointSize(25)
        self.info_box.setAlignment(QtCore.Qt.AlignCenter)
        self.info_box.setObjectName("info_box")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.info_box)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.start = QtWidgets.QPushButton(self.info_box)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.gridLayout_10.addWidget(self.start, 1, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.rotate_val = QtWidgets.QLabel(self.info_box)
        self.rotate_val.setFont(font)
        self.rotate_val.setObjectName("rotate_val")
        self.gridLayout_9.addWidget(self.rotate_val, 3, 1, 1, 1)
        self.round_val = QtWidgets.QLabel(self.info_box)
        self.round_val.setObjectName("round_val")
        self.round_val.setFont(font)
        self.gridLayout_9.addWidget(self.round_val, 2, 1, 1, 1)
        self.kind_val = QtWidgets.QLabel(self.info_box)
        self.kind_val.setFont(font)
        self.kind_val.setObjectName("kind_val")
        self.gridLayout_9.addWidget(self.kind_val, 0, 1, 1, 1)
        self.radius_val = QtWidgets.QLabel(self.info_box)
        self.radius_val.setFont(font)
        self.radius_val.setObjectName("radius_val")
        self.gridLayout_9.addWidget(self.radius_val, 1, 1, 1, 1)
        self.radius_val2 = QtWidgets.QLabel(self.info_box)
        self.radius_val2.setFont(font)
        self.radius_val2.setObjectName("radius_val2")
        self.gridLayout_9.addWidget(self.radius_val2, 1, 2, 1, 1)
        self.round_val2 = QtWidgets.QLabel(self.info_box)
        self.round_val2.setFont(font)
        self.round_val2.setObjectName("round_val2")
        self.gridLayout_9.addWidget(self.round_val2, 2, 2, 1, 1)
        self.rotate = QtWidgets.QLabel(self.info_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.rotate.setFont(font)
        self.rotate.setAlignment(QtCore.Qt.AlignCenter)
        self.rotate.setObjectName("rotate")
        self.gridLayout_9.addWidget(self.rotate, 3, 0, 1, 1)

        self.kind = QtWidgets.QLabel(self.info_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.kind.setFont(font)
        self.kind.setAlignment(QtCore.Qt.AlignCenter)
        self.kind.setObjectName("kind")
        self.gridLayout_9.addWidget(self.kind, 0, 0, 1, 1)

        self.radius = QtWidgets.QLabel(self.info_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.radius.setFont(font)
        self.radius.setAlignment(QtCore.Qt.AlignCenter)
        self.radius.setObjectName("rotate")
        self.gridLayout_9.addWidget(self.radius, 1, 0, 1, 1)

        self.round = QtWidgets.QLabel(self.info_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.round.setFont(font)
        self.round.setAlignment(QtCore.Qt.AlignCenter)
        self.round.setObjectName("round")
        self.gridLayout_9.addWidget(self.round, 2, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.info_box, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 3, 0, 1, 1)
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setContentsMargins(-1, -1, 0, -1)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.error_box = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.error_box.setFont(font)
        self.error_box.setAlignment(QtCore.Qt.AlignCenter)
        self.error_box.setObjectName("error_box")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.error_box)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tool_life = QtWidgets.QLabel(self.error_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tool_life.setFont(font)
        self.tool_life.setObjectName("tool_life")
        self.gridLayout_11.addWidget(self.tool_life, 4, 0, 1, 1)
        self.tooler_error_val = QtWidgets.QLabel(self.error_box)
        self.tooler_error_val.setMaximumSize(QtCore.QSize(200, 50))
        self.tooler_error_val.setAlignment(QtCore.Qt.AlignCenter)
        self.tooler_error_val.setText("")
        self.tooler_error_val.setObjectName("tooler_error_val")
        self.gridLayout_11.addWidget(self.tooler_error_val, 0, 1, 1, 1)
        self.matter_val = QtWidgets.QLabel(self.error_box)
        self.matter_val.setMaximumSize(QtCore.QSize(5000, 50))
        self.matter_val.setText("")
        self.matter_val.setObjectName("matter_val")
        self.matter_val.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_11.addWidget(self.matter_val, 2, 1, 1, 1)
        self.tool_life_val = QtWidgets.QLabel(self.error_box)
        self.tool_life_val.setMaximumSize(QtCore.QSize(5000, 50))
        self.tool_life_val.setText("")
        self.tool_life_val.setObjectName("tool_life_val")
        self.tool_life_val.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_11.addWidget(self.tool_life_val, 4, 1, 1, 1)
        self.Def_val = QtWidgets.QLabel(self.error_box)
        self.Def_val.setMaximumSize(QtCore.QSize(5000, 50))
        self.Def_val.setText("")
        self.Def_val.setObjectName("tool_life_val")
        self.Def_val.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_11.addWidget(self.Def_val, 3, 1, 1, 1)
        self.burr_error = QtWidgets.QLabel(self.error_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.burr_error.setFont(font)
        self.burr_error.setObjectName("burr_error")
        self.gridLayout_11.addWidget(self.burr_error, 0, 0, 1, 1)
        self.stopper_error = QtWidgets.QLabel(self.error_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stopper_error.setFont(font)
        self.stopper_error.setObjectName("stopper_error")
        self.gridLayout_11.addWidget(self.stopper_error, 1, 0, 1, 1)
        self.Deformation_error = QtWidgets.QLabel(self.error_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Deformation_error.setFont(font)
        self.Deformation_error.setObjectName("Deformation_error")
        self.gridLayout_11.addWidget(self.Deformation_error, 3, 0, 1, 1)
        self.matter = QtWidgets.QLabel(self.error_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.matter.setFont(font)
        self.matter.setObjectName("matter")
        self.gridLayout_11.addWidget(self.matter, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.ng_good = QtWidgets.QLabel(self.error_box)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.ng_good.setFont(font)
        self.ng_good.setObjectName("ng_good")
        self.ng_good.setMaximumSize(QtCore.QSize(500, 130))
        self.gridLayout_4.addWidget(self.ng_good, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.error_box, 0, 1, 1, 1)
        self.img = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(100)
        self.img.setFont(font)
        self.img.setText("")
        self.img.setObjectName("img")
        self.gridlayout.addWidget(self.img, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridlayout, 2, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_9.addWidget(self.name)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(352, 0))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.verticalLayout_8.addWidget(self.logo)
        self.co_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.co_name.setFont(font)
        self.co_name.setObjectName("co_name")
        self.verticalLayout_8.addWidget(self.co_name)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.camera_rg = QtWidgets.QLabel(self.centralwidget)
        self.camera_rg.setMaximumSize(QtCore.QSize(50, 50))
        self.camera_rg.setText("")
        self.camera_rg.setObjectName("camera_rg")
        self.gridLayout_3.addWidget(self.camera_rg, 3, 1, 1, 1)
        self.server_rg = QtWidgets.QLabel(self.centralwidget)
        self.server_rg.setMaximumSize(QtCore.QSize(50, 50))
        self.server_rg.setText("")
        self.server_rg.setObjectName("server_rg")
        self.gridLayout_3.addWidget(self.server_rg, 2, 1, 1, 1)
        self.server = QtWidgets.QLabel(self.centralwidget)
        self.server.setMaximumSize(QtCore.QSize(100, 300))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.server.setFont(font)
        self.server.setAlignment(QtCore.Qt.AlignCenter)
        self.server.setObjectName("server")
        self.gridLayout_3.addWidget(self.server, 2, 0, 1, 1)
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setMaximumSize(QtCore.QSize(250, 300))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.camera.setFont(font)
        self.camera.setAlignment(QtCore.Qt.AlignCenter)
        self.camera.setObjectName("camera")
        self.gridLayout_3.addWidget(self.camera, 3, 0, 1, 1)

        self.HB = QtWidgets.QLabel(self.centralwidget)
        self.HB.setMaximumSize(QtCore.QSize(100, 300))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.HB.setFont(font)
        self.HB.setAlignment(QtCore.Qt.AlignCenter)
        self.HB.setObjectName("HB")
        self.gridLayout_3.addWidget(self.HB, 0, 0, 1, 1)

        self.HB_Val = QtWidgets.QComboBox(self.centralwidget)
        self.HB_Val.setObjectName("HB_Val")
        self.HB_Val.setMinimumSize(QtCore.QSize(160, 30))
        self.gridLayout_3.addWidget(self.HB_Val, 0, 2, 1, 1)
        self.HB_Val.addItem('A')
        self.HB_Val.addItem('B')
        self.HB_Val.addItem('C')
        self.HB_Val.addItem('D')

        self.Tool_Val = QtWidgets.QComboBox(self.centralwidget)
        self.Tool_Val.setObjectName("HB_Val")
        self.Tool_Val.setMinimumSize(QtCore.QSize(160, 30))
        self.gridLayout_3.addWidget(self.Tool_Val, 1, 2, 1, 1)
        self.Tool_Val.addItem('A')
        self.Tool_Val.addItem('B')
        self.Tool_Val.addItem('C')
        self.Tool_Val.addItem('D')

        self.Tool = QtWidgets.QLabel(self.centralwidget)
        self.Tool.setMaximumSize(QtCore.QSize(100, 300))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Tool.setFont(font)
        self.Tool.setAlignment(QtCore.Qt.AlignCenter)
        self.Tool.setObjectName("Tool")
        self.gridLayout_3.addWidget(self.Tool, 1, 0, 1, 1)

        self.server_info = QtWidgets.QPushButton(self.centralwidget)
        self.server_info.setMinimumSize(QtCore.QSize(160,40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.server_info.setFont(font)
        self.server_info.setObjectName("server_info")
        self.server_info.setStyleSheet("background-color: #dddddd")
        self.gridLayout_3.addWidget(self.server_info, 2, 2, 1, 1)
        self.camera_info = QtWidgets.QPushButton(self.centralwidget)
        self.camera_info.setStyleSheet("background-color: #dddddd")
        self.camera_info.setMinimumSize(QtCore.QSize(160,40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.camera_info.setFont(font)
        self.camera_info.setObjectName("camera_info")
        self.gridLayout_3.addWidget(self.camera_info, 3, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "절단봉 불량검출 프로그램"))
        #MainWindow.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.tool_life_box.setTitle(_translate("MainWindow", "Tool-life"))
        self.cut_num.setText(_translate("MainWindow", "90"))
        self.wear.setText(_translate("MainWindow", "80"))
        self.label.setText(_translate("MainWindow", "절단 횟수"))
        self.label_2.setText(_translate("MainWindow", "마모도"))
        self.info_box.setTitle(_translate("MainWindow", "절단봉 정보"))
        self.start.setText(_translate("MainWindow", "file input"))
        self.rotate_val.setText(_translate("MainWindow", "90   도"))
        self.round_val.setText(_translate("MainWindow", "20cm /"))
        self.round_val2.setText(_translate("MainWindow", "20cm"))
        self.kind_val.setText(_translate("MainWindow", "A 형"))
        self.radius_val.setText(_translate("MainWindow", "10cm /"))
        self.radius_val2.setText(_translate("MainWindow", "10cm"))
        self.rotate.setText(_translate("MainWindow", "- 회전"))
        self.round.setText(_translate("MainWindow", "- 둘레"))
        self.kind.setText(_translate("MainWindow", "- 종류"))
        self.radius.setText(_translate("MainWindow", "- 지름"))
        self.error_box.setTitle(_translate("MainWindow", "불량 검출"))
        self.tool_life.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:25pt;\">툴라이프 수명</span></p></body></html>"))
        self.burr_error.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:25pt;\">B U R R</span></p></body></html>"))
        self.Deformation_error.setText(_translate("MainWindow","<html><head/><body><p align=\"left\"><span style=\" font-size:25pt;\">찍  힘</span></p></body></html>"))
        self.stopper_error.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:25pt;\">(stopper)</span></p></body></html>"))
        self.matter.setText(_translate("MainWindow", "<html><head/><body><p align=\"left\"><span style=\" font-size:25pt;\">기  공</span></p></body></html>"))
        self.ng_good.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:45pt;\">NG / GOOD</span></p></body></html>"))
        self.name.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">절단봉 불량 검출</p><p align=\"center\">프로그램</p></body></html>"))
        pixmap = QtGui.QPixmap('img/logo.PNG')
        pixmap = pixmap.scaledToWidth(120)
        #self.logo.setPixmap(pixmap)
        #self.logo.setAlignment(Qt.AlignHCenter)
        #pixmap_co = QtGui.QPixmap('img/samkwang.PNG')
        #pixmap_co = pixmap_co.scaledToHeight(35)
        #self.co_name.setPixmap(pixmap_co)
        self.co_name.setAlignment(Qt.AlignHCenter)
        self.server.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">SERVER</span></p></body></html>"))
        self.camera.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">CAMERA</span></p></body></html>"))
        self.HB.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">환        봉</span></p></body></html>"))
        self.Tool.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">TOOL</span></p></body></html>"))
        self.server_info.setText(_translate("MainWindow", "로봇정보"))
        self.camera_info.setText(_translate("MainWindow", "카메라정보"))
        green = QtGui.QPixmap('img/green.png')
        red = QtGui.QPixmap('img/red.png')
        green1 = green.scaledToWidth(30)
        red1 = red.scaledToWidth(30)
        green2 = green.scaledToWidth(40)
        red2 = red.scaledToWidth(40)
        self.server_rg.setPixmap(green1)
        self.server_rg.setAlignment(Qt.AlignVCenter)
        self.camera_rg.setPixmap(green1)
        self.camera_rg.setAlignment(Qt.AlignVCenter)
        self.matter_val.setPixmap(green2)
        self.tool_life_val.setPixmap(red2)
        self.tooler_error_val.setPixmap(red2)
        self.Def_val.setPixmap(green2)
        self.ng_good.setStyleSheet("background-color: #ff0000")
        tool = QtGui.QPixmap('img/tool.PNG')
        tool = tool.scaledToWidth(340)
        self.tool_img.setPixmap(tool)
        pixmap_m = QtGui.QPixmap('img/0_0.jpg')
        pixmap_m = pixmap_m.scaledToWidth(540)
        self.img.setPixmap(pixmap_m)
        self.start.setStyleSheet("background-color: #dddddd")

    @pyqtSlot(str,int,int,int,str)
    def show_img(self, p,radius,rotate,num,mamo):

        pixmap_m = QtGui.QPixmap(p+'/matter.jpg')
        pixmap_m = pixmap_m.scaledToWidth(540)
        self.img.setPixmap(pixmap_m)
        _translate = QtCore.QCoreApplication.translate
        self.round_val.setText('{}cm  /'.format(int(2*radius*3.14)))
        self.rotate_val.setText('{}°'.format(rotate))
        self.radius_val.setText('{}cm  /'.format(2*radius))
        self.wear.setText('{}'.format(mamo))
        self.cut_num.setText('{}'.format(num))

    def change_HB(self):
        print('HI')
        self.kind_val.setText(self.HB_Val.currentText())