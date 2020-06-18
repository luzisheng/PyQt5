from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap, QColor, QIcon
from classes import modal,Logica, Worker, variable
from resources import *

class UIAgregarVariableModal(modal):

    def __init__(self,Parent,var:variable = None,IsEdit = False,**kwargs):
        super(UIAgregarVariableModal,self).__init__(Parent)
        self.ID = kwargs["ID"]
        self.Token = kwargs["Token"]
        if not var is None:
            self.variable = var
        else:
            self.variable = variable()
        self.IsEdit = IsEdit
        self.setupUi()

    def setupUi(self):
        AgregarVariableModal = self
        AgregarVariableModal.setObjectName("AgregarVariableModal")
        AgregarVariableModal.setWindowModality(QtCore.Qt.WindowModal)
        AgregarVariableModal.resize(420, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AgregarVariableModal.sizePolicy().hasHeightForWidth())
        AgregarVariableModal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        AgregarVariableModal.setFont(font)
        AgregarVariableModal.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AgregarVariableModal.setWindowIcon(icon)
        AgregarVariableModal.setStyleSheet("background-color: rgb(255, 255, 255);")
        AgregarVariableModal.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.verticalLayout = QtWidgets.QVBoxLayout(AgregarVariableModal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(AgregarVariableModal)
        self.MainFrame.setMinimumSize(QtCore.QSize(0, 0))
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
        self.ContentBox = QtWidgets.QGroupBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentBox.sizePolicy().hasHeightForWidth())
        self.ContentBox.setSizePolicy(sizePolicy)
        self.ContentBox.setMinimumSize(QtCore.QSize(350, 0))
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
        self.ContentFrame = QtWidgets.QFrame()
        self.ContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContentFrame.setObjectName("ContentFrame")
        self.txtNombre = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtNombre.setGeometry(QtCore.QRect(140, 15, 101, 21))
        self.txtNombre.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtNombre.setObjectName("txtNombre")
        self.label_8 = QtWidgets.QLabel(self.ContentFrame)
        self.label_8.setGeometry(QtCore.QRect(60, 265, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lblNombre = QtWidgets.QLabel(self.ContentFrame)
        self.lblNombre.setGeometry(QtCore.QRect(60, 20, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.boxNotificar = QtWidgets.QCheckBox(self.ContentFrame)
        self.boxNotificar.setGeometry(QtCore.QRect(140, 225, 51, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.boxNotificar.setFont(font)
        self.boxNotificar.setObjectName("boxNotificar")
        self.cmbNotificar = QtWidgets.QComboBox(self.ContentFrame)
        self.cmbNotificar.setGeometry(QtCore.QRect(190, 225, 41, 25))
        self.cmbNotificar.setObjectName("cmbNotificar")
        self.label_9 = QtWidgets.QLabel(self.ContentFrame)
        self.label_9.setGeometry(QtCore.QRect(60, 193, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.cmbVariable = QtWidgets.QComboBox(self.ContentFrame)
        self.cmbVariable.setGeometry(QtCore.QRect(140, 122, 101, 25))
        self.cmbVariable.setObjectName("cmbVariable")
        self.label_10 = QtWidgets.QLabel(self.ContentFrame)
        self.label_10.setGeometry(QtCore.QRect(60, 227, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.ContentFrame)
        self.label_11.setGeometry(QtCore.QRect(60, 160, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.ContentFrame)
        self.label_12.setGeometry(QtCore.QRect(60, 125, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.txtExpresion = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtExpresion.setGeometry(QtCore.QRect(140, 187, 101, 21))
        self.txtExpresion.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtExpresion.setObjectName("txtExpresion")
        self.cmbNivel = QtWidgets.QComboBox(self.ContentFrame)
        self.cmbNivel.setGeometry(QtCore.QRect(140, 261, 112, 25))
        self.cmbNivel.setObjectName("cmbNivel")
        self.btnAceptar_2 = QtWidgets.QPushButton(self.ContentFrame)
        self.btnAceptar_2.setGeometry(QtCore.QRect(130, 300, 71, 41))
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
        self.label_13 = QtWidgets.QLabel(self.ContentFrame)
        self.label_13.setGeometry(QtCore.QRect(60, 90, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.txtNotificar = QtWidgets.QSpinBox(self.ContentFrame)
        self.txtNotificar.setGeometry(QtCore.QRect(240, 225, 60, 26))
        self.txtNotificar.setObjectName("txtNotificar")
        self.txtNotificar.setMaximum(999999)
        self.txtNotificar.setMinimum(0)
        self.cmbSenal = QtWidgets.QComboBox(self.ContentFrame)
        self.cmbSenal.setGeometry(QtCore.QRect(140, 51, 101, 25))
        self.cmbSenal.setObjectName("cmbSenal")
        self.cmbTipo = QtWidgets.QComboBox(self.ContentFrame)
        self.cmbTipo.setGeometry(QtCore.QRect(140, 88, 101, 25))
        self.cmbTipo.setObjectName("cmbTipo")
        self.label_14 = QtWidgets.QLabel(self.ContentFrame)
        self.label_14.setGeometry(QtCore.QRect(60, 55, 75, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.cmbColor = QtWidgets.QComboBox(self.ContentFrame)
        self.cmbColor.setGeometry(QtCore.QRect(140, 156, 101, 25))
        self.cmbColor.setObjectName("cmbColor")
        self.UtilsFrame = QtWidgets.QFrame()
        self.UtilsFrame.setGeometry(QtCore.QRect(50, 100, 256, 132))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/source/img/retry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon3)
        self.btnReload.setIconSize(QtCore.QSize(24, 24))
        self.btnReload.setFlat(True)
        self.btnReload.setObjectName("btnReload")
        self.utilsLayout.addWidget(self.btnReload, 0, QtCore.Qt.AlignHCenter)
        self.ContentLayout.addWidget(self.UtilsFrame,0,QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.ContentBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.MainFrame)

        self.cmbSenal.addItem("Analogica")
        self.cmbSenal.addItem("Digital")

        self.cmbTipo.addItem("Lectura")
        self.cmbTipo.addItem("Escritura")

        self.cmbNotificar.addItem("<")
        self.cmbNotificar.addItem(">")
        self.cmbNotificar.addItem("!=")
        self.cmbNotificar.addItem("==")
        
        self.addColorItems()
        self.addNotifyItems()

        self.retranslateUi(AgregarVariableModal)
        QtCore.QMetaObject.connectSlotsByName(AgregarVariableModal)
        self.parent.signals.resize.connect(self.center)
        self.btnExit.clicked.connect(self.exit)
        self.btnReload.clicked.connect(self.obtenerVariablesFunciones)
        self.btnReload.hide()
        self.cmbNotificar.setEnabled(False)
        self.txtNotificar.setEnabled(False)
        self.cmbNivel.setEnabled(False)
        self.cmbTipo.currentIndexChanged.connect(self.updateVariablesFunciones)
        self.cmbSenal.currentIndexChanged.connect(self.cmbSenal_CurrentIndexChange)
        self.boxNotificar.stateChanged.connect(self.boxNotificar_StateChange)
        self.btnAceptar_2.clicked.connect(self.btnAceptar_Click)

    def disconnectSignals(self):
        self.parent.signals.resize.disconnect(self.center)
        self.btnExit.clicked.disconnect(self.exit)
        self.cmbTipo.currentIndexChanged.disconnect(self.updateVariablesFunciones)
        self.cmbSenal.currentIndexChanged.disconnect(self.cmbSenal_CurrentIndexChange)
        self.boxNotificar.stateChanged.disconnect(self.boxNotificar_StateChange)
        self.btnAceptar_2.clicked.disconnect(self.btnAceptar_Click)

    def btnAceptar_Click(self):
        var = self.variable
        try:
            var.nombre = self.txtNombre.text()
            var.expresion = self.txtExpresion.text()
            var.pin = (self.cmbVariable.itemData(self.cmbVariable.currentIndex()))["PIN"]
            var.analogic = True if self.cmbSenal.currentText() == "Analogica" else False
            var.output = True if self.cmbTipo.currentText() == "Escritura" else False
            var.displayColor = None if not self.cmbColor.isEnabled() else self.cmbColor.currentText()
            var.notify = None if not self.boxNotificar.isChecked() else self.cmbNotificar.currentText().rjust(2,"-") + self.txtNotificar.value().__str__()
            var.nivel = None if not self.boxNotificar.isChecked() else self.cmbNivel.itemData(self.cmbNivel.currentIndex())["color"]
        except ValueError as vError:
            QtWidgets.QMessageBox.warning(self,"¡Error!",vError.__str__())
            return
        response = self.prompt("Confirmacion","¿Son estos datos correctos?")
        if response == QtWidgets.QMessageBox.Yes:
            self.success(var)
        
    def showEvent(self,ev):
        self.center()
        self.obtenerVariablesFunciones()
        
    def obtenerVariablesFunciones(self):
        self.btnReload.hide()
        self.lblStatus.setText("Cargando...")
        self.movie = QMovie(":/source/img/Cargando.gif")
        self.movie.start()
        self.Status.setMovie(self.movie)
        worker = Worker(Logica.ObtenerVariablesFunciones,**{"ID":self.ID,"Token":self.Token,"access_token":self.session.access_token})
        worker.signals.result.connect(self.obtenerVariablesFuncionesCallback)
        worker.signals.error.connect(self.obtenerVariablesFuncionesCallback)
        self.threadpool.start(worker)

    def addColorItems(self):
        colors = {"aqua","aquamarine","beige","black","blue","blueviolet","brown","burlywood","chartreuse",
            "cadetblue","chocolate","crimson","cyan","darkblue","fuchsia","gold","gray",
            "green","greenyellow","hotpink","indigo","lime","magenta","navy","olive",
            "orange","orangered","orchid","palegreen","purple","red","salmon","silver",
            "skyblue","slateblue","springgreen","tomato","turquoise","violet","wheat","yellow","yellowgreen"}

        for color in colors:
            pixmap = QPixmap(25,25)
            pixmap.fill(QColor(color))
            Icon = QIcon(pixmap)
            self.cmbColor.addItem(Icon,color)

    def addNotifyItems(self):
        colors = [{"color":"aqua","text":"Informativa"},
                {"color":"orange","text":"Advertencia"},
                {"color":"green","text":"Normal"},
                {"color":"red","text":"Grave"}]

        for c in colors:
            pixmap = QPixmap(25,25)
            pixmap.fill(QColor(c["color"]))
            Icon = QIcon(pixmap)
            self.cmbNivel.addItem(Icon,c["text"],c)

    def obtenerVariablesFuncionesCallback(self,response):
        if isinstance(response,Exception): # if data returned is a Exception
            self.btnReload.show()
            self.lblStatus.setText("¡Error! Ha ocurrido un error")
            self.movie = QMovie(":/source/img/Error.png")
            self.movie.start()
            self.Status.setMovie(self.movie)
            return
        if len(response) == 0:
            self.btnReload.show()
            self.lblStatus.setText("¡Vacio! Aún no hay nada")
            self.movie = QMovie(":/source/img/Empty.png")
            self.movie.start()
            self.Status.setMovie(self.movie)
            return
        self.btnReload.clicked.disconnect(self.obtenerVariablesFunciones)
        self.UtilsFrame.deleteLater()
        self.variablesFunciones = response
        self.updateVariablesFunciones()
        if self.IsEdit:
            self.lblTitle.setText("Editar Variable")
            self.txtNombre.setText(self.variable.nombre)
            self.txtExpresion.setText("" if self.variable.expresion is None else  self.variable.expresion)
            self.cmbSenal.setCurrentIndex(self.cmbSenal.findText("Analogica" if self.variable.analogic else "Digital"))
            self.cmbTipo.setCurrentIndex(self.cmbTipo.findText("Lectura" if not self.variable.output else "Escritura"))
            self.cmbColor.setCurrentIndex(self.cmbColor.findText(self.variable.displayColor) if self.variable.displayColor != None else 0 )
            self.boxNotificar.setChecked(True if self.variable.notify != None else False)
            self.cmbVariable.setCurrentIndex(self.cmbVariable.findText(self.variable.pin))
            self.cmbNotificar.setCurrentIndex(self.cmbNotificar.findText(self.variable.notify.replace("-"," ")[0:2].strip()) if self.variable.notify != None else 0 )
            self.txtNotificar.setValue(int(self.variable.notify[2:]) if self.variable.notify != None else 0 )
            self.cmbNivel.setCurrentIndex(self.cmbNivel.findText( self.findNotify(self.variable.nivel) ) if self.variable.nivel != None else 0)
        self.ContentLayout.addWidget(self.ContentFrame)

    def findNotify(self,color):
        switcher = {
            "aqua":"Informativa",
            "orange":"Advertencia",
            "green":"Normal",
            "red":"Grave"
        }
        return switcher.get(color,"Informativa")

    def updateVariablesFunciones(self):
        self.cmbSenal_CurrentIndexChange()
        self.cmbVariable.clear()
        variables = list(self.filterVars(True if self.cmbTipo.currentText() == "Escritura" else False))
        for v in variables:
            self.cmbVariable.addItem(v["PIN"],v)

    def boxNotificar_StateChange(self,status):
        if status == 0:
           self.cmbNotificar.setEnabled(False)
           self.cmbNivel.setEnabled(False)
           self.txtNotificar.setEnabled(False)
        else:
           self.cmbNotificar.setEnabled(True)
           self.cmbNivel.setEnabled(True)
           self.txtNotificar.setEnabled(True)
                
    def cmbSenal_CurrentIndexChange(self):
        IsOutput = True if self.cmbTipo.currentText() == "Escritura" else False
        Analogic = True if self.cmbSenal.currentText() == "Analogica" else False

        self.cmbColor.setEnabled(False)
        self.txtExpresion.setEnabled(False)
        self.boxNotificar.setEnabled(False)
        self.cmbNotificar.setEnabled(False)
        self.txtNotificar.setEnabled(False)
        self.boxNotificar.setChecked(False)
        if not IsOutput and Analogic: # Lectura analogica
           self.txtExpresion.setEnabled(True)
           self.boxNotificar.setEnabled(True)
        if not IsOutput and not Analogic: #Lectura Digital
           self.cmbColor.setEnabled(True)
           self.boxNotificar.setEnabled(True)

    def filterVars(self,IsOutput = False):
        for v in self.variablesFunciones:
           if self.isBool(v["IsOutput"]) == IsOutput:
                yield(v)

    def isBool(self,v):
        return str(v).lower() in ("yes","True","true",1,"t")

    def retranslateUi(self, AgregarVariableModal):
        _translate = QtCore.QCoreApplication.translate
        AgregarVariableModal.setWindowTitle(_translate("AgregarVariableModal", "Sistema SCADA"))
        self.lblSCADA.setText(_translate("AgregarVariableModal", "SCADA"))
        self.lblTitle.setText(_translate("AgregarVariableModal", "Agregar Variable"))
        self.ContentBox.setTitle(_translate("AgregarVariableModal", "Información"))
        self.label_8.setText(_translate("AgregarVariableModal", "Nivel:"))
        self.lblNombre.setText(_translate("AgregarVariableModal", "Nombre:"))
        self.boxNotificar.setText(_translate("AgregarVariableModal", "Si X"))
        self.label_9.setText(_translate("AgregarVariableModal", "Expresion:"))
        self.label_10.setText(_translate("AgregarVariableModal", "Notificar:"))
        self.label_11.setText(_translate("AgregarVariableModal", "Color:"))
        self.label_12.setText(_translate("AgregarVariableModal", "Variable:"))
        self.btnAceptar_2.setText(_translate("AgregarVariableModal", "OK"))
        self.label_13.setText(_translate("AgregarVariableModal", "Tipo:"))
        self.label_14.setText(_translate("AgregarVariableModal", "Señal:"))
        self.lblStatus.setText(_translate("AgregarVariableModal", "Cargando..."))
        self.btnReload.setText(_translate("AgregarVariableModal", "Reintentar"))