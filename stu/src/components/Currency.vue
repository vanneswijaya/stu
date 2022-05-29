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

const chartData = ref({
  labels: ["1", "5", "10", "15", "20", "31"],
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
        <div class="text-3xl font-medium">HKD $7.85</div>
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
      <div class="flex justify-center rounded-3xl w-full h-16 bg-white/5 p-5">
        Buy Instant
      </div>
      <div class="flex justify-center rounded-3xl w-full h-16 bg-white/5 p-5">
        Buy Planned
      </div>
    </section>
  </div>
</template>
