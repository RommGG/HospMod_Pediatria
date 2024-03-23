<template>
  <b-container fluid>
    <Form @submit="onSubmit()" :validation-schema="schema" v-slot="{ errors }">
      <b-row>
        <b-col lg="12">
          <iq-card>
            <template v-slot:headerTitle>
              <h4 class="card-title">Registrar un Nacimiento</h4>
            </template>
            <template v-slot:body>
              <div class="new-user-info">
                <b-row>
                  <b-form-group class="col-md-6" label="Nombre Completo Padre:" label-for="PadreName">
                    <Field type="text" placeholder="Nombre" class="form-control mb-2"
                      name="FirstName" :rules="isRequire" :class="{ 'is-invalid': errors.FirstName }" />                 
                  </b-form-group>


                  <b-form-group class="col-md-6" label="Nombre Completo Madre:" label-for="MadreName">
                    <Field type="text" class="form-control mb-2" placeholder="Nombre"
                      :rules="isRequire" name="LastName" :class="{ 'is-invalid': errors.LastName }" />
                  </b-form-group>



                  <b-form-group class="col-md-6" label="Fecha de Nacimiento:" label-for="add1">
                    <Field class="form-control mb-2"  type="date" name="Address1"
                      placeholder="Fecha" :rules="isRequire" :class="{ 'is-invalid': errors.Address1 }" />
                  </b-form-group>




                  <b-form-group class="col-md-6" label="Hora de Nacimiento:" label-for="add2">
                    <Field class="form-control mb-2" type="time" name="Address2" id="add2"
                      placeholder="Street Address 2" :rules="isRequire" :class="{ 'is-invalid': errors.Address2 }">
                    </Field>
                  </b-form-group>



                  <b-form-group class="col-md-4" label="Peso:" label-for="dname">
                    <Field class="form-control mb-2"  type="text" name="DepartmentName"
                      id="dname" placeholder="Peso" :rules="isRequire" :class="{ 'is-invalid': errors.DepartmentName }">
                    </Field>
                  </b-form-group>



                  <b-form-group class="col-md-4" label="Temperatura:" label-for="mobno">
                    <Field class="form-control mb-2"  type="number" placeholder="Temperatura (°C)"
                      name="mobno" :rules="isRequire" :class="{ 'is-invalid': errors.mobno }"></Field>
                  </b-form-group>

                  <!-- <b-form-group class="col-md-4" label="Temperatura:" label-for="mobno">
                    <Field class="form-control mb-2"  type="text" placeholder="Temperatura (°C)"
                      name="MobileNo" :rules="isRequire" :class="{ 'is-invalid': errors.MobileNo }"></Field>
                  </b-form-group> -->



                  <b-form-group class="col-md-4" label="Frecuencia Cardiaca:" label-for="mobno">
                    <Field class="form-control"  type="text"
                      placeholder="Frecuencia Cardiaca" name="Alt_ContactNO" :rules="isRequire"
                      :class="{ 'is-invalid': errors.Alt_ContactNO }"></Field>
                  </b-form-group>



                  <b-form-group class="col-md-6" label="Presion Arterial Sistolica:" label-for="uname">
                    <Field class="form-control mb-2"  type="text"
                      placeholder="Presion Arterial Sistolica" name="Email" :rules="isRequire"
                      :class="{ 'is-invalid': errors.Email }"></Field>                    
                  </b-form-group>



                  <b-form-group class="col-md-6" label="Presion Arterial Distolica:" label-for="pno">
                    <Field class="form-control mb-2"  type="text" name="pincode" id="pno"
                      placeholder="Presion Arterial Distolica" :rules="isRequire"
                      :class="{ 'is-invalid': errors.pincode }"></Field>                   
                  </b-form-group>



                  <b-form-group class="col-md-12" label="Numero Telefonico:" label-for="MobileNo">
                    <Field class="form-control mb-2"  type="number" placeholder="Ingrese su numero de telefono"
                      name="MobileNo" :rules="isRequire" :class="{ 'is-invalid': errors.MobileNo }"></Field>
                  </b-form-group>




                  <b-form-group class="col-md-12" label="Email de Contacto:" label-for="emai">
                    <Field class="form-control mb-2"  type="email" name="email" id="email"
                      placeholder="Email de Contacto" :rules="isRequire" :class="{ 'is-invalid': errors.email }"></Field>                    
                  </b-form-group>




                  <b-form-group class="col-md-12" label="Observaciones:" label-for="city">
                    <Field class="form-control mb-2"  type="text" name="city" id="city"
                      placeholder="Observaciones" :rules="isRequire" :class="{ 'is-invalid': errors.city }"></Field>                    
                  </b-form-group>
                </b-row>
                <hr />

                <b-button variant="primary mt-2" type="submit">Crear Nuevo Registro</b-button>
              </div>
            </template>
          </iq-card>
        </b-col>



        <b-col md="12">
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
        </b-col>



      </b-row>
    </Form>
  </b-container>
</template>
<script>
import { xray } from "../../config/pluginInit";
import iqCard from "../../components/xray/cards/iq-card";

import { Form, Field } from "vee-validate";


export default {
  name: "AddUser",
  components: { iqCard, Form, Field },
  mounted() {
    xray.index();
  },
  data() {
    
    return {
      

      columns: [
        { label: "Nombre", field: "Nombre", headerClass: "text-left" },
        { label: "Tipo de Consulta", field: "tConsulta", headerClass: "text-left" },
        { label: "Observaciones", field: "Observaciones", headerClass: "text-left" },

      ],
      rows: [
        {
          id: 1,
          Nombre: " \u00A0",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",

        },
        {
          id: 2,
          Nombre: " \u00A0 ",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",

        },
        {
          id: 3,
          Nombre: " \u00A0 ",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",

        },
        {
          id: 4,
          Nombre: " \u00A0 ",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",

        },
        {
          id: 5,
          Nombre: " \u00A0 ",
          tConsulta: " \u00A0 ",
          Observaciones: " \u00A0 ",
        },
      ],




    };
  },
  // computed: {
  //   fullName: function () {
  //     return this.user.fname + " " + this.user.lname;
  //   },
  // },

};
</script>
