<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link :to="{ name: 'Login' }"> Login </router-link>|
    <router-link :to="{ name: 'SignUp' }"> Sign Up </router-link>
    <div v-if="auth.authorized">
      <router-link :to="{ name: 'User' }"> Perfil </router-link>|
      <router-link to="/tutoriales-main"> Tutoriales </router-link>|
      <router-link to="/Beneficios-main"> Beneficios </router-link>|
      <router-link to="/modelo-de-clases"> Modelo de clases </router-link>|
      <router-link to="/tips-main"> Tips </router-link>|
      <router-link to="/material-adicional"> Material adicional </router-link>|
      <router-link to="/herramientas-digitales">
        Herramientas digitales </router-link
      >| <router-link to="/juegos-main"> Juegos </router-link>|
      <router-link to="/logout"> Salir </router-link>
    </div>
  </nav>
</template>

<script>
import { auth } from "@/LoginService";
export default {
  name: "TheNavigation",
  data() {
    return {
      auth,
    };
  },
};
</script>

<style>
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
