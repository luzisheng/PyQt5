from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from classes import modal, device, Logica, Worker
from forms.Widgets import UIDispositivoModalWidget
from resources import *

class UIImportarDispositivoModal(modal):

    def __init__(self,**kwargs):
        self.workSpaces = dict()
        self.UIContainer = []
        super(UIImportarDispositivoModal,self).__init__(**kwargs)
        self.setupUi()

    def setupUi(self):
        ImportarDispositivo = self
        ImportarDispositivo.setObjectName("ImportarDispositivo")
        ImportarDispositivo.setWindowModality(QtCore.Qt.WindowModal)
        ImportarDispositivo.resize(719, 719)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImportarDispositivo.sizePolicy().hasHeightForWidth())
        ImportarDispositivo.setSizePolicy(sizePolicy)
        ImportarDispositivo.setMinimumSize(QtCore.QSize(480, 620))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        ImportarDispositivo.setFont(font)
        ImportarDispositivo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImportarDispositivo.setWindowIcon(icon)
        ImportarDispositivo.setStyleSheet("background-color: rgb(255, 255, 255);")
        ImportarDispositivo.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.verticalLayout = QtWidgets.QVBoxLayout(ImportarDispositivo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(ImportarDispositivo)
        self.MainFrame.setMinimumSize(QtCore.QSize(360, 0))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(4)
        self.shadow.setOffset(2)
        self.MainFrame.setGraphicsEffect(self.shadow)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleFrame = QtWidgets.QFrame(self.MainFrame)
        self.TitleFrame.setMaximumSize(QtCore.QSize(16777215, 116))
        self.TitleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TitleFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TitleFrame.setObjectName("TitleFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.TitleFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblUDB = QtWidgets.QLabel(self.TitleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUDB.sizePolicy().hasHeightForWidth())
        self.lblUDB.setSizePolicy(sizePolicy)
        self.lblUDB.setMinimumSize(QtCore.QSize(0, 116))
        self.lblUDB.setMaximumSize(QtCore.QSize(16777215, 116))
        self.lblUDB.setStyleSheet("background-color: rgb(65, 105, 225);\n"
"margin:0px;")
        self.lblUDB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblUDB.setText("")
        self.lblUDB.setPixmap(QtGui.QPixmap(":/source/img/logo.png"))
        self.lblUDB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUDB.setObjectName("lblUDB")
        self.gridLayout.addWidget(self.lblUDB, 0, 0, 1, 1)
        self.ExitFrame = QtWidgets.QFrame(self.TitleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitFrame.sizePolicy().hasHeightForWidth())
        self.ExitFrame.setSizePolicy(sizePolicy)
        self.ExitFrame.setMinimumSize(QtCore.QSize(0, 116))
        self.ExitFrame.setMaximumSize(QtCore.QSize(16777215, 116))
        self.ExitFrame.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.ExitFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ExitFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ExitFrame.setLineWidth(0)
        self.ExitFrame.setObjectName("ExitFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ExitFrame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnExit = QtWidgets.QPushButton(self.ExitFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setMaximumSize(QtCore.QSize(32, 32))
        self.btnExit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnExit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source/img/Cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon1)
        self.btnExit.setIconSize(QtCore.QSize(24, 24))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout_4.addWidget(self.btnExit, 0, 1, 1, 1)
        self.lblIIE = QtWidgets.QLabel(self.ExitFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIIE.sizePolicy().hasHeightForWidth())
        self.lblIIE.setSizePolicy(sizePolicy)
        self.lblIIE.setMaximumSize(QtCore.QSize(16777215, 116))
        self.lblIIE.setStyleSheet("background-color: rgb(65, 105, 225);\n"
"margin:0px;")
        self.lblIIE.setText("")
        self.lblIIE.setPixmap(QtGui.QPixmap(":/source/img/iiie.png"))
        self.lblIIE.setScaledContents(False)
        self.lblIIE.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIIE.setObjectName("lblIIE")
        self.gridLayout_4.addWidget(self.lblIIE, 0, 0, 2, 1)
        self.gridLayout.addWidget(self.ExitFrame, 0, 2, 1, 1)
        self.lblSCADA = QtWidgets.QLabel(self.TitleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSCADA.sizePolicy().hasHeightForWidth())
        self.lblSCADA.setSizePolicy(sizePolicy)
        self.lblSCADA.setMinimumSize(QtCore.QSize(250, 116))
        self.lblSCADA.setMaximumSize(QtCore.QSize(16777215, 116))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.lblSCADA.setFont(font)
        self.lblSCADA.setAutoFillBackground(False)
        self.lblSCADA.setStyleSheet("color: rgb(255, 255, 0);background-color: rgb(65, 105, 225);\n"
"margin:0px;")
        self.lblSCADA.setObjectName("lblSCADA")
        self.gridLayout.addWidget(self.lblSCADA, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.TitleFrame)
        self.lblTitle = QtWidgets.QLabel(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("margin-top:5px;")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_2.addWidget(self.lblTitle)
        self.ContentBox = QtWidgets.QGroupBox(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentBox.sizePolicy().hasHeightForWidth())
        self.ContentBox.setSizePolicy(sizePolicy)
        self.ContentBox.setMinimumSize(QtCore.QSize(672, 520))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ContentBox.setFont(font)
        self.ContentBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ContentBox.setObjectName("ContentBox")
        self.ContainerScroll = QtWidgets.QScrollArea(self.ContentBox)
        self.ContainerScroll.setGeometry(QtCore.QRect(5, 45, 660, 471))
        self.ContainerScroll.setMinimumSize(QtCore.QSize(660, 0))
        self.ContainerScroll.setMaximumSize(QtCore.QSize(16777215, 167777))
        self.ContainerScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ContainerScroll.setLineWidth(0)
        self.ContainerScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ContainerScroll.setWidgetResizable(False)
        self.ContainerScroll.setObjectName("ContainerScroll")
        self.ScrollContainer = QtWidgets.QWidget()
        self.ScrollContainer.setGeometry(QtCore.QRect(0, 0, 660, 470))
        self.ScrollContainer.setMinimumSize(QtCore.QSize(0, 470))
        self.ScrollContainer.setObjectName("ScrollContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ScrollContainer)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop)
        self.UtilsFrame = QtWidgets.QFrame(self.ScrollContainer)
        self.UtilsFrame.setMinimumSize(QtCore.QSize(256, 132))
        self.UtilsFrame.setMaximumSize(QtCore.QSize(128, 128))
        self.UtilsFrame.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.UtilsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.UtilsFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.UtilsFrame.setLineWidth(0)
        self.UtilsFrame.setObjectName("UtilsFrame")
        self.utilsLayout = QtWidgets.QVBoxLayout(self.UtilsFrame)
        self.utilsLayout.setContentsMargins(0, 0, 0, 0)
        self.utilsLayout.setSpacing(0)
        self.utilsLayout.setObjectName("utilsLayout")
        self.Status = QtWidgets.QLabel(self.UtilsFrame)
        self.Status.setMaximumSize(QtCore.QSize(64, 64))
        self.Status.setText("")
        self.Status.setPixmap(QtGui.QPixmap(":/source/img/Cargando.gif"))
        self.Status.setScaledContents(True)
        self.Status.setObjectName("Status")
        self.utilsLayout.addWidget(self.Status, 0, QtCore.Qt.AlignHCenter)
        self.lblStatus = QtWidgets.QLabel(self.UtilsFrame)
        self.lblStatus.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.utilsLayout.addWidget(self.lblStatus)
        self.btnReload = QtWidgets.QPushButton(self.UtilsFrame)
        self.btnReload.setMinimumSize(QtCore.QSize(0, 16))
        self.btnReload.setMaximumSize(QtCore.QSize(132, 42))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnReload.setFont(font)
        self.btnReload.setStyleSheet("border: 1px solid rgb(0, 170, 255);padding:5px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/retry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon2)
        self.btnReload.setIconSize(QtCore.QSize(24, 24))
        self.btnReload.setFlat(True)
        self.btnReload.setObjectName("btnReload")
        self.utilsLayout.addWidget(self.btnReload, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.UtilsFrame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ContainerScroll.setWidget(self.ScrollContainer)
        self.txtCount = QtWidgets.QLabel(self.ContentBox)
        self.txtCount.setGeometry(QtCore.QRect(10, 10, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtCount.setFont(font)
        self.txtCount.setObjectName("txtCount")
        self.lblProyecto = QtWidgets.QLabel(self.ContentBox)
        self.lblProyecto.setGeometry(QtCore.QRect(490, 10, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblProyecto.setFont(font)
        self.lblProyecto.setObjectName("lblProyecto")
        self.comboBox = QtWidgets.QComboBox(self.ContentBox)
        self.comboBox.setGeometry(QtCore.QRect(565, 7, 100, 25))
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.ContentBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.MainFrame)

        self.retranslateUi(ImportarDispositivo)
        QtCore.QMetaObject.connectSlotsByName(ImportarDispositivo)

        # listener
        self.parent.signals.resize.connect(self.center)
        self.btnExit.clicked.connect(self.exit)
        self.comboBox.currentIndexChanged.connect(self.mostrarDispositivos)
        self.btnReload.clicked.connect(self.obtenerWorkSpaces)

    def disconnectSignals(self):
        self.parent.signals.resize.disconnect(self.center)
        self.btnExit.clicked.disconnect(self.exit)
        self.comboBox.currentIndexChanged.disconnect(self.mostrarDispositivos)

    def showEvent(self,event):
        self.center()
        self.comboBox.setEnabled(False)
        self.obtenerWorkSpaces()

    def obtenerWorkSpaces(self):
        self.updateState("Cargando...",QMovie(":/source/img/Cargando.gif"))
        self.worker = Worker(Logica.ObtenerWorkspaces,**{"access_token":self.session.access_token})
        self.worker.signals.finished.connect(self.showAction)
        self.worker.start()
        
    def showAction(self,response):
        self.worker.signals.finished.disconnect(self.showAction)
        self.worker.deleteLater()
        del self.worker
        if isinstance(response,Exception):
            self.updateState("??Error! Ha ocurrido un error",QMovie(":/source/img/Error.png"),True)
            return
        self.workSpaces = response
        if len(self.workSpaces) == 0:
            self.updateState("??Vacio! Aqui no hay nada",QMovie(":/source/img/Empty.png"),True)
            return
        self.btnReload.clicked.disconnect(self.obtenerWorkSpaces)
        self.UtilsFrame.hide()
        self.comboBox.setEnabled(True)
        for w in self.workSpaces:
            self.comboBox.addItem(w.nombre,w)
        self.comboBox.setCurrentIndex(0)
        self.mostrarDispositivos(0)

    def mostrarDispositivos(self,index):
        self.ScrollContainer.setGeometry(QtCore.QRect(0, 0, 660, 470))
        for ui in self.UIContainer:
            ui.close()
        self.UIContainer.clear()
        QtWidgets.QApplication.processEvents()
        workSpace = self.comboBox.itemData(index)
        if len(workSpace.devices) == 0:
            self.UtilsFrame.show()
            self.updateState("??Vacio! Aqui no hay nada",QMovie(":/source/img/Empty.png"),True)
            return
        else:
            self.UtilsFrame.hide()
        for d in workSpace.devices:
            UI = UIDispositivoModalWidget(d,True)
            self.verticalLayout_3.addWidget(UI,0,QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
            UI.signals.edit.connect(self.success) # signal indicates is import not edit really
            self.UIContainer.append(UI)
        if len(workSpace.devices)*200 > 399:
           self.ScrollContainer.setGeometry(QtCore.QRect(5,45,660,(len(workSpace.devices)*200)+35))

    def updateState(self,text,Movie = None,Reload = False):
        self.Status.setMovie(Movie)
        self.lblStatus.setText(text)
        Movie.start() if Movie != None else None
        self.btnReload.hide() if Reload is False else self.btnReload.show()
        Movie.setScaledSize(QtCore.QSize(64,64))

    def retranslateUi(self, ImportarDispositivo):
        _translate = QtCore.QCoreApplication.translate
        ImportarDispositivo.setWindowTitle(_translate("ImportarDispositivo", "Sistema SCADA"))
        self.lblSCADA.setText(_translate("ImportarDispositivo", "SCADA"))
        self.lblTitle.setText(_translate("ImportarDispositivo", "Importar Dispositivo"))
        self.lblStatus.setText(_translate("ImportarDispositivo", "Cargando..."))
        self.btnReload.setText(_translate("ImportarDispositivo", "Reintentar"))
        self.txtCount.setText(_translate("ImportarDispositivo", "Total: 0 Dispositivos"))
        self.lblProyecto.setText(_translate("ImportarDispositivo", "Proyecto:"))
