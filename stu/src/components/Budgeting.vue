<template>
    <div
    class="flex flex-col h-screen w-screen bg-dark text-white px-10 py-10 overflow-auto"
    >
    <section>
        <div class="text-2xl font-medium">Budgeting & Savings</div>
        <div class="text-xl font-thin">Plan your future</div>
    </section>
    <section class="flex flex-col gap-5 justify-center mt-4">
        <div class="text-xl font-light">Your Savings</div>
        <div class="flex items-center rounded-3xl shrink-0 w-full h-24 bg-white/5 p-5">
            <div class="w-1/4 flex justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-8" fill="currentColor" viewBox="0 0 576 512"><path d="M575.8 255.5C575.8 273.5 560.8 287.6 543.8 287.6H511.8L512.5 447.7C512.5 450.5 512.3 453.1 512 455.8V472C512 494.1 494.1 512 472 512H456C454.9 512 453.8 511.1 452.7 511.9C451.3 511.1 449.9 512 448.5 512H392C369.9 512 352 494.1 352 472V384C352 366.3 337.7 352 320 352H256C238.3 352 224 366.3 224 384V472C224 494.1 206.1 512 184 512H128.1C126.6 512 125.1 511.9 123.6 511.8C122.4 511.9 121.2 512 120 512H104C81.91 512 64 494.1 64 472V360C64 359.1 64.03 358.1 64.09 357.2V287.6H32.05C14.02 287.6 0 273.5 0 255.5C0 246.5 3.004 238.5 10.01 231.5L266.4 8.016C273.4 1.002 281.4 0 288.4 0C295.4 0 303.4 2.004 309.5 7.014L564.8 231.5C572.8 238.5 576.9 246.5 575.8 255.5L575.8 255.5z"/></svg>
            </div>
            <div class="w-3/4 flex flex-col">
                <div class="text-md font-medium">New Apartment</div>
                <div class="text-sm font-thin">By 2025</div>
                <div class="flex gap-2 text-xs items-center mt-2">
                    <div>{{savings.apartment.current/1000}}K</div>
                    <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
                        <div class="bg-secondary h-2.5 rounded-full" :style="savings.apartment.prog"></div>
                    </div>
                    <div class="text-light">{{savings.apartment.target/1000}}K</div>
                </div>
            </div>
        </div>
        <div class="flex items-center rounded-3xl shrink-0 w-full h-24 bg-white/5 p-5">
            <div class="w-1/4 flex justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-8" fill="currentColor" viewBox="0 0 640 512"><path d="M623.1 136.9l-282.7-101.2c-13.73-4.91-28.7-4.91-42.43 0L16.05 136.9C6.438 140.4 0 149.6 0 160s6.438 19.65 16.05 23.09L76.07 204.6c-11.89 15.8-20.26 34.16-24.55 53.95C40.05 263.4 32 274.8 32 288c0 9.953 4.814 18.49 11.94 24.36l-24.83 149C17.48 471.1 25 480 34.89 480H93.11c9.887 0 17.41-8.879 15.78-18.63l-24.83-149C91.19 306.5 96 297.1 96 288c0-10.29-5.174-19.03-12.72-24.89c4.252-17.76 12.88-33.82 24.94-47.03l190.6 68.23c13.73 4.91 28.7 4.91 42.43 0l282.7-101.2C633.6 179.6 640 170.4 640 160S633.6 140.4 623.1 136.9zM351.1 314.4C341.7 318.1 330.9 320 320 320c-10.92 0-21.69-1.867-32-5.555L142.8 262.5L128 405.3C128 446.6 213.1 480 320 480c105.1 0 192-33.4 192-74.67l-14.78-142.9L351.1 314.4z"/></svg>
            </div>
            <div class="w-3/4 flex flex-col">
                <div class="text-md font-medium">Master Degree</div>
                <div class="text-sm font-thin">By 2023</div>
                <div class="flex gap-2 text-xs items-center mt-2">
                    <div>{{savings.masterDegree.current/1000}}K</div>
                    <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
                        <div class="bg-secondary h-2.5 rounded-full" :style="savings.masterDegree.prog"></div>
                    </div>
                    <div class="text-light">{{savings.masterDegree.target/1000}}K</div>
                </div>
            </div>
        </div>
    </section>
    <section class="flex flex-col gap-5 justify-center mt-10">
        <div class="text-xl font-light">Plan More</div>
        <div class="flex flex-wrap gap-x-5 gap-y-3">
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
            </div>
            <div
                class="flex flex-col justify-center items-center rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5"
            >
                <div class="w-10 h-10 flex justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-8" fill="currentColor" viewBox="0 0 512 512"><path d="M512 256C512 397.4 397.4 512 256 512C114.6 512 0 397.4 0 256C0 114.6 114.6 0 256 0C397.4 0 512 114.6 512 256zM51.68 295.1L83.41 301.5C91.27 303.1 99.41 300.6 105.1 294.9L120.5 279.5C132 267.1 151.6 271.1 158.9 285.8L168.2 304.3C172.1 313.9 182.8 319.1 193.5 319.1C208.7 319.1 219.6 305.4 215.2 290.8L209.3 270.9C204.6 255.5 216.2 240 232.3 240H234.6C247.1 240 260.5 233.3 267.9 222.2L278.6 206.1C284.2 197.7 283.9 186.6 277.8 178.4L261.7 156.9C251.4 143.2 258.4 123.4 275.1 119.2L292.1 114.1C299.6 113.1 305.7 107.8 308.6 100.6L324.9 59.69C303.4 52.12 280.2 48 255.1 48C141.1 48 47.1 141.1 47.1 256C47.1 269.4 49.26 282.5 51.68 295.1L51.68 295.1zM450.4 300.4L434.6 304.9C427.9 306.7 420.8 304 417.1 298.2L415.1 295.1C409.1 285.7 398.7 279.1 387.5 279.1C376.4 279.1 365.1 285.7 359.9 295.1L353.8 304.6C352.4 306.8 350.5 308.7 348.2 309.1L311.1 330.1C293.9 340.2 286.5 362.5 294.1 381.4L300.5 393.8C309.1 413 331.2 422.3 350.1 414.9L353.5 413.1C363.6 410.2 374.8 411.8 383.5 418.1L385 419.2C422.2 389.7 449.1 347.8 459.4 299.7C456.4 299.4 453.4 299.6 450.4 300.4H450.4zM156.1 367.5L188.1 375.5C196.7 377.7 205.4 372.5 207.5 363.9C209.7 355.3 204.5 346.6 195.9 344.5L163.9 336.5C155.3 334.3 146.6 339.5 144.5 348.1C142.3 356.7 147.5 365.4 156.1 367.5V367.5zM236.5 328.1C234.3 336.7 239.5 345.4 248.1 347.5C256.7 349.7 265.4 344.5 267.5 335.9L275.5 303.9C277.7 295.3 272.5 286.6 263.9 284.5C255.3 282.3 246.6 287.5 244.5 296.1L236.5 328.1zM321.7 120.8L305.7 152.8C301.7 160.7 304.9 170.4 312.8 174.3C320.7 178.3 330.4 175.1 334.3 167.2L350.3 135.2C354.3 127.3 351.1 117.6 343.2 113.7C335.3 109.7 325.6 112.9 321.7 120.8V120.8z"/></svg>
                </div>
                <div class="text-lg font-thin">Vacation</div>
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
            </div>
            <div
                class="flex flex-col justify-center items-center rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5"
            >
                <div class="w-10 h-10 flex justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="text-white h-8" fill="currentColor" viewBox="0 0 384 512"><path d="M320 0H64C37.5 0 16 21.5 16 48v416C16 490.5 37.5 512 64 512h256c26.5 0 48-21.5 48-48v-416C368 21.5 346.5 0 320 0zM240 447.1C240 456.8 232.8 464 224 464H159.1C151.2 464 144 456.8 144 448S151.2 432 160 432h64C232.8 432 240 439.2 240 447.1zM304 384h-224V64h224V384z"/></svg>
                </div>
                <div class="text-lg font-thin">New Phone</div>
            </div>
            </div>
    </section>
    </div>
</template>

<script>
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
export default {
    name: 'Budgeting',
    setup(){
        var savings = ref({
            apartment: {
                current: 450000,
                target: 1000000,
                prog: "width: 0%",
            },
            masterDegree:{
                current: 1500000,
                target: 2000000,
                prog: "width: 0%",
            },
        });
        return {
            savings,
        }
    },
    mounted(){
        this.savings.apartment.prog = `width: ${(this.savings.apartment.current/this.savings.apartment.target)*100}%`; 
        this.savings.masterDegree.prog = `width: ${(this.savings.masterDegree.current/this.savings.masterDegree.target)*100}%`; 
    }
}
</script>

<style>

</style>