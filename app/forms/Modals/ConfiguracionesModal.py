from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from classes import Logica,Worker,workSpace, configuracion, modal
from resources import *

class UIConfiguracionesModal(modal):

    def __init__(self,**kwargs):
        super(UIConfiguracionesModal,self).__init__(**kwargs)
    
    def setupUI(self):
        ConfiguracionesModal = self
        ConfiguracionesModal.setObjectName("ConfiguracionesModal")
        ConfiguracionesModal.setWindowModality(QtCore.Qt.WindowModal)
        ConfiguracionesModal.resize(497, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfiguracionesModal.sizePolicy().hasHeightForWidth())
        ConfiguracionesModal.setSizePolicy(sizePolicy)
        ConfiguracionesModal.setMinimumSize(QtCore.QSize(480, 720))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        ConfiguracionesModal.setFont(font)
        ConfiguracionesModal.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfiguracionesModal.setWindowIcon(icon)
        ConfiguracionesModal.setStyleSheet("background-color: rgb(255, 255, 255);")
        ConfiguracionesModal.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConfiguracionesModal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(ConfiguracionesModal)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentBox.sizePolicy().hasHeightForWidth())
        self.ContentBox.setSizePolicy(sizePolicy)
        self.ContentBox.setMinimumSize(QtCore.QSize(401, 520))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ContentBox.setFont(font)
        self.ContentBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ContentBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.ContentBox.setFlat(False)
        self.ContentBox.setObjectName("ContentBox")
        self.ContentLayout = QtWidgets.QVBoxLayout(self.ContentBox)
        self.ContentLayout.setContentsMargins(10, 10, 10, 10)
        self.ContentLayout.setSpacing(10)
        self.ContentLayout.setObjectName("ContentLayout")
        self.ContentAPILocal = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.ContentAPILocal.setFont(font)
        self.ContentAPILocal.setObjectName("ContentAPILocal")
        self.ContentLocalLayout = QtWidgets.QGridLayout(self.ContentAPILocal)
        self.ContentLocalLayout.setContentsMargins(0, 0, 0, 0)
        self.ContentLocalLayout.setSpacing(0)
        self.ContentLocalLayout.setObjectName("ContentLocalLayout")
        self.lblIPLocal = QtWidgets.QLabel(self.ContentAPILocal)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblIPLocal.setFont(font)
        self.lblIPLocal.setLineWidth(0)
        self.lblIPLocal.setObjectName("lblIPLocal")
        self.ContentLocalLayout.addWidget(self.lblIPLocal, 0, 0, 1, 1)
        self.txtIPLocal = QtWidgets.QLineEdit(self.ContentAPILocal)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtIPLocal.setFont(font)
        self.txtIPLocal.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtIPLocal.setObjectName("txtIPLocal")
        self.ContentLocalLayout.addWidget(self.txtIPLocal, 0, 1, 1, 1)
        self.lblPuertoLocal = QtWidgets.QLabel(self.ContentAPILocal)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblPuertoLocal.setFont(font)
        self.lblPuertoLocal.setLineWidth(0)
        self.lblPuertoLocal.setObjectName("lblPuertoLocal")
        self.ContentLocalLayout.addWidget(self.lblPuertoLocal, 0, 2, 1, 1)
        self.txtPuertoLocal = QtWidgets.QLineEdit(self.ContentAPILocal)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtPuertoLocal.setFont(font)
        self.txtPuertoLocal.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtPuertoLocal.setObjectName("txtPuertoLocal")
        self.ContentLocalLayout.addWidget(self.txtPuertoLocal, 0, 3, 1, 1)
        self.ContentMongoDB = QtWidgets.QGroupBox() #asd
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ContentMongoDB.setFont(font)
        self.ContentMongoDB.setObjectName("ContentMongoDB")
        self.ContentMongoLayout = QtWidgets.QGridLayout(self.ContentMongoDB)
        self.ContentMongoLayout.setContentsMargins(0, 0, 0, 0)
        self.ContentMongoLayout.setSpacing(0)
        self.ContentMongoLayout.setObjectName("ContentMongoLayout")
        self.lblIPMongo = QtWidgets.QLabel(self.ContentMongoDB)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblIPMongo.setFont(font)
        self.lblIPMongo.setLineWidth(0)
        self.lblIPMongo.setObjectName("lblIPMongo")
        self.ContentMongoLayout.addWidget(self.lblIPMongo, 0, 0, 1, 1)
        self.txtIPMongo = QtWidgets.QLineEdit(self.ContentMongoDB)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtIPMongo.setFont(font)
        self.txtIPMongo.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtIPMongo.setObjectName("txtIPMongo")
        self.ContentMongoLayout.addWidget(self.txtIPMongo, 0, 1, 1, 1)
        self.lblPuertoMOngo = QtWidgets.QLabel(self.ContentMongoDB)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblPuertoMOngo.setFont(font)
        self.lblPuertoMOngo.setLineWidth(0)
        self.lblPuertoMOngo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPuertoMOngo.setObjectName("lblPuertoMOngo")
        self.ContentMongoLayout.addWidget(self.lblPuertoMOngo, 0, 2, 1, 1)
        self.txtPuertoMongo = QtWidgets.QLineEdit(self.ContentMongoDB)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtPuertoMongo.setFont(font)
        self.txtPuertoMongo.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtPuertoMongo.setObjectName("txtPuertoMongo")
        self.ContentMongoLayout.addWidget(self.txtPuertoMongo, 0, 3, 1, 1)
        self.lblUsuarioMongo = QtWidgets.QLabel(self.ContentMongoDB)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsuarioMongo.setFont(font)
        self.lblUsuarioMongo.setLineWidth(0)
        self.lblUsuarioMongo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUsuarioMongo.setObjectName("lblUsuarioMongo")
        self.ContentMongoLayout.addWidget(self.lblUsuarioMongo, 1, 0, 1, 1)
        self.txtUsuarioMongo = QtWidgets.QLineEdit(self.ContentMongoDB)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtUsuarioMongo.setFont(font)
        self.txtUsuarioMongo.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        #self.txtUsuarioMongo.setInputMask("")
        self.txtUsuarioMongo.setText("")
        self.txtUsuarioMongo.setObjectName("txtUsuarioMongo")
        self.ContentMongoLayout.addWidget(self.txtUsuarioMongo, 1, 1, 1, 1)
        self.lblPasswordMongo = QtWidgets.QLabel(self.ContentMongoDB)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblPasswordMongo.setFont(font)
        self.lblPasswordMongo.setLineWidth(0)
        self.lblPasswordMongo.setObjectName("lblPasswordMongo")
        self.ContentMongoLayout.addWidget(self.lblPasswordMongo, 1, 2, 1, 1)
        self.txtPassMongo = QtWidgets.QLineEdit(self.ContentMongoDB)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtPassMongo.setFont(font)
        self.txtPassMongo.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtPassMongo.setInputMask("")
        self.txtPassMongo.setText("")
        self.txtPassMongo.setObjectName("txtPassMongo")
        self.ContentMongoLayout.addWidget(self.txtPassMongo, 1, 3, 1, 1)
        self.ContentAPIExterna = QtWidgets.QGroupBox() # asd
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ContentAPIExterna.setFont(font)
        self.ContentAPIExterna.setObjectName("ContentAPIExterna")
        self.ContentExternaLayout = QtWidgets.QGridLayout(self.ContentAPIExterna)
        self.ContentExternaLayout.setContentsMargins(0, 0, 0, 0)
        self.ContentExternaLayout.setSpacing(0)
        self.ContentExternaLayout.setObjectName("ContentExternaLayout")
        self.lblIPExterna = QtWidgets.QLabel(self.ContentAPIExterna)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblIPExterna.setFont(font)
        self.lblIPExterna.setLineWidth(0)
        self.lblIPExterna.setObjectName("lblIPExterna")
        self.ContentExternaLayout.addWidget(self.lblIPExterna, 0, 0, 1, 1)
        self.txtIPExterna = QtWidgets.QLineEdit(self.ContentAPIExterna)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtIPExterna.setFont(font)
        self.txtIPExterna.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        #self.txtIPExterna.setInputMask("")
        self.txtIPExterna.setObjectName("txtIPExterna")
        self.ContentExternaLayout.addWidget(self.txtIPExterna, 0, 1, 1, 1)
        self.btnAceptar = QtWidgets.QPushButton()
        self.btnAceptar.setMinimumSize(QtCore.QSize(128, 48))
        self.btnAceptar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setStyleSheet("border:1px solid green;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAceptar.setIcon(icon2)
        self.btnAceptar.setIconSize(QtCore.QSize(24, 24))
        self.btnAceptar.setShortcut("")
        self.btnAceptar.setCheckable(False)
        self.btnAceptar.setFlat(True)
        self.btnAceptar.setObjectName("btnAceptar")
        #UtilsFrame
        self.UtilsFrame = QtWidgets.QFrame(self.ContentBox)
        self.UtilsFrame.setGeometry(QtCore.QRect(30, 20, 256, 132))
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
        self.Status.setMinimumSize(QtCore.QSize(64,64))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/retry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon)
        self.btnReload.setIconSize(QtCore.QSize(24, 24))
        self.btnReload.setFlat(True)
        self.btnReload.setObjectName("btnReload")
        self.utilsLayout.addWidget(self.btnReload, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.ContentBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.MainFrame)
        self.retranslateUi(ConfiguracionesModal)
        QtCore.QMetaObject.connectSlotsByName(ConfiguracionesModal)
        self.btnReload.hide()
        #Movie
        self.movie = QMovie(":/source/img/Cargando.gif")
        self.movie.setScaledSize(QtCore.QSize(64,64))
        self.Status.setMovie(self.movie)

        self.ContentLayout.addWidget(self.UtilsFrame, 0, QtCore.Qt.AlignHCenter)

        # listener
        self.parent.signals.resize.connect(self.center)
        self.btnExit.clicked.connect(self.exit)
        self.btnAceptar.clicked.connect(self.btnAceptar_Click)
        self.btnReload.clicked.connect(self.ObtenerConfguraciones)

        self.shortcut = QtWidgets.QShortcut(QtCore.Qt.Key_Return,self)
        self.shortcut.activated.connect(self.btnAceptar_Click)

    def showEvent(self,event):
        self.center()
        self.ObtenerConfguraciones()

    def ObtenerConfguraciones(self):
        self.btnReload.hide()
        self.lblStatus.setText("Cargando...")
        self.movie = QMovie(":/source/img/Cargando.gif")
        self.movie.setScaledSize(QtCore.QSize(64,64))
        self.movie.start()
        self.Status.setMovie(self.movie)
        self.worker = Worker(Logica.ObtenerConfiguraciones,**{"access_token":self.session.access_token})
        self.worker.signals.finished.connect(self.obtenerConfiguracionesCallBack)
        self.worker.start()
        
    def obtenerConfiguracionesCallBack(self,response):
        self.worker.finished.disconnect(self.obtenerConfiguracionesCallBack)
        self.worker.deleteLater()
        del self.worker
        if isinstance(response,Exception):
            self.btnReload.show()
            self.lblStatus.setText("??Error! Ha ocurrido un error")
            self.movie = QMovie(":/source/img/Error.png")
            self.movie.setScaledSize(QtCore.QSize(64,64))
            self.movie.start()
            self.Status.setMovie(self.movie)
            return
        if len(response) == 0:
            self.btnReload.show()
            self.lblStatus.setText("??Vacio! A??n no hay nada")
            self.movie = QMovie(":/source/img/Empty.png")
            self.movie.setScaledSize(QtCore.QSize(64,64))
            self.movie.start()
            self.Status.setMovie(self.movie)
            return
        self.btnReload.clicked.disconnect(self.ObtenerConfguraciones)
        self.UtilsFrame.deleteLater()
        self.config = configuracion(response)
        self.txtIPLocal.setText(response["APISCADA"]["Host"])
        self.txtPuertoLocal.setText(response["APISCADA"]["Port"])
        self.txtIPMongo.setText(response["MONGO"]["MONGO_HOST"])
        self.txtPuertoMongo.setText(response["MONGO"]["MONGO_PORT"])
        self.txtUsuarioMongo.setText(response["MONGO"]["MONGO_USER"])
        self.txtPassMongo.setText(response["MONGO"]["MONGO_PASS"])
        self.txtIPExterna.setText(response["APIPARTICLE"]["URI"])
        self.ContentLayout.addWidget(self.ContentAPILocal)
        self.ContentLayout.addWidget(self.ContentMongoDB)
        self.ContentLayout.addWidget(self.ContentAPIExterna)
        self.ContentLayout.addWidget(self.btnAceptar, 0, QtCore.Qt.AlignHCenter)

    def btnAceptar_Click(self):
        try:
            self.config.apiLocal.IP = self.txtIPLocal.text()
            self.config.apiLocal.puerto = self.txtPuertoLocal.text()
            self.config.mongoDB.IP = self.txtIPMongo.text()
            self.config.mongoDB.puerto = self.txtPuertoMongo.text()
            self.config.mongoDB.usuario = self.txtUsuarioMongo.text()
            self.config.mongoDB.password = self.txtPassMongo.text()
            self.config.apiExterna.uri = self.txtIPExterna.text()
        except ValueError as e:
            QMessageBox.warning(self,"??Error!",str(e))
            return
        response = QMessageBox.question(self,"??Confirmacion!","??Seguro que desea guardar estas configuraciones?\nCualquier error podria provocar que API SCADA\nno se ejecute correctamente")
        if response == QMessageBox.Yes:
            self.guardarConfiguracione()

    def guardarConfiguracione(self):
        self.btnAceptar.hide()
        self.Status = QtWidgets.QLabel(self.ContentBox)
        self.Status.setMaximumSize(QtCore.QSize(64, 64))
        self.Status.setText("")
        self.Status.setPixmap(QtGui.QPixmap(":/source/img/Cargando.gif"))
        self.Status.setScaledContents(True)
        self.Status.setObjectName("Status")
        self.movie = QMovie(":/source/img/Cargando.gif")
        self.movie.start()
        self.Status.setMovie(self.movie)
        self.ContentLayout.addWidget(self.Status, 0, QtCore.Qt.AlignHCenter)
        self.worker = Worker(Logica.GuardarConfiguraciones,**{"access_token":self.getAccessToken(),"data":self.config.toJSON() } )
        self.worker.signals.finished.connect(self.guardarConfiguracionesCallback)
        self.worker.start()

    def guardarConfiguracionesCallback(self,response):
        self.worker.finished.disconnect(self.guardarConfiguracionesCallback)
        self.worker.deleteLater()
        del self.worker
        self.movie.deleteLater()
        self.Status.deleteLater()
        if isinstance(response,Exception):
            QMessageBox.warning(self,"??Error!",str(response))
            self.btnAceptar.show()
            return
        if response["success"] == "false":
            QMessageBox.warning(self,"??Error!",str(response["Message"]))
            self.btnAceptar.show()
        else:
            QMessageBox.information(self,"??Exito!","??Exito! Configuraciones actualizadas\nSurtiran efecto la proxima vez que\nse inicie el servicio API SCADA")
            self.success(None)

    def disconnectSignals(self):
        self.parent.signals.resize.disconnect(self.center)
        self.btnExit.clicked.disconnect(self.exit)
        self.btnAceptar.clicked.disconnect(self.btnAceptar_Click)

    def retranslateUi(self, ConfiguracionesModal):
        _translate = QtCore.QCoreApplication.translate
        ConfiguracionesModal.setWindowTitle(_translate("ConfiguracionesModal", "Sistema SCADA"))
        self.lblSCADA.setText(_translate("ConfiguracionesModal", "SCADA"))
        self.lblTitle.setText(_translate("ConfiguracionesModal", "Configuraciones"))
        self.ContentBox.setTitle(_translate("ConfiguracionesModal", "Conexi??n"))
        self.ContentAPILocal.setTitle(_translate("ConfiguracionesModal", "API Local"))
        self.lblIPLocal.setText(_translate("ConfiguracionesModal", "Direcci??n IP:"))
        self.txtIPLocal.setText(_translate("ConfiguracionesModal", "127.0.0.1"))
        self.lblPuertoLocal.setText(_translate("ConfiguracionesModal", "Puerto:"))
        self.txtPuertoLocal.setText(_translate("ConfiguracionesModal", "8080"))
        self.ContentMongoDB.setTitle(_translate("ConfiguracionesModal", "MongoDB"))
        self.lblIPMongo.setText(_translate("ConfiguracionesModal", "Direcci??n IP:"))
        self.txtIPMongo.setText(_translate("ConfiguracionesModal", "127.0.0.1"))
        self.lblPuertoMOngo.setText(_translate("ConfiguracionesModal", "Puerto:"))
        self.txtPuertoMongo.setText(_translate("ConfiguracionesModal", "8080"))
        self.lblUsuarioMongo.setText(_translate("ConfiguracionesModal", "Usuario:"))
        self.lblPasswordMongo.setText(_translate("ConfiguracionesModal", "Contrase??a:"))
        self.ContentAPIExterna.setTitle(_translate("ConfiguracionesModal", "API Externa"))
        self.lblIPExterna.setText(_translate("ConfiguracionesModal", "Direcci??n IP:"))
        self.txtIPExterna.setText(_translate("ConfiguracionesModal", "api.particle.io/v1/devices"))
        self.btnAceptar.setText(_translate("ConfiguracionesModal", "Aceptar"))
        self.lblStatus.setText(_translate("Form", "Cargando..."))
        self.btnReload.setText(_translate("Form", "Reintentar"))
