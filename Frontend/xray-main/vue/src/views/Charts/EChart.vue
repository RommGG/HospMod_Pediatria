<template>
  <b-container fluid>
    <b-row>
     
      <b-col lg="4">
        <iq-card body-class="iq-card-body ps-0 pe-0 pt-0">
          <template v-slot:body>
            <div class="docter-details-block">
              <div class="doc-profile-bg bg-primary" style="height: 150px"></div>
              <div class="docter-profile text-center">
                <b-img :src="doctor.profilecopia" alt="profile-img" class="avatar-130 img-fluid"
                  style="border-radius: 100%;" />
              </div>
              <div class="text-center mt-3 ps-3 pe-3">
                <h4><b>Juan Carlos González Fernández</b></h4>
                <p>Paciente</p>
              </div>
              <hr />
              <ul class="doctoe-sedual d-flex align-items-center justify-content-between p-0 m-0">
                <li class="text-center">
                  <a :href="doctor.perfilInfanteUrl" class="btn-link">
                    <button type="button" class="btn rounded-pill btn-info">&nbsp;&nbsp;Ver seguimiento&nbsp;&nbsp;</button>
                  </a>
                </li>
              </ul>
            </div>
          </template>
        </iq-card>
      </b-col>
      
     
      <b-col lg="8">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>Pie Chart</h4>
          </template>
          <template v-slot:body>

            <v-chart class="chart" :option="PieChartOption" />

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
import VChart from "vue-echarts";
import { ref } from "vue";
// import ECharts from 'vue-echarts'
//mport * as echarts from "echarts";

export default {
  name: "HighCharts",
  components: { iqCard, VChart },
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

    
    
    
    const PieChartOption = ref({
      tooltip: {
        trigger: "item",
      },
      legend: {
        orient: "vertical",
        left: "left",
      },
      series: [
        {
          name: "Access From",
          type: "pie",
          radius: "50%",
          data: [
            { value: 1048, name: "January" },
            { value: 735, name: "February" },
            { value: 580, name: "March" },
            { value: 484, name: "April" },
            { value: 300, name: "May" },
          ],
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
          },
        },
      ],
    });
    

    return {

      PieChartOption
      
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
  height: 342px;
  width: 785px;
}
</style>
