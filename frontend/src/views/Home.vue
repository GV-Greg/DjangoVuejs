<template>
  <div class="home">
    <router-link to="/dirhm" class="btn btn-warning btn-lg">
      <v-icon name="hi-arrow-right" class="me-2" /> Accéder à DIRHM
    </router-link>
  </div>
</template>

<script setup>
// Pas de logique requise
</script>

<style scoped lang="scss">
  .home {
    .btn-warning {
      // Utilisation des variables et mixins définies
      padding: $spacing-md $spacing-xl;
      font-size: 1.25rem;
      
      &:hover {
        background-color: darken($color-warning, 5%);
        transform: scale(1.05);
      }
    }
  }
</style>