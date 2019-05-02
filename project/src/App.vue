<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloPDPD api-url="http://localhost:8000/meetupsapi/upcoming" @rendered="onRender"/>
  </div>
</template>

<script>
import HelloPDPD from './components/HelloPDPD.vue'

export default {
  name: 'app',
  components: {
    HelloPDPD
  },
  methods: {
    onRender() {
      alert('rendered!');
    }
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
