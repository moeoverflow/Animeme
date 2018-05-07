<template>
  <div class="columns" id="wrapper">
    <div class="column is-9 player-area">
      <player></player>
    </div>
      <div class="column is-3 control-area">
        control area
      </div>
  </div>
</template>

<script>
  import Player from './Player/Player'

  export default {
    name: 'main-window',
    components: {
      Player
    },
    methods: {}
  }
</script>

<style>
  @import "~bulma/css/bulma.css";

  #wrapper {
    height: 100vh;
  }
  

  .player-area {
    background-color: cadetblue;
  }
  .control-area {
    background-color: chocolate;
  }
</style>
