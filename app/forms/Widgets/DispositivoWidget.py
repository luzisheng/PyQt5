from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from classes.inheritables.widget import widget
from resources.resources import *
from classes.objects.workSpace import workSpace
from classes.utils.timer import timer
from forms.Widgets.AIWidget import UIAIVariable
from forms.Widgets.AOWidget import UIAOVariable
from forms.Widgets.DOWidget import UIDOVariable
from forms.Widgets.DIWidget import UIDIVariable

class UIDispositivoWidget(widget):

    def __init__(self,Parent):
        self.__dispostivo = None
        self.__parent = Parent
        self.__dispostivo = None
        super(UIDispositivoWidget,self).__init__(Parent)
        self.setupUi()

    def setupUi(self):
        DispositivoWidget = self
        DispositivoWidget.setObjectName("DispositivoWidget")
        DispositivoWidget.setWindowModality(QtCore.Qt.WindowModal)
        DispositivoWidget.resize(330, 200)
        DispositivoWidget.setMinimumSize(QtCore.QSize(165, 115))
        self.MainFrame = QtWidgets.QFrame(DispositivoWidget)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 330, 200))
        self.MainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainFrame.setObjectName("MainFrame")
        self.Container = QtWidgets.QGroupBox(self.MainFrame)
        self.Container.setGeometry(QtCore.QRect(0, 0, 329, 199))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.Container.setFont(font)
        self.Container.setObjectName("Container")
        self.lblImagen = QtWidgets.QLabel(self.Container)
        self.lblImagen.setGeometry(QtCore.QRect(10, 50, 120, 115))
        self.lblImagen.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblImagen.setLineWidth(0)
        self.lblImagen.setText("")
        self.lblImagen.setPixmap(QtGui.QPixmap(":/source/img/if_16_1751363.png"))
        self.lblImagen.setScaledContents(True)
        self.lblImagen.setObjectName("lblImagen")
        self.StatusFrame = QtWidgets.QFrame(self.Container)
        self.StatusFrame.setGeometry(QtCore.QRect(5, 20, 321, 24))
        self.StatusFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.StatusFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.StatusFrame.setLineWidth(0)
        self.StatusFrame.setObjectName("StatusFrame")
        self.lblStatus = QtWidgets.QLabel(self.StatusFrame)
        self.lblStatus.setGeometry(QtCore.QRect(10, 5, 45, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblStatus.setObjectName("lblStatus")
        self.lblTime = QtWidgets.QLabel(self.StatusFrame)
        self.lblTime.setGeometry(QtCore.QRect(180, 5, 100, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTime.setFont(font)
        self.lblTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTime.setObjectName("lblTime")
        self.Time = QtWidgets.QLabel(self.StatusFrame)
        self.Time.setGeometry(QtCore.QRect(285, 0, 24, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setLineWidth(0)
        self.Time.setText("")
        self.Time.setTextFormat(QtCore.Qt.PlainText)
        self.Time.setScaledContents(True)
        self.Time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Time.setObjectName("Time")
        self.Status = QtWidgets.QLabel(self.StatusFrame)
        self.Status.setGeometry(QtCore.QRect(71, 5, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Status.setFont(font)
        self.Status.setStyleSheet("color:green;")
        self.Status.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Status.setObjectName("Status")
        self.StatusCircle = QtWidgets.QLabel(self.StatusFrame)
        self.StatusCircle.setGeometry(QtCore.QRect(56, 8, 12, 12))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.StatusCircle.setFont(font)
        self.StatusCircle.setStyleSheet("background-color:green;border-radius:5px;")
        self.StatusCircle.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusCircle.setMidLineWidth(1)
        self.StatusCircle.setText("")
        self.StatusCircle.setObjectName("StatusCircle")
        self.lblLast = QtWidgets.QLabel(self.Container)
        self.lblLast.setGeometry(QtCore.QRect(10, 175, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblLast.setFont(font)
        self.lblLast.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblLast.setObjectName("lblLast")
        self.Last = QtWidgets.QLabel(self.Container)
        self.Last.setGeometry(QtCore.QRect(86, 175, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Last.setFont(font)
        self.Last.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Last.setTextFormat(QtCore.Qt.RichText)
        self.Last.setObjectName("Last")
        self.VariablesScroll = QtWidgets.QScrollArea(self.Container)
        self.VariablesScroll.setGeometry(QtCore.QRect(145, 50, 175, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VariablesScroll.sizePolicy().hasHeightForWidth())
        self.VariablesScroll.setSizePolicy(sizePolicy)
        self.VariablesScroll.setMinimumSize(QtCore.QSize(175, 115))
        self.VariablesScroll.setLineWidth(0)
        self.VariablesScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.VariablesScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.VariablesScroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.VariablesScroll.setWidgetResizable(False)
        self.VariablesScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.VariablesScroll.setObjectName("VariablesScroll")
        self.VariablesFrame = QtWidgets.QWidget()
        self.VariablesFrame.setGeometry(QtCore.QRect(0, 0, 175, 115))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VariablesFrame.sizePolicy().hasHeightForWidth())
        self.VariablesFrame.setSizePolicy(sizePolicy)
        self.VariablesFrame.setMinimumSize(QtCore.QSize(175, 115))
        self.VariablesFrame.setSizeIncrement(QtCore.QSize(0, 0))
        self.VariablesFrame.setObjectName("VariablesFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.VariablesFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.VariablesScroll.setWidget(self.VariablesFrame)

        self.retranslateUi(DispositivoWidget)
        QtCore.QMetaObject.connectSlotsByName(DispositivoWidget)

        timer.signals.time_elapsed.connect(self.test)
        self.movie = QMovie(":/source/img/Cargando.gif")
        self.movie.setScaledSize(QtCore.QSize(64,64))

        asd = UIAIVariable()
        self.verticalLayout.addWidget(asd)
        asf = UIAOVariable()
        self.verticalLayout.addWidget(asf)
        asg = UIDIVariable()
        self.verticalLayout.addWidget(asg)
        ash = UIDOVariable()
        self.verticalLayout.addWidget(ash)
        asj = UIDIVariable()
        self.verticalLayout.addWidget(asj)
        ask = UIAIVariable()
        self.verticalLayout.addWidget(ask)
        asq = UIAOVariable()
        self.verticalLayout.addWidget(asq)
        self.VariablesFrame.setGeometry(0,0,175,175)

        #self.movie.start()
        #self.Time.setMovie(self.movie)

    def test(self):
        time = int(self.Time.text())-1
        if time == 0:
            print("update time")
            time = 30
        self.Time.setText(str(time))


    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            #event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            point = self.pos() + event.globalPos() - self.dragPos
            if ((point.x() <= 0 or point.x() >= self.__parent.frameSize().width() - 330 ) or (point.y() <= 0 or point.y() >= self.__parent.frameSize().height() - 200)) :
                event.ignore()
            else:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()

    def retranslateUi(self, DispositivoWidget):
        _translate = QtCore.QCoreApplication.translate
        DispositivoWidget.setWindowTitle(_translate("DispositivoWidget", "Form"))
        self.Container.setTitle(_translate("DispositivoWidget", "Dispositivo 1"))
        self.lblStatus.setText(_translate("DispositivoWidget", "Estado:"))
        self.lblTime.setText(_translate("DispositivoWidget", "Actualizando en"))
        self.Time.setText(_translate("DispostivoWidget","30"))
        self.Status.setText(_translate("DispositivoWidget", "Conectado"))
        self.lblLast.setText(_translate("DispositivoWidget", "Ultima Vez:"))
        self.Last.setText(_translate("DispositivoWidget", "20/05/2020 02:34:32pm"))
