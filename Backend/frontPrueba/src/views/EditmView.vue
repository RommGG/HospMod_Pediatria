<template>
  <div>
    <h1>Actualizar Datos</h1>
    <div v-if="message" style="margin-top: 10px;">
      {{ message }}
    </div>
    <form @submit.prevent="submitForm">
      <label for="nombrep">Nombre:</label>
      <input type="text" id="nombrep" v-model="paciente.nombres">
      <br>
      <label for="apellidop">Apellido Paterno:</label>
      <input type="text" id="apellidop" v-model="paciente.apellidop">
      <br>
      <label for="apellidom">Apellido Materno:</label>
      <input type="text" id="apellidom" v-model="paciente.apellidom">
      <br>
      <label for="fechaNacimiento">Fecha de Nacimiento:</label>
      <input type="date" id="fechaNacimiento" v-model="paciente.fecha_nacimiento">
      <br>
      <label for="edad">Edad:</label>
      <input type="number" id="edad" v-model="paciente.edad_anos" >
      <br>
      <label for="peso">Peso:</label>
      <input type="number" id="peso" v-model="paciente.peso" step="0.1">
      <br>
      <label for="longitud">Longitud:</label>
      <input type="number" id="longitud" v-model="paciente.longitud" step="0.1">
      <br>
      <label for="perimetroCraneal">Perímetro Craneal:</label>
      <input type="number" id="perimetroCraneal" v-model="paciente.perimetro_craneal" step="0.1">
      <br>
      <label for="temperatura">Temperatura:</label>
      <input type="number" id="temperatura" step="0.1" v-model="paciente.temperatura" >
      <br>
      <label for="frecuenciaRespiratoria">Frecuencia Respiratoria:</label>
      <input type="number" id="frecuenciaRespiratoria" v-model="paciente.frecuencia_respiratoria">
      <br>
      <label for="frecuenciaCardiaca">Frecuencia Cardíaca:</label>
      <input type="number" id="frecuenciaCardiaca" v-model="paciente.frecuencia_cardiaca">
      <br>
      <label for="presionSistolica">Presión Arterial Sistólica:</label>
      <input type="number" id="presionSistolica" v-model="paciente.presion_arteria_sistolica">
      <br>
      <label for="presionDiastolica">Presión Arterial Diastólica:</label>
      <input type="number" id="presionDiastolica" v-model="paciente.presion_arteria_diastolica">
      <br>
      <div v-for="(vacuna, index) in paciente.vacunas_administradas" :key="index">
        <label :for="'vacuna_' + index">Vacuna {{ index + 1 }}:</label>
        <input type="text" :id="'vacuna_' + index" v-model="paciente.vacunas_administradas[index]">
        <button type="button" @click="eliminarVacuna(index)" v-if="index > 2">Eliminar</button>
      </div>
      <button type="button" @click="agregarVacuna">Agregar Vacuna</button>
      
      <div v-for="(cita, index) in paciente.citas" :key="index">
        <label :for="'cita_' + index">Cita {{ index + 1 }}:</label>
        <input type="date" :id="'cita_' + index" :value="cita" @input="actualizarCita($event, index)">
        <button type="button" @click="eliminarCita(index)" v-if="index > 2">Eliminar</button>
      </div>
      <button type="button" @click="agregarCita">Agregar Cita</button>
      <br>

      
      <div v-for="(examen, index) in paciente.examenes_medicos_realizados" :key="index">
        <label :for="'examen_' + index">Examen {{ index + 1 }}:</label>
        <input type="text" :id="'examen_' + index" v-model="paciente.examenes_medicos_realizados[index]">
        <button type="button" @click="eliminarExamen(index)" v-if="index > 2">Eliminar</button>
      </div>
      <button type="button" @click="agregarExamen">Agregar Examen</button>
      <br>
      <label for="observaciones">Observaciones:</label>
      <textarea id="observaciones" v-model="paciente.observaciones"></textarea>
      <br>

      <button type="submit">Actualizar</button>
    </form>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data() {
    return {
      paciente: {
        sexo: '',
        apellidop: '',
        apellidom: '',
        nombres: '',
        fecha_nacimiento: '',
        fecha_ultima_cita: '',
        edad_anos: 0,
        peso: 0,
        longitud: 0,
        perimetro_craneal: 0,
        temperatura: 0,
        frecuencia_respiratoria: 0,
        frecuencia_cardiaca: 0,
        presion_arteria_sistolica: 0,
        presion_arteria_diastolica: 0,
        vacunas_administradas: [],
        citas: [],
        examenes_medicos_realizados: [],
        observaciones: ''
      },
      message: ''
    };
  },
  mounted() {
    this.obtenerDatosPaciente();
  },
  methods: {

    agregarVacuna() {
      this.paciente.vacunas_administradas.push('');
    },
    // Método para eliminar una vacuna
    eliminarVacuna(index) {
      this.paciente.vacunas_administradas.splice(index, 1);
    },
    
    agregarCita() {
        this.citas.push('');
      },
      eliminarCita(index) {
        this.citas.splice(index, 1);
      },

      actualizarCita(event, index) {
        this.citas[index] = event.target.value;
      },


    // Método para agregar un examen médico
    agregarExamen() {
      this.paciente.examenes_medicos_realizados.push('');
    },
    // Método para eliminar un examen médico
    eliminarExamen(index) {
      this.paciente.examenes_medicos_realizados.splice(index, 1);
    },

    obtenerDatosPaciente() {
      const id = this.$route.params.id;
      fetch(`http://localhost:8000/hospital/api/mongo/${id}/`)
        .then(response => {
          if (!response.ok) {
            throw new Error('No se pudieron obtener los datos del paciente.');
          }
          return response.json();
        })
        .then(data => {
          // Mapear los datos de la respuesta de la API al objeto paciente
          this.paciente.sexo = data.sexo;
          this.paciente.apellidop = data.apellidop;
          this.paciente.apellidom = data.apellidom;
          this.paciente.nombres = data.nombres;
          this.paciente.fecha_nacimiento = data.fecha_nacimiento;
          this.paciente.fecha_ultima_cita = data.fecha_ultima_cita;
          this.paciente.edad_anos = data.edad_anos;
          this.paciente.peso = data.peso;
          this.paciente.longitud = data.longitud;
          this.paciente.perimetro_craneal = data.perimetro_craneal;
          this.paciente.temperatura = data.temperatura;
          this.paciente.frecuencia_respiratoria = data.frecuencia_respiratoria;
          this.paciente.frecuencia_cardiaca = data.frecuencia_cardiaca;
          this.paciente.presion_arteria_sistolica = data.presion_arteria_sistolica;
          this.paciente.presion_arteria_diastolica = data.presion_arteria_diastolica;
          this.paciente.vacunas_administradas = data.vacunas_administradas;
          this.paciente.citas = data.citas;
          this.paciente.examenes_medicos_realizados = data.examenes_medicos_realizados;
          this.paciente.observaciones = data.observaciones;
        })
        .catch(error => {
          this.message = "Error al obtener los datos del paciente: " + error.message;
        });
    },
    submitForm() {
      this.message = "Guardando cambios...";
      const id = this.$route.params.id;
      
      fetch(`http://localhost:8000/hospital/api/mongo/${id}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.paciente),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('No se pudieron guardar los cambios.');
        }
        this.message = "¡Paciente editado exitosamente!";
      })
      .catch(error => {
        this.message = "Error al guardar los cambios: " + error.message;
      });
    }
  }
}
</script>
