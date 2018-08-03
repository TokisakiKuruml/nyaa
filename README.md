# 前言
这是一个在某神秘网站（笑）上爬取神秘链接的爬虫。此爬虫使用的是scrapy爬虫框架，代码虽然简单但是还是用起来还是很有趣。

# 数据保存<br>
本爬虫使用的是mysql进行数据保存，只需修改`settings.py`中的数据库信息和`items.py`中`table`(数据库表)即可。
```
MYSQL_HOST = 'localhost'
```
```
MYSQL_DATABASE = 'nyaa'
```
```
MYSQL_PORT = 3306
```
```
MYSQL_USER = 'root'
```
```
MYSQL_PASSWORD = '123456'
```
# 代理
#### 代理池代理
使用此代理需先运行代理池，然后修改`settings.py`中的代理池的接口地址。
```
PROXY_URL ='http://localhost:5555/random'
```

#### 本地代理
使用本地代理时，请确保本机已开启代理。并清楚使用的协议类型。<br>
确认后修改`ProxyMiddleware2`中的：<br>
```
proxy = '127.0.0.1:1080'//本地代理的端口
```
```
uri = 'socks5://{proxy}'.format(proxy=proxy)//协议类型修改
```
##### ！注意：使用本地代理ip长时间爬取有可能回返回403.
完成以上步骤后请打开`settings.py`中对应的函数。
```
DOWNLOADER_MIDDLEWARES = {
   # 'nyaa.middlewares.ProxyMiddleware': 300,
   'nyaa.middlewares.ProxyMiddleware2': 300,
}
```
# 最后
scrapy crawl ny<br>
即可启动
