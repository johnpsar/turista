<template>
  <Modal v-if="isModalVisible" @close-modal="isModalVisible = false">
    <template #header>
      <div class="info-modal-header">
        <div class="info-modal-header-back" @click="isModalVisible = false">
          <div class="info-modal-header-back-icon">
            <img :src="BackIcon" />
          </div>
          <div class="info-modal-header-back-text">Back</div>
        </div>
      </div>
    </template>
    <template #content>
      <div class="info-modal-content">
        <div class="info-modal-content-image">
          <img :src="imageUrl" />
        </div>
        <div class="info-modal-content-stats">
          <div class="info-modal-content-stats-data busy">
            <div class="info-modal-content-stats-data-icon">
              <img :src="Busy" />
            </div>
            <div class="info-modal-content-stats-data-primary">{{ timeToVisit[Math.floor(Math.random() * 15)] }}</div>
            <div class="info-modal-content-stats-data-secondary">Ideal time to visit</div>
          </div>
          <div class="info-modal-content-stats-data distance">
            <div class="info-modal-content-stats-data-icon">
              <img :src="Distance" />
            </div>
            <div class="info-modal-content-stats-data-primary">5km</div>
            <div class="info-modal-content-stats-data-secondary">Direction</div>
          </div>
          <div class="info-modal-content-stats-data weather">
            <div class="info-modal-content-stats-data-icon">
              <img :src="Sun" />
            </div>
            <div class="info-modal-content-stats-data-primary">
              {{ props.weather[0].temperature }}
            </div>
            <div class="info-modal-content-stats-data-secondary">
              {{ props.weather[0].condition }}
            </div>
          </div>
        </div>
        <div class="info-modal-content-info">
          <div class="info-modal-content-info-title">{{ data[activeSlide].name }}</div>
          <div class="info-modal-content-info-content">
            {{ data[activeSlide].desc }}
          </div>
        </div>
      </div>
    </template>
  </Modal>
  <div class="timeline-container">
    <div class="bg" v-bind:style="{
      backgroundImage: `url(&quot;${imageUrl}&quot;)`,
    }" />
    <div class="timeline-container-content">
      <div class="timeline-container-content-weather">
        <Weather :weather="props.weather" />
      </div>
      <div class="timeline-container-content-title">
        Follow these steps for optimal enjoyment.
      </div>
      <div class="timeline-container-content-slided">
        <swiper :slidesPerView="slidesPerView" :navigation="true" :modules="modules" class="mySwiper" ref="myswiper"
          @swiper="setSwiperRef" @slideChange="onSlideChange" :virtual="true">
          <swiper-slide v-for="index in props.count" :key="index" :virtualIndex="index">
            <!-- <img :src="images[index - 1]"  /> -->
            <TimelineCard v-model="isModalVisible" :image="props.data[activeSlide].path" @refresh="onRefresh(index)"
              :checkedIn="checkedIn[index - 1]" :recommendation="props.data[index - 1]"
              @checkin="onCheckIn(index - 1)" />
            <!-- TODO: @refresh -->
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import BackIcon from "../assets/icons/back.svg";
import Busy from "../assets/icons/busy.svg";
import Distance from "../assets/icons/distance.svg";
import Sun from "../assets/icons/sun.svg";
import Weather from "../components/Weather.vue";
import Modal from "../components/Modal.vue";
import TimelineCard from "../components/TimelineCard.vue";
// import Swiper JS
import { Swiper, SwiperSlide } from "swiper/vue";
// import Swiper styles
import "swiper/css";
import "swiper/css/virtual";
import { Navigation, Virtual } from "swiper";
import { computed, onMounted, ref, watch } from "vue";
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

const images = [
  Museum1,
  Museum4,
  Out1,
  Out2,
  Beach2,
  Out3,
  Out4,
  Religion1,
  Religion2,
  Museum3,
  Religion3,
  Nature1,
  Museum5,
  Nature2,
  Nature3,
  Museum2,
  Beach1,
  Beach3,
];

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
const props = defineProps<{
  data: recommendation[];
  weather: weather[];
  count: number;

}>();


const emit = defineEmits<{
  (e: "refresh", v: number): void;
}>();

//TODO: checkedin array computed
const checkedIn = ref([false, false, false, false, false, false, false]);
const timeToVisit = ref(["9:00-11:00", "15:00-17:00", "16:00-17:00", "11:00-12:00", "13:00-14:00", "17:00-19:00", "18:00-19:00", "20:00-21:00", "10:00-12:00", "18:00-22:00", "9:00-11:00", "15:00-17:00", "16:00-17:00", "11:00-12:00", "13:00-14:00"]);
const modules = [Navigation, Virtual];
const isModalVisible = ref(false);
//@ts-ignore
let swiperRef = null;
//@ts-ignore
const setSwiperRef = (swiper) => {
  swiperRef = swiper;
};
const activeSlide = ref(0);
//@ts-ignore
const slideTo = (index) => {
  //@ts-ignore
  swiperRef.slideTo(index - 1, 0);
};

