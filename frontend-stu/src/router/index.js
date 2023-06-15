import { createWebHistory, createRouter } from "vue-router";
import Home from "../components/Home.vue";
import Lending from "../components/Lending.vue";
import LendingDetails from "../components/LendingDetails.vue";
import Exchange from "../components/Exchange.vue";
import InstantExchange from "../components/InstantExchange.vue";
import PlannedExchange from "../components/PlannedExchange.vue";
import Currency from "../components/Currency.vue";
import Expense from "../components/Expense.vue";
import Budgeting from "../components/Budgeting.vue";
import Completed from "../components/Completed.vue";

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
    path: "/completed",
    name: "Completed",
    component: Completed,
    meta: {
      footer: false,
      onPage: "completed",
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
    path: "/lending-details",
    name: "LendingDetails",
    component: LendingDetails,
    meta: {
      footer: false,
      onPage: "lending-details",
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
  {
    path: "/budgeting",
    name: "budgeting",
    component: Budgeting,
    meta: {
      footer: false,
      onPage: "budgeting",
    },
  },
];

const router = createRouter({
  mode: "history",
  history: createWebHistory(),
  routes,
    scrollBehavior(to, from, savedPosition) {
      return new Promise((resolve, reject) => {
        if (to.path == '/completed') {
          setTimeout(() => {
            resolve({ left: 0, top: 0});
          }, 0);
        } else {
          setTimeout(() => {
            resolve({ left: 0, top: 0, behavior: "smooth"});
          }, 0);
        }
      });
    },
});

export default router;
