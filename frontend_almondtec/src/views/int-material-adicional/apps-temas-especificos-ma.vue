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
        <p class="title">Aplicaciones</p>
      </div>
    </div>
  </section>
  <div class="box cta">
    <p class="has-text-centered">
      <span class="tag is-primary">Seleccione</span> la aplicacion
    </p>
  </div>
  <!-- post 1-->
  <div class="columns features" style="margin-top: 10px">
    <div class="column is-4">
      <div class="card is-shady">
        <div class="card-image">
          <figure class="image is-4by3">
            <img
              src="https://blob.sololearn.com/avatars/sololearn.png"
              alt="Placeholder image"
              class="modal-button"
              data-target="modal-image2"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="content">
            <h4>Sololearn</h4>
            <p>
              SoloLearn es una plataforma diseñada para enseñar programación, de
              forma gratuita y desde cero, a todos los usuarios interesados en
              aprender a programar.
            </p>
            <a href="https://www.sololearn.com">
              <span
                class="button is-link modal-button"
                data-target="modal-image2"
                >Ir a la aplicación</span
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
    style="margin-top: -665px; width: 520px; margin-left: 580px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://www.eastersealstech.com/wp-content/uploads/2020/01/imathematics-app.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>iMathematics</h4>
          <p>
            iMathematics es la mejor aplicación en la AppStore para el estudio
            de las matemáticas! Con más de 120 temas, más de 700 fórmulas,
            interfaz atractiva, con 8 solucionadores y calculadoras, y una
            versión especial para el iPad!
          </p>
          <a href="http://www.mobixee.com/portfolio/item/imathematics/">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ir a la aplicación</span
            >
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
