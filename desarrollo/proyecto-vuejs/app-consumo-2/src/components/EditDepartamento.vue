<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo_depa">Costo</label>
                <input
                    type="text"
                    class="form-control"
                    id="costo_depa"
                    v-model="departamento.costo_depa"
                    v-validate="'required'"
                    name="costo_depa"
                    placeholder="Ingrese costo_depa"
                    :class="{'is-invalid': errors.has('departamento.costo_depa') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="num_cuartos">Tipo</label>
                <input
                    type="text"
                    class="form-control"
                    id="num_cuartos"
                    v-model="departamento.num_cuartos"
                    v-validate="'required'"
                    name="tipo"
                    placeholder="Ingrese num_cuartos"
                    :class="{'is-invalid': errors.has('departamentos.num_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="num_banios">Tipo</label>
                <input
                    type="text"
                    class="form-control"
                    id="num_banios"
                    v-model="departamento.num_banios"
                    v-validate="'required'"
                    name="tipo"
                    placeholder="Ingrese num_banios"
                    :class="{'is-invalid': errors.has('departamentos.num_banios') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="valor_alicuta">Tipo</label>
                <input
                    type="text"
                    class="form-control"
                    id="valor_alicuta"
                    v-model="departamento.valor_alicuta"
                    v-validate="'required'"
                    name="tipo"
                    placeholder="Ingrese valor_alicuta"
                    :class="{'is-invalid': errors.has('departamentos.valor_alicuta') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
            </div>

            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                costo_depa: '',
                num_cuartos: '',
                num_banios:'',
                valor_alicuta:'',
                propietario: '',
            },
            estudiantesList: [],
            submitted: false
        }
    },
    mounted() {
        this.getEstudiantesList(),
        axios.get('http://127.0.0.1:8000/api/numerost/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.telefono = response.data
        });
    },
    methods: {
      getEstudiantesList() {
            axios
            .get('http://127.0.0.1:8000/api/estudiantes/')
            .then(response => {
                this.estudiantesList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/numerost/${this.telefono.id}/`,
                        this.telefono
                    )
                    .then(response => {
                        this.$router.push('/telefonos');
                    })
            });
        }
    },
}
</script>
