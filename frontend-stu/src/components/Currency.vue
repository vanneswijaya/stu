<script setup>
import { ref } from "vue";
import { Line } from "vue-chartjs";
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

var cValues = ref([])
var cLabels = ref([])
cValues.value = [5.774151530133701,5.7530817684312385,5.76544239766191,5.77905947365134,5.762625294210719,5.755027096480725,5.781878237890959,5.804666001451537,5.779695452994126,5.777380587554022,5.76389230399571,5.752723777121603,5.74136830103246,5.744742927721244,5.736929673569422,5.717232928276818,5.73450111330404,5.747613558999526,5.727620331537806,5.738017561688632,5.761193123338398,5.734151262789548,5.773417643250147,5.798124694206806,5.783868017740056,5.791095431822317,5.8139965154831685,5.8242241399338495,5.801901086706407,5.834287269126208,5.8262182460035765]
cLabels.value = [23,24,25,26,27,28,29,30,31,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

const chartData = ref({
  labels: cLabels.value,
  datasets: [
    {
      label: "Exchange rate in HKD",
      data: cValues.value,
      backgroundColor: "rgba(34, 197, 94, 0.2)",
      borderColor: "rgba(34, 197, 94, 1)",
      borderWidth: 2,
    },
  ],
});
</script>

<template>
  <div
    class="flex flex-col h-screen w-screen bg-dark text-white px-10 pt-5 pb-10 overflow-auto"
  >
    <section>
      <div class="flex flex-row gap-x-3 justify-center">
        <div class="w-10 h-10 mt-1">
          <img src="../assets/us.png" alt="" />
        </div>
        <div class="text-2xl font-light">USD</div>
      </div>
    </section>
    <section>
      <div class="mt-5">
        <div class="font-light">Current exchange rate</div>
        <div class="text-3xl font-medium">HKD $5.82</div>
        <div class="text-2xl font-light text-green-500">+ 0.98%</div>
      </div>
    </section>
    <section class="my-8">
      <Line :chart-data="chartData" />
    </section>
    <section>
      <div class="mt-5">
        <div class="font-light">Your USD balance</div>
        <div class="text-3xl font-medium">USD $2,131</div>
      </div>
    </section>
    <section class="flex flex-col mt-5 gap-y-3">
      <router-link to="/exchange">
        <div class="flex justify-center rounded-3xl w-full h-16 bg-white/5 p-5">
          Buy Instant
        </div>
      </router-link>
      <router-link to="/planned-exchange">
        <div class="flex justify-center rounded-3xl w-full h-16 bg-white/5 p-5">
          Buy Planned
        </div>
      </router-link>
    </section>
  </div>
</template>
