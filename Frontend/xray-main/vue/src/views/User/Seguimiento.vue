<template>
  <b-container fluid>
    <b-row>
      <b-col md="8">
        <iq-card body-class="iq-card-body">
          <template v-slot:headerTitle>
            <div class="iq-card-header d-flex justify-content-between">
              <div class="iq-header-title">
                <h4 class="card-title">Informacion Personal</h4>
              </div>
            </div>
            <div class="iq-card-body">
              <div class="about-info m-0 p-2">
                <div class="row">
                  <div class="col-4">Nombre del Paciente:</div>
                  <div class="col-8"></div>
                  <div class="col-4">Nombre del Padre:</div>
                  <div class="col-8"></div>
                  <div class="col-4">Tipo de Nacimiento:</div>
                  <div class="col-8"></div>
                  <div class="col-4">Edad:</div>
                  <div class="col-8"></div>
                  <div class="col-4">Telefono de Contacto:</div>
                  <div class="col-8"></div>
                  <div class="col-4">Email de Contacto:</div>
                  <div class="col-8"></div>
                  <br>
                </div>
              </div>
            </div>

          </template>
        </iq-card>

      </b-col>


      <b-col md="4">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Citas</h4>
          </template>
          <template v-slot:body>
            <ul class="m-0 p-0 today-schedule">
              <li class="d-flex">
                <div class="schedule-icon">
                  <i class="ri-checkbox-blank-circle-fill text-primary" />
                </div>
                <div class="schedule-text">
                  <span>Ultima Cita</span> <span>Viernes 12 de Febrero de 2024 a las 11:30 am.</span>
                </div>
              </li>
              <li class="d-flex">
                <div class="schedule-icon">
                  <i class="ri-checkbox-blank-circle-fill text-success" />
                </div>
                <div class="schedule-text">
                  <span>Proxima Cita</span> <span>Viernes 12 de Abril de 2024 a las 11:30 am.</span>
                </div>
              </li>
            </ul>
          </template>
        </iq-card>
      </b-col>

      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>Ultimas Consultas</h4>
          </template>
          <template v-slot:body>
            <div class="table-responsive">
              <table class="table table-striped table-bordered">
                <thead>
                  <tr>
                    <th v-for="data in columns" :key="data">
                      {{ data.label }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="items in rows" :key="items">
                    <td>{{ items.Nombre }}</td>
                    <td>{{ items.fConsulta }}</td>
                    <td>{{ items.tConsulta }}</td>
                    <td>{{ items.Observaciones }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </template>
        </iq-card>
      </b-col>



    </b-row>
  </b-container>
</template>
<script>
import iqCard from "../../components/xray/cards/iq-card";
import { xray } from "../../config/pluginInit";
// import HighCharts from "highcharts";
// import More from "highcharts/highcharts-more";
// More(HighCharts);

// Echart
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";


// import ECharts from 'vue-echarts'
//mport * as echarts from "echarts";

export default {
  name: "HighCharts",
  components: { iqCard },
  mounted() {
    xray.index();
  },
  setup() {
    use([
      CanvasRenderer,
      PieChart,
      TitleComponent,
      TooltipComponent,
      LegendComponent,
    ]);







    return {




      columns: [
        { label: "Nombre", field: "Nombre", headerClass: "text-left" },
        { label: "Fecha de Consulta", field: "fConsulta ", headerClass: "text-left" },
        { label: "Tipo de Consulta", field: "tConsulta", headerClass: "text-left" },
        { label: "Observaciones", field: "Observaciones", headerClass: "text-left" },

      ],
      rows: [
        {
          id: 1,
          Nombre: " \u00A0",
          fConsulta: " \u00A0",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",

        },
        {
          id: 2,
          Nombre: " \u00A0",
          fConsulta: " \u00A0",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",

        },
        {
          Nombre: " \u00A0",
          fConsulta: " \u00A0",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",

        },
        {
          id: 4,
          Nombre: " \u00A0 ",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",

        },
        {
          id: 5,
          Nombre: " \u00A0",
          fConsulta: " \u00A0",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",
        },
      ],

    };
  },
  data() {
    return {
      doctor: {
        profilecopia: require('../personas/1.jpg'),
        profilecopia2: require('../personas/2.jpg'),
        profilecopia3: require('../personas/3.jpg'),
        profilecopia4: require('../personas/4.jpg'),
        profilecopia5: require('../personas/5.jpg'),
        profilecopia6: require('../personas/6.jpg'),
        perfilInfanteUrl: require('../User/Profile.vue'),
      },
      chart: null,
      xVal: 0,
      options: {
        exportEnabled: true,
        title: {
          text: "live random data",
        },
        data: [
          {
            type: "line",
            dataPoints: [],
          },
        ],
      },
      styleOptions: {
        width: "100%",
        height: "345px",
        fontSize: "18px",
      },
    };
  },
  methods: {
    updateChart(count) {
      count = count || 1;
      var yVal = 100;
      for (var j = 0; j < count; j++) {
        yVal = yVal + Math.round(5 + Math.random() * (-5 - 5));
        this?.options.data[0].dataPoints.push({
          x: this.xVal++,
          y: yVal,
        });
      }
      if (!!this.options.data[0].dataPoints.length > 10) {
        this.options.data[0].dataPoints.shift();
      }
      this.chart.render();
      setTimeout(this.updateChart, 1000);
    },
    chartInstance(chart) {
      this.chart = chart;
      this.updateChart(100);
    },
  },
};
</script>
<style scoped>
.chart {
  height: 245px;
  width: 100%;
}
</style>
