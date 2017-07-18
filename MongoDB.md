# MongoDB

> MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

## 关系型数据库
> 1. 数据库有行、列的概念，数据有关系，数据不是散的。
> 2. 数据库能够提供非常方便的接口，让增删改查操作变得简单
> 3. 数据库不能自己玩，要给向PHP、.net、jsp等语言提供接口

## NoSQL
> 没有行、列的概念。用JSON来存储数据。集合就相当于“表”，文档就相当于“行”。

## SQL和NOSQL的比较
NoSQL数据库在以下的这几种情况下比较适用：
1. 数据模型比较简单；
2. 需要灵活性更强的IT系统；
3. 对数据库性能要求较高；
4. 不需要高度的数据一致性；
5. 对于给定key，比较容易映射复杂值的环境。

> 有些系统，特别需要筛选。比如，筛选出所有女生大于20岁的。那么SQL型数据库，非常擅长！因为它有行、列的概念。但是，有些系统，真的不需要进行那么多的筛选，比如站内信。站内信只需要存储就好了。不需要筛选。那么NoSQL的。

## 下载MongoDB
[https://www.mongodb.com/download-center?jmp=nav#community](https://www.mongodb.com/download-center?jmp=nav#community)

## 安装环境
> Windows 7 64位

## 安装MongoDB
![](http://i.imgur.com/tXIe2rl.png)
> 如果你的系统是 Windows Server 2008 R2 or Windows 7 ，需要安装一个补丁<br>
> [https://support.microsoft.com/zh-cn/help/2731284/33-dos-error-code-when-memory-memory-mapped-files-are-cleaned-by-usin](https://support.microsoft.com/zh-cn/help/2731284/33-dos-error-code-when-memory-memory-mapped-files-are-cleaned-by-usin)

![](http://i.imgur.com/g3QPCl8.png)

## 加载环境变量
![](http://i.imgur.com/Vz7BWNI.png)
> 测试

![](http://i.imgur.com/G1xasUP.png)

> mongo   使用数据库<br>
> mongod  开机<br>
> mongoimport  导入数据

## 开启数据库
> mongod --dbpath D:\AppServ\Mongo<br>
> --dbpath就是选择数据库文档所在的文件夹<br>
> mongoDB中，真的有物理文件，对应一个个数据库。U盘可以拷走<br>
> 一定要保持，开机这个CMD不能动了，不能关，不能ctrl+c。 一旦这个cmd有问题了，数据库就自动关闭了。

![](http://i.imgur.com/nZxvOxA.png)

> 新开窗口，输出 `mongo` 连接数据库

![](http://i.imgur.com/GArOujF.png)