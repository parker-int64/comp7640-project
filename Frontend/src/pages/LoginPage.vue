<script setup>
import { useRouter } from 'vue-router'   //引入路由




</script>


<template>
    <div class="container">
        <h2>User Login</h2>
        <form>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter your username">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password">
            </div>
            <button type="submit" class="btn">Login</button>
            <button type="" class="btn" @click="">Register</button>
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
    width: 80%;
    /* 使用百分比定义宽度 */
    max-width: 4000px;
    /* 设置最大宽度 */
    margin: 1000px auto;
    /* 使用百分比定义边距 */
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
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

input[type=" text"],
input[type="password"] {
    width: 100%;
    padding: 8px;
    font-size: 16px;
    border-radius: 3px;
    border:
        1px solid #ccc;
}

.btn {
    display: block;
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border-radius:
        3px;
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
