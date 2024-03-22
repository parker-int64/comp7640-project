<script setup>
import ItemCarousel from '../components/ItemCarousel.vue'
import ItemCard from '../components/ItemCard.vue'
import { NLayout, NGrid, NGi, NFlex, NDivider, NH1, NIcon, NButton, NDropdown } from 'naive-ui'
import { FilterOutline } from '@vicons/ionicons5'

const dropOptions = [
    {
        label: "All",
        key: 'all'
    },
    {
        label: "Vendor",
        key: 'vendor'
    }
]

const handleSelect = (key) => {
    console.log("Key", key);
}

</script>


<template>
    <n-layout content-style="padding: 24px;">
        <n-h1>Home Page</n-h1>
        <n-flex justify="center" align="center">
            <ItemCarousel style="padding-bottom: 10px; max-width: 75vw;" />
        </n-flex>

        <n-divider />

        <n-flex justify="space-between" align="center">
            <n-h1>Recommend for You</n-h1>
            <n-dropdown trigger="hover" :options="dropOptions" @select="handleSelect">
                <n-button text>
                    <template #icon>
                        <n-icon :component="FilterOutline" />
                    </template>
                    Filter
                </n-button>
            </n-dropdown>
        </n-flex>

        
        
        <n-grid :x-gap="12" :y-gap="8" cols="2 s:3 m:4 l:4 xl:5 2xl:6" responsive="screen">
            <n-gi>
                <ItemCard />
            </n-gi>
            <n-gi>
                <ItemCard />
            </n-gi>
            <n-gi>
                <ItemCard />
            </n-gi>
            <n-gi>
                <ItemCard />
            </n-gi>
            <n-gi>
                <ItemCard />
            </n-gi>
            <n-gi>
                <ItemCard />
            </n-gi>
        </n-grid>
        
    </n-layout>

</template>


<style scoped>

</style>
