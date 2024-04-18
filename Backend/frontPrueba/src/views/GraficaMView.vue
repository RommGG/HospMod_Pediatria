<template>
  <div>
  </div>


  <div style="width: 500px; height: 600px;">
    <canvas id="chartSql1"></canvas>
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
      previousData: [],// Almacenar los datos anteriores
      colors: [
                'rgb(255, 99, 132)', // Rojo suave
                'rgb(255, 159, 64)', // Naranja suave
                'rgb(139, 195, 74)', // Verde lima suave
                'rgb(75, 192, 192)',] // Verde azulado suave 
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
      fetch('http://127.0.0.1:8000/hospital/api/nciudad/')
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
      const lugares = this.data.map(item => item.lugar_nacimiento);
      const cantidades = this.data.map(item => item.cantidad_nacimientos);
  
      const ctx = document.getElementById('chartSql1').getContext('2d');
      if (this.chart) {
        this.chart.destroy(); // Destruir la instancia anterior del gráfico si existe
      }
      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: lugares,
          datasets: [
            {
              label: 'Nacimientos',
              data: cantidades,
              backgroundColor: this.colors,
              borderColor: '#ffffff',
              borderWidth: 1
            }
          ]
        },
        options: {
          animation: {
                        onComplete: () => {
                            delayed= true;
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
