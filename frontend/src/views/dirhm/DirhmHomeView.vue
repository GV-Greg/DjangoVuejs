<script setup>
    import { ref, onMounted } from 'vue'
    import { useRouter } from 'vue-router'
    import http from '@/services/api'

    const router = useRouter()
    const hasConfig = ref(false)
    const fusionEnabled = ref(false)

    onMounted(async () => {
        try {
            const { data } = await http.get('dirhm/config/')
            hasConfig.value = data.exists
            fusionEnabled.value = data.fusion_enabled
        } catch (e) {
            hasConfig.value = false
        }
    })

    const goToConfig = () => {
        router.push({ name: 'dirhm-config' })
    }
</script>

<template>
    <div class="container py-4 text-center">
      <h2>Bienvenue dans l'interface DIRHM</h2>
      <p v-if="hasConfig" class="text-success">
        Configuration active – Fusion {{ fusionEnabled ? 'activée' : 'désactivée' }}
      </p>
      <p v-else class="text-warning">Aucune configuration active.</p>
  
      <button class="btn btn-warning btn-lg mt-4" @click="goToConfig">
        {{ hasConfig ? 'Gérer la configuration' : 'Configurer l’application' }}
      </button>
    </div>
  </template>