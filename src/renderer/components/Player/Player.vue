<template>
  <div id="player">
    <div class="has-vertically-aligned-content">
      <display-screen></display-screen>
    </div>
    <hover-toolbar></hover-toolbar>
  </div>
</template>

<script>
  import DisplayScreen from './DisplayScreen'
  import HoverToolbar from './HoverToolbar'

  export default {
    name: 'player',
    components: {
      DisplayScreen,
      HoverToolbar
    },
    methods: {}
  }
</script>

<style scoped lang="scss">
  #player {
    height: 100%;
    display: flex;
    position: relative;
  }

  /* make content vertically aligned */
  .has-vertically-aligned-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
</style>
