import json

def export_json(csv_list):
    with open('feb-24-run.json', 'w') as f:
        json.dump(csv_list, f, indent=4)