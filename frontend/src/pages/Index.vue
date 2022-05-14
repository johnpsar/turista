<template>
  <div class="index-container">
    <div class="index-container-header">
      <div class="index-container-header-logo">
        <img src="../assets/turistaLogoGradient.png" />
      </div>
    </div>
    <div class="index-container-content">
      <h1 class="index-container-content-title">
        We find the best path for you, based on<br />
        <div>
          <img src="../assets/weather.png" alt="" /> weather conditions,<br />
          <img src="../assets/people.png" alt="" /> crowd situation,<br />
          and above all <br />
          <img src="../assets/preferences.png" alt="" /> your preferences
        </div>
      </h1>
      <div class="index-container-content-start" @click="router.push('/home')">
        Get Started
      </div>

      <!-- Button trigger modal -->
      <button ref="mybutton" type="button" id="invisible-btn" class="btn btn-primary" data-bs-toggle="modal"
        data-bs-target="#indexModal">
        Launch demo modal
      </button>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="indexModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
      aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h2 class="modal-title" id="exampleModalLabel">
              We are so glad you are here <img :src="Heart" />
            </h2>
          </div>
          <div class="modal-body">
            Before you begin planning your trip, we request access to your
            device's current location <img :src="Location" />. Don't worry,
            location data are only used to verify your position for our reward
            system as well as crowd management and no data will be saved!
          </div>
          <div class="modal-footer justify-content-center">
            <button type="button" class="btn btn-success" data-bs-dismiss="modal">
              Allow access
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import Location from "../assets/icons/current-location.svg";
import Heart from "../assets/icons/heart.svg";

const isVisible = ref(true);
const place = ref("");
const router = useRouter();
const mybutton = ref<any>();
onMounted(() => {
  mybutton.value.click();
});
</script>

<style scoped lang="scss">
.index-container {
  font-family: "Montserrat Alternates", sans-serif;
  width: 100%;
  height: 100%;

  &-header {
    height: 20%;
    width: 100%;

    &-logo {
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;

      img {
        width: 90%;
        height: auto;
        max-height: 100%;
        object-fit: contain;
        margin-top: 7%;
      }
    }
  }

  &-content {
    width: 100%;
    height: 90%;
    padding-top: 15%;
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
      font-size: 1.8em;
      margin-bottom: 15%;
      margin-top: 3%;
      font-style: italic;
      font-weight: 700;
      display: block;
      line-height: 1.7;

      img {
        width: 32px;
      }
    }

    &-start {
      width: 40%;
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

.modal-body {
  font-size: 1.1em;
}

.modal h2 {
  font-size: 1.3em;
}

#invisible-btn {
  display: none;
}

@media (min-width: 1024px) {
  .index-container {
    font-family: "Montserrat Alternates", sans-serif;
    width: 100%;
    height: 100%;

    &-header {
      height: 20%;
      width: 100%;

      &-logo {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;

        img {
          width: 90%;
          height: auto;
          max-height: 100%;
          object-fit: contain;
        }
      }
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
        width: auto;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
        font-size: 32px;
        margin-bottom: 15%;
        font-style: italic;
        font-weight: 700;
        display: block;
        line-height: 1.7;

        img {
          width: 32px;
        }
      }

      &-start {
        width: 40%;
        height: 60px;
        color: white;
        font-size: 32px;
        font-weight: 600;
        background: #ff8811;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 12px;
      }
    }
  }

  .btn-success {
    width: 40%;
    font-size: 20px;
    font-weight: 600;
  }

  .modal-body {
    font-size: 24px;
  }

  .modal h2 {
    font-size: 30px;
  }

  #invisible-btn {
    display: none;
  }

  .modal-dialog {}

}
</style>
