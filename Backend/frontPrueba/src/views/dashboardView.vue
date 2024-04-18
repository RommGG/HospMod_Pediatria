<template>
  <div>
    <div class="charts-container">
        <div class="chart-wrapper">
            <h1>Nacimientos Por Año</h1>
            <canvas id="chartMongo1"></canvas>
          </div>

                <div class="chart-wrapper">
                  <h1>Cantidad de pacientes por genero</h1>
                  <canvas id="chartMongo2"></canvas>
                  <br>
                <div>

                  <div class="xd">
                    <h2>
                      <p>Total de pacientes en mongo:</p>
                      <p v-if="totalpMongo !== null">{{ totalpMongo }}</p>
                      <p v-else>Cargando...</p>
                    </h2>
                  </div>
                </div>
          </div>

      </div>
  </div>
</template>

<script>
/*eslint-disable*/

import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      totalpMongo: null,
      pollingInterval3: null,
      chart1: null,
      chart2: null,
      pollingInterval1: null,
      pollingInterval2: null,
      data1: [],
      data2: [],
      previousData1: [], // Almacenar los datos anteriores
      previousData2: [], // Almacenar los datos anteriores
      colors1: [
        'rgb(255, 99, 132)', 'rgb(255, 159, 64)', 'rgb(255, 205, 86)',
        'rgb(75, 192, 192)', 'rgb(54, 162, 235)', 'rgb(153, 102, 255)',
        'rgb(201, 203, 207)', 'rgb(255, 87, 34)', 'rgb(255, 193, 7)',
        'rgb(139, 195, 74)', 'rgb(33, 150, 243)', 'rgb(233, 30, 99)',
        'rgb(255, 152, 0)', 'rgb(205, 220, 57)', 'rgb(0, 188, 212)',
        'rgb(124, 77, 255)', 'rgb(255, 235, 59)', 'rgb(139, 195, 74)',
        'rgb(100, 181, 246)', 'rgb(255, 174, 66)', 'rgb(33, 150, 243)',
        'rgb(144, 164, 174)', 'rgb(233, 30, 99)', 'rgb(0, 150, 136)'
      ], // Colores de las donas
      colors2: ['rgb(75, 192, 192)', 'rgb(255, 99, 132)'] // Colores de las barras
    };
  },
  mounted() {
    this.loadData1(); // Cargar datos al inicio
    this.loadData2(); // Cargar datos al inicio
    this.startPolling1(); // Iniciar polling
    this.startPolling2();
    this.startPolling3(); // Iniciar polling
    this.obtenertotalpMongo();
    // setInterval(this.obtenertotalpMongo, 2500)
  },
  beforeUnmount() {
    clearInterval(this.pollingInterval1); // Limpiar el intervalo al destruir el componente
    clearInterval(this.pollingInterval2); // Limpiar el intervalo al destruir el componente
    clearInterval(this.pollingInterval3)
  },
  methods: {

    obtenertotalpMongo() {
      fetch('http://127.0.0.1:8000/hospital/api/consulta/')
        .then(response => {
          if (!response.ok) {
            throw new Error('Error al obtener los datos');
          }
          return response.json();
        })
        .then(data => {
          this.totalpMongo = data.cantidad_pacientes;
        })
        .catch(error => {
          this.totalpMongo = 'Error al obtener los datos';
        });
    },

    loadData1() {
      fetch('http://127.0.0.1:8000/hospital/api/pacientes/')
        .then(response => {
          if (!response.ok) {
            console.log('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          if (this.hasDataChanged1(data)) { // Verificar si los datos han cambiado
            this.data1 = data;
            this.updateChart1();
            this.previousData1 = data.slice(); // Actualizar los datos anteriores
          }
        })
        .catch(error => {
          console.log('Error al obtener datos:', error);
        });
    },
    loadData2() {
      fetch('http://127.0.0.1:8000/hospital/api/pacientes2/')
        .then(response => {
          if (!response.ok) {
            console.log('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          if (this.hasDataChanged2(data)) { // Verificar si los datos han cambiado
            this.data2 = data;
            this.updateChart2();
            this.previousData2 = data.slice(); // Actualizar los datos anteriores
          }
        })
        .catch(error => {
          console.log('Error al obtener datos:', error);
        });
    },
    updateChart1() {
      const ctx = document.getElementById('chartMongo1').getContext('2d');
      const anio = this.data1.map(item => item.year);
      const cantidad = this.data1.map(item => item.personas_count);
      if (this.chart1) {
        this.chart1.destroy(); // Destruir la instancia anterior del gráfico si existe
      }
      this.chart1 = new Chart(ctx, {
        type: 'doughnut', // Tipo de gráfico de dona
        data: {
          labels: anio,
          datasets: [{
            label: 'Nacimientos',
            data: cantidad,
            backgroundColor: this.colors1.slice(0, anio.length), // Usar colores de forma secuencial
            borderColor: '#ffffff',
            borderWidth: 1
          }]
        },
        options: {
          animation: {
            onComplete: () => { },
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
    },
    updateChart2() {
      const ctx = document.getElementById('chartMongo2').getContext('2d');
      if (!this.chart2) {
        const masculinoData = this.data2.find(item => item._id === 'Masculino');
        const femeninoData = this.data2.find(item => item._id === 'Femenino');
        this.chart2 = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: ['Masculino', 'Femenino'],
            datasets: [{
              label: 'Nacimientos',
              data: [masculinoData.count, femeninoData.count],
              backgroundColor: this.colors2,
              borderColor: '#ffffff',
              borderWidth: 1
            }]
          },
          options: {
            animation: {
              onComplete: () => { },
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
      } else {
        const masculinoData = this.data2.find(item => item._id === 'Masculino');
        const femeninoData = this.data2.find(item => item._id === 'Femenino');
        this.chart2.data.datasets[0].data = [masculinoData.count, femeninoData.count];
        this.chart2.update();
      }
    },
    startPolling1() {
      if (!this.pollingInterval1) {
        this.pollingInterval1 = setInterval(() => {
          this.loadData1(); // Cargar datos cada 2.5 segundos
        }, 2500);
      }
    },

    startPolling2() {
      if (!this.pollingInterval2) {
        this.pollingInterval2 = setInterval(() => {
          this.loadData2(); // Cargar datos cada 2.5 segundos
        }, 2500);
      }
    },

    startPolling3() {
      if (!this.pollingInterval3) {
        this.pollingInterval3 = setInterval(() => {
          this.obtenertotalpMongo(); // Cargar datos cada 2.5 segundos
        }, 2500);
      }
    },


    hasDataChanged1(newData) {
      // Comparar los nuevos datos con los datos anteriores
      return JSON.stringify(newData) !== JSON.stringify(this.previousData1);
    },
    hasDataChanged2(newData) {
      // Comparar los nuevos datos con los datos anteriores
      return JSON.stringify(newData) !== JSON.stringify(this.previousData2);
    }
  }
};
</script>

<style scoped>
.charts-container {
  display: flex;
}

.chart-wrapper {
  flex: 1;
  margin-right: 20px;
  /* Ajusta el margen entre los gráficos */
  width: 500px;
  /* Ancho fijo */
  height: 600px;
  /* Alto fijo */
}

canvas {
  width: 100%;
  height: 100%;
}

.xd{
  background-color: gray; 
  border-radius:25px;
   padding:10px
}



</style>
