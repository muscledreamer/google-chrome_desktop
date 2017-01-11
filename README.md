# Ubuntu google_chrome代理问题

### 由于google浏览器代理窗口无法打开，所以只能用命令行设置代理启动浏览器

首先翻墙，翻墙方式这里省略，用命令行启动google_chrome:

```
google-chrome --proxy-server="socks5://[ip]:[端口]"
```
启动后可通过IP检测，是否翻墙启动成功

### 下面介绍一下如何直接启动设置代理后的google-chrome：

首先我们要将goole-chrome 固定在启动器，在配置路径下有一个google-chrome.desktop文件
```
/usr/share/applications/google-chrome.desktop
```
找到修改这一行
```
Exec=/usr/bin/google-chrome-stable %U --proxy-server="socks5://[IP]:[端口]
```
关闭所有google-chrome再次从启动器启动就会OK了
可进行ip检测(==启动浏览器前勿忘翻墙==)

## 这里的python 脚本，是为了方便大家更换IP时，自动修改配置文件

下载直接运行tools.py即可修改（==有的机器可能要修改脚本中的配置文件路径以及网卡名称==） 


```
#配置文件路径
desktop_pwd = "/usr/share/applications/google-chrome.desktop"

#网卡
network_card = 'enp9s0'

```
* 设置desktop后从启动器启动的google浏览器都会自动配置代理，如果不需要代理启动，大家可以直接通过终端启动

```
google-chrom
```

* 由于启动器不能同时启动两种模式下的浏览器，所以确保一种模式启动时，没有另一种浏览器正在使用

### 如果有什么具体问题，欢迎大家与我交流：


### Wechet: bojingqian1313
