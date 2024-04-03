import json   

json_file_path = 'data_raw.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)


min_x = 0
min_y = 0
for annotation in data:
    y, x = annotation['coords']

    if min_x < x:
        min_x = x
    if min_y < y:
        min_y = y

print('x: ',min_x,'; y: ', min_y)