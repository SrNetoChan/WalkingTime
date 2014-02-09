# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Walking Time
                                 A QGIS plugin
 Calculates walking time and other trails values into fields in a  linestring
 vector layer, based on slope derived from an elevation raster
                              -------------------
        begin                : 2013-09-27
        copyright          : (C) 2013 by Alexandre Neto / Cascais Ambiente
        email                : alexandre.neto@cascaisambiente.pt
 ***************************************************************************/

****************************************************************************
 *                                                                                                                   *
 *   This program is free software; you can redistribute it and/or modify      *
 *   it under the terms of the GNU General Public License as published by   *
 *   the Free Software Foundation; either version 2 of the License, or           *
 *   (at your option) any later version.                                                           *
 *                                                                                                                   *
 ***************************************************************************
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
        if not(self.dlg.exec_()):
            # If dialog is closed or cancelled nothing more is done
            return
        else:
            pass

         # use layers according to dialog comboboxes
        self.line_vlayer = self.dlg.vector_line_layers[self.dlg.comboBox_line_layer.currentText()][0]
        self.elevation_rlayer = self.dlg.raster_layers[self.dlg.comboBox_elevation_layer.currentText()]
        line_vlayer = self.line_vlayer
        elevation_rlayer = self.elevation_rlayer
        
        # get sampling interval from average pixel size of the elevation raster
        self.interval = self.rasterMeanPixelSize(elevation_rlayer)
        
        # Verify if user wants to use existing fields or new fields
        if self.dlg.radioButton_update_fields.isChecked():
            time_field_idx = self.dlg.comboBox_time_field.currentIndex()
            invers_time_field_idx = self.dlg.comboBox_rev_time_field.currentIndex()
        else:
            # Create new fields in vector layer
            caps = line_vlayer.dataProvider().capabilities()
            if caps & QgsVectorDataProvider.AddAttributes:
                new_fields = [  QgsField(self.dlg.lineEdit_time_field_name.text(), QVariant.Double, "double", 20,  2), 
                                        QgsField(self.dlg.lineEdit_rev_time_field_name.text(), QVariant.Double, "double",  20,  2)]
                line_vlayer.dataProvider().addAttributes(new_fields)
                line_vlayer.updateFields()
                n_fields = line_vlayer.dataProvider().fields().count()
                time_field_idx = n_fields - 2
                invers_time_field_idx = n_fields - 1
            else:
                print "Upss"
                return
        
        # Future development add ascend and descend accumulations and "vertical" distance calculation
        #distance_idx = line_vlayer.pendingFields().indexFromName('dist')
        #ascend_idx = line_vlayer.pendingFields().indexFromName('sub_acum')
        #descend_idx = line_vlayer.pendingFields().indexFromName('desc_acum')
                
        # See if "use selected features only" box is checked and if there are selected features in line layer
        if self.dlg.checkBox_selected_features_only.isChecked() and line_vlayer.selectedFeatureCount () > 0 :
            features = line_vlayer.selectedFeatures()
        # otherwise use all features in line layer
        else:
            features =line_vlayer.getFeatures()
        
        # Iterate line layer features, calculate and fill all walking time attributes
        for feature in features:
            geom =  feature.geometry()
            attributes = feature.attributes()
            #attributes[distance_idx] = geom.length()
            #attributes[time_field_idx], attributes[invers_time_field_idx], attributes[ascend_idx], attributes[descend_idx] = self.timeCalc(geom, elevation_rlayer)
            attributes[time_field_idx], attributes[invers_time_field_idx] = self.timeCalc(geom)
            feature.setAttributes(attributes)
            line_vlayer.updateFeature(feature)

    # Function to calculate the time and reverse time for a geometry feature 
    def timeCalc(self, geom):
        # get base velocity from GUI
        base_velocity = self.dlg.doubleSpinBox_base_velocity.value()

        # Set values to initial state
        interval = self.interval
        distance = 0
        time = 0
        inverse_time = 0
        ascend = 0
        descend = 0
        
        while distance <= geom.length():
            point = geom.interpolate(distance).asPoint()
            point_to_raster = self.elevation_rlayer.dataProvider().identify(point, QgsRaster.IdentifyFormatValue)
            elevation = point_to_raster.results()[1]
            if distance > 0:
                dh = elevation - last_elevation
                if dh > 0:
                    ascend += dh
                else:
                    descend += dh
                # Calculate estimated velocities using  tobbler function for the segment
                velocity = self.tobblerHikingFunction(base_velocity, interval,dh)
                reverse_velocity = self.tobblerHikingFunction(base_velocity, interval,-dh)
                # Add segment times  in  minutes
                time += interval /  velocity * 60 / 1000
                inverse_time += interval / reverse_velocity * 60 / 1000
            
            last_elevation = elevation
            distance += interval
                    
        #MUST FIX - Add last portion of the line
        return time, inverse_time # Later  ascend,  descend

    # Adaptation of Tobblers Hiking function allowing use different base velocity
    def tobblerHikingFunction (self, base_vel, dx,dh):
        # - base_vel is the expected velocity in flat terrain (km/h)
        # - dx is the distance between the points
        # - dh is the elevation diference in the same units as the distance
        
        # calculates top velocity achived on gentle slope for flat terrain velocity used  
        # The original formula top velocity was 6.0 km/h
        top_velocity = base_vel / exp(-0.175) # -3.5*0.05
        
        # calculate segment estimated velocity (km\h)
        velocity = top_velocity * exp(-3.5 * abs(dh/dx + 0.05))
        
        return velocity
    
    # calculates the average size of the raster pixel
    def rasterMeanPixelSize(self, raster):
        # calculates the average size of the raster pixel
        mean = (raster.rasterUnitsPerPixelX() + raster.rasterUnitsPerPixelY()) / 2.0
        return mean

