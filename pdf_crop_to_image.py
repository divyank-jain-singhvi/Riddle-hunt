import fitz  
from PIL import Image

pdf_path = "demo3.pdf" 
output_folder = r"C:\Users\divyank.singhvi\Divyank\ctc_code\demo"


crop_left = 60   
crop_right = 15  
crop_top = 60    
crop_bottom = 60

doc = fitz.open(pdf_path)

for i in range(len(doc)):
    page = doc.load_page(i)
    pix = page.get_pixmap()
    
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    left = crop_left
    top = crop_top
    right = image.width - crop_right
    bottom = image.height - crop_bottom

    cropped_image = image.crop((left, top, right, bottom))

    cropped_image.save(f"{output_folder}/page_{i+1}.jpg", "JPEG")

print("Conversion and cropping complete!")
