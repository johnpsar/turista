<template>
  <div class="afterhome-container">
    <div class="afterhome-container-header">
      <Header />
    </div>
    <div class="afterhome-container-content">
      <h1 class="afterhome-container-content-title">
        Tell us how many places you want to visit ...
      </h1>
      <div class="afterhome-container-content-pair">
        <div class="afterhome-container-content-pair-input">
          <input type="number" min="1" max="10" placeholder="Number of places (e.g. 5)" v-model="num" />
        </div>
        <div class="afterhome-container-content-pair-go" @click="router.push('/afterafterhome')">
          Go
        </div>
      </div>
      <div class="afterhome-container-content-image">
        <img src="../assets/acropolis.png" alt="acropolis" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import Header from "../components/Header.vue";
import { useRouter, useRoute } from "vue-router";

const emit = defineEmits<{
  (e: "updateCount", v: number): void;
}>();
const isVisible = ref(true);
const num = ref();
const router = useRouter();
watch(num, () => emit("updateCount", num.value))
</script>

<style scoped lang="scss">
.afterhome-container {
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
    padding-top: 25%;
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
      margin-bottom: 10%;
      font-style: italic;
      font-weight: 700;
    }

    &-pair {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 80%;

      &-input {
        width: 75%;

        input {
          height: 40px;
          font-size: 0.9em;
          width: 100%;
          border-radius: 12px;
          padding: 0 12px;
        }
      }

      &-go {
        width: 20%;
        height: 40px;
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

    &-image {
      margin: 10% auto;

      img {
        width: 185px;
      }
    }
  }
}

@media (min-width: 1024px) {
  .afterhome-container {
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
      padding-top: 10%;
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
        margin-bottom: 6%;
        font-style: italic;
        font-weight: 700;
      }

      &-pair {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 80%;

        &-input {
          width: 75%;

          input {
            height: 60px;
            font-size: 24px;
            width: 100%;
            border-radius: 12px;
            padding: 0 12px;
          }
        }

        &-go {
          width: 20%;
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

      &-image {
        width: 30%;
        max-width: 400px;
        height: auto;
        padding-bottom: 20px;

        img {
          width: 100%;
          height: auto;
          margin-top: -60px;
        }
      }
    }
  }
}
</style>
