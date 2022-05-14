<template>
  <router-view :place="place" :date="date" :count="count" :recommendations="recommendations"
    @updatePlace="onUpdatePlace" @updateCount="onUpdateCount" @updateDate="onUpdateDate"
    @updateRecommendations="onUpdateRecommendations" />
</template>

<script setup lang="ts">
import { ref } from "vue";

const place = ref("");
const date = ref("");
const count = ref(0);
const recommendations = ref<Array<number>>([])
function onUpdatePlace(p: string) {
  place.value = p;
}
function onUpdateDate(d: string) {
  date.value = d;
}
function onUpdateCount(c: number) {
  count.value = c;
}

function onUpdateRecommendations(c: number[]) {
  recommendations.value = c;
  console.log(recommendations.value)
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jura&family=Montserrat+Alternates:ital@0;1&display=swap");

#app {
  height: 100%;
  width: 100%;
}

html,
body {
  font-size: 14px;
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  overflow: auto;
}

button {
  border: none;
  background: none;
  cursor: pointer;
  padding: 0;
  margin: 0;
  user-select: none;
  -webkit-user-select: none;
}

.p-link {
  box-shadow: none !important;
}

.p-checkbox-box {
  box-shadow: none !important;
}

.p-dropdown {
  box-shadow: none !important;
}

.p-inputtext {
  box-shadow: none !important;
  border: 1px solid black !important;
}

.p-highlight {
  background: #ff8811 !important;
  border: none;
}

.p-button-label {
  color: #ff8811;
}
</style>
