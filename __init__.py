# -*- coding: utf-8 -*-
"""
Green Area Calculator - QGIS Plugin
=================================

A QGIS plugin that calculates the proportion of green vegetation areas 
within census sectors of a city. This tool helps urban planners and 
researchers analyze the distribution of green spaces across different
urban regions.

Features:
- Calculate green area percentage per census sector
- Generate summary statistics
- Export results to various formats

Author: Indiara Elis
Email: your.email@domain.com
Repository: https://github.com/username/GreenAreaCalculator
License: GNU General Public License v2 or later
Version: 1.0.0
"""


def classFactory(iface):
    """
    Initialize the Green Area Calculator plugin.
    
    This is the main entry point required by QGIS to load the plugin.
    The function name 'classFactory' is mandatory.
    
    Args:
        iface: A QGIS interface instance that will be passed to the plugin class.
              This provides access to QGIS GUI elements.
        
    Returns:
        GreenAreaCalculatorPlugin: An instance of the main plugin class.
    """
    from .main_plugin import GreenAreaCalculatorPlugin
    return GreenAreaCalculatorPlugin(iface)