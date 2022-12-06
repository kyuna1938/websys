<template>
  <RankPage />
  <PieChart />
</template>

<script>
import RankPage from './components/RankPage.vue';
import PieChart from './components/PieChart.vue';

export default {
  name: 'App',
  components: {
    RankPage,
    PieChart
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
