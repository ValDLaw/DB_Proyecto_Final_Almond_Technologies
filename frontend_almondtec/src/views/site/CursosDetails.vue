<template>
  <div>
    <section>
      <h1>{{ extras?.curso_nombre }}</h1>
      <div class="todo-details">
        <div v-for="extra in extras?.extras" :key="extra.nombre">
          {{ extra.nombre }}
          {{ extra.tema }}
          <a
            href="https://www.youtube.com/playlist?list=PLlM0tKd2OBZWEswsYYOVFBteewbC8htFK"
          >
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </a>
        </div>
        <div>
          <button @click="Abandonar">Abandonar el curso</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
const { default: axios } = require("axios");
export default {
  name: "CursosDetails",
  data() {
    return {
      extras: null,
    };
  },
  props: {
    curso_id: {
      type: String,
      required: true,
    },
  },
  mounted() {
    this.getExtras();
  },
  methods: {
    getExtras() {
      axios
        .get("http://127.0.0.1:5000/cursos/" + this.curso_id, {
          headers: { Authorization: localStorage.getItem("token") },
        })
        .then((response) => {
          this.extras = response.data;
          console.log(this.extras);
        })
        .catch((e) => console.log(e));
    },
    async Abandonar() {
      await axios
        .delete("http://127.0.0.1:5000/abandonar/" + this.curso_id, {
          headers: { Authorization: localStorage.getItem("token") },
        })
        .then((response) => {
          this.extras = response.data;
          console.log(this.extras);
          this.$router.push("/user");
        })
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
