<!-- ConView.vue -->
<template>
    <div>
        <div>
          <h2>
            <p>Total de pacientes en mysql:</p>
            <p v-if="totalpSql !== null">{{ totalpSql }}</p>
            <p v-else>Cargando...</p>
          </h2>
        </div>
        <div>
          <h2>
            <p>Total de pacientes en mongo:</p>
            <p v-if="totalpMongo !== null">{{ totalpMongo }}</p>
            <p v-else>Cargando...</p>
          </h2>
        </div>
    </div>
  </template>
  

<script>


/*eslint-disable*/

export default {

    data() {
        return {
            bebes: [],
            paginatedBebes: [],
            message: '',
            paginaActual: 1,
            itemsPorPagina: 10,
            totalpSql: null,
            totalpMongo: null
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
        //   this.obtenerBebes();
        this.obtenerTotalSQL();
        this.obtenertotalpMongo();

        setInterval(this.obtenertotalpMongo, 2000)
        // No es recomendable hacer peticiones tan frecuentes, esto es solo para ejemplo.
        setInterval(this.obtenerTotalSQL, 2000);
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
                    this.totalpMongo = data.cantidad; // Asegúrate de que el campo coincida con lo que devuelve tu API
                })
                .catch(error => {
                    this.totalpMongo = 'Error al obtener los datos';
                });
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
                    if (Array.isArray(data) && data.length > 0) {
                        // Acceder al primer elemento del array y obtener el valor de total_pacientes
                        this.totalpSql = data[0].total_pacientes;
                    } else {
                        throw new Error('No se encontraron datos válidos');
                    }
                })
                .catch(error => {
                    this.totalpSql = 'Error al obtener los datos';
                });
        },
    }
}

</script>

<style>
  
</style>
