<template>
    <div class="pt-5">
        <div v-if="departamentos && departamentos.length">
            <div class="card mb-3" v-for="departamento of departamentos" v-bind:key="departamento.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <div class="card-body">
                            <span class="card-title"><b>Costo:</b> {{ departamento.costo_depa }}</span>
                            <br>
                            <span class="card-text"><b>Cuartos:</b> {{ departamento.num_cuartos }}</span>
                            <br>
                            <br>
                            <span class="card-text"><b>Banios:</b> {{ departamento.num_banios }}</span>
                            <br>
                            <br>
                            <span class="card-text"><b>Alicuta:</b> {{ departamento.valor_alicuta }}</span>
                            <br>
                            <router-link :to="{name: 'edit_telefono', params: { id: departamento.id }}" class="btn btn-sm btn-primary">Editar</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteDepartamento(departamento)">Eliminar</button>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <span class="card-text"><b>Propietario:</b> {{ departamento.propietario_str }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="departamentos.length == 0"> Sin Departamentos</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamentos: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteTelefono: function(e) {
            if (confirm('Eliminar ' + e.departamentos)) {
                axios.delete(e.url)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/departamento/')
                .then( response => {
                    this.departamentos = response.data
                });
        }
    },
}
</script>
