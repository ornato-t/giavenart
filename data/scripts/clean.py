import json   

json_file_path = 'data_raw.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)

out = []
for annotation in data:
    y, x = annotation['coords']
    contents = annotation['contents']

    x_corrected = ((1600 - x) * 2) - 200
    y_corrected = ((2000 - y) * 2) - 378

    # Convert to REM
    x_corrected = x_corrected / 16
    y_corrected = y_corrected / 16

    out.append({
        "text": contents,
        "coords": [int(x_corrected), int(y_corrected)]
    })

with open('data.json', 'w') as file:
    json.dump(out, file, indent=4)
