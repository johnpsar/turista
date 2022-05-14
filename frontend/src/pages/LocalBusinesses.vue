<template>
  <div class="food-container">
    <div class="food-container-header">
      <Header />
    </div>
    <div class="food-container-content">
      <h1 class="food-container-content-title">
        {{ props.type.charAt(0).toUpperCase() }}{{ props.type.slice(1) }}
      </h1>
      <div class="food-container-content-cards">
        <div
          class="row"
          v-for="option in displayed.slice(0, 2)"
          :key="option.name"
        >
          <div class="col-6">
            <div class="card">
              <img :src="option.image" class="card-img-top" alt="..." />
              <div class="card-body">
                <h5 class="card-title">{{ option.name }} <img :src="Map" /></h5>
              </div>
            </div>
          </div>
        </div>
        <div
          class="row"
          v-for="option in displayed.slice(2, 4)"
          :key="option.name"
        >
          <div class="col-6">
            <div class="card">
              <img :src="option.image" class="card-img-top" alt="..." />
              <div class="card-body">
                <h5 class="card-title">{{ option.name }} <img :src="Map" /></h5>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="food-container-content-back2break"
        @click="router.push('/break')"
      >
        Back
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Header from "../components/Header.vue";
import { useRouter, useRoute } from "vue-router";
import Map from "../assets/icons/map.svg";

import Food1 from "../assets/local_businesses/pantheon.jpg";
import Food2 from "../assets/local_businesses/gb_roof_garden.jpg";
import Food3 from "../assets/local_businesses/dinner_in_the_sky.jpg";
import Food4 from "../assets/local_businesses/psarochori.jpg";

import Drink1 from "../assets/local_businesses/ale_blues.jpg";
import Drink2 from "../assets/local_businesses/a_for_athens.jpg";
import Drink3 from "../assets/local_businesses/Rabbithole.jpg";
import Drink4 from "../assets/local_businesses/tiki_tiki_bar.jpg";

import Coffee1 from "../assets/local_businesses/il_coffee_and_resto.jpg";
import Coffee2 from "../assets/local_businesses/cultivos_coffee.jpg";
import Coffee3 from "../assets/local_businesses/portatif_cafe.jpg";
import Coffee4 from "../assets/local_businesses/victory_cafe.jpg";

import Shop1 from "../assets/local_businesses/olive_tree.png";
import Shop2 from "../assets/local_businesses/canvas.png";
import Shop3 from "../assets/local_businesses/fotinis_deli.png";
import Shop4 from "../assets/local_businesses/Pantopolion.png";
import { computed } from "@vue/reactivity";

const props = defineProps<{
  type: string;
}>();
const router = useRouter();

const food = [
  { name: "Pantheon", image: Food1 },
  { name: "Great Britain Roof Garden", image: Food2 },
  { name: "Dinner In The Sky", image: Food3 },
  { name: "Psarochori", image: Food4 },
];
const drink = [
  { name: "Ale Blues", image: Drink1 },
  { name: "A for Athens", image: Drink2 },
  { name: "Rabbithole", image: Drink3 },
  { name: "Tiki Tiki Bar", image: Drink4 },
];
const coffee = [
  { name: "Il coffee", image: Coffee1 },
  { name: "Cultivos coffee", image: Coffee2 },
  { name: "Portatif cafe", image: Coffee3 },
  { name: "Victory cafe", image: Coffee4 },
];
const shop = [
  { name: "Olive Tree", image: Shop1 },
  { name: "Canvas", image: Shop2 },
  { name: "Fotinis Deli", image: Shop3 },
  { name: "Pantopolion", image: Shop4 },
];

const displayed = computed(() => {
  switch (props.type) {
    case "food":
      return food;
    case "drinks":
      return drink;
    case "coffee":
      return coffee;
    case "souvenirs":
      return shop;
    default:
      return food;
  }
});
</script>

<style scoped lang="scss">
.food-container {
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
    padding-top: 2%;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-y: auto;
    overflow-x: hidden;

    &::-webkit-scrollbar {
      display: none;
    }

    &-title {
      width: 80%;
      display: flex;
      justify-content: center;
      align-items: center;
      color: black;
      font-size: 2em;
      margin-bottom: 5%;
      font-style: italic;
      font-weight: 700;
    }

    &-cards {
      .col-6 {
        height: 180px !important;
        margin: 2% auto;

        .card {
          height: 100%;
        }
      }

      .card-title {
        font-size: 1.2em !important;
        font-weight: bold;
      }
    }

    &-back2break {
      width: 25%;
      height: 40px;
      color: white;
      font-size: 14px;
      font-weight: 600;
      background: #ff8811;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 12px;
      margin-top: 5%;
    }
  }

  @media (min-width: 1024px) {
    .food-container {
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
        padding-top: 3%;
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow-y: auto;
        overflow-x: hidden;

        &::-webkit-scrollbar {
          display: none;
        }

        &-title {
          width: 80%;
          display: flex;
          justify-content: center;
          align-items: center;
          color: black;
          font-size: 32px;
          margin-bottom: 3%;
          font-style: italic;
          font-weight: 700;
        }

        &-cards {
          .col-6 {
            height: 400px !important;
            width:440px;
            margin: 1% auto;

            .card {
              height: 100%;
              width:100%;
            }
          }

          .card-title {
            font-size: 1.2em !important;
            font-weight: bold;
          }
        }

        &-back2break {
          width: 25%;
          min-height: 60px;
          height: 60px !important;
          color: white;
          font-size: 30px;
          font-weight: 600;
          background: #ff8811;
          display: flex;
          justify-content: center;
          align-items: center;
          border-radius: 12px;
          margin-top: 1%;
        }
      }
    }
  }
}
</style>
