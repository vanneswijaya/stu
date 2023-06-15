import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { vfmPlugin } from 'vue-final-modal'
import "./index.css";

const app = createApp(App).use(router).use(vfmPlugin).mount("#app");