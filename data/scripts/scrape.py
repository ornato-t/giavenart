import json
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal

def extract_text_and_coordinates(pdf_path):
    data = []
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, (LTTextBoxHorizontal, LTTextLineHorizontal)):
                x, y, text = element.bbox[0], element.bbox[1], element.get_text()
                data.append({
                    "contents": text,
                    "coords": [x, y]
                })
    return data

# Replace 'your_pdf_file.pdf' with the path to your PDF file
data = extract_text_and_coordinates('source.pdf')

# Save the data to a JSON file
with open('data_raw.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
