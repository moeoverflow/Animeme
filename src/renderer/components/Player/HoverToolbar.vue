<template>
  <div id="hover-toolbar">
    <div class="buttons has-addons is-centered">
      <span class="button is-primary is-inverted is-borderless">
        <i class="fas fa-play"></i>
      </span>
      <span class="button is-primary is-inverted is-borderless">
        <i class="fas fa-compress"></i>
      </span>
      <span class="button is-primary is-inverted is-borderless">
        <i class="fas fa-search-minus"></i>
      </span>
      <span class="button is-primary is-inverted is-borderless">
        <i class="fas fa-search-plus"></i>
      </span>
    </div>
  </div>
</template>

<script>
  import fontawesome from '@fortawesome/fontawesome'
  import faPlay from '@fortawesome/fontawesome-free-solid/faPlay'
  import faSearchPlus from '@fortawesome/fontawesome-free-solid/faSearchPlus'
  import faSearchMinus from '@fortawesome/fontawesome-free-solid/faSearchMinus'
  import faCompress from '@fortawesome/fontawesome-free-solid/faCompress'

  fontawesome.library.add(faPlay)
  fontawesome.library.add(faSearchPlus)
  fontawesome.library.add(faSearchMinus)
  fontawesome.library.add(faCompress)

  export default {
    name: 'hover-toolbar',
    components: {},
    methods: {}
  }
</script>

<style scoped lang="scss">
  @import "~bulma/sass/utilities/_all";
  @import "~bulma/sass/base/_all";
  @import "~bulma/sass/elements/button";

  #player #hover-toolbar {
    position: absolute;
    left: 50%;
    bottom: 12px;
    transform: translate(-50%, 0);
  }

</style>
