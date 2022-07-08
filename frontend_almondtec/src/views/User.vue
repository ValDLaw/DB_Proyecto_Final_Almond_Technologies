<template>
  <div>
    <h1>Welcome!</h1>

    <div class="box">
      <h1>Perfil</h1>
      <ul>
        <div v-for="item in data" :key="item.nombres">
          <li>
            {{ item }}
          </li>
        </div>
      </ul>
    </div>
  </div>
</template>
<script>
import User from "@/UserService";
export default {
  name: "User",
  created() {
    this.getUser();
  },
  methods: {
    getUser() {
      User.getUser().then((response) => {
        console.log("response: ", response);
        this.data = response.data;
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
  border: 1px solid red;
}
ul {
  list-style: none;
  padding: 0px;
  margin: 0px;
  width: 300px;
}
</style>
