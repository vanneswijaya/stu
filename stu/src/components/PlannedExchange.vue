<script setup></script>
<template class="">
  <div class="h-full w-screen bg-dark py-10 px-10">
    <div class="text-lg text-white font-bold mb-4">Planned Exchange</div>
    <div class="h-full rounded-lg ">
      
      <div class="text-white mt-8">
        Historical Price
      </div>
      <section class="mb-8">
        <Line :chart-data="chartData" />
      </section>

      <button @click="convert()" class="my-4 h-16 w-1/2 bg-secondary rounded-lg text-white text-lg">
        <span>Convert {{fromCurrency.name}}</span>
        <span> to </span>
        <span>{{toCurrency.name}}</span>
      </button>

      <div class="text-lg mb-8">
        <p class="mb-2 text-primary">Planned Exchange Rate</p>
        <div class="flex">
          <div class="h-16 w-2/5 bg-white/5 rounded-l-lg flex justify-between items-center px-4">
            <div class="flex">
              <span class="text-white text-lg mr-3">1 {{toCurrency.name}}</span>
            </div>
            <span class="text-white text-lg">=</span>
          </div>
          <div class="h-16 w-3/5 bg-white/5 rounded-r-lg text-lg">
            <input type="number" v-model="targetRate" class="h-16 w-3/5 bg-white/5 text-white text-lg p-4 mr-2">
            <span class="text-white text-lg">{{toCurrency.name}}</span>
          </div>
        </div>
      </div>

      <div class="mb-4">
        <div id="fromCurrency" class="flex">
          <input type="number" disabled v-model="store.fromCurrency.amount" class="h-16 w-3/5 bg-white/5 rounded-l-lg text-white text-lg p-4">
          <div type="text" class="flex h-16 w-2/5 bg-white/5 rounded-r-lg text-white justify-center p-4">
            <div class="flex items-center">
              <img class="h-5 w-7 mr-2" :src="fromCurrency.flag" alt="">
            </div>
            <div class="flex items-center">
              <p class="mr-2 text-lg">{{fromCurrency.name}}</p>
            </div>
          </div>
        </div>
        <div class="grid py-2 place-items-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-5" fill="currentColor" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z"/></svg>
        </div>
        <div id="toCurrency" class="flex">
          <input type="number" disabled v-model="amount" class="h-16 w-3/5 bg-white/5 rounded-l-lg text-white text-lg p-4">
          <div type="text" class="flex h-16 w-2/5 bg-white/5 rounded-r-lg text-white justify-center p-4">
            <div class="flex items-center">
              <img class="h-5 w-7 mr-2" :src="toCurrency.flag" alt="">
            </div>
            <div class="flex items-center">
              <p class="mr-2 text-lg">{{toCurrency.name}}</p>
            </div>
          </div>
        </div>
      </div>
<!-- 
      <span class="text-white">
        You will save 
      </span>
      <span class="text-primary">
        {{store.toCurrency.amount - amount}} IDR
      </span> -->
      
      <button @click="convert()" class="mt-4 h-16 w-full bg-secondary rounded-lg text-white text-lg">
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
import { Line } from "vue-chartjs";

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
var currentRate = ref(1.5)

var amount = ref(0)

watch(targetRate, (newAmount, oldAmount) => {
  console.log(targetRate)
  amount.value = store.fromCurrency.amount * targetRate.value
})

import {
  Chart as ChartJS,
  ArcElement,
  LineElement,
  BarElement,
  PointElement,
  BarController,
  BubbleController,
  DoughnutController,
  LineController,
  PieController,
  PolarAreaController,
  RadarController,
  ScatterController,
  CategoryScale,
  LinearScale,
  LogarithmicScale,
  RadialLinearScale,
  TimeScale,
  TimeSeriesScale,
  Decimation,
  Filler,
  Legend,
  Title,
  Tooltip,
  SubTitle,
} from "chart.js";

ChartJS.register(
  ArcElement,
  LineElement,
  BarElement,
  PointElement,
  BarController,
  BubbleController,
  DoughnutController,
  LineController,
  PieController,
  PolarAreaController,
  RadarController,
  ScatterController,
  CategoryScale,
  LinearScale,
  LogarithmicScale,
  RadialLinearScale,
  TimeScale,
  TimeSeriesScale,
  Decimation,
  Filler,
  Legend,
  Title,
  Tooltip,
  SubTitle
);

const chartData = ref({
  labels: [
    5.774151530133701,
    5.7530817684312385,
    5.76544239766191,
    5.77905947365134,
    5.762625294210719,
    5.755027096480725,
    5.781878237890959,
    5.804666001451537,
    5.779695452994126,
    5.777380587554022,
    5.76389230399571,
    5.752723777121603,
    5.74136830103246,
    5.744742927721244,
    5.736929673569422,
    5.717232928276818,
    5.73450111330404,
    5.747613558999526,
    5.727620331537806,
    5.738017561688632,
    5.761193123338398,
    5.734151262789548,
    5.773417643250147,
    5.798124694206806,
    5.783868017740056,
    5.791095431822317,
    5.8139965154831685,
    5.8242241399338495,
    5.801901086706407,
    5.834287269126208,
    5.8262182460035765
    ],
  datasets: [
    {
      label: "Exchange rate in HKD",
      data: [3, 5, 3, 10, 25, 23],
      backgroundColor: "rgba(34, 197, 94, 0.2)",
      borderColor: "rgba(34, 197, 94, 1)",
      borderWidth: 2,
    },
  ],
});





</script>