<template>
  <div class="home-container">
    <div class="home-container-header">
      <Header />
    </div>
    <div class="home-container-content">
      <h1 class="home-container-content-title">
        Tell us where you're going ...
      </h1>
      <div class="home-container-content-pair">
        <div class="home-container-content-pair-input">
          <input
            list="places"
            placeholder="Trip destination (e.g. Rome)"
            v-model="place"
          />
          <datalist id="places">
            <option value="Athens"></option>
            <option value="Paris"></option>
            <option value="Rome"></option>
            
          </datalist>
        </div>
        <div
          class="home-container-content-pair-go"
          @click="router.push('/afterhome')"
        >
          Go
        </div>
      </div>
      <div class="earth">
        <Earth />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import Header from "../components/Header.vue";
import Earth from "../components/Earth.vue";
import { useRouter, useRoute } from "vue-router";

const emit = defineEmits<{
  (e: "updatePlace", v: string): void;
}>();
const isVisible = ref(true);
const place = ref("");
const router = useRouter();
watch(place, () => emit("updatePlace", place.value));
</script>

<style scoped lang="scss">
.home-container {
  font-family: "Montserrat Alternates", sans-serif;
  width: 100%;
  height: 100%;

  &-header {
    height: 10%;
    width: 100%;
  }

  &-content {
    width: 100%;
    height: 60%;
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
  }
}

@media (min-width: 1024px) {
  .earth {
    height: 300px;
    width: 300px;
    ::v-deep(.globe) {
      margin-top: 10%;
      transform: scale(2);
      left: 0;
      right: 0;
      margin-left: auto;
      margin-right: auto;
    }
  }
  .home-container {
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

      &-title {
        width: 80%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
        font-size: 40px;
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
    }
  }
}
</style>
