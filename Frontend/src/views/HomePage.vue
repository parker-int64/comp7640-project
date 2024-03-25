<script setup>
import ItemCarousel from '../components/ItemCarousel.vue'
import ItemCard from '../components/ItemCard.vue'
import { NLayout, NGrid, NGi, NFlex, NDivider, NH1, NIcon, NButton, NDropdown, NSpin } from 'naive-ui'
import { FilterOutline } from '@vicons/ionicons5'
import { onMounted, ref } from 'vue'
import { RouterLink } from 'vue-router'
import Spinner from '../components/Spinner.vue'
import { useItemDataStore } from '../stores/itemData'
import { storeToRefs } from 'pinia'
 
// our image assets
// using webpack, dynamically import the webp images

const dropOptions = [
    {
        label: "All",
        key: 'all'
    },
    {
        label: "Vendor",
        key: 'vendor'
    }
]

const handleSelect = (key) => {
    console.log("Key", key);
}


// use the store items
const itemStore = useItemDataStore()


// by default, you shall see a circle running in home page.
// once we connected to the database, we shall present all the contents.
const items = ref(null)
const itemLoading = ref(true) // by default, loading spin...

// retrieve data from database
itemStore.getItemData().then(() => {

    if(itemStore.itemData) {
        items.value = itemStore.itemData
        itemLoading.value = false
    }

})

// find our image's path
const getItemImgUrl = (id) => {
    return new URL(`../assets/products/product_${id}.webp`, import.meta.url).href
}

const getBannerImgUrls = () => {
    const ids = [ 2004, 2003 , 2007, 2023]

    let urls = []

    for(const id of ids){
        let url = new URL(`../assets/banners/banner_${id}.webp`, import.meta.url).href
        urls.push(url)
    }

    return urls
}



</script>


<template>
    <n-layout v-if="!itemLoading" content-style="padding: 24px;">
        <n-h1>Home Page</n-h1>
        <n-flex justify="center" align="center">
            <ItemCarousel :img-urls="getBannerImgUrls()" style="padding-bottom: 10px; max-width: 75vw;"  />
        </n-flex>

        <n-divider />

        <n-flex justify="space-between" align="center">
            <n-h1>Recommend for You</n-h1>
            <n-dropdown trigger="hover" :options="dropOptions" @select="handleSelect">
                <n-button text>
                    <template #icon>
                        <n-icon :component="FilterOutline" />
                    </template>
                    Filter
                </n-button>
            </n-dropdown>
        </n-flex>

        
        
        <n-grid :x-gap="12" :y-gap="8" cols="2 s:3 m:4 l:4 xl:5 2xl:6" responsive="screen">
            <n-gi v-for="(item, index) in items">
                <router-link :to="{ name: 'product', params: { id: `${item[0]}`, imgUrl: getItemImgUrl(item[0]) }}" >
                    <ItemCard 
                        v-bind:item-price="`¥ ${item[2]}`" 
                        v-bind:item-name="item[1]" 
                        v-bind:item-img-src="getItemImgUrl(item[0])"
                    />
                </router-link>
            </n-gi>
        </n-grid>
        
    </n-layout>


    <Spinner v-if="itemLoading" />

</template>


<style scoped>

</style>
