# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WalkingTime
                                 A QGIS plugin
 Adds walking time fields to linestring vector layer, based on slope derived from an elevation raster
                              -------------------
        begin                : 2013-09-27
        copyright            : (C) 2013 by Alexandre Neto / Cascais Ambiente
        email                : alexandre.neto@cascaisambiente.pt
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from math import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from ui_walkingtime import WtPluginDialog
import os.path


class WalkingTime:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'walkingtime_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        # self.dlg = WtPluginDialog(iface)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/walkingtime/icon.png"),
            u"WalkingTime", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Walking time", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Walking time", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        #show the dialog
        # self.dlg.show()
        self.dlg = WtPluginDialog(self.iface)
        # Run the dialog event loop
        result = self.dlg.exec_()

