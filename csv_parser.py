import pandas as pd

df = pd.read_csv('test-data/feb-24-run.csv')

df = df.rename(columns= {
    "Laps": "laps",
    "Time": "time",
    "Distancemi": "distance",
    "Avg Pacemin/mi": "avg pace",
    "Avg HRbpm": "avg hr",
    "Avg Run Cadencespm": "avg cad",
    "CaloriesC": "cal"
})

total_mi = df["distance"].iloc[-1]
total_time = df["time"].iloc[-1]

print(f"Total time: {total_time}")
print(f"Total miles: {total_mi} mi")
print()

all_laps = []
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
    print(lap_data)