<template>

  <h1> S3とRDS </h1>

  <div class="my-3">
    <router-link v-bind:to="{name: 'home'}" class="btn btn-primary mx-2">
      Home
    </router-link>
    <router-link v-bind:to="{name: 'upload'}" class="btn btn-primary mx-2">
      Upload
    </router-link>
    <router-link v-bind:to="{name: 'delete'}" class="btn btn-primary mx-2">
      Delete
    </router-link>  
  </div>

  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
}
</script>
