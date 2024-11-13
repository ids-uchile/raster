# PDF Rasterizer


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

**PDF Rasterizer** is a Python-based tool designed to convert vector-based PDF files into rasterized PDFs. By rasterizing PDFs, you can control the resolution (DPI) of the output, ensuring consistent visual quality across different platforms and devices. This is particularly useful for preserving the exact appearance of PDFs, especially when dealing with complex graphics or ensuring compatibility for specific printing requirements.

## Features

- **Batch Processing:** Automatically processes all PDF files placed in the `in` directory.
- **Customizable DPI:** Set your desired resolution (default is 330 DPI) to balance quality and file size.
- **Idempotent Operations:** Skips already rasterized PDFs in the `out` directory to save time and resources.
- **Simple Directory Setup:** Uses designated `in` and `out` folders for organized input and output management.
- **Cross-Platform Compatibility:** Runs on any system with Python 3.6 or higher.

## Directory Structure

```
pdf_rasterizer/
│
├── in/
│   └── .gitkeep
├── out/
│   └── .gitkeep
├── batch_rasterize_pdf.py
├── requirements.txt
└── README.md
```

- **`in/`**: Place your source PDF files here.
- **`out/`**: Rasterized PDFs will be saved here automatically.
- **`batch_rasterize_pdf.py`**: The main Python script for rasterizing PDFs.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`README.md`**: Provides an overview and instructions for the project.

## Installation

### Prerequisites

- **Python 3.6 or higher**: Ensure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone git@github.com:ids-uchile/raster.git
cd pdf_rasterizer
```

### Create Virtual Environment (Optional but Recommended)

Creating a virtual environment helps manage dependencies and avoid conflicts.

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **On macOS and Linux:**

  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

### Prepare Directories

Ensure that the project directory contains the `in` and `out` folders. If they don't exist, the script will create them automatically.

### Add PDF Files

Place all the PDF files you wish to rasterize into the `in` directory.

### Run the Script

Execute the Python script to start the rasterization process.

```bash
python batch_rasterize_pdf.py
```

### What Happens Next

- The script scans the `in` directory for all `.pdf` files.
- For each PDF, it checks if a corresponding rasterized version (with `_raster.pdf` appended to the filename) exists in the `out` directory.
- If the rasterized PDF does not exist, the script rasterizes the PDF at 330 DPI and saves it to the `out` directory.
- Existing rasterized PDFs in the `out` directory are skipped to prevent redundant processing.

## Example

Assuming you have a PDF named `sample_document.pdf` in the `in` folder, after running the script, you'll find `sample_document_raster.pdf` in the `out` folder.

```bash
# Before running the script
pdf_rasterizer/
│
├── in/
│   └── sample_document.pdf
├── out/
│   └── .gitkeep
├── batch_rasterize_pdf.py
├── requirements.txt
└── README.md

# After running the script
pdf_rasterizer/
│
├── in/
│   └── sample_document.pdf
├── out/
│   ├── sample_document_raster.pdf
│   └── .gitkeep
├── batch_rasterize_pdf.py
├── requirements.txt
└── README.md
```

## Notes

- **DPI Settings:** The default DPI is set to 330, which provides a good balance between quality and file size. You can adjust this value in the `batch_rasterize_pdf.py` script if needed.
- **Performance:** Rasterizing high-resolution PDFs can be resource-intensive. Ensure your system has adequate memory and processing power, especially when dealing with large or numerous PDF files.
- **File Naming:** Rasterized PDFs retain the original filename with `_raster` appended before the `.pdf` extension. For example, `document.pdf` becomes `document_raster.pdf`.
- **Error Handling:** The script includes basic error handling. If a PDF cannot be processed, an error message will be displayed, and the script will continue processing the remaining files.

