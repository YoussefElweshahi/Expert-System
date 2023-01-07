from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(714, 573)
        self.concept_list = QtWidgets.QListWidget(Dialog)
        self.concept_list.setGeometry(QtCore.QRect(10, 30, 161, 201))
        self.concept_list.setObjectName("concept_list")
        self.property_list = QtWidgets.QListWidget(Dialog)
        self.property_list.setGeometry(QtCore.QRect(10, 270, 161, 221))
        self.property_list.setObjectName("property_list")
        self.value_list = QtWidgets.QListWidget(Dialog)
        self.value_list.setGeometry(QtCore.QRect(260, 30, 161, 201))
        self.value_list.setObjectName("value_list")
        self.memory_list = QtWidgets.QListWidget(Dialog)
        self.memory_list.setGeometry(QtCore.QRect(240, 310, 251, 221))
        self.memory_list.setObjectName("memory_list")
        self.disease_list = QtWidgets.QListWidget(Dialog)
        self.disease_list.setGeometry(QtCore.QRect(520, 80, 181, 241))
        self.disease_list.setObjectName("disease_list")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 0, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 280, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(560, 50, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.linkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.linkButton.setGeometry(QtCore.QRect(260, 240, 168, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(
                "../../../../../usr/share/icons/oxygen/22x22/actions/insert-horizontal-rule.png"
            ),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.linkButton.setIcon(icon)
        self.linkButton.setObjectName("linkButton")
        self.clearmemory = QtWidgets.QPushButton(Dialog)
        self.clearmemory.setGeometry(QtCore.QRect(240, 523, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setUnderline(True)
        font.setBold(True)
        self.clearmemory.setFont(font)
        self.clearmemory.setMouseTracking(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "../../../../../usr/share/icons/oxygen/16x16/actions/application-exit.png"
            ),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.clearmemory.setIcon(icon1)
        self.clearmemory.setObjectName("clearmemory")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QtWidgets.QApplication.translate("Dialog", "Dialog", None)
        )
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Concept", None))
        self.label_2.setText(
            QtWidgets.QApplication.translate("Dialog", "Property", None)
        )
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Value", None))
        self.label_4.setText(
            QtWidgets.QApplication.translate("Dialog", "Working Memory", None)
        )
        self.label_5.setText(
            QtWidgets.QApplication.translate("Dialog", "Disease", None)
        )
        self.linkButton.setText(
            QtWidgets.QApplication.translate("Dialog", "Add Tuple", None)
        )
        self.clearmemory.setText(
            QtWidgets.QApplication.translate("Dialog", "Clear Memory", None)
        )
