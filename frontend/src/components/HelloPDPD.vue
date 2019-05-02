<template>
    <div class="hello">
        <h1>Talks!</h1>

        <el-tabs v-model="active_tab">
            <el-tab-pane label="Upcoming" name="upcoming">
                <TalkCollection :talks="upcomingTalks"></TalkCollection>
            </el-tab-pane>

            <el-tab-pane label="Past" name="past">
                <TalkCollection :talks="pastTalks"></TalkCollection>
            </el-tab-pane>
        </el-tabs>

    </div>
</template>

<script>
import TalkCollection from './TalkCollection.vue'

const axios = require('axios')
const upcomingUrl = 'http://localhost:8000/meetupsapivue/upcoming'
const pastUrl = 'http://localhost:8000/meetupsapivue/past'

export default {
    name: 'HelloPDPD',
    components: {
        TalkCollection
    },
    data() {
        return {
            upcomingTalks: [],
            pastTalks: [],
            active_tab: 'upcoming'
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
