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
            <!-- Configuration existante -->
            <div v-if="configStore.hasConfig" class="config-details">
              <div class="alert alert-success">
                <v-icon name="hi-check" class="me-2" /> <strong>Configuration active</strong>
              </div>
              
              <div class="mb-4">
                <h4>Détails de la configuration actuelle</h4>
                <div class="table-responsive">
                  <table class="table table-striped">
                    <tbody>
                      <tr>
                        <th scope="row">Identifiant</th>
                        <td>{{ configStore.currentConfig.id }}</td>
                      </tr>
                      <tr>
                        <th scope="row">Fusion</th>
                        <td>
                          <span class="badge" :class="configStore.isFusionEnabled ? 'bg-success' : 'bg-secondary'">
                            {{ configStore.isFusionEnabled ? 'Activée' : 'Désactivée' }}
                          </span>
                        </td>
                      </tr>
                      <tr>
                        <th scope="row">Date de création</th>
                        <td>{{ formatDate(configStore.currentConfig.created_at) }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              
              <div>
                <button class="btn btn-warning" @click="showConfigForm = true">
                  <v-icon name="hi-cog" class="me-2" /> Créer une nouvelle configuration
                </button>
              </div>
            </div>
            
            <!-- Aucune configuration existante -->
            <div v-else class="text-center py-3">
              <div class="alert alert-info">
                <v-icon name="hi-information-circle" class="me-2" /> Aucune configuration active n'a été trouvée. Veuillez créer une nouvelle configuration.
              </div>
              <button class="btn btn-warning" @click="showConfigForm = true">
                <v-icon name="hi-cog" class="me-2" /> Créer une configuration
              </button>
            </div>
            
            <!-- Formulaire de configuration -->
            <div v-if="showConfigForm" class="config-form mt-4">
              <div class="card">
                <div class="card-header">
                  Nouvelle configuration
                </div>
                <div class="card-body">
                  <form @submit.prevent="saveConfig">
                    <div class="mb-3 form-check">
                      <input type="checkbox" class="form-check-input" id="fusion" v-model="configForm.fusion">
                      <label class="form-check-label" for="fusion">Activer la fusion</label>
                    </div>
                    
                    <div class="d-flex justify-content-between">
                      <button type="button" class="btn btn-secondary" @click="cancelForm">
                        <v-icon name="hi-x" class="me-2" /> Annuler
                      </button>
                      <button type="submit" class="btn btn-warning" :disabled="isSaving">
                        <span v-if="isSaving" class="spinner-border spinner-border-sm me-2" role="status"></span>
                        <v-icon v-else name="hi-check" class="me-2" /> Créer
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
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
  @import '@/assets/scss/variables';
  @import '@/assets/scss/mixins';
  
  .dirhm-config {
    max-width: 800px;
    margin: 0 auto;
  }
  </style>