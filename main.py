from PIL import Image
import os
from tqdm import tqdm  # tqdm provides a progress bar
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert_images_to_txt(input_folder, output_folder):
    texts = []
    jpg_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]
    progress_bar = tqdm(total=len(jpg_files), desc='Converting Images', unit='image')

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for filename in jpg_files:
        jpg_path = os.path.join(input_folder, filename)
        image = Image.open(jpg_path)
        text = pytesseract.image_to_string(image)
        texts.append(text)

        # Save text to file
        txt_filename = filename.replace('.jpg', '.txt')
        txt_path = os.path.join(output_folder, txt_filename)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

        progress_bar.update(1)

    progress_bar.close()
    return texts

# Usage:
input_folder = r""
output_folder = r""
texts = convert_images_to_txt(input_folder, output_folder)
