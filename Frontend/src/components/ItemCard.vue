<script setup>
  import { ref } from 'vue';
  import { NCard, NImage, NDivider } from 'naive-ui'

  const props = defineProps({
    itemImgSrc: {
      type: String,
      default: "https://placehold.co/400.svg"   // act like a fallback, since there's something wrong with the `fallback-src` in `n-image`
    },
    itemName: {
        type: String,
        default: "Item Placeholder"
    },
    itemPrice: {
        type: String,
        default: "$ 0"
    }
  })


  const showLoadingError = () => {
      console.log(e)
  }

  const onLoading = () => {

  }


  const redirectToItemPage = (itemId) => {
    console.log("Redirecting")
  }
</script>


<template>
    <n-card :title="itemName" @click="redirectToItemPage" hoverable embedded>
    <template #cover>
      <n-image
        :src="itemImgSrc"
        preview-disabled
        @on-error="showLoadingError"
        @on-load="onLoading"
      />
    </template>
    {{ itemPrice }}
  </n-card>
</template>



<style scoped>

</style>