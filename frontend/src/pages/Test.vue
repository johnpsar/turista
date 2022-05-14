<template>

<div class="content">
        <button  @click="onClick" class="btn-primary btn"> Change</button>
</div>
<div class="pretty">

   {{countries}}
</div>
</template>


<script setup lang="ts">
import Header from "../components/Header.vue"
import { useRouter, useRoute } from 'vue-router'
import { onMounted, ref } from "vue";
import axios from 'axios';
import Sidebar from "primevue/sidebar";
const isVisible = ref(true);

const router=useRouter()

const props=defineProps<{
    zoneId:string
}>()
function onClick(){
    alert('gia');
    router.push('/home')
}
const countries=ref<any>()

onMounted(async () => {
  try{
      const response=await axios.get('http://127.0.0.1:8000/test/getall')
      countries.value=response.data
  }catch(e){
      console.log(e)
  }
})

</script>

<style scoped >
.pretty{
    font-size: 40px;
    color:hotpink;
}
</style>