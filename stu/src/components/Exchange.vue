<script setup></script>
<template>
  <div class="h-screen w-screen bg-dark py-32 px-10">
    <div class="text-xl text-white font-bold">Instant Exchange</div>
    <div class="text-lg text-tertiary font-thin mb-8">What do you need ?</div>
    <div class="h-96 rounded-lg ">
      <div id="fromCurrency" class="flex">
        <input type="number" v-model="fromCurrencyAmount" placeholder="0.0" class="h-16 w-3/5 bg-white/5 rounded-l-lg text-white text-2xl p-4">
        <div type="text" @click="fromCurrencyModal = true" class="flex cursor-pointer h-16 w-2/5 bg-white/5 rounded-r-lg text-white justify-center p-4">
          <div class="flex items-center">
            <img class="h-5 w-7 mr-2" :src="fromCurrency.flag" alt="">
          </div>
          <div class="flex items-center">
            <p class="mr-2 text-xl">{{fromCurrency.name}}</p>
          </div>
          <div class="flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-3" fill="currentColor" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M192 384c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L192 306.8l137.4-137.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-160 160C208.4 380.9 200.2 384 192 384z"/></svg>
          </div>
        </div>
      </div>
      <div class="grid p-3 place-items-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-5" fill="currentColor" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z"/></svg>
      </div>
      <div id="toCurrency" class="flex mb-12">
        <input type="number" v-model="toCurrencyAmount" placeholder="0.0" class="h-16 w-3/5 bg-white/5 rounded-l-lg text-white text-2xl p-4">
        <div type="text" @click="toCurrencyModal = true" class="flex cursor-pointer h-16 w-2/5 bg-white/5 rounded-r-lg text-white justify-center p-4">
          <div class="flex items-center">
            <img class="h-5 w-7 mr-2" :src="toCurrency.flag" alt="">
          </div>
          <div class="flex items-center">
            <p class="mr-2 text-xl">{{toCurrency.name}}</p>
          </div>
          <div class="flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-3" fill="currentColor" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M192 384c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L192 306.8l137.4-137.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-160 160C208.4 380.9 200.2 384 192 384z"/></svg>
          </div>
        </div>
      </div>
      
      <button @click="convert()" class="h-16 w-full bg-secondary rounded-lg text-white text-lg">
        <span>Continue {{fromCurrency.name}}</span>
        <span> to </span>
        <span>{{toCurrency.name}}</span>
      </button>
    </div>
    <div>
      <vue-final-modal v-model="fromCurrencyModal">
        <div class="py-32 px-8">
          <div class="px-6 h-full w-full bg-dark rounded-xl">
            <div id="title" class="flex text-white text-md  pt-6 pb-4 justify-between">
              <span>Select a currency</span>
              <button @click="fromCurrencyModal = false" >X</button>
            </div>
            <div id="search-title" class="">
              <input type="text" v-model="searchCurrency" placeholder="Search currency name" class="h-12 w-full bg-white/5 rounded-lg text-white text-md p-4 mb-4">
              <hr class="mb-4">
            </div>
            <div class="h-96 overflow-auto">
              <div v-for="currency in filteredListCurrencies" :key="currency.name" id="currency-card" @click="fromCurrencyChange(currency), fromCurrencyModal = false" class="cursor-pointer flex bg-white/10 h-16 rounded-lg items-center px-6 mb-4">
                <img class="h-5 w-7 mr-4" :src="currency.flag" alt="">
                <span class="text-white text-lg">{{currency.name}}</span>
              </div>
            </div>
            <div class="h-4">

            </div>

            
          </div>
        </div>
      </vue-final-modal>
    </div>
    
    <div>
      <vue-final-modal v-model="toCurrencyModal">
        <div class="py-32 px-8">
          <div class="px-6 h-full w-full bg-dark rounded-xl">
            <div id="title" class="flex text-white text-md  pt-6 pb-4 justify-between">
              <span>Select a currency</span>
              <button @click="toCurrencyModal = false" >X</button>
            </div>
            <div id="search-title" class="">
              <input type="text" v-model="searchCurrency" placeholder="Search currency name" class="h-12 w-full bg-white/5 rounded-lg text-white text-md p-4 mb-4">
              <hr class="mb-4">
            </div>
            <div class="h-96 overflow-auto">
              <div v-for="currency in filteredListCurrencies" :key="currency.name" id="currency-card" @click="toCurrencyChange(currency), toCurrencyModal = false" class="cursor-pointer flex bg-white/10 h-16 rounded-lg items-center px-6 mb-4">
                <img class="h-5 w-7 mr-4" :src="currency.flag" alt="">
                <span class="text-white text-lg">{{currency.name}}</span>
              </div>
            </div>
            <div class="h-4">

            </div>

            
          </div>
        </div>
      </vue-final-modal>
    </div>
  </div>
