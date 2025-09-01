# Green Area Calculator - QGIS Plugin

![QGIS Version](https://img.shields.io/badge/QGIS-3.16%2B-green.svg)
![License](https://img.shields.io/badge/License-GPLv2-blue.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-yellow.svg)

A powerful QGIS plugin for calculating green vegetation areas per census sector using advanced NDVI analysis and spatial statistics.

## 🌟 Features

### Core Functionality
- **NDVI-based Analysis**: Calculate vegetation indices from multispectral imagery
- **Sector Statistics**: Automated green area calculation per census sector
- **Cross-Platform**: Compatible with Windows, Linux, and macOS
- **User-Friendly Interface**: Intuitive dialog-based workflow

### Technical Features
- **Multi-format Support**: Works with various raster and vector formats
- **Batch Processing**: Handle multiple sectors efficiently
- **Custom Thresholding**: Adjustable NDVI thresholds for different vegetation types
- **Export Capabilities**: Generate reports and export results to multiple formats

### Visualization
- **Thematic Mapping**: Automatic classification and coloring of results
- **Statistical Charts**: Visual representation of green area distribution
- **Interactive Results**: Click-to-query functionality for detailed sector information

## 📦 Installation

### From QGIS Plugin Repository (Recommended)
1. Open QGIS
2. Go to `Plugins` > `Manage and Install Plugins...`
3. Search for "Green Area Calculator"
4. Click `Install Plugin`
5. Restart QGIS if prompted

### Manual Installation
1. Download the latest release from [GitHub Releases](https://github.com/indiaraelis/GreenAreaCalculator/releases)
2. Extract the ZIP file to your QGIS plugins directory:
   - **Windows**: `C:\Users\%USERNAME%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
3. Restart QGIS
4. Enable the plugin in `Plugins` > `Manage and Install Plugins...`

### Development Installation
```bash
git clone https://github.com/indiaraelis/GreenAreaCalculator.git
cd GreenAreaCalculator
# The plugin will be available after QGIS restart
```

## 🚀 Usage

### Basic Workflow
1. **Prepare Data**:
   - Load census sector polygon layer (Shapefile, GeoPackage, etc.)
   - Load vegetation raster layer (GeoTIFF, IMG, etc.) with infrared band

2. **Open Plugin**:
   - Go to `Vector` > `Green Area Calculator`
   - Or click the toolbar icon 🌿

3. **Configure Parameters**:
   - Select census layer from dropdown
   - Select vegetation raster layer
   - Adjust NDVI thresholds if needed
   - Set output parameters

4. **Execute Analysis**:
   - Click `Calculate` button
   - Monitor progress in the status bar
   - View results in the output panel

5. **Review Results**:
   - New layer with statistics added to QGIS
   - Visualize green area distribution
   - Export results if needed

### Advanced Configuration

#### NDVI Threshold Settings
```python
# Default NDVI thresholds
urban_area = -0.1 to 0.2
sparse_vegetation = 0.2 to 0.4
dense_vegetation = 0.4 to 1.0
```

#### Output Options
- **Statistical Summary**: CSV export with detailed metrics
- **Thematic Maps**: Pre-configured symbology for quick visualization
- **Attribute Table**: Enhanced data table with calculated fields

## 📋 Requirements

### Software Requirements
- **QGIS**: Version 3.16 or higher
- **Python**: 3.7 or higher (included with QGIS)
- **GDAL**: 3.0 or higher (included with QGIS)

### Data Requirements
- **Census Data**: Polygon layer with census sector boundaries
- **Imagery Data**: Multispectral raster with:
  - Red band (typically band 3 or 4)
  - Near-Infrared band (typically band 4 or 5)
- **Coordinate System**: Consistent CRS between all layers

### System Requirements
- **RAM**: Minimum 4GB (8GB recommended for large datasets)
- **Storage**: Sufficient space for temporary files and results
- **Processing**: Multi-core support for faster computation

## 🛠️ Configuration

### Plugin Settings
Access settings through QGIS preferences:
1. Go to `Settings` > `Options` > `Advanced` > `Green Area Calculator`
2. Adjust default parameters:
   - NDVI thresholds
   - Output directory
   - Temporary file handling
   - Memory usage limits

### Customizing Analysis
```python
# Example of custom NDVI thresholds
plugin.set_ndvi_thresholds(
    urban_max=0.2,
    sparse_min=0.2,
    sparse_max=0.4,
    dense_min=0.4
)
```

## 📊 Outputs

### Generated Layers
- **Green Area Statistics**: Polygon layer with calculated metrics
- **NDVI Raster**: Calculated vegetation index layer (optional)
- **Classification Map**: Thematic raster of vegetation density

### Statistical Outputs
- **Percentage of green area** per census sector
- **Total green area** in square meters/kilometers
- **Vegetation density distribution**
- **Comparative statistics** between sectors

### Export Formats
- **GeoJSON**: For web mapping applications
- **CSV**: For statistical analysis in external software
- **PDF**: Printable reports with charts and maps
- **Shapefile**: Compatible with most GIS software

## 🐛 Troubleshooting

### Common Issues

#### "No valid layers found"
- Ensure layers are properly loaded in QGIS
- Check that layers have compatible coordinate systems
- Verify that raster has required bands

#### "NDVI calculation failed"
- Confirm raster has infrared and red bands
- Check for NoData values in input raster
- Verify raster pixel values are valid

#### Performance issues
- Use smaller tile sizes for large datasets
- Increase available memory in plugin settings
- Consider preprocessing large rasters

### Error Messages
| Error Message | Solution |
|---------------|----------|
| "Invalid raster format" | Convert to GeoTIFF or compatible format |
| "Coordinate system mismatch" | Reproject layers to common CRS |
| "Insufficient memory" | Reduce processing tile size |
| "No infrared band found" | Check raster band configuration |

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Code Standards
- Follow PEP 8 guidelines
- Use descriptive variable names
- Add comments for complex logic
- Include type hints where appropriate

### Testing
```bash
# Run basic tests
python -m pytest tests/

# Test specific functionality
python test_calculation.py
```

## 📝 Changelog

### Version 1.0.0
- Initial release with basic functionality
- NDVI-based green area calculation
- Census sector statistics
- Basic export capabilities

### Upcoming Features
- Machine learning classification
- Time series analysis
- Advanced visualization options
- Cloud processing integration

## 📄 License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

### Documentation
- [User Guide](docs/user_guide.md)
- [API Reference](docs/api.md)
- [Tutorials](docs/tutorials/)

### Community Support
- [QGIS Forum](https://forum.qgis.org/)
- [GitHub Issues](https://github.com/indiaraelis/GreenAreaCalculator/issues)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/qgis+plugin)

### Professional Support
For enterprise support and custom development, contact: 
- **Email**: indiaraelis@gmail.com
- **LinkedIn**: [Your Website](https://www.linkedin.com/in/indiaraelis/)

## 🔗 Related Projects

- [QGIS](https://qgis.org/) - Free and Open Source Geographic Information System
- [GDAL](https://gdal.org/) - Geospatial Data Abstraction Library
- [NumPy](https://numpy.org/) - Scientific computing with Python

## 📊 Citation

If you use this plugin in your research, please cite:

```bibtex
@software{GreenAreaCalculator2024,
  author = {Elis, Indiara},
  title = {Green Area Calculator: QGIS Plugin for Vegetation Analysis},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/indiaraelis/GreenAreaCalculator}}
}
```

## 🌐 Links

- **GitHub Repository**: https://github.com/indiaraelis/GreenAreaCalculator
- **QGIS Plugin Page**: https://plugins.qgis.org/plugins/GreenAreaCalculator/
- **Issue Tracker**: https://github.com/indiaraelis/GreenAreaCalculator/issues
- **Documentation**: https://github.com/indiaraelis/GreenAreaCalculator/wiki

---

**Happy mapping!** 🌿 If you find this plugin useful, please consider giving it a star on GitHub!