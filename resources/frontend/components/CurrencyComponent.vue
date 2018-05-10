<template>
  <div>
    <select v-model='fromCurrency'  @change='getCurrency()'>
      <option selected="selected" disabled='disabled'>Choose currency code</option>
      <option v-for='code of defaultCodes' :value="code.code">{{code.country}}</option>
    </select>
    <select v-model='toCurrency' @change='getCurrency()'>
      <option selected="selected" disabled='disabled'>Choose currency code</option>
      <option v-for='code of codes' :value="code.code">{{code.country}}</option>
    </select>
    <input type="text" v-model="count" @change="calculate()">
    <span>{{result}}</span>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      count: 1,
      result: 0,
      currency: 0,
      toCurrency: '',
      fromCurrency: '',
      codes: [],
      defaultCodes: [
        {
          'code':'EUR',
          'country':'Euro',
        },
         {
          'code':'USD',
          'country':'US Dollar',
        },
         {
          'code':'PLN',
          'country':'Polish zloty',
        },
         {
          'code':'CSK',
          'country':'Czech koruna',
        }
      ]
    }
  },
  mounted () {
    axios.get('/api/codes/')
      .then(response => {
        this.codes = response.data
      })
      .catch(e => {
        console.error(e)
      })
  },
  methods:{
    getCurrency(){
      let self = this;
      if (self.fromCurrency === '' || self.toCurrency === "" ) return;
      axios.get(`/api/currency/${self.fromCurrency}/${self.toCurrency}/`)
        .then(response => {
          if (response.data.value !== undefined){
            self.result = response.data.value
            self.currency = self.result
          } else {
            console.error(response.data.error)
          }
         
        })
        .catch(e => {
          console.error(e)
        })
    },
    calculate(){
      this.result = parseFloat(this.currency)*parseInt(this.count)
    }
  }
}
</script>

<style lang='scss'>
span{
    font-size: 2em;
}
</style>