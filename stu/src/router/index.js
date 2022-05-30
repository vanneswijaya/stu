import { createWebHistory, createRouter } from "vue-router";
import Home from "../components/Home.vue";
import Lending from "../components/Lending.vue";
import Exchange from "../components/Exchange.vue";
import InstantExchange from "../components/InstantExchange.vue";
import PlannedExchange from "../components/PlannedExchange.vue";
import Currency from "../components/Currency.vue";
import Expense from "../components/Expense.vue";

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
  {
    path: "/exchange",
    name: "exchange",
    component: Exchange,
    meta: {
      footer: false,
      onPage: "exchange",
    },
  },
  {
    path: "/instant-exchange",
    name: "instant-exchange",
    component: InstantExchange,
    meta: {
      footer: false,
      onPage: "instant-exchange",
    },
  },
  {
    path: "/planned-exchange",
    name: "planned-exchange",
    component: PlannedExchange,
    meta: {
      footer: false,
      onPage: "planned-exchange",
    },
  },
  {
    path: "/currency",
    name: "currency",
    component: Currency,
    meta: {
      footer: false,
      onPage: "currency",
    },
  },
  {
    path: "/expense",
    name: "expense",
    component: Expense,
    meta: {
      footer: false,
      onPage: "expense",
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
