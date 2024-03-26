import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchContents } from '../requests/fetch'

// Shared variable item data
export const useItemDataStore = defineStore('itemData', () => {

    const itemData = ref(null) // All the data

    const searchItemData = ref(null)   // The search result

    const getItemData = async() => {
        if(itemData.value === null){
            let res = await fetchContents("/getProducts")
            if ( res ) {
                itemData.value = res
            }
        }
    }


    const getSearchItemResult = async (body) => {
        let res = await fetchContents("/getProducts", body)
        if ( res ) {
            searchItemData.value = res
        }
    }


    const addItemStatus = ref(null)

    const addItem = async (body) => {
        let res = await fetchContents("/addProduct", body)

        if ( res ){
            addItemStatus.value = res
        }
    }



    return { itemData, getItemData, searchItemData, getSearchItemResult, addItemStatus, addItem }
})



