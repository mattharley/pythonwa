<template>
    <div class="hello">
        <div v-for="talk in talks">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <div>
                        <div><a :href="talk.event_url ">{{ talk.event_name }}</a></div>
                    </div>
                </div>
                <div v-html="talk.event_description"></div>
            </el-card>
        </div>
    </div>
</template>

<script>
export default {
    name: 'TalkCollection',
    props: {
        talks: Array
    }
};
</script>

<style scoped>

</style>
