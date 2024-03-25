import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

// Shared variable item data
export const useItemDataStore = defineStore('itemData', () => {

    const itemData = ref(null)

    const getItemData = async() => {
        if(itemData.value === null){
            // use axio to request our data
            await axios({
                method: 'post',
                url: "/getProducts",
                headers: {
                    'Content-Type': 'application/json',
                }
            }).then((res) => {
                if(res.data){
                    itemData.value = res.data // well, I think we should be careful
                    // console.log(`Received from database:`)
                    // console.log(itemData.value);
                }
            }).catch((e) => {
                console.log(`Error Response: \n ${e}`,)
            })
        }
    }

    return { itemData, getItemData }
})