</template>

<script setup>
import { VueFinalModal, ModalsContainer } from 'vue-final-modal'
import { ref, reactive, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { store } from '../store/store.js'

var listCurrencies = ref([
  {
    'name':'HKD',
    'flag':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/640px-Flag_of_Hong_Kong.svg.png'
  },
  {
    'name':'IDR',
    'flag':'https://flagpedia.net/data/flags/w580/id.png'
  },
  {
    'name':'USD',
    'flag':'https://flagpedia.net/data/flags/w702/us.webp'
  },
  {
    'name':'SGD',
    'flag':'https://flagpedia.net/data/flags/h80/sg.webp'
  },
  {
    'name':'MYR',
    'flag':'https://flagpedia.net/data/flags/w580/my.png'
  },
  {
    'name':'PHP',
    'flag':'https://flagpedia.net/data/flags/h80/ph.webp'
  },
  {
    'name':'THB',
    'flag':'https://flagpedia.net/data/flags/h80/th.webp'
  },
  {
    'name':'AUD',
    'flag':'https://flagpedia.net/data/flags/h80/au.webp'
  },
  {
    'name':'CAD',
    'flag':'https://flagpedia.net/data/flags/h80/ca.webp'
  }
])

var filteredListCurrencies = ref([
  {
    'name':'HKD',
    'flag':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/640px-Flag_of_Hong_Kong.svg.png'
  },
  {
    'name':'IDR',
    'flag':'https://flagpedia.net/data/flags/w580/id.png'
  },
  {
    'name':'USD',
    'flag':'https://flagpedia.net/data/flags/w702/us.webp'
  },
  {
    'name':'SGD',
    'flag':'https://flagpedia.net/data/flags/h80/sg.webp'
  },
  {
    'name':'MYR',
    'flag':'https://flagpedia.net/data/flags/w580/my.png'
  },
  {
    'name':'PHP',
    'flag':'https://flagpedia.net/data/flags/h80/ph.webp'
  },
  {
    'name':'THB',
    'flag':'https://flagpedia.net/data/flags/h80/th.webp'
  },
  {
    'name':'AUD',
    'flag':'https://flagpedia.net/data/flags/h80/au.webp'
  },
  {
    'name':'CAD',
    'flag':'https://flagpedia.net/data/flags/h80/ca.webp'
  }
])

var fromCurrency = ref({
    'name':'HKD',
    'flag':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/640px-Flag_of_Hong_Kong.svg.png'
  })
var toCurrency = ref({
    'name':'IDR',
    'flag':'https://flagpedia.net/data/flags/w580/id.png'
  })

var fromCurrencyModal = ref(false)
var toCurrencyModal = ref(false)

var fromCurrencyAmount = ref(0)
var toCurrencyAmount = ref(0)

var searchCurrency = ref("")

const router = useRouter()
const route = useRoute()

function fromCurrencyChange(i){
  console.log(i)
  fromCurrency.value = i;
}

function toCurrencyChange(i){
  console.log(i)
  toCurrency.value = i;
}

function filteredCurrencies(i){
  console.log(i)
  filteredListCurrencies = listCurrencies.value.filter(currency => currency.name.toLowerCase().includes(i.toLowerCase()))
}

watch(searchCurrency, (newSearch) => {
  filteredCurrencies(newSearch)
})

function convert() {
  store.fromCurrency.name = fromCurrency.value.name
  store.fromCurrency.flag = fromCurrency.value.flag
  store.fromCurrency.amount = fromCurrencyAmount
  store.toCurrency.name = toCurrency.value.name
  store.toCurrency.flag = toCurrency.value.flag
  store.toCurrency.amount = toCurrencyAmount

  router.push({
    name: 'instant-exchange'
  })
}



</script>