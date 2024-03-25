import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

// Shared variable item data
export const useItemDataStore = defineStore('customerData', () => {

    // Store the customerData
    const customerData = ref(null)

    // Store the response state
    const resValue = ref(null)

    const getcustomerData = async() => {
        // use axio to request our data
        await axios({
            method: 'post',
            url: "/getVendor",
            headers: {
                'Content-Type': 'application/json',
            }
        }).then((res) => {
            if(res.data){
                customerData.value = res.data
            }
        }).catch((e) => {
            resValue.value = e
            console.log(`Error Response: \n ${e}`,)
        })
    }


    const addCustomer = async (data) => {
        // use axio to request our data
        await axios({
            method: 'post',
            url: "/addCustomer",
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


    return { customerData, getcustomerData, addCustomer, resValue }

})

