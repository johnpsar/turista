<template>
  <div class="weather-pair-container">
    <div class="weather-pair-container-icon">
      <img :src="image" />
    </div>
    <div class="weather-pair-container-pair">
      <div class="weather-pair-container-pair-date"> {{props.when}}</div>
      <div class="weather-pair-container-pair-info">{{props.temperature}} C</div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  image: string;
  when:string;
  temperature:string;
}>();
</script>

<style scoped lang="scss">
.weather-pair-container {
  width: 100%;
  height: 100%;
  display: flex;
  &-icon {
    width: 40%;
    height: 100%;
    & img {
      width: 100%;
      height: 100%;
    }
  }
  &-pair {
    display: flex;
    flex-direction: column;
    justify-content: center;
    &-date {
      font-weight: 400;
      font-size: 12px;
      color: white;
    }
    &-info {
      font-weight: 600;
      font-size: 14px;
      color: #ffffff;
      text-shadow: 0px 4px 4px rgba(41, 45, 50, 0.25);
    }
  }
}
</style>