function onSlideChange() {
  //@ts-ignore
  activeSlide.value = swiperRef.activeIndex as number;
}
function onCheckIn(index: number) {
  console.log(index);
  checkedIn.value[index] = !checkedIn.value[index];
}

const slidesPerView = computed(() => {
  if (screen.width > 1024) {
    return 2.2;
  } else {
    return 1.2;
  }
});
const imageUrl =computed( ()=>new URL(props.data[activeSlide.value].path, import.meta.url).href)

function onRefresh(index: number) {
  emit("refresh", index - 1);
}
</script>

<style scoped lang="scss">
.info-modal {
  &-header {
    width: 100%;
    height: 60px;
    display: flex;
    align-items: center;

    &-back {
      width: 104px;
      height: 44px;
      display: flex;
      justify-content: center;
      align-items: center;
      background: #ffffff50;
      backdrop-filter: blur(15px);
      border-radius: 25px;
    }
  }

  &-content {
    width: 100%;
    height: calc(100% - 60px);
    padding: 4px 0;
    overflow: auto;

    &-image {
      width: 100%;
      height: 240px;
      margin-bottom: 12px;

      img {
        width: 100%;
        height: 100%;
        border-radius: 15px;
        object-fit: cover;
      }
    }

    &-stats {
      height: 80px;
      width: 100%;
      display: flex;

      &-data {
        width: 33%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;

        &-icon {
          height: 50%;
          width: 100%;

          img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
          }
        }

        &-primary {
          font-weight: 600;
          font-size: 16px;
          color: white;
        }

        &-secondary {
          font-weight: 400;
          font-size: 12px;
          color: #ffffff90;
        }
      }
    }

    &-info {
      color: white;
      padding: 4px;

      &-title {
        font-weight: 600;
        font-size: 18px;
      }

      &-content {
        font-weight: 400;
        font-size: 14px;
      }
    }
  }
}

.busy,
.distance {
  //hackia gia mikrotero border
  border-right: 1px solid #fff;
}

.timeline-container {
  width: 100%;
  height: 100%;

  &-header {
    height: 10%;
    width: 100%;
  }

  &-content {
    height: 90%;
    width: 100%;

    &-weather {
      width: 100%;
      height: 80px;
      z-index: 100;
    }

    &-title {
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      font-weight: 600;
      font-size: 16px;
      color: #fff;
      text-shadow: 0px 4px 4px rgba(41, 45, 50, 0.25);
    }

    &-slides {
      width: 100%;
      height: 90%;
    }
  }
}

.bg {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  filter: blur(8px);
  -webkit-filter: blur(8px);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  z-index: -1;
}

swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  /* Center slide text vertically */
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide img {
  margin: 40px 0 0 40px;
  display: block;
  width: 240px;
  height: 366px;
  border-radius: 15px;
  object-fit: cover;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px,
    rgba(0, 0, 0, 0.3) 0px 18px 36px -18px;
}

@media (min-width: 1024px) {
  .timeline-container-content-title {
    font-size: 32px;
  }

  .info-modal {
    &-header {
      width: 100%;
      height: 60px;
      display: flex;
      align-items: center;

      &-back {
        width: 104px;
        height: 44px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: #ffffff50;
        backdrop-filter: blur(15px);
        border-radius: 25px;
      }
    }

    &-content {
      width: 100%;
      height: calc(100% - 60px);
      padding: 4px 0;
      overflow: auto;

      &-image {
        width: 100%;
        height: 50%;
        margin-bottom: 12px;

        img {
          width: 100%;
          height: 100%;
          border-radius: 15px;
          object-fit: cover;
        }
      }

      &-stats {
        height: 80px;
        width: 100%;
        display: flex;

        &-data {
          width: 33%;
          height: 100%;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: space-between;

          &-icon {
            height: 50%;
            width: 100%;

            img {
              width: 100%;
              height: 100%;
              border-radius: 50%;
            }
          }

          &-primary {
            font-weight: 600;
            font-size: 16px;
            color: white;
          }

          &-secondary {
            font-weight: 400;
            font-size: 12px;
            color: #ffffff90;
          }
        }
      }

      &-info {
        color: white;
        padding: 4px;
        width: 100%;
        height: 40%;
        overflow: auto;

        &-title {
          font-weight: 600;
          font-size: 24px;
        }

        &-content {
          font-weight: 400;
          font-size: 14px;
        }
      }
    }
  }
}
</style>
