<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Pacientes</h4>
          </template>
          <template v-slot:body>
            <b-row>
              <div class="table-ad mb-3 me-2">
                <b-button
                  variant=" float-end outline-link"
                  class="me-1">Filtrar</b-button>

              </div>
              <b-col md="12" class="table-responsive w-100">
                <b-table striped bordered hover :items="rows" :fields="columns">
                  <template v-slot:cell(NombrePaciente)="data">
                    <span v-if="!data.item.editable">{{ data.item.NombrePaciente }}</span>
                    <input
                      type="text"
                      v-model="data.item.NombrePaciente"
                      v-else
                      class="form-control text-center"
                    />
                  </template>
                  <template v-slot:cell(edad)="data">
                    <span v-if="!data.item.editable">{{ data.item.edad }}</span>
                    <input
                      type="text"
                      v-model="data.item.edad"
                      v-else
                      class="form-control text-center"
                    />
                  </template>
                  <template v-slot:cell(NombrePadre)="data">
                    <span v-if="!data.item.editable">{{
                      data.item.NombrePadre
                    }}</span>
                    <input
                      type="text"
                      v-model="data.item.NombrePadre"
                      v-else
                      class="form-control text-center"
                    />
                  </template>
                  <template v-slot:cell(NombreMadre)="data">
                    <span v-if="!data.item.editable">{{
                      data.item.NombreMadre
                    }}</span>
                    <input
                      type="text"
                      v-model="data.item.NombreMadre"
                      v-else
                      class="form-control text-center"
                    />
                  </template>
                  <template v-slot:cell(FechaNac)="data">
                    <span v-if="!data.item.editable">{{ data.item.FechaNac }}</span>
                    <input
                      type="text"
                      v-model="data.item.FechaNac"
                      v-else
                      class="form-control text-center"
                    />
                  </template>


                  <template v-slot:cell(segui)>
                    <td>
                      <a href="./Seguimiento" class="indigo-text" style="align-items: center;"
                        
                      >Ver Seguimiento</a>
                    </td>
                  </template>
                  
                 
                </b-table>
              </b-col>
            </b-row>
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
  methods: {
    add() {
      let obj = this.default();
      this.rows.push(obj);
    },
    default() {
      return {
        id: this.rows.length,
        NombrePaciente: "",
        edad: "",
        NombrePadre: "",
        NombreMadre: "",
        FechaNac: "2011/04/25",
        Segui: "$0",
      };
    },
    edit(item) {
      item.editable = true;
    },
    submit(item) {
      item.editable = false;
    },

  },
  data() {
    return {
      columns: [
        { label: "Nombre Paciente", key: "NombrePaciente", class: "text-left" },
        { label: "Edad", key: "edad", class: "text-left" },
        { label: "Nombre Padre", key: "NombrePadre", class: "text-left" },
        { label: "Nombre Madre", key: "NombreMadre", class: "text-left" },
        { label: "Fecha Nacimiento", key: "FechaNac", class: "text-left" },
        { label: "Seguimiento", key: "segui", class: "text-left" },
      ],
      rows: [
        {
          id: 1,
          NombrePaciente:  " \u00A0 ",
          edad:  " \u00A0 ",
          NombrePadre:  " \u00A0 ",
          NombreMadre:  " \u00A0  ",
          FechaNac:  " \u00A0 ",


        },
        {
          id: 1,
          NombrePaciente:  " \u00A0 ",
          edad:  " \u00A0 ",
          NombrePadre:  " \u00A0 ",
          NombreMadre:  " \u00A0  ",
          FechaNac:  " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente:  " \u00A0 ",
          edad:  " \u00A0 ",
          NombrePadre:  " \u00A0 ",
          NombreMadre:  " \u00A0  ",
          FechaNac:  " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente:  " \u00A0 ",
          edad:  " \u00A0 ",
          NombrePadre:  " \u00A0 ",
          NombreMadre:  " \u00A0  ",
          FechaNac:  " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente:  " \u00A0 ",
          edad:  " \u00A0 ",
          NombrePadre:  " \u00A0 ",
          NombreMadre:  " \u00A0  ",
          FechaNac:  " \u00A0 ",


        },
        {
          id: 1,
          NombrePaciente:  " \u00A0 ",
          edad:  " \u00A0 ",
          NombrePadre:  " \u00A0 ",
          NombreMadre:  " \u00A0  ",
          FechaNac:  " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente:  " \u00A0 ",
          edad:  " \u00A0 ",
          NombrePadre:  " \u00A0 ",
          NombreMadre:  " \u00A0  ",
          FechaNac:  " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente:  " \u00A0 ",
          edad:  " \u00A0 ",
          NombrePadre:  " \u00A0 ",
          NombreMadre:  " \u00A0  ",
          FechaNac:  " \u00A0 ",

        },
      ],
    };
  },
};
</script>
