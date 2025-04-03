<template>
    <div class="dirhm-config container py-4">
      <div class="card">
        <div class="card-body">
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="card-title mb-0">Configuration DIRHM</h1>
            <router-link to="/dirhm" class="btn btn-outline-secondary">
              <v-icon name="hi-arrow-left" class="me-2" /> Retour
            </router-link>
          </div>
          
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
          
          <div v-else>
            <!-- Reste du contenu inchangé -->
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useConfigStore } from '@/stores/configStore'
  
  const configStore = useConfigStore()
  const showConfigForm = ref(false)
  const isSaving = ref(false)
  
  const configForm = ref({
    fusion: false
  })
  
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
  
  const saveConfig = async () => {
    isSaving.value = true
    
    try {
      // Création d'une nouvelle configuration (toujours active)
      await configStore.createConfig({
        fusion: configForm.value.fusion,
        active: true
      })
      
      showConfigForm.value = false
    } catch (error) {
      console.error('Erreur lors de la sauvegarde de la configuration:', error)
    } finally {
      isSaving.value = false
    }
  }
  
  const cancelForm = () => {
    configForm.value = {
      fusion: false
    }
    
    showConfigForm.value = false
  }
  
  // Fonction d'aide pour formater les dates
  const formatDate = (dateString) => {
    if (!dateString) return ''
    
    const options = { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    }
    
    return new Date(dateString).toLocaleDateString('fr-FR', options)
  }
  </script>
  
  <style lang="scss">
  @use '@/assets/scss/variables' as vars;
  @use '@/assets/scss/mixins' as mixins;
  
  .dirhm-config {
    max-width: 800px;
    margin: 0 auto;
  }
  </style>