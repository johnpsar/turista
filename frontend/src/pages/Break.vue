<template>
  <div class="break-container">
    <div class="break-container-header">
      <Header />
    </div>
    <div class="break-container-content">
      <h1 class="break-container-content-title">
        Break Time<img src="../assets/coffee-break.png" />
      </h1>
      <h2 class="break-container-content-more">
        We recommend visitng local restaurants, cafes, as well as souvenir shops
        to take the most of your vacation. <br />
        <p>Click a category to see some of our favorite places!</p>
      </h2>

      <div class="break-container-content-sponsored">
        <div class="row">
          <div class="col restaurants" @click="router.push('/places/food')">
            Food<br /><img src="../assets/food.png" />
          </div>
          <div class="col cafes" @click="router.push('/places/coffee')">
            Coffee<br />
            <img src="../assets/coffee-cup.png" /><img src="../assets/coffee.png" />
          </div>
        </div>
        <div class="row">
          <div class="col souvenirs" @click="router.push('/places/souvenirs')">
            Souvenirs<br /><img src="../assets/souvenirs.png" />
          </div>
          <div class="col drinks" @click="router.push('/places/drinks')">
            Drinks<br /><img src="../assets/cocktail.png" />
          </div>
        </div>
      </div>

      <!-- <h1 class="break-container-content-title" style="margin-top: 7%; font-size: 1.8em;">
                Enjoy!
            </h1> -->
      <div class="break-container-content-back2route" @click="router.push('/route')">
        Back to My Route
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Header from "../components/Header.vue";
import { useRouter, useRoute } from "vue-router";
const router = useRouter();
</script>

<style scoped lang="scss">
.break-container {
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
    overflow: hidden;

    &-title {
      width: 80%;
      display: flex;
      justify-content: center;
      align-items: center;
      color: black;
      font-size: 2em;
      margin-bottom: 2%;
      font-style: italic;
      font-weight: 700;

      img {
        width: 35px;
        margin-left: 2%;
      }
    }

    &-more {
      width: 85%;
      font-size: 1.1em;
      font-weight: 600;
      margin: 3% auto;
      margin-right: 3%;

      img {
        width: 20px;
        margin-left: 1%;
      }

      p {
        margin-top: 3%;
      }
    }

    &-sponsored {
      .col {
        width: 130px;
        height: 120px;
        margin: 2%;
        border-radius: 12px;
        font-size: 1.5em;
        font-weight: 600;
        text-align: center;
        color: white;
      }

      .restaurants {
        background-color: #f2ca80;
      }

      .restaurants img {
        width: 55px;
        margin-top: 15%;
      }

      .cafes {
        background-color: #9cc4e8;
      }

      .cafes img {
        height: 47px;
        margin-top: 15%;
      }

      .souvenirs {
        background-color: #7de2c2;
      }

      .souvenirs img {
        height: 60px;
        margin-top: 15%;
      }

      .drinks {
        background-color: #e2807d;
      }

      .drinks img {
        height: 60px;
        margin-top: 15%;
      }
    }

    &-back2route {
      width: 43%;
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
}

@media (min-width: 1024px) {
  .break-container {
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
      overflow: hidden;

      &-title {
        width: 80%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
        font-size: 40px;
        margin-bottom: 2%;
        font-style: italic;
        font-weight: 700;

        img {
          width: 40px;
          margin-left: 2%;
        }
      }

      &-more {
        width: 85%;
        font-size: 26px;
        font-weight: 600;
        margin: 3% auto;
        margin-right: 3%;

        img {
          width: 20px;
          margin-left: 1%;
        }

        p {
          margin-top: 3%;
        }
      }

      &-sponsored {
        .col {
          width: 200px;
          height: 130px;
          margin: 2%;
          border-radius: 12px;
          font-size: 1.5em;
          font-weight: 600;
          text-align: center;
          color: white;
        }

        .restaurants {
          background-color: #f2ca80;
        }

        .restaurants img {
          width: 55px;
          margin-top: 15%;
        }

        .cafes {
          background-color: #9cc4e8;
        }

        .cafes img {
          height: 47px;
          margin-top: 15%;
        }

        .souvenirs {
          background-color: #7de2c2;
        }

        .souvenirs img {
          height: 60px;
          margin-top: 15%;
        }

        .drinks {
          background-color: #e2807d;
        }

        .drinks img {
          height: 60px;
          margin-top: 15%;
        }
      }

      &-back2route {
        width: 43%;
        height: 50px;
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
  }
}
</style>
