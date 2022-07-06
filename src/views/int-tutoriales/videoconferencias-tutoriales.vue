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
        <p class="title">Tutoriales de videoconferencias</p>
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
            src="https://www.silicon.es/wp-content/uploads/2022/04/zoom-png-logo-download-transparent-20-1.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Zoom</h4>
          <p>
            Zoom utiliza los servicios de la nube en Internet para realizar
            videoconferencias por video, audio o ambos, uniendo a personas de
            todo el mundo a través de una cámara web o un teléfono.
          </p>
          <a
            href="https://www.youtube.com/playlist?list=PLlM0tKd2OBZWacH3ZDDcKON2qarKVr9LN"
          >
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </a>
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
            src="data:image/png;base64,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"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Google Meet.</h4>
          <p>
            Google Meet funciona en cualquier dispositivo. Únete a reuniones
            desde un ordenador de escritorio o portátil, con un
            dispositivoAndroid o con un iPhone o iPad. Si tu organización
            necesita utilizar una sala de conferencias, el hardware de Google
            Meet ofrece opciones de gran calidad a un precio asequible.
          </p>
          <a
            href="https://www.youtube.com/playlist?list=PLlM0tKd2OBZV8Mg-aHB8Xo6fvff8pXdiv"
          >
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
    style="margin-top: 10px; width: 520px; margin-left: 300px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://logodownload.org/wp-content/uploads/2017/05/skype-logo-1.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Skype</h4>
          <p>
            Skype es un software que permite que todo el mundo se comunique.
            Millones de personas y empresas ya usan Skype para hacer llamadas y
            videollamadas gratis individuales y grupales, enviar mensajes
            instantáneos y compartir archivos con otras personas que usan Skype.
          </p>
          <a
            href="https://www.youtube.com/playlist?list=PLlM0tKd2OBZWbbLVFAVuIgrIielFxLB9O"
          >
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </a>
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
            src="https://proyectosbeta.net/wp-content/uploads/2020/04/LogoJitsiMeet-imagen-destacada.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Jitsy.</h4>
          <p>
            Jitsi Meet sirve para realizar videollamadas o conferencias de hasta
            100 participantes de manera gratuita y sin necesidad de cuenta. Sus
            opciones son más avanzadas que en el resto de herramientas del
            estilo, pudiendo ver estadísticas de los participantes como el
            tiempo que ha hablado en total.
          </p>
          <a
            href="https://www.youtube.com/playlist?list=PLlM0tKd2OBZV5FaZTKEprLYtwhtUCx5XV"
          >
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
