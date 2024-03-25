<script setup>
import {NAvatar, NFlex, NH1, NLayoutHeader, NInput, NIcon, NDropdown, NButton} from 'naive-ui'
import logoUrl from '@/assets/icon.svg'
import { SearchOutline, 
         PersonCircleOutline as UserIcon, 
         LogOutOutline  as LogoutIcon } 
        from "@vicons/ionicons5";
import { h, ref } from 'vue';

import { RouterLink, useRoute, useRouter } from 'vue-router';


const userLogin = ref(false)



const renderIcon = (icon) => {
  return () => {
    return h(NIcon, null, {
      default: () => h(icon)
    });
  };
};

const userDropOptions = [
    {
      label: 'Logout',
      key: 'logout',
      icon: renderIcon(LogoutIcon)
    }
]


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
            <n-input placeholder="Search" style="width: 240px;">
                <template #prefix>
                    <n-icon :component="SearchOutline" />
                </template>
            </n-input>
            <n-dropdown v-if="userLogin" :options="userDropOptions">
                <n-button>{{ "Hello, " +  }}</n-button>
            </n-dropdown>
            <router-link to="/login">
                <n-button text>
                    <template #icon>
                    <n-icon>
                        <UserIcon />
                    </n-icon>
                    </template>
                    login
                </n-button>
            </router-link>
        </n-flex>

        </n-flex>
    </n-layout-header>
</template>


<style scoped>

</style>