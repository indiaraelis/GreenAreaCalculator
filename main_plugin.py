# -*- coding: utf-8 -*-
"""
Main plugin class for Green Area Calculator
Author: Indiara Elis
License: GPLv2 or later
"""

import os
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsMessageLog, Qgis, QgsApplication
from qgis.gui import QgsMessageBar

# Import local modules
from .green_area_calculator import GreenAreaCalculatorDialog


class GreenAreaCalculatorPlugin:
    """Main plugin class that integrates with QGIS."""
    
    def __init__(self, iface):
        """Initialize plugin with QGIS interface.
        
        Args:
            iface: QGIS interface object provided by QGIS
        """
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.dialog = None
        self.action = None
        
        # Initialize message logging
        QgsMessageLog.logMessage(
            "Green Area Calculator plugin initialized", 
            "GreenAreaCalculator", 
            Qgis.Info
        )

    def initGui(self):
        """Initialize the plugin GUI and add it to QGIS menus."""
        # Set up icon path - use QGIS icon if custom icon not available
        icon_path = os.path.join(self.plugin_dir, "icon.png")
        if not os.path.exists(icon_path):
            icon = QgsApplication.getThemeIcon("/mActionShowPythonDialog.svg")
            QgsMessageLog.logMessage(
                "Using QGIS default icon", 
                "GreenAreaCalculator", 
                Qgis.Info
            )
        else:
            icon = QIcon(icon_path)
        
        # Create action with icon and text
        self.action = QAction(
            icon, 
            "Green Area Calculator", 
            self.iface.mainWindow()
        )
        self.action.setObjectName("greenAreaCalculatorAction")
        self.action.triggered.connect(self.run)
        self.action.setWhatsThis("Calculate green areas per census sector")
        self.action.setToolTip("Green Area Calculator: Calculate vegetation coverage per census sector")
        
        # Add to Vector menu as appropriate for spatial analysis tools
        self.iface.addPluginToVectorMenu("&Green Area Calculator", self.action)
        self.iface.addToolBarIcon(self.action)
        
        QgsMessageLog.logMessage(
            "Green Area Calculator GUI initialized", 
            "GreenAreaCalculator", 
            Qgis.Info
        )

    def unload(self):
        """Cleanup when plugin is unloaded from QGIS."""
        # Remove from menu and toolbar
        self.iface.removePluginVectorMenu("&Green Area Calculator", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        # Close dialog if open
        if self.dialog and self.dialog.isVisible():
            self.dialog.close()
            self.dialog = None
            
        QgsMessageLog.logMessage(
            "Green Area Calculator plugin unloaded", 
            "GreenAreaCalculator", 
            Qgis.Info
        )

    def run(self):
        """Run the plugin - show the main dialog."""
        try:
            # Create dialog if it doesn't exist
            if not self.dialog:
                self.dialog = GreenAreaCalculatorDialog(self.iface)
            
            # Show and activate dialog
            self.dialog.show()
            self.dialog.raise_()
            self.dialog.activateWindow()
            
            QgsMessageLog.logMessage(
                "Green Area Calculator dialog shown", 
                "GreenAreaCalculator", 
                Qgis.Info
            )
            
        except Exception as e:
            # Handle errors gracefully with user-friendly messages
            error_msg = f"Error starting Green Area Calculator: {str(e)}"
            self.iface.messageBar().pushMessage(
                "Error", 
                error_msg, 
                level=Qgis.Critical, 
                duration=5
            )
            QgsMessageLog.logMessage(
                error_msg, 
                "GreenAreaCalculator", 
                Qgis.Critical
            )