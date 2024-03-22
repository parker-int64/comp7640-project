<script setup>

import { ref } from 'vue'

import { NH1, NFlex, NLayout, NCard, NButton, NIcon, NForm, NFormItem, NInput, NMessageProvider } from 'naive-ui'

import { useMessage } from "naive-ui"

import { LogInOutline } from '@vicons/ionicons5'

import axios from 'axios';

const message = useMessage()

const formRef = ref(null)

const formValue = ref({
    user: {
        name: "",
        passwd: "",
        repeatPasswd:""
    },
})

const rules = ref({
    rules: {
        user: {
          name: {
            required: true,
            message: "Enter your name",
            trigger: "blur",
            validator(rule, value) {
                if(!value){
                    return new Error("Empty username");
                }
            }
          },
          passwd: {
            required: true,
            message: "Enter your password",
            trigger: "blur"
          },
          repeatPasswd: {
            required: true,
            message: "Repeat your password",
            trigger: "blur"
          }
        },
    },
})


const isLogin = ref(false); // Default, no login

const toggleLogin = ref(false)


const switchLogin = () => {
    toggleLogin.value = !toggleLogin.value
}


const handleUsernameInput = () => {
    console.log(formValue.value.user)
}


const handleLogin = () => {
   // get the username and password
   const userInfo = formValue.value.user

   // Post to backend
    axios({
        method: 'post',
        url: "/validUser",
        data: userInfo
    })

    console.log("Send the post..")
}

</script>

<template>
    <n-message-provider>
        <n-layout style="margin-top: auto;">
            <n-flex justify="center" align="center">
                <n-card :title="toggleLogin ? 'Sign Up' : 'Sign In'"  size="large">
                    <n-form
                    ref="formRef"
                    :label-width="120"
                    :model="formValue"
                    :rules="rules"
                    size="large"
                    >
                        <n-form-item  path="user.name" label="Username">
                            <n-input 
                            v-model:value="formValue.user.name"
                            @input="handleUsernameInput" 
                            placeholder="Enter your username"
                            @keydown.enter.prevent
                        />
                        </n-form-item>
    
                        <n-form-item path="user.passwd" label="Password">
                            <n-input
                                v-model:value="formValue.user.passwd"
                                type="password"
                                @input="handlePasswordInput"
                                @keydown.enter.prevent
                                placeholder="Enter your password"
                            />
                        </n-form-item>
    
    
                        <n-form-item path="user.repeatPasswd" label="Repeat Your Password" v-if=toggleLogin>
                            <n-input
                                v-model:value="formValue.user.repeatPasswd"
                                type="password"
                                @input="handleRepeatPasswd"
                                @keydown.enter.prevent
                            />
                        </n-form-item>
    
                        <n-form-item v-if=!toggleLogin>
                            <n-flex justify="space-between" align="center" style="min-width: 100%;">
                                <n-button @click="handleLogin">
                                    <template #icon>
                                        <n-icon>
                                            <log-in-outline />
                                        </n-icon>
                                    </template>
                                    Login
                                </n-button>
                                <n-button text @click="switchLogin">
                                    No account? Sign Up
                                </n-button>
                            </n-flex>
                        </n-form-item>
    
    
                        <n-form-item v-if=toggleLogin>
                            <n-flex justify="space-between" align="center" style="min-width: 100%;">
                                <n-button @click="handleReg">
                                    Sign Up
                                </n-button>
    
                                <n-button text @click="switchLogin">
                                    Already have an account? Sign In
                                </n-button>
                            </n-flex>
                        </n-form-item>
                    </n-form>
                </n-card>
            </n-flex>
        </n-layout>
    </n-message-provider>

</template>


<style scoped>

.n-card {
  max-width: 600px;
}

</style>
