<template>
    <div>
      <h2>Editar Información del Bebé</h2>
  
      <div v-if="message" style="margin-top: 10px;">
        {{ message }}
      </div>
  
      <form @submit.prevent="submitForm">
        
        <input type="number" id="id" v-model="bebe.id" style="display: none;">
        <label for="sexo">Sexo :</label><br>
        <input type="text" id="sexo" v-model="bebe.sexo" required><br><br>
      
        <label for="fechaNacimiento">Fecha de Nacimiento:</label><br>
        <input type="date" id="fechaNacimiento" v-model="bebe.fecha_nacimiento" required><br><br>
      
        <label for="horaNacimiento">Hora de Nacimiento:</label><br>
        <input type="time" id="horaNacimiento" v-model="bebe.hora_nacimiento" required><br><br>
      
        <label for="lugarNacimiento">Lugar de Nacimiento:</label><br>
        <select id="lugarNacimiento" v-model="bebe.lugar_nacimiento" required>
          <option value="">Seleccionar</option>
          <option value="Xicotepec">Xicotepec</option>
          <option value="Huachinango">Huachinango</option>
          <!-- Agrega más opciones según sea necesario -->
        </select><br><br>
      
        <label for="peso">Peso:</label><br>
        <input type="number" id="peso" step="0.01" v-model="bebe.peso" required><br><br>
      
        <label for="longitud">Longitud:</label><br>
        <input type="number" id="longitud" step="0.01" v-model="bebe.longitud" required><br><br>
      
        <label for="nPadre">Nombre del padre:</label><br>
        <input type="text" id="nPadre" v-model="bebe.nombre_padre" required><br><br>
      
        <label for="nMadre">Nombre de la Madre:</label><br>
        <input type="text" id="nMadre" v-model="bebe.nombre_madre" required><br><br>
      
        <label for="telefonoContacto">Teléfono de contacto:</label><br>
        <input type="text" id="telefonoContacto" v-model="bebe.telefono_contacto" required><br><br>
      
        <label for="emailC">Email de contacto:</label><br>
        <input type="email" id="emailC" v-model="bebe.email_contacto" required><br><br>
      
        <label for="observaciones">Observaciones:</label><br>
        <textarea id="observaciones" v-model="bebe.observaciones"></textarea><br><br>
      
        <label for="tipoNacimiento">Tipo de Nacimiento:</label><br>
        <input type="text" id="tipoNacimiento" v-model="bebe.tipo_nacimiento"><br><br>
      
        <label for="frecuenciaCardiaca">Frecuencia Cardíaca:</label><br>
        <input type="number" id="frecuenciaCardiaca" v-model="bebe.frecuencia_cardiaca"><br><br>
      
        <label for="temperatura">Temperatura:</label><br>
        <input type="number" id="temperatura" step="0.01" v-model="bebe.temperatura"><br><br>
      
        <label for="presionArterialSistolica">Presión Arterial Sistólica:</label><br>
        <input type="number" id="presionArterialSistolica" v-model="bebe.presion_arterial_sistolica"><br><br>
      
        <label for="presionArterialDiastolica">Presión Arterial Diastólica:</label><br>
        <input type="number" id="presionArterialDiastolica" v-model="bebe.presion_arterial_diastolica"><br><br>
      
        <!-- Agrega los demás campos de la tabla aquí -->
      
        <button type="submit">Guardar Cambios</button>
      </form>
      
    </div>
  </template>
  