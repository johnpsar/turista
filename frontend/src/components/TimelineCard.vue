<template>
  <div class="timeline-card-container">
    <div class="timeline-card-container-image" @click="emit('update:modelValue', true)">
      <img :src="imageUrl" />
      <i class="pi pi-arrow-right" />
    </div>
    <div class="timeline-card-container-buttons">
      <div class="timeline-card-container-buttons-checkin" :class="props.checkedIn ? 'selected' : ''"
        @click="emit('checkin')">
        Check In
      </div>
      <div class="timeline-card-container-buttons-change" @click="emit('refresh')">Refresh</div>
    </div>
  </div>
  <!-- TODO:change hardcoded values -->
  <div class="title">{{ props.recommendation.name }}</div>
  <div class="discover"><u>Discover</u><img :src="Back" /></div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import Acropole from "../assets/acropole.jpg";
import Back from "../assets/icons/back.svg";
interface recommendation {
  id: string;
  name: string;
  url: string;
}
const props = defineProps<{
  image: string;
  modelValue: boolean;
  checkedIn: boolean;
  recommendation: recommendation;
}>();
const emit = defineEmits<{
  (e: "update:modelValue", v: boolean): void;
  (e: "refresh"): void;
  (e: "checkin"): void;
}>();

const imageUrl =computed( ()=>new URL(props.image, import.meta.url).href)
</script>

<style scoped lang="scss">
.timeline-card-container {
  width: 100%;
  height: 100%;
  padding: 4px 0;

  &-image {
    width: 240px;
    height: 366px;
    display: flex;
    align-items: center;
    justify-content: space-between;

    img {
      margin: 4px 0 0 40px;
      display: block;
      width: 100%;
      height: 100%;
      border-radius: 15px;
      object-fit: cover;
      box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px,
        rgba(0, 0, 0, 0.3) 0px 18px 36px -18px;
    }
  }

  &-buttons {
    width: 80%;
    margin-left: 40px;
    height: 60px;
    display: flex;
    justify-content: space-around;
    align-items: center;

    &-checkin {
      width: 80px;
      height: 40px;
      background: grey;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 8px;
    }

    &-change {
      width: 80px;
      height: 40px;
      background: black;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 8px;
    }
  }
}

.selected {
  background: green;
}

.title {
  position: absolute;
  top: 5%;
  left: 28.5%;
  font-weight: 600;
  font-size: 22px;
  color: white;
  text-shadow: 0px 4px 4px rgba(41, 45, 50, 0.25);
}

.discover {
  position: absolute;
  top: 73%;
  left: 25%;
  font-weight: 600;
  font-size: 18px;
  color: #ffffff;
  text-shadow: 0px 4px 4px rgba(41, 45, 50, 0.25);

  img {
    transform: rotate(180deg);
  }


}

.pi-arrow-right {
  font-size: 20px;
  margin-left: 12px;
  color: white;
}

@media (min-width: 1024px) {
  .timeline-card-container {
    width: 100%;
    height: 100%;
    padding: 4px 0;

    &-image {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 75%;
      height: 100%;

      img {
        margin: 4px 0 0 40px;
        display: block;
        width: 480px;
        height: 700px;
        border-radius: 15px;
        object-fit: cover;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px,
          rgba(0, 0, 0, 0.3) 0px 18px 36px -18px;
      }
    }

    &-buttons {
      width: 60%;
      margin-left: 40px;
      height: 60px;
      display: flex;
      justify-content: space-around;
      align-items: center;

      &-checkin {
        width: 80px;
        height: 40px;
        background: grey;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 8px;
      }

      &-change {
        width: 80px;
        height: 40px;
        background: black;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 8px;
      }
    }
  }

  .selected {
    background: green;
  }

  .title {
    position: absolute;
    top: 5%;
    left: 28.5%;
    font-weight: 600;
    font-size: 32px;
    color: white;
    text-shadow: 0px 4px 4px rgba(41, 45, 50, 0.25);
  }

  .discover {
    position: absolute;
    top: 80%;
    left: 40%;
    font-weight: 600;
    font-size: 24px;
    color: #ffffff;
    text-shadow: 0px 4px 4px rgba(41, 45, 50, 0.25);

    img {
      transform: rotate(180deg);
    }
  }

  .pi-arrow-right {
    font-size: 100px;
    margin-left: 30px;
    color: white;
  }
}
</style>
