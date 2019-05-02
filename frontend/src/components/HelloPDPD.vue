<template>
    <div class="hello">
        <h1>Talks!</h1>

        <el-tabs v-model="active_tab">
            <el-tab-pane label="Upcoming" name="upcoming">
                <div v-for="talk in upcomingTalks">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <div>
                                <div><a :href="talk.event_url ">{{ talk.event_name }}</a></div>
                            </div>
                        </div>
                        <div v-html="talk.event_description"></div>
                    </el-card>
                </div>
            </el-tab-pane>

            <el-tab-pane label="Past" name="past">
                <p>Only show Robin's talks? <el-switch v-model="robin"></el-switch></p>
                <div v-for="talk in pastTalks" v-if="!robin || (robin && talk.og_event_description.indexOf('Robin') >= 0)">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <div>
                                <div><a :href="talk.event_url ">{{ talk.event_name }}</a></div>
                            </div>
                        </div>
                        <div v-html="talk.event_description"></div>
                    </el-card>
                </div>
            </el-tab-pane>
        </el-tabs>

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
