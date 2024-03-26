<script setup>
import { NH1,NFlex, NLayout, NGi, NGrid, NP} from 'naive-ui'
import { onActivated, onMounted, ref, watch } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router'

import ItemCard from '../components/ItemCard.vue';

import { useItemDataStore } from '../stores/itemData';

import { storeToRefs } from 'pinia';


const route = useRoute()

const router = useRouter()

const searchValue = ref(route.params.searchParam)

const itemStore = useItemDataStore()

const { searchItemData } = storeToRefs(itemStore)

const items = ref(null)

const searchResult = ref(false) // by default, nothing will show


// find our image's path
const getItemImgUrl = (id) => {
    return new URL(`../assets/products/product_${id}.webp`, import.meta.url).href
}


const loadSeachResult = (payload) => {
    itemStore.getSearchItemResult(payload).then(() => {
        if(itemStore.searchItemData) {
            searchValue.value = route.params.searchParam
            items.value = itemStore.searchItemData
            searchResult.value = true
        }
    })
}


onMounted(() => {
    loadSeachResult({"keywords": route.params.searchParam})
})






watch(
    () => router.currentRoute.value,
    (newValue)=> {
        let newUrl = newValue.fullPath
        let newSearchParam = newValue.params.searchParam
        
        searchValue.value = newSearchParam
        
        console.log(newValue)
        console.log(newSearchParam)

        const payload = {
            "keywords": newSearchParam
        }

        loadSeachResult(payload)

})

</script>

<template>

    <n-layout>
        <n-flex style="max-width: 80vw;" align="start" vertical>
            <n-h1>{{ `Search result for ${searchValue}` }}</n-h1>
            <n-grid v-if="searchResult" :x-gap="12" :y-gap="8" cols="2 s:3 m:4 l:4 xl:5 2xl:6" responsive="screen">
                <n-gi v-for="(item, index) in items">
                    <router-link :to="{ name: 'product', params: { id: `${item['product_ID']}`, imgUrl: getItemImgUrl(item['product_ID']) }}" >
                        <ItemCard 
                            v-bind:item-price="`¥ ${item['price']}`" 
                            v-bind:item-name="item['product_name']" 
                            v-bind:item-img-src="getItemImgUrl(item['product_ID'])"
                        />
                    </router-link>
                </n-gi>
            </n-grid>
        </n-flex>
        <n-flex v-if="!searchResult" justify="center" align="center"><n-p>No match found.</n-p></n-flex>
    </n-layout>

</template>


<style scoped>

</style>