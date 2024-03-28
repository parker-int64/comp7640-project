<script setup>
import {NFlex, NH1, NLayoutHeader, NInput, NIcon, NButton} from 'naive-ui'
import logoUrl from '@/assets/icon.svg'
import { SearchOutline, 
         PersonCircleOutline as UserIcon, 
         ReceiptOutline,
         HomeOutline } 
        from "@vicons/ionicons5";

import { RouterLink, useRouter } from 'vue-router';


const router = useRouter()


const handleKeyUp = (e) => {
    if (e.key === 'Enter') {
        let value = e.target.value

        if(value){
            router.push(`/search/${value}`)
        } else {
            router.push('/')
        }

    }
}

</script>

<template>
    <n-layout-header 
        style="padding-left: 20px; padding-right: 20px;"
        bordered
    >
        <n-flex justify="space-between" align="center" size="large">
            <fragment>
                <n-flex align="center" size="small">
                    <router-link to="/"><img
                        width="36"
                        :src="logoUrl"
                        alt="logo"
                        style="display: block; margin: auto"
                    /></router-link>
                    <n-h1 style="margin: 10px 0 10px 0">E-Store</n-h1>
                </n-flex>
            </fragment>

        <n-flex>
            <n-input 
                placeholder="Search" 
                style="width: 240px;"
                @update-value="onInputChange"
                @keyup="handleKeyUp($event)"
            >
                <template #prefix>
                    <n-icon :component="SearchOutline" />
                </template>
            </n-input>
            
            <router-link to="/">
                <n-button text>
                    <template #icon>
                    <n-icon>
                        <HomeOutline />
                    </n-icon>
                    </template>
                    Home
                </n-button>
            </router-link>


            <router-link to="/manage">
                <n-button text>
                    <template #icon>
                    <n-icon>
                        <UserIcon />
                    </n-icon>
                    </template>
                    Manage
                </n-button>
            </router-link>

            <router-link to="/trans">
                <n-button text>
                    <template #icon>
                    <n-icon>
                        <ReceiptOutline />
                    </n-icon>
                    </template>
                    Transactions
                </n-button>
            </router-link>
        </n-flex>

        </n-flex>
    </n-layout-header>
</template>


<style scoped>

</style>