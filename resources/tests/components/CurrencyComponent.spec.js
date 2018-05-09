import Vue from 'vue/dist/vue.esm.js';
import CurrencyComponent from '../../frontend/components/CurrencyComponent.vue';

function renderComponent(Component, props) {
    const Ctor = Vue.extend(Component)
    const vm = new Ctor(props).$mount()
    return vm;
}

describe('CurrencyComponent', () => {
    it('should have mounted method', function () {
        expect(typeof CurrencyComponent.mounted).toBe('function')
	});
	it('should have empty codes array', function () {
        expect(typeof CurrencyComponent.data).toBe('function')
    });
});