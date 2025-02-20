<template>
  <div class="decision-tree container py-4">
    <!-- Sélection du programme -->
    <ProgramSelector v-if="!selectedProgram"
                    @program-selected="selectProgram" />

    <!-- Navigation dans les sujets -->
    <SubjectNavigator v-else-if="!selectedQuestion"
                     :program="selectedProgram"
                     @question-selected="selectQuestion"
                     @reset="reset" />

    <!-- Affichage des questions et réponses -->
    <QuestionViewer v-else
                   :question="selectedQuestion"
                   @back="selectedQuestion = null" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProgramSelector from './ProgramSelector.vue'
import SubjectNavigator from './SubjectNavigator.vue'
import QuestionViewer from './QuestionViewer.vue'

const selectedProgram = ref(null)
const selectedQuestion = ref(null)

const selectProgram = (program) => {
  selectedProgram.value = program
  selectedQuestion.value = null
}

const selectQuestion = (question) => {
  selectedQuestion.value = question
}

const reset = () => {
  selectedProgram.value = null
  selectedQuestion.value = null
}
</script>

<style scoped>
.decision-tree {
  min-height: 100vh;
  padding-bottom: 2rem;
}
</style>
