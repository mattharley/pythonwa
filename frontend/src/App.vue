<template>
  <div id="app">
    <el-row>
      <el-col :span="16" :offset="4">
        <img alt="Vue logo" src="./assets/logo.png">
        <HelloPDPD></HelloPDPD>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import HelloPDPD from './components/HelloPDPD.vue'

export default {
  name: 'app',
  components: {
    HelloPDPD
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
