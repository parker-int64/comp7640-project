<script setup>
import Spinner from '../components/Spinner.vue'
import { NLayout, NFlex, NGi, NGrid, NCard, NH1, NH2, NP, 
        NImage, NButton, NRate, NModalProvider, NModal, useModal, NTag, NSelect, useDialog } from 'naive-ui'

import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useItemDataStore } from '../stores/itemData';
import { useCustomerDataStore } from '../stores/customerData'
import { useTransDataStore } from '../stores/transData'

const itemStore = useItemDataStore()
const customerStore = useCustomerDataStore()
const transData = useTransDataStore()
const itemLoading = ref(true) // loading something by default...

const route = useRoute();
const router = useRouter()
const modal = useModal()

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

    let retItem = []

    data.forEach(element => {
        if ( element['product_ID'] === parseInt(id) ) {
            retItem = element
        } 
    })
    
    return retItem ? retItem : null
}



// show submit modal
const showSelectModal = ref(false)

const selectValue = ref(null)

const selectOptions = ref([])

// handle the order button
const handleOrder = () => {
    showSelectModal.value = true

    let retSelectOps = []

    customerStore.getCustomerData().then(() => {
        if ( customerStore.customerData ) {
            for(const value of Object.values(customerStore.customerData)) {
                retSelectOps.push({
                    label: `User: ${value['contact_number']} with ID ${value['customer_ID']}`,
                    value: `${value['customer_ID']}`
                })
            }
        }

        selectOptions.value = retSelectOps
    })


}

const dialog = useDialog()
const submitOrder = () => {


    if(selectValue.value === null) {
        dialog.error({
            title: "Error",
            content: "You must select a user...",
            positiveText: 'Dismiss',
        })
    }
    else {
        // add transaction
        let body = {
            productId: itemInfo.value.itemId, 
            amount: itemInfo.value.itemPrice, 
            customerId: parseInt(selectValue.value)
        }

        transData.addTrans(body).then(() => {

            if(transData.addTransStatus.message === 'ok') {
                dialog.success({
                    title: "Success",
                    content: "A new transaction has been added!",
                    positiveText: 'Acknowledged',
                })
            } else {
                dialog.error({
                    title: "Message",
                    content: "Database process failed...",
                    positiveText: 'Dismiss',
                })
            }
        })
    }



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
            itemId: singleItem['product_ID'],
            itemName: singleItem['product_name'],
            itemPrice: singleItem['price'],
            itemTags: [singleItem['Tag1'], singleItem['Tag2'], singleItem['Tag3']],
            vendorId: singleItem['vendor_ID'],
            itemVendor: singleItem['business_name'],
            vendorFeedback: singleItem['customer_feedback_score']
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
        
                                <n-flex align="center" justify="center"> 
                                    <n-p style="margin: 0;">{{ `Tag ` }}</n-p>
                                    <n-tag v-for="(itemTag, index) in itemInfo.itemTags">{{ itemTag }}</n-tag>  
                                </n-flex>
                                <n-p>{{ `Vendor: ${itemInfo.itemVendor} (Vendor ID: ${itemInfo.vendorId})` }}</n-p>
                                <n-p>{{ `Vendor Rating: ${itemInfo.vendorFeedback}` }}</n-p>
                                <n-rate allow-half :value="parseFloat(itemInfo.vendorFeedback)" readonly />

                                <n-modal 
                                    v-model:show="showSelectModal" 
                                    :mask-closable="false" 
                                    preset="dialog" 
                                    positive-text="Confirm"
                                    @positive-click="submitOrder"
                                    title="User required"
                                >
                                    <n-flex justify="center" align="start" vertical>
                                        <n-p>You need to select a user</n-p>
                                        <n-select v-model:value="selectValue" :options="selectOptions" />
                                    </n-flex>
                                </n-modal>
                                <n-button  style="margin-top: 20px;" @click="handleOrder">Order Now!</n-button>
                            </n-flex>
                        </n-card>
                    </n-flex>
                </n-gi>
            </n-grid>
        </n-flex>
        
    </n-layout>
    <Spinner v-if="itemLoading" />
</template>