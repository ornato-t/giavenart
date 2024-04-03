import json   

json_file_path = 'data.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)

annotations = data
min_x = 1e4
min_y = 1e4

for annotation in annotations:
    x, y = annotation['coords']

    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y

print('Minimum coordinates:', min_x, min_y)