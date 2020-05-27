from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from classes.inheritables.widget import widget
from classes.objects.workSpace import variable

class UIDIVariable(widget):

    def __init__(self):
        self.__variable = None
        self.__dispostivo = None
        super(UIDIVariable,self).__init__()
        self.setupUi()

    def setupUi(self):
        DIVariable = self
        DIVariable.setObjectName("DIVariable")
        DIVariable.resize(150, 25)
        DIVariable.setMinimumSize(QtCore.QSize(150, 25))
        self.MainFrame = QtWidgets.QFrame(DIVariable)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 150, 25))
        self.MainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setLineWidth(0)
        self.MainFrame.setObjectName("MainFrame")
        self.lblTileScroll = QtWidgets.QScrollArea(self.MainFrame)
        self.lblTileScroll.setGeometry(QtCore.QRect(0, 0, 110, 25))
        self.lblTileScroll.setMinimumSize(QtCore.QSize(110, 20))
        self.lblTileScroll.setMaximumSize(QtCore.QSize(100, 25))
        self.lblTileScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTileScroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTileScroll.setLineWidth(0)
        self.lblTileScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lblTileScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblTileScroll.setWidgetResizable(True)
        self.lblTileScroll.setObjectName("lblTileScroll")
        self.ScrollLayout = QtWidgets.QWidget()
        self.ScrollLayout.setGeometry(QtCore.QRect(0, 0, 110, 25))
        self.ScrollLayout.setObjectName("ScrollLayout")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.ScrollLayout)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.lblTitle = QtWidgets.QLabel(self.ScrollLayout)
        self.lblTitle.setMaximumSize(QtCore.QSize(16666672, 16666672))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setLineWidth(0)
        self.lblTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblTitle.setWordWrap(True)
        self.lblTitle.setIndent(5)
        self.lblTitle.setObjectName("lblTitle")
        self.vboxlayout.addWidget(self.lblTitle)
        self.lblTileScroll.setWidget(self.ScrollLayout)
        self.lblValue = QtWidgets.QLabel(self.MainFrame)
        self.lblValue.setGeometry(QtCore.QRect(123, 3, 20, 20))
        self.lblValue.setStyleSheet("background-color:green;border-radius:8px;")
        self.lblValue.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblValue.setText("")
        self.lblValue.setObjectName("lblValue")

        self.retranslateUi(DIVariable)
        QtCore.QMetaObject.connectSlotsByName(DIVariable)

    def retranslateUi(self, DIVariable):
        _translate = QtCore.QCoreApplication.translate
        DIVariable.setWindowTitle(_translate("DIVariable", "Form"))
        self.lblTitle.setText(_translate("DIVariable", "DI0"))
