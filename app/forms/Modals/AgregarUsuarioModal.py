from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from classes import modal, Logica, Worker, usuario
from functools import partial
from resources import *

class UIAgregarUsuarioModal(modal):

    def __init__(self,**kwargs):
        super(UIAgregarUsuarioModal,self).__init__(**kwargs)
        self.isEdit = kwargs["IsEdit"]
        if kwargs["Usuario"] is None:
            self.usuario = usuario()
        else:
            self.usuario = kwargs["Usuario"]

    def setupUI(self):
        AgregarUsuarioModal = self
        AgregarUsuarioModal.setObjectName("AgregarUsuarioModal")
        AgregarUsuarioModal.setWindowModality(QtCore.Qt.WindowModal)
        AgregarUsuarioModal.resize(370, 486)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AgregarUsuarioModal.sizePolicy().hasHeightForWidth())
        AgregarUsuarioModal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        AgregarUsuarioModal.setFont(font)
        AgregarUsuarioModal.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../.designer/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AgregarUsuarioModal.setWindowIcon(icon)
        AgregarUsuarioModal.setStyleSheet("background-color: rgb(255, 255, 255);")
        AgregarUsuarioModal.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.verticalLayout = QtWidgets.QVBoxLayout(AgregarUsuarioModal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(AgregarUsuarioModal)
        self.MainFrame.setMinimumSize(QtCore.QSize(0, 0))
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
        self.lblSCADA = QtWidgets.QLabel(self.TitleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSCADA.sizePolicy().hasHeightForWidth())
        self.lblSCADA.setSizePolicy(sizePolicy)
        self.lblSCADA.setMinimumSize(QtCore.QSize(150, 116))
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
        self.gridLayout.addWidget(self.ExitFrame, 0, 2, 1, 1)
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
        self.verticalLayout_2.addWidget(self.TitleFrame)
        self.lblTitle = QtWidgets.QLabel(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 38))
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentBox.sizePolicy().hasHeightForWidth())
        self.ContentBox.setSizePolicy(sizePolicy)
        self.ContentBox.setMinimumSize(QtCore.QSize(300, 0))
        self.ContentBox.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ContentBox.setFont(font)
        self.ContentBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ContentBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ContentBox.setFlat(True)
        self.ContentBox.setObjectName("ContentBox")
        self.ContentLayout = QtWidgets.QVBoxLayout(self.ContentBox)
        self.ContentLayout.setContentsMargins(0, 0, 0, 0)
        self.ContentLayout.setSpacing(0)
        self.ContentLayout.setObjectName("ContentLayout")
        self.ContentFrame = QtWidgets.QFrame(self.ContentBox)
        self.ContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContentFrame.setObjectName("ContentFrame")
        self.txtNombre = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtNombre.setGeometry(QtCore.QRect(120, 35, 101, 21))
        self.txtNombre.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtNombre.setObjectName("txtNombre")
        self.lblNombre = QtWidgets.QLabel(self.ContentFrame)
        self.lblNombre.setGeometry(QtCore.QRect(40, 40, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.lblTipo = QtWidgets.QLabel(self.ContentFrame)
        self.lblTipo.setGeometry(QtCore.QRect(40, 160, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTipo.setFont(font)
        self.lblTipo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTipo.setObjectName("lblTipo")
        self.btnAceptar_2 = QtWidgets.QPushButton(self.ContentFrame)
        self.btnAceptar_2.setGeometry(QtCore.QRect(111, 200, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar_2.setFont(font)
        self.btnAceptar_2.setStyleSheet("border:1px solid green;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAceptar_2.setIcon(icon2)
        self.btnAceptar_2.setIconSize(QtCore.QSize(24, 24))
        self.btnAceptar_2.setShortcut("")
        self.btnAceptar_2.setCheckable(False)
        self.btnAceptar_2.setFlat(True)
        self.btnAceptar_2.setObjectName("btnAceptar_2")
        self.lblEmail = QtWidgets.QLabel(self.ContentFrame)
        self.lblEmail.setGeometry(QtCore.QRect(40, 120, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblEmail.setFont(font)
        self.lblEmail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblEmail.setObjectName("lblEmail")
        self.cmbTipo = QtWidgets.QComboBox(self.ContentFrame)
        self.cmbTipo.setGeometry(QtCore.QRect(120, 155, 101, 25))
        self.cmbTipo.setObjectName("cmbTipo")
        self.lblUsuario = QtWidgets.QLabel(self.ContentFrame)
        self.lblUsuario.setGeometry(QtCore.QRect(40, 80, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblUsuario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUsuario.setObjectName("lblUsuario")
        self.txtUsuario = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtUsuario.setGeometry(QtCore.QRect(120, 75, 101, 21))
        self.txtUsuario.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtEmail = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtEmail.setGeometry(QtCore.QRect(120, 115, 101, 21))
        self.txtEmail.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtEmail.setObjectName("txtEmail")
        self.Status = QtWidgets.QLabel(self.ContentFrame)
        self.Status.setGeometry(QtCore.QRect(121, 200, 51, 51))
        self.Status.setMaximumSize(QtCore.QSize(64, 64))
        self.Status.setText("")
        self.Status.setPixmap(QtGui.QPixmap(":/source/img/Cargando.gif"))
        self.Status.setScaledContents(True)
        self.Status.setObjectName("Status")
        self.ContentLayout.addWidget(self.ContentFrame)
        self.verticalLayout_2.addWidget(self.ContentBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.MainFrame)

        self.retranslateUi(AgregarUsuarioModal)
        QtCore.QMetaObject.connectSlotsByName(AgregarUsuarioModal)
        self.center()

        self.shortcut = QtWidgets.QShortcut(Qt.Key_Return,self)
        self.shortcut.activated.connect(self.validarUsuario)
         # movie

        self.movie = QMovie(":/source/img/Cargando.gif") # 80 ,200
        self.movie.setScaledSize(QtCore.QSize(48,48))
        self.Status.setMovie(self.movie)
        self.Status.hide()
        
        #listener
        self.parent.signals.resize.connect(self.center)
        self.btnExit.clicked.connect(self.exit)
        self.btnAceptar_2.clicked.connect(self.validarUsuario)

    def showEvent(self,evt):
        self.cmbTipo.addItem("Usuario")
        self.cmbTipo.addItem("Administrador")
        if self.isEdit and not self.session.usuario == "administrador.scada":
            self.cmbTipo.setEnabled(False)
        if not self.isEdit and not self.session.usuario == "administrador.scada":
            self.cmbTipo.removeItem("Administrador")
        if self.isEdit:
            self.lblTitle.setText("Editar usuario")
            self.txtNombre.setText(self.usuario.nombres)
            self.txtUsuario.setText(self.usuario.usuario)
            self.txtEmail.setText(self.usuario.email)
            self.cmbTipo.setCurrentIndex(self.cmbTipo.findText(self.usuario.tipo))
     
    def disconnectSignals(self):
        self.parent.signals.resize.disconnect(self.center)
        self.btnExit.clicked.disconnect(self.exit)
        self.btnAceptar_2.clicked.disconnect(self.validarUsuario)

    def validarUsuario(self):
        try:
            self.usuario.nombres = self.txtNombre.text()
            self.usuario.usuario = self.txtUsuario.text()
            self.usuario.email = self.txtEmail.text()
            if self.session.usuario == "administrador.scada":
                self.usuario.tipo = self.cmbTipo.currentText()
        except ValueError as vError:
            QMessageBox.warning(self,"??Error!",str(vError))
            return
        reply = self.prompt("Confirmacion","??Son estos datos correctos?")
        if reply == QMessageBox.Yes:
            self.btnAceptar_2.hide()
            self.Status.show()
            self.movie.start()
            if not self.isEdit:
                self.worker = Worker(Logica.agregarUsuario,**{"access_token":self.session.access_token,"data":self.usuario.toJSON()})
            else:
                self.worker = Worker(Logica.editarUsuario,**{"access_token":self.session.access_token,"data":self.usuario.toJSON()})
            self.worker.signals.finished.connect(partial(self.validarUsuarioAction,user=self.usuario))
            self.worker.start()
    
    def validarUsuarioAction(self,response,user):
        self.worker.signals.finished.disconnect()
        self.worker.deleteLater()
        del self.worker
        self.btnAceptar_2.show()
        self.Status.hide()
        self.movie.stop()
        if isinstance(response,Exception):
            QMessageBox.warning(self,"??Error!",str(response))
            return
        if response["Success"] == 'false':
            QMessageBox.warning(self,'??Error!',response["Message"])
            return
        self.success(user)

    def retranslateUi(self, AgregarUsuarioModal):
        _translate = QtCore.QCoreApplication.translate
        AgregarUsuarioModal.setWindowTitle(_translate("AgregarUsuarioModal", "Sistema SCADA"))
        self.lblSCADA.setText(_translate("AgregarUsuarioModal", "SCADA"))
        self.lblTitle.setText(_translate("AgregarUsuarioModal", "Agregar Usuario"))
        self.ContentBox.setTitle(_translate("AgregarUsuarioModal", "Informaci??n"))
        self.lblNombre.setText(_translate("AgregarUsuarioModal", "Nombre:"))
        self.lblTipo.setText(_translate("AgregarUsuarioModal", "Tipo:"))
        self.btnAceptar_2.setText(_translate("AgregarUsuarioModal", "OK"))
        self.lblEmail.setText(_translate("AgregarUsuarioModal", "Email:"))
        self.lblUsuario.setText(_translate("AgregarUsuarioModal", "Usuario:"))
