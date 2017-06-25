#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
import logging
from PyQt4 import QtCore
from PyQt4 import QtGui
import ui_main
from diagram import *
from fill_operators import *


__author__ = "M.A. Peinado"
__copyright__ = "2017, M.A. Peinado"
__credits__ = ["Miguel A. Peinado"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "M.A. Peinado"
__email__ = "miguel.peinado@sespa.es"
__status__ = "Beta testing"


class Main(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    """ Load GUI and manages user interaction as:
        - loading images
        - Mouse operation
    """
    # todo: icon and operability of show info action
    # todo: action for help (documentation)

    def __init__(self, parent=None):
        # Invoke parent's method
        super(Main, self).__init__(parent)
        #
        # <------------------------ Gui setup ----------------------->
        #
        self.setupUi(self)
        # Additional GUI tweaks
        if not fill_skimage(self.tool_skimage):
            return
        #
        # if not fill_opencv(self.tool_opencv):
        #     QtGui.QErrorMessage
        #     return
        # Add view(s)

        w = QtGui.QWidget()
        c = Canvas()

        l = QtGui.QHBoxLayout()
        self.tab_canvas.removeTab(0)
        self.tab_canvas.addTab(c, "new")
        l.addWidget(self.tab_canvas)
        w.setLayout(l)
        self.setCentralWidget(w)
        #
        # <------------------------------ Signals ----------------------------->
        #
        self.act_new.triggered.connect(self.add_tab)
        # self.act_load.triggered.connect(self.load_image)
        # self.act_clear.triggered.connect(self.view.show_info)

        #
        # <----------------------------- Attributes --------------------------->
        #
        self._current_dir = os.getcwd()
        #
        # Create logging...
        #
        from os.path import expanduser
        home = expanduser("~")
        logging.basicConfig(format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                            datefmt='%m-%d %H:%M', filename=home + '/grip.log',
                            filemode='w', level=logging.INFO)
        logging.info('Grip started')
        self.show_message("Log file created in " + home)
        # ...and install exception handler
        # sys.excepthook = self.exception_handler

#
# <------------------------------ Slots and events----------------------------->
#
    def add_tab(self):
        pass

    def show_message(self, txt):
        """Show message in status bar"""
        self.statusbar.showMessage(txt)

# Autolauncher
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = Main()
    c.show()
    app.exec_()