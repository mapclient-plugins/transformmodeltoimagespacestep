# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label1)

        self.lineEdit1 = QLineEdit(self.configGroupBox)
        self.lineEdit1.setObjectName(u"lineEdit1")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit1)

        self.label2 = QLabel(self.configGroupBox)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label2)

        self.lineEdit2 = QLineEdit(self.configGroupBox)
        self.lineEdit2.setObjectName(u"lineEdit2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit2)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.label1.setText(QCoreApplication.translate("ConfigureDialog", u"Mirror:  ", None))
        self.label2.setText(QCoreApplication.translate("ConfigureDialog", u"Z Shift:  ", None))
    # retranslateUi

