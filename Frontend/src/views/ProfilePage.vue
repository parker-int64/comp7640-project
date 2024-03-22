<script setup>
import { NFlex, NLayout, NH1, NCard, NP, NGrid, NGi, NButton, NIcon } from 'naive-ui';
import { ref } from 'vue';
import { CreateOutline, CheckmarkSharp } from '@vicons/ionicons5'


const isVendor = ref(false)

const toggleEdit = ref(false) // I mean, if they want to update their profile.


const handleProfileEdit = () => {
    // First, toggle the edit mode
    toggleEdit.value = true

    
}


const handleProfileSubmit = () => {
    // Change the toggle mode back
    toggleEdit.value = false
}
</script>

<template>
    <n-layout style="margin: auto; max-width: 600px">
        <n-flex justify="center" align="start" vertical>
            <n-h1>Profile</n-h1>
            <n-card :title="isVendor ?  'Hello, dear vendor!' : 'Hello, dear customer!' ">
                <n-grid :x-gap="12" :y-gap="8" :cols="2">
                    <n-gi>
                        <n-p> {{ isVendor ? "Vendor ID" : "Customer ID" }} </n-p>
                    </n-gi>
                    <n-gi>
                        <n-p> placeholder </n-p>
                    </n-gi>
                    <n-gi>
                        <n-p> {{ isVendor ? "Vendor ID" : "Customer ID" }} </n-p>
                    </n-gi>
                    <n-gi>
                        <n-p> placeholder </n-p>
                    </n-gi>
                </n-grid>
                
                <n-flex justify="start" align="center" style="margin-top: 20px;">
                    <n-button v-if=!toggleEdit @click="handleProfileEdit">
                        <template #icon>
                            <n-icon>
                                <create-outline />
                            </n-icon>
                        </template>
                        Edit
                    </n-button>
                    <n-button v-if=toggleEdit type="success" @click="handleProfileSubmit">
                        <template #icon>
                            <n-icon>
                                <checkmark-sharp />
                            </n-icon>
                        </template>
                        Save
                    </n-button>
                </n-flex>
            </n-card>
        </n-flex>
    </n-layout>
</template>


<style scoped>


</style>