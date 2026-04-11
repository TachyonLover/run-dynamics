fetch("feb-24-run.json")
  .then(response => response.json())
  .then(data => {
    console.log(data);

    const summary = data.summary;
    const splits = data.splits;

    const summaryBox = document.querySelector("#summary-box");
    const tableBody = document.querySelector("#splits-table tbody");
    const toggleBtn = document.querySelector("#toggle-details-btn");
    const detailsPanel = document.querySelector("#details-panel");
    const runDate = document.querySelector("#run-date");

    // Optional: update this later when you store real date data in JSON
    runDate.textContent = "Insert date here";

    summaryBox.innerHTML = `
      <h2>Run Summary</h2>
      <div class="summary-stats">
        <div class="summary-item">
          <span class="summary-label">Total Time</span>
          <span class="summary-value">${summary.time}</span>
        </div>
        <div class="summary-item">
          <span class="summary-label">Total Distance</span>
          <span class="summary-value">${summary.distance} mi</span>
        </div>
        <div class="summary-item">
          <span class="summary-label">Average Pace</span>
          <span class="summary-value">${summary.avg_pace}</span>
        </div>
        <div class="summary-item">
          <span class="summary-label">Average HR</span>
          <span class="summary-value">${summary.avg_hr}</span>
        </div>
        <div class="summary-item">
          <span class="summary-label">Average Cadence</span>
          <span class="summary-value">${summary.avg_cadence}</span>
        </div>
        <div class="summary-item">
          <span class="summary-label">Calories Burned</span>
          <span class="summary-value">${summary.cals_burned}</span>
        </div>
      </div>
    `;

    splits.forEach(split => {
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

    toggleBtn.addEventListener("click", () => {
      detailsPanel.classList.toggle("hidden");

      if (detailsPanel.classList.contains("hidden")) {
        toggleBtn.textContent = "More";
      } else {
        toggleBtn.textContent = "Less";
      }
    });
  })
  .catch(error => {
    console.error("Error loading run data:", error);
  });