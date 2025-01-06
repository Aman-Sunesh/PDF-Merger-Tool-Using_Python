
# PDF Merger Application

## Overview
This PDF merger application enables users to combine multiple PDF files into one, either by merging entire documents or selecting specific pages. Built using Python and the `pypdf` library, this tool offers a user-friendly command-line interface for customizing PDF output.

## Prerequisites
Before running this application, make sure you have the following:
- Python 3.8 or higher
- `pypdf`

## Installation

### Python Installation
Download and install Python from [python.org](https://www.python.org/downloads/).

### Library Installation
Use pip to install the required Python library:
```bash
pip install pypdf
```

### Clone the Repository
```bash
git clone https://github.com/yourusername/PDF-Merger-Tool-Using-Python.git
cd PDF-Merger-Tool-Using-Python
```

## Usage
To run the application, navigate to the application directory and run:
```bash
python pdf_merger.py
```

## Functionality

### Merge Entire PDFs
- **Usage**: Select option 1 to merge entire PDFs. You will be prompted to specify the PDF files to merge.

### Merge Specific Pages
- **Usage**: Select option 2 to merge specific pages from multiple PDFs. You will need to input the page ranges for each PDF.

### Exit
- **Option**: Select option 3 to exit the application.

## Important Notes
Ensure that the PDF files you intend to merge are located in the same directory as the script or specify the correct path to the files when prompted.

## Troubleshooting

### PDF File Not Found
Ensure that the file names are entered correctly and that the PDFs exist in the specified directory. Check for typos and try again.

### Installation Issues
If you encounter any issues with library installation, ensure you have the correct version of Python installed, and try reinstalling the `pypdf` library.
