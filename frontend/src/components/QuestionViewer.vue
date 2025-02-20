<template>
  <div class="question-viewer">
    <div class="card">
      <div class="card-body">
        <button class="btn btn-link mb-3" @click="$emit('back')">
          ← Retour aux sujets
        </button>
        
        <h3 class="card-title mb-4">{{ question.text }}</h3>
        
        <div v-if="answers.length > 0" class="answers-section">
          <div v-for="answer in answers" 
               :key="answer.id" 
               class="answer-card mb-4">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Réponse</h5>
                <p class="card-text">{{ answer.text }}</p>
                
                <div v-if="answer.documentation_text" class="documentation-text mt-3">
                  <h6>Documentation</h6>
                  <div class="documentation-content">
                    {{ answer.documentation_text }}
                  </div>
                </div>
                
                <div v-if="answer.documentation_url" class="mt-3">
                  <a :href="answer.documentation_url" 
                     target="_blank" 
                     class="btn btn-outline-warning">
                    Voir la documentation complète
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div v-else class="text-center py-4">
          <p class="text-muted">Chargement des réponses...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
  question: {
    type: Object,
    required: true
  }
})

const API_URL = import.meta.env.VITE_API_URL
const answers = ref([])

onMounted(async () => {
  await loadAnswers()
})

watch(() => props.question, async () => {
  await loadAnswers()
})

const loadAnswers = async () => {
  try {
    const response = await axios.get(`${API_URL}/api/answers/by_question/?question_id=${props.question.id}`)
    answers.value = response.data
  } catch (error) {
    console.error('Error loading answers:', error)
  }
}
</script>

<style scoped>
.question-viewer {
  max-width: 800px;
  margin: 0 auto;
}

.documentation-content {
  background-color: #f8f9fa;
  padding: 1rem;
  border-radius: 0.25rem;
  white-space: pre-wrap;
}

.answer-card {
  transition: all 0.3s ease;
}

.answer-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
