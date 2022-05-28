<script setup></script>
<template>
  <div class="h-full w-screen bg-dark py-10 px-10">
    <div class="text-xl text-white font-bold mb-8">Instant Exchange</div>
    <div class="h-full rounded-lg ">

      <div class="text-lg mb-8">
        <p class="mb-2 text-tertiary">Current Exchange Rate</p>
        <div class="flex">
          <div class="h-16 w-1/2 bg-white/5 rounded-l-lg flex items-center px-4">
            <span class="text-white text-xl">1 {{fromCurrency.name}}</span>
          </div>
          <div class="h-16 w-1/2 bg-white/5 rounded-r-lg">

          </div>
        </div>
      </div>

      <div>
        <div id="fromCurrency" class="flex">
          <input type="number" disabled v-model="store.fromCurrency.amount" class="h-16 w-3/5 bg-white/5 rounded-l-lg text-white text-xl p-4">
          <div type="text" class="flex h-16 w-2/5 bg-white/5 rounded-r-lg text-white justify-center p-4">
            <div class="flex items-center">
              <img class="h-5 w-7 mr-2" :src="fromCurrency.flag" alt="">
            </div>
            <div class="flex items-center">
              <p class="mr-2 text-xl">{{fromCurrency.name}}</p>
            </div>
          </div>
        </div>
        <div class="grid py-2 place-items-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-5" fill="currentColor" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z"/></svg>
        </div>
        <div id="toCurrency" class="flex">
          <input type="number" disabled v-model="store.toCurrency.amount" class="h-16 w-3/5 bg-white/5 rounded-l-lg text-white text-xl p-4">
          <div type="text" class="flex h-16 w-2/5 bg-white/5 rounded-r-lg text-white justify-center p-4">
            <div class="flex items-center">
              <img class="h-5 w-7 mr-2" :src="toCurrency.flag" alt="">
            </div>
            <div class="flex items-center">
              <p class="mr-2 text-xl">{{toCurrency.name}}</p>
            </div>
          </div>
        </div>
      </div>

      <hr class="my-8">

      <div class="text-lg mb-8">
        <p class="mb-2 text-primary">Targeted Exchange Rate</p>
        <div class="flex">
          <div class="h-16 w-1/2 bg-white/5 rounded-l-lg">
            
          </div>
          <div class="h-16 w-1/2 bg-white/5 rounded-r-lg">

          </div>
        </div>
      </div>

      <div class="mb-16">
        <div id="fromCurrency" class="flex">
          <input type="number" disabled v-model="store.fromCurrency.amount" class="h-16 w-3/5 bg-white/5 rounded-l-lg text-white text-2xl p-4">
          <div type="text" class="flex h-16 w-2/5 bg-white/5 rounded-r-lg text-white justify-center p-4">
            <div class="flex items-center">
              <img class="h-5 w-7 mr-2" :src="fromCurrency.flag" alt="">
            </div>
            <div class="flex items-center">
              <p class="mr-2 text-xl">{{fromCurrency.name}}</p>
            </div>
          </div>
        </div>
        <div class="grid py-2 place-items-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-5" fill="currentColor" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z"/></svg>
        </div>
        <div id="toCurrency" class="flex">
          <input type="number" disabled v-model="store.toCurrency.amount" class="h-16 w-3/5 bg-white/5 rounded-l-lg text-white text-2xl p-4">
          <div type="text" class="flex h-16 w-2/5 bg-white/5 rounded-r-lg text-white justify-center p-4">
            <div class="flex items-center">
              <img class="h-5 w-7 mr-2" :src="toCurrency.flag" alt="">
            </div>
            <div class="flex items-center">
              <p class="mr-2 text-xl">{{toCurrency.name}}</p>
            </div>
          </div>
        </div>
      </div>
      
      <button @click="convert()" class="h-16 w-full bg-secondary rounded-lg text-white text-lg">
        <span>Convert {{fromCurrency.name}}</span>
        <span> to </span>
        <span>{{toCurrency.name}}</span>
      </button>
    </div>

  </div>
</template>

<script setup>
import { VueFinalModal, ModalsContainer } from 'vue-final-modal'
import { ref, reactive, watch, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { store } from '../store/store.js'

// onMounted(() => {
//   fromCurrency.value = store.fromCurrency
//   toCurrency.value = store.toCurrency
// })

// var toCurrency = ref({
//     'name':'IDR',
//     'flag':'https://flagpedia.net/data/flags/w580/id.png',
//     'amount': 2000
//   })

// var fromCurrency = ref({
//     'name':'HKD',
//     'flag':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/640px-Flag_of_Hong_Kong.svg.png',
//     'amount': 1000
//   })

var fromCurrency = ref(store.fromCurrency)
var toCurrency = ref(store.toCurrency)
var targetRate = ref(0)
var currentRate = ref("1,852.36")






</script>