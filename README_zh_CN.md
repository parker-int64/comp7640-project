
<div align="center">
    <p> <a href="./README.md">English</a> | 简体中文</p>
</div>




# COMP 7640 Database Management 小组项目


## 项目要求

下面是一些软件要求：

|名称|最低版本要求|
|:----:|:----:|
|Python|3.11|
|Node|18.18|
|npm|9.8|
|mysql|8.3|


你可以在`requirements.txt`中看到其它python的依赖信息

## 如何运行


+ Clone 本仓库，如果是下载的源码，请直接解压后进行下一步
```{shell}
git clone https://github.com/parker-int64/comp7640-project
```

如果代码是zip包，请解压后直接进入终端使用

+ 初始化虚拟环境
```{shell}
cd comp7640-project
python -m venv venv
```

+ 激活虚拟环境
  - 在Unix(MacOS)/Linux 操作系统上
  ```
  source ./venv/bin/activate
  ```
  - 使用Windows Powershell
  ```
   & .\venv\Scripts\activate
  ```
  - 使用Windows Command Prompt
  ```
  .\venv\Scripts\activate.bat
  ```

+ 使用pip安装依赖
```Shell
pip install -r requirements.txt
```

+ 准备数据

数据库数据库应该提前准备，如要正常运行本程序，需要在项目根目录创建一个`sqlconf.json`。

（在本程序中，我们准备了`comp7640_frontend_version.sql`专门用于前端使用。）

`sqlconf.json`

```{json}
{
    "host": "localhost",
    "user": "<Your database user>",     
    "passwd": "<Your password>"
}

```

+ 运行程序

```shell
python main.py
```

+ 然后，打开浏览器 输入 'http://localhost:5000'

如果直接运行遇见问题，可以进入Debug模式


## Debug 模式
+ 前端Debug:

```
cd ./Frontend

npm install

npm run dev
```

+ 后端Debug:

```
cd ./Backend/src

python app_test.py
```