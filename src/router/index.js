import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  //tutoriales
  //1
  {
    path: "/apps-organizacionales-tutoriales",
    name: "apps-organizacionales-tutoriales",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-tutoriales/apps-organizacionales-tutoriales.vue"
      ),
  },
  //2
  {
    path: "/pizarras-virtuales-tutoriales",
    name: "pizarras-virtuales-tutoriales",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-tutoriales/Pizarras-virtuales-tutoriales.vue"
      ),
  },
  //3
  {
    path: "/plataformas-virtuales-tutoriales",
    name: "plataformas-virtuales-tutoriales",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-tutoriales/plataformas-virtuales-tutoriales.vue"
      ),
  },
  //4
  {
    path: "/videoconferencias-tutoriales",
    name: "videoconferencias-tutoriales",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-tutoriales/videoconferencias-tutoriales.vue"
      ),
  },
  //Material adicional
  //1
  {
    path: "/apps-participativa-ma",
    name: "apps-participativa-ma",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-material-adicional/apps-participativa-ma.vue"
      ),
  },
  //2
  {
    path: "/apps-temas-especificos-ma",
    name: "apps-temas-especificos-ma",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-material-adicional/apps-temas-especificos-ma.vue"
      ),
  },

  //herramientas digitales
  //1
  {
    path: "/apps-organizacionales-hd",
    name: "apps-organizacionales-hd",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-herramientas-digitales/apps-organizacionales-hd.vue"
      ),
  },
  //2
  {
    path: "/pizarras-virtuales-hd",
    name: "pizarras-virtuales-hd",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-herramientas-digitales/pizarras-virtuales-hd.vue"
      ),
  },
  //3
  {
    path: "/plataformas-virtuales-hd",
    name: "plataformas-virtuales-hd",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-herramientas-digitales/plataformas-virtuales-hd.vue"
      ),
  },
  //4
  {
    path: "/videoconferencias-hd",
    name: "videoconferencias-hd",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/int-herramientas-digitales/videoconferencias-hd.vue"
      ),
  },

  //main
  //beneficios
  {
    path: "/Beneficios-main",
    name: "Beneficios-main",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/main/Beneficios-main.vue"
      ),
  },
  //herramientas digitales
  {
    path: "/herramientas-digitales",
    name: "herramientas-digitales",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/main/herramientas-digitales.vue"
      ),
  },
  //juegos
  {
    path: "/juegos-main",
    name: "juegos-main",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/main/juegos-main.vue"),
  },
  //material adicional
  {
    path: "/material-adicional",
    name: "material-adicional",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/main/material-adicional.vue"
      ),
  },
  //tips
  {
    path: "/tips-main",
    name: "tips-main",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/main/tips-main.vue"),
  },
  //tutoriales
  {
    path: "/tutoriales-main",
    name: "tutoriales-main",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/main/tutoriales-main.vue"
      ),
  },
  //Modelo de clases
  {
    path: "/modelo-de-clases",
    name: "modelo-de-clases",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/main/modelo-de-clases.vue"
      ),
  },
  //inicio de sesion
  //login
  {
    path: "/login-is",
    name: "login-is",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/inicio-sesion/login-is.vue"
      ),
  },
  //password
  {
    path: "/password-is",
    name: "password-is",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/inicio-sesion/password-is.vue"
      ),
  },
  //sign up
  {
    path: "/sign-up",
    name: "sign-up",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/inicio-sesion/sign-up.vue"
      ),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
