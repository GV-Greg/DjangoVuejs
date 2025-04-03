<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark mb-4">
      <div class="container">
        <router-link class="navbar-brand" to="/">
          Application
        </router-link>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" 
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/">
                <v-icon name="hi-home" class="me-1" /> Accueil
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/dirhm">
                <v-icon name="hi-cog" class="me-1" /> DIRHM
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <router-view />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useConfigStore } from '@/stores/configStore'

const configStore = useConfigStore()

onMounted(async () => {
  // Vérifier si une configuration existe lors de l'initialisation de l'application
  await configStore.checkIfConfigExists()
})
</script>

<style scoped>

</style>