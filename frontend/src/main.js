import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

// Import Oh Vue Icons
import { OhVueIcon, addIcons } from 'oh-vue-icons'
import { 
  HiHome, 
  HiCog, 
  HiArrowRight, 
  HiArrowLeft, 
  HiCheck, 
  HiExclamation, 
  HiInformationCircle, 
  HiX 
} from 'oh-vue-icons/icons'

// Import Bootstrap JS pour la navbar
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// Import des styles Sass
import './assets/scss/main.scss'

// Ajouter les icônes que nous utiliserons
addIcons(
    HiHome, 
    HiCog, 
    HiArrowRight, 
    HiArrowLeft, 
    HiCheck, 
    HiExclamation, 
    HiInformationCircle, 
    HiX
  )

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.component('v-icon', OhVueIcon)

app.mount('#app')
