<template>
  <nav>
    <router-link to="/">Cuenta </router-link> |
    <router-link to="/tutoriales-main">Tutoriales </router-link>|
    <router-link to="/Beneficios-main">Beneficios </router-link>|
    <router-link to="/modelo-de-clases">Modelo de clases </router-link>|
    <router-link to="/tips-main">Tips </router-link>|
    <router-link to="/material-adicional">Material </router-link>|
    <router-link to="/herramientas-digitales">Herramientas </router-link>|
    <router-link to="/juegos-main">Juegos </router-link>|
    <router-link to="/apps-organizacionales-hd">Salir </router-link>
  </nav>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

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
