<template>
  <div class="program-selector">
    <h2 class="mb-4">Sélectionnez votre programme</h2>
    <div v-if="error" class="alert alert-danger">
      {{ error }}
    </div>
    <div class="row">
      <div v-for="program in programs" 
           :key="program.id" 
           class="col-md-4 mb-4">
        <div class="card h-100" 
             :class="{ 'border-warning': selectedProgram?.id === program.id }"
             @click="selectProgram(program)">
          <div class="card-body text-center">
            <h3 class="card-title">{{ program.name }}</h3>
            <p class="card-text">{{ program.description }}</p>
            <button class="btn" 
                    :class="selectedProgram?.id === program.id ? 'btn-warning' : 'btn-outline-warning'"
                    @click.stop="confirmProgram(program)">
              Sélectionner
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- Debug info -->
    <div class="mt-4 p-3 bg-dark text-warning" style="border-radius: 4px;">
      <pre>Nombre de programmes : {{ programs.length }}
Programmes : {{ JSON.stringify(programs, null, 2) }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
console.log('API_URL:', API_URL)

const programs = ref([])
const selectedProgram = ref(null)
const error = ref(null)

const emit = defineEmits(['program-selected'])

onMounted(async () => {
  try {
    console.log('Fetching programs...')
    const response = await axios.get(`${API_URL}/api/programs/available_programs/`)
    console.log('Response:', response.data)
    programs.value = response.data
  } catch (error) {
    console.error('Error fetching programs:', error)
    error.value = `Erreur lors du chargement des programmes: ${error.message}`
  }
})

const selectProgram = (program) => {
  selectedProgram.value = program
}

const confirmProgram = (program) => {
  selectedProgram.value = program
  emit('program-selected', program)
}
</script>

<style scoped>
.card {
  cursor: pointer;
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.card.border-warning {
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

pre {
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>
