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
        <p class="title">Material adicional</p>
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
              src="https://www.clickbinar.com/wp-content/uploads/2021/04/ClickBinar-Niel-Tan-Traffic-Sources.png"
              alt="Placeholder image"
              class="modal-button"
              data-target="modal-image2"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="content">
            <h4>Aplicaciones para volver mas participativa a la clase</h4>
            <p>
              El día a día en el aula puede ser más dinámico si incorporamos
              herramientas digitales en la práctica docente, creando nuevas
              rutinas y motivando a los alumnos y alumnas a participar y adoptar
              un rol más activo.
            </p>

            <router-link to="/apps-participativa-ma">
              <span
                class="button is-link modal-button"
                data-target="modal-image2"
                >Ver aplicaciones</span
              >
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- post 2-->
  <div
    class="columns features"
    style="margin-top: -665px; width: 520px; margin-left: 580px"
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
          <h4>Organización</h4>
          <p>
            Crear listas de tareas con sus correspondientes recordatorios o
            establecer rutinas de trabajo son algunas de las funciones que
            incluyen las apps de organización más populares.
          </p>
          <router-link to="/apps-organizacionales-hd">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver aplicaciones</span
            >
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <!-- post 3-->
  <div
    class="columns features"
    style="margin-top: -615px; width: 520px; margin-left: 1120px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://ehssansindi.com/wp-content/uploads/2021/03/home-1.gif"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Aplicaciones para aprender sobre temas especificos</h4>
          <p>
            La educación online (también llamada virtual), es el desarrollo de
            distintos programas cuyo objetivo es formar o enseñar a través de la
            Internet.
          </p>
          <router-link to="/apps-temas-especificos-ma">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver aplicaciones</span
            >
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
