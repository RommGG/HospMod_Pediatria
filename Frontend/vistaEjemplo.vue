<template>
    <div>
      <h2>Registro de Bebé</h2>
  
        <div v-if="message" style="margin-top: 10px;">
          {{ message }}
        </div>
      <form @submit.prevent="submitForm">
          <label for="sexo">Sexo :</label><br>
          <input type="text" id="sexo" v-model="sexo" required><br><br>
  
          <label for="fechaNacimiento">Fecha de Nacimiento:</label><br>
          <input type="date" id="fechaNacimiento" v-model="fechaNacimiento"><br><br>
          
          <label for="horaNacimiento">Hora de Nacimiento:</label><br>
          <input type="time" id="horaNacimiento" v-model="horaNacimiento"><br><br>
          
          <label for="lugarNacimiento">Lugar de Nacimiento:</label><br>
          <select id="lugarNacimiento" v-model="lugarNacimiento">
            <option value="">Seleccionar</option>
            <option value="opcion1">Xicotepec</option>
            <option value="opcion2">Huachinango</option>
            <option value="opcion3"></option>
          </select><br><br>
          
          
          <label for="peso">Peso (kg):</label><br>
          <input type="number" id="peso" v-model="peso" step="0.01"><br><br>
          
          <label for="longitud">Longitud (cm):</label><br>
          <input type="number" id="longitud" v-model="longitud" step="0.01"><br><br>
          
          <label for="nombrePadre">Nombre del Padre:</label><br>
          <input type="text" id="nombrePadre" v-model="nombrePadre"><br><br>
          
          <label for="nombreMadre">Nombre de la Madre:</label><br>
          <input type="text" id="nombreMadre" v-model="nombreMadre"><br><br>
          
          <label for="telefonoContacto">Teléfono de Contacto:</label><br>
          <input type="text" id="telefonoContacto" v-model="telefonoContacto"><br><br>
          
          <label for="emailContacto">Email de Contacto:</label><br>
          <input type="email" id="emailContacto" v-model="emailContacto"><br><br>
          
          <label for="observaciones">Observaciones:</label><br>
          <textarea id="observaciones" v-model="observaciones"></textarea><br><br>
          
          <label for="tipoNacimiento">Tipo de Nacimiento:</label><br>
          <select id="tipoNacimiento" v-model="tipoNacimiento">
            <option value="normal">Normal</option>
            <option value="cesarea">Cesárea</option>
          </select><br><br>
          
          <label for="frecuenciaCardiaca">Frecuencia Cardíaca:</label><br>
          <input type="number" id="frecuenciaCardiaca" v-model="frecuenciaCardiaca"><br><br>
          
          <label for="temperatura">Temperatura (°C):</label><br>
          <input type="number" id="temperatura" v-model="temperatura" step="0.01"><br><br>
          
          <label for="presionArterialSistolica">Presión Arterial Sistólica:</label><br>
          <input type="number" id="presionArterialSistolica" v-model="presionArterialSistolica"><br><br>
          
          <label for="presionArterialDiastolica">Presión Arterial Diastólica:</label><br>
          <input type="number" id="presionArterialDiastolica" v-model="presionArterialDiastolica"><br><br>
          
          <button type="submit">Registrar Bebé</button>
      </form>
  
    </div>
  </template>

  <script>
/* eslint-disable */

/*Esta parte del codigo es para conectarse a la api*/
export default {
  data() {
    return {
      sexo:'',
      fechaNacimiento: '',
      horaNacimiento: '',
      lugarNacimiento: '',
      peso: null,
      longitud: null,
      nombrePadre: '',
      nombreMadre: '',
      telefonoContacto: '',
      emailContacto: '',
      observaciones: '',
      tipoNacimiento: 'normal',
      frecuenciaCardiaca: null,
      temperatura: null,
      presionArterialSistolica: null,
      presionArterialDiastolica: null,
      message: ''
    }
  },
  methods: {
    submitForm() {
      let data = {
        sexo: this.sexo,
        fecha_nacimiento: this.fechaNacimiento,
        hora_nacimiento: this.horaNacimiento,
        lugar_nacimiento: this.lugarNacimiento,
        peso: this.peso,
        longitud: this.longitud,
        nombre_padre: this.nombrePadre,
        nombre_madre: this.nombreMadre,
        telefono_contacto: this.telefonoContacto,
        email_contacto: this.emailContacto,
        observaciones: this.observaciones,
        tipo_nacimiento: this.tipoNacimiento,
        frecuencia_cardiaca: this.frecuenciaCardiaca,
        temperatura: this.temperatura,
        presion_arterial_sistolica: this.presionArterialSistolica,
        presion_arterial_diastolica: this.presionArterialDiastolica
      };

      fetch('http://127.0.0.1:8000/hospital/api/v1nacimientos/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Hubo un problema al registrar el bebé.');
        }
        return response.json();
      })
      .then(data => {
        this.message = "¡Bebé registrado exitosamente!";
        // Limpiar los campos del formulario después del registro exitoso
        this.resetForm();
      })
      .catch(error => {
        this.message = "Error: " + error.message;
      });
    },
    resetForm() {
      // Reinicia todos los campos del formulario después del registro exitoso
      this.sexo = '';
      this.fechaNacimiento = '';
      this.horaNacimiento = '';
      this.lugarNacimiento = '';
      this.peso = null;
      this.longitud = null;
      this.nombrePadre = '';
      this.nombreMadre = '';
      this.telefonoContacto = '';
      this.emailContacto = '';
      this.observaciones = '';
      this.tipoNacimiento = '';
      this.frecuenciaCardiaca = null;
      this.temperatura = null;
      this.presionArterialSistolica = null;
      this.presionArterialDiastolica = null;
    }
  }
}
</script>
