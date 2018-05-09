import Vue from 'vue/dist/vue.esm.js';
import Currency from './components/CurrencyComponent.vue';

new Vue({
	el: '#index',
	components: {
		'currency-component': Currency
	}
})