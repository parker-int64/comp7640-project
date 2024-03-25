import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

// Shared variable item data
export const useItemDataStore = defineStore('vendorData', () => {

    // Store the vendorData
    const vendorData = ref(null)

    // Store the response state
    const resValue = ref(null)

    const getVendorData = async() => {
        // use axio to request our data
        await axios({
            method: 'post',
            url: "/getVendor",
            headers: {
                'Content-Type': 'application/json',
            }
        }).then((res) => {
            if(res.data){
                vendorData.value = res.data
            }
        }).catch((e) => {
            resValue.value = e
            console.log(`Error Response: \n ${e}`,)
        })
    }


    const addVendor = async (data) => {
        // use axio to request our data
        await axios({
            method: 'post',
            url: "/addVendor",
            data: data,
            headers: {
                'Content-Type': 'application/json',
            }
        }).then((res) => {
            if(res.data){
                resValue.value = res.data
            }
        }).catch((e) => {
            console.log(`Error Response: \n ${e}`,)
        })
    }

    return { vendorData, getVendorData, addVendor, resValue }

})

