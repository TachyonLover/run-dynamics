import pandas as pd

def parse_csv(csv_file):
    df = pd.read_csv(csv_file)
    df = df.rename(columns= {
    "Laps": "laps",
    "Time": "time",
    "Distancemi": "distance",
    "Avg Pacemin/mi": "avg pace",
    "Avg HRbpm": "avg hr",
    "Avg Run Cadencespm": "avg cad",
    "CaloriesC": "cal"
    })

    splits_list = []
    summary_row = df[df["laps"] == "Summary"].iloc[0]

    summary_lap_data = {
                "time": summary_row["time"],
                "distance": float(summary_row["distance"]),
                "avg_pace": summary_row["avg pace"],
                "avg_hr": int(summary_row["avg hr"]),
                "avg_cadence": int(summary_row["avg cad"]),
                "cals_burned": int(summary_row["cal"]),
            }
    
    splits_rows = df[df["laps"] != "Summary"]

    for index, row in splits_rows.iterrows():
            lap_data = {
                "lap": row["laps"],
                "time": row["time"],
                "distance": float(row["distance"]),
                "avg_pace": row["avg pace"],
                "avg_hr": int(row["avg hr"]),
                "avg_cadence": int(row["avg cad"]),
                "cals_burned": int(row["cal"]),
            }
            splits_list.append(lap_data)

    return summary_lap_data, splits_list