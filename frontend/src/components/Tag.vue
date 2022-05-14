<template>
  <div class="tag-container" :class="props.type">
    <div class="tag-container-icon">
      <img
        v-if="props.type === 'wind'"
        src="../assets/icons/wind.svg"
      />
      <img v-else-if="props.type === 'rain'" src="../assets/icons/rain.svg" />

      <img v-else-if="props.type === 'sun'" src="../assets/icons/sun.svg" />

      <img v-else-if="props.type === 'snow'" src="../assets/icons/snow.svg" />
    </div>
    <div class="tag-container-title">
      Ideal for {{ props.type }}
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  type: "sun" | "rain" | "snow" | "wind";
}>();
</script>

<style scoped lang="scss">
.tag-container {
  width: auto;
  height: 36px;
  padding:0 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-radius: 12px;
  margin-bottom: 4px;//todo remove
  
  &-icon {
    width: 30px;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 12px;
    img {
      width: 100%;
      height: 100%;
      object-fit: fill;
    }
  }
  &-title {
    font-size: 12px;
    font-weight: 600;
  }
}

.wind{
  border: 1px solid green;

}
.rain{
  border: 1px solid blue;

}
.snow{
  border: 1px solid aqua;

}
.sun{
  border: 1px solid orange;

}
</style>
