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
