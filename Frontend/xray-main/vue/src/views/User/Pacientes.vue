<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Pacientes</h4>
          </template>
          
          <br>
          <div style="background-color: white; padding: 10px; border-radius: 25px; display: flex; align-items: center;">
            

            <table mb="2">
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
                    <button @click="eliminarBebe(bebe.id)"
                      style="margin-top: 3px; border-radius: 25px; background-color: red">
                      <i class="fas fa-trash-alt"></i> Eliminar
                    </button>
                    &nbsp;&nbsp;&nbsp;

                    <button style="margin-top: 3px; border-radius: 25px; background-color: #FFAB04 ">
                      <router-link :to="{ name: 'editars', params: { id: bebe.id } }" class="router-link-custom">
                        <i class="fas fa-edit"></i> Editar
                      </router-link>
                    </button>
                    &nbsp;&nbsp;&nbsp;

                    <button style="margin-top: 3px; border-radius: 25px;">
                      <router-link :to="{ name: 'seguim', params: { id: bebe.id } }" class="router-link-custom">
                        <i class="fas fa-user-alt"></i> Seguimiento
                      </router-link>
                    </button>
                  </td>
                </tr>
                <div style="margin-top: 10px;">
                  <button @click="paginar('anterior')" :disabled="paginaActual === 1"
                    style="background-color: black;">Anterior</button>&nbsp;
                  <button @click="paginar('siguiente')" :disabled="paginaActual * itemsPorPagina >= bebes.length"
                    style="background-color: black;">Siguiente</button>
                </div>

                <!-- Mostrar el número de página actual y el número total de páginas -->
                <div style="margin-top: 10px;">
                  Página {{ paginaActual }} de {{ totalPages }}<br><br>
                </div>
              </tbody>
            </table>
          </div>
        </iq-card>
      </b-col>
    </b-row>
    <br><br>
  </b-container>
</template>






<script>
import { xray } from "../../config/pluginInit";
//import iqCard from "../../components/xray/cards/iq-card";
export default {
  name: "UiDataTable",
  //components: { iqCard },
  mounted() {
    xray.index();
    this.obtenerBebes();

  },





  computed: {
    totalPages() {
      return Math.ceil(this.totalBebes.length / this.itemsPorPagina);
    },
    totalBebes() {
      return this.bebes;
    },
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
    }










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
          NombrePaciente: " \u00A0 ",
          edad: " \u00A0 ",
          NombrePadre: " \u00A0 ",
          NombreMadre: " \u00A0  ",
          FechaNac: " \u00A0 ",


        },
        {
          id: 1,
          NombrePaciente: " \u00A0 ",
          edad: " \u00A0 ",
          NombrePadre: " \u00A0 ",
          NombreMadre: " \u00A0  ",
          FechaNac: " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente: " \u00A0 ",
          edad: " \u00A0 ",
          NombrePadre: " \u00A0 ",
          NombreMadre: " \u00A0  ",
          FechaNac: " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente: " \u00A0 ",
          edad: " \u00A0 ",
          NombrePadre: " \u00A0 ",
          NombreMadre: " \u00A0  ",
          FechaNac: " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente: " \u00A0 ",
          edad: " \u00A0 ",
          NombrePadre: " \u00A0 ",
          NombreMadre: " \u00A0  ",
          FechaNac: " \u00A0 ",


        },
        {
          id: 1,
          NombrePaciente: " \u00A0 ",
          edad: " \u00A0 ",
          NombrePadre: " \u00A0 ",
          NombreMadre: " \u00A0  ",
          FechaNac: " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente: " \u00A0 ",
          edad: " \u00A0 ",
          NombrePadre: " \u00A0 ",
          NombreMadre: " \u00A0  ",
          FechaNac: " \u00A0 ",

        },
        {
          id: 1,
          NombrePaciente: " \u00A0 ",
          edad: " \u00A0 ",
          NombrePadre: " \u00A0 ",
          NombreMadre: " \u00A0  ",
          FechaNac: " \u00A0 ",

        },
      ],

      bebes: [], // Inicialmente la lista de bebés estará vacía
      paginatedBebes: [], // Lista de bebés a mostrar en la página actual
      message: '',
      paginaActual: 1,
      itemsPorPagina: 10, // Página actual



    };
  },
};
</script>


<style scoped>
/* Estilos para iconos de Font Awesome */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
</style>

<style>
/* Estilos para la tabla */
table {
  width: auto;
  border-collapse: collapse;
  margin-left: 0 auto;
  margin-right: 0 auto;
}

.router-link-custom {
  text-decoration: none;
  /* Elimina el subrayado */
  color: inherit;
  /* Usa el color heredado del padre */
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
</style>
