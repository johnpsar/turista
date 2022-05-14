<template>
  <div class="icons">
    <div class="icon" v-for="icon in images">
      <img :src="icon" />
    </div>
  </div>
  <div class="image-card-container">
    <div class="image-card-container-image" :class="props.isSelected ? 'selected-image' : ''">
      <img :src="props.img" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import Sun from "../assets/icons/sun.svg";
import Wind from "../assets/icons/wind.svg";
import Snow from "../assets/icons/snow.svg";
import Rain from "../assets/icons/rain.svg";

const props = defineProps<{
  img: string;
  tags: string[];
  isSelected: boolean;
}>();

const images = computed(() => {
  let temp: string[] = [];
  props.tags.forEach((tag) => {
    switch (tag) {
      case "sun":
        temp.push(Sun);
        break;
      case "rain":
        temp.push(Rain);
        break;
      case "snow":
        temp.push(Snow);
        break;
      case "wind":
        temp.push(Wind);
        break;
      default:
        break;
    }
  });
  return temp;
});
</script>

<style scoped lang="scss">
.image-card-container {
  width: 160px;
  height: 160px;
  display: flex;
  justify-content: center;
  align-items: center;

  //   border: 1px solid black;
  &-image {
    width: 150px;
    height: 150px;
    border-radius: 12px;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;

    img {
      background: #00000010;
      border-radius: 50%;
      width: 100%;
      height: 100%;
      border-radius: 12px;
      object-fit: fill;
    }
  }
}

.icons {
  display: flex;
  gap: 10px;
  margin-left: 18px;
}

.icon {
  width: 24px;
  height: 24px;

  img {
    margin-top: 40px;
    background: #00000010;
    border-radius: 50%;
    position: relative;
    z-index: 1;
    width: 24px;
    height: 24px;
  }
}

.selected-image {
  box-shadow: #06BCC1 0px 0px 0px 3px;

}
</style>
