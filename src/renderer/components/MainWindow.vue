<template>
  <div id="wrapper">
    <div class="topbar">
      <top-bar></top-bar>
    </div>
    <div class="columns is-gapless content">
      <div class="column is-9 player-area">
        <player></player>
      </div>
        <div class="column is-3 panel-area">
          <panel></panel>
        </div>
    </div>
  </div>
</template>

<script>
  import TopBar from './TopBar/TopBar'
  import Player from './Player/Player'
  import Panel from './Panels/Panel'

  export default {
    name: 'main-window',
    components: {
      TopBar,
      Player,
      Panel
    },
    methods: {}
  }
</script>

<style lang="scss">
  @import "~bulma/sass/utilities/_all";
  @import "~bulma/sass/grid/columns";

  $background-color: #313131;
  $topbar-color: #161616;
  $player-color: #0f0f0f;

  body {
    margin: 0;
    background-color: $background-color;
  }
  #wrapper {
    height: 100vh;
  }

  $topbar-height: 80px;
  .topbar {
    height: $topbar-height;
    -webkit-app-region: drag;
    background-color: $topbar-color;
  }
  .content {
    position: absolute;
    top: $topbar-height;
    bottom: 0;
    width: 100%;
  }

  .player-area {
    background-color: $player-color;
  }

  .panel-area {
    background-color: $background-color;
  }
</style>
