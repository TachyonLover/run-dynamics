fetch("feb-24-run.json")
  .then(response => response.json())
  .then(data => {
    console.log(data);

    const tableBody = document.querySelector("#splits-table tbody");

    data.forEach(split => {
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