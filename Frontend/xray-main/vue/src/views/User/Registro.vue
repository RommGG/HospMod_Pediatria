<template>
  <b-container fluid>

    <form @submit.prevent="submitForm" v-validate>
      <b-row>
        <b-col lg="12">
          <iq-card>
            <template v-slot:headerTitle>
              <h4 class="card-title">Registrar un Nacimiento</h4>
            </template>
            <template v-slot:body>
              <div class="new-user-info">
                <b-row>
                  <b-form-group class="col-md-6" label="Nombre Completo Padre:" label-for="nombrePadre">
                    <input type="text" placeholder="Nombre del padre" class="form-control mb-2" id="nombrePadre"
                      v-model="nombrePadre">
                      <span v-if="errors.has('nombrePadre')" class="invalid-feedback">{{ errors.first('nombrePadre') }}</span>

                  </b-form-group>


                  <b-form-group class="col-md-6" label="Nombre Completo Madre:" label-for="nombreMadre">
                    <input type="text" id="nombreMadre" placeholder="Nombre de la madre" class="form-control mb-2"
                      v-model="nombreMadre">

                  </b-form-group>



                  <b-form-group class="col-md-6" label="Fecha de Nacimiento:" label-for="fechaNacimiento">
                    <input type="date" id="fechaNacimiento" placeholder="Fecha de nacimiento" class="form-control mb-2"
                      v-model="fechaNacimiento">

                  </b-form-group>




                  <b-form-group class="col-md-6" label="Hora de Nacimiento:" label-for="horaNacimiento">
                    <input type="time" id="horaNacimiento" placeholder="Hora de nacimiento" class="form-control mb-2"
                      v-model="horaNacimiento">
                  </b-form-group>

                  <b-form-group class="col-md-4" label="Lugar de nacimiento:" label-for="lugarNacimiento">
                    <b-form-select v-model="lugarNacimiento" id="lugarNacimiento">
                      <b-form-select-option :value="null" disabled selected>Seleccionar</b-form-select-option>
                      <b-form-select-option value="opcion1">Xicotepec</b-form-select-option>
                      <b-form-select-option value="opcion2">Huachinango</b-form-select-option>
                      <b-form-select-option value="opcion3">Villa Avila Camacho</b-form-select-option>
                      <b-form-select-option value="opcion3">Necaxa</b-form-select-option>

                    </b-form-select>
                  </b-form-group>

                  <b-form-group class="col-md-4" label="Sexo:" label-for="sexo">
                    <b-form-select v-model="sexo" id="sexo">
                      <b-form-select-option :value="null" disabled selected>Seleccionar</b-form-select-option>
                      <b-form-select-option value="opcion1">Masculino</b-form-select-option>
                      <b-form-select-option value="opcion2">Femenino</b-form-select-option>


                    </b-form-select>
                  </b-form-group>






                  <b-form-group class="col-md-4" label="Tipo de nacimiento:" label-for="tipoNacimiento">
                    <b-form-select v-model="tipoNacimiento" id="tipoNacimiento">
                      <b-form-select-option :value="null" disabled selected>Seleccionar</b-form-select-option>
                      <b-form-select-option value="opcion1">Normal</b-form-select-option>
                      <b-form-select-option value="opcion2">Cesarea</b-form-select-option>


                    </b-form-select> 
                  </b-form-group>


                  <b-form-group class="col-md-4" label="Peso:" label-for="peso">
                    <input type="number" id="peso" v-model="peso" step="0.01" placeholder="Peso"
                      class="form-control mb-2">
                  </b-form-group>

                  <b-form-group class="col-md-4" label="Longitud:" label-for="longitud">
                    <input type="number" id="longitud" v-model="longitud" step="0.01" placeholder="Longitud"
                      class="form-control mb-2">
                  </b-form-group>



                  <b-form-group class="col-md-4" label="Temperatura:" label-for="temperatura">
                    <input type="number" id="temperatura" placeholder="Temperatura" class="form-control mb-2"
                      v-model="temperatura" step="0.01">

                  </b-form-group>

                  <!-- <b-form-group class="col-md-4" label="Temperatura:" label-for="mobno">
                    <Field class="form-control mb-2"  type="text" placeholder="Temperatura (°C)"
                      name="MobileNo" :rules="isRequire" :class="{ 'is-invalid': errors.MobileNo }"></Field>
                  </b-form-group> -->



                  <b-form-group class="col-md-4" label="Frecuencia Cardiaca:" label-for="frecuenciaCardiaca">
                    <input type="number" id="frecuenciaCardiaca" placeholder="Frecuencia cardiaca"
                      class="form-control mb-2" v-model="frecuenciaCardiaca">
                  </b-form-group>



                  <b-form-group class="col-md-4" label="Presión Arterial Sistólica:"
                    label-for="presionArterialSistolica">
                    <input type="number" id="presionArterialSistolica" v-model="presionArterialSistolica"
                      placeholder="Presión arteral sistólica" class="form-control mb-2">
                  </b-form-group>



                  <b-form-group class="col-md-4" label="Presión Arterial Distólica:"
                    label-for="presionArterialDiastolica">
                    <input type="number" id="presionArterialDiastolica" v-model="presionArterialDiastolica"
                      placeholder="Presión arteral distólica" class="form-control mb-2">

                  </b-form-group>



                  <b-form-group class="col-md-6" label="Numero Telefonico:" label-for="telefonoContacto">
                    <input type="text" id="telefonoContacto" v-model="telefonoContacto"
                      placeholder="Telefonó de contacto" class="form-control mb-2">

                  </b-form-group>




                  <b-form-group class="col-md-6" label="Email de Contacto:" label-for="emailContacto">
                    <input type="email" id="emailContacto" v-model="emailContacto" placeholder="Email de contacto"
                      class="form-control mb-2">
                  </b-form-group>




                  <b-form-group class="col-md-12" label="Observaciones:" label-for="observaciones">
                    <textarea id="observaciones" v-model="observaciones" laceholder="Observaciones"
                      class="form-control mb-2"></textarea>
                  </b-form-group>




                  





                  <b-button variant="primary mt-2" type="submit">Crear Nuevo Registro</b-button>



                </b-row>
                <hr />

              </div>
            </template>
          </iq-card>
        </b-col>



        <!-- <b-col md="12">
          <iq-card>
            <template v-slot:headerTitle>
              <h4 class="card-title">Ultimos registros</h4>
            </template>
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
                      <td>{{ items.Nombre }}</td>
                      <td>{{ items.tConsulta }}</td>
                      <td>{{ items.Observaciones }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </template>
          </iq-card>
        </b-col> -->


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
      tipoNacimiento: 'normal',
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
