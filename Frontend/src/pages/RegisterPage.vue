<script setup>

</script>


<template>
    <div class="container">
        <h2>User Registration</h2>
        <form>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter a username">
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="text" id="email" name="email" placeholder="Enter your email">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter a password">
            </div>
            <button type="submit" class="btn">Register</button>
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