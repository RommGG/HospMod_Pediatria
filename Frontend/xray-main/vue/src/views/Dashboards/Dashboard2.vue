dashboard nuevo

<template>
  <b-container fluid>
    <b-row>
      <div
        style="background-color: white; padding: 55px 15px; border-radius: 25px; display: flex; align-items: center;">
        <!-- Contenedor para los gráficos -->
        <!-- <div> -->
          <div class="charts-container">
            <div class="chart-wrapper">
              <div style="width: 300px;">
                <canvas id="partoNaturalChart"></canvas>
              </div>
              <div style="width: 300px;">
                <canvas id="cesareaChart"></canvas>
              </div>
            </div>


            <div class="chart-wrapper">
              <div>
                <canvas id="chartSql1"></canvas>
              </div>
            </div>

            <br>
            <div>
              <div class="chart-wrapper">

                <div class="xd">
                  <h2>
                    <p>Total de pacientes en MySQL:</p>
                    <p v-if="totalpSql !== null">{{ totalpSql }}</p>
                    <p v-else>Cargando...</p>
                  </h2>
                </div>
              </div>
            </div>
          </div>

        <!-- </div> -->

      </div>

      <div>
        <!-- Contenido del componente de la tabla de bebés -->
        <div v-if="message" style="margin-top: 10px;">
          {{ message }}
        </div>
      </div>



      <div>
        <h1>Listado de Bebés</h1>
        <table>
          <thead>
            <tr>
              <th>Id del Bebe</th>
              <th>Sexo del Bebe</th>
              <th>Nombre del Padre</th>
              <th>Nombre de la Madre</th>
              <th>Fecha de nacimiento</th>
              <th>Acciones</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="(bebe, index) in paginatedBebes" :key="index">
              <td>{{ bebe.id }}</td>
              <td>{{ bebe.sexo }}</td>
              <td>{{ bebe.nombre_padre }}</td>
              <td>{{ bebe.nombre_madre }}</td>
              <td>{{ bebe.fecha_nacimiento }}</td>
              <td>
                <button @click="eliminarBebe(bebe.id)">
                  <i class="fas fa-trash-alt"></i> Eliminar
                </button>
                &nbsp;&nbsp;&nbsp;

                <button style="margin-top: 5px;">
                  <router-link :to="{ name: 'editars', params: { id: bebe.id } }" class="router-link-custom">
                    <i class="fas fa-edit"></i> Editar
                  </router-link>

                </button>
              </td>
            </tr>
          </tbody>

        </table>

        <div style="margin-top: 10px;">
          <button @click="paginar('anterior')" :disabled="paginaActual === 1"
            style="background-color: black;">Anterior</button>&nbsp;
          <button @click="paginar('siguiente')" :disabled="paginaActual * itemsPorPagina >= bebes.length"
            style="background-color: black;">Siguiente</button>
        </div>

        <!-- Mostrar el número de página actual y el número total de páginas -->
        <div style="margin-top: 10px;">
          Página {{ paginaActual }} de {{ totalPages }}
        </div>

      </div>




    </b-row>


  </b-container>
</template>
<script>
/*eslint-disable*/
import { xray } from "../../config/pluginInit";
import { useStore } from "../../store/pinia/index";
import { mapState } from "pinia";
// Chart
import ApexChart from "../../components/xray/charts/ApexChart";

import Chart from 'chart.js/auto';



