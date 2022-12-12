<template>
    <div>
      <h1 class="mb-4">Y書店売り上げランキング</h1>
      <div class="mb-4">
        <form>
          <label>Start Date:</label>
          <input type="date" v-model="startDate">
          <label>End Date:</label>
          <input type="date" v-model="endDate">
        </form>
      </div>
      <table>
        <thead>
          <tr>
            <th>Rank</th>
            <th>Name</th>
            <th>quantity</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(ranking, index) in rankings" :key="ranking.name">
            <td>{{ index + 1 }}</td>
            <td><router-link :to="('/novel/' + ranking.book_id)">{{ ranking.name }}</router-link></td>
            <td>{{ ranking.quantity }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        startDate: '',
        endDate: '',
        rankings: []
      }
    },
    watch: {
      startDate: function() {
        this.getRankings()
      },
      endDate: function() {
        this.getRankings()
      }
    },
    methods: {
      getRankings() {
        const params = {
          start_date: this.startDate,
          end_date: this.endDate
        }
        const url = process.env.VUE_APP_API_DEV + '/ranks'
        axios.get(url, { params })
          .then(response => {
            this.rankings = response.data;
        })
      }
    },
    beforeMount() {
      const date = new Date()
      this.startDate = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
      this.endDate = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
    },
    mounted() {
      this.getRankings()
      
    }
  }
  </script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
}
th {
  text-align: left;
}
tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>
  