<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
      <div class="container">
        <router-link class="navbar-brand" to="/">
          Documentation Assistant
        </router-link>
      </div>
    </nav>

    <router-view />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import 'bootswatch/dist/lux/bootstrap.min.css'

onMounted(() => {
  console.log('Application montée')
})
</script>

<style>
#app {
  min-height: 100vh;
  background-color: #002B36;
}

.navbar {
  background-color: #073642 !important;
}

.navbar-brand {
  color: #B58900 !important;
  font-weight: bold;
}
</style>
