# TIFF to PNG Converter
A Python script for converting TIFF images to PNG format while maintaining high image quality. This tool provides a user-friendly GUI interface for file selection and supports both single file conversion and batch processing of directories.

## Features
- GUI interface for easy file and directory selection
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
- tkinter (usually comes with Python)

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

1. Run the script:
```bash
python tiff_converter.py
```

2. Choose conversion mode:
   - Click "Yes" to convert a single file
   - Click "No" to convert all files in a directory

3. Use the file dialogs to:
   - Select input TIFF file(s) or directory
   - Choose output location for PNG file(s)

4. Optional: Adjust quality setting via command line:
```bash
python tiff_converter.py -q 90
```

### Command Line Arguments
- `-q, --quality`: Output quality from 0 to 95 (optional, default: 95)

## Examples
1. Basic usage with GUI:
```bash
python tiff_converter.py
```
Follow the dialog prompts to select files and locations.

2. Set custom quality with GUI:
```bash
python tiff_converter.py -q 85
```
Use the GUI to select files, but with 85% quality setting.

## Error Handling
The script includes comprehensive error handling:
- Logs all operations and errors
- Continues processing remaining files if one fails
- Provides clear error messages in both GUI and logs
- Creates output directories if they don't exist
- Shows warning dialogs for common issues

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
- Uses tkinter for GUI interface
- Thanks to all contributors

## Support
If you encounter any issues or have questions, please:
1. Check the existing issues in the repository
2. Create a new issue with a detailed description of your problem
3. Include any relevant error messages and logs

## Changelog
### Version 1.1.0
- Added GUI interface for file selection
- Improved user experience with dialog boxes
- Added interactive mode selection
- Enhanced error reporting with GUI alerts

### Version 1.0.0
- Initial release
- Basic TIFF to PNG conversion
- Directory processing support
- Quality configuration
- Logging implementation
