# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexandre.neto\Dropbox\Trabalho\Plugins QGIS\WalkingTime\ui_walkingtime.ui'
#
# Created: Wed Nov 20 16:58:01 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WalkingTime(object):
    def setupUi(self, WalkingTime):
        WalkingTime.setObjectName(_fromUtf8("WalkingTime"))
        WalkingTime.resize(290, 396)
        self.widget = QtGui.QWidget(WalkingTime)
        self.widget.setGeometry(QtCore.QRect(10, 12, 271, 375))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(self.widget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout_3.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_2.addWidget(self.radioButton_2, 3, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setEnabled(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.gridLayout_2.addWidget(self.comboBox_4, 2, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 5, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 4, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_4.addWidget(self.pushButton, 3, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_4.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(WalkingTime)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), WalkingTime.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), WalkingTime.reject)
        QtCore.QMetaObject.connectSlotsByName(WalkingTime)

    def retranslateUi(self, WalkingTime):
        WalkingTime.setWindowTitle(_translate("WalkingTime", "WalkingTime", None))
        self.groupBox.setTitle(_translate("WalkingTime", "Inputs", None))
        self.label.setText(_translate("WalkingTime", "Line Layer", None))
        self.label_2.setText(_translate("WalkingTime", "Elevation raster", None))
        self.checkBox_2.setText(_translate("WalkingTime", "Use only selected features", None))
        self.groupBox_3.setTitle(_translate("WalkingTime", "Parameters", None))
        self.label_5.setText(_translate("WalkingTime", "Plain velocity (km\\ h)", None))
        self.groupBox_2.setTitle(_translate("WalkingTime", "Output", None))
        self.radioButton.setText(_translate("WalkingTime", "Update fields", None))
        self.label_3.setText(_translate("WalkingTime", "Time", None))
        self.label_4.setText(_translate("WalkingTime", "Reverse time", None))
        self.radioButton_2.setText(_translate("WalkingTime", "Create new fields", None))
        self.label_6.setText(_translate("WalkingTime", "Time", None))
        self.label_7.setText(_translate("WalkingTime", "Reverse time", None))
        self.pushButton.setText(_translate("WalkingTime", "Help", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WalkingTime = QtGui.QDialog()
    ui = Ui_WalkingTime()
    ui.setupUi(WalkingTime)
    WalkingTime.show()
    sys.exit(app.exec_())

