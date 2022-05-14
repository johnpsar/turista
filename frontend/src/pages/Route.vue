<template>
  <div class="timeline-container">
    <div class="timeline-container-header">
      <Header />
    </div>
    <div
      class="bg"
      v-bind:style="{
        backgroundImage: `url(&quot;${imageUrl}&quot;)`,
      }"
    ></div>
    <div class="timeline-container-content">
      <div v-if="detailedView === false" class="main">
        <RouteView :data="displayedData" :count="props.count"/>
      </div>
      <div v-else class="main">
        <TimelineView
          @refresh="onRefresh"
          :data="displayedData"
          :count="props.count"
          :weather="myWeather"
        />
      </div>
      <button
        class="end-route"
        id="detailedRoute-btn"
        @click="router.push('/end')"
      >
        End route
      </button>
    </div>
  </div>
  <div class="detailed-view-button" @click="detailedView = !detailedView">
    <img v-if="!detailedView" :src="Grid" />
    <img v-else :src="List" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from "vue";
import Header from "../components/Header.vue";
import Timeline from "primevue/timeline";
import { useRouter, useRoute } from "vue-router";
import Grid from "../assets/icons/grid.svg";
import List from "../assets/icons/list.svg";
import TimelineView from "../components/TimelineView.vue";
import RouteView from "../components/RouteView.vue";
import axios from "axios";
import { computed } from "@vue/reactivity";
import A from "../assets/background.jpg"
const props = defineProps<{
  date: string;
  place: string;
  count: number;
  recommendations: number[];
}>();
interface recommendation {
  id: string;
  name: string;
  url: string;
  type: string;
  idk: unknown;
  path: string;
  desc: string;
}
interface weather {
  condition: string;
  temperature: string;
}

const myData = ref<recommendation[]>([]);
const displayedData = ref<recommendation[]>([]);
const myWeather = ref<weather[]>([]);
const imageUrl =ref(new URL("../assets/background.jpg", import.meta.url).href)

onMounted(async () => {
  const options = {
    place: props.place,
    count: props.count,
    recommendations_selected: props.recommendations,
  };

  try {
    const { data } = await axios.post<recommendation[]>(
      "http://127.0.0.1:8000/places/route",
      options
    );
    data.forEach((e, index) => {
      //an spaei kati einai atuo
      myData.value.push({
        id: e.id,
        name: e.name,
        url: e.url,
        type: e.type,
        idk: e.idk,
        path: e.path,
        desc: e.desc,
      });
      if(index===0){
        imageUrl.value=new URL(e.path, import.meta.url).href
      }
    });
    displayedData.value = [...myData.value];
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.log("error message: ", error.message);
      return error.message;
    }
  }
  const weatherOptions = {
    date: props.date,
    place: props.place,
  };

  try {
    const { data } = await axios.post<weather[]>(
      "http://127.0.0.1:8000/places/weather",
      weatherOptions
    );
    console.log(data);
    data.forEach((e) => {
      myWeather.value.push({
        condition: e.condition,
        temperature: e.temperature,
      });
    });
  } catch (error) {
    console.log(error);
  }
});




const overlay = ref<{
  toggle: () => void;
}>();

const router = useRouter();

const detailedView = ref(false);

function onRefresh(index:number){
  displayedData.value.splice(index,1)
  console.log(displayedData.value)
  console.log("refresh",index)
}
</script>

<style scoped lang="scss">
.main {
  overflow: auto;
}

.timeline-container {
  font-family: "Montserrat Alternates", sans-serif;
  width: 100%;
  height: 100%;

  &-header {
    height: 10%;
    width: 100%;
  }

  &-content {
    width: 100%;
    height: 90%;
    display: block;

    #detailedRoute-btn {
      display: block;
      width: 50%;
      height: 44px;
      font-size: 16px;
      font-weight: 600;
      justify-content: center;
      align-items: center;
      color: white;
      background-color: #ff8811;
      border-radius: 12px;
      margin: 0% auto;
    }

    &-card {
      text-align: center;
      border: 4px solid #06bcc1;
      border-radius: 12px;
      max-width: 100%;
      padding: 5%;
      background-color: rgba($color: white, $alpha: 0.5);

      &-body {
        text-align: center;
        align-items: center;
        justify-content: center;
        padding: 2%;

        hr {
          height: 1px;
          background-color: #ff8811;
          width: 80%;
          margin-left: auto;
          margin-right: auto;
          margin-top: 0;
          margin-bottom: 2%;
        }

        &-text {
          #checkin-icon {
            margin: 0 5%;
            display: inline-block;
          }

          #map-btn {
            margin: 0 5%;
            display: inline-block;
          }
        }
      }
    }
  }
}

.info-content {
  width: 230px;
  height: 80px;

  &-icon {
    margin: 2%;
  }

  &-text {
    display: inline-block;
  }
}

.information-button {
  width: 44px;
  height: 44px;
  position: absolute;
  top: 85%;
  right: 5%;
  z-index: 2;
}

.bg {
  position: absolute;
  top: 0;
  height: 100%;
  width: 100%;
  filter: blur(8px);
  -webkit-filter: blur(8px);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  z-index: -1;
}

::v-deep(.p-timeline .p-timeline-event-marker) {
  border: 2px solid #ff8811;
  background-color: #ff8811;
}

.detailed-view-button {
  width: 44px;
  height: 44px;
  position: absolute;
  top: 75%;
  right: 5%;
  z-index: 2;
  background: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;

  img {
    width: 30px;
    height: 40px;
  }
}

@media (min-width: 1024px) {
  .detailed-view-button {
    width: 80px;
    height: 80px;
  }
}
</style>
