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
        <p class="title">Aplicaciones tecnologicas con descuento</p>
      </div>
    </div>
  </section>
  <div class="box cta">
    <p class="has-text-centered">
      <span class="tag is-primary">Seleccione</span> la aplicacion para acceder
      al descuento
    </p>
  </div>
  <!-- post 1-->
  <div class="columns features" style="margin-top: 10px">
    <div class="column is-4">
      <div class="card is-shady">
        <div class="card-image">
          <figure class="image is-4by3">
            <img
              src="https://images.samsung.com/is/image/samsung/assets/global/about-us/brand/logo/360_197_1.png?$FB_TYPE_B_PNG$"
              alt="Placeholder image"
              class="modal-button"
              data-target="modal-image2"
            />
          </figure>
        </div>
        <div class="card-content">
          <div class="content">
            <h4>Samsung</h4>
            <p>
              El programa ofrece productos enfocados a contribuir con el
              desempeño académico de los estudiantes, como, por ejemplo:
              tablets, smartphones, audífonos bluetooth, relojes inteligentes,
              monitores para escritorio, etc. El programa irá actualizando su
              catálogo continuamente, añadiendo los últimos lanzamientos y
              ofertas extendidas a la comunidad universitaria.
            </p>
            <a
              href="https://estudiantes.samsung.com.pe/?utm_source=s-membersNewsRoom&utm_medium=image&utm_campaign=CMO-EppStudent-users-CommunityNewsromm-202204-tactica&cid=pe_owned_CommunityNewsromm_s-membersNewsRoom_EppStudent_users-CMO-none_202204_image_smembersCommNewsroom"
            >
              <span
                class="button is-link modal-button"
                data-target="modal-image2"
                >Ir a la pagina</span
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
    style="margin-top: -725px; width: 520px; margin-left: 580px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://logos-marcas.com/wp-content/uploads/2020/04/Apple-Logo.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Apple</h4>
          <p>
            El descuento de estudiantes de Apple permite ahorrar en un nuevo Mac
            o iPad con los descuentos para el sector educativo. Disponible para
            estudiantes inscritos o admitidos en una universidad, padres o
            madres que realizan compras para estudiantes universitarios y
            profesores u otro personal del sector educativo.pie de página* Para
            empezar, comprueba si cumples los requisitos.pie de página
          </p>

          <a href="https://www.apple.com/es/shop/education-pricing">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ir a la pagina</span
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
            src="data:image/png;base64,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"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Lenovo</h4>
          <p>
            Puede acceder a un código de descuento para estudiantes de Lenovo
            desde Lenovo's sitio web oficial. El descuento varía según el
            producto y puedes ahorrar hasta un 30% descuento en su compra.
          </p>
          <a href="https://www.lenovo.com/pe/es/estudiantes">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ir a la pagina</span
            >
          </a>
        </div>
      </div>
    </div>
  </div>
  <!-- titulo 2-->

  <section class="hero is-info is-small" style="margin-top: 50px">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title">Capacitaciones virtuales gratuitas</p>
      </div>
    </div>
  </section>
  <!-- post 3-->
  <div
    class="columns features"
    style="margin-top: 10px; width: 520px; margin-left: 300px"
  >
    <div class="card is-shady">
      <div class="card-image">
        <figure class="image is-4by3">
          <img
            src="https://i2.wp.com/www.ugelcrucero.edu.pe/wp-content/uploads/2018/04/descarga-1.png?resize=225%2C225"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>Peru Educa</h4>
          <p>
            El Sistema Digital para el Aprendizaje PerúEduca es una página
            oficial del Ministerio de Educación del Perú que permite a los
            profesores, directivos, alumnos y padres de familia acceder a
            herramientas, servicios y recursos educativos de acuerdo con sus
            propios gustos y necesidades de información
          </p>

          <a href="https://www.perueduca.pe/#/home">
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
            src="https://upload.wikimedia.org/wikipedia/commons/8/85/Logo_del_Colegio_Profesional_de_Profesores_del_Perú.jpg"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h4>COLEGIO PROFESIONAL DE PROFESORES DEL PERU - CPPP</h4>
          <p>
            La función del COLEGIO PROFESIONAL DE PROFESORES DEL PERU - CPPP es
            brindar a sus miembros Profesores de Educación Colegiados, los
            servicios profesionales, culturales y de defensa en el cumplimiento
            de las normas éticas y deontológicas de la profesión, así como de
            las demás normas legales pertinentes.
          </p>

          <a href="https://colegiodeprofesoresdelperu.org">
            <span class="button is-link modal-button" data-target="modal-image2"
              >Ver tutoriales</span
            >
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
