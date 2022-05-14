<template>
  <div class="timeline-container">
    <div class="timeline-container-content">
      <Timeline
        class="timeline"
        :value="props.data.slice(0, Math.floor(props.count / 2))"
        align="alternate"
      >
        <template #content="slotProps">
          <div class="timeline-container-content-card">
            <div class="timeline-container-content-card-body">
              <h2 class="timeline-container-content-card-body-title">
                {{ slotProps.item.name }}
              </h2>
              <hr />
              <div class="timeline-container-content-card-body-text">
                <button
                  id="map-btn"
                  classs="timeline-container-content-card-body-title-map"
                >
                  <a :href="slotProps.item.url" target="_blank"
                    ><img :src="Map"
                  /></a>
                </button>
              </div>
            </div>
          </div>
        </template>
      </Timeline>
      <div class="break-card">
        <div class="break-card-body">
          <h2 class="break-card-body-title">Stop! Time for a break</h2>
          <hr />
          <div class="break-card-body-text">
            <button id="break-btn" @click="router.push('/break')">
              View More
              <img :src="Cup" />
              <img :src="KitchenTools" />
            </button>
          </div>
        </div>
      </div>
      <Timeline
        class="timeline"
        :value="props.data.slice(Math.floor(props.count / 2), props.count)"
        align="alternate"
      >
        <template #opposite="slotProps">
          <div class="timeline-container-content-card">
            <div class="timeline-container-content-card-body">
              <h2 class="timeline-container-content-card-body-title">
                {{ slotProps.item.name }}
              </h2>
              <hr />
              <div class="timeline-container-content-card-body-text">
                <button
                  id="map-btn"
                  classs="timeline-container-content-card-body-title-map"
                >
                  <a :href="slotProps.item.url" target="_blank"
                    ><img :src="Map"
                  /></a>
                </button>
              </div>
            </div>
          </div>
        </template>
      </Timeline>
      <div class="information-button" @click="overlay?.toggle">
        <img :src="Info" />
      </div>
      <OverlayPanel ref="overlay" class="overlay">
        <div class="info-content">
          <img class="info-content-icon" :src="Map" />
          <p class="info-content-text">: See location in google maps</p>
        </div>
      </OverlayPanel>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, watch } from "vue";
import Timeline from "primevue/timeline";
import { useRouter, useRoute } from "vue-router";
import Map from "../assets/icons/map.svg";
import Info from "../assets/icons/info.svg";
import Cup from "../assets/icons/cup.svg";
import KitchenTools from "../assets/icons/tools-kitchen.svg";

import OverlayPanel from "primevue/overlaypanel";


const overlay = ref<{
  toggle: () => void;
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
const props = defineProps<{
  data: recommendation[];
  count: number;
}>();

onMounted(()=>console.log(props.data))


const router = useRouter();
</script>

<style scoped lang="scss">
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

    &-card {
      font-family: "Montserrat Alternates", sans-serif;
      font-weight: 700 !important;
      text-align: center;
      border: 3px solid #06bcc1;
      border-radius: 12px;
      max-width: 100%;
      padding: 5%;
      background-color: rgba($color: white, $alpha: 0.5);

      &-body {
        text-align: center;
        align-items: center;
        justify-content: center;
        padding: 2%;

        &-title {
          font-weight: 700 !important;
          font-size: 17px;
        }

        hr {
          height: 2px;
          background-color: #ff8811;
          width: 80%;
          margin-left: auto;
          margin-right: auto;
          margin-top: 0;
          margin-bottom: 2%;
        }

        &-text {
          #map-btn {
            margin: 0 5%;
            display: inline-block;
          }
        }
      }
    }
  }
}

.break {
  &-card {
    text-align: center;
    margin: 3%;
    border: 3px solid red;
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
        background-color: red;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        margin-top: 0;
        margin-bottom: 2%;
      }

      &-title {
        font-weight: 900;
      }

      &-text {
        #break-btn {
          margin-top: 3%;
          margin-bottom: 0;
          padding: 3%;
          border: 2px solid #06bcc1;
          border-radius: 10px;
          font-weight: 700;
          background-color: rgba($color: white, $alpha: 0.7);
        }
      }
    }
  }
}

.info-content {
  width: 230px;
  height: 40px;

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

.timeline {
  margin: 5% auto;
}

::v-deep(.p-timeline .p-timeline-event-marker) {
  border: 2px solid #ff8811;
  background-color: #ff8811;
}

@media (min-width: 1024px) {
  .information-button {
    width: 80px;
    height: 80px;
    position: absolute;
    top: 85%;
    right: 5%;
    z-index: 2;
  }
}
</style>
