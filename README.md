# Walking Time QGIS Plugin

The Walking time is a QGIS python plugin that uses Tobbler’s hiking function to
estimate the travel time along a line taking in account the path slope.

The input data required are a vector layer with lines and a raster layer with
elevation values.

The user can adjust the base velocity (on flat terrain) according
to the type of walking or walker. By default, the value used is 5 km \ h .

The plugin updates or creates fields with estimated time in minutes in forward
and reverse directions. The user can run the plugin for all elements of the
vector layer, or only on selected routes.

The plugin can be used to prepare a network (graph) to perform network
analysis when the use of travel walking time as cost is intended.
