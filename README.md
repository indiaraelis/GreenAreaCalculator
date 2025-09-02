# Green Area Calculator - QGIS Plugin

![QGIS Version](https://img.shields.io/badge/QGIS-3.16%2B-green.svg)
![License](https://img.shields.io/badge/License-GPLv2-blue.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

A QGIS plugin for calculating green vegetation areas per census sector using NDVI analysis and spatial statistics.

## 🌟 Features

### Core Functionality
- **NDVI-based Analysis**: Calculate vegetation indices from multispectral imagery
- **Sector Statistics**: Automated green area calculation per census sector
- **Cross-Platform**: Compatible with Windows, Linux, and macOS
- **User-Friendly Interface**: Simple dialog-based workflow

### Technical Features
- **Multi-format Support**: Works with various raster and vector formats
- **Custom Thresholding**: Adjustable NDVI parameters for different vegetation types
- **Real-time Validation**: Visual feedback for layer selection
- **Progress Tracking**: Built-in progress indicators for long operations

## 📦 Installation

### From QGIS Plugin Repository (Recommended)
1. Open QGIS
2. Go to `Plugins` → `Manage and Install Plugins...`
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
4. Enable the plugin in `Plugins` → `Manage and Install Plugins...`

### Development Installation
```bash
git clone https://github.com/indiaraelis/GreenAreaCalculator.git
cd GreenAreaCalculator
# Copy to QGIS plugins directory
```

## 🚀 Usage

### Basic Workflow
1. **Prepare Data**:
   - Load census sector polygon layer
   - Load multispectral raster with red and near-infrared bands

2. **Open Plugin**:
   - Go to `Vector` → `Green Area Calculator`
   - Or use the toolbar icon 🌿

3. **Configure Analysis**:
   - Select census layer from dropdown
   - Select vegetation raster layer
   - Both layers must have the same coordinate system

4. **Execute Calculation**:
   - Click `Calculate` button
   - Monitor progress in the dialog
   - Results will be added to QGIS

### Step-by-Step Guide

#### 1. Data Preparation
Ensure your data meets these requirements:
- **Census Layer**: Polygon vector layer (Shapefile, GeoPackage, etc.)
- **Vegetation Layer**: Multispectral raster with bands for NDVI calculation
- **Coordinate System**: Both layers should use the same CRS

#### 2. Plugin Interface
The plugin dialog contains:
- **Census Sectors Layer**: Dropdown to select polygon layer
- **Vegetation Layer**: Dropdown to select raster layer
- **Calculate Button**: Starts the analysis (enabled when both layers selected)
- **Progress Bar**: Shows calculation progress

#### 3. Results
After calculation:
- New attributes added to census layer with green area statistics
- Success message displayed in QGIS message bar
- Results available for visualization and export

## 📋 Requirements

### Software Requirements
- **QGIS**: Version 3.16 or higher
- **Python**: 3.7 or higher (included with QGIS)
- **Operating System**: Windows, Linux, or macOS

### Data Requirements
- **Census Data**: Polygon layer with sector boundaries
- **Imagery Data**: Raster layer with vegetation information
- **Coordinate System**: Consistent CRS between all layers

### System Requirements
- **RAM**: Minimum 4GB (8GB recommended for large datasets)
- **Storage**: Sufficient space for temporary processing files
- **Processing**: Multi-core support improves performance

## 🛠️ Configuration

The plugin uses standard QGIS libraries and requires no external dependencies. All configuration is done through the simple dialog interface.

### Default Settings
- NDVI calculation uses standard red and near-infrared bands
- Progress feedback provided during calculation
- Results integrated directly into QGIS project

## 📊 Output

### Generated Data
- **Enhanced Census Layer**: Original layer with added green area statistics
- **Calculation Results**: Percentage and area measurements per sector
- **QGIS Integration**: Results immediately available for mapping and analysis

### Supported Formats
Input layers can be in any format supported by QGIS:
- **Vector**: Shapefile, GeoPackage, PostGIS, etc.
- **Raster**: GeoTIFF, IMG, ERDAS, etc.

## 🐛 Troubleshooting

### Common Issues

#### "No layers available"
- **Solution**: Load vector and raster layers into QGIS before opening the plugin
- **Check**: Ensure layers are valid and properly loaded

#### "Please select both layers"
- **Solution**: Select both census and vegetation layers from dropdowns
- **Verify**: Both dropdowns show layer names, not empty selections

#### Plugin doesn't appear in menu
- **Solution**: Enable plugin in `Plugins` → `Manage and Install Plugins...`
- **Check**: Plugin is installed in correct QGIS plugins directory

### Performance Tips
- Use appropriate raster resolution for your analysis area
- Ensure sufficient system memory for large datasets
- Close unnecessary applications during processing

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup
1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/GreenAreaCalculator.git`
3. Create feature branch: `git checkout -b feature/new-feature`
4. Make changes and test
5. Submit pull request

### Code Standards
- Follow PEP 8 guidelines
- Use English for comments and documentation  
- Test on multiple platforms when possible
- Add appropriate error handling

### Reporting Issues
- Use [GitHub Issues](https://github.com/indiaraelis/GreenAreaCalculator/issues)
- Include QGIS version, operating system, and error details
- Provide sample data if possible

## 📄 License

This project is licensed under the GNU General Public License v2.0 or later - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

### Documentation
- [User Guide](https://github.com/indiaraelis/GreenAreaCalculator/wiki)
- [API Documentation](https://github.com/indiaraelis/GreenAreaCalculator/wiki/API)

### Community Support
- [GitHub Issues](https://github.com/indiaraelis/GreenAreaCalculator/issues)
- [QGIS Community Forum](https://forum.qgis.org/)

### Contact
- **Email**: indiaraelis@gmail.com
- **GitHub**: [@indiaraelis](https://github.com/indiaraelis)

## 🔗 Related Projects

- [QGIS](https://qgis.org/) - Free and Open Source Geographic Information System
- [GDAL](https://gdal.org/) - Geospatial Data Abstraction Library
- [NumPy](https://numpy.org/) - Scientific computing with Python

## 📊 Citation

If you use this plugin in your research, please cite:

```bibtex
@software{GreenAreaCalculator2025,
  author = {Elis, Indiara},
  title = {Green Area Calculator: QGIS Plugin for Vegetation Analysis},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/indiaraelis/GreenAreaCalculator}
}
```

## 🌐 Links

- **GitHub Repository**: https://github.com/indiaraelis/GreenAreaCalculator
- **Issue Tracker**: https://github.com/indiaraelis/GreenAreaCalculator/issues
- **QGIS Plugin Repository**: https://plugins.qgis.org/plugins/GreenAreaCalculator/

---

**Happy mapping!** 🌿 If you find this plugin useful, please consider giving it a star on GitHub!