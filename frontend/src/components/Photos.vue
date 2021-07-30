<template>
    <section id="photos" class="md:max-w-xl mx-auto">
        <div class="text-center">
            <Carousel>
                <Slide v-for="index in 8" :key="index">
                    <img :src="imageUrl(index)" />
                </Slide>
                <template #addons>
                    <Navigation />
                    <Pagination />
                </template>
            </Carousel>
        </div>
    </section>
</template>

<script>
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide, Pagination, Navigation } from "vue3-carousel";

export default {
    components: {
        Carousel,
        Slide,
        Pagination,
        Navigation
    },
    data() {
        return {
            items: new Array(8),
        };
    },
    methods: {
        imageUrl(index) {
            // need to do this because of the dynamic naming of images
            // see: https://vitejs.dev/guide/assets.html#new-url-url-import-meta-url
            return new URL(`../assets/photo${index}.jpeg`, import.meta.url);
        }
    }
};
</script>

<style>
@tailwind screens;

.carousel__prev {
    transform: translate(25%, -50%);
}
.carousel__next {
    transform: translate(-25%, -50%);
}

@screen md {
    .carousel__prev {
        transform: translate(-50%, -50%);
    }
    .carousel__next {
        transform: translate(50%, -50%);
    }
}
</style>