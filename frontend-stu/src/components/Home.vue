<script setup></script>

<template>
  <Transition name="slide-fade">
    <div
      class="flex flex-col h-full w-screen bg-dark text-white px-10 py-10 overflow-auto"
    >
      <section>
        <div class="text-2xl font-medium">Hi Ponto!</div>
        <div class="text-xl font-thin">Welcome back</div>
      </section>
      <section
        class="relative flex flex-col rounded-3xl bg-gradient-to-br from-primary to-secondary mt-10 h-48 w-full"
      >
        <router-link to="/expense">
          <div class="ml-5 mt-5">
            <div class="font-light">Balance</div>
            <div class="text-3xl font-medium">24,250 HKD</div>
            <div class="font-light uppercase mt-3">Richard Ponto</div>
          </div>
        </router-link>
        <div class="absolute top-0 right-2 h-24 w-24">
          <img src="../assets/logo.png" alt="" />
        </div>
        <div class="absolute bottom-5 left-5">
          <div class="font-light">2877-5542-4040-9891</div>
        </div>
      </section>
      <section class="font-light flex flex-wrap justify-center w-full h-28 mt-10">
        <div>
          <router-link to="/exchange">
            <div
              class="flex justify-center pt-2 rounded-xl w-36 h-10 bg-white/5"
            >
              Instant
            </div>
          </router-link>
          <router-link to="/lending">
            <div
              class="flex justify-center pt-2 rounded-xl mt-3 w-36 h-10 bg-white/5"
            >
              Lending
            </div>
          </router-link>
        </div>
        <div class="w-3"></div>
        <div class="">
          <router-link to="/planned-exchange">
            <div
              class="flex justify-center pt-2 rounded-xl w-36 h-10 bg-white/5"
            >
              Planned
            </div>
          </router-link>
          <router-link to="/budgeting">
            <div
              class="flex justify-center pt-2 rounded-xl mt-3 w-36 h-10 bg-white/5"
            >
              Savings
            </div>
          </router-link>
        </div>
      </section>
      <section class="flex flex-col mt-2">
        <div class="text-xl font-light">My Currencies</div>
        <div class="flex flex-nowrap mt-3 gap-x-5 overflow-auto">
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">HKD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/hk.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">Balance</div>
            <div class="text-2xl font-light">$ 12,113</div>
          </div>
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">USD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/us.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">Balance</div>
            <div class="text-2xl font-light">$ 2,703</div>
          </div>
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">SGD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/sg.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">Balance</div>
            <div class="text-2xl font-light">$ 5,110</div>
          </div>
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">AUD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/aus.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">Balance</div>
            <div class="text-2xl font-light">$ 350</div>
          </div>
        </div>
      </section>
      <section class="flex flex-col mt-4">
        <div class="text-xl font-light">Top Currencies</div>
        <div class="flex flex-nowrap mt-3 gap-x-5 overflow-auto">
          <router-link to="/currency">
            <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
              <div class="text-2xl font-light">USD</div>
              <div class="absolute top-6 right-5 w-10 h-10">
                <img src="../assets/us.png" alt="" />
              </div>
              <div class="text-lg font-thin mt-3">HKD $2,703</div>
              <div class="text-2xl font-light text-green-500">+ 0.98%</div>
            </div>
          </router-link>
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">SGD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/sg.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">HKD $5,110</div>
            <div class="text-2xl font-light text-green-500">+ 0.77%</div>
          </div>
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">AUD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/aus.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">HKD $3,110</div>
            <div class="text-2xl font-light text-green-500">+ 0.68%</div>
          </div>
        </div>
      </section>
      <section class="flex flex-col mt-4">
        <div class="text-xl font-light">Gainers & Losers</div>
        <div class="flex flex-nowrap mt-3 gap-x-5 overflow-auto">
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">USD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/us.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">HKD $2,703</div>
            <div class="text-2xl font-light text-green-500">+ 0.98%</div>
          </div>
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">SGD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/sg.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">HKD $5,110</div>
            <div class="text-2xl font-light text-red-600">- 0.77%</div>
          </div>
          <div class="relative rounded-3xl shrink-0 w-36 h-36 bg-white/5 p-5">
            <div class="text-2xl font-light">AUD</div>
            <div class="absolute top-6 right-5 w-10 h-10">
              <img src="../assets/aus.png" alt="" />
            </div>
            <div class="text-lg font-thin mt-3">HKD $3,110</div>
            <div class="text-2xl font-light text-green-500">+ 0.68%</div>
          </div>
        </div>
      </section>
      <section class="flex flex-col mt-4">
        <div class="text-xl font-light">Trending News</div>
        <div class="flex flex-col mt-3 gap-x-5">
          <div
            class="flex flex-row gap-x-3 rounded-3xl w-full h-36 bg-white/5 p-5"
          >
            <div
              class="rounded-3xl bg-cover bg-center h-full w-24"
              style="
                background-image: url('https://fairforex.com/wp-content/uploads/2020/02/instrument-chart-2.jpg');
              "
            ></div>
            <div class="flex flex-col w-36">
              <div class="text-base font-light leading-tight">
                EUR News: Recent Bullish Momentum
              </div>
              <div class="text-sm font-thin mt-3">New York Times</div>
              <div class="text-sm font-light">1h ago</div>
            </div>
          </div>
        </div>
        <div class="flex flex-col mt-3 gap-x-5">
          <div
            class="flex flex-row gap-x-3 rounded-3xl w-full h-36 bg-white/5 p-5"
          >
            <div
              class="rounded-3xl bg-cover bg-center h-full w-24"
              style="
                background-image: url('https://a.c-dn.net/c/content/dam/publicsites/igcom/uk/images/news-article-image-folder/BG_gbp_pound_sterling_987894514.png');
              "
            ></div>
            <div class="w-36">
              <div class="text-base font-light leading-tight">
                GBP Frailties Remain Despite New Windfall Tax
              </div>
              <div class="text-sm font-thin mt-3">Washington Times</div>
              <div class="text-sm font-light">12h ago</div>
            </div>
          </div>
        </div>
        <div class="flex flex-col mt-3 gap-x-5">
          <div
            class="flex flex-row gap-x-3 rounded-3xl w-full h-36 bg-white/5 p-5"
          >
            <div
              class="rounded-3xl bg-cover bg-center h-full w-24"
              style="
                background-image: url('https://imageio.forbes.com/specials-images/imageserve//627bed7c3718be3a3bc88a13/0x0.jpg?format=jpg&width=1200');
              "
            ></div>
            <div class="w-36">
              <div class="text-base font-light leading-tight">
                Coinbase Sold Over $1B in Shares
              </div>
              <div class="text-sm font-thin mt-3">Daily FX</div>
              <div class="text-sm font-light">11h ago</div>
            </div>
          </div>
        </div>
        <div class="flex flex-col mt-5 gap-x-5">
          <div class="flex justify-center rounded-3xl w-full h-16 bg-white/5 p-5">
            See More
          </div>
        </div>
      </section>
    </div>
  </Transition>
</template>

<style>
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>