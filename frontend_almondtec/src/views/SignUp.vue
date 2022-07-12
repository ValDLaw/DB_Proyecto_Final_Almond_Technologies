<template>
  <div>
    <h1>Sign Up</h1>
    <form @submit.prevent="signup">
      <input v-model="id" type="number" minlength="9" placeholder="id" /><br />
      <input v-model="nombres" type="text" placeholder="nombres" /><br />
      <input v-model="apellidos" type="text" placeholder="apellidos" /><br />
      <input v-model="email" type="email" placeholder="email" /><br />
      <input v-model="password" type="password" placeholder="password" /><br />
      <button type="submit">SignUp</button>
    </form>
  </div>
</template>

<script>
import { auth } from "../LoginService";
export default {
  name: "SignUp",
  data() {
    console.log("auth: ", auth);
    return {
      id: "",
      nombres: "",
      apellidos: "",
      email: "",
      password: "",
    };
  },
  methods: {
    async signup() {
      const url = "http://127.0.0.1:5002/signup";
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
          id: this.id,
          nombres: this.nombres,
          apellidos: this.apellidos,
          email: this.email,
          password: this.password,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.log("response: ", response);
      const data = await response.json();
      console.log("data: ", data);
      auth.displayNotification(data["message"], "danger");
      if (data["success"]) {
        this.$router.push({
          name: "Login",
        });
      }
    },
  },
};
</script>

<style scoped>
input[type="text"],
input[type="password"],
input[type="email"],
input[type="number"] {
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
