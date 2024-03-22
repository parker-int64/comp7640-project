<script setup>
import { useRouter, useRoute } from 'vue-router'   //引入路由
import { ref } from 'vue'

const routes = useRoute();      //与后端交互
const router = useRouter();    //页面导航

const isLogin = ref(true); // 切换登录和注册的状态
//传到后端的数据结构
const username = ref('');
const password = ref('');
//邮箱功能砍掉
// const email = ref('');


const toggleForm = () => {
    isLogin.value = !isLogin.value;
};

// 处理表单提交逻辑
const handleSubmit = (event) => {
    event.preventDefault();

}

// 使用路由导航
const handleRegister = () => {

    router.push('/register');
}

</script>


<template>

    <div class="container">
        <h2 v-if="isLogin">Sign in</h2>
        <h2 v-else>Sign up</h2>

        <form @submit.prevent="isLogin ? login() : register()">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" v-model="username" required>
            </div>

            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" v-model="password" required>
            </div>
            <!-- 邮箱功能砍掉 -->
            <!-- <div v-if="!isLogin">
                <label for="email">E-mail:</label>
                <input type="email" id="email" v-model="email" required>
            </div> -->


        </form>
        <button type="submit" class="btn">{{ isLogin ? 'Sign in' : 'Sign up' }}</button>
        <button @click="toggleForm" class="btn">{{ isLogin ? 'No account？Go sign up' : 'Have account？Go Sign in'
            }}</button>
    </div>


</template>


<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    margin: 0;
    padding: 0;
}

.container {
    width: 100% auto;
    margin: 100px auto;
    background-color: #fff;
    padding: 15px;
    border-radius: 5px;
    box-shadow: none;
    /* 取消边缘阴影 */

    display: flex;
    flex-direction: column;
    align-items: center;
}

h2 {
    text-align: center;
    color: #333;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
    width: 50% auto;
    padding: 6px;
    font-size: 20px;
    border-radius: 3px;
    border: 1px solid #ccc;
}

.btn {
    display: block;
    width: 200px;
    margin-top: 10px;
    /* 添加上边距使按钮与输入框对齐 */
    padding: 10px;
    font-size: 16px;
    border-radius: 3px;
    background-color: #4CAF50;
    color: #fff;
    text-align: center;
    align-items: center;
    text-decoration: none;
    cursor: pointer;
}

.btn:hover {
    background-color: #45a049;
}
</style>
