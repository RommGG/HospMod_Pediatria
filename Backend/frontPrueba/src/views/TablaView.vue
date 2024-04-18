<template>
  <div>
    <div v-if="message" style="margin-top: 10px;">
      {{ message }}
    </div>

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
              <router-link :to="{ name: 'editar', params: { id: bebe.id }}" class="router-link-custom">
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
</template>

<script>
export default {
  data() {
    return {
      bebes: [], 
      paginatedBebes: [], // Lista de bebés a mostrar en la página actual
      message: '',
      paginaActual: 1,
      itemsPorPagina: 10,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.totalBebes.length / this.itemsPorPagina);
    },
    totalBebes() {
      return this.bebes;
    },
  },
  mounted() {
    // Cuando el componente se monta, cargar la lista de bebés desde la API
    this.obtenerBebes();
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
    }
  }
}
</script>

<style scoped>
/* Estilos para iconos de Font Awesome */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
</style>

<style>
/* Estilos para la tabla */
table {
  width: 80%;
  border-collapse: collapse;
  margin-left: 0 auto;
  margin-right: 0 auto;
}

.router-link-custom {
  text-decoration: none; /* Elimina el subrayado */
  color: inherit; /* Usa el color heredado del padre */
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
