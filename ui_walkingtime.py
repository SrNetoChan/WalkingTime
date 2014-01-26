# -*- coding: utf-8 -*-

"""
Module implementing WtPluginDialog.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from Ui_ui_walkingtime import Ui_WalkingTime
from math import *

class WtPluginDialog(QDialog, Ui_WalkingTime):
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
        self.legend=self.iface.legendInterface()
        self.loaded_layers = self.legend.layers()
        
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
        self.vector_line_layers = {}
        self.raster_layers = {}
        for i in range(len(self.loaded_layers)):
            layer = self.loaded_layers[i]
            fields_names = []
            # Select line vector layers
            if (layer.type() == layer.VectorLayer) and (layer.geometryType() == QGis.Line):
                layer_info = [layer]
                provider = layer.dataProvider()
                fields = provider.fields()
                for j in range(len(fields)):
                    fields_names.append(fields[j].name())
                layer_info += [fields_names]
                self.vector_line_layers[unicode(layer.name())] = layer_info
            elif layer.type() == layer.RasterLayer:
                self.raster_layers[unicode(layer.name())] = layer
            else:
                pass
        vector_line_layers = list(self.vector_line_layers)
        raster_layers =list(self.raster_layers)
        return vector_line_layers,  raster_layers
    
    def update_fields(self):
        self.comboBox_time_field.clear()
        self.comboBox_rev_time_field.clear()
        line_layer_fields = self.vector_line_layers[self.comboBox_line_layer.currentText()][1]
        self.comboBox_time_field.addItems(line_layer_fields)
        self.comboBox_rev_time_field.addItems(line_layer_fields)
    
    def test(self):
        self.iface.messageBar().pushMessage("Walkingtime Plugin","message",0,10)
    
    def run(self):
         # use layers according to dialog comboboxes
        line_vlayer = self.vector_line_layers[self.comboBox_line_layer.currentText()][0]
        elevation_rlayer = self.raster_layers[self.comboBox_elevation_layer.currentText()]
    
        # use fields according to dialog comboboxes
        # FIX ME - implement the new fields option
        time_field_idx = self.comboBox_time_field.currentIndex()
        invers_time_field_idx = self.comboBox_rev_time_field.currentIndex()
        
        # Future development add ascend and descend accumulations and "vertical" distance calculation
        #distance_idx = line_vlayer.pendingFields().indexFromName('dist')
        #ascend_idx = line_vlayer.pendingFields().indexFromName('sub_acum')
        #descend_idx = line_vlayer.pendingFields().indexFromName('desc_acum')
        
        
        # See if "use selected features only" box is checked and if there are selected features in line layer
        if self.checkBox_selected_features_only.isChecked() and line_vlayer.selectedFeatureCount () > 0 :
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
            attributes[time_field_idx], attributes[invers_time_field_idx] = self.timeCalc(geom, elevation_rlayer)
            feature.setAttributes(attributes)
            line_vlayer.updateFeature(feature)
     
    # Function to calculate the time and reverse time for a geometry feature 
    def timeCalc(self, geom, rlayer):
        # get base velocity from GUI
        base_velocity = self.doubleSpinBox_base_velocity.value()
        
        # Calculate sampling interval from raster cell mean size
        interval = self.rasterMeanPixelSize(rlayer)
        
        # Set values to initial state
        distance = 0
        time = 0
        inverse_time = 0
        ascend = 0
        descend = 0
        while distance <= geom.length():
            point = geom.interpolate(distance).asPoint()
            point_to_raster = rlayer.dataProvider().identify(point, QgsRaster.IdentifyFormatValue)
            elevation = point_to_raster.results()[1]
            if distance > 0:
                dh = elevation - last_elevation
                if dh > 0:
                    ascend += dh
                else:
                    descend += dh
                time += interval / self.tobblerHikingFunction(base_velocity, interval,dh) * 60 / 1000
                inverse_time += interval / self.tobblerHikingFunction(base_velocity, interval,-dh) * 60 / 1000
            #print time
            
            last_elevation = elevation
            distance += interval
                    
        #MUST FIX - Add last portion of the line
        return time, inverse_time # Later  ascend,  descend

    # Adaptation of Tobblers Hiking function allowing use different base velocity
    def tobblerHikingFunction (self, base_vel, dx,dh):
        # - base_vel is the expected velocity in flat terrain (km/h)
        # - dx is the distance between the points
        # - dh is the elevation diference in the same unit as the distance
        
        # calculates top velocity achived on gentle slope for flat terrain velocity used  
        # The original formula top velocity was 6.0
        top_velocity = base_vel / exp(-0.175) # -3.5*0.05
        
        # calculate segment estimated velocity (km\h)
        velocity = top_velocity * exp(-3.5 * abs(dh/dx + 0.05))
        
        return velocity
    
    def rasterMeanPixelSize(self, raster):
        r = raster
        mean = (raster.rasterUnitsPerPixelX() + raster.rasterUnitsPerPixelY()) / 2.0
        return mean
