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
        if lap == "Summary":
            continue
        lap_data = {
            "lap": lap,
            "time": df["time"].iloc[int(lap)-1],
            "distance": float(df["distance"].iloc[int(lap) - 1]),
            "avg pace": df["avg pace"].iloc[int(lap) - 1],
            "avg hr": int(df["avg hr"].iloc[int(lap) - 1]),
            "avg cadence": int(df["avg cad"].iloc[int(lap) - 1]),
            "cals burned": int(df["cal"].iloc[int(lap) - 1]),
        }
        sum_laps_list.append(lap_data)

    return sum_laps_list