> python 在 winodws 下的基础环境搭建

## Windows 环境配置
### Python 下载

> <a href="https://www.python.org/" target="_blank">Python 官网</a>

### Windows 环境

Windiws新版终端需要设置为`remotesigned`模式
以管理员模式执行以下
```
set-ExecutionPolicy RemoteSigned
```

### Python虚拟环境
> 可将多个项目之间的模块隔离

```
python -m venv venv
```
- 创建环境后激活环境
```
.\venv\Scripts\actvate
```
- Liunx
```
source actvate
```

### 配置pip国内源
- Windiws
 `C:\Users\xxxx\`下创建`pip\pip.ini`
    ```
    [global]
    timeout = 6000
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    trusted-host = pypi.tuna.tsinghua.edu.cn
    ```


## windows创建 `.py`文件
- powerShell
```
echo >>demo.py
```
- windows 有提示直接回车跳过
