# import module
from pdf2image import convert_from_path

def save_first_page():
    # Store Pdf with convert_from_path function
    images = convert_from_path('global_report.pdf',500,poppler_path=r'C:\Program Files\poppler-22.11.0\Library\bin')

    # for i in range(len(images)):
    # 	# Save pages as images in the pdf
    # 	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

    images[0].save('./tmp/firstpage_global_report.png', 'PNG')