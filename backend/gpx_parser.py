import gpxpy

def parse_gpx(gpx_file):

    with open(gpx_file, 'r') as f:
        gpx = gpxpy.parse(f)

    data_pt_list = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:

                data_pt = {
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
                            data_pt.update({"hr":int(ext_child.text)})
                        elif "cad" in ext_child.tag:
                            data_pt.update({"cadence":int(ext_child.text)})

                data_pt_list.append(data_pt)

    return data_pt_list