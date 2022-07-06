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
        <p class="title">Tutoriales</p>
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
  <div
    class="columns features"
    style="margin-top: 10px; width: 520px; margin-left: 300px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://www.clickbinar.com/wp-content/uploads/2021/04/ClickBinar-Niel-Tan-Traffic-Sources.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Plataformas Virtuales</h4>
          <p>
            Son sistemas de gestión de aprendizaje, que permiten distribuir y
            controlar diversos tipos de contenidos y recursos educativos,
          </p>
          <router-link to="/plataformas-virtuales-tutoriales">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <!-- post 2-->
  <div
    class="columns features"
    style="margin-top: -664px; width: 520px; margin-left: 840px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://www.ganeshawebtech.com/wp-content/uploads/2022/01/ios_abanner.svg"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Videoconferencias</h4>
          <p>
            Las videoconferencias permiten mantener reuniones con grupos de
            personas situadas en lugares alejados entre sí
          </p>
          <router-link to="/videoconferencias-tutoriales">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </router-link>
        </div>
      </div>
    </div>
  </div>

  <!-- post 3-->
  <div
    class="columns features"
    style="margin-top: 80px; width: 520px; margin-left: 300px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://meunion.com.tr/wp-content/uploads/2021/02/Scrum-board-bro.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Pizarras virtuales</h4>
          <p>
            Las pizarras online son plataformas en la nube para el trabajo
            colaborativo, que pueden usarse en combinación con tu sistema de
            Videoconferencias o un aula virtual y tiene una variedad de
            funciones y herramientas
          </p>
          <router-link to="/pizarras-virtuales-tutoriales">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <!-- post 4-->
  <div
    class="columns features"
    style="margin-top: -664px; width: 520px; margin-left: 840px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://img.freepik.com/vector-gratis/ilustracion-concepto-tablero-scrum_114360-1591.jpg"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Apps de organizacion</h4>
          <p>
            Las app de organizacion permiten crear listas de tareas con sus
            correspondientes recordatorios o establecer rutinas de trabajo son
            algunas de las funciones que incluyen las apps de organización más
            populares
          </p>
          <router-link to="/apps-organizacionales-tutoriales">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
