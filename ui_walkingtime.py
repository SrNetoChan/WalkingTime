# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Walking Time
                                 A QGIS plugin
 Module implementing WtPluginDialog. The Dialog for Walking time plugin.
                              -------------------
        begin                : 2013-09-27
        copyright          : (C) 2013 by Alexandre Neto / Cascais Ambiente
        email                : alexandre.neto@cascaisambiente.pt
 ***************************************************************************/

****************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************
"""
from __future__ import absolute_import
from builtins import str

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog
from qgis.core import QgsProject
import os


pluginPath = os.path.dirname(__file__)
WIDGET, BASE = uic.loadUiType(
    os.path.join(pluginPath, 'ui_walkingtime.ui'))

class WtPluginDialog(BASE, WIDGET):
    """
    Class documentation goes here.
    """
    def __init__(self, iface):
        """
        Constructor
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        
        self.mc = self.iface.mapCanvas()
        #self.legend = self.iface.legendInterface()
        self.loaded_layers = [layer for layer in QgsProject.instance().mapLayers().values()]
        
        # UI CCONNECTORS
        self.buttonBox_ok_cancel.accepted.connect(self.run)
        self.buttonBox_ok_cancel.rejected.connect(self.close)
        self.comboBox_line_layer.currentIndexChanged.connect(self.update_fields)
        
        # Get line layers and raster layers from legend
        vector_line_layers, raster_layers = self.get_useful_layers()
        
        # Populate comboboxes
        self.comboBox_line_layer.clear()
        self.comboBox_line_layer.addItems(vector_line_layers)
        
        self.comboBox_elevation_layer.clear()
        self.comboBox_elevation_layer.addItems(raster_layers)
        #self.repaint()
   
    def get_useful_layers(self):
        """
        Purpose: iterate the map legend and return a list of line vector layers (with fields)
        and a list of raster layers.
        vector_line_layers is like {Layer1name:[Layer 1,[fileld1, field2, ...]], Layer2Name: [Layer 2,[fileld1, field2, ...]],...}
        
        """
        self.vector_line_layers = {}
        self.raster_layers = {}
        
        for layer in self.loaded_layers:
            fields_names = []

            # select line vector layers
            if (layer.type() == layer.VectorLayer) and (layer.geometryType() == 1):
                layer_info = [layer]
                provider = layer.dataProvider()
                fields = provider.fields()
                # get vector layer fields
                for field in fields:
                    fields_names.append(field.name())
                layer_info += [fields_names]
                self.vector_line_layers[str(layer.name())] = layer_info
            
            # select raster layers
            elif layer.type() == layer.RasterLayer:
                self.raster_layers[str(layer.name())] = layer
            else:
                pass
        
        vector_line_layers = list(self.vector_line_layers)
        raster_layers =list(self.raster_layers)
        
        return vector_line_layers,  raster_layers
    
    def update_fields(self):
        """
        Purpose: refresh list of available fields in update fields
        """
        self.comboBox_time_field.clear()
        self.comboBox_rev_time_field.clear()
        line_layer_fields = self.vector_line_layers[self.comboBox_line_layer.currentText()][1]
        self.comboBox_time_field.addItems(line_layer_fields)
        self.comboBox_rev_time_field.addItems(line_layer_fields)
        
        # auto select time and time_rev fields if they exist
        if 'time' in line_layer_fields:
            index = line_layer_fields.index('time')
            self.comboBox_time_field.setCurrentIndex(index)
        if 'rev_time' in line_layer_fields:
            index = line_layer_fields.index('rev_time')
            self.comboBox_rev_time_field.setCurrentIndex(index)
    
    def run(self):
        pass
        return
