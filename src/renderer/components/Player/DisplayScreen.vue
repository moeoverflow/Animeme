<template>
  <div id="display-screen">
    <video loop="loop" muted="muted" autoplay="autoplay" playsinline="">
      <source src="https://animeloop.org/files/mp4_1080p/59a945347019f27433a48139.mp4" type="video/mp4">
    </video>
  </div>
</template>

<script>
  export default {
    name: 'display-screen',
    components: {},
    methods: {}
  }
</script>

<style scoped>
  video {
    width: 100%;
  }
</style>
