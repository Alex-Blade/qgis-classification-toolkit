# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(451, 362)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.predict = QtWidgets.QWidget()
        self.predict.setObjectName("predict")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.predict)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolBox = QtWidgets.QToolBox(self.predict)
        self.toolBox.setObjectName("toolBox")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 411, 68))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 411, 68))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.toolBox.addItem(self.page_4, "")
        self.verticalLayout_4.addWidget(self.toolBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.predict)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.predict)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.tabWidget.addTab(self.predict, "")
        self.config = QtWidgets.QWidget()
        self.config.setObjectName("config")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.config)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.config)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 409, 272))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.add_to_pipe = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_to_pipe.sizePolicy().hasHeightForWidth())
        self.add_to_pipe.setSizePolicy(sizePolicy)
        self.add_to_pipe.setIconSize(QtCore.QSize(16, 16))
        self.add_to_pipe.setFlat(False)
        self.add_to_pipe.setObjectName("add_to_pipe")
        self.horizontalLayout_2.addWidget(self.add_to_pipe)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pipe_el_title = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pipe_el_title.setObjectName("pipe_el_title")
        self.verticalLayout_2.addWidget(self.pipe_el_title)
        self.pipe_el_layout = QtWidgets.QHBoxLayout()
        self.pipe_el_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.pipe_el_layout.setObjectName("pipe_el_layout")
        self.pipe_element = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.pipe_element.setObjectName("pipe_element")
        self.pipe_el_layout.addWidget(self.pipe_element)
        self.remove = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy)
        self.remove.setObjectName("remove")
        self.pipe_el_layout.addWidget(self.remove)
        self.verticalLayout_2.addLayout(self.pipe_el_layout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.config, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "DockWidget"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("DockWidget", "Model #1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("DockWidget", "Model #2"))
        self.label_3.setText(_translate("DockWidget", "There will be something"))
        self.pushButton.setText(_translate("DockWidget", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.predict), _translate("DockWidget", "Classify"))
        self.add_to_pipe.setText(_translate("DockWidget", "+"))
        self.pipe_el_title.setText(_translate("DockWidget", "Some Label"))
        self.remove.setText(_translate("DockWidget", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config), _translate("DockWidget", "Configuration"))
