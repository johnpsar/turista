<template>
  <div>
    <div class="sidebar">
      <Sidebar v-model:visible="isNavBarVisible" position="right" class="sidebar-sidebar">
        <div v-if="isSignInClicked === false" class="sidebar-choice">
          <img :src="Google" />
          <button type="button" data-bs-toggle="modal" data-bs-target="#signin-modal" @click="isNavBarVisible = false">
            Sign in
          </button>
        </div>
        <div v-if="isSignInClicked === true" class="sidebar-choice">
          <img :src="MyAccount" />My Account
        </div>
        <div class="sidebar-choice">
          <img :src="Communication" />
          <button type="button" data-bs-toggle="modal" data-bs-target="#communication-modal"
            @click="isNavBarVisible = false">
            Communication
          </button>
        </div>
        <div class="sidebar-choice">
          <img src="../assets/way.png" style="width: 30px" />
          <button @click="router.push('/route')">My route</button>
        </div>
        <div class="sidebar-choice">
          <img src="../assets/store.png" style="width: 30px" />
          <button @click="router.push('/break')">Local Bussinesses</button>
        </div>
        <div class="sidebar-choice"><img :src="Settings" />Settings</div>
        <div v-if="isSignInClicked === true" class="sidebar-choice">
          <img :src="SignOut" />
          <button type="button" @click="
  isNavBarVisible = false;
isSignInClicked = false;
          ">
            Sign out
          </button>
        </div>
      </Sidebar>
    </div>
    <div class="header-container">
      <div class="header-container-image" @click="router.push('/home')">
        <img src="../assets/turistaLogoWhite.png" />
      </div>
      <div class="header-container-navigation">
        <div class="header-container-navigation-icon pi pi-align-justify" style="color: white"
          @click="isNavBarVisible = true" />
      </div>
    </div>

    <!-- Communication Modal -->
    <div class="modal fade" id="communication-modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
      aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title" id="staticBackdropLabel">
              Do you need help <img :src="Help" />
            </h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h2>
              Tell us your problem and we'll communicate with you as soon as
              possible
            </h2>
            <form>
              <div class="form-group">
                <div class="row justify-content-center">
                  <div class="col">
                    <label for="first-name">First name</label>
                    <input id="first-name" type="text" class="form-control" placeholder="Alex" />
                  </div>
                  <div class="col">
                    <label for="last-name">Last name</label>
                    <input id="last-name" type="text" class="form-control" placeholder="Richardson" />
                  </div>
                </div>
                <div class="row email justify-content-center">
                  <label for="email">Email</label>
                  <input id="email" type="email" class="form-control" placeholder="email@example.com" />
                </div>
                <div class="row txt justify-content-center">
                  <textarea class="form-control" id="com-textarea" rows="4"
                    placeholder="Write your problem here ..."></textarea>
                </div>
                <div class="row justify-content-center">
                  <div id="send-btn">Send</div>
                </div>
              </div>
            </form>
            <div class="row justify-content-center">
              <p class="media"><img :src="Phone" /> 210 0000000</p>
              <p class="media"><img :src="Email" /> info@turista.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Sign in Modal -->
    <div class="modal fade" id="signin-modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
      aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title" id="staticBackdropLabel">
              Sign in <img :src="Google" />
            </h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h2>
              Sign in with your google account to benefit from our rewards
              program!
              <img :src="Gift" />
            </h2>
            <div class="google-login">
              <button @click="isSignInClicked = true" type="button" class="login-with-google-btn"
                data-bs-dismiss="modal">
                Sign in with Google
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Sidebar from "primevue/sidebar";
import { useRouter } from "vue-router";
import MyAccount from "../assets/icons/myaccount.svg";
import Communication from "../assets/icons/communication.svg";
import Settings from "../assets/icons/settings.svg";
import SignOut from "../assets/icons/logout.svg";
import Phone from "../assets/icons/phone-call.svg";
import Email from "../assets/icons/mail.svg";
import Help from "../assets/icons/help.svg";
import Google from "../assets/icons/google.svg";
import Gift from "../assets/icons/gift.svg";
import GoogleSignIn from "../assets/icons/google-signin.svg";

const isSignInClicked = false;

