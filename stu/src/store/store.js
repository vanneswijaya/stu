import { reactive } from 'vue'

export const store = reactive({
  fromCurrency: {
    'name':'HKD',
    'flag':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/640px-Flag_of_Hong_Kong.svg.png',
    'amount': 1000
  },
  toCurrency: {
    'name':'IDR',
    'flag':'https://flagpedia.net/data/flags/w580/id.png',
    'amount': 1500
  }
})


  