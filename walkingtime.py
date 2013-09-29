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
# from walkingtimedialog import WalkingTimeDialog
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
        # self.dlg = WalkingTimeDialog()

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
        mc = self.iface.mapCanvas()
        loaded_layers = mc.layers()
        # show the dialog
        #self.dlg.show()
        # Run the dialog event loop
        #result = self.dlg.exec_()
        # See if OK was pressed
        #if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
        
#FIX        # Adicionar mecanismo de escolha de layers
        line_vlayer = loaded_layers[1]
        elevation_rlayer = loaded_layers[3]
        
        # adicionar campos tempo_min e distancia caso necessário
        
        #Identify the index number of the fields
        time_field_idx = line_vlayer.pendingFields().indexFromName('tempo')
        distance_idx = line_vlayer.pendingFields().indexFromName('dist')
                
        for feature in line_vlayer.getFeatures():
            geom =  feature.geometry()
            attributes = feature.attributes()
            attributes[distance_idx] = geom.length()
            attributes[time_field_idx] = timeCalc(geom, elevation_rlayer)
            feature.setAttributes(attributes)
            line_vlayer.updateFeature(feature)
    
def timeCalc(geom, rlayer):
    # FIX - read interval from raster layer (size of the cells)
    interval = 4.0
    distance = 0
    time = 0
    while distance <= geom.length():
        point = geom.interpolate(distance).asPoint()
        point_to_raster = rlayer.dataProvider().identify(point, QgsRaster.IdentifyFormatValue)
        elevation = point_to_raster.results()[1]
        if distance > 0:
            dh = last_elevation - elevation
            time += interval / tobblerHikingFunction(interval,dh) * 60 / 1000
        #print time
        last_elevation = elevation
        distance += interval
        
    #MUST FIX
    return time

def tobblerHikingFunction (dx,dh):
    return 5 * exp(-3.5 * abs(dh/dx + 0.05)) 
