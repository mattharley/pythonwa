<template>
    <div class="hello">
        <h1>Talks!</h1>
        <div v-for="talk in pastTalks" v-if="talk.og_event_description.indexOf('Robin') >= 0">
            <h2><a :href="talk.event_url" target="_blank">{{ talk.event_name }}</a></h2>
            <div v-html="talk.event_description"></div>
        </div>

    </div>
</template>

<script>
const axios = require('axios');
const upcomingUrl = 'http://localhost:8000/meetupsapivue/upcoming'
const pastUrl = 'http://localhost:8000/meetupsapivue/past'

export default {
    name: 'HelloPDPD',
    data() {
        return {
            upcomingTalks: [],
            pastTalks: [],
            active_tab: 'upcoming',
            robin: true
        };
    },
    mounted() {
        axios.get(upcomingUrl)
            .then((response) => this.upcomingTalks = response.data.events);

        axios.get(pastUrl)
            .then((response) => this.pastTalks = response.data.events);
    }
};
</script>

<style scoped>

</style>
