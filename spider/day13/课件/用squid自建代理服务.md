## squid是什么？

Squid是一个高性能的代理缓存服务器，Squid支持FTP、gopher、HTTPS和HTTP协议。和一般的代理缓存软件不同，Squid用一个单独的、非模块化的、I/O驱动的进程来处理所有的客户端请求。



## squid工作原理

 Squid是一个缓存Internet数据的一个软件，它接收用户的下载申请，并自动处理所下载的数据。也就是说，当一个用户想要下载一个主页时，它向Squid发出一个申请，要Squid替它下载，然后Squid 连接所申请网站并请求该主页，接着把该主页传给用户同时保留一个备份，当别的用户申请同样的页面时，Squid把保存的备份立即传给用户，减少了向Internet提交重复的Web请求的过程，提高了用户下载网页的速度，隐藏了客户机的真实IP，如下图所示：


![img](imgs/squid.png)



## 准备工作

- 公网服务器一台，linux操作系统（以腾讯云，linux操作系统为例）
- xshell远程工具，远程操作公网服务器



## 使用远程工具连接到服务器

```
使用xshell实现远程连接服务器
```







## 如何操作

#### 1.安装

```python
1.sudo apt-get update  更新
2.sudo apt-get install squid  在线安装squid
3.sudo apt-get remove squid   删除
```



#### 2.验证安装是否成功

```
squid3 -v
有出现版本号就说明安装成功
```

#### 3.设置

```
进入到/etc/squid文件夹
cd /etc/squid
里面会有一个squid.conf文件，
sudo vim squid.conf 
修改 http_access deny all
为  http_access allow all
默认端口是 3128 
```



#### 4.启动

```
启动任务
service squid start
输入命令查看监听
netstat -ntl
```

![](imgs/开启端口.png)



#### 5.服务器开放端口

![](imgs/服务器开放端口.png)



#### 6.设置代理

![](imgs/设置代理.png)



#### 7.访问成功

![img](imgs/访问成功.png)

#### 8.关闭防火墙

```
如果打开安全组端口还是不行关闭防火墙

关闭防火墙
systemctl stop firewalld
关闭防火墙自启
systemctl disable firewalld
#查看默认防火墙状态（关闭后显示notrunning，开启后显示running)

```

