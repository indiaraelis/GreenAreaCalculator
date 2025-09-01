# -*- coding: utf-8 -*-
"""
Green Area Calculator Dialog
Main calculation logic and user interface
Author: Indiara Elis
License: GPLv2 or later
"""

import os
import sys
from qgis.PyQt import QtWidgets, QtCore
from qgis.PyQt.QtCore import Qt, QObject
from qgis.core import (
    QgsProject, QgsMessageLog, Qgis, QgsVectorLayer, 
    QgsRasterLayer, QgsNetworkAccessManager
)
from qgis.gui import QgsMessageBar

# Import UI class
from .ui_green_area_calculator_dialog import Ui_GreenAreaCalculatorDialog


class GreenAreaCalculatorDialog(QtWidgets.QDialog, Ui_GreenAreaCalculatorDialog):
    """Main dialog for Green Area Calculator plugin."""
    
    def __init__(self, iface, parent=None):
        """Initialize dialog with QGIS interface.
        
        Args:
            iface: QGIS interface object
            parent: Parent widget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.setWindowTitle("Green Area Calculator")
        
        # Set up UI enhancements
        self.setup_ui_enhancements()
        
        # Check available layers on startup
        self.check_available_layers()
        
        QgsMessageLog.logMessage(
            "Green Area Calculator dialog initialized", 
            "GreenAreaCalculator", 
            Qgis.Info
        )

    def setup_ui_enhancements(self):
        """Set up UI enhancements and signal connections."""
        # Connect signals
        self.comboCensusLayer.currentIndexChanged.connect(self.on_layer_selected)
        self.comboVegetationLayer.currentIndexChanged.connect(self.on_layer_selected)
        self.buttonCalculate.clicked.connect(self.calculate_areas)
        
        # Set up progress bar
        self.progressBar.setVisible(False)
        
        # Set placeholder texts
        self.comboCensusLayer.setPlaceholderText("Select census sector layer")
        self.comboVegetationLayer.setPlaceholderText("Select vegetation layer")

    def check_available_layers(self):
        """Check and update available layers in comboboxes."""
        try:
            layers = QgsProject.instance().mapLayers().values()
            
            # Filter layers by type
            vector_layers = [
                layer for layer in layers 
                if isinstance(layer, QgsVectorLayer)
            ]
            raster_layers = [
                layer for layer in layers 
                if isinstance(layer, QgsRasterLayer)
            ]
            
            # Update comboboxes
            self.update_layer_combobox(
                self.comboCensusLayer, 
                vector_layers, 
                "Select census layer"
            )
            self.update_layer_combobox(
                self.comboVegetationLayer, 
                raster_layers + vector_layers, 
                "Select vegetation layer"
            )
            
            # Update status indicators
            self.update_status_indicator()
            
        except Exception as e:
            QgsMessageLog.logMessage(
                f"Error checking available layers: {str(e)}", 
                "GreenAreaCalculator", 
                Qgis.Warning
            )

    def update_layer_combobox(self, combobox, layers, placeholder):
        """Update layer combobox with available layers.
        
        Args:
            combobox: QComboBox to update
            layers: List of QGIS layers
            placeholder: Placeholder text when no layers available
        """
        combobox.clear()
        combobox.addItem("")  # Empty selection
        
        for layer in layers:
            combobox.addItem(layer.name(), layer)
            
        if combobox.count() == 1:  # Only empty item
            combobox.setPlaceholderText(f"No layers available - {placeholder}")
        else:
            combobox.setPlaceholderText(placeholder)

    def update_status_indicator(self):
        """Update visual status indicators based on layer selection."""
        census_selected = self.comboCensusLayer.currentText() != ""
        vegetation_selected = self.comboVegetationLayer.currentText() != ""
        
        # Update button state
        self.buttonCalculate.setEnabled(census_selected and vegetation_selected)
        
        # Visual feedback
        census_style = "color: green; font-weight: bold;" if census_selected else "color: red;"
        vegetation_style = "color: green; font-weight: bold;" if vegetation_selected else "color: red;"
        
        self.labelCensus.setStyleSheet(census_style)
        self.labelVegetation.setStyleSheet(vegetation_style)

    def on_layer_selected(self):
        """Handle layer selection change."""
        self.update_status_indicator()

    def calculate_areas(self):
        """Main calculation method with proper error handling."""
        try:
            # Show progress indicator
            self.progressBar.setVisible(True)
            self.progressBar.setRange(0, 0)  # Indeterminate progress
            self.buttonCalculate.setEnabled(False)
            QtWidgets.QApplication.processEvents()
            
            # Get selected layers
            census_layer = self.get_selected_layer(self.comboCensusLayer)
            vegetation_layer = self.get_selected_layer(self.comboVegetationLayer)
            
            if not census_layer or not vegetation_layer:
                raise ValueError("Please select both census and vegetation layers")
            
            # Perform calculation (implement your logic here)
            result = self.perform_calculation(census_layer, vegetation_layer)
            
            # Show success message
            self.iface.messageBar().pushMessage(
                "Success", 
                "Green area calculation completed", 
                level=Qgis.Success, 
                duration=3
            )
            
            return result
            
        except Exception as e:
            # Handle errors gracefully
            error_msg = f"Calculation error: {str(e)}"
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
            return None
            
        finally:
            # Clean up UI
            self.progressBar.setVisible(False)
            self.buttonCalculate.setEnabled(True)

    def get_selected_layer(self, combobox):
        """Get selected layer from combobox.
        
        Args:
            combobox: QComboBox containing layers
            
        Returns:
            QgsMapLayer or None: Selected layer or None if not available
        """
        if combobox.currentIndex() > 0:  # Not the empty item
            return combobox.currentData()
        return None

    def perform_calculation(self, census_layer, vegetation_layer):
        """Perform the actual green area calculation.
        
        Args:
            census_layer: QgsVectorLayer with census sectors
            vegetation_layer: QgsRasterLayer with vegetation data
            
        Returns:
            dict: Calculation results
        """
        # Implement your calculation logic here
        # This is where your NDVI/vegetation analysis goes
        
        QgsMessageLog.logMessage(
            f"Calculating green areas for {census_layer.name()} "
            f"using {vegetation_layer.name()}", 
            "GreenAreaCalculator", 
            Qgis.Info
        )
        
        # Placeholder - replace with actual calculation
        return {
            "status": "success",
            "message": "Calculation completed",
            "data": {}  # Your result data here
        }

    def closeEvent(self, event):
        """Handle dialog close event.
        
        Args:
            event: Close event
        """
        QgsMessageLog.logMessage(
            "Green Area Calculator dialog closed", 
            "GreenAreaCalculator", 
            Qgis.Info
        )
        event.accept()