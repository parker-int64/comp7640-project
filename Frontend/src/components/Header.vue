<script setup>
    import {NAvatar, NFlex, NH2, NLayoutHeader, NInput, NIcon} from 'naive-ui'
    import logoUrl from '@/assets/icon.svg'
    import { SearchOutline } from "@vicons/ionicons5";
</script>

<template>
    <n-layout-header style="height: 8vh; padding-left: 20px; padding-right: 20px;">
        <n-flex justify="space-between" align="center" size="large">
        <img
            width="36"
            :src="logoUrl"
            alt="logo"
        />
        <n-h2>E-Store</n-h2>

        <n-flex>
            <n-input placeholder="Search" style="width: 240px;">
            <template #prefix>
                <n-icon :component="SearchOutline" />
            </template>
            </n-input>
            <n-avatar :style="{
                color: 'yellow',
                backgroundColor: 'purple',   
                }"
            >K</n-avatar>
        </n-flex>

        </n-flex>
    </n-layout-header>
</template>


<style scoped>

</style>