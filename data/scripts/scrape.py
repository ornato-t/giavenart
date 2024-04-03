import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import json

def extract_autocad_shx_text(pdf_name):
    # Use PdfReader instead of PdfFileReader
    pdf = PyPDF2.PdfReader(open(pdf_name, "rb"))
    numPages = len(pdf.pages)
    annotations_data = []

    for i in range(numPages):
        page = pdf.pages[i]
        annotations = page.get('/Annots')
        if annotations:
            for annot in annotations:
                # Use get_object instead of getObject
                obj = annot.get_object()
                if 'AutoCAD SHX Text' in obj.values():
                    contents = obj.get('/Contents')
                    rect = obj.get('/Rect')
                    print(f"Page {i+1}, Contents: {contents}, Rect: {rect}")

                    center_x = (rect[0] + rect[2]) / 2
                    center_y = (rect[1] + rect[3]) / 2

                    annotations_data.append({
                        "contents": contents,
                        "rect": rect,
                        "coords": [center_x, center_y]
                    })
    # Save the extracted data to a JSON file
    with open("data_raw.json", "w") as outfile:
        json.dump(annotations_data, outfile, indent=4)

if __name__ == '__main__':
    pdf_name = 'source.pdf'
    extract_autocad_shx_text(pdf_name)
