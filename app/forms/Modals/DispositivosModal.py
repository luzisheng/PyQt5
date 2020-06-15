from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from classes import modal, device
from forms.Widgets import UIDispositivoModalWidget
from forms.Modals.AgregarDispositivoModal import UIAgregarDispositvoModal
from resources import *

class UIDispositvoModal(modal):

    def __init__(self,MainWindow,session:object,dict:dict):
        self.workSpaces = dict
        self.UIContainer = []
        super(UIDispositvoModal,self).__init__(MainWindow,session)
        self.__parent = MainWindow
        self.__session = session
        self.setupUi()

    def setupUi(self):
        DispositvoModal = self
        DispositvoModal.setObjectName("DispositvoModal")
        DispositvoModal.setWindowModality(QtCore.Qt.WindowModal)
        DispositvoModal.resize(720, 739)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DispositvoModal.sizePolicy().hasHeightForWidth())
        DispositvoModal.setSizePolicy(sizePolicy)
        DispositvoModal.setMinimumSize(QtCore.QSize(480, 720))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        DispositvoModal.setFont(font)
        DispositvoModal.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DispositvoModal.setWindowIcon(icon)
        DispositvoModal.setStyleSheet("background-color: rgb(255, 255, 255);")
        DispositvoModal.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.verticalLayout = QtWidgets.QVBoxLayout(DispositvoModal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(DispositvoModal)
        self.MainFrame.setMinimumSize(QtCore.QSize(360, 0))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleFrame = QtWidgets.QFrame(self.MainFrame)
        self.TitleFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.ContentBox.setMinimumSize(QtCore.QSize(672, 535))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ContentBox.setFont(font)
        self.ContentBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ContentBox.setObjectName("ContentBox")
        self.btnAgregar = QtWidgets.QPushButton(self.ContentBox)
        self.btnAgregar.setGeometry(QtCore.QRect(390, 0, 95, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAgregar.sizePolicy().hasHeightForWidth())
        self.btnAgregar.setSizePolicy(sizePolicy)
        self.btnAgregar.setMinimumSize(QtCore.QSize(92, 38))
        self.btnAgregar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setStyleSheet("border:1px solid green;top:0px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/Agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregar.setIcon(icon2)
        self.btnAgregar.setIconSize(QtCore.QSize(24, 24))
        self.btnAgregar.setShortcut("")
        self.btnAgregar.setCheckable(False)
        self.btnAgregar.setFlat(True)
        self.btnAgregar.setObjectName("btnAgregar")
        self.btnExportar = QtWidgets.QPushButton(self.ContentBox)
        self.btnExportar.setGeometry(QtCore.QRect(185, 0, 95, 40))
        self.btnExportar.setMinimumSize(QtCore.QSize(92, 38))
        self.btnExportar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnExportar.setFont(font)
        self.btnExportar.setStyleSheet("border:1px solid green;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/source/img/Exportar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportar.setIcon(icon3)
        self.btnExportar.setIconSize(QtCore.QSize(24, 24))
        self.btnExportar.setShortcut("")
        self.btnExportar.setCheckable(False)
        self.btnExportar.setFlat(True)
        self.btnExportar.setObjectName("btnExportar")
        self.btnImportar = QtWidgets.QPushButton(self.ContentBox)
        self.btnImportar.setGeometry(QtCore.QRect(290, 0, 95, 40))
        self.btnImportar.setMinimumSize(QtCore.QSize(92, 38))
        self.btnImportar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnImportar.setFont(font)
        self.btnImportar.setStyleSheet("border:1px solid green;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/source/img/Importar-SM.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImportar.setIcon(icon4)
        self.btnImportar.setIconSize(QtCore.QSize(24, 24))
        self.btnImportar.setShortcut("")
        self.btnImportar.setCheckable(False)
        self.btnImportar.setFlat(True)
        self.btnImportar.setObjectName("btnImportar")
        self.ContainerScroll = QtWidgets.QScrollArea(self.ContentBox)
        self.ContainerScroll.setGeometry(QtCore.QRect(5, 45, 660, 470))
        self.ContainerScroll.setMinimumSize(QtCore.QSize(660, 470))
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
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/source/img/retry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon5)
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

        self.retranslateUi(DispositvoModal)
        QtCore.QMetaObject.connectSlotsByName(DispositvoModal)
        self.btnReload.hide()
        self.btnAgregar.setEnabled(False)
        self.btnImportar.setEnabled(False)
        self.btnExportar.setEnabled(False)
        
        #listener
        self.__parent.signals.resize.connect(lambda : self.center(self.__parent))
        self.btnExit.clicked.connect(self.exit)
        self.btnAgregar.clicked.connect(self.agregarDispositivo)
        self.btnImportar.clicked.connect(self.importarDispositivos)
        self.btnExportar.clicked.connect(self.exportarDispositivos)

    def disconnectSignals(self):
        self.__parent.signals.resize.disconnect()
        self.btnExit.clicked.disconnect(self.exit)

    def showEvent(self,event):
        self.center(self.__parent)
        self.movie = QMovie(":/source/img/Cargando.gif")
        self.movie.setScaledSize(QtCore.QSize(64,64))
        self.movie.start()
        self.Status.setMovie(self.movie)
        
        if len(self.workSpaces) == 0:
            self.movie = QMovie(":/source/img/Empty.png")
            self.movie.start()
            self.Status.setMovie(self.movie)
            self.lblStatus.setText("¡Vacio! Aqui no hay nada")
            return
        if self.workSpaces is None:
            self.movie = QMovie(":/source/img/Error.png")
            self.movie.start()
            self.Status.setMovie(self.movie)
            self.lblStatus.setText("¡Error! Ha ocurrido un error")
            return
        self.UtilsFrame.deleteLater()
        self.btnAgregar.setEnabled(True)
        self.btnExportar.setEnabled(True)
        self.btnImportar.setEnabled(True)
        for w in self.workSpaces.items():
            self.comboBox.addItem(w[1].workSpace.nombre,w[1])
        self.comboBox.setCurrentIndex(0)
        self.comboBox.currentIndexChanged.connect(self.mostrarDispositivos)
        self.mostrarDispositivos(0)

    def editarDispositivio(self,dev:device):
        print(dev.__dict__)

    def eliminarDispositivo(self,dev:device):
        print(dev.__dict__)

    def copiarDispositivo(self,dev:device):
        print(dev.__dict__)
    
    def agregarDispositivo(self):
        UIAgregar = UIAgregarDispositvoModal(self,self.__session)
        UIAgregar.show()

    def importarDispositivos(self):
        pass

    def exportarDispositivos(self):
        pass
    
    def mostrarDispositivos(self,index):
        for ui in self.UIContainer:
            ui.disconnectSignals()
            ui.close()
            ui.deleteLater()
        self.UIContainer.clear()
        QtWidgets.QApplication.processEvents()
        container = self.comboBox.itemData(index)
        for d in container.workSpace.devices:
            UI = UIDispositivoModalWidget(d)
            self.verticalLayout_3.addWidget(UI,0,QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
            UI.deviceSignals.edit.connect(self.editarDispositivio)
            UI.deviceSignals.delete.connect(self.eliminarDispositivo)
            UI.deviceSignals.copy.connect(self.copiarDispositivo)
            self.UIContainer.append(UI)
        if len(container.workSpace.devices)*200 > 399:
           self.ScrollContainer.setGeometry(QtCore.QRect(5,45,660,(len(container.workSpace.devices)*200)+35))

    def retranslateUi(self, DispositvoModal):
        _translate = QtCore.QCoreApplication.translate
        DispositvoModal.setWindowTitle(_translate("DispositvoModal", "Sistema SCADA"))
        self.lblSCADA.setText(_translate("DispositvoModal", "SCADA"))
        self.lblTitle.setText(_translate("DispositvoModal", "Gestión de Dispositivos"))
        self.btnAgregar.setText(_translate("DispositvoModal", "Agregar"))
        self.btnExportar.setText(_translate("DispositvoModal", "Exportar"))
        self.btnImportar.setText(_translate("DispositvoModal", "Importar"))
        self.lblStatus.setText(_translate("DispositvoModal", "Cargando..."))
        self.btnReload.setText(_translate("DispositvoModal", "Reintentar"))
        self.txtCount.setText(_translate("DispositvoModal", "Total: 0 Dispositivos"))
        self.lblProyecto.setText(_translate("DispositvoModal", "Proyecto:"))
