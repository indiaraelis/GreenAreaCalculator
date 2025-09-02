# -*- coding: utf-8 -*-
"""
Main plugin class for Green Area Calculator
Cross-platform QGIS plugin for vegetation analysis
"""

import os
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsMessageLog, Qgis, QgsApplication
from qgis.gui import QgsMessageBar

from .green_area_calculator import GreenAreaCalculatorDialog


class GreenAreaCalculatorPlugin:
    """Main plugin class for QGIS integration."""
    
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.dialog = None
        self.action = None
        
        QgsMessageLog.logMessage("Plugin initialized", "GreenAreaCalculator", Qgis.Info)

    def initGui(self):
        """Initialize the plugin GUI elements."""
        icon_path = os.path.join(self.plugin_dir, "icon.png")
        
        # Use default icon if custom icon not found
        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
        else:
            icon = QgsApplication.getThemeIcon("/mActionShowPythonDialog.svg")
            QgsMessageLog.logMessage("Using default icon", "GreenAreaCalculator", Qgis.Info)
        
        self.action = QAction(icon, "Green Area Calculator", self.iface.mainWindow())
        self.action.setObjectName("greenAreaCalculatorAction")
        self.action.triggered.connect(self.run)
        self.action.setWhatsThis("Calculate green areas per census sector")
        self.action.setToolTip("Green Area Calculator")
        
        # Add to Vector menu as it's spatial analysis
        self.iface.addPluginToVectorMenu("&Green Area Calculator", self.action)
        self.iface.addToolBarIcon(self.action)
        
        QgsMessageLog.logMessage("GUI initialized", "GreenAreaCalculator", Qgis.Info)

    def unload(self):
        """Clean up when plugin is unloaded."""
        self.iface.removePluginVectorMenu("&Green Area Calculator", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        # Close dialog if open
        if self.dialog and self.dialog.isVisible():
            self.dialog.close()
            self.dialog = None
            
        QgsMessageLog.logMessage("Plugin unloaded", "GreenAreaCalculator", Qgis.Info)

    def run(self):
        """Execute the plugin - show main dialog."""
        try:
            if not self.dialog:
                self.dialog = GreenAreaCalculatorDialog(self.iface)
            
            self.dialog.show()
            self.dialog.raise_()
            self.dialog.activateWindow()
            
            QgsMessageLog.logMessage("Dialog displayed", "GreenAreaCalculator", Qgis.Info)
            
        except Exception as e:
            error_msg = f"Error opening plugin: {str(e)}"
            self.iface.messageBar().pushMessage(
                "Error", error_msg, level=Qgis.Critical, duration=5
            )
            QgsMessageLog.logMessage(error_msg, "GreenAreaCalculator", Qgis.Critical)