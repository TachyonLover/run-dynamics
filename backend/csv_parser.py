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

    sum_laps_list = []
    
    for lap in df["laps"]:

        # For now, the "Summary" row is being treated as a lap, but it might be better to handle it separately in the future.

        if lap == "Summary":
            summary_row = df[df["laps"] == "Summary"].iloc[0]
            lap_data = {
                "lap": lap,
                "time": summary_row["time"],
                "distance": float(summary_row["distance"]),
                "avg_pace": summary_row["avg pace"],
                "avg_hr": int(summary_row["avg hr"]),
                "avg_cadence": int(summary_row["avg cad"]),
                "cals_burned": int(summary_row["cal"]),
            }

        else:
            lap_data = {
                "lap": lap,
                "time": df["time"].iloc[int(lap)-1],
                "distance": float(df["distance"].iloc[int(lap) - 1]),
                "avg_pace": df["avg pace"].iloc[int(lap) - 1],
                "avg_hr": int(df["avg hr"].iloc[int(lap) - 1]),
                "avg_cadence": int(df["avg cad"].iloc[int(lap) - 1]),
                "cals_burned": int(df["cal"].iloc[int(lap) - 1]),
            }
        sum_laps_list.append(lap_data)

    return sum_laps_list