# -*- coding: utf-8 -*-
"""
Green Area Calculator - QGIS Plugin
Calculates green vegetation areas per census sector
Author: Indiara Elis
License: GPLv2 or later
"""


def classFactory(iface):
    """Main plugin entry point required by QGIS.
    
    Args:
        iface: QGIS interface object
        
    Returns:
        GreenAreaCalculatorPlugin: Plugin instance
    """
    from .main_plugin import GreenAreaCalculatorPlugin
    return GreenAreaCalculatorPlugin(iface)