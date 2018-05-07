<template>
  <div id="panel">
    <div class="container">
      <div class="title">
        <img id="logo" src="~@/assets/logo.png" alt="animeme-app">
      </div>

      <div class="buttons has-addons is-centered is-marginless switch-area">
        <a class="button is-medium is-primary is-inverted is-outlined is-marginless">
          <span class="icon is-medium">
            <i class="fas fa-crop"></i>
          </span>
          <span>Crop</span>
        </a>
        <a class="button is-medium is-primary is-inverted is-outlined is-marginless">
          <span class="icon is-medium">
            <i class="fas fa-arrows-alt-v"></i>
          </span>
          <span>Resize</span>
        </a>
      </div>

      <div class="buttons has-addons is-centered is-marginless switch-area">
        <a class="button is-medium is-primary is-inverted is-outlined is-fullwidth">
          <span class="icon is-medium">
            <i class="fas fa-magic"></i>
          </span>
          <span>Magic</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
  import fontawesome from '@fortawesome/fontawesome'
  import faCrop from '@fortawesome/fontawesome-free-solid/faCrop'
  import faArrowsAltV from '@fortawesome/fontawesome-free-solid/faArrowsAltV'
  import faMagic from '@fortawesome/fontawesome-free-solid/faMagic'

  fontawesome.library.add(faCrop)
  fontawesome.library.add(faArrowsAltV)
  fontawesome.library.add(faMagic)

  export default {
    name: 'panel',
    components: {
    },
    methods: {}
  }
</script>

<style scoped lang="scss">
  @import "~bulma/sass/utilities/_all";
  @import "~bulma/sass/base/_all";
  @import "~bulma/sass/layout/_all";
  @import "~bulma/sass/elements/button";

  .switch-area {
    margin: 12px !important;
  }

  .buttons {
    .button {
      flex: 1;
    }
  }

  .title {
    margin: 8px 16px;

    #logo {
      width: 100%;
    }
  }
</style>
