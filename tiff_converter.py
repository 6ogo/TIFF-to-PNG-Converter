import os
from PIL import Image
import argparse
from pathlib import Path
import logging

def setup_logging():
    """Configure logging settings"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def convert_tiff_to_png(input_path, output_path=None, quality=95):
    """
    Convert a TIFF image to PNG format while preserving quality.
    
    Args:
        input_path (str): Path to the input TIFF file
        output_path (str, optional): Path for the output PNG file. If not provided,
                                   will use the same location as input with .png extension
        quality (int, optional): Quality setting for the output PNG (0-95). Defaults to 95
    
    Returns:
        str: Path to the converted PNG file
    """
    try:
        # Create output path if not provided
        if output_path is None:
            output_path = str(Path(input_path).with_suffix('.png'))
        
        # Open and convert the image
        with Image.open(input_path) as img:
            # Preserve the color mode
            if img.mode in ['RGBA', 'RGB']:
                converted_img = img
            else:
                converted_img = img.convert('RGB')
            
            # Save as PNG with high quality
            converted_img.save(
                output_path,
                'PNG',
                optimize=True,
                quality=quality
            )
            
            logging.info(f'Successfully converted {input_path} to {output_path}')
            return output_path
            
    except Exception as e:
        logging.error(f'Error converting {input_path}: {str(e)}')
        raise

def process_directory(input_dir, output_dir=None, quality=95):
    """
    Convert all TIFF files in a directory to PNG format.
    
    Args:
        input_dir (str): Directory containing TIFF files
        output_dir (str, optional): Directory for output PNG files
        quality (int, optional): Quality setting for the output PNGs
    """
    input_path = Path(input_dir)
    
    # Create output directory if specified
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    # Process all TIFF files
    tiff_files = list(input_path.glob('*.tif')) + list(input_path.glob('*.tiff'))
    
    if not tiff_files:
        logging.warning(f'No TIFF files found in {input_dir}')
        return
    
    for tiff_file in tiff_files:
        if output_dir:
            output_file = output_path / f'{tiff_file.stem}.png'
        else:
            output_file = None
            
        try:
            convert_tiff_to_png(str(tiff_file), str(output_file) if output_file else None, quality)
        except Exception as e:
            logging.error(f'Failed to convert {tiff_file}: {str(e)}')
            continue

def main():
    parser = argparse.ArgumentParser(description='Convert TIFF images to PNG format')
    parser.add_argument('input', help='Input TIFF file or directory')
    parser.add_argument('-o', '--output', help='Output PNG file or directory (optional)')
    parser.add_argument('-q', '--quality', type=int, default=95,
                        help='Output quality (0-95, default: 95)')
    
    args = parser.parse_args()
    
    setup_logging()
    
    input_path = Path(args.input)
    
    if input_path.is_file():
        convert_tiff_to_png(str(input_path), args.output, args.quality)
    elif input_path.is_dir():
        process_directory(str(input_path), args.output, args.quality)
    else:
        logging.error(f'Input path {args.input} does not exist')

if __name__ == '__main__':
    main()
