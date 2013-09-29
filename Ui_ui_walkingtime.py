# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Dropbox/Trabalho/QGIS/Plugins-QGIS/WalkingTime/ui_walkingtime.ui'
#
# Created: Sun Sep 29 23:27:21 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WalkingTime(object):
    def setupUi(self, WalkingTime):
        WalkingTime.setObjectName(_fromUtf8("WalkingTime"))
        WalkingTime.resize(389, 286)
        self.buttonBox = QtGui.QDialogButtonBox(WalkingTime)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.comboBox = QtGui.QComboBox(WalkingTime)
        self.comboBox.setGeometry(QtCore.QRect(207, 20, 161, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(WalkingTime)
        self.comboBox_2.setGeometry(QtCore.QRect(207, 60, 161, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label = QtGui.QLabel(WalkingTime)
        self.label.setGeometry(QtCore.QRect(20, 30, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(WalkingTime)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 111, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(WalkingTime)
        self.checkBox.setGeometry(QtCore.QRect(20, 100, 151, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.comboBox_3 = QtGui.QComboBox(WalkingTime)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 160, 171, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_4 = QtGui.QComboBox(WalkingTime)
        self.comboBox_4.setGeometry(QtCore.QRect(200, 160, 171, 27))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.lineEdit = QtGui.QLineEdit(WalkingTime)
        self.lineEdit.setGeometry(QtCore.QRect(20, 200, 171, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(WalkingTime)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 200, 171, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.checkBox_2 = QtGui.QCheckBox(WalkingTime)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 130, 291, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.retranslateUi(WalkingTime)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), WalkingTime.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), WalkingTime.reject)
        QtCore.QMetaObject.connectSlotsByName(WalkingTime)

    def retranslateUi(self, WalkingTime):
        WalkingTime.setWindowTitle(QtGui.QApplication.translate("WalkingTime", "WalkingTime", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WalkingTime", "Line Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WalkingTime", "Elevation raster", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("WalkingTime", "Use existing fileds", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("WalkingTime", "Use only selected features", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WalkingTime = QtGui.QDialog()
    ui = Ui_WalkingTime()
    ui.setupUi(WalkingTime)
    WalkingTime.show()
    sys.exit(app.exec_())

