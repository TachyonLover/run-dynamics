import gpxpy

def main():

    path = "test-data/feb-24-run.gpx"

    with open(path, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    total_pts = 0

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                total_pts += 1

    # Garmin GPX files are 1 point per second; so number of points = duration in secs.
    print(f"There is a total of {total_pts} seconds in your activity.\nGarmin logs data every second so 1 point = 1 second.")
    print()

    data_point_list = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:

                data_point = {
                    "time":point.time.isoformat(),
                    "latitude":point.latitude,
                    "longitude": point.longitude,
                    "elevation":point.elevation
                }

                # Garmin stores HR and cadence inside GPX extension tags.
                # Must extract manually from extension children.
                for ext in point.extensions:
                    for ext_child in list(ext):
                        if "hr" in ext_child.tag:
                            data_point.update({"hr":int(ext_child.text)})
                        elif "cad" in ext_child.tag:
                            data_point.update({"cadence":int(ext_child.text)})

                data_point_list.append(data_point)

    print(data_point_list[1])

if __name__ == "__main__":
    main()