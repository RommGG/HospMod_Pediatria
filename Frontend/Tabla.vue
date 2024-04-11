<template>
    <div>
      <h1>Listado de Bebés</h1>
  
      <!-- Aqui va el div del mesaje  -->
      <table>
        <thead>
          <tr>
            <th>Id del Bebe</th>
            <th>Sexo del Bebe</th>
            <th>Nombre del Padre</th>
            <th>Nombre de la Madre</th>
            <th>Fecha de nacimiento</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(bebe, index) in paginatedBebes" :key="index">
            <td>{{ bebe.id }}</td>
            <td>{{ bebe.sexo }}</td>
            <td>{{ bebe.nombre_padre }}</td>
            <td>{{ bebe.nombre_madre }}</td>
            <td>{{ bebe.fecha_nacimiento }}</td>
            <td>
              <button @click="eliminarBebe(bebe.id)">
                <i class="fas fa-trash-alt"></i> Eliminar
              </button>
              &nbsp;&nbsp;&nbsp;
  
              <button style="margin-top: 5px;">
                <router-link :to="{ name: 'editar', params: { id: bebe.id }}" class="router-link-custom">
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
        <button @click="paginar('siguiente')" :disabled="paginaActual * itemsPorPagina >= bebes.length"
          style="background-color: black;">Siguiente</button>
      </div>
  
      <!-- Mostrar el número de página actual y el número total de páginas -->
      <div style="margin-top: 10px;">
        Página {{ paginaActual }} de {{ totalPages }}
      </div>
    </div>
  </template>