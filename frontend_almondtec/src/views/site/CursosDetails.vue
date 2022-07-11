<template>
  <div>
    <section>
      <h1>{{ curso.name }}</h1>
      <div class="todo-details">
        {{ curso.nombre }}
      </div>
    </section>
    <section class="extras">
      <h2>Top extras in {{ curso.nombre }}</h2>
      <div class="cards">
        <div v-for="extra in curso.extras" :key="extra.tema" class="card">
          <router-link
            :to="{
              name: 'ExtraDetails',
              params: { evidenceSlug: evidence.slug },
            }"
          >
            <img
              :src="require(`@/assets/${evidence.image}`)"
              :alt="evidence.name"
            />
            <span class="card__text">
              {{ evidence.name }}
            </span>
          </router-link>
        </div>
      </div>
      <router-view />
    </section>
  </div>
</template>

<script>
export default {
  name: "CursosDetails",
  data() {
    return {};
  },
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  computed: {
    cursos() {
      return {}; //db.cursos.find((c) => c.id === this.slug);
    },
  },
  beforeCreate() {},
  created() {},
  beforeMount() {},
  mounted() {},
  beforeUpdate() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<style scoped>
img {
  max-width: 600px;
  max-height: 400px;
}
.todo-details {
  display: flex;
  justify-content: space-between;
}
.cards {
  display: flex;
  flex-direction: row;
}
.cards img {
  max-height: 200px;
}

.card {
  padding: 0 20px;
  position: relative;
}

.card__text {
  position: absolute;
  color: white;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 25px;
  font-weight: bold;
  text-decoration: none;
}
</style>
