<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <iq-card>
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
                    <td>{{ items.name }}</td>
                    <td>{{ items.position }}</td>
                    <td>{{ items.office }}</td>
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
import { xray } from "../../config/pluginInit";
import iqCard from "../../components/xray/cards/iq-card";
export default {
  name: "UiDataTable",
  components: { iqCard },
  mounted() {
    xray.index();
  },
  data() {
    return {
      columns: [
        { label: "Name", field: "name", headerClass: "text-left" },
        { label: "Position", field: "position", headerClass: "text-left" },
        { label: "Office", field: "office", headerClass: "text-left" },

      ],
      rows: [
        {
          id: 1,
          name: " \u00A0 ",
          position: " \u00A0 ",
          office: " \u00A0 ",

        },
        {
          id: 2,
          name: " \u00A0 ",
          position: " \u00A0 ",
          office: " \u00A0 ",

        },
        {
          id: 3,
          name: " \u00A0 ",
          position: " \u00A0 ",
          office: " \u00A0 ",

        },
        {
          id: 4,
          name: " \u00A0 ",
          position: " \u00A0 ",
          office: " \u00A0 ",

        },
        {
          id: 5,
          name: " \u00A0 ",
          position: " \u00A0 ",
          office: " \u00A0 ",
        },
      ],
    };
  },
};
</script>
