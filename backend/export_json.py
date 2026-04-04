import json

def export_json(csv_summary, csv_splits):
    data = {
        "summary": csv_summary,
        "splits": csv_splits
    }
    with open('feb-24-run.json', 'w') as f:
        json.dump(data, f, indent=4)