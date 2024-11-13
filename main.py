import fitz  # PyMuPDF
from PIL import Image
import sys
import os

def rasterize_pdf(input_pdf_path, output_pdf_path, dpi=330):
    """
    Rasterizes each page of the input PDF and compiles them into a new PDF.

    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path where the output PDF will be saved.
    :param dpi: Resolution in DPI for rasterization.
    """
    # Check if input PDF exists
    if not os.path.isfile(input_pdf_path):
        print(f"Error: The file '{input_pdf_path}' does not exist.")
        sys.exit(1)

    try:
        # Open the input PDF
        pdf_document = fitz.open(input_pdf_path)
        print(f"Opened '{input_pdf_path}' successfully.")
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        sys.exit(1)

    # Calculate zoom factor based on DPI (72 is the default DPI in PDF)
    zoom_factor = dpi / 72
    transform = fitz.Matrix(zoom_factor, zoom_factor)

    raster_images = []

    print("Rasterizing pages...")
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap(matrix=transform)

        # Convert pixmap to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        raster_images.append(img)
        print(f"Rasterized page {page_number + 1}/{len(pdf_document)}.")

    if not raster_images:
        print("No pages were rasterized.")
        sys.exit(1)

    print("Assembling rasterized images into PDF...")
    try:
        # Save all images into a single PDF file
        raster_images[0].save(
            output_pdf_path,
            save_all=True,
            append_images=raster_images[1:],
            resolution=dpi
        )
        print(f"Rasterized PDF saved as '{output_pdf_path}'.")
    except Exception as e:
        print(f"Error saving rasterized PDF: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python rasterize_pdf.py input.pdf output.pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = input_pdf.split(".")[0] + "_raster.pdf" 

    # You can change the DPI here if needed
    desired_dpi = 330

    rasterize_pdf(input_pdf, output_pdf, dpi=desired_dpi)

if __name__ == "__main__":
    main()

