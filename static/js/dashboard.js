const attackData = {
    labels: ["SQL Injection", "XSS", "Traversal", "Command Injection", "LFI"],
    datasets: [{
        data: [
            document.getElementById("sql").value,
            document.getElementById("xss").value,
            document.getElementById("traversal").value,
            document.getElementById("lfi").value,
            document.getElementById("command").value
        ],
        backgroundColor: [
            "#ef4444",
            "#f59e0b",
            "#3b82f6",
            "#22c55e",
            "#a855f7"
        ],
        borderColor: "#0f172a",
        borderWidth: 3,
        hoverOffset: 12
    }]
};

const config = {
    type: 'pie',
    data: attackData,

    options: {

        responsive: true,
        maintainAspectRatio: true,

        animation: {
            animateRotate: true,
            duration: 1000
        },

        plugins: {

            legend: {
                position: 'bottom',
                align: 'center',

                labels: {
                    color: "#e2e8f0",
                    font: {
                        size: 14,
                        weight: "bold"
                    },
                    boxWidth: 18,
                    boxHeight: 12,
                    padding: 15
                }
            },

            tooltip: {
                enabled: true,
                backgroundColor: "#1e293b",
                titleColor: "#ffffff",
                bodyColor: "#e2e8f0",
                borderColor: "#334155",
                borderWidth: 1
            }

        }

    }
};

new Chart(
    document.getElementById("attackChart"),
    config
);