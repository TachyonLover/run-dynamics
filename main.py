from backend.gpx_parser import parse_gpx
from backend.csv_parser import parse_csv
from backend.export_json import export_json


def main():
    gpx = 'test-data/feb-24-run.gpx'
    csv = 'test-data/feb-24-run.csv'

    gpx_data = parse_gpx(gpx)
    csv_data = parse_csv(csv)

    export_json(csv_data)

if __name__ == "__main__":
    main()