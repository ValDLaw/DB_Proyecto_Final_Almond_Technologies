<template>
  <div>
    <div class="box1">
      <h1>Perfil</h1>
      <ul>
        <div class="per"></div>
        <p>ID: {{ datos?.id }}</p>
        <p>Nombres: {{ datos?.nombres }}</p>
        <p>Apellidos: {{ datos?.apellidos }}</p>
      </ul>
    </div>
    <div class="box2" v-if="datos?.rol == 'estudiante'">
      <h1>Cursos inscritos</h1>
      <section class="evidences">
        <h2>Usted está inscrito en los siguientes cursos</h2>
        <div v-for="curso in cursos?.cursos_inscritos" :key="curso.id">
          <router-link
            :to="{
              name: 'Cursos',
              params: { curso_id: curso.id },
            }"
          >
            {{ curso.nombre }}</router-link
          >
        </div>
        <router-view />
        <div>
          <button @click="$router.push('/matricular')" link>
            Matricularse en un curso
          </button>
        </div>
      </section>
      <p>Total:{{ cursos?.total_cursos_inscritos }}</p>
    </div>
  </div>
  <!-- FIN creacion de botones para cursos -->
</template>

<script>
const { default: axios } = require("axios");
export default {
  name: "User",
  data() {
    return {
      datos: null,
      cursos: null,
      cursos_i: [],
    };
  },
  mounted() {
    this.getUser();
    this.getCursosInscritos();
    this.getCursosEnsenados();
  },
  methods: {
    getUser() {
      axios
        .get("http://127.0.0.1:5002/user", {
          headers: { Authorization: localStorage.getItem("token") },
        })
        .then((response) => {
          this.datos = response.data;
          console.log(this.datos);
        })
        .catch((e) => console.log(e));
    },
    getCursosInscritos() {
      axios
        .get("http://127.0.0.1:5002/user/cursos", {
          headers: { Authorization: localStorage.getItem("token") },
        })
        .then((responses) => {
          this.cursos = responses.data;
          this.cursos_i = responses.data.cursos_inscritos;
          console.log(this.cursos_i);
        })
        .catch((e) => console.log(e));
    },
    getCursosEnsenados() {
      axios
        .get("http://127.0.0.1:5002/user/cursos", {
          headers: { Authorization: localStorage.getItem("token") },
        })
        .then((responses) => {
          this.cursos = responses.data;
          this.cursos_i = responses.data.cursos_inscritos;
          console.log(this.cursos_i);
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.box1 {
  width: 30%;
  padding: 12px 20px;
  margin: 3px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.box2 {
  width: 30%;
  padding: 12px 20px;
  margin: 3px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
.per {
  text-align: justify;
  text-justify: inter-word;
}
</style>
