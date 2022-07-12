<template>
  <div
    v-if="show"
    :class="`alert alert-${category} d-flex justify-content-center`"
    role="alert"
  >
    <p v-show="show">{{ message }}</p>
  </div>
</template>

<script>
import { auth } from "@/LoginService";

export default {
  name: "ShowMessage",
  props: ["message", "category", "show"],
  watch: {
    show() {
      setTimeout(() => {
        auth.showNotification = false;
        auth.notificationMessage = "";
        auth.notificationCategory = "";
      }, 5002);
    },
  },
};
</script>
