<template>
  <div style="width: 500px; height: 600px;">
    <canvas id="chartMongo2"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      chart: null,
      pollingInterval: null,
      previousData: [], // Almacenar los datos anteriores
      colors: ['rgb(255, 99, 132)', 'rgb(75, 192, 192)'], // Colores de las barras
      currentData: {
        masculino: 0,
        femenino: 0
      }
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
      fetch('http://127.0.0.1:8000/hospital/api/pacientes2/')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          // Extraer los datos necesarios
          const masculinoData = data.find(item => item._id === 'Masculino');
          const femeninoData = data.find(item => item._id === 'Femenino');

          // Comparar los datos nuevos con los actuales
          if (this.currentData.masculino !== masculinoData.count ||
              this.currentData.femenino !== femeninoData.count) {
            // Si hay cambios, actualizar los datos actuales y la gráfica
            this.currentData.masculino = masculinoData.count;
            this.currentData.femenino = femeninoData.count;
            this.updateChart(masculinoData.count, femeninoData.count);
          }
        })
        .catch(error => {
          console.error('Error al obtener datos:', error);
        });
    },
    updateChart(masculinoCount, femeninoCount) {
      const ctx = document.getElementById('chartMongo2').getContext('2d');
      if (this.chart) {
        // Actualizar etiquetas y datos del gráfico existente
        this.chart.data.labels = ['Masculino', 'Femenino'];
        this.chart.data.datasets[0].data = [masculinoCount, femeninoCount];
        this.chart.update(); // Actualizar el gráfico con los nuevos datos
      } else {
        // Crear un nuevo gráfico con los datos recibidos
        this.chart = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: ['Masculino', 'Femenino'],
            datasets: [{
              label: 'Nacimientos',
              data: [masculinoCount, femeninoCount],
              backgroundColor: this.colors,
              borderColor: '#ffffff',
              borderWidth: 1
            }]
          },
          options: {
            animation: {
              onComplete: () => {},
              delay: (context) => {
                let delay = 0;
                if (context.type === 'data' && context.mode === 'default') {
                  delay = context.dataIndex * 300 + context.datasetIndex * 100;
                }
                return delay;
              },
            },
            scales: {
              x: {
                stacked: true
              },
              y: {
                stacked: true
              }
            }
          }
        });
      }
    },
    startPolling() {
      this.pollingInterval = setInterval(() => {
        this.loadData(); // Cargar datos cada 2.5 segundos
      }, 2500);
    }
  }
};
</script>
