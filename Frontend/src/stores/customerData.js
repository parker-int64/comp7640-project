import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchContents } from '../requests/fetch'


export const useCustomerDataStore = defineStore('customerData', () => {

    const customerData = ref(null)

    const getCustomerData = async() => {
        let res = await fetchContents("/getCustomer")
        if ( res ) {
            customerData.value = res
        }
    }

    return { customerData, getCustomerData }
})