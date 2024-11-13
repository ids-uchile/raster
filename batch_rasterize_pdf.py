import fitz  # PyMuPDF
from PIL import Image
import os
import sys

def rasterize_pdf(input_pdf_path, output_pdf_path, dpi=330):
    """
    Rasterizes each page of the input PDF and compiles them into a new PDF.

    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path where the output PDF will be saved.
    :param dpi: Resolution in DPI for rasterization.
    """
    try:
        # Open the input PDF
        pdf_document = fitz.open(input_pdf_path)
    except Exception as e:
        print(f"Error opening '{input_pdf_path}': {e}")
        return False

    # Calculate zoom factor based on DPI (72 is the default DPI in PDF)
    zoom_factor = dpi / 72
    transform = fitz.Matrix(zoom_factor, zoom_factor)

    raster_images = []

    for page_number in range(len(pdf_document)):
        try:
            page = pdf_document.load_page(page_number)
            pix = page.get_pixmap(matrix=transform)

            # Convert pixmap to PIL Image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            raster_images.append(img)
        except Exception as e:
            print(f"Error rasterizing page {page_number + 1} of '{input_pdf_path}': {e}")
            return False

    if not raster_images:
        print(f"No pages were rasterized for '{input_pdf_path}'.")
        return False

    try:
        # Save all images into a single PDF file
        raster_images[0].save(
            output_pdf_path,
            save_all=True,
            append_images=raster_images[1:],
            resolution=dpi
        )
    except Exception as e:
        print(f"Error saving rasterized PDF '{output_pdf_path}': {e}")
        return False

    return True

def ensure_directory(path):
    """
    Ensures that a directory exists. If it does not, creates it.

    :param path: Path to the directory.
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            print(f"Created directory: '{path}'")
        except Exception as e:
            print(f"Error creating directory '{path}': {e}")
            sys.exit(1)

def main():
    # Define input and output directories
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(current_dir, "in")
    output_dir = os.path.join(current_dir, "out")

    # Ensure that input and output directories exist
    ensure_directory(input_dir)
    ensure_directory(output_dir)

    # List all PDF files in the input directory
    input_pdfs = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    if not input_pdfs:
        print(f"No PDF files found in the 'in' directory: '{input_dir}'")
        sys.exit(0)

    print(f"Found {len(input_pdfs)} PDF file(s) in '{input_dir}'.")

    processed_count = 0
    skipped_count = 0

    for pdf_file in input_pdfs:
        input_pdf_path = os.path.join(input_dir, pdf_file)
        base_name, ext = os.path.splitext(pdf_file)
        output_pdf_name = f"{base_name}_raster{ext}"
        output_pdf_path = os.path.join(output_dir, output_pdf_name)

        if os.path.isfile(output_pdf_path):
            print(f"Skipping '{pdf_file}': Rasterized version already exists.")
            skipped_count += 1
            continue

        print(f"Rasterizing '{pdf_file}'...")
        success = rasterize_pdf(input_pdf_path, output_pdf_path, dpi=330)

        if success:
            print(f"Saved rasterized PDF as '{output_pdf_name}'.")
            processed_count += 1
        else:
            print(f"Failed to rasterize '{pdf_file}'.")

    print("\nProcessing Complete.")
    print(f"Total PDFs found: {len(input_pdfs)}")
    print(f"Rasterized: {processed_count}")
    print(f"Skipped (already rasterized): {skipped_count}")

if __name__ == "__main__":
    main()

