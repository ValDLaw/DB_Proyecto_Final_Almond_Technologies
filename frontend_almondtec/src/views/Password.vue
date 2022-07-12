<template>
  <div>
    <h1>Password</h1>
    <form @submit.prevent="new_p">
      <input v-model="id" type="number" minlength="9" placeholder="id" /><br />
      <input v-model="email" type="email" placeholder="email" /><br />
      <input
        v-model="new_password"
        type="password"
        placeholder="password"
      /><br />
      <button type="submit">Cambiar Contraseña</button>
    </form>
  </div>
</template>

<script>
import { auth } from "../LoginService";
export default {
  name: "New_Password",
  data() {
    console.log("auth: ", auth);
    return {
      id: "",
      email: "",
      new_password: "",
    };
  },
  methods: {
    async new_p() {
      const url = "http://127.0.0.1:5000/password";
      const response = await fetch(url, {
        method: "PATCH",
        body: JSON.stringify({
          id: this.id,
          email: this.email,
          new_password: this.new_password,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.log("response: ", response);
      const data = await response.json();
      console.log("data: ", data);
      if (data["success"]) {
        this.$router.push({
          name: "Login",
        });
      }
      auth.displayNotification(data["message"], "danger");
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
