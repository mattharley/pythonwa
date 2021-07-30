<template>
    <section id="sponsors">
        <div class="mt-20 text-center">
            <p class="max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-2xl md:max-w-3xl">
                Thanks to our awesome sponsors
            </p>
        </div>
        <div class="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8 flex items-center">
            <div class="grid grid-cols-2 gap-8 md:grid-cols-6 lg:grid-cols-5">
                <div class="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
                    <a href="https://hipflaskapp.com/">
                        <img class="h-12" src="../assets/hipflask.png" alt="Hipflask" />
                    </a>
                </div>
                <div class="col-span-1 flex justify-center md:col-span-3 lg:col-span-1">
                    <a href="http://robin.com.au">
                        <div class="flex">
                            <ChatIcon class="h-10"/> <span class="ml-1 mt-1 text-2xl">robin.com.au</span>
                        </div>
                    </a>
                </div>
                <div class="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
                    <a href="https://www.nowhereman.com.au/">
                        <img class="h-12" src="../assets/nowhereman.png" alt="Nowhereman Brewing" />
                    </a>
                </div>
                <div class="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
                    <a href="https://nform.com.au/">
                        <img class="h-12" src="../assets/nform.png" alt="nForm" />
                    </a>
                </div>
                <div class="col-span-2 flex justify-center md:col-span-3 lg:col-span-1">
                    <a href="https://spacecubed.com/">
                        <img class="h-12" src="../assets/spacecubed.png" alt="Spacecubed" />
                    </a>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { ChatIcon } from "@heroicons/vue/outline";

export default {
    components: {
        ChatIcon,
    },
};
</script>    
