<script setup>
import Spinner from '../components/Spinner.vue'
import { NLayout, NFlex, NGi, NGrid, NCard, NH1, NH2, NP, 
        NImage, NButton, NRate, NModalProvider, NModal, useModal, NTag } from 'naive-ui'

import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useItemDataStore } from '../stores/itemData';



const itemStore = useItemDataStore()

const userLogin = ref(false)

const itemLoading = ref(true) // loading something by default...

const route = useRoute();
const router = useRouter()

const imgSrc = ref("https://placehold.co/400.svg")

// some info around the data
const itemInfo = ref({
    itemId: null,
    itemName: null,
    itemPrice: 0,
    itemTags: [],
    vendorId: null,
    itemVendor: null,
    vendorFeedback: null
})

// clear enough, huh?
// well, I don't know
// Yet gpt told me it should work...
const findItemArrById = (data, id) => {

    let item = []
    const search = data.forEach(element => {
        if(element[0] === parseInt(id)){
            item = element
        }
    });
    return item ? item : null
}

const modal = useModal()

const onPositiveClick = () => {
    router.push('/login')

}


// handle the order button
const handleOrder = () => {
    const modalInst = modal.create({
        title: 'Sign in required',
        content: 'Sign in to continue.',
        preset: 'dialog',
        maskClosable: false,
        positiveText: 'Sign in',
        onPositiveClick: onPositiveClick
    })
}

// find our image's path
const getItemImgUrl = (id) => {
    return new URL(`../assets/products/product_${id}.webp`, import.meta.url).href
}



itemStore.getItemData().then(() => {
    if(itemStore.itemData) {
        const singleItem = findItemArrById(itemStore.itemData, route.params.id)
        console.log(singleItem)
        itemInfo.value = {
            itemId: singleItem[0],
            itemName: singleItem[1],
            itemPrice: singleItem[2],
            itemTags: [singleItem[3], singleItem[4], singleItem[5]],
            vendorId: singleItem[6],
            itemVendor: singleItem[7],
            vendorFeedback: singleItem[8]
        }

        itemLoading.value = false
    }
})


</script>



<template>
    
    <n-layout v-if="!itemLoading" style="height: 100%;">
        <n-flex>
            <n-grid x-gap="12" y-gap="12" cols="1 s:1 m:2 x:2 xl:2" item-responsive responsive="screen">
                <n-gi span="1 s:1 m:1">
                    <n-flex justify="center" align="center">
                        <n-image
                            :src="getItemImgUrl(route.params.id)"
                            @on-error="showLoadingError"
                            @on-load="onLoading"
                            width="400"
                            height="400"
                            object-fit="fill"
                        />
                    </n-flex>
                </n-gi>

                <n-gi>
                    <n-flex justify="center" align="start" style="margin-bottom: 30px;">

                        <n-card>
                            <n-flex justify="center" align="start" vertical>
        
                                <n-h1>{{ itemInfo.itemName }}</n-h1>
        
                                <n-h2>{{ `Price ¥ ${itemInfo.itemPrice}`  }}</n-h2>
        
                                <n-p>{{ `Product ID: ${itemInfo.itemId}`}}</n-p>
        
                                <n-flex align="center" align="center"> 
                                    <n-p>{{ `Tag ` }}</n-p>
                                    <n-tag v-for="(itemTag, index) in itemInfo.itemTags">{{ itemTag }}</n-tag>  
                                </n-flex>
                                <n-p>{{ `Vendor: ${itemInfo.itemVendor} (Vendor ID: ${itemInfo.vendorId})` }}</n-p>
                                <n-p>{{ `Vendor Rating: ${itemInfo.vendorFeedback}` }}</n-p>
                                <n-rate allow-half :value="parseFloat(itemInfo.vendorFeedback)" readonly />
                                <n-modal-provider>
                                    <n-button  style="margin-top: 20px;" @click="handleOrder">Order Now!</n-button>
                                </n-modal-provider>
                            </n-flex>
                        </n-card>
                    </n-flex>
                </n-gi>
            </n-grid>
        </n-flex>
        
    </n-layout>
    <Spinner v-if="itemLoading" />
</template>