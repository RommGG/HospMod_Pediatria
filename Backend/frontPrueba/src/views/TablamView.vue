<template>
    <div>
        <h1>Listado de pacientes</h1>
       
        <div v-if="message" style="margin-top: 10px;">
            {{ message }}
        </div>
        <table>
            <thead>
                <tr>
                    <th>Id del paciente</th>
                    <th>Sexo del paciente</th>
                    <th>Edad</th>
                    <th>Peso(KG)</th>
                    <th>Fecha de nacimiento</th>
                    <th>Acciones</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="(paciente, index) in paginatedpacientes" :key="index">
                    <td>{{ paciente.nombres }}</td>
                    <td>{{ paciente.sexo }}</td>
                    <td>{{ paciente.edad_anos }}</td>
                    <td>{{ paciente.peso }}</td>
                    <td>{{ paciente.fecha_nacimiento }}</td>
                    <td>
                        <button @click="eliminarpaciente(paciente._id)">
                            <i class="fas fa-trash-alt"></i> Eliminar
                        </button>
                        &nbsp;&nbsp;&nbsp;

                        <button style="margin-top: 5px;">
                            <router-link :to="{ name: 'editarm', params: { id: paciente._id } }"
                                class="router-link-custom">
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
            <button @click="paginar('siguiente')" :disabled="paginaActual * itemsPorPagina >= pacientes.length"
                style="background-color: black;">Siguiente</button>
        </div>

        <!-- Mostrar el número de página actual y el número total de páginas -->
        <div style="margin-top: 10px;">
            Página {{ paginaActual }} de {{ totalPages }}
        </div>
    </div>
</template>



<script>
/* eslint-disable */
export default {
    data() {
        return {
            pacientes: [], // la lista de bebés estará vacía
            paginatedpacientes: [], // Lista de bebés a mostrar en la página actual
            message: '',
            paginaActual: 1,
            itemsPorPagina: 10,
        };
    },
    computed: {
        totalPages() {
            return Math.ceil(this.totalpacientes.length / this.itemsPorPagina);
        },
        totalpacientes() {
            return this.pacientes;
        },
    },
    mounted() {
        // Cuando el componente se monta, cargar la lista de bebés desde la API
        this.obtenerpacientes();
    },
    methods: {

        obtenerpacientes() {
            fetch('http://127.0.0.1:8000/hospital/api/mongo/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Hubo un problema al obtener la lista de pacientes.');
                    }
                    return response.json();
                })
                .then(data => {
                    // Asignar la lista de bebés obtenida desde la API a la variable pacientes
                    this.pacientes = data;
                    // Llamar a la función para mostrar los primeros 10 datos
                    this.mostrarDatosPaginados();
                })
                .catch(error => {
                    this.message = "Error: " + error.message;
                });
        },
        eliminarpaciente(_id) {
            // Eliminar los caracteres adicionales del ID (por ejemplo, '${}' si existen)
            const id = _id.replace(/\${|}/g, '');

            console.log("Id que se debe eliminar:", id); // Agregar este console.log para depurar

            fetch(`http://127.0.0.1:8000/hospital/api/mongo/${id}/`, {
                method: 'DELETE'
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Hubo un problema al eliminar al paciente.');
                    }
                    this.message = "Paciente eliminado exitosamente!";
                    const id = this.pacientes[1]
                    console.log('Paciente Eliminado', id)
                    // Eliminar paciente de la lista después de eliminarlo en el backend
                    this.pacientes = this.pacientes.filter(paciente => paciente._id !== _id);
                    // Actualizar los datos paginados después de eliminar un paciente
                    this.mostrarDatosPaginados();
                })
                .catch(error => {
                    this.message = "Error: " + error.message;
                });
        }

        ,

        mostrarDatosPaginados() {
            const inicio = (this.paginaActual - 1) * this.itemsPorPagina;
            const fin = this.paginaActual * this.itemsPorPagina;
            this.paginatedpacientes = this.pacientes.slice(inicio, fin);
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