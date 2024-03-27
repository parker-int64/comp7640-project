import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchContents } from '../requests/fetch'

export const useTransDataStore = defineStore('transData', () => {

    const transData = ref(null)
    const addTransStatus = ref(null)
    const delTransStatus = ref(null)

    const getTransData = async() => {
        let res = await fetchContents("/getTrans")
        if ( res ) {
            transData.value = res
        }
    }

    const addTrans = async (body) => {
        let res = await fetchContents("/addTrans", body)
        if ( res ) {
            addTransStatus.value = res
        }
    }


    const delTrans = async (body) => {
        let res = await fetchContents("/delTrans")
        if ( res ) {
            delTransStatus.value = res
        }
    }




    return { transData, getTransData, addTrans, addTransStatus, delTrans, delTransStatus }
})