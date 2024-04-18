<template>
    <div>
        <!-- Slot donde se incluirá el contenido desde el componente padre -->
        <h1>Nacimientos Por Año</h1>
        <div style="width: 500px; height: 600px;">
            <canvas id="chartMongo1"></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
    data() {
        return {
            chart: null,
            pollingInterval: null,
            data: [],
            previousData: [], // Almacenar los datos anteriores
            colors: [
                'rgb(255, 99, 132)', // Rojo suave
                'rgb(255, 159, 64)', // Naranja suave
                'rgb(255, 205, 86)', // Amarillo suave
                'rgb(75, 192, 192)', // Verde azulado suave
                'rgb(54, 162, 235)', // Azul suave
                'rgb(153, 102, 255)', // Púrpura suave
                'rgb(201, 203, 207)', // Gris suave
                'rgb(255, 87, 34)', // Rojo anaranjado suave
                'rgb(255, 193, 7)', // Amarillo dorado suave
                'rgb(139, 195, 74)', // Verde lima suave
                'rgb(33, 150, 243)', // Azul cielo suave
                'rgb(233, 30, 99)', // Rosa suave
                'rgb(255, 152, 0)', // Naranja ámbar suave
                'rgb(205, 220, 57)', // Lima suave
                'rgb(0, 188, 212)', // Azul turquesa suave
                'rgb(124, 77, 255)', // Púrpura profundo suave
                'rgb(255, 235, 59)', // Amarillo limón suave
                'rgb(139, 195, 74)', // Verde lima suave
                'rgb(100, 181, 246)', // Azul claro suave
                'rgb(255, 174, 66)', // Naranja suave
                'rgb(33, 150, 243)', // Azul cielo suave
                'rgb(144, 164, 174)', // Azul acero suave
                'rgb(233, 30, 99)', // Rosa suave
                'rgb(0, 150, 136)', // Verde azulado suave
            ]
        };
    },
    mounted() {
        this.loadData(); // Cargar datos al inicio
        this.startPolling(); // Iniciar polling
    },
    beforeUnmount() {
        clearInterval(this.pollingInterval); // Limpiar el intervalo al destruir el componente
    },
    methods: {
        loadData() {
            fetch('http://127.0.0.1:8000/hospital/api/pacientes/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (this.hasDataChanged(data)) { // Verificar si los datos han cambiado
                        this.data = data;
                        this.updateChart();
                        this.previousData = data.slice(); // Actualizar los datos anteriores
                    }
                })
                .catch(error => {
                    console.error('Error al obtener datos:', error);
                });
        },
        updateChart() {
            
            let delayed;
            const anio = this.data.map(item => item.year);
            const cantidad = this.data.map(item => item.personas_count);

            const ctx = document.getElementById('chartMongo1').getContext('2d');
            if (this.chart) {
                this.chart.destroy(); // Destruir la instancia anterior del gráfico si existe
            }
            this.chart = new Chart(ctx, {
                type: 'doughnut', // Tipo de gráfico de dona
                data: {
                    labels: anio,
                    datasets: [
                        {
                            label: 'Nacimientos',
                            data: cantidad,
                            backgroundColor: this.colors.slice(0, anio.length), // Usar colores de forma secuencial
                            borderColor: '#ffffff',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    animation: {
                        onComplete: () => {
                            delayed = true;
                        },
                        delay: (context) => {
                            let delay = 0;
                            if (context.type === 'data' && context.mode === 'default' && !delayed) {
                                delay = context.dataIndex * 300 + context.datasetIndex * 100;
                            }
                            return delay;
                        },
                    },
                    scales: {
                        x: {
                            stacked: true,
                        },
                        y: {
                            stacked: true
                        }
                    }
                }
            });
        },
        startPolling() {
            this.pollingInterval = setInterval(() => {
                this.loadData(); // Cargar datos cada 3 segundos
            }, 2500);
        },
        hasDataChanged(newData) {
            // Comparar los nuevos datos con los datos anteriores
            return JSON.stringify(newData) !== JSON.stringify(this.previousData);
        }
    }
};
</script>