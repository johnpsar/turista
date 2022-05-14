import { createApp } from 'vue'
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import router from "./router";
//Primevue
import PrimeVue from 'primevue/config';
import "primeicons/primeicons.css";
import "primevue/resources/themes/saga-purple/theme.css";
import "primevue/resources/primevue.min.css";
createApp(App).use(router).use(PrimeVue).mount('#app')
