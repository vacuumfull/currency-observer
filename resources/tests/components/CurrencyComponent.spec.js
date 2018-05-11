import Vue from 'vue/dist/vue.esm.js';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import CurrencyComponent from '../../frontend/components/CurrencyComponent.vue';

function renderComponent(Component, props) {
    const Ctor = Vue.extend(Component)
    const vm = new Ctor(props).$mount()
    return vm;
}

let mock = new MockAdapter(axios);
mock.onGet('/api/codes/').reply(200, {
    users: [
        {
            "code": "AED",
            "country": "UA Emirates dirham"
        },
        {
            "code": "AUD",
            "country": "Australian dollar"
        }
    ]
});
mock.onGet('/api/currency/PLN/AED/').reply(
    200, {"currency":"PLN\/AED","type":"converted","date":"2018-05-09 16:43:58","value":1.02225}
);


describe('CurrencyComponent', () => {
    let vm;
    beforeEach(function() {
        vm = renderComponent(CurrencyComponent, {
            data:{
                count: 1,
                result: 0,
                currency: 0,
                toCurrency: '',
                fromCurrency: '',
                codes: [],
            },
            mounted(){
                return this.codes = [{
                    "code": "AED",
                    "country": "UA Emirates dirham"
                },
                {
                    "code": "AUD",
                    "country": "Australian dollar"
                }]
            }
        })

    });

    it('should have mounted method', function () {
        expect(typeof CurrencyComponent.mounted).toBe('function')
    });
    it('should have data attrs', function () {
        expect(vm.count).toEqual(1)
        expect(vm.codes.length).toEqual(2)
        expect(vm.result).toEqual(0)
        expect(vm.toCurrency).toEqual('')
        expect(vm.fromCurrency).toEqual('')
    });

    it('should have method getCurrency', function () {
        expect(typeof CurrencyComponent.methods.getCurrency).toBe('function')
    })
    it('should get correct result from getCurrency', function(done){
        vm.fromCurrency = 'PLN'
        vm.toCurrency = 'AED'
        vm.getCurrency()
        setTimeout(()=>{
            done();
            expect(vm.result).toEqual(1.02225)
        }, 1500)
    })
    it('test result of calculate method', function(){
        vm.currency = 1.675
        vm.count = 3
        vm.calculate()
        expect(vm.result).toEqual(vm.currency * vm.count)
    })

});