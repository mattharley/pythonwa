<template>
    <section id="talks" class="md:max-w-4xl mx-auto">
        <teleport to="body">
            <TransitionRoot as="template" :show="openModal">
                <Dialog as="div" static class="fixed z-10 inset-0 overflow-y-auto" @close="open = false" :open="open">
                    <div class="flex items-center justify-center min-h-screen p-2 xs:pt-4 xs:px-4 text-center sm:block sm:p-0">
                        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                            <DialogOverlay class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
                        </TransitionChild>

                        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
                        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                            <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-sm w-full sm:p-6">
                                <div class="flex justify-between">
                                    <div></div>
                                    <div>
                                        <button type="button" class="bg-white rounded-md text-gray-400 hover:text-gray-500" @click="closeModal">
                                            <span class="sr-only">Close</span>
                                            <XIcon class="h-6 w-6" aria-hidden="true" />
                                        </button>
                                    </div>
                                </div>
                                <div v-if="success" class="py-2 text-center">
                                    <span class="inline-flex items-center px-5 py-2 rounded-md text-sm font-medium bg-green-100 text-green-800">
                                        {{ success }}
                                    </span>
                                </div>
                                <div v-else-if="error" class="py-2 text-center space-y-6">
                                    <span class="inline-flex items-center px-5 py-2 rounded-md text-sm font-medium bg-red-100 text-red-800">
                                        {{ error }}
                                    </span>
                                    <div>
                                        <a @click.prevent="error = ''" href="#">
                                            Try again?
                                        </a>
                                    </div>
                                </div>
                                <div v-else>
                                    <form class="space-y-6" @submit.prevent="onSubmit">
                                        <div>
                                            <label for="email" class="block text-sm font-medium text-gray-700">
                                                Name
                                            </label>
                                            <div class="mt-1">
                                                <input v-model="form.name" id="name" name="name" required="true" class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
                                            </div>
                                        </div>

                                        <div>
                                            <label for="email" class="block text-sm font-medium text-gray-700">
                                                Email address
                                            </label>
                                            <div class="mt-1">
                                                <input v-model="form.email" id="email" name="email" type="email" autocomplete="email" required="true" class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
                                            </div>
                                        </div>

                                        <div>
                                            <label for="email" class="block text-sm font-medium text-gray-700">
                                                Topic (optional)
                                            </label>
                                            <div class="mt-1">
                                                <input v-model="form.topic" id="topic" name="topc" class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
                                            </div>
                                        </div>

                                        <div>
                                            <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                                                Send
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </TransitionChild>
                    </div>
                </Dialog>
            </TransitionRoot>
        </teleport>

        <div class="bg-white border-b px-4 py-5 sm:px-6 shadow rounded-t-md">
            <div class="-ml-4 -mt-2 flex items-center justify-between flex-wrap sm:flex-nowrap">
                <div class="ml-4 mt-2">
                    <h3 class="text-lg leading-6 font-medium text-gray-900">
                        Upcoming Talks
                    </h3>
                </div>
                <div class="ml-4 mt-2 flex-shrink-0">
                    <button @click="openModal = true" type="button" class="relative inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
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
                            <div class="talk-description" v-html="talk.description"></div>
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
    Dialog, 
    DialogOverlay, 
    DialogTitle, 
    TransitionChild, 
    TransitionRoot
} from '@headlessui/vue';

import { 
    ChatAlt2Icon, 
    ClockIcon, 
    LocationMarkerIcon, 
    UserCircleIcon,
    XIcon
} from '@heroicons/vue/outline';

export default {
    components: {
        Dialog, 
        DialogOverlay, 
        DialogTitle, 
        TransitionChild, 
        TransitionRoot,
        ChatAlt2Icon,
        ClockIcon,
        LocationMarkerIcon,
        UserCircleIcon,
        XIcon   
    },
    data() {
        return {
            talks: [],
            openModal: false,
            form: {
                name: '',
                email: '',
                topic: ''
            },
            success: '',
            error: ''
        }
    },
    mounted() {
        this.fetchTalks()
    },
    methods: {
        async fetchTalks() {
            const response = await fetch(`${import.meta.env.VITE_API_URL}/talks/future`);
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
        },
        async onSubmit() {
            try {
                const response = await fetch(
                    `${import.meta.env.VITE_API_URL}/talks/apply`, 
                    { 
                        method: 'POST', 
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(this.form)
                    }
                );
                this.success = 'Thank you for submitting your talk';
            } catch (error) {
                this.error = 'There was an error submitting your talk';
            }
        },
        async resetForm() {
            this.openModal = false;
            setTimeout(_ => {
                this.success = '';
                this.error = '';
                this.form = {
                    name: '',
                    email: '',
                    topic: ''
                };
            }, 500);
        },
        closeModal() {
            if (this.success) {
                this.resetForm();
                return;
            }
            this.openModal = false;
        }
    }
};
</script>

<style>
.talk-description  a{ 
    color: rgb(37, 99, 235);
}

.talk-description p {
    margin-block-start: 1em;
    margin-block-end: 1em;
}
</style>
