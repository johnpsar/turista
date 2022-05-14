<template>
  <!-- TODO: content is not scrollable in modal -->
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
          <img :src="images[activeSlide]" />
        </div>
        <div class="info-modal-content-stats">
          <div class="info-modal-content-stats-data busy">
            <div class="info-modal-content-stats-data-icon">
              <img :src="Busy" />
            </div>
            <div class="info-modal-content-stats-data-primary">0</div>
            <div class="info-modal-content-stats-data-secondary">Not Busy</div>
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
            <div class="info-modal-content-stats-data-primary">16 C</div>
            <div class="info-modal-content-stats-data-secondary">Sunny</div>
          </div>
        </div>
        <div class="info-modal-content-info">
          <div class="info-modal-content-info-title">Lorem ipsum,Athens</div>
          <div class="info-modal-content-info-content">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis
            pretium augue nec nisl lobortis, eleifend imperdiet eros molestie.
            In facilisis urna at nibh fermentum, eget accumsan elit tristique.
            Aliquam rhoncus, velit vitae maximus tristique, erat diam malesuada
            sapien, eget varius diam nulla in orci. Nullam a nisi lacus.
            Pellentesque pharetra enim leo, et consectetur leo lacinia a. Proin
            elementum dui sit amet nunc venenatis aliquam. Pellentesque
            consequat ac enim vel ullamcorper. Vestibulum in nisl aliquam,
            scelerisque ipsum ut, ullamcorper nibh. Nunc iaculis tincidunt ante
            et consectetur. Sed sit amet velit nisl. Nam sodales urna egestas
            convallis sodales. Mauris non vestibulum tortor.
          </div>
        </div>
      </div>
    </template>
  </Modal>
  <div class="timeline-container">
    <div class="timeline-container-header">
      <Header />
    </div>
    <div
      class="bg"
      v-bind:style="{
        backgroundImage: `url(&quot;${images[activeSlide]}&quot;)`,
      }"
    />
    <div class="timeline-container-content">
      <div class="timeline-container-content-weather">
        <Weather />
      </div>
      <div class="timeline-container-content-title">
        Follow these steps for optimal enjoyment.
      </div>
      <div class="timeline-container-content-slided">
        <swiper
          :slidesPerView="1.2"
          :navigation="true"
          :modules="modules"
          class="mySwiper"
          ref="myswiper"
          @swiper="setSwiperRef"
          @slideChange="onSlideChange"
          :virtual="true"
        >
          <swiper-slide
            v-for="index in images.length"
            :key="index"
            :virtualIndex="index"
          >
            <!-- <img :src="images[index - 1]"  /> -->
            <TimelineCard
              v-model="isModalVisible"
              :image="images[index - 1]"
              :checkedIn="checkedIn[index - 1]"
              @checkin="onCheckIn(index - 1)"
            />
            <!-- TODO: @refresh -->
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Acropole from "../assets/acropole.jpg";
import Amazon from "../assets/amazon.jpg";
import Barcelone from "../assets/barcelone.jpg";
import Canada from "../assets/canada.jpg";
import Dubai from "../assets/dubai.jpg";
import EasterIslands from "../assets/easter-islands.jpg";
import Egypt from "../assets/egypt.jpg";
import BackIcon from "../assets/icons/back.svg";
import Busy from "../assets/icons/busy.svg";
import Distance from "../assets/icons/distance.svg";
import Sun from "../assets/icons/sun.svg";
import Header from "../components/Header.vue";
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
const images = [
  Acropole,
  Amazon,
  Barcelone,
  Canada,
  Dubai,
  EasterIslands,
  Egypt,
];
//TODO: checkedin array computed
const checkedIn = ref([false, false, false, false, false, false, false]);
const modules = [Navigation, Virtual];
const isModalVisible = ref(false);
let swiperRef = null;
const setSwiperRef = (swiper) => {
  swiperRef = swiper;
};
const activeSlide = ref(0);

const slideTo = (index) => {
  swiperRef.slideTo(index - 1, 0);
};

function onSlideChange() {
  activeSlide.value = swiperRef.activeIndex as number;
}
function onCheckIn(index: number) {
  console.log(index)
  checkedIn.value[index] = !checkedIn.value[index];
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
        font-size: 24px;
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
      height: 10%;
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
  height: 90%;
  width: 100%;
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
</style>
