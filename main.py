import fitz  # pdf
# import fitz  # doc-docx
# import fitz  # pptx-ppt
# import fitz  # image
# import fitz  # image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image


def extract_text_from_local_image(image_path):
    image = Image.open(image_path)

    # Utilisation de pytesseract pour effectuer l'OCR
    extracted_text = pytesseract.image_to_string(image, lang='eng')

    return extracted_text



# def extract_text_from_pdf(file_path):
#     text = ""
#     try:
#         # Ouverture du fichier
#         with fitz.open(file_path) as pdf_document:
            
#             for page_number in range(pdf_document.page_count):
#                 page = pdf_document[page_number]
#                 text += page.get_text()
#                 print(page.get_links()[0].get("uri"))

#     except Exception as e:
#         print(f"Une erreur s'est produite : {e}")
#     return text


if __name__ == "__main__":
    # pdf_file_path = "assets/CV_Appolinaire_ADANDE (1).pdf"
    # extracted_text = extract_text_from_pdf(pdf_file_path)

    # if extracted_text:
    #     print("Texte extrait avec succès :")
    #     print(extracted_text)
    # else:
    #     print("L'extraction du texte a échoué.")

    # Exemple d'utilisation avec une image locale
    image_path = "./assets/Capture d'écran 2024-02-10 125444.png"
    result_text = extract_text_from_local_image(image_path)

    print("Texte extrait de l'image :\n", result_text)