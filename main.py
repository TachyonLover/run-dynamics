from gpx_parser import parse_gpx
from csv_parser import parse_csv


def main():
    gpx = 'test-data/feb-24-run.gpx'
    csv = 'test-data/feb-24-run.csv'

    gpx_data = parse_gpx(gpx)
    csv_data = parse_csv(csv)

    print(gpx_data[1])
    print(csv_data)

if __name__ == "__main__":
    main()