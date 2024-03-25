import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchContents } from '../requests/fetch'

// Shared variable item data
export const useItemDataStore = defineStore('itemData', () => {

    const itemData = ref(null)

    const getItemData = async() => {
        if(itemData.value === null){
            let res = await fetchContents("/getProducts")
            if ( res ) {
                itemData.value = res
            }
        }
    }

    return { itemData, getItemData }
})



