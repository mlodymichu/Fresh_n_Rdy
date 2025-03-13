import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import {createPinia} from 'pinia'
import router from './router/router'

const app = createApp(App)

// app.use(createPinia())



createApp(App)
  .use(router)  // Użyj routera
  .mount('#app')