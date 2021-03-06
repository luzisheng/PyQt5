from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from classes import modal, Logica, Worker
from datetime import date, timedelta
from functools import partial
from resources import *

class UIReportesModal(modal):

    def __init__(self,**kwargs):
        self.UIContainer = dict()
        super(UIReportesModal,self).__init__(**kwargs)

    def setupUI(self):
        ReportesModal = self
        ReportesModal.setObjectName("ReportesModal")
        ReportesModal.setWindowModality(QtCore.Qt.WindowModal)
        ReportesModal.resize(740, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReportesModal.sizePolicy().hasHeightForWidth())
        ReportesModal.setSizePolicy(sizePolicy)
        ReportesModal.setMinimumSize(QtCore.QSize(480, 620))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        ReportesModal.setFont(font)
        ReportesModal.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReportesModal.setWindowIcon(icon)
        ReportesModal.setStyleSheet("background-color: rgb(255, 255, 255);")
        ReportesModal.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.verticalLayout = QtWidgets.QVBoxLayout(ReportesModal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(ReportesModal)
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
        self.lblInicio = QtWidgets.QLabel(self.ContentBox)
        self.lblInicio.setGeometry(QtCore.QRect(215, 12, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblInicio.setFont(font)
        self.lblInicio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblInicio.setObjectName("lblInicio")
        self.btnAgregar = QtWidgets.QPushButton(self.ContentBox)
        self.btnAgregar.setGeometry(QtCore.QRect(580, 0, 80, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAgregar.sizePolicy().hasHeightForWidth())
        self.btnAgregar.setSizePolicy(sizePolicy)
        self.btnAgregar.setMinimumSize(QtCore.QSize(75, 40))
        self.btnAgregar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setStyleSheet("border:1px solid green;top:0px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/Reportes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregar.setIcon(icon2)
        self.btnAgregar.setIconSize(QtCore.QSize(24, 24))
        self.btnAgregar.setShortcut("")
        self.btnAgregar.setCheckable(False)
        self.btnAgregar.setFlat(True)
        self.btnAgregar.setObjectName("btnAgregar")
        self.dateStart = QtWidgets.QDateEdit(self.ContentBox)
        self.dateStart.setGeometry(QtCore.QRect(261, 8, 85, 26))
        self.dateStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 6, 24), QtCore.QTime(0, 0, 0)))
        self.dateStart.setCalendarPopup(True)
        self.dateStart.setObjectName("dateStart")
        self.btnExportar = QtWidgets.QPushButton(self.ContentBox)
        self.btnExportar.setGeometry(QtCore.QRect(10, 0, 85, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExportar.sizePolicy().hasHeightForWidth())
        self.btnExportar.setSizePolicy(sizePolicy)
        self.btnExportar.setMinimumSize(QtCore.QSize(80, 35))
        self.btnExportar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnExportar.setFont(font)
        self.btnExportar.setStyleSheet("border:1px solid green;top:0px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/source/img/Exportar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportar.setIcon(icon3)
        self.btnExportar.setIconSize(QtCore.QSize(24, 24))
        self.btnExportar.setShortcut("")
        self.btnExportar.setCheckable(False)
        self.btnExportar.setFlat(True)
        self.btnExportar.setObjectName("btnExportar")
        self.tableWidget = QtWidgets.QTableWidget(self.ContentBox)
        self.tableWidget.setGeometry(QtCore.QRect(2, 50, 668, 469))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.dateEnd = QtWidgets.QDateEdit(self.ContentBox)
        self.dateEnd.setGeometry(QtCore.QRect(400, 8, 85, 26))
        self.dateEnd.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 6, 25), QtCore.QTime(0, 0, 0)))
        self.dateEnd.setCalendarPopup(True)
        self.dateEnd.setObjectName("dateEnd")
        self.lblInicio_2 = QtWidgets.QLabel(self.ContentBox)
        self.lblInicio_2.setGeometry(QtCore.QRect(350, 12, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblInicio_2.setFont(font)
        self.lblInicio_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblInicio_2.setObjectName("lblInicio_2")
        self.UtilsFrame = QtWidgets.QFrame(self.ContentBox)
        self.UtilsFrame.setGeometry(QtCore.QRect(220, 210, 256, 132))
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
        self.cmbNivel = QtWidgets.QComboBox(self.ContentBox)
        self.cmbNivel.setGeometry(QtCore.QRect(490, 10, 81, 25))
        self.cmbNivel.setObjectName("cmbNivel")
        self.btnReload = QtWidgets.QPushButton(self.ContentBox)
        self.btnReload.setGeometry(QtCore.QRect(100, 0, 100, 40))
        self.btnReload.setMinimumSize(QtCore.QSize(0, 16))
        self.btnReload.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnReload.setFont(font)
        self.btnReload.setStyleSheet("border: 1px solid rgb(0, 170, 255);padding:5px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/source/img/retry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon4)
        self.btnReload.setIconSize(QtCore.QSize(24, 24))
        self.btnReload.setFlat(True)
        self.btnReload.setObjectName("btnReload")
        self.verticalLayout_2.addWidget(self.ContentBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.MainFrame)
        self.retranslateUi(ReportesModal)
        QtCore.QMetaObject.connectSlotsByName(ReportesModal)
        self.tableWidget.hide()
        self.center()
        self.addNotifyItems()
        self.cmbNivel.setCurrentIndex(self.cmbNivel.findText(self.findNotify("white")))
        self.dateStart.setDate(date.today() - timedelta(days=1))
        self.dateEnd.setDate(date.today() + timedelta(days=1))
        #listener
        self.parent.signals.resize.connect(self.center)
        self.btnExit.clicked.connect(self.exit)
        self.cmbNivel.currentIndexChanged.connect(self.obtenerReportes)
        self.dateStart.dateChanged.connect(self.obtenerReportes)
        self.dateEnd.dateChanged.connect(self.obtenerReportes)
        self.btnReload.clicked.connect(self.obtenerReportes)
        self.btnExportar.clicked.connect(self.exportarReportes)
        
    def showEvent(self,evt):
        self.obtenerReportes()

    def obtenerReportes(self,index=0):
        self.tableWidget.hide()
        self.UtilsFrame.show()
        self.updateState("Cargando",QMovie(":/source/img/Cargando.gif"))
        dateStart = self.dateStart.date().toPyDate().__format__("%Y-%m-%d")
        dateEnd = self.dateEnd.date().toPyDate().__format__("%Y-%m-%d")
        nivel = self.cmbNivel.itemData(self.cmbNivel.currentIndex())["color"]
        if dateStart > dateEnd:
           self.updateState("??Error! Fechas invalidas",QMovie(":/source/img/Error.png"))
           QMessageBox.warning(self,"??Error!","??Error! Rango de fechas invalido")
           return
        self.worker = Worker(Logica.ObtenerReportes,**{"access_token":self.session.access_token,"dateStart":dateStart,"dateEnd":dateEnd,"nivel":nivel})
        self.worker.signals.finished.connect(self.obtenerReportesAction)
        self.worker.start()

    def obtenerReportesAction(self,response):
        self.worker.signals.finished.disconnect(self.obtenerReportesAction)
        self.worker.deleteLater()
        del self.worker
        if isinstance(response,Exception):
           self.updateState("??Error! Ha ocurrido un error",QMovie(":/source/img/Error.png"))
           return
        if len(response) == 0:
           self.updateState("??Vacio! No hay reportes", QMovie(":/source/img/Empty.png"))
           return
        self.reportes= response
        self.UtilsFrame.hide()
        self.tableWidget.show()
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(response))
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(["Nivel","Variable","Dispositivo","Fecha","Hora","Condicion","Usuario","Valor","Mensaje"])
        for i,reporte in enumerate(response):
            pixmap = QPixmap(25,25)
            pixmap.fill(QColor(reporte.nivel))
            Icon = QIcon(pixmap)
            self.tableWidget.setItem(i,0,QTableWidgetItem(Icon,self.findNotify(reporte.nivel)))
            self.tableWidget.setItem(i,1,QTableWidgetItem(reporte.nombreVariable))
            self.tableWidget.setItem(i,2,QTableWidgetItem(reporte.nombreDispositivo))
            self.tableWidget.setItem(i,3,QTableWidgetItem(reporte.fecha))
            self.tableWidget.setItem(i,4,QTableWidgetItem(reporte.hora))
            self.tableWidget.setItem(i,5,QTableWidgetItem(reporte.condicion))
            self.tableWidget.setItem(i,6,QTableWidgetItem(reporte.usuario))
            self.tableWidget.setItem(i,7,QTableWidgetItem(reporte.value.__str__()))
            self.tableWidget.setItem(i,8,QTableWidgetItem(reporte.mensaje))

    def exportarReportes(self):
        from PyQt5.QtWidgets import QFileDialog, QMessageBox
        if len(self.reportes) == 0:
            QMessageBox.information(self,"??Aviso!","No hay nada que exportar")
            return
        fileName = QFileDialog.getSaveFileName(self,"Abrir",filter="Excel files (*.xlsx)")  # options=QtWidgets.QFileDialog.DontUseNativeDialog
        if all(fileName):
            response = Logica.ExportarReportes(filename=fileName[0],reportes=self.reportes)
            if response is False:
                QMessageBox.warning(self,"??Error!","Fallo al guardar")
                return
            QMessageBox.information(self,"??Exito!","Exportado exitosamente")
            
    def addNotifyItems(self):
        colors = [{"color":"aqua","text":"Informativa"},
                 {"color":"orange","text":"Advertencia"},
                 {"color":"green","text":"Normal"},
                 {"color":"red","text":"Grave"},
                 {"color":"white","text":"Todos"}]

        for c in colors:
            pixmap = QPixmap(25,25)
            pixmap.fill(QColor(c["color"]))
            Icon = QIcon(pixmap)
            self.cmbNivel.addItem(Icon,c["text"],c)

    def findNotify(self,color):
        switcher = {
            "aqua":"Informativa",
            "orange":"Advertencia",
            "green":"Normal",
            "red":"Grave",
            "white":"Todos"
        }
        return switcher.get(color,"Informativa")
        
    def disconnectSignals(self): 
        self.parent.signals.resize.disconnect(self.center)
        self.btnExit.clicked.disconnect(self.exit)
        self.cmbNivel.currentIndexChanged.disconnect(self.obtenerReportes)
        self.dateStart.dateChanged.disconnect(self.obtenerReportes)
        self.dateEnd.dateChanged.disconnect(self.obtenerReportes)
        self.btnReload.clicked.disconnect(self.obtenerReportes)
        
    def updateState(self,text,Movie = None):
        self.Status.setMovie(Movie)
        self.lblStatus.setText(text)
        Movie.start() if Movie != None else None
        Movie.setScaledSize(QtCore.QSize(64,64))

    def retranslateUi(self, ReportesModal):
        _translate = QtCore.QCoreApplication.translate
        ReportesModal.setWindowTitle(_translate("ReportesModal", "Sistema SCADA"))
        self.lblSCADA.setText(_translate("ReportesModal", "SCADA"))
        self.lblTitle.setText(_translate("ReportesModal", "Reportes"))
        self.lblInicio.setText(_translate("ReportesModal", "Desde"))
        self.btnAgregar.setText(_translate("ReportesModal", "Filtrar"))
        self.dateStart.setDisplayFormat(_translate("ReportesModal", "d/M/yyyy"))
        self.btnExportar.setText(_translate("ReportesModal", "Exportar"))
        self.dateEnd.setDisplayFormat(_translate("ReportesModal", "d/M/yyyy"))
        self.lblInicio_2.setText(_translate("ReportesModal", "Hasta:"))
        self.lblStatus.setText(_translate("ReportesModal", "Cargando..."))
        self.btnReload.setText(_translate("ReportesModal", "Actualizar"))

