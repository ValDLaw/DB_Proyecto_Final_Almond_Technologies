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
        <p class="title">Juegos interactivos</p>
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
              src="https://i1.wp.com/arbolabc.nyc3.cdn.digitaloceanspaces.com/Enlazanos/logo_lulu.png?w=442&ssl=1"
              alt="Placeholder image"
              class="modal-button"
              data-target="modal-image2"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="content">
            <h4>Arbol ABC</h4>
            <p>
              Arbol ABC es un mundo imaginario donde los pequeños ayudan a los
              personajes para completar los juegos. Este enfoque hace que el
              aprendizaje sea amigable y accesible para los niños creando un
              contexto que conecta las diferentes áreas del conocimiento
            </p>

            <a href="https://arbolabc.com">
              <span
                class="button is-link modal-button"
                data-target="modal-image2"
                >Ir a juegos</span
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
            src="https://static.comunicae.com/photos/notas/1122778/1437465971_Mundo_Primaria.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Mundo primaria.</h4>
          <p>
            Mundo Primaria es un lugar de aprendizaje y entretenimiento. Como
            está dirigido principalmente a niños y niñas entre 3 y 12 años, los
            contenidos relacionados con las asignaturas del colegio aparecen
            organizados por cursos, áreas temáticas y edades.
          </p>
          <a href="https://www.mundoprimaria.com">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ir a juegos</span
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
            src="https://asociacioncultural.gsdeducacion.com/wp-content/uploads/2019/05/a-look-at-minecraft-education-edition-004-1024x576-945x532.jpg"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Minecraft education</h4>
          <p>
            Minecraft education es una plataforma de aprendizaje basada en
            juegos que desarrolla habilidades, da rienda suelta a la creatividad
            e involucra a los estudiantes a la colaboración.
          </p>
          <a href="https://education.minecraft.net/en-us">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ir a juego</span
            >
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
