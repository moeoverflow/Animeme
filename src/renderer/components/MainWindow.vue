<template>
  <div class="columns is-gapless is-flex-tablet" id="wrapper">
    <div class="column is-9 player-area">
      <player></player>
    </div>
      <div class="column is-3 panel-area">
        <panel></panel>
      </div>
  </div>
</template>

<script>
  import Player from './Player/Player'
  import Panel from './Panels/Panel'

  export default {
    name: 'main-window',
    components: {
      Player,
      Panel
    },
    methods: {}
  }
</script>

<style lang="scss">
  @import "~bulma/sass/utilities/_all";
  @import "~bulma/sass/grid/columns";

  body {
    margin: 0;
    background-color: #313131;
  }
  #wrapper {
    height: 100vh;
  }
  
  .player-area {
    background-color: #202020;
  }

  .panel-area {
    background-color: #313131;
  }
</style>
