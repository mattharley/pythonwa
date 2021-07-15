<template>
  <div>
    <div class="mt-20 text-center">
      <p class="max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-2xl md:max-w-3xl">
        Thanks to our awesome sponsors
      </p>
    </div>
    <div class="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8 flex items-center">
      <div class="grid grid-cols-2 gap-8 md:grid-cols-6 lg:grid-cols-5">
        <div class="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
          <img class="h-12" src="../assets/hipflask.png" alt="Hipflask" />
        </div>
        <div class="col-span-1 flex justify-center md:col-span-3 lg:col-span-1">
          <ChatIcon class="h-10"/> <span class="ml-1 mt-1 text-2xl">robin.com.au</span>
        </div>
        <div class="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
          <img class="h-12" src="../assets/nowhereman.png" alt="Nowhereman Brewing" />
        </div>
        <div class="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
          <img class="h-12" src="../assets/nform.png" alt="nForm" />
        </div>
        <div class="col-span-2 flex justify-center md:col-span-3 lg:col-span-1">
          <img class="h-12" src="../assets/spacecubed.png" alt="Spacecubed" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ChatIcon } from '@heroicons/vue/outline';

export default {
  components: {
    ChatIcon
  }
}
</script>    
