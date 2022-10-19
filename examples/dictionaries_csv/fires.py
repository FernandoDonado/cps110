import json

fire_file = open('fires.json')

file_data = fire_file.read()
records = json.loads(file_data)

for rec in records:
    print(rec['street'], rec['station'])

    