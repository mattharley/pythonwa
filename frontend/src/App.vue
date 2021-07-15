<template>
  <div class="bg-gray-50">
    <Header />
    <Talks />
    <Photos />
    <Sponsors />
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Photos from './components/Photos.vue';
import Sponsors from './components/Sponsors.vue';
import Talks from './components/Talks.vue';

export default {
  components: {
    Header,
    Photos,
    Sponsors,
    Talks
  }
};
</script>

