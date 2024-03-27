<script setup>
import { NLayout, NFlex, NDataTable, NH1, NSelect, NP } from 'naive-ui' 
import { onMounted, ref } from 'vue';
import { useTransDataStore } from '../stores/transData'

const transStore = useTransDataStore()

const trans = ref(null)
const selectValue = ref(null)
const selectOptions = ref([])

const tColumns = ref([])

const tData = ref([])

const updateTableContent = (id) => {
  if ( id === 'all' ) {
    tData.value = trans.value
  } else {
    tData.value = filterByUserId(trans.value, id)
    
  }
} 



const filterByUserId = (data, id) =>{
  return data.filter(e => e.customer_ID === id)
}


onMounted(() => {
  transStore.getTransData().then(() => {
      if( transStore.transData ) {
        trans.value = transStore.transData

        let retSelectOptions = []

        retSelectOptions.push({
          label: 'All',
          value: 'all'
        })
        // create select drop down
        const idValues = Object.values(trans.value)
        const newArr = [...new Set(idValues.map(item => item.customer_ID))].map((e)=> {
          return {
            label: `Customer ID ${e}`,
            value: e
          }
        })

        retSelectOptions = retSelectOptions.concat(newArr)

        selectOptions.value = retSelectOptions
        
        // create columns
        tColumns.value = [
          {
            title: "Transaction ID",
            key: "transaction_ID"
          },

          {
            title: 'Date',
            key: 'date'
          },
          
          {
            title: 'Total Amount',
            key: 'total_amount'
          },

          {
            title: 'Product Name',
            key: 'product_name'
          },

          {
            title: 'Customer ID',
            key: 'customer_ID'
          },

          {
            title: 'Contact Number',
            key: 'contact_number'
          },

          {
            title: "Shipping Address",
            key: 'shipping_details'
          }
        ]

        tData.value = Object.values(trans.value)
      }
  })

})

</script>



<template>
    <n-layout>
        <n-h1>Transaction Records</n-h1>

        <n-p>Please specify a user/customer, or by default, you may view all transaction records </n-p>
        <n-flex justify="center" align="center" vertical style="margin-bottom: 30px;">
          <n-select v-model:value="selectValue" :options="selectOptions" @update-value="updateTableContent" placeholder="All" default-value="All" />
          <n-data-table :columns="tColumns" :data="tData" />
        </n-flex>
    </n-layout>
</template>