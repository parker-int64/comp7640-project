<script setup>
import { useRouter, useRoute } from 'vue-router'   //引入路由
import { ref } from 'vue'

const routes = useRoute();
const router = useRouter();    //页面导航

const data = ref({
    username: "",
    password: "",
})

const handleSubmit = (event) => {
    event.preventDefault();
    // 处理注册逻辑


    // 示例：向后端发送注册请求
    fetch('/api/register', {
        method: 'POST',
        body: JSON.stringify(data.value),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            // 处理响应
            if (response.ok) {
                // 注册成功后的逻辑
                router.push('/login'); // 跳转到登录页面
            } else {
                // 注册失败后的逻辑
                console.log('注册失败');
            }
        })
        .catch(error => {
            // 错误处理
            console.log('发生错误', error);
        });
}

const handleLogin = () => {
    router.push('/login'); // 跳转到登录页面
}

</script>


<template>
    <div class="container">
        <h2>User Registration</h2>
        <form @submit="handleSubmit" v-if="routes.name != 'register'">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter your username"
                    v-model="data.username">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password"
                    v-model="data.password">
            </div>
            <button type="submit" class="btn">Register</button>
            <button type="button" class="btn" @click="handleLogin">Login</button>
        </form>
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
    width: 300px;
    margin: 100px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);

    display: flex;
    flex-direction: column;
    align-items: stretch;
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
    width: 100%;
    padding: 8px;
    font-size: 16px;
    border-radius: 3px;
    border: 1px solid #ccc;
}

.btn {
    display: block;
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border-radius: 3px;
    background-color: #4CAF50;
    color: #fff;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
}

.btn:hover {
    background-color: #45a049;
}
</style>