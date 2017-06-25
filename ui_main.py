# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/Flower-power-green.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tab_canvas = QtGui.QTabWidget(self.centralwidget)
        self.tab_canvas.setGeometry(QtCore.QRect(30, 10, 78, 72))
        self.tab_canvas.setTabShape(QtGui.QTabWidget.Rounded)
        self.tab_canvas.setElideMode(QtCore.Qt.ElideNone)
        self.tab_canvas.setTabsClosable(True)
        self.tab_canvas.setMovable(True)
        self.tab_canvas.setObjectName(_fromUtf8("tab_canvas"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lb_dummy = QtGui.QLabel(self.tab)
        self.lb_dummy.setObjectName(_fromUtf8("lb_dummy"))
        self.verticalLayout_5.addWidget(self.lb_dummy)
        self.tab_canvas.addTab(self.tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar_main = QtGui.QToolBar(MainWindow)
        self.toolbar_main.setMovable(False)
        self.toolbar_main.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolbar_main.setIconSize(QtCore.QSize(36, 36))
        self.toolbar_main.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar_main.setObjectName(_fromUtf8("toolbar_main"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar_main)
        self.dock_operators = QtGui.QDockWidget(MainWindow)
        self.dock_operators.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dock_operators.setObjectName(_fromUtf8("dock_operators"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tab_operators = QtGui.QTabWidget(self.dockWidgetContents)
        self.tab_operators.setObjectName(_fromUtf8("tab_operators"))
        self.tab_custom = QtGui.QWidget()
        self.tab_custom.setObjectName(_fromUtf8("tab_custom"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_custom)
        self.verticalLayout_2.setMargin(5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tool_custom = QtGui.QToolBox(self.tab_custom)
        self.tool_custom.setObjectName(_fromUtf8("tool_custom"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 190, 384))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.tool_custom.addItem(self.page_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tool_custom)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/3rd-party/Icons/Flower-power-green.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_operators.addTab(self.tab_custom, icon1, _fromUtf8(""))
        self.tab_skimage = QtGui.QWidget()
        self.tab_skimage.setObjectName(_fromUtf8("tab_skimage"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_skimage)
        self.verticalLayout_4.setMargin(5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tool_skimage = QtGui.QToolBox(self.tab_skimage)
        self.tool_skimage.setObjectName(_fromUtf8("tool_skimage"))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.tool_skimage.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tool_skimage)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/3rd-party/Icons/skimage_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_operators.addTab(self.tab_skimage, icon2, _fromUtf8(""))
        self.tab_opencv = QtGui.QWidget()
        self.tab_opencv.setObjectName(_fromUtf8("tab_opencv"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_opencv)
        self.verticalLayout_3.setMargin(5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tool_opencv = QtGui.QToolBox(self.tab_opencv)
        self.tool_opencv.setObjectName(_fromUtf8("tool_opencv"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page.setObjectName(_fromUtf8("page"))
        self.tool_opencv.addItem(self.page, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tool_opencv)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/3rd-party/Icons/opencv_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_operators.addTab(self.tab_opencv, icon3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tab_operators)
        self.dock_operators.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_operators)
        self.act_load = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/load.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_load.setIcon(icon4)
        self.act_load.setObjectName(_fromUtf8("act_load"))
        self.act_exit = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/exit.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit.setIcon(icon5)
        self.act_exit.setObjectName(_fromUtf8("act_exit"))
        self.act_play = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/play.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_play.setIcon(icon6)
        self.act_play.setObjectName(_fromUtf8("act_play"))
        self.act_new = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/new.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_new.setIcon(icon7)
        self.act_new.setObjectName(_fromUtf8("act_new"))
        self.act_open = QtGui.QAction(MainWindow)
        self.act_open.setObjectName(_fromUtf8("act_open"))
        self.act_clear = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/clear.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_clear.setIcon(icon8)
        self.act_clear.setObjectName(_fromUtf8("act_clear"))
        self.act_help = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/help.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_help.setIcon(icon9)
        self.act_help.setObjectName(_fromUtf8("act_help"))
        self.act_settings = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/settings.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_settings.setIcon(icon10)
        self.act_settings.setObjectName(_fromUtf8("act_settings"))
        self.act_stop = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/pause.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_stop.setIcon(icon11)
        self.act_stop.setObjectName(_fromUtf8("act_stop"))
        self.act_save = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/save.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_save.setIcon(icon12)
        self.act_save.setObjectName(_fromUtf8("act_save"))
        self.act_copy = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/copy.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_copy.setIcon(icon13)
        self.act_copy.setObjectName(_fromUtf8("act_copy"))
        self.act_paste = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/Main/Icons/paste.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_paste.setIcon(icon14)
        self.act_paste.setObjectName(_fromUtf8("act_paste"))
        self.toolbar_main.addAction(self.act_new)
        self.toolbar_main.addAction(self.act_load)
        self.toolbar_main.addAction(self.act_save)
        self.toolbar_main.addAction(self.act_exit)
        self.toolbar_main.addSeparator()
        self.toolbar_main.addAction(self.act_copy)
        self.toolbar_main.addAction(self.act_paste)
        self.toolbar_main.addAction(self.act_clear)
        self.toolbar_main.addSeparator()
        self.toolbar_main.addAction(self.act_play)
        self.toolbar_main.addAction(self.act_stop)
        self.toolbar_main.addSeparator()
        self.toolbar_main.addAction(self.act_settings)
        self.toolbar_main.addSeparator()
        self.toolbar_main.addAction(self.act_help)

        self.retranslateUi(MainWindow)
        self.tab_canvas.setCurrentIndex(0)
        self.tab_operators.setCurrentIndex(0)
        self.tool_custom.setCurrentIndex(0)
        self.tool_skimage.setCurrentIndex(0)
        self.tool_opencv.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Grip (A Graphic tool for image processing)", None))
        self.lb_dummy.setText(_translate("MainWindow", "TextLabel", None))
        self.tab_canvas.setTabText(self.tab_canvas.indexOf(self.tab), _translate("MainWindow", "erase", None))
        self.toolbar_main.setWindowTitle(_translate("MainWindow", "Main Toolbar", None))
        self.dock_operators.setWindowTitle(_translate("MainWindow", "Operators", None))
        self.tool_custom.setItemText(self.tool_custom.indexOf(self.page_3), _translate("MainWindow", "Page 1", None))
        self.tab_operators.setTabText(self.tab_operators.indexOf(self.tab_custom), _translate("MainWindow", "Custom", None))
        self.tool_skimage.setItemText(self.tool_skimage.indexOf(self.page_2), _translate("MainWindow", "Page 1", None))
        self.tab_operators.setTabText(self.tab_operators.indexOf(self.tab_skimage), _translate("MainWindow", "scikit-image", None))
        self.tool_opencv.setItemText(self.tool_opencv.indexOf(self.page), _translate("MainWindow", "Other", None))
        self.tab_operators.setTabText(self.tab_operators.indexOf(self.tab_opencv), _translate("MainWindow", "OpenCV", None))
        self.act_load.setText(_translate("MainWindow", "Load", None))
        self.act_load.setToolTip(_translate("MainWindow", "Load a processing file", None))
        self.act_exit.setText(_translate("MainWindow", "Exit", None))
        self.act_exit.setToolTip(_translate("MainWindow", "Exit program", None))
        self.act_play.setText(_translate("MainWindow", "Play", None))
        self.act_play.setToolTip(_translate("MainWindow", "Execute pipe", None))
        self.act_new.setText(_translate("MainWindow", "New", None))
        self.act_new.setToolTip(_translate("MainWindow", "New processing", None))
        self.act_open.setText(_translate("MainWindow", "Open", None))
        self.act_open.setToolTip(_translate("MainWindow", "Open a dataset", None))
        self.act_clear.setText(_translate("MainWindow", "Clear", None))
        self.act_clear.setToolTip(_translate("MainWindow", "Clear actual processing", None))
        self.act_help.setText(_translate("MainWindow", "Help", None))
        self.act_settings.setText(_translate("MainWindow", "Settings", None))
        self.act_settings.setToolTip(_translate("MainWindow", "Configure", None))
        self.act_stop.setText(_translate("MainWindow", "Stop", None))
        self.act_save.setText(_translate("MainWindow", "Save", None))
        self.act_save.setToolTip(_translate("MainWindow", "Save the pipeline", None))
        self.act_copy.setText(_translate("MainWindow", "Copy", None))
        self.act_copy.setToolTip(_translate("MainWindow", "Copy selected items", None))
        self.act_paste.setText(_translate("MainWindow", "Paste", None))
        self.act_paste.setToolTip(_translate("MainWindow", "Paste clipboard items", None))

import icons_rc