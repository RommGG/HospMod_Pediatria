<template>
  <b-container fluid>
    <form @submit.prevent="submitForm">
      <b-row>
        <b-col lg="12">
          <iq-card>
            <template v-slot:headerTitle>
              <h4 class="card-title">Registrar un Nacimiento</h4>
            </template>

            <template v-slot:body>
              <div class="new-user-info">
                <b-row>

                  <b-form-group class="col-md-4" label="Sexo:" label-for="sexo">

                    <b-form-select v-model="sexo" id="sexo" required>
                      <option :value="null" disabled selected>Seleccionar</option>
                      <option value="Masculino">Masculino</option>
                      <option value="Femenino">Femenino</option>
                    </b-form-select>
                  </b-form-group>

                  <b-form-group class="col-md-4" label="Fecha de Nacimiento:" label-for="fechaNacimiento">
                    <input type="date" id="fechaNacimiento" v-model="fechaNacimiento" class="form-control mb-2">
                  </b-form-group>

                  <b-form-group class="col-md-4" label="Hora de Nacimiento:" label-for="horaNacimiento">
                    <input type="time" id="horaNacimiento" v-model="horaNacimiento" class="form-control mb-2">
                  </b-form-group>

                  <b-form-group class="col-md-4" label="Lugar de nacimiento:" label-for="lugarNacimiento">
                    <b-form-select id="lugarNacimiento" v-model="lugarNacimiento">
                      <option :value="null" disabled selected>Seleccionar</option>
                      <option value="Xicotepec">Xicotepec</option>
                      <option value="Huachinango">Huachinango</option>
                      <option value="Villa Avila Camacho">Villa Avila Camacho</option>
                      <option value="Necaxa">Necaxa</option>
                    </b-form-select>
                  </b-form-group>


                  <b-form-group class="col-md-4" label="Peso:" label-for="peso">
                    <input type="number" id="peso" v-model="peso" step="0.01" placeholder="Peso"
                      class="form-control mb-2">
                  </b-form-group>
                  <b-form-group class="col-md-4" label="Longitud:" label-for="longitud">
                    <input type="number" id="longitud" v-model="longitud" step="0.01" class="form-control mb-2">
                  </b-form-group>

                  <b-form-group class="col-md-6" label="Nombre Completo Padre:" label-for="nombrePadre">
                    <input type="text" id="nombrePadre" v-model="nombrePadre" class="form-control mb-2">
                  </b-form-group>

                  <b-form-group class="col-md-6" label="Nombre Completo Madre:" label-for="nombreMadre">
                    <input type="text" id="nombreMadre" v-model="nombreMadre" class="form-control mb-2">
                  </b-form-group>



                  <b-form-group class="col-md-6" label="Numero Telefonico:" label-for="telefonoContacto">
                    <input type="text" id="telefonoContacto" v-model="telefonoContacto" class="form-control mb-2">
                  </b-form-group>

                  <b-form-group class="col-md-6" label="Email de Contacto:" label-for="emailContacto">
                    <input type="email" id="emailContacto" v-model="emailContacto" class="form-control mb-2">
                  </b-form-group>

                  <b-form-group class="col-md-6" label="Observaciones:" label-for="observaciones">
                    <textarea id="observaciones" v-model="observaciones" class="form-control mb-2"></textarea>
                  </b-form-group>


                  <b-form-group class="col-md-6" label="Tipo de nacimiento:" label-for="tipoNacimiento">
                    <b-form-select id="tipoNacimiento" v-model="tipoNacimiento">
                      <option value="normal">normal</option>
                      <option value="cesarea">cesarea</option>
                    </b-form-select>
                  </b-form-group>


                  <b-form-group class="col-md-3" label="Frecuencia Cardiaca:" label-for="frecuenciaCardiaca">
                    <input type="number" id="frecuenciaCardiaca" v-model="frecuenciaCardiaca" class="form-control mb-2">
                  </b-form-group>

                  <b-form-group class="col-md-3" label="Temperatura:" label-for="temperatura">
                    <input type="number" id="temperatura" v-model="temperatura" step="0.01" class="form-control mb-2">
                  </b-form-group>



                  <b-form-group class="col-md-3" label="Presión Arterial Sistólica:"
                    label-for="presionArterialSistolica">
                    <input type="number" id="presionArterialSistolica" v-model="presionArterialSistolica"
                      class="form-control mb-2">

                  </b-form-group>


                  <b-form-group class="col-md-3" label="Presión Arterial Distólica:"
                    label-for="presionArterialDiastolica">
                    <input type="number" id="presionArterialDiastolica" v-model="presionArterialDiastolica"
                      class="form-control mb-2">

                  </b-form-group>
                  <b-button variant="primary mt-2" type="submit">Registrar Bebé</b-button>
                </b-row>
              </div>
            </template>
          </iq-card>
        </b-col>

      </b-row>
    </form>





  </b-container>
</template>


<script>
/*eslint-disable*/
import { xray } from "../../config/pluginInit";
import iqCard from "../../components/xray/cards/iq-card";

import { Form } from "vee-validate";


export default {
  name: "AddUser",
  components: { iqCard, Form },


  data() {
    return {
      sexo: '',
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
      tipoNacimiento: '',
      frecuenciaCardiaca: null,
      temperatura: null,
      presionArterialSistolica: null,
      presionArterialDiastolica: null,
      message: ''
    }
  },

  mounted() {
    xray.index();
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

      fetch('http://127.0.0.1:8000/hospital/api/nacimientos/', {
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
};

</script>
