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
      label: "Spending in HKD",
      data: [3, 5, 3, 10, 25, 23],
      backgroundColor: "rgba(12, 166, 233, 0.2)",
      borderColor: "rgba(12, 166, 233, 1)",
      borderWidth: 2,
    },
  ],
});
</script>

<template>
  <div
    class="flex flex-col h-full w-screen bg-dark text-white px-10 py-10 overflow-auto"
  >
    <section>
      <div class="text-2xl font-medium">Expenses</div>
      <div class="text-xl font-thin">My budget summary</div>
    </section>
    <section class="flex justify-center">
      <section
        class="flex flex-col justify-center items-center rounded-full border-primary border-4 mt-10 h-56 w-56"
      >
        <div class="mt-5 text-center">
          <div class="font-light">Total spending</div>
          <div class="text-3xl font-medium">2,139 HKD</div>
          <div class="font-light uppercase mt-3">May 2022</div>
        </div>
      </section>
    </section>
    <section class="flex flex-col mt-8">
      <div class="text-xl font-light">Categories</div>
      <div class="flex flex-wrap mt-3 gap-x-5 gap-y-3">
        <div
          class="flex flex-col justify-center items-center rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5"
        >
          <div class="w-10 h-10">
            <img
              src="https://www.seekpng.com/png/full/89-891649_communication-provider-icon-white-car-icon-vector.png"
              alt=""
            />
          </div>
          <div class="text-lg font-thin">Transport</div>
          <div class="text-2xl font-light">$121.3</div>
        </div>
        <div
          class="flex flex-col justify-center items-center rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5"
        >
          <div class="w-10 h-10">
            <img
              src="https://icon-library.com/images/food-icon-white/food-icon-white-15.jpg"
              alt=""
            />
          </div>
          <div class="text-lg font-thin">F&B</div>
          <div class="text-2xl font-light">$511.20</div>
        </div>
        <div
          class="flex flex-col justify-center items-center rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5"
        >
          <div class="w-10 h-10">
            <img
              src="https://pnggrid.com/wp-content/uploads/2021/07/White-YouTube-Logo-Transparent.png"
              alt=""
            />
          </div>
          <div class="text-lg font-thin">Entertainment</div>
          <div class="text-2xl font-light">$1,010.11</div>
        </div>
        <div
          class="flex flex-col justify-center items-center rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5"
        >
          <div class="w-10 h-10">
            <img
              src="https://flaticons.net/icon.php?slug_category=shopping&slug_icon=shoe"
              alt=""
            />
          </div>
          <div class="text-lg font-thin">Others</div>
          <div class="text-2xl font-light">$133.03</div>
        </div>
      </div>
    </section>
    <section class="flex flex-col mt-10">
      <div class="text-xl font-light">Transaction History</div>
      <div class="flex flex-col mt-3 gap-y-3">
        <div class="rounded-3xl w-full h-28 bg-white/5 p-5">
          <div class="relative">
            <div class="text-lg font-light">App Store</div>
            <div class="absolute top-1 right-0 w-6 h-6">
              <img
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/App_Store_%28iOS%29.svg/640px-App_Store_%28iOS%29.svg.png"
                alt=""
              />
            </div>
          </div>
          <div class="relative">
            <div class="absolute text-lg font-thin mt-3">May 30, 2022</div>
            <div class="absolute right-0 top-3 text-lg font-light text-red-600">
              - $422.19
            </div>
          </div>
        </div>
        <div class="rounded-3xl w-full h-28 bg-white/5 p-5">
          <div class="relative">
            <div class="text-lg font-light">Transfer from Simon</div>
            <div class="absolute top-1 right-0 w-10 h-10">
              <img src="../assets/us.png" alt="" />
            </div>
          </div>
          <div class="relative">
            <div class="absolute text-lg font-thin mt-3">May 29, 2022</div>
            <div
              class="absolute right-0 top-3 text-lg font-light text-green-500"
            >
              + $20.33
            </div>
          </div>
        </div>
        <div class="rounded-3xl w-full h-28 bg-white/5 p-5">
          <div class="relative">
            <div class="text-lg font-light">McDonald's Mongkok</div>
            <div class="absolute top-1 right-0 w-6 h-6">
              <img
                src="https://www.pikpng.com/pngl/b/523-5236319_mcdonalds-mcdonalds-diet-coke-clipart.png"
                alt=""
              />
            </div>
          </div>
          <div class="relative">
            <div class="absolute text-lg font-thin mt-3">May 11, 2022</div>
            <div class="absolute right-0 top-3 text-lg font-light text-red-600">
              - $200.10
            </div>
          </div>
        </div>
      </div>
      <div class="flex flex-col mt-5 gap-x-5">
        <div class="flex justify-center rounded-3xl w-full h-16 bg-white/5 p-5">
          See All
        </div>
      </div>
    </section>
    <section class="mt-10">
      <div class="text-xl font-light">My Stats</div>
      <div class="text-xl font-thin mb-5">May 2022</div>
      <Line :chart-data="chartData" />
    </section>
  </div>
</template>
