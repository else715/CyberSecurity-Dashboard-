document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/logs')
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("logTable");
            data.forEach(log => {
                let row = `<tr>
                    <td>${log.timestamp}</td>
                    <td>${log.source_ip}</td>
                    <td>${log.severity}</td>
                    <td>${log.message}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        });

    fetch('/api/threats')
        .then(response => response.json())
        .then(data => {
            let ctx = document.getElementById('threatChart').getContext('2d');
            let threatTypes = data.map(threat => threat.type);
            let threatLevels = data.map(threat => threat.risk_level);

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: threatTypes,
                    datasets: [{
                        label: 'Threat Risk Level',
                        data: threatLevels,
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                }
            });
        });
});
