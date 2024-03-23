<template>
  <b-container fluid>
    <b-row>
      <b-col lg="8">
        <iq-card className="iq-card-block iq-card-stretch iq-card-height1">
          <template v-slot:headerTitle>
            <h4 class="card-title">Atenciones mas en el año 2023</h4>
          </template>
          <template v-slot:body>
            <ApexChart element="home-chart-05" :chartOption="chart5" v-if="$route.meta.dark" />
            <ApexChart element="home-chart-05" :chartOption="chart5" v-else />
          </template>
        </iq-card>
      </b-col>

      <b-col lg="4">
        <iq-card
          
        >
          <template v-slot:body>
            <img style="height: 425px; width: 290px;"
              src="../../assets/images/page-img/foto.png"
              class="rounded"
              alt="banner-img"
            />
          </template>
        </iq-card>
      </b-col>
      <b-col lg="4">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Satisfaccion de Pacientes</h4>
          </template>
          <template v-slot:body>
            <h2>
              3,897   <small class="text-secondary font-size-14"
                >  Reseñas de pacientes</small
              >
            </h2>
            <div class="progress mt-3 ">
              <div
                class="progress-bar bg-primary"
                role="progressbar"
                aria-valuenow="40"
                aria-valuemin="0"
                aria-valuemax="100"
                style="width: 40%"
              ></div>
              <div
                class="progress-bar bg-warning"
                role="progressbar"
                aria-valuenow="20"
                aria-valuemin="0"
                aria-valuemax="100"
                style="width: 20%"
              ></div>
              <div
                class="progress-bar bg-info"
                role="progressbar"
                aria-valuenow="10"
                aria-valuemin="0"
                aria-valuemax="100"
                style="width: 10%"
              ></div>
              <div
                class="progress-bar bg-danger"
                role="progressbar"
                aria-valuenow="40"
                aria-valuemin="0"
                aria-valuemax="100"
                style="width: 40%"
              ></div>
              <div
                class="progress-bar bg-success"
                role="progressbar"
                aria-valuenow="20"
                aria-valuemin="0"
                aria-valuemax="100"
                style="width: 20%"
              ></div>
              <div
                class="progress-bar bg-secondary"
                role="progressbar"
                aria-valuenow="10"
                aria-valuemin="0"
                aria-valuemax="100"
                style="width: 10%"
              ></div>
            </div>
            <div class="table-responsive mt-4">
              <table class="table mb-0 table-borderless">
                <tbody>
                  <tr>
                    <td>
                      <div class="iq-profile-avatar status-online mt-4"></div>
                    </td>
                    <td>
                      <h4>Excelente</h4>
                    </td>
                    <td><span class="text-muted">2400</span></td>
                    <td>60%</td>
                  </tr>
                  <tr>
                    <td>
                      <div class="iq-profile-avatar mt-4"></div>
                    </td>
                    <td>
                      <h4>Muy buena</h4>
                    </td>
                    <td><span class="text-muted">1200</span></td>
                    <td>30%</td>
                  </tr>
                  <tr>
                    <td>
                      <div class="iq-profile-avatar mt-4"></div>
                    </td>
                    <td>
                      <h4>Buena</h4>
                    </td>
                    <td><span class="text-muted">240</span></td>
                    <td>6%</td>
                  </tr>
                  <tr>
                    <td>
                      <div class="iq-profile-avatar mt-4"></div>
                    </td>
                    <td>
                      <h4>Aceptable</h4>
                    </td>
                    <td><span class="text-muted">80</span></td>
                    <td>2%</td>
                  </tr>
                  <tr>
                    <td>
                      <div class="iq-profile-avatar status-away mt-4"></div>
                    </td>
                    <td>
                      <h4>Mala</h4>
                    </td>
                    <td><span class="text-muted">40</span></td>
                    <td>1%</td>
                  </tr>
                  <tr>
                    <td>
                      <div class="iq-profile-avatar mt-4"></div>
                    </td>
                    <td>
                      <h4>Muy mala</h4>
                    </td>
                    <td><span class="text-muted">40</span></td>
                    <td>1%</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </template>
        </iq-card>
      </b-col>
      <b-col style="padding-top: 0px;">
        <b-row>
          <b-col lg="12" v-for="(item, index) in charts" :key="index">
            <iq-card>
              <template v-slot:headerTitle>
                <h4>{{ item.title }}</h4>
              </template>
              <template v-slot:body>
                <ApexChart :element="item.type" :chartOption="item.bodyData" />
              </template>
            </iq-card>
          </b-col>
        </b-row>
      </b-col>


      



    </b-row>








  </b-container>
</template>
<script>
import { xray } from "../../config/pluginInit";
import { useStore } from "../../store/pinia/index";
import { mapState } from "pinia";
// Chart
import ApexChart from "../../components/xray/charts/ApexChart";


import IqCard from "../../components/xray/cards/iq-card";
export default {
  name: "DashboardTwo",
  components: { IqCard, ApexChart },
  mounted() {
    xray.index();
  },
  computed: {
    ...mapState(useStore, {
      selectedLang: "lang",
    }),
  },
  watch: {},
  methods: {},
  data() {
    return {

      charts: [{

        title: "Infantes Vacunados en el Año 2023",
        type: "line-area",
        bodyData: {
          chart: {
            height: 375,
            type: "area",
          },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            curve: "smooth",
          },
          colors: ["#089bab", "#FC9F5B"],
          series: [
            {
              name: "Niños",
              data: [31, 40, 28, 51, 42, 109, 100, 25, 13, 41, 50, 100],
            },
            {
              name: "Niñas",
              data: [11, 32, 45, 32, 34, 52, 41, 19, 74, 15 , 95, 95],
            },
          ],

          xaxis: {
            type: "text",
            categories: [
              "Enero de 2023",
              "Febrero de 2023",
              "Marzo de 2023",
              "Abril de 2023",
              "Mayo de 2023",
              "Junio de 2023",
              "Julio de 2023",
              "Agosto de 2023",
              "Septiembre de 2023",
              "Octubre de 2023",
              "Noviembre de 2023",
              "Diciembre de 2023",
            ],
          },
          tooltip: {
            x: {
              format: "dd/MM/yy HH:mm",
            },
          },
        },
      }
      ],


      chart5: {
        series: [
          {
            name: "Niños",
            data: [44, 55, 41, 67, 22, 43],
          },
          {
            name: "Niñas",
            data: [13, 23, 20, 8, 13, 27],
          },

        ],
        colors: ["#089bab", "#FC9F5B", "#5bc5d1"],
        chart: {
          type: "bar",
          height: 350,
          stacked: true,
          toolbar: {
            show: true,
          },
          zoom: {
            enabled: true,
          },
        },
        responsive: [
          {
            breakpoint: 480,
            options: {
              legend: {
                position: "bottom",
                offsetX: -10,
                offsetY: 0,
              },
            },
          },
        ],
        plotOptions: {
          bar: {
            horizontal: false,
          },
        },
        xaxis: {
          type: "text",
          categories: [
            "Resfriado",
            "Gripe",
            "Infecciones de Oido",
            "Varicela",
            "Sarampion",
            "Poliomielitis",
          ],
        },
        legend: {
          position: "right",
          offsetY: 40,
        },
        fill: {
          opacity: 1,
        },
      },




    };
  },
};
</script>
