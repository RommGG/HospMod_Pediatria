<template>
    <div>
      <div v-if="mensaje">{{ mensaje }}</div>
      <h1>Insertar Datos</h1>
      <form @submit.prevent="insertarDatos">
        <label for="nombres">Nombre(s)</label>
        <input type="text" id="nombres" v-model="nombres">
        <br>
        <label for="apellidop">Apellido Paterno</label>
        <input type="text" id="apellidop" v-model="apellidop">
        <br>
        <label for="apellidom">Apellido Materno</label>
        <input type="text" id="apellidom" v-model="apellidom">
        <br>
        <label for="sexo">Sexo :</label><br>
        <select id="sexo" v-model="sexo" required>
          <option value="">Seleccionar</option>
          <option value="Masculino">Masculino</option>
          <option value="Femenino">Femenino</option>
        </select><br>
        <br>
        <label for="fecha_nacimiento">Fecha de Nacimiento:</label>
        <input type="date" id="fecha_nacimiento" v-model="fechaNacimiento">
        <br>

        <label for="edad_anos">Edad (años):</label>
        <input type="number" id="edad_anos" v-model="edadAnos">
        <br>
        <label for="peso">Peso (kg):</label>
        <input type="number" id="peso" step="0.1" v-model="peso">
        <br>
        <label for="longitud">Longitud (cm):</label>
        <input type="number" id="longitud" step="0.1" v-model="longitud">
        <br>
        <label for="perimetro_craneal">Perímetro Craneal (cm):</label>
        <input type="number" id="perimetro_craneal" step="0.1" v-model="perimetroCraneal">
        <br>
        <label for="temperatura">Temperatura (°C):</label>
        <input type="number" id="temperatura" step="0.1" v-model="temperatura">
        <br>
        <label for="frecuencia_respiratoria">Frecuencia Respiratoria:</label>
        <input type="number" id="frecuencia_respiratoria" v-model="frecuenciaRespiratoria">
        <br>
        <label for="frecuencia_cardiaca">Frecuencia Cardíaca:</label>
        <input type="number" id="frecuencia_cardiaca" v-model="frecuenciaCardiaca">
        <br>
        <label for="presion_arteria_sistolica">Presión Arterial Sistólica:</label>
        <input type="number" id="presion_arteria_sistolica" v-model="presionArterialSistolica">
        <br>
        <label for="presion_arteria_diastolica">Presión Arterial Diastólica:</label>
        <input type="number" id="presion_arteria_diastolica" v-model="presionArterialDiastolica">
        <br>
        <div v-for="(vacuna, index) in vacunas" :key="index">
          <label :for="'vacuna_' + index">Vacuna {{ index + 1 }}:</label>
          <input type="text" :id="'vacuna_' + index" :value="vacuna" @input="actualizarVacuna($event, index)">
          <button type="button" @click="eliminarVacuna(index)" v-if="index > 2">Eliminar</button>
        </div>
        <button type="button" @click="agregarVacuna">Agregar Vacuna</button>
        <br>

        <div v-for="(cita, index) in citas" :key="index">
          <label :for="'cita_' + index">Cita {{ index + 1 }}:</label>
          <input type="date" :id="'cita_' + index" :value="cita" @input="actualizarCita($event, index)">
          <button type="button" @click="eliminarCita(index)" v-if="index > 2">Eliminar</button>
        </div>
        <button type="button" @click="agregarCita">Agregar Cita</button>
        <br>

      
        <div v-for="(examen, index) in examenes" :key="index">
          <label :for="'examen_' + index">Examen {{ index + 1 }}:</label>
          <input type="text" :id="'examen_' + index" :value="examen" @input="actualizarExamen($event, index)">
          <button type="button" @click="eliminarExamen(index)" v-if="index > 2">Eliminar</button>
        </div>
        <button type="button" @click="agregarExamen">Agregar Examen</button>
        <br>
        <label for="observaciones">Observaciones:</label>
        <textarea id="observaciones" v-model="observaciones"></textarea>
        <br>
        <label for="fecha_ultima_cita">Fecha de la ultima cita:</label>
        <input type="date" id="fecha_ultima_cita" v-model="fecha_ultima_cita">
        <br>
        


        <button type="submit">Insertar</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        nombres :'',
        apellidop:'',
        apellidom:'',
        sexo:'',
        fechaNacimiento: '',
        fecha_ultima_cita:'',
        edadAnos: null,
        peso: null,
        longitud: null,
        perimetroCraneal: null,
        temperatura: null,
        frecuenciaRespiratoria: null,
        frecuenciaCardiaca: null,
        presionArterialSistolica: null,
        presionArterialDiastolica: null,
        vacunas: [''],
        citas:[''],
        examenes: [''],
        observaciones: '',
        mensaje: ''
      };
    },
    methods: {
      insertarDatos() {
        const data = {
          nombres :this.nombres,
          apellidop:this.apellidop,
          apellidom:this.apellidom,
          sexo:this.sexo,
          fecha_nacimiento: this.fechaNacimiento,
          fecha_ultima_cita:this.fecha_ultima_cita,
          edad_anos: this.edadAnos,
          peso: this.peso,
          longitud: this.longitud,
          perimetro_craneal: this.perimetroCraneal,
          temperatura: this.temperatura,
          frecuencia_respiratoria: this.frecuenciaRespiratoria,
          frecuencia_cardiaca: this.frecuenciaCardiaca,
          presion_arteria_sistolica: this.presionArterialSistolica,
          presion_arteria_diastolica: this.presionArterialDiastolica,
          vacunas_administradas: this.vacunas.filter(vacuna => vacuna.trim() !== ''),
          citas: this.citas.filter(cita => cita.trim() !== ''),
          examenes_medicos_realizados: this.examenes.filter(examen => examen.trim() !== ''),
          observaciones: this.observaciones
        };
  
        fetch('http://127.0.0.1:8000/hospital/api/mongo/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })
        .then(response => {
          if (response.ok) {
            this.mensaje = 'Datos insertados correctamente.';
            this.limpiarCampos();
          } else {
            this.mensaje = 'Error al insertar los datos.';
          }
        })
        .catch(error => {
          this.mensaje = 'Error al insertar los datos.';
          console.error(error);
        });
      },
      agregarVacuna() {
        this.vacunas.push('');
      },
      eliminarVacuna(index) {
        this.vacunas.splice(index, 1);
      },
      actualizarVacuna(event, index) {
        this.vacunas[index] = event.target.value;
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





      agregarExamen() {
        this.examenes.push('');
      },
      eliminarExamen(index) {
        this.examenes.splice(index, 1);
      },

      actualizarExamen(event, index) {
        this.examenes[index] = event.target.value;
      },
      limpiarCampos() {
        this.nombres ='',
        this.apellidop='',
        this.apellidom='',
        this.sexo='',
        this.fechaNacimiento = '',
        this.fecha_ultima_cita = '',
        this.edadAnos = null;
        this.peso = null;
        this.longitud = null;
        this.perimetroCraneal = null;
        this.temperatura = null;
        this.frecuenciaRespiratoria = null;
        this.frecuenciaCardiaca = null;
        this.presionArterialSistolica = null;
        this.presionArterialDiastolica = null;
        this.vacunas = [''];
        this.examenes = [''];
        this.citas = [''];
        this.observaciones = '';
      }
    }
  };
  </script>
  
  <style scoped>
  /* Estilos CSS específicos del componente */
  </style>
  