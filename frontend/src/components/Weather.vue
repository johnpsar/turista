<template>
  <div class="weather-container">
    <div class="weather-container-current-weather">
      <WeatherPair
        when="Now"
        :image="imageNow"
        :temperature="props.weather[0].temperature"
      />
    </div>
    <div class="weather-container-later-weather">
      <WeatherPair
        when="In 3 hours"
        :image="imageLater"
        :temperature="props.weather[1].temperature"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import WeatherPair from "./WeatherPair.vue";
import Sun from "../assets/3d/sun.svg";
import Rain from "../assets/3d/rain.svg";
import SunCloud from "../assets/3d/suncloud.svg";
import { computed } from "vue";

const imageNow = computed(() => {
  switch (props.weather[0].condition) {
    case "sun":
      return Sun;
    case "rain":
      return Rain;
    case "wind":
      return SunCloud;
    default:
      return Sun;
  }
});
const imageLater = computed(() => {
  switch (props.weather[1].condition) {
    case "sun":
      return Sun;
    case "rain":
      return Rain;
    case "wind":
      return SunCloud;
    default:
      return Sun;
  }
});
interface weather {
  condition: string;
  temperature: string;
}
const props = defineProps<{
  weather: weather[];
}>();
</script>

<style scoped lang="scss">
.weather-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  &-current-weather {
    width: 50%;
    height: 100%;
  }
  &-later-weather {
    width: 50%;
    height: 100%;
  }
}
</style>
