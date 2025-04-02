<template>
  <div>
    <input v-model="query" placeholder="Digite o termo de busca" />
    <button @click="buscar">Buscar</button>
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.id">
        {{ operadora.nome }} - Despesa: {{ operadora.despesa_trimestre }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      operadoras: []
    }
  },
  methods: {
    async buscar() {
      try {
        const resposta = await axios.get('http://localhost:5000/busca', {
          params: { q: this.query }
        });
        this.operadoras = resposta.data;
      } catch (error) {
        console.error('Erro na busca:', error);
      }
    }
  }
}
</script>
