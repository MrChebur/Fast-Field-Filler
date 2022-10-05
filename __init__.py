# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FastFieldFiller
                                 A QGIS plugin
 The plugin was created to quickly fill in the fields in the attribute table.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-30
        copyright            : (C) 2022 by MrChebur
        email                : hidden
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FastFieldFiller class from file FastFieldFiller.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .fast_field_filler import FastFieldFiller
    return FastFieldFiller(iface)
