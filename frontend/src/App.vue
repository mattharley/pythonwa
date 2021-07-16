<template>
  <div class="bg-gray-50">
    <Header />
    <Talks />
    <Photos />
    <Sponsors />
    <Code />
    <Footer />
  </div>
</template>

<script>
import Code from './components/Code.vue';
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';
import Photos from './components/Photos.vue';
import Sponsors from './components/Sponsors.vue';
import Talks from './components/Talks.vue';

export default {
  components: {
    Code,
    Footer,
    Header,
    Photos,
    Sponsors,
    Talks
  }
};
</script>

