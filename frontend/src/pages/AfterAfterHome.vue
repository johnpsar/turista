<template>
  <div class="afterafterhome-container">
    <div class="afterafterhome-container-header">
      <Header />
    </div>
    <div class="afterafterhome-container-content">
      <h1 class="afterafterhome-container-content-title">
        Tell us the date of your tour ...
      </h1>
      <div class="afterafterhome-container-content-pair">
        <div class="afterafterhome-container-content-pair-input">
          <Calendar v-model="date" dateFormat="m/d/yy" :showIcon="true" :showButtonBar="true" :minDate="minDate" />
        </div>
        <div class="afterafterhome-container-content-pair-go" @click="router.push('/recommendations')">
          Go
        </div>
      </div>
      <div class="afterafterhome-container-content-image">
        <img src="../assets/trip_date.png" alt="calendar" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from "vue";
import Header from "../components/Header.vue";
import { useRouter, useRoute } from "vue-router";
import Calendar from "primevue/calendar";
const emit = defineEmits<{
  (e: "updateDate", v: string): void;
}>();
const date = ref();
const minDate = ref(new Date()); //minDate is today
const place = ref("");
const router = useRouter();
const dateObj = computed(() => translateDate(new Date(date.value)));


watch(dateObj, () => emit("updateDate", dateObj.value));

function translateDate(date: Date): string {
  let dd = date.getDate();
  let mm = date.getMonth() + 1; //January is 0 so need to add 1 to make it 1
  let yyyy = date.getFullYear();


  let transDate = mm + '/' + dd + '/' + yyyy;

  return transDate
}
</script>

<style scoped lang="scss">
.afterafterhome-container {
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
      margin: 13% auto;

      img {
        width: 185px;
      }
    }
  }
}

::v-deep(.p-inputtext) {
  border-radius: 12px;
}

::v-deep(.p-inputtext-focus) {
  border: none;
}

::v-deep(.p-button) {
  background-color: #ff8811;
  border: none;
  border-radius: 8px;
  margin-left: 4%;
  transition: none;
}

::v-deep(.p-button-text) {
  background-color: #ff8811;
}

::v-deep(.p-button:enabled:hover) {
  background-color: #ff8811;
  border: none;
}


@media (min-width: 1024px) {
  .afterafterhome-container {
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
        font-size: 32px;
        margin-bottom: 10%;
        font-style: italic;
        font-weight: 700;
      }

      &-pair {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 30%;
        min-width: 600px;

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
          height: 60px;
          color: white;
          font-size: 30px;
          font-weight: 600;
          background: #ff8811;
          display: flex;
          justify-content: center;
          align-items: center;
          border-radius: 12px;
        }
      }

      &-image {
        margin: 4% auto;

        img {
          width: 300px;
        }
      }
    }
  }

  ::v-deep(.p-inputtext) {
    width: 400px;
    height: 44px;
    border-radius: 12px;
  }

  ::v-deep(.p-inputtext-focus) {
    border: none;
  }

  ::v-deep(.p-button) {
    background-color: #ff8811;
    border: none;
    width: 40px;
    margin-left: 12px;
    border-radius: 8px;
  }
}
</style>
