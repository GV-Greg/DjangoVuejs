<template>
    <div class="dirhm-home container py-4">
      <div class="card">
        <div class="card-body">
          <h1 class="card-title mb-4">DIRHM</h1>
          
          <div v-if="configStore.isLoading" class="text-center py-4">
            <div class="spinner-border text-warning" role="status">
              <span class="visually-hidden">Chargement...</span>
            </div>
            <p class="mt-2">Chargement des données...</p>
          </div>
          
          <div v-else-if="configStore.error" class="alert alert-danger">
            {{ configStore.error }}
            <button class="btn btn-sm btn-outline-danger ms-2" @click="checkConfig">
              Réessayer
            </button>
          </div>
          
          <div v-else class="text-center py-4">
            <h2 class="mb-4">Bienvenue dans l'interface DIRHM</h2>
            
            <div class="config-status mb-4">
              <div v-if="configStore.hasConfig" class="alert alert-success">
                <strong>État de la configuration:</strong> 
                <span class="badge ms-2" :class="configStore.isFusionEnabled ? 'bg-success' : 'bg-secondary'">
                  Fusion {{ configStore.isFusionEnabled ? 'Activée' : 'Désactivée' }}
                </span>
              </div>
              
              <div v-else class="alert alert-warning">
                Aucune configuration active n'est définie.
              </div>
            </div>
            
            <router-link to="/dirhm/config" class="btn btn-warning btn-lg">
              <v-icon name="hi-cog" class="me-2" /> 
              {{ configStore.hasConfig ? 'Gérer la configuration' : 'Créer une configuration' }}
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { useConfigStore } from '@/stores/configStore'
  
  const configStore = useConfigStore()
  
  // Charger les données au montage du composant
  onMounted(async () => {
    await checkConfig()
  })
  
  const checkConfig = async () => {
    try {
      await configStore.checkIfConfigExists()
    } catch (error) {
      console.error('Erreur lors du chargement des données:', error)
    }
  }
  </script>
  
  <style scoped lang="scss">
  .dirhm-home {
    max-width: 800px;
    margin: 0 auto;
  }
  </style>