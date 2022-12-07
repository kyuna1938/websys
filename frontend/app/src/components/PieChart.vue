// PieChart.vue
<template>
  <h1>{{ ratings.name }} の購入者の性別比</h1>
  <div>
    <canvas id="pie-chart" width="400" height="400"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';

export default {
  data() {
    return {
      ratings: [],
      index: '',
    }
  },
  methods: {
    renderChart(){
      let ctx = document.getElementById("pie-chart");
      new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ["男性", "女性", "その他"],
          datasets: [{
            data: [this.ratings.man, this.ratings.woman, this.ratings.other]
          }]
        },
        options: {
          responsive: false,
        }
      });
    },
    getRatio: async function(){
      const id = this.index;
      const url = process.env.VUE_APP_API_DEV + '/ranks/' + id
      await axios.get(url)
        .then(response => {
          this.ratings = response.data;
      });
      this.renderChart();
    }
  },
  beforeMount (){
    this.index = this.$route.params.index;
  },
  mounted () {
    this.getRatio();
  }
}
</script>

<style>
#pie-chart {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>