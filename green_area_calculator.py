# -*- coding: utf-8 -*-
"""
Green Area Calculator Dialog
Main calculation logic and user interface for vegetation analysis
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

from .ui_green_area_calculator_dialog import Ui_GreenAreaCalculatorDialog


class GreenAreaCalculatorDialog(QtWidgets.QDialog, Ui_GreenAreaCalculatorDialog):
    """Dialog principal do plugin."""
    
    def __init__(self, iface, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.setWindowTitle("Green Area Calculator")
        
        self._setup_connections()
        self._load_layers()
        
        # Initialize logging
        QgsMessageLog.logMessage("Dialog initialized", "GreenAreaCalculator", Qgis.Info)

    def _setup_connections(self):
        """Connect UI signals and setup interface elements."""
        self.comboCensusLayer.currentIndexChanged.connect(self._on_layer_change)
        self.comboVegetationLayer.currentIndexChanged.connect(self._on_layer_change)
        self.buttonCalculate.clicked.connect(self.run_calculation)
        
        # Hide progress bar initially
        self.progressBar.setVisible(False)
        
        # Set placeholder texts
        self.comboCensusLayer.setPlaceholderText("Select census layer")
        self.comboVegetationLayer.setPlaceholderText("Select vegetation layer")

    def _load_layers(self):
        """Load available layers into combo boxes."""
        project = QgsProject.instance()
        layers = project.mapLayers().values()
        
        # Separate vector and raster layers
        vectors = [l for l in layers if isinstance(l, QgsVectorLayer)]
        rasters = [l for l in layers if isinstance(l, QgsRasterLayer)]
        
        self._populate_combo(self.comboCensusLayer, vectors, "No vector layers available")
        self._populate_combo(self.comboVegetationLayer, rasters + vectors, "No layers available")
        
        self._update_button_state()

    def _populate_combo(self, combo, layers, empty_msg):
        """Populate combo box with available layers."""
        combo.clear()
        combo.addItem("")  # Empty selection
        
        if not layers:
            combo.setPlaceholderText(empty_msg)
            return
            
        for layer in layers:
            combo.addItem(layer.name(), layer)

    def _update_button_state(self):
        """Update button state based on layer selection."""
        census_ok = self.comboCensusLayer.currentText() != ""
        veg_ok = self.comboVegetationLayer.currentText() != ""
        
        self.buttonCalculate.setEnabled(census_ok and veg_ok)
        
        # Simple visual feedback
        if census_ok:
            self.labelCensus.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.labelCensus.setStyleSheet("color: #666;")
            
        if veg_ok:
            self.labelVegetation.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.labelVegetation.setStyleSheet("color: #666;")

    def _on_layer_change(self):
        """Handle layer selection changes."""
        self._update_button_state()

    def run_calculation(self):
        """Execute the main calculation process."""
        try:
            # Show progress indicator
            self.progressBar.setVisible(True)
            self.progressBar.setRange(0, 0)  # Indeterminate progress
            self.buttonCalculate.setEnabled(False)
            QtWidgets.QApplication.processEvents()
            
            census_layer = self._get_selected_layer(self.comboCensusLayer)
            veg_layer = self._get_selected_layer(self.comboVegetationLayer)
            
            if not census_layer or not veg_layer:
                raise ValueError("Please select both layers before calculating")
            
            # Perform the actual calculation
            result = self._do_calculation(census_layer, veg_layer)
            
            self.iface.messageBar().pushMessage(
                "Success", 
                "Green area calculation completed successfully", 
                level=Qgis.Success, 
                duration=3
            )
            
            return result
            
        except Exception as e:
            error_msg = f"Calculation error: {str(e)}"
            self.iface.messageBar().pushMessage(
                "Error", error_msg, level=Qgis.Critical, duration=5
            )
            QgsMessageLog.logMessage(error_msg, "GreenAreaCalculator", Qgis.Critical)
            return None
            
        finally:
            # UI cleanup
            self.progressBar.setVisible(False)
            self.buttonCalculate.setEnabled(True)

    def _get_selected_layer(self, combo):
        """Get the selected layer from combo box."""
        if combo.currentIndex() > 0:
            return combo.currentData()
        return None

    def _do_calculation(self, census_layer, veg_layer):
        """Perform the actual green area calculation logic here."""
        # TODO: Implement your NDVI/vegetation analysis logic
        
        QgsMessageLog.logMessage(
            f"Calculating green areas for {census_layer.name()} using {veg_layer.name()}", 
            "GreenAreaCalculator", 
            Qgis.Info
        )
        
        # Placeholder for actual calculation
        return {
            "status": "success",
            "message": "Calculation completed",
            "data": {}
        }

    def closeEvent(self, event):
        """Handle dialog close event."""
        QgsMessageLog.logMessage("Dialog closed", "GreenAreaCalculator", Qgis.Info)
        event.accept()