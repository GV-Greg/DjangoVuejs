<template>
  <div class="subject-navigator">
    <!-- Fil d'Ariane -->
    <nav aria-label="breadcrumb" class="mb-4">
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a href="#" @click.prevent="goToProgram">{{ program.name }}</a>
        </li>
        <li v-for="(subject, index) in subjectPath" 
            :key="subject.id" 
            class="breadcrumb-item"
            :class="{ active: index === subjectPath.length - 1 }">
          <template v-if="index === subjectPath.length - 1">
            {{ subject.title }}
          </template>
          <a v-else 
             href="#" 
             @click.prevent="navigateToSubject(subject, index)">
            {{ subject.title }}
          </a>
        </li>
      </ol>
    </nav>

    <!-- Liste des sujets -->
    <div v-if="currentSubjects.length > 0" class="subjects-list mb-4">
      <div class="list-group">
        <a v-for="subject in currentSubjects"
           :key="subject.id"
           href="#"
           class="list-group-item list-group-item-action"
           :class="{ 'active': currentSubject?.id === subject.id }"
           @click.prevent="selectSubject(subject)">
          <h5 class="mb-1">{{ subject.title }}</h5>
          <p class="mb-1" v-if="subject.description">{{ subject.description }}</p>
          <small>
            {{ subject.sub_subjects?.length ? `${subject.sub_subjects.length} sous-sujets` : '' }}
            {{ subject.questions?.length ? `${subject.questions.length} questions` : '' }}
          </small>
        </a>
      </div>
    </div>

    <!-- Questions du sujet actuel -->
    <div v-if="currentSubject?.questions?.length" class="questions-section">
      <h4 class="mb-3">Questions sur {{ currentSubject.title }}</h4>
      <div class="list-group">
        <a v-for="question in currentSubject.questions"
           :key="question.id"
           href="#"
           class="list-group-item list-group-item-action"
           @click.prevent="selectQuestion(question)">
          {{ question.text }}
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
  program: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['question-selected', 'reset'])

const API_URL = import.meta.env.VITE_API_URL
const currentSubjects = ref([])
const currentSubject = ref(null)
const subjectPath = ref([])

onMounted(async () => {
  await loadRootSubjects()
})

watch(() => props.program, async () => {
  await loadRootSubjects()
})

const loadRootSubjects = async () => {
  try {
    const response = await axios.get(`${API_URL}/api/subjects/by_program/?program_id=${props.program.id}`)
    currentSubjects.value = response.data
    currentSubject.value = null
    subjectPath.value = []
  } catch (error) {
    console.error('Error loading subjects:', error)
  }
}

const selectSubject = async (subject) => {
  currentSubject.value = subject
  subjectPath.value.push(subject)

  if (subject.sub_subjects?.length > 0) {
    currentSubjects.value = subject.sub_subjects
  } else {
    currentSubjects.value = []
  }
}

const navigateToSubject = async (subject, index) => {
  subjectPath.value = subjectPath.value.slice(0, index + 1)
  currentSubject.value = subject
  
  if (subject.sub_subjects?.length > 0) {
    currentSubjects.value = subject.sub_subjects
  } else {
    currentSubjects.value = []
  }
}

const selectQuestion = (question) => {
  emit('question-selected', question)
}

const goToProgram = () => {
  emit('reset')
}
</script>

<style scoped>
.subject-navigator {
  max-width: 800px;
  margin: 0 auto;
}

.breadcrumb {
  background-color: #f8f9fa;
  padding: 0.75rem 1rem;
  border-radius: 0.25rem;
}

.list-group-item {
  transition: all 0.2s ease;
}

.list-group-item:hover {
  background-color: #f8f9fa;
}
</style>
