<template>
    <b-container fluid>
        <form @submit.prevent="submitForm">
            <b-row>
                <b-col lg="12">
                    <iq-card>
                        <template v-slot:headerTitle>
                            <h4 class="card-title">Editar datos del paciente</h4>
                        </template>

                        <template v-slot:body>
                            <div class="new-user-info">
                                <b-row>

                                    <input type="number" id="id" v-model="bebe.id" style="display: none;">

                                    <b-form-group class="col-md-4" label="Sexo:" label-for="sexo">
                                        <b-form-select id="sexo" v-model="bebe.sexo" required>
                                            <option value="">Seleccionar</option>
                                            <option value="Masculino">Masculino</option>
                                            <option value="Femenino">Femenino</option>
                                        </b-form-select>
                                    </b-form-group>




                                    <b-form-group class="col-md-4" label="Fecha de Nacimiento:"
                                        label-for="fechaNacimiento">
                                        <input type="date" id="fechaNacimiento" v-model="bebe.fecha_nacimiento"
                                            class="form-control mb-2" required>
                                    </b-form-group>

                                    <b-form-group class="col-md-4" label="Hora de nacimiento:"
                                        label-for="horaNacimiento">
                                        <input type="time" id="horaNacimiento" v-model="bebe.hora_nacimiento"
                                            class="form-control mb-2" required>
                                    </b-form-group>


                                    <b-form-group class="col-md-4" label="Lugar de nacimiento:"
                                        label-for="lugarNacimiento">
                                        <b-form-select id="lugarNacimiento" v-model="bebe.lugar_nacimiento" required>
                                            <option value="">Seleccionar</option>
                                            <option value="Xicotepec">Xicotepec</option>
                                            <option value="Huachinango">Huachinango</option>
                                            <!-- Agrega más opciones según sea necesario -->
                                        </b-form-select>
                                    </b-form-group>

                                    <b-form-group class="col-md-4" label="Peso:" label-for="peso">
                                        <input type="number" id="peso" step="0.01" v-model="bebe.peso"
                                            class="form-control mb-2" required>
                                    </b-form-group>

                                    <b-form-group class="col-md-4" label="Longitud:" label-for="longitud">
                                        <input type="number" id="longitud" step="0.01" v-model="bebe.longitud"
                                            class="form-control mb-2" required>
                                    </b-form-group>


                                    <b-form-group class="col-md-6" label="Nombre del padre:" label-for="nPadre">
                                        <input type="text" id="nPadre" v-model="bebe.nombre_padre"
                                            class="form-control mb-2" required>
                                    </b-form-group>


                                    <b-form-group class="col-md-6" label="Nombre de la madre:" label-for="nMadre">
                                        <input type="text" id="nMadre" v-model="bebe.nombre_madre"
                                            class="form-control mb-2" required>
                                    </b-form-group>


                                    <b-form-group class="col-md-6" label="Teléfono de contacto:"
                                        label-for="telefonoContacto">
                                        <input type="text" id="telefonoContacto" v-model="bebe.telefono_contacto"
                                            class="form-control mb-2" required>
                                    </b-form-group>

                                    <b-form-group class="col-md-6" label="Email de contacto:" label-for="emailC">
                                        <input type="email" id="emailC" v-model="bebe.email_contacto"
                                            class="form-control mb-2" required>
                                    </b-form-group>


                                    <b-form-group class="col-md-6" label="Observaciones:" label-for="observaciones">
                                        <textarea id="observaciones" v-model="bebe.observaciones"
                                            class="form-control mb-2"></textarea>
                                    </b-form-group>


                                    <b-form-group class="col-md-6" label="Tipo de nacimiento:"
                                        label-for="tipoNacimiento">
                                        <input type="text" id="tipoNacimiento" v-model="bebe.tipo_nacimiento"
                                            class="form-control mb-2">
                                    </b-form-group>

                                    <b-form-group class="col-md-3" label="Frecuencia cardíaca:"
                                        label-for="frecuenciaCardiaca">
                                        <input type="number" id="frecuenciaCardiaca" class="form-control mb-2"
                                            v-model="bebe.frecuencia_cardiaca">
                                    </b-form-group>


                                    <b-form-group class="col-md-3" label="Temperatura:" label-for="temperatura">
                                        <input type="number" id="temperatura" step="0.01" class="form-control mb-2"
                                            v-model="bebe.temperatura">
                                    </b-form-group>



                                    <b-form-group class="col-md-3" label="Presión Arterial Sistólica:"
                                        label-for="presionArterialSistolica">
                                        <input type="number" id="presionArterialSistolica" class="form-control mb-2"
                                            v-model="bebe.presion_arterial_sistolica">
                                    </b-form-group>


                                    <b-form-group class="col-md-3" label="Presión Arterial Diastólica:"
                                        label-for="presionArterialDiastolica">

                                        <input type="number" id="presionArterialDiastolica"
                                            v-model="bebe.presion_arterial_diastolica" class="form-control mb-2">
                                    </b-form-group>
                                    <!-- Agrega los demás campos de la tabla aquí -->

                                    <button variant="primary mt-2" type="submit">Guardar Cambios</button>
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
            bebe: {
                fecha_nacimiento: '',
                hora_nacimiento: '',
                lugar_nacimiento: '',
                peso: '',
                longitud: '',
                nombre_padre: '',
                nombre_madre: '',
                telefono_contacto: '',
                email_contacto: '',
                observaciones: '',
                tipo_nacimiento: '',
                frecuencia_cardiaca: '',
                temperatura: '',
                presion_arterial_sistolica: '',
                presion_arterial_diastolica: ''
            },
            message: ''
        };
    },
    mounted() {
        this.obtenerDatosBebe();
    },
    methods: {
        obtenerDatosBebe() {
            const id = this.$route.params.id;
            fetch(`http://localhost:8000/hospital/api/nacimientos/${id}/`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('No se pudieron obtener los datos del bebé.');
                    }
                    return response.json();
                })
                .then(data => {
                    this.bebe = data;
                })
                .catch(error => {
                    this.message = "Error al obtener los datos del bebé: " + error.message;
                });
        },
        submitForm() {
            this.message = "Guardando cambios...";
            const id = this.$route.params.id;

            fetch(`http://localhost:8000/hospital/api/nacimientos/${id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.bebe),
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('No se pudieron guardar los cambios.');
                    }
                    this.message = "¡Bebé editado exitosamente!";
                })
                .catch(error => {
                    this.message = "Error al guardar los cambios: " + error.message;
                });
        }
    }
};

</script>