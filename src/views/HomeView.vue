<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/almond.png" />
    <HelloWorld msg="Welcome to Almond Technologies world's" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld,
  },
};
</script>
