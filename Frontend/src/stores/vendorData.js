import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchContents } from '../requests/fetch'

export const useVendorDataStore = defineStore('vendorData', () => {

    const vendorData = ref(null)

    const getVendorData = async() => {
        if(vendorData.value === null){
            let res = await fetchContents("/getVendors")
            if ( res ) {
                vendorData.value = res
            }
        }
    }

    return { vendorData, getVendorData }
})