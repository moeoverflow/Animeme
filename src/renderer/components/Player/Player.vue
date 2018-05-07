<template>
  <div id="player">
    <div class="container">
      <display-screen></display-screen>
    </div>
    <div class="container">
      <progress-bar></progress-bar>
    </div>
    <div class="container">
      <play-controller></play-controller>
    </div>
  </div>
</template>

<script>
  import DisplayScreen from './DisplayScreen'
  import ProgressBar from './ProgressBar'
  import PlayController from './PlayController'

  export default {
    name: 'player',
    components: {
      DisplayScreen,
      ProgressBar,
      PlayController
    },
    methods: {}
  }
</script>

<style>
  #player {
    padding: 12px 0 12px 12px;
  }

  .container {
    margin: 8px 0;
  }
</style>
