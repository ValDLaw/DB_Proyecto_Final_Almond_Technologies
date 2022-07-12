<template>
  <div>
    <section class="evidences">
      <h2>Usted se puede matricular en los siguientes cursos</h2>
      <div
        v-for="curso in cursos_disponibles?.cursos_disponibles"
        :key="curso.id"
      >
        {{ curso.nombre }}
        <div>
          <button @click="Matricularse(curso.id)">
            Matricularse en este curso
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Axios from "axios";
let axios = Axios.create({
  baseURL: "http://127.0.0.1:5002",
});
export default {
  name: "CursosDetails",
  data() {
    return {
      cursos_disponibles: null,
      data: "",
    };
  },
  mounted() {
    this.Matricular();
  },
  methods: {
    Matricular() {
      axios
        .get("http://127.0.0.1:5002/user/cursos_disponibles", {
          headers: { Authorization: localStorage.getItem("token") },
        })
        .then((response) => {
          this.cursos_disponibles = response.data;
          console.log(this.cursos_disponibles);
        })
        .catch((e) => console.log(e));
    },
    Matricularse(curso_id) {
      axios
        .get("http://127.0.0.1:5002/matricular/" + curso_id, {
          headers: {
            Authorization: localStorage.getItem("token"),
          },
        })
        .then((response) => {
          console.log(response);
        })
        .then(this.$router.push("/user"))
        .catch((e) => console.log(e));
    },
  },
  beforeCreate() {},
  created() {},
  beforeMount() {},
  beforeUpdate() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<style scoped>
img {
  max-width: 600px;
  max-height: 400px;
}
.todo-details {
  display: flex;
  justify-content: space-between;
}
.cards {
  display: flex;
  flex-direction: row;
}
.cards img {
  max-height: 200px;
}

.card {
  padding: 0 20px;
  position: relative;
}

.card__text {
  position: absolute;
  color: white;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 25px;
  font-weight: bold;
  text-decoration: none;
}
</style>