const router = useRouter();
const isNavBarVisible = ref(false);
const isVisible = ref(false);
</script>

<style scoped lang="scss">
.header-container {
  font-family: "Montserrat Alternates", sans-serif;
  width: 100%;
  height: 10vh;
  align-items: center;
  background: #06bcc1;
  display: flex;
  justify-content: space-between;
  overflow: hidden;

  &-image {
    // width: 35%;
    height: 100%;
    display: flex;
    justify-content: flex-start;
    align-items: center;

    img {
      width: 100%;
      height: auto;
      max-height: 100%;
      object-fit: contain;
    }
  }

  &-navigation {
    width: 10%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    &-button {
      width: 60px;
      height: 44px;
    }
  }
}

.pi-align-justify {
  font-size: 24px;
}

.sidebar-choice {
  font-family: "Montserrat Alternates", sans-serif;
  font-size: 1.5em;
  margin-bottom: 5%;
  color: black;

  img {
    margin-right: 10px;
  }
}

.modal-title {
  font-size: 1.5em;

  img {
    width: 24px;
  }
}

.modal h2 {
  font-size: 1em;
  margin: 0 8%;
  margin-bottom: 3%;
}

textarea {
  margin: 5% 0 !important;
}

#send-btn {
  width: 20%;
  height: 30px;
  color: white;
  font-size: 1em;
  font-weight: 600;
  background: #ff8811;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 12px;
  margin: auto;
  margin-bottom: 5%;
}

.media {
  text-align: center;
}

.row {
  width: 90% !important;
  margin: auto !important;
}

.email,
.txt {
  padding: 0 10px !important;
}

.login-with-google-btn {
  transition: background-color 0.3s, box-shadow 0.3s;

  padding: 12px 16px 12px 42px;
  border: none;
  border-radius: 3px;
  box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 1px 1px rgba(0, 0, 0, 0.25);

  color: #757575;
  font-size: 14px;
  font-weight: 500;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;

  background-image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJNMTcuNiA5LjJsLS4xLTEuOEg5djMuNGg0LjhDMTMuNiAxMiAxMyAxMyAxMiAxMy42djIuMmgzYTguOCA4LjggMCAwIDAgMi42LTYuNnoiIGZpbGw9IiM0Mjg1RjQiIGZpbGwtcnVsZT0ibm9uemVybyIvPjxwYXRoIGQ9Ik05IDE4YzIuNCAwIDQuNS0uOCA2LTIuMmwtMy0yLjJhNS40IDUuNCAwIDAgMS04LTIuOUgxVjEzYTkgOSAwIDAgMCA4IDV6IiBmaWxsPSIjMzRBODUzIiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNNCAxMC43YTUuNCA1LjQgMCAwIDEgMC0zLjRWNUgxYTkgOSAwIDAgMCAwIDhsMy0yLjN6IiBmaWxsPSIjRkJCQzA1IiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNOSAzLjZjMS4zIDAgMi41LjQgMy40IDEuM0wxNSAyLjNBOSA5IDAgMCAwIDEgNWwzIDIuNGE1LjQgNS40IDAgMCAxIDUtMy43eiIgZmlsbD0iI0VBNDMzNSIgZmlsbC1ydWxlPSJub256ZXJvIi8+PHBhdGggZD0iTTAgMGgxOHYxOEgweiIvPjwvZz48L3N2Zz4=);
  background-color: white;
  background-repeat: no-repeat;
  background-position: 12px 14px;

  &:hover {
    box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 2px 4px rgba(0, 0, 0, 0.25);
  }

  &:active {
    background-color: #eeeeee;
  }

  &:focus {
    outline: none;
    box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 2px 4px rgba(0, 0, 0, 0.25),
      0 0 0 3px #c8dafc;
  }
}

.google-login {
  display: flex;
  justify-content: center;
}

@media (min-width: 1024px) {
  .pi-align-justify {
    font-size: 40px;
  }

  .sidebar-choice {
    font-size: 34px;
  }

  .sidebar-sidebar {
    width: 500px;

    ::v-model(.p-sidebar-right) {
      width: 800px;
    }
  }
}
</style>

<style>
@media (min-width: 1024px) {
  .p-sidebar-right {
    width: 20%;
  }
}
</style>
