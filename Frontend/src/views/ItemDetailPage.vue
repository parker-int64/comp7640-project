<script setup>
import ItemCarousel from '../components/ItemCarousel.vue';
import { NLayout, NFlex, NGi, NGrid, NCard, NH1 } from 'naive-ui' 
</script>



<template>
    <n-layout style="height: 100%;">
        
        <n-flex vertical>
            <n-grid x-gap="12" cols="1 s:2 m:2 l:2 xl:2 2xl:2" responsive="screen">
                <n-gi>
                    <ItemCarousel />
                </n-gi>
                <n-gi>
                    <NCard>
                        <n-h1>Item name placeholder</n-h1>
                        <p>Card Area1</p>
                    </NCard>
                </n-gi>
            </n-grid>
        </n-flex>
            
    </n-layout>
</template>