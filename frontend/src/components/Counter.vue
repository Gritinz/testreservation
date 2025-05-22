<template>
  <div>
    <h1>Compteur: {{ counter }}</h1>
    <button @click="updateCounter('increment')">+1</button>
    <button @click="updateCounter('decrement')">-1</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      counter: 0,
      apiUrl: 'https://votre-django.onrender.com '
    };
  },
  mounted() {
    this.getCounter();
  },
  methods: {
    async getCounter() {
      const response = await axios.get(`${this.apiUrl}/api/counter/`);
      this.counter = response.data.count;
    },
    async updateCounter(action) {
      await axios.post(`${this.apiUrl}/api/counter/${action}/`);
      this.getCounter();
    }
  }
};
</script>