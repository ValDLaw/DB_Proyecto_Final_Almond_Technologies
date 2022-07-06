<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      “La tecnologia es importante, pero lo unico que realmente importa es lo
      que hacemos con ella”
    </p>
    <h3>Mision</h3>
    <ul>
      <li>
        <p>
          “La misión de Almond Technologies es informar y capacitar a
          estudiantes y profesores con el objetivo de tener una mayor eficiencia
          en el uso de los recursos TIC para que de esta manera se pueda mejorar
          la calidad de educación desde el medio por el que se brindan las
          clases.”
        </p>
      </li>
    </ul>
    <h3>Vision</h3>
    <ul>
      <li>
        <p>
          “La visión de nuestra empresa es llegar a tener una educación con
          altos estándares de calidad mediante el aprovechamiento de los
          recursos digitales para que de esta manera se incrementen los
          conocimientos de la población en este ámbito.”
        </p>
      </li>
    </ul>
    <h3>Feedback</h3>
    <ul>
      <li>
        <a
          href="https://forms.gle/wG9LrsiYMqDT5wVh9"
          target="_blank"
          rel="noopener"
          >Dar Feedback</a
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
