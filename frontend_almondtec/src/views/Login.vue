<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="auth.login(email, password)">
      <input v-model="email" type="email" placeholder="email" /><br />
      <input v-model="password" type="password" placeholder="password" /><br />
      <button type="submit">Login</button>
    </form>
    <router-link to="/password"> ¿Olvidaste tu contraseña? </router-link>
  </div>
</template>

<script>
import { auth } from "@/LoginService.js";
export default {
  name: "Login",
  data() {
    console.log("auth: ", auth);
    return {
      email: "",
      password: "",
      auth,
    };
  },
};
</script>

<style scoped>
input[type="text"],
input[type="password"],
input[type="email"] {
  width: 20%;
  padding: 12px 20px;
  margin: 3px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #04aa6d;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 20%;
}

button:hover {
  opacity: 0.8;
}

.container {
  padding: 16px;
}
</style>
