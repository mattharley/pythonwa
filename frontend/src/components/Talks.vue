<template>
    <section id="talks" class="md:max-w-4xl mx-auto">
        <div class="bg-white border-b px-4 py-5 sm:px-6 shadow rounded-t-md">
            <div class="-ml-4 -mt-2 flex items-center justify-between flex-wrap sm:flex-nowrap">
                <div class="ml-4 mt-2">
                    <h3 class="text-lg leading-6 font-medium text-gray-900">
                        Upcoming Talks
                    </h3>
                </div>
                <div class="ml-4 mt-2 flex-shrink-0">
                    <button type="button" class="relative inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                        Apply to talk
                    </button>
                </div>
            </div>
        </div>
        <div class="bg-white shadow rounded-b-md">
            <ul class="divide-y divide-gray-200">
                <li v-for="talk in talks" :key="talk.link">
                    <div class="p-4 sm:p-6">
                        <a :href="talk.link" class="block hover:bg-gray-50">
                            <p class="font-medium text-blue-600 truncate">{{ talk.name }}</p>
                        </a>
                        <p class="mt-2 flex items-center text-sm text-gray-500">
                            <ClockIcon class="mr-1.5 h-5 w-5 text-gray-400" aria-hidden="true" />
                            <span class="truncate">{{ talk.time }}</span>
                        </p>
                        <p class="mt-2 flex items-center text-sm text-gray-500">
                            <LocationMarkerIcon class="mr-1.5 h-5 w-5 text-gray-400" aria-hidden="true" />
                            <span class="truncate">{{ talk.venue }}</span>
                        </p>
                        <p class="mt-2 flex items-center text-sm text-gray-500">
                            <UserCircleIcon class="mr-1.5 h-5 w-5 text-gray-400" aria-hidden="true" />
                            <span class="truncate">{{ talk.attendance }}</span>
                        </p>
                        <p class="mt-2 text-sm">
                            <div v-html="talk.description"></div>
                        </p>
                    </div>
                </li>
            </ul>
        </div>
    </section>
</template>

<script>
import { DateTime } from "luxon";

import { 
    ChatAlt2Icon, 
    ClockIcon, 
    LocationMarkerIcon, 
    UserCircleIcon 
} from '@heroicons/vue/outline';

export default {
    components: {
        ChatAlt2Icon,
        ClockIcon,
        LocationMarkerIcon,
        UserCircleIcon
    },
    data() {
        return {
            talks: []
        }
    },
    mounted() {
        this.fetchTalks()
    },
    methods: {
        async fetchTalks() {
            const response = await fetch(`${import.meta.env.VITE_API_URL}/events/future`);
            const talks = await response.json();
            this.talks = talks.map(talk => {
                const time = DateTime.fromMillis(talk.time).toLocaleString(DateTime.DATETIME_FULL);
                const venue = `${talk.venue.name} @ ${talk.venue.address_1}`;
                return {
                    name: talk.name,
                    time: time,
                    venue: venue,
                    attendance: talk.attendance,
                    description: talk.description,
                    link: talk.link
                }
            });
        }
    }
};
</script>

<style scoped>
a { 
    @apply text-blue-600
}
p {
    
}
</style>