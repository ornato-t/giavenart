import json   

json_file_path = 'data_raw.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)

out = []
rem_unit = 16
scale = 1.6
for annotation in data:
    x, y = annotation['coords']
    contents = annotation['contents']

    x_corrected = (x - 255) * scale
    y_corrected = (1903 - y) * scale

    # Convert to REM
    x_corrected = x_corrected / rem_unit
    y_corrected = y_corrected / rem_unit

    out.append({
        "text": contents,
        "coords": [int(x_corrected), int(y_corrected)]
    })

with open('data.json', 'w') as file:
    json.dump(out, file, indent=4)