import IqCard from "../../components/xray/cards/iq-card";
export default {
  name: "DashboardTwo",
  components: { IqCard, ApexChart },
  mounted() {
    xray.index();

  },
  data() {
    return {
      bebes: [],
      paginatedBebes: [], // Lista de bebés a mostrar en la página actual
      message: '',
      paginaActual: 1,
      itemsPorPagina: 10,
      partoNaturalChart: null,
      cesareaChart: null,
      chartSql1: null,
      totalpSql: null,
      currentData: {
        pnMasculino: null,
        pnFemenino: null,
        cMasculino: null,
        cFemenino: null,
      },
      data: {
        labels: [],
        datasets: [{
          label: 'Parto Natural',
          data: [],
          backgroundColor: ['skyblue', 'lightpink']
        },
        {
          label: 'Cesárea',
          data: [],
          backgroundColor: ['skyblue', 'lightpink']
        }
        ]
      },
      chartData: [],
      previousChartData: [], // Almacenar los datos anteriores
      colors: [
        'rgb(255, 99, 132)', // Rojo suave
        'rgb(255, 159, 64)', // Naranja suave
        'rgb(139, 195, 74)', // Verde lima suave
        'rgb(75, 192, 192)', // Verde azulado suave 
      ]


    };
  },

  computed: {

    ...mapState(useStore, {
      selectedLang: "lang",
    }),
    totalPages() {
      return Math.ceil(this.totalBebes.length / this.itemsPorPagina);
    },
    totalBebes() {
      return this.bebes;
    },
  },
  mounted() {
    this.obtenerBebes();
    this.loadData(); // Cargar datos al inicio
    this.startPolling(); // Iniciar polling
    this.obtenerTotalSQL();
    setInterval(this.obtenerTotalSQL, 2000);

  },
  beforeUnmount() {
    clearInterval(this.pollingInterval); // Limpiar el intervalo al destruir el componente



  },


  methods: {
    obtenerBebes() {
      fetch('http://localhost:8000/hospital/api/nacimientos/') // Corregir la URL del endpoint
        .then(response => {
          if (!response.ok) {
            throw new Error('Hubo un problema al obtener la lista de bebés.');
          }
          return response.json();
        })
        .then(data => {
          // Asignar la lista de bebés obtenida desde la API a la variable bebes
          this.bebes = data;
          // Llamar a la función para mostrar los primeros 10 datos
          this.mostrarDatosPaginados();
        })
        .catch(error => {
          this.message = "Error: " + error.message;
        });
    },
    eliminarBebe(id) {
      fetch(`http://localhost:8000/hospital/api/nacimientos/${id}/`, { // Corregir la URL del endpoint
        method: 'DELETE'
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Hubo un problema al eliminar el bebé.');
          }
          this.message = "¡Bebé eliminado exitosamente!";
          // Eliminar el bebé de la lista después de eliminarlo en el backend
          this.bebes = this.bebes.filter(bebe => bebe.id !== id);
          // Actualizar los datos paginados después de eliminar un bebé
          this.mostrarDatosPaginados();
        })
        .catch(error => {
          this.message = "Error: " + error.message;
        });
    },
    mostrarDatosPaginados() {
      const inicio = (this.paginaActual - 1) * this.itemsPorPagina;
      const fin = this.paginaActual * this.itemsPorPagina;
      this.paginatedBebes = this.bebes.slice(inicio, fin);
    },
    paginar(direccion) {
      if (direccion === 'anterior') {
        this.paginaActual--;
      } else {
        this.paginaActual++;
      }
      // Llamar a la función para mostrar los datos de la página actual
      this.mostrarDatosPaginados();
    },
    obtenerTotalSQL() {
      fetch('http://127.0.0.1:8000/hospital/api/partos/')
        .then(response => {
          if (!response.ok) {
            throw new Error('Error al obtener los datos');
          }
          return response.json();
        })
        .then(data => {
          if (Array.isArray(data) && data.length > 0) { // Cambio 'bebes' por 'data'
            // Acceder al primer elemento del array y obtener el valor de total_pacientes
            this.totalpSql = data[0].total_pacientes; // Cambio 'bebes' por 'data'
          } else {
            throw new Error('No se encontraron datos válidos');
          }
        })
        .catch(error => {
          this.totalpSql = 'Error al obtener los datos';
        });
    },
    loadData() {
      fetch('http://127.0.0.1:8000/hospital/api/partos/')
        .then(response => {
          if (!response.ok) {
            throw new Error('Error al recuperar los datos de partos');
          }
          return response.json();
        })
        .then(data => {
          const newPnMasculino = data[0].pn_masculino;
          const newPnFemenino = data[0].pn_femeninos;
          const newCMasculino = data[0].c_masculino;
          const newCFemenino = data[0].c_femenino;
          if (this.currentData.pnMasculino !== newPnMasculino || this.currentData.pnFemenino !== newPnFemenino || this.currentData.cMasculino !== newCMasculino || this.currentData.cFemenino !== newCFemenino) {
            this.currentData.pnMasculino = newPnMasculino;
            this.currentData.pnFemenino = newPnFemenino;
            this.currentData.cMasculino = newCMasculino;
            this.currentData.cFemenino = newCFemenino;
            this.updatePartoNaturalChart(newPnMasculino, newPnFemenino);
            this.updateCesareaChart(newCMasculino, newCFemenino);
          }
        })
        .catch(error => {
          console.error('Error al cargar los datos desde la API de partos:', error);
        });

      fetch('http://127.0.0.1:8000/hospital/api/nciudad/')
        .then(response => {
          if (!response.ok) {
            throw new Error('Error al recuperar los datos de nacimiento');
          }
          return response.json();
        })
        .then(data => {
          if (this.hasDataChanged(data)) { // Verificar si los datos han cambiado
            this.chartData = data;
            this.updateChartSql1();
            this.previousChartData = data.slice(); // Actualizar los datos anteriores
          }
        })
        .catch(error => {
          console.error('Error al obtener datos de nacimiento:', error);
        });
    },
    updatePartoNaturalChart(pnMasculino, pnFemenino) {
      const ctx = document.getElementById('partoNaturalChart').getContext('2d');
      if (this.partoNaturalChart) {
        this.partoNaturalChart.destroy(); // Destruir la instancia anterior del gráfico si existe
      }
      this.partoNaturalChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['Masculino', 'Femenino'],
          datasets: [{
            label: 'Parto Natural',
            data: [pnMasculino, pnFemenino],
            backgroundColor: this.data.datasets[0].backgroundColor
          }]
        },
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: 'Comparación en Parto Natural'
            },
            tooltips: {
              enabled: false
            }
          }
        }
      });
    },
    updateCesareaChart(cMasculino, cFemenino) {

      const ctx = document.getElementById('cesareaChart').getContext('2d');
      if (this.cesareaChart) {
        this.cesareaChart.destroy(); // Destruir la instancia anterior del gráfico si existe
      }
      this.cesareaChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['Masculino', 'Femenino'],
          datasets: [{
            label: 'Cesárea',
            data: [cMasculino, cFemenino],
            backgroundColor: this.data.datasets[1].backgroundColor
          }]
        },
        options: {
          responsive: true,

          plugins: {
            title: {
              display: true,
              text: 'Comparación en Parto por Cesárea'
            },
            tooltips: {
              enabled: false
            }
          }
        }
      });
    },
    updateChartSql1() {
      const lugares = this.chartData.map(item => item.lugar_nacimiento);
      const cantidades = this.chartData.map(item => item.cantidad_nacimientos);
      let delayed;
      const ctx = document.getElementById('chartSql1').getContext('2d');
      if (this.chartSql1) {
        this.chartSql1.destroy(); // Destruir la instancia anterior del gráfico si existe
      }
      this.chartSql1 = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: lugares,
          datasets: [{
            label: 'Nacimientos',
            data: cantidades,
            backgroundColor: this.colors,
            borderColor: '#ffffff',
            borderWidth: 1
          }]
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
      }, 3000);
    },
    hasDataChanged(newData) {
      // Comparar los nuevos datos con los datos anteriores
      return JSON.stringify(newData) !== JSON.stringify(this.previousChartData);
    }



  }


};
</script>


<style scoped>
/* Estilos para iconos de Font Awesome */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

/* Estilos para la tabla */
table {
  width: 80%;
  border-collapse: collapse;
  margin-left: 0 auto;
  margin-right: 0 auto;
}

th,
td {
  border: 1px solid #dddddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

/* Estilos para los botones */
button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 8px 12px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: #45a049;
}

/* Estilos para el ícono */
.fas.fa-trash-alt {
  margin-right: 5px;
}

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

.xd {
  background-color: gray;
  border-radius: 25px;
  padding: 10px;
}
</style>
