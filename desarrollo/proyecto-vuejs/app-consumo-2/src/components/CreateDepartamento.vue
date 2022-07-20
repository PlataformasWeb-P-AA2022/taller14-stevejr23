<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo_depa">Costo Departamentos</label>
                <input
                    type="text"
                    class="form-control"
                    id="costo_depa"
                    v-model="departamento.costo_depa"
                    v-validate="'required'"
                    name="costo_depa"
                    placeholder="Ingres costo_depa"
                    :class="{'is-invalid': errors.has('departamento.costo_depa') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="num_cuartos">Numeros Cuartos</label>
                <input
                    type="text"
                    class="form-control"
                    id="num_cuartos"
                    v-model="departamento.num_cuartos"
                    v-validate="'required'"
                    name="num_cuartos"
                    placeholder="Ingrese num_cuartos"
                    :class="{'is-invalid': errors.has('departamento.num_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid num_cuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="num_banios">Numero Banios</label>
                <input
                    type="text"
                    class="form-control"
                    id="num_banios"
                    v-model="departamento.num_banios"
                    v-validate="'required'"
                    name="num_banios"
                    placeholder="Ingrese num_banios"
                    :class="{'is-invalid': errors.has('departamento.num_banios') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid num_banios.
                </div>
            </div>

                <div class="form-group">
                <label for="valor_alicuta">Valor Alicuta</label>
                <input
                    type="text"
                    class="form-control"
                    id="valor_alicuta"
                    v-model="departamento.valor_alicuta"
                    v-validate="'required'"
                    name="valor_alicuta"
                    placeholder="Ingrese valor_alicuta"
                    :class="{'is-invalid': errors.has('departamento.valor_alicuta') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid valor_alicuta.
                </div>
            </div>


            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
            </div>
            <br>
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
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getPropietariosList()
    },
    methods: {
      getPropietariosList() {
            axios
            .get('http://127.0.0.1:8000/api/propietarios/')
            .then(response => {
                this.propietariosList = response.data
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
                axios.post('http://127.0.0.1:8000/api/departamento/',
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>
