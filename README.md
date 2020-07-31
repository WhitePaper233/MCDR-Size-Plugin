# MCDR-Size-Plugin
Use command to get your server's save size.

用一条指令来获取您服务器存档的大小！

Pass in Windows10 and Centos8.

在 Windows10 和 Centos8 系统下测试通过.

------

## How to install it?如何安装它？

Download the last release and put it in "plugins"(in your MCDR folder)

下载最新的release然后将其放在你MCDR目录下的“plugins”文件夹中即可

## How to use it?如何使用它？

Type command "!!getsize" in game if you haven't changed anything.

如果你没有更改任何东西，在游戏中输入“!!getsize”指令

## How to change command?如何更改指令？

1.Open "Size.py" file 

打开“Size.py”文件 

2.Change line8

更改第8行的内容

Example:

例子：

Change this

将这个

```python
command = '!!getsize'
```

To:

更改为：

```python
command = '!!save size'
```

Then you can use "!!save size" to get your server's save size.

然后你就能使用“!!save size”获取服务器存档大小了

------

## Q&A：

1.Q:Why not support Bukkit / Spiogt?

A:![Not Vanilla](https://i.loli.net/2020/07/31/iVHD7o8QCpKYPsM.jpg)

2.Q:Muti-Language?

A:No.
