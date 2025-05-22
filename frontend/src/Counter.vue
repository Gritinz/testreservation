<template>
  <div>
    <h1>Compteur : {{ counter }}</h1>
    <button @click="updateCounter('/api/counter/inc')">+1</button>
    <button @click="updateCounter('/api/counter/dec')">-1</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      counter: 0
    };
  },
  methods: {
    async updateCounter(url) {
      const res = await axios.post(url);
      this.counter = res.data.value;
    },
    async fetchCounter() {
      const res = await axios.get('/api/counter');
      this.counter = res.data.value;
    }
  },
  mounted() {
    this.fetchCounter();
  }
};
</script>