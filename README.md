************************
Walking Time QGIS Plugin
************************

The Walking time is a QGIS python plugin that uses Tobbler’s hiking function to estimate the travel time along a line depending on the slope.

The input data required are a vector layer with lines and a raster layer with elevation values. One can adjust the base velocity (on flat terrain) according to the type of walking or walker. By default, the value used is 5 km \ h . The plugin update or create fields with estimated time in minutes in forward and in reverse direction. One can run the plugin for all elements of the vector layer, or only on selected routes.

The plugin can also been used to prepare a network (graph) to perform network analysis when the use of travel walking time as cost is intended.
