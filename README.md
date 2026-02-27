# run-dynamics
An interactive running analytics dashboard with GPX parsing and time-synced performance visualization.

• Run Dynamics is an interactive running analytics project focused on parsing and visualizing GPX/CSV activity data.
• The goal of this project is the build a performance dashboard that can:
- Parse GPX (and later CSV) run files
- Extract time-series metrics such as heart rate, cadence, elevation, and GPS coordinates
- Support a live replay map of a run
- Expand in the future to include additional contextual data (e.g., weather)

Current Status
• v0.1 - GPX parsing implemented
• Extracts time, latitude, longitude, elevation, heart rate, and cadence.
• Structures run data into a list of dictionaries for further processing

Planned features
• JSON export for frontend integration
• Interactive dashboard with charts
• Live run replay map
• Weather and environmental data

Tech Stack (so far)
Python
gpxpy
