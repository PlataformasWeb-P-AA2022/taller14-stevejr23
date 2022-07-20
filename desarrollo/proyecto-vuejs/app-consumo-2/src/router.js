import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/index'
    },
    {
       path: "/create",
       name: "create",
       component: () => import("./components/Create.vue")
    },
    {
       path: "/edit/:id",
       name: "edit",
       component: () => import("./components/Edit.vue")
     },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/Index.vue")
    },
    {
      path: "/departamentos",
      name: "departamentos",
      component: () => import("./components/DepartamentosList.vue")
    },
    {
      path: "/create_departamentos",
      name: "create_departamentos",
      component: () => import("./components/CreateDepartamento.vue")
    },
    {
       path: "/edit_departamentos/:id",
       name: "edit_departamentos",
       component: () => import("./components/EditDepartamento.vue")
     },
  ]
});
