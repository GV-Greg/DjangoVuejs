<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import http from '@/services/api'

const fusion = ref(false)
const router = useRouter()

watch(fusion, async (value) => {
    await http.post('dirhm/config/', { fusion: value })
    .then((response) => {
        if(response.status === 201) {
            router.push({ name: 'dirhm-home' })
        }
    }).catch((error) => {
      console.error('Erreur lors de la mise à jour de la config :', error)
    })
})
</script>

<template>
  <div class="container py-4">
    <h2>Configurer l’application</h2>
    <div class="form-check form-switch mt-4">
      <input class="form-check-input" type="checkbox" v-model="fusion" id="fusionSwitch">
      <label class="form-check-label" for="fusionSwitch">
        Dirhm avec fusion H+ {{ fusion ? 'activée' : 'désactivée' }}
      </label>
    </div>
  </div>
</template>
