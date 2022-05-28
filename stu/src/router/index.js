import { createWebHistory, createRouter } from "vue-router";
import Home from "../components/Home.vue";
import Lending from "../components/Lending.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      footer: false,
      onPage: "home",
    },
  },
  {
    path: "/lending",
    name: "Lending",
    component: Lending,
    meta: {
      footer: false,
      onPage: "lending",
    },
  },
];

const router = createRouter({
  mode: "history",
  history: createWebHistory(),
  routes,
  //   scrollBehavior(to, from, savedPosition) {
  //     return new Promise((resolve, reject) => {
  //       setTimeout(() => {
  //         resolve({ left: 0, top: 0, behavior: "smooth" });
  //       }, 300);
  //     });
  //   },
});

export default router;
