import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

// Import du thème Solar de Bootswatch
import 'bootswatch/dist/solar/bootstrap.min.css'
// Import des styles personnalisés
import './assets/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
