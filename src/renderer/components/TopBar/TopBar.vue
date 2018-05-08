<template>
  <div id="top-bar">
    <div class="title">Animeme</div>
    <div class="tool-bar level">
      <div class="level-left">
        <p class="buttons has-addons">
          <a class="button">
            <span class="icon is-large">
              <i class="fas fa-file"></i>
            </span>
          </a>
        </p>
      </div>
      <div class="level-right">
        <p class="buttons has-addons">
          <a class="button">
            <span class="icon is-large">
              <i class="fas fa-info-circle"></i>
            </span>
          </a>
        </p>
        <p class="buttons has-addons">
          <a class="button">
            <span class="icon is-large">
              <i class="fas fa-cog"></i>
            </span>
          </a>
          <a class="button">
            <span class="icon is-large">
              <i class="fas fa-sign-out-alt"></i>
            </span>
          </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
  import fontawesome from '@fortawesome/fontawesome'
  import faFile from '@fortawesome/fontawesome-free-solid/faFile'
  import faCog from '@fortawesome/fontawesome-free-solid/faCog'
  import faInfoCircle from '@fortawesome/fontawesome-free-solid/faInfoCircle'
  import faSignOutAlt from '@fortawesome/fontawesome-free-solid/faSignOutAlt'

  fontawesome.library.add(faFile)
  fontawesome.library.add(faCog)
  fontawesome.library.add(faInfoCircle)
  fontawesome.library.add(faSignOutAlt)

  export default {
    name: 'top-bar',
    components: {
    },
    methods: {}
  }
</script>

<style scoped lang="scss">
  @import "~bulma/sass/utilities/_all";
  @import "~bulma/sass/base/_all";
  @import "~bulma/sass/components/level";

  $button-color: #c1c1c1;
  $button-background-color: #313131;
  $button-border-width: 0;
  $button-hover-color: #fff;
  @import "~bulma/sass/elements/button";

  .title {
    padding: 2px;
    text-align: center;
    color: lightgray;
    font-size: 0.9rem;
  }

  .tool-bar {
    height: 59px;
  }

  .buttons {
    margin-left: 12px;
    margin-right: 12px;
    margin-bottom: -0.5em !important;

    .button {
      width: 30px;
      height: 30px;
      padding: 5px;
    }
  }
</style>
