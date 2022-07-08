<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div>
      <h4>
        “La tecnologia es importante, pero lo unico que realmente importa es lo
        que hacemos con ella”
      </h4>
    </div>
    <div>
      <div>
        <h2>Mision</h2>
        <div>
          <p>
            “La misión de Almond Technologies es informar y capacitar a
            estudiantes y profesores con el objetivo de tener una mayor
            eficiencia en el uso de los recursos TIC para que de esta manera se
            pueda mejorar la calidad de educación desde el medio por el que se
            brindan las clases.”
          </p>
        </div>
      </div>
      <br />
      <div>
        <h2>Vision</h2>
        <div>
          <p>
            “La visión de nuestra empresa es llegar a tener una educación con
            altos estándares de calidad mediante el aprovechamiento de los
            recursos digitales para que de esta manera se incrementen los
            conocimientos de la población en este ámbito.”
          </p>
        </div>
      </div>
    </div>
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
h2 {
  width: 50%;
  padding: 12px 20px;
  margin: 3px 0;
  display: inline-block;
  border: none;
  box-sizing: border-box;
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
p {
  width: 40%;
  background-color: #42b98352;
  padding: 12px 20px;
  margin: 3px 0;
  display: inline-block;
  border: none;
  box-sizing: border-box;
}
</style>
