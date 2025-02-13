import os
from PIL import Image
import argparse
from pathlib import Path
import logging
import tkinter as tk
from tkinter import filedialog, messagebox

def setup_logging():
    """Configure logging settings"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def get_path_from_dialog(is_file=False, is_save=False):
    """
    Open file dialog to get input/output path
    
    Args:
        is_file (bool): True for file selection, False for directory
        is_save (bool): True for save dialog, False for open dialog
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    try:
        if is_file:
            if is_save:
                path = filedialog.asksaveasfilename(
                    defaultextension='.png',
                    filetypes=[('PNG files', '*.png'), ('All files', '*.*')]
                )
            else:
                path = filedialog.askopenfilename(
                    filetypes=[('TIFF files', '*.tif *.tiff'), ('All files', '*.*')]
                )
        else:
            path = filedialog.askdirectory(
                title='Select directory'
            )
        
        return path if path else None
        
    except Exception as e:
        logging.error(f'Error in file dialog: {str(e)}')
        return None

def convert_tiff_to_png(input_path, output_path=None, quality=95):
    """
    Convert a TIFF image to PNG format while preserving quality.
    
    Args:
        input_path (str): Path to the input TIFF file
        output_path (str, optional): Path for the output PNG file
        quality (int, optional): Quality setting for the output PNG (0-95)
    
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
        msg = f'No TIFF files found in {input_dir}'
        logging.warning(msg)
        messagebox.showwarning('Warning', msg)
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
    parser.add_argument('-q', '--quality', type=int, default=95,
                        help='Output quality (0-95, default: 95)')
    
    args = parser.parse_args()
    
    setup_logging()
    
    # Ask user if they want to convert a single file or directory
    root = tk.Tk()
    root.withdraw()
    choice = messagebox.askquestion('Input Type', 
                                  'Do you want to convert a single file?\n\n' +
                                  'Select "Yes" for single file\n' +
                                  'Select "No" for directory')
    
    if choice == 'yes':
        # Single file conversion
        input_path = get_path_from_dialog(is_file=True, is_save=False)
        if input_path:
            output_path = get_path_from_dialog(is_file=True, is_save=True)
            if output_path:
                convert_tiff_to_png(input_path, output_path, args.quality)
    else:
        # Directory conversion
        print("\nSelect input directory containing TIFF files...")
        input_dir = get_path_from_dialog(is_file=False)
        if input_dir:
            print("\nSelect output directory for PNG files (optional)...")
            output_dir = get_path_from_dialog(is_file=False)
            if input_dir:  # Allow output_dir to be None
                process_directory(input_dir, output_dir, args.quality)
    
    print("\nConversion complete!")
    input("Press Enter to exit...")

if __name__ == '__main__':
    main()
