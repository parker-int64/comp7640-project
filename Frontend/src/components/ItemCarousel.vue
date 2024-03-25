<script setup>
import { NCarousel } from 'naive-ui';

import { useRouter } from 'vue-router';


const router = useRouter()

const props = defineProps({
  imgUrls: {
    type: Array,
    default: () => [],
    require: true
  },

})


const navToItem = (index) => {
  const ids = [ 2004, 2003 , 2007, 2023]
  router.push(`/item/${ids[index]}`)
} 

</script>


<template>
    <n-carousel autoplay>
        <!-- Consider using v-if to dynamically generate pictures in parent component. In the mean time, think of using the fallback src url -->
        <img
          class="carousel-img"
          v-for="(imgUrl, index) in imgUrls"
          :src="imgUrl"
          @click="navToItem(index)"
        />

      <template #dots="{ total, currentIndex, to }">
        <ul class="custom-dots">
          <li
            v-for="index of total"
            :key="index"
            :class="{ ['is-active']: currentIndex === index - 1 }"
            @click="to(index - 1)"
          />
        </ul>
      </template>
    </n-carousel>
  </template>
  
<style scoped>
  .carousel-img {
    width: 100%;
    height: 240px;
    object-fit: cover;
  }



.custom-dots {
  display: flex;
  margin: 0;
  padding: 0;
  position: absolute;
  bottom: 20px;
  left: 20px;
}

.custom-dots li {
  display: inline-block;
  width: 12px;
  height: 4px;
  margin: 0 3px;
  border-radius: 4px;
  background-color: rgba(255, 255, 255, 0.8);
  transition: width 0.3s, background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-dots li.is-active {
  width: 40px;
  background: #000000;
}
  </style>