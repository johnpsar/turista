<template>
  <div class="container">
    <img
      :src="props.image"
      alt="Avatar"
      class="image"
      :class="props.number > -1 ? 'selected' : ''"
    />
    <div class="middle" v-if="props.number > -1">
      <div class="text">{{ props.number }}</div>
    </div>
    <template v-for="(i,index) in icons" :key="i">
      <img class="icon" :class="`icon${index}`" :src="i" />

    </template>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import Acropole from "../assets/acropole.jpg";
import Rain from "../assets/icons/rain.svg";
import Snow from "../assets/icons/snow.svg";
import Sun from "../assets/icons/sun.svg";
import Wind from "../assets/icons/wind.svg";

const props = defineProps<{
  image: string;
  number: number;
  isRain:boolean;
  isSun:boolean;
  isWind:boolean;
  isSnow:boolean;
}>();
const icons=ref<Array<string>>([])


onMounted(() => {
  if(props.isRain) icons.value.push(Rain)
  if(props.isSun) icons.value.push(Sun)
  if(props.isSnow) icons.value.push(Snow)
  if(props.isWind) icons.value.push(Wind)

  
})
</script>

<style scoped lang="scss">
.container {
  position: relative;
  width: 100%;
  height: 100%;
}

.image {
  opacity: 1;
  display: block;
  width: 100%;
  height: 100%;
  border-radius: 5px;
  transition: 0.5s ease;
  backface-visibility: hidden;
  object-fit: cover;
}

.middle {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: 0.5s ease;
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
  opacity: 1;
  background-color: #2669a070;
  border-radius: 5px;
  width: calc(100% - 20px);
}

.selected .image {
  opacity: 0.3;
}

.text {
  background-color: #00000080;
  color: white;
  font-size: 16px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon {
  width: 22px;
  height: 22px;
  position: absolute;
  z-index: 100;
}

.icon0 {
  top: 10px;
  left: 20px;
}
.icon1{
  top: 10px;
  left: 50px;
}
.icon2 {
  top: 10px;
  left: 80px;
}

.icon3 {
  top: 10px;
  left: 110px;
}

@media (min-width: 1024px) {
  .icon {
    width: 36px;
    height: 36px;
    position: absolute;
    z-index: 100;
    border-radius: 12px;
  }

  .icon0 {
    top: 10px;
    left: 20px;
  }
  .icon1 {
    top: 10px;
    left: 60px;
  }
  .icon2{
    top: 10px;
    left: 100px;
  }

  .icon3 {
    top: 10px;
    left: 140px;
  }
}
</style>
