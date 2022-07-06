<template>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link
      rel="shortcut icon"
      href="../images/fav_icon.png"
      type="image/x-icon"
    />
    <title>Inicio</title>
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/overlayscrollbars/1.9.1/css/OverlayScrollbars.min.css"
    />
    <link
      href="https://fonts.googleapis.com/css?family=Open+Sans"
      rel="stylesheet"
    />
    <!-- Bulma Version 0.9.0-->
    <link
      rel="stylesheet"
      href="https://unpkg.com/bulma@0.9.0/css/bulma.min.css"
    />
    <link rel="stylesheet" type="text/css" href="../css/hero.css" />
    <link
      rel="stylesheet"
      href="https://unpkg.com/bulma-modal-fx/dist/css/modal-fx.min.css"
    />
  </head>

  <section class="hero is-info is-small">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title">
          Aplicaciones para volver mas participativa a la clase
        </p>
      </div>
    </div>
  </section>
  <div class="box cta">
    <p class="has-text-centered">
      <span class="tag is-primary">Seleccione</span> la aplicacion que desea
      aprender.
    </p>
  </div>
  <!-- post 1-->
  <div class="columns features" style="margin-top: 10px">
    <div class="column is-4">
      <div class="card is-shady">
        <div class="card-image">
          <figure class="image is-4by3">
            <img
              src="https://cdn-icons-png.flaticon.com/512/2965/2965289.png"
              alt="Placeholder image"
              class="modal-button"
              data-target="modal-image2"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="content">
            <h4>Jamboard</h4>
            <p>
              Jamboard es una pantalla inteligente que te permite extraer con
              rapidez imágenes de una búsqueda en Google, guardar el trabajo en
              la nube automáticamente, usar la herramienta de reconocimiento de
              formas y escritura a mano fácil de leer, y dibujar con una pluma
            </p>

            <a href="https://jamboard.google.com">
              <span
                class="button is-link modal-button"
                data-target="modal-image2"
                >Ver tutoriales</span
              >
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- post 2-->
  <div
    class="columns features"
    style="margin-top: -675px; width: 520px; margin-left: 580px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://quizizz.com/media/resource/gs/quizizz-media/quizzes/355f75e2-5b89-4e2e-a6bf-7a97e6af05d6?w=200&h=200"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Quizziz</h4>
          <p>
            Quizizz es una web/app gratuita que permite crear cuestionarios
            online de manera lúdica y divertida, que los estudiantes pueden
            responder de tres maneras distintas: En un juego en directo, como
            tareas, o de manera individual.
          </p>
          <a href="https://quizizz.com/?fromBrowserLoad=true">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </a>
        </div>
      </div>
    </div>
  </div>
  <!-- post 3-->
  <div
    class="columns features"
    style="margin-top: -665px; width: 520px; margin-left: 1120px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://educaciontech.com/wp-content/uploads/2021/01/kahootapplogobetter.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Kahoot!</h4>
          <p>
            Kahoot permite la creación de juegos de aprendizaje, o elegir entre
            los ya creados, para comenzar a trabajar un tema, revisar y reforzar
            contenidos e incluso realizar evaluaciones. La motivación de
            nuestros alumnos aumenta con el uso de esta herramienta.
          </p>
          <a href="https://kahoot.com/kahoot-study/">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
