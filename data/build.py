import json

def create_html_from_json(json_file_path, html_file_path):
    # Step 1: Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Step 2: Parse the JSON data
    annotations = data

    # Step 3: Generate the HTML content

    html_content = '<html><body>'
    for annotation in annotations:
        x, y = annotation['coords']
        content = annotation['text']

        # Position the text box using CSS
        html_content += f'<div style="position: absolute; left: {x}rem; top: {y}rem;">{content}</div>'
    html_content += '</body></html>'

    # Step 4: Write the HTML content to a file
    with open(html_file_path, 'w') as file:
        file.write(html_content)

if __name__ == '__main__':
    json_file_path = 'data.json'
    html_file_path = 'result.html'
    create_html_from_json(json_file_path, html_file_path)
