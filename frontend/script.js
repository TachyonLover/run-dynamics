fetch("feb-24-run.json")
  .then(response => response.json())
  .then(data => {
    const summary = data.summary;
    const summaryBox = document.querySelector("#summary-box");
    
    summaryBox.innerHTML = `
      <h2>Run Summary</h2>
      <p><strong>Total Time:</strong> ${summary.time}</p>
      <p><strong>Total Distance:</strong> ${summary.distance}</p>
      <p><strong>Average Pace:</strong> ${summary.avg_pace}</p>
      <p><strong>Average Heart Rate:</strong> ${summary.avg_hr}</p>
      <p><strong>Average Cadence:</strong> ${summary.avg_cadence}</p>
      <p><strong>Calories Burned:</strong> ${summary.cals_burned}</p>
    `;

    console.log(data);

    const tableBody = document.querySelector("#splits-table tbody");

    data.splits.forEach(split => {
      const row = document.createElement("tr");

      row.innerHTML = `
        <td>${split.lap}</td>
        <td>${split.time}</td>
        <td>${split.distance}</td>
        <td>${split.avg_pace}</td>
        <td>${split.avg_hr}</td>
        <td>${split.avg_cadence}</td>
        <td>${split.cals_burned}</td>
      `;

      tableBody.appendChild(row);
    });
  });