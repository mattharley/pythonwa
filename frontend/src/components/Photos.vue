<template>
  <div class="md:max-w-xl mx-auto">
    <div class="text-center">
      <Carousel>
        <Slide v-for="index in 8" :key="index">
          <img :src="`/src/assets/photo${index}.jpeg`" />
        </Slide>
        <template #addons>
          <Navigation />
          <Pagination />
        </template>
      </Carousel>
    </div>
  </div>
</template>

<script>
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default {
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data() {
    return {
      items: new Array(8)
    }
  }
};
</script>
