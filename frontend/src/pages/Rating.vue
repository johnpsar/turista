<template>
  <div class="rating-container">
    <div class="rating-container-header">
      <Header />
    </div>
    <div class="rating-container-content">
      <h1 class="rating-container-content-title">
        Thank you for sightseeing with us!
      </h1>

      <div class="rating-container-content-rate card">
        <div class="row justify-content-center">
          <div class="col-10">
            <div class="comment-box ml-2">
              <h2>Help us become better!</h2>
              <div class="stars">
                <input type="radio" name="rating" value="5" id="5" /><label for="5">☆</label>
                <input type="radio" name="rating" value="4" id="4" /><label for="4">☆</label>
                <input type="radio" name="rating" value="3" id="3" /><label for="3">☆</label>
                <input type="radio" name="rating" value="2" id="2" /><label for="2">☆</label>
                <input type="radio" name="rating" value="1" id="1" /><label for="1">☆</label>
              </div>
              <div class="comment-area">
                <textarea class="form-control" placeholder="Tell us your opinion ..." rows="5"></textarea>
              </div>
              <div id="submit-btn">Submit</div>
            </div>
          </div>
        </div>
      </div>
      <div class="rating-container-content-restart" @click="router.push('/home')">
        Create another path
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Header from "../components/Header.vue";
import { useRouter, useRoute } from "vue-router";

const isVisible = ref(true);
const place = ref("");
const router = useRouter();
</script>

<style scoped lang="scss">
.rating-container {
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
      font-size: 2em;
      margin-bottom: 10%;
      font-style: italic;
      font-weight: 700;
    }

    &-rate {
      position: relative;
      display: flex;
      flex-direction: column;
      min-width: 0;
      padding: 15px;
      width: 80%;
      word-wrap: break-word;
      background-color: #fff;
      background-clip: border-box;
      border-radius: 6px;
      margin-bottom: 5%;

      .comment-box {
        padding: 5px;
        text-align: center;
      }

      h2 {
        font-size: 1.2em;
      }

      .comment-area textarea {
        resize: none;
        border: 1px solid #ad9f9f;
      }

      .form-control:focus {
        color: #495057;
        background-color: #fff;
        border-color: #ffffff;
        outline: 0;
      }

      #submit-btn {
        width: 30%;
        height: 30px;
        color: white;
        font-size: 0.9em;
        font-weight: 600;
        background: #ff8811;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 12px;
        margin-top: 4%;
      }

      .stars {
        display: flex;
        margin-top: -10px;
        flex-direction: row-reverse;
        margin-left: -4px;
        justify-content: center;
      }

      .stars>input {
        display: none;
      }

      .stars>label {
        position: relative;
        width: 19px;
        font-size: 25px;
        color: #ff8811;
        cursor: pointer;
      }

      .stars>label::before {
        content: "\2605";
        position: absolute;
        opacity: 0;
      }

      .stars>label:hover:before,
      .stars>label:hover~label:before {
        opacity: 1 !important;
      }

      .stars>input:checked~label:before {
        opacity: 1;
      }

      .stars:hover>input:checked~label:before {
        opacity: 0.4;
      }
    }

    &-restart {
      width: 50%;
      height: 40px;
      color: white;
      font-size: 15px;
      font-weight: 600;
      background: #ff8811;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 12px;
      margin-top: 8%;
    }
  }

  @media (min-width: 1024px) {
    .rating-container {
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
          margin-bottom: 4%;
          font-style: italic;
          font-weight: 700;
        }

        &-rate {
          position: relative;
          display: flex;
          flex-direction: column;
          min-width: 0;
          padding: 15px;
          width: 80%;
          word-wrap: break-word;
          background-color: #fff;
          background-clip: border-box;
          border-radius: 6px;
          margin-bottom: 5%;
          font-size: 30px;
        }
      }
    }

    .comment-area textarea {
      resize: none;
      height: 200px;
      font-size: 24px;
    }

    #submit-btn {
      height: 60px;
    }

    .rating-container-content-restart {
      height: 60px;
      font-size: 32px;
    }
  }
}
</style>
