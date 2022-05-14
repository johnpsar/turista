<template>
  <div class="recommendations-container">
    <div class="recommendations-container-header">
      <Header />
    </div>
    <div class="recommendations-container-title">
      Select images you like and we 'll find you places you 'll love.
    </div>
    <!-- TODO: be able to remove images when you click second time -->
    <div class="recommendations-container-images">
      <template v-for="(image, index) in images" :key="index">
        <div :class="`div${index} image`" @click="onClick(index)">
          <recommendation-card :isRain="tags[index].isRain" :isSnow="tags[index].isSnow" :isWind="tags[index].isWind"
            :isSun="tags[index].isSun" :image="image" :number="
              isSelected(index)
                ? selected.findIndex((i) => i === index) + 1
                : -1
            " />
        </div>
      </template>
    </div>
    <div class="proceed-button" v-if="selected.length > 0" @click="router.push('/route')">
      My route &nbsp;<img :src="Back" />
    </div>
  </div>
  <div class="information-button" @click="overlay?.toggle">
    <img :src="Info" />
  </div>
  <OverlayPanel ref="overlay" class="overlay">
    <div class="recommendations-container-content-tags">
      <div>
        <Tag type="wind" />
        <Tag type="snow" />
      </div>
      <div>
        <Tag type="rain" />
        <Tag type="sun" />
      </div>
    </div>
  </OverlayPanel>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from "vue";
import Header from "../components/Header.vue";
import RecommendationCard from "../components/RecommendationCard.vue";
import Back from "../assets/icons/back.svg";
import { useRouter } from "vue-router";
import OverlayPanel from "primevue/overlaypanel";
import Tag from "../components/Tag.vue";
import Info from "../assets/icons/info.svg";

import Museum1 from "../assets/recommendations/museums1.jpg";
import Museum2 from "../assets/recommendations/museums2.jpg";
import Museum3 from "../assets/recommendations/museums3.jpg";
import Museum4 from "../assets/recommendations/museums4.jpg";
import Museum5 from "../assets/recommendations/museums5.jpg";
import Out1 from "../assets/recommendations/out1.jpg";
import Out2 from "../assets/recommendations/out2.jpg";
import Out3 from "../assets/recommendations/out3.jpg";
import Out4 from "../assets/recommendations/out4.jpg";
import Religion1 from "../assets/recommendations/religion1.jpg";
import Religion2 from "../assets/recommendations/religion2.jpg";
import Religion3 from "../assets/recommendations/religion3.jpg";
import Nature1 from "../assets/recommendations/nature1.jpg";
import Nature2 from "../assets/recommendations/nature2.jpg";
import Nature3 from "../assets/recommendations/nature3.jpg";
import Beach1 from "../assets/recommendations/beach1.jpg";
import Beach2 from "../assets/recommendations/beach2.jpg";
import Beach3 from "../assets/recommendations/beach3.jpg";

const emit = defineEmits<{
  (e: "updateRecommendations", v: number[]): void;
}>();
const router = useRouter();

const overlay = ref<{
  toggle: () => void;
}>();

const images = [
  Beach2,
  Out1,
  Beach1,
  Out2,
  Museum5,
  Religion3,
  Out3,
  Nature3,
  Religion1,
  Museum3,
  Museum1,
  Beach3,
  Museum4,
  Religion2,
  Nature1,
  Museum2,
  Out4,
  Nature2,
];

const tags = [
  { isRain: false, isWind: false, isSnow: false, isSun: true },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
  { isRain: false, isWind: false, isSnow: false, isSun: true },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
  { isRain: true, isWind: true, isSnow: true, isSun: true },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
  { isRain: true, isWind: true, isSnow: true, isSun: true },
  { isRain: true, isWind: true, isSnow: true, isSun: false },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
  { isRain: true, isWind: true, isSnow: true, isSun: false },
  { isRain: false, isWind: true, isSnow: true, isSun: true },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
  { isRain: true, isWind: true, isSnow: true, isSun: true },
  { isRain: false, isWind: false, isSnow: false, isSun: true },
  { isRain: false, isWind: true, isSnow: false, isSun: true },
];
const selected = ref<Array<number>>([]);
function onClick(index: number) {
  const indexInArray = selected.value.findIndex((i) => i === index);
  if (indexInArray >= 0) {
    selected.value.slice(indexInArray, 1);
  } else {
    selected.value.push(index);
    ratings.value[index] = 5;
    emit("updateRecommendations", ratings.value);
  }
}
function isSelected(index: number) {
  return selected.value.findIndex((i) => i === index) >= 0;
}
const ratings = ref<Array<number>>([]);
onMounted(() => {
  for (let i = 0; i < 18; i++) {
    ratings.value[i] = 1;
  }
  emit("updateRecommendations", ratings.value);
});
</script>

<style scoped lang="scss">
.cover {
  position: absolute;
  z-index: 10;
  width: 200px;
  height: 100px;
  background: #0000ff50;
}

.recommendations-container {
  font-family: "Montserrat Alternates", sans-serif;
  font-style: italic;
  width: 100%;
  height: 100%;

  &-images {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(12, 120px);
    grid-column-gap: 0px;
    grid-row-gap: 0px;
  }

  &-title {
    margin: 8px;
    font-size: 24px;
    font-weight: 600;
    padding: 4px 16px;
    color: #000;
  }
}

.div1 {
  grid-area: 1 / 1 / 3 / 2;
}

.div2 {
  grid-area: 1 / 2 / 2 / 3;
}

.div3 {
  grid-area: 2 / 2 / 4 / 3;
}

.div4 {
  grid-area: 3 / 1 / 4 / 2;
}

.div5 {
  grid-area: 4 / 1 / 6 / 2;
}

.div6 {
  grid-area: 4 / 2 / 5 / 3;
}

.div7 {
  grid-area: 5 / 2 / 7 / 3;
}

.div8 {
  grid-area: 6 / 1 / 7 / 2;
}

.div9 {
  grid-area: 7 / 1 / 9 / 2;
}

.div10 {
  grid-area: 7 / 2 / 8 / 3;
}

.div11 {
  grid-area: 8 / 2 / 10 / 3;
}

.div12 {
  grid-area: 10 / 2 / 11 / 3;
}

.div13 {
  grid-area: 11 / 2 / 13 / 3;
}

.div14 {
  grid-area: 9 / 1 / 10 / 2;
}

.div15 {
  grid-area: 10 / 1 / 12 / 2;
}

.div16 {
  grid-area: 12 / 1 / 13 / 2;
}

.image {
  width: 100%;
  height: 100%;
  padding: 4px;

  img {
    width: 100%;
    height: 100%;
    object-fit: fill;
    border-radius: 12px;
  }
}

.proceed-button {
  position: absolute;
  top: 90%;
  right: 15%;
  width: 260px;
  height: 50px;
  background: #ff8811;
  border-radius: 12px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 20px;
  font-weight: 600;
  z-index: 100;

  img {
    transform: rotate(180deg);
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

@media (min-width: 1024px) {
  .information-button {
    width: 66px;
    height: 66px;
    position: absolute;
    top: 85%;
    right: 5%;
    z-index: 2;
  }

  .recommendations-container {
    &-title {
      width: 100%;
      display: flex;
      justify-content: center;
      font-size: 40px;
    }
  }

  .proceed-button {
    position: absolute;
    top: 90%;
    right: 15%;
    width: 70%;
    height: 70px;
    background: #ff8811;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 30px;
    font-weight: 600;

    img {
      transform: rotate(180deg);
    }
  }
}
</style>
