# Redis
> Redis 与其他 key - value 缓存产品有以下三个特点：
- Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
- Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
- Redis支持数据的备份，即master-slave模式的数据备份。 

# 安装Redis
> 环境:windows 7 64位
> 下载地址：[https://github.com/MSOpenTech/redis/releases](https://github.com/MSOpenTech/redis/releases)
> 下载完毕后，将压缩包解压，在cmd上进入解压文件夹。
> 输入命令：redis-server.exe redis.windows.conf 开启redis

![](http://i.imgur.com/WSwD5ar.png)

> 测试Redis
> 重新开一个cmd窗口
> 设置键值对测试

![](http://i.imgur.com/u5kMt9d.png)

> 安装成功