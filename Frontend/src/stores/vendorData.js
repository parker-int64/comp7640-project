import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchContents } from '../requests/fetch'

export const useVendorDataStore = defineStore('vendorData', () => {

    const vendorData = ref(null)


    const addVendorStatus = ref(null)

    const getVendorData = async() => {
        let res = await fetchContents("/getVendor")
        if ( res ) {
            vendorData.value = res
        }
    }


    const addVendor = async(body) => {
        let res = await fetchContents("/addVendor", body)
        if ( res ) {
            addVendorStatus.value = res
        }
    }

    return { vendorData, getVendorData, addVendorStatus ,addVendor }
})