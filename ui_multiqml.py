# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiqml.ui'
#
# Created: Sat Jan 17 16:21:03 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MultiQmlForm(object):
    def setupUi(self, MultiQmlForm):
        MultiQmlForm.setObjectName("MultiQmlForm")
        MultiQmlForm.resize(278, 189)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MultiQmlForm.sizePolicy().hasHeightForWidth())
        MultiQmlForm.setSizePolicy(sizePolicy)
        MultiQmlForm.setSizeGripEnabled(False)
        MultiQmlForm.setModal(False)
        self.gridLayout = QtGui.QGridLayout(MultiQmlForm)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(MultiQmlForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.rbnRasterLayers = QtGui.QRadioButton(MultiQmlForm)
        self.rbnRasterLayers.setCheckable(True)
        self.rbnRasterLayers.setChecked(False)
        self.rbnRasterLayers.setObjectName("rbnRasterLayers")
        self.gridLayout.addWidget(self.rbnRasterLayers, 0, 1, 1, 1)
        self.rbnVectorLayers = QtGui.QRadioButton(MultiQmlForm)
        self.rbnVectorLayers.setObjectName("rbnVectorLayers")
        self.gridLayout.addWidget(self.rbnVectorLayers, 0, 2, 1, 1)
        self.lvMapLayers = QtGui.QListView(MultiQmlForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvMapLayers.sizePolicy().hasHeightForWidth())
        self.lvMapLayers.setSizePolicy(sizePolicy)
        self.lvMapLayers.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lvMapLayers.setObjectName("lvMapLayers")
        self.gridLayout.addWidget(self.lvMapLayers, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbnApplyStyle = QtGui.QPushButton(MultiQmlForm)
        self.pbnApplyStyle.setObjectName("pbnApplyStyle")
        self.verticalLayout.addWidget(self.pbnApplyStyle)
        self.pbnRestoreDefaultStyle = QtGui.QPushButton(MultiQmlForm)
        self.pbnRestoreDefaultStyle.setObjectName("pbnRestoreDefaultStyle")
        self.verticalLayout.addWidget(self.pbnRestoreDefaultStyle)
        self.pbnSelectAllLayers = QtGui.QPushButton(MultiQmlForm)
        self.pbnSelectAllLayers.setObjectName("pbnSelectAllLayers")
        self.verticalLayout.addWidget(self.pbnSelectAllLayers)
        self.pbnClose = QtGui.QPushButton(MultiQmlForm)
        self.pbnClose.setObjectName("pbnClose")
        self.verticalLayout.addWidget(self.pbnClose)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 2)
        self.label.setBuddy(self.lvMapLayers)

        self.retranslateUi(MultiQmlForm)
        QtCore.QMetaObject.connectSlotsByName(MultiQmlForm)
        MultiQmlForm.setTabOrder(self.pbnApplyStyle, self.lvMapLayers)
        MultiQmlForm.setTabOrder(self.lvMapLayers, self.pbnRestoreDefaultStyle)
        MultiQmlForm.setTabOrder(self.pbnRestoreDefaultStyle, self.pbnSelectAllLayers)
        MultiQmlForm.setTabOrder(self.pbnSelectAllLayers, self.rbnRasterLayers)
        MultiQmlForm.setTabOrder(self.rbnRasterLayers, self.rbnVectorLayers)
        MultiQmlForm.setTabOrder(self.rbnVectorLayers, self.pbnClose)

    def retranslateUi(self, MultiQmlForm):
        MultiQmlForm.setWindowTitle(QtGui.QApplication.translate("MultiQmlForm", "Assign style", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MultiQmlForm", "Layers:", None, QtGui.QApplication.UnicodeUTF8))
        self.rbnRasterLayers.setText(QtGui.QApplication.translate("MultiQmlForm", "Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.rbnVectorLayers.setText(QtGui.QApplication.translate("MultiQmlForm", "Vector", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnApplyStyle.setText(QtGui.QApplication.translate("MultiQmlForm", "Apply style ...", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnRestoreDefaultStyle.setText(QtGui.QApplication.translate("MultiQmlForm", "Restore initial style", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnSelectAllLayers.setText(QtGui.QApplication.translate("MultiQmlForm", "Select all layers", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnClose.setText(QtGui.QApplication.translate("MultiQmlForm", "Close", None, QtGui.QApplication.UnicodeUTF8))

