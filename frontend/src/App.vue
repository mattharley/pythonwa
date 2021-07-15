<template>
  <div class="bg-gray-50">
    <Header />
    <Photos />
    <Sponsors />
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Photos from './components/Photos.vue';
import Sponsors from './components/Sponsors.vue';

export default {
  components: {
    Header,
    Photos,
    Sponsors
  }
};
</script>

