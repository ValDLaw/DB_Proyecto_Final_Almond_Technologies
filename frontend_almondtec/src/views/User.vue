<template>
  <div>
    <div class="box">
      <h1>Perfil</h1>
      <ul>
        <div class="per">
          <p>Nombres: {{ profile["nombres"] }}</p>
          <p>Apellidos: {{ profile["apellidos"] }}</p>
          <p>Correo Electrónico: {{ profile["email"] }}</p>
        </div>
      </ul>
    </div>
    <div>
      {% if profile["rol"] == "estudiante" %}
      <section class="cursos">
      <h2>Usted se encuentra matriculad@ en los siguientes cursos</h2>
      <div class="cards">
        <div
          v-for="curso in "
          :key="evidence.name"
          class="card"
        >
          <router-link
            :to="{
              name: 'EvidenceDetails',
              params: { evidenceSlug: evidence.slug },
            }"
          >
            <img
              :src="require(`@/assets/${evidence.image}`)"
              :alt="evidence.name"
            />
            <span class="card__text">
              {{ evidence.name }}
            </span>
          </router-link>
        </div>
      </div>
      <router-view />
    </section>
      {% else %}
      <div *ngIf="show">
        <div>show is ture</div>
      </div>
      {% endif %}
    </div>
  </div>
</template>
<script>
import { auth } from "@/LoginService";
import User from "@/UserService";
export default {
  name: "User",
  created() {
    this.getUser();
  },
  data() {
    return {
      profile: {},
      auth,
    };
  },
  computed: {
    estudiante() {
      return db.estudiante.find((e) => e.id === this.slug);
    },
  },
  methods: {
    getUser() {
      User.getUser().then((response) => {
        console.log("response: ", response);
        this.profile = response.data;
      });
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
.box {
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
