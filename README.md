# JPGtoPNGConverter

## Overview

The **JPGtoPNGConverter** is a lightweight Python script designed to convert `.jpg` and `.jpeg` images in a specified input directory into `.png` format. The converted images are saved in a user-specified output directory while preserving the original filenames. The script also ensures the output directory is created if it doesn't already exist.

---

## Features

- Supports both `.jpg` and `.jpeg` file formats.
- Converts images to `.png` format while preserving the original filenames.
- Automatically creates the output directory if it doesn't already exist.
- Provides a simple command-line interface for easy usage.

---

## Requirements

### Python
Ensure you have **Python 3.x** installed. You can download Python from the official [Python Downloads](https://www.python.org/downloads/) page.

Check your Python installation by running:
```bash
python --version
```

### Python Library: Pillow
The script requires the **Pillow** library for image manipulation. Install it using the following command:
```bash
pip install pillow
```

---

## Installation & Setup

1. Clone or download the script to your local machine.
2. Navigate to the script's directory using a terminal or command prompt.

---

## Usage

Run the script from the terminal or command prompt using the following syntax:
```bash
python JPGtoPNGConverter.py <input_directory> <output_directory>
```

### Arguments:
- `<input_directory>`: Path to the folder containing `.jpg` or `.jpeg` files.
- `<output_directory>`: Path to the folder where converted `.png` files will be saved.

### Example Usage
If your input directory is `Pokedex` and your output directory is `New`, run the following command:
```bash
python JPGtoPNGConverter.py .\JPGtoPNGConverter\Pokedex .\JPGtoPNGConverter\New
```

This command will scan the `Pokedex` folder for `.jpg` and `.jpeg` files, convert them to `.png` format, and save the converted files in the `New` folder.

---

## Folder Structure:

**Before Running the Script**:
```
JPGtoPNGConverter/
├───New/       (Empty - Output folder)
└───Pokedex/
    ├── photo1.jpg
    ├── photo2.jpeg
```

**After Running the Script**:
```
JPGtoPNGConverter/
├───New/
│   ├── photo1.png
│   ├── photo2.png
└───Pokedex/
    ├── photo1.jpg
    ├── photo2.jpeg
```

---

## What the Script Does

1. **Input Directory Scanning**:
   - The script scans the **`<input_directory>`** for files with `.jpg` or `.jpeg` extensions.

2. **Image Conversion**:
   - Each `.jpg` or `.jpeg` file is opened using the Pillow library and converted to `.png` format.

3. **Output Directory Creation**:
   - If the specified **`<output_directory>`** doesn’t exist, the script creates it automatically.

4. **Filename Preservation**:
   - The script retains the original filenames while changing the file extension to `.png`.

---

## Error Handling

- If the `<input_directory>` doesn't exist, the script will terminate with an appropriate error message.
- Files that are not `.jpg` or `.jpeg` are ignored.

