<template>
  <the-navigation />
  <ShowMessage
    :show="auth.showNotification"
    :category="auth.notificationCategory"
    :message="auth.notificationMessage"
  />
  <router-view :key="$route.path" />
</template>

<script>
import TheNavigation from "./components/TheNavigation.vue";
import ShowMessage from "./components/ShowMessage.vue";
import { auth } from "@/LoginService.js";

export default {
  name: "App",
  components: {
    TheNavigation,
    ShowMessage,
  },
  data() {
    return {
      auth,
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
