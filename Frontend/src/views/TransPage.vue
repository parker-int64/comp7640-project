<script setup>
import { NLayout, NFlex, NCard, NDataTable, NH1 } from 'naive-ui' 


const tableColumns = [
    {
      title: 'Name',
      key: 'name'
    },
    {
      title: 'Age',
      key: 'age'
    },
    {
      title: 'Address',
      key: 'address'
    },
    {
      title: 'Tags',
      key: 'tags'
    },
    {
      title: 'Action',
      key: 'actions'
    }
]

</script>



<template>
    <n-layout>
        <n-h1>Transaction Records</n-h1>
        <n-flex justify="center" align="center" vertical>
            <n-data-table :columns="tableColumns" :data="data" />
        </n-flex>
    </n-layout>
</template>