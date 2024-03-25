import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchContents } from '../requests/fetch'

export const useTransDataStore = defineStore('transData', () => {

    const transData = ref(null)

    const getTransData = async() => {
        if(transData.value === null){
            let res = await fetchContents("/getTrans")
            if ( res ) {
                transData.value = res
            }
        }
    }

    return { transData, getTransData }
})