from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from classes import modal, device, Logica, Worker, usuario
from forms.Widgets import UIUsuarioWidget
from .AgregarUsuarioModal import UIAgregarUsuarioModal
from functools import partial
from resources import *

class UIUsuariosModal(modal):

    def __init__(self,MainWindow):
        self.UIContainer = dict()
        super(UIUsuariosModal,self).__init__(MainWindow)
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
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.ContainerScroll.setGeometry(QtCore.QRect(5, 65, 660, 451))
        self.ContainerScroll.setMinimumSize(QtCore.QSize(660, 0))
        self.ContainerScroll.setMaximumSize(QtCore.QSize(16777215, 167777))
        self.ContainerScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ContainerScroll.setLineWidth(0)
        self.ContainerScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ContainerScroll.setWidgetResizable(False)
        self.ContainerScroll.setObjectName("ContainerScroll")
        self.ScrollContainer = QtWidgets.QWidget()
        self.ScrollContainer.setGeometry(QtCore.QRect(0, 0, 660, 450))
        self.ScrollContainer.setMinimumSize(QtCore.QSize(0, 450))
        self.ScrollContainer.setObjectName("ScrollContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ScrollContainer)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 10)
        self.verticalLayout_3.setSpacing(8)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/retry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon2)
        self.btnReload.setIconSize(QtCore.QSize(24, 24))
        self.btnReload.setFlat(True)
        self.btnReload.setObjectName("btnReload")
        self.utilsLayout.addWidget(self.btnReload, 0, QtCore.Qt.AlignHCenter)
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
        self.lblTipo = QtWidgets.QLabel(self.ContentBox)
        self.lblTipo.setGeometry(QtCore.QRect(520, 10, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTipo.setFont(font)
        self.lblTipo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTipo.setObjectName("lblTipo")
        self.cmbTipo = QtWidgets.QComboBox(self.ContentBox)
        self.cmbTipo.setGeometry(QtCore.QRect(565, 7, 100, 25))
        self.cmbTipo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.cmbTipo.setObjectName("cmbTipo")
        self.btnAgregar = QtWidgets.QPushButton(self.ContentBox)
        self.btnAgregar.setGeometry(QtCore.QRect(430, 0, 95, 40))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/source/img/Agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregar.setIcon(icon3)
        self.btnAgregar.setIconSize(QtCore.QSize(24, 24))
        self.btnAgregar.setShortcut("")
        self.btnAgregar.setCheckable(False)
        self.btnAgregar.setFlat(True)
        self.btnAgregar.setObjectName("btnAgregar")
        self.lblNombre = QtWidgets.QLabel(self.ContentBox)
        self.lblNombre.setGeometry(QtCore.QRect(50, 45, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.lblNombre_2 = QtWidgets.QLabel(self.ContentBox)
        self.lblNombre_2.setGeometry(QtCore.QRect(180, 45, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre_2.setFont(font)
        self.lblNombre_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre_2.setObjectName("lblNombre_2")
        self.lblNombre_3 = QtWidgets.QLabel(self.ContentBox)
        self.lblNombre_3.setGeometry(QtCore.QRect(320, 45, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre_3.setFont(font)
        self.lblNombre_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre_3.setObjectName("lblNombre_3")
        self.lblNombre_4 = QtWidgets.QLabel(self.ContentBox)
        self.lblNombre_4.setGeometry(QtCore.QRect(440, 45, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre_4.setFont(font)
        self.lblNombre_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre_4.setObjectName("lblNombre_4")
        self.lblNombre_5 = QtWidgets.QLabel(self.ContentBox)
        self.lblNombre_5.setGeometry(QtCore.QRect(550, 45, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre_5.setFont(font)
        self.lblNombre_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre_5.setObjectName("lblNombre_5")
        self.verticalLayout_2.addWidget(self.ContentBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.MainFrame)
        self.verticalLayout_3.setAlignment(Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.UtilsFrame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(ImportarDispositivo)
        QtCore.QMetaObject.connectSlotsByName(ImportarDispositivo)

        self.cmbTipo.addItem("Administrador")
        self.cmbTipo.addItem("Usuario")
        self.cmbTipo.addItem("Todos")
        self.cmbTipo.setCurrentIndex(self.cmbTipo.findText("Todos"))

        #listener
        self.parent.signals.resize.connect(self.center)
        self.btnExit.clicked.connect(self.exit)
        self.btnReload.clicked.connect(self.obtenerUsuarios)
        self.cmbTipo.currentIndexChanged.connect(self.mostrarUsuarios)
        self.btnAgregar.clicked.connect(self.agregarUsuario)

    def showEvent(self,evt):
        self.center()
        self.obtenerUsuarios()

    def obtenerUsuarios(self):
        self.UtilsFrame.show()
        self.updateState("Cargando...",QMovie(":/source/img/Cargando.gif"))
        worker = Worker(Logica.ObtenerUsuarios,**{"access_token":self.session.access_token})
        worker.signals.finished.connect(self.obtenerUsuariosAction)
        self.threadpool.start(worker)

    def obtenerUsuariosAction(self,response):
        if isinstance(response,Exception): # if data returned is a Exception
            self.updateState("¡Error! Ha ocurrido un error",QMovie(":/source/img/Error.png"),True)
            return
        if len(response) == 0:
            self.updateState("¡Vacio! Fallo al obtener los usuarios",QMovie(":/source/img/Empty.png"),True)
            return
        self.UtilsFrame.hide()
        self.usuarios = response
        self.txtCount.setText("Total: %s Usuarios" % len(self.usuarios))
        self.mostrarUsuarios(2)

    def mostrarUsuarios(self,index):
        self.ScrollContainer.setGeometry(QtCore.QRect(5, 65, 660, 451))
        self.cleanUI()
        filter = self.cmbTipo.currentText()
        if not filter == "Todos":
           filterUsr = list(self.filter(filter))
        else:
           filterUsr = self.usuarios
        if len(filterUsr) == 0:
           self.UtilsFrame.show()
           self.updateState("¡Vacio! No hay usuario de este tipo",QMovie(":/source/img/Empty.png"),True)
           return
        else:
           self.UtilsFrame.hide()
        for usr in filterUsr:
           UIUsuario = UIUsuarioWidget(usr)
           UIUsuario.signals.enable.connect(self.habilitarUsuario)
           UIUsuario.signals.disable.connect(self.deshabilitarUsuario)
           UIUsuario.signals.edit.connect(self.editarUsuario)
           UIUsuario.signals.delete.connect(self.eliminarUsuario)
           self.verticalLayout_3.addWidget(UIUsuario,0,Qt.AlignTop | Qt.AlignHCenter)
           self.UIContainer[usr.id] = UIUsuario

    def agregarUsuario(self):
        UIAgregar = UIAgregarUsuarioModal(self.parent)
        UIAgregar.signals.success.connect(self.agregarUsuarioAction)
        UIAgregar.show()

    def agregarUsuarioAction(self,usr:usuario):
        self.usuarios.append(usr)
        self.mostrarUsuarios(2)

    def editarUsuario(self,usr:usuario):
        UIEditar = UIAgregarUsuarioModal(self.parent,True,user=usr)
        UIEditar.signals.success.connect(self.editarUsuarioAction)
        UIEditar.show()

    def editarUsuarioAction(self,usr:usuario):
        self.UIContainer[usr.id].updateUI(usr)
        for i,user in enumerate(self.usuarios):
            if user.id == usr.id:
                self.usuarios[i] = usr

    def eliminarUsuario(self,user:usuario):
        self.ContentBox.setEnabled(False)
        worker = Worker(Logica.eliminarUsuario,**{"access_token":self.session.access_token,"id":user.id})
        worker.signals.finished.connect(partial(self.eliminarUsuarioAction,usr=user))
        self.threadpool.start(worker)

    def eliminarUsuarioAction(self,response,usr):
        self.ContentBox.setEnabled(True)
        if isinstance(response,Exception):
            QMessageBox.warning(self,"¡Error!","¡Error! Fallo al contactar con el servicio SCADA")
            return
        if response["Success"] == 'false':
            QMessageBox.warning(self,'¡Error!',response["Message"])
            return
        self.usuarios.remove(usr)
        self.UIContainer[usr.id].close()
        del self.UIContainer[usr.id]

    def habilitarUsuario(self,usr:usuario):
        self.ContentBox.setEnabled(False)
        worker = Worker(Logica.habilitarUsuario,**{"access_token":self.session.access_token,"id":usr.id})
        worker.signals.finished.connect(partial(self.habilitarUsuarioAction,usr=usr))
        self.threadpool.start(worker)

    def deshabilitarUsuario(self,usr:usuario):
        self.ContentBox.setEnabled(False)
        worker = Worker(Logica.deshabilitarUsuario,**{"access_token":self.session.access_token,"id":usr.id})
        worker.signals.finished.connect(partial(self.habilitarUsuarioAction,usr=usr))
        self.threadpool.start(worker)

    def habilitarUsuarioAction(self,response,usr:usuario):
        self.ContentBox.setEnabled(True)
        if isinstance(response,Exception):
            QMessageBox.warning(self,"¡Error!","¡Error! Fallo al contactar con el servicio SCADA")
            return
        if response["Success"] == 'false':
            QMessageBox.warning(self,'¡Error!',response["Message"])
            return
        usr.enabled = not usr.enabled
        self.UIContainer[usr.id].updateUI(usr)

    def cleanUI(self):
        for UI in self.UIContainer.items():
            UI[1].signals.enable.disconnect(self.habilitarUsuario)
            UI[1].signals.disable.disconnect(self.deshabilitarUsuario)
            UI[1].close()
        self.UIContainer.clear()

    def filter(self,filter):
        for u in self.usuarios:
           if u.tipo == filter:
                yield(u)

    def disconnectSignals(self):
        self.parent.signals.resize.disconnect(self.center)
        self.btnExit.clicked.disconnect(self.exit)
        self.cmbTipo.currentIndexChanged.disconnect(self.mostrarUsuarios)
        self.cleanUI()

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
        self.lblTitle.setText(_translate("ImportarDispositivo", "Usuarios"))
        self.lblStatus.setText(_translate("ImportarDispositivo", "Cargando..."))
        self.btnReload.setText(_translate("ImportarDispositivo", "Reintentar"))
        self.txtCount.setText(_translate("ImportarDispositivo", "Total: 0 Usuarios"))
        self.lblTipo.setText(_translate("ImportarDispositivo", "Tipo"))
        self.btnAgregar.setText(_translate("ImportarDispositivo", "Agregar"))
        self.lblNombre.setText(_translate("ImportarDispositivo", "Nombres:"))
        self.lblNombre_2.setText(_translate("ImportarDispositivo", "Usuario:"))
        self.lblNombre_3.setText(_translate("ImportarDispositivo", "Email:"))
        self.lblNombre_4.setText(_translate("ImportarDispositivo", "Tipo:"))
        self.lblNombre_5.setText(_translate("ImportarDispositivo", "Acciones"))