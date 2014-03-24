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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Walking time"


def description():
    return "Calculate walking travel time from linestring vector layer, based on slope derived from an elevation raster"


def version():
    return "Version 0.1.0"


def icon():
    return "icon.svg"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "Alexandre Neto"

def email():
    return "senhor.neto.gmail.com"

def classFactory(iface):
    # load WalkingTime class from file WalkingTime
    from walkingtime import WalkingTime
    return WalkingTime(iface)
