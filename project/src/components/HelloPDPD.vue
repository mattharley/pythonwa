<template>
    <div id="app">
        <h3>My talks</h3>
        <ul>
            <li v-for="talk in talks" v-bind:key="talk.event_name">{{ talk.event_name }}</li>
        </ul>
        <pre>{{ talks }}</pre>
    </div>
</template>

<script>
var axios = require('axios');
var api_url = 'http://localhost:8000/meetupsapi/upcoming';

export default {
  name: 'HelloPDPD',
  data() {
      return {
          talks: []
      };
  },
  mounted() {
      axios.get(api_url)
          .then(this.on_response);
  },
  methods: {
      on_response(response) {
          this.talks = response.data.events;
      }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
