# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emprestimo_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(325, 213)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_cpf_funcionario_emprestimo = QLabel(self.widget)
        self.lbl_cpf_funcionario_emprestimo.setObjectName(u"lbl_cpf_funcionario_emprestimo")

        self.verticalLayout.addWidget(self.lbl_cpf_funcionario_emprestimo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_cpf_funcionario_emprestimo = QLineEdit(self.widget)
        self.txt_cpf_funcionario_emprestimo.setObjectName(u"txt_cpf_funcionario_emprestimo")

        self.horizontalLayout_2.addWidget(self.txt_cpf_funcionario_emprestimo)

        self.btn_consulta_funcionario = QPushButton(self.widget)
        self.btn_consulta_funcionario.setObjectName(u"btn_consulta_funcionario")

        self.horizontalLayout_2.addWidget(self.btn_consulta_funcionario)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbl_nome_funcionario_emprestimo = QLabel(self.widget)
        self.lbl_nome_funcionario_emprestimo.setObjectName(u"lbl_nome_funcionario_emprestimo")

        self.verticalLayout.addWidget(self.lbl_nome_funcionario_emprestimo)

        self.txt_nome_funcionario_emprestimo = QLineEdit(self.widget)
        self.txt_nome_funcionario_emprestimo.setObjectName(u"txt_nome_funcionario_emprestimo")

        self.verticalLayout.addWidget(self.txt_nome_funcionario_emprestimo)

        self.lbl_tipo_uniforme = QLabel(self.widget)
        self.lbl_tipo_uniforme.setObjectName(u"lbl_tipo_uniforme")

        self.verticalLayout.addWidget(self.lbl_tipo_uniforme)

        self.cb_uniforme = QComboBox(self.widget)
        self.cb_uniforme.setObjectName(u"cb_uniforme")

        self.verticalLayout.addWidget(self.cb_uniforme)

        self.btn_confirmar_emprestimo = QPushButton(self.widget)
        self.btn_confirmar_emprestimo.setObjectName(u"btn_confirmar_emprestimo")

        self.verticalLayout.addWidget(self.btn_confirmar_emprestimo)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_cpf_funcionario_emprestimo.setText(QCoreApplication.translate("Dialog", u"CPF do funcionario", None))
        self.btn_consulta_funcionario.setText(QCoreApplication.translate("Dialog", u"Consultar", None))
        self.lbl_nome_funcionario_emprestimo.setText(QCoreApplication.translate("Dialog", u"Nome do funcionario", None))
        self.lbl_tipo_uniforme.setText(QCoreApplication.translate("Dialog", u"Tipo de uniforme", None))
        self.btn_confirmar_emprestimo.setText(QCoreApplication.translate("Dialog", u"Confirma", None))
    # retranslateUi

