# TIFF to PNG Converter
A Python script for converting TIFF images to PNG format while maintaining high image quality. This tool supports both single file conversion and batch processing of directories.

## Features
- High-quality TIFF to PNG conversion
- Batch processing of multiple files
- Configurable output quality
- Automatic color mode handling
- Detailed logging
- Support for custom output directories
- Error handling and recovery

## Prerequisites
- Python 3.6 or higher
- Pillow library

## Installation
1. Clone this repository or download the script:
```bash
git clone https://github.com/6ogo/tiff-converter.git
cd tiff-converter
```

2. Install the required dependencies:
```bash
pip install Pillow
```

## Usage
### Basic Usage
Convert a single TIFF file:
```bash
python tiff_converter.py input.tif
```

### Advanced Options
1. Convert a single file with custom output path:
```bash
python tiff_converter.py input.tif -o output.png
```

2. Convert all TIFF files in a directory:
```bash
python tiff_converter.py input_directory
```

3. Convert all TIFF files in a directory to a different output directory:
```bash
python tiff_converter.py input_directory -o output_directory
```

4. Adjust output quality (0-95, default is 95):
```bash
python tiff_converter.py input.tif -q 90
```

### Command Line Arguments
- `input`: Input TIFF file or directory (required)
- `-o, --output`: Output PNG file or directory (optional)
- `-q, --quality`: Output quality from 0 to 95 (optional, default: 95)

## Examples
1. Convert a single file:
```bash
python tiff_converter.py scan.tif
```
This will create `scan.png` in the same directory.

2. Convert multiple files with custom quality:
```bash
python tiff_converter.py scans_folder -o converted_images -q 85
```
This will convert all TIFF files in `scans_folder` to PNGs in `converted_images` with 85% quality.

## Error Handling
The script includes comprehensive error handling:
- Logs all operations and errors
- Continues processing remaining files if one file fails
- Provides clear error messages for troubleshooting
- Creates output directories if they don't exist

## Logging
The script generates logs with the following information:
- Conversion start and completion times
- Any errors or warnings encountered
- Processing status for each file
- Final conversion summary

## Technical Details

### Supported Input Formats
- `.tif`
- `.tiff`

### Color Mode Handling
- Preserves RGBA and RGB color modes
- Automatically converts other color modes to RGB
- Maintains transparency when present in original file

### Output Optimization
- Uses PNG optimization
- Configurable quality settings
- Maintains original image dimensions

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Built using the [Pillow](https://pillow.readthedocs.io/en/stable/) library
- Inspired by the need for high-quality image format conversion
- Thanks to all contributors

## Support
If you encounter any issues or have questions, please:
1. Check the existing issues in the repository
2. Create a new issue with a detailed description of your problem
3. Include any relevant error messages and logs

## Changelog
### Version 1.0.0
- Initial release
- Basic TIFF to PNG conversion
- Directory processing support
- Quality configuration
- Logging implementation
