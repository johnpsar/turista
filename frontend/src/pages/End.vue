<template>
  <div class="end-container">
    <div class="end-container-header">
      <Header />
    </div>
    <div class="end-container-content">
      <h1 class="end-container-content-title">
        Congratulations <img :src="Confetti" />
      </h1>
      <h2 class="end-container-content-more">
        You contributed in the mission of delivering more sustainable tourism
        for everyone!
      </h2>
      <div class="end-container-content-description">
        <div class="end-container-content-description-pair">
          <div><img src="../assets/clock.png" /></div>
          <div>You saved 1 hour and 38 minutes of waiting in queues<br /></div>
        </div>
        <div class="end-container-content-description-pair">
          <div><img src="../assets/crowd.png" /></div>
          <div>You helped reducing queues in Athens by 2%<br /></div>
        </div>
        <div class="end-container-content-description-pair">
          <div><img src="../assets/route.png" /></div>
          <div>You visited 8 out of 10 suggested places<br /></div>
        </div>
        <div class="end-container-content-description-pair">
          <div><img src="../assets/souvenir.png" /></div>
          <div>
            You won free participation in our mothly giveaway of free airplane tickets for two to anywhere
            <br />
          </div>
        </div>
      </div>
      <div class="end-container-content-gotorate" @click="router.push('/rating')">
        Rate us
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Header from "../components/Header.vue";
import Confetti from "../assets/icons/confetti.svg";
import Clock from "../assets/icons/clock.svg";
import { useRouter, useRoute } from "vue-router";
const router = useRouter();
</script>

<style scoped lang="scss">
.end-container {
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
    padding-top: 5%;
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
      margin-bottom: 5%;
      font-style: italic;
      font-weight: 700;
    }

    &-more {
      width: 85%;
      font-size: 1.3em;
      font-weight: 600;
      margin: 3% auto;
    }

    &-description {
      width: 90%;
      margin: 5% auto;
      font-size: 1.1em;
      display: flex;
      flex-direction: column;

      &-pair {
        display: flex;
        align-items: center;
        margin: 3%;

        img {
          width: 30px;
        }

        div:nth-child(2) {
          margin-left: 4%;
        }
      }
    }

    &-gotorate {
      width: 30%;
      height: 30px;
      color: white;
      font-size: 16px;
      font-weight: 600;
      background: #ff8811;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 12px;
    }
  }

  @media (min-width: 1024px) {
    .end-container {
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
        padding-top: 5%;
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
          margin-bottom: 5%;
          font-style: italic;
          font-weight: 700;
        }

        &-more {
          width: 85%;
          font-size: 30px;
          font-weight: 600;
          margin: 1% auto;
        }

        &-description {
          width: 90%;
          margin: 0 auto;
          font-size: 30px;

          display: flex;
          flex-direction: column;

          &-pair {
            display: flex;
            align-items: center;
            margin: 2.5%;

            img {
              width: 30px;
            }

            div:nth-child(2) {
              margin-left: 4%;
            }
          }
        }

        &-gotorate {
          width: 30%;
          height: 60px;
          color: white;
          font-size: 16px;
          font-weight: 600;
          background: #ff8811;
          display: flex;
          justify-content: center;
          align-items: center;
          border-radius: 12px;
        }
      }
    }
  }
}
</style>
