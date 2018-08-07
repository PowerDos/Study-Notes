# Docker
> 部分总结来自网络
### 目录
1. [Docker](#docker)
	- [简介](#简介)
	- [优点](#优点)
	- [基本概念](#基本概念)
	- [安装Docker](#安装docker)
	- [卸载Docker](#卸载docker)

## 简介
> Docker 最初是 dotCloud 公司创始人 Solomon Hykes 在法国期间发起的一个公司内部项目，它是基于 dotCloud 公司多年云服务技术的一次革新，并于 2013 年 3 月以 Apache 2.0 授权协议开源，主要项目代码在 GitHub 上进行维护。Docker 项目后来还加入了 Linux 基金会，并成立推动 开放容器联盟（OCI）。

> Docker 在容器的基础上，进行了进一步的封装，从文件系统、网络互联到进程隔离等等，极大的简化了容器的创建和维护。使得 Docker 技术比虚拟机技术更为轻便、快捷

> 下面的图片比较了 Docker 和传统虚拟化方式的不同之处。传统虚拟机技术是虚拟出一套硬件后，在其上运行一个完整操作系统，在该系统上再运行所需应用进程；而容器内的应用进程直接运行于宿主的内核，容器内没有自己的内核，而且也没有进行硬件虚拟。因此容器要比传统虚拟机更为轻便。

![](https://i.imgur.com/LYT5wO2.png)
![](https://i.imgur.com/4m35Hyw.png)

## 优点
### 更高效的利用系统资源
> 由于容器不需要进行硬件虚拟以及运行完整操作系统等额外开销，Docker 对系统资源的利用率更高。无论是应用执行速度、内存损耗或者文件存储速度，都要比传统虚拟机技术更高效。因此，相比虚拟机技术，一个相同配置的主机，往往可以运行更多数量的应用。

### 更快速的启动时间
> 传统的虚拟机技术启动应用服务往往需要数分钟，而 Docker 容器应用，由于直接运行于宿主内核，无需启动完整的操作系统，因此可以做到秒级、甚至毫秒级的启动时间。大大的节约了开发、测试、部署的时间

### 一致的运行环境
> 开发过程中一个常见的问题是环境一致性问题。由于开发环境、测试环境、生产环境不一致，导致有些 bug 并未在开发过程中被发现。而 Docker 的镜像提供了除内核外完整的运行时环境，确保了应用运行环境一致性，从而不会再出现 **这段代码在我机器上没问题啊** 这类问题。

### 持续交付和部署
> 对开发和运维（DevOps）人员来说，最希望的就是一次创建或配置，可以在任意地方正常运行。

> 使用 Docker 可以通过定制应用镜像来实现持续集成、持续交付、部署。开发人员可以通过 Dockerfile 来进行镜像构建，并结合 持续集成(Continuous Integration) 系统进行集成测试，而运维人员则可以直接在生产环境中快速部署该镜像，甚至结合 持续部署(Continuous Delivery/Deployment) 系统进行自动部署。

> 而且使用 Dockerfile 使镜像构建透明化，不仅仅开发团队可以理解应用运行环境，也方便运维团队理解应用运行所需条件，帮助更好的生产环境中部署该镜像。

### 更轻松的迁移
> 由于 Docker 确保了执行环境的一致性，使得应用的迁移更加容易。Docker 可以在很多平台上运行，无论是物理机、虚拟机、公有云、私有云，甚至是笔记本，其运行结果是一致的。因此用户可以很轻易的将在一个平台上运行的应用，迁移到另一个平台上，而不用担心运行环境的变化导致应用无法正常运行的情况。

### 更轻松的维护和扩展
> Docker 使用的分层存储以及镜像的技术，使得应用重复部分的复用更为容易，也使得应用的维护更新更加简单，基于基础镜像进一步扩展镜像也变得非常简单。此外，Docker 团队同各个开源项目团队一起维护了一大批高质量的 官方镜像，既可以直接在生产环境使用，又可以作为基础进一步定制，大大的降低了应用服务的镜像制作成本。

### 对比传统虚拟机总结
| 特性 | Docker |  VM  |
| :----: | :--------: | :---------: |
| 启动 | 秒级 | 分钟级 |
| 硬盘使用 | 一般为 MB | 一般为 GB |
| 性能 | 接近原生 | 弱于 |
| 系统支持量 | 单机支持上千个容器 | 一般几十个 |

## 基本概念
### 仓库、镜像、容器关系图
![](https://i.imgur.com/CrHFr1j.jpg)

### 镜像
> Docker的镜像概念类似于虚拟机里的镜像，是一个只读的模板，一个独立的文件系统，包括运行容器所需的数据，可以用来创建新的容器。

> 例如：一个镜像可以包含一个完整的 CentOS 操作系统环境，里面仅安装了MongoDB或用户需要的其它应用程序

> Docker与操作系统的关系:
> 对于 Linux 而言，内核启动后，会挂载 root 文件系统为其提供用户空间支持。
> 对于 Docker 镜像（Image），就相当于是一个 root 文件系统。比如官方镜像 CentOS:7.4 就包含了完整的一套 CentOS 最小系统的 root 文件系统。

> Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

> Docker的镜像实际上由一层一层的文件系统组成，这种层级的文件系统被称为UnionFS。镜像可以基于Dockerfile构建，Dockerfile是一个描述文件，里面包含若干条命令，每条命令都会对基础文件系统创建新的层次结构。严格来说，镜像并非是像一个 ISO 那样的打包文件，镜像只是一个虚拟的概念，其实际体现并非由一个文件组成，而是由一组文件系统组成，或者说，由多层文件系统联合组成。

### 容器
> 镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的 类 和 实例 一样，镜像是静态的定义，容器是镜像运行时的实体。

> Docker容器类似虚拟机，可以支持的操作包括启动，停止，删除等。每个容器间是相互隔离的，容器中会运行特定的应用，包含特定应用的代码及所需的依赖文件。

> 容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 命名空间。因此容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全。

> 可以把容器看做是一个简易版的 Linux 环境（包括root用户权限、进程空间、用户空间和网络空间等）和运行在其中的应用程序。

### 仓库
> 镜像构建完成后，可以很容易的在当前宿主机上运行，但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，Docker Registry 就是这样的服务。

> Docker 仓库是用来包含镜像的位置，Docker提供一个注册服务器（Register）来保存多个仓库，每个仓库又可以包含多个具备不同tag的镜像。Docker运行中使用的默认仓库是 Docker Hub 公共仓库。

> 仓库支持的操作类似git，当用户创建了自己的镜像之后就可以使用 push 命令将它上传到公有或者私有仓库，这样下次在另外一台机器上使用这个镜像时候，只需要从仓库上 pull 下来就可以了。

## 安装Docker
> Docker 有两个版本 CE 和 EE, CE 即社区版（免费，支持周期三个月），EE 即企业版，强调安全，付费使用

> 安装环境 Centos 7

> Docker要求64位的系统且内核版本至少为3.10, 我们可以执行`uname -r`查看系统内核

```shell
$ uname -r

3.10.0-514.21.1.el7.x86_64
```

> 如果系统存在老版本的docker，需要先卸载老版本的docker

```shell
$ sudo yum remove docker \
                  docker-common \
                  docker-selinux \
                  docker-engine
```
> 安装依赖

```shell
$ sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```

> 鉴于国内网络问题，建议使用国内源,执行下面的命令添加 yum 软件源

```shell
# 国内 yum 软件源
$ sudo yum-config-manager \
    --add-repo \
    https://mirrors.ustc.edu.cn/docker-ce/linux/centos/docker-ce.repo

# 官方 yum 软件源
$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

> 这里可以安装最新版的Docker CE，也可以安装测试版的Docker CE

```shell
$ sudo yum-config-manager --enable docker-ce-edge # 安装最新版，这里我们选择最新版

$ sudo yum-config-manager --enable docker-ce-test # 也可以安装测试版
```
> 更新 yum 软件源缓存，并安装 Docker CE

```shell
$ sudo yum makecache fast & yum install docker-ce
```

> 官网还提供其他方式安装可以执行前往查看


[https://docs.docker.com/engine/installation/linux/docker-ce/centos/#install-docker-ce-1](https://docs.docker.com/engine/installation/linux/docker-ce/centos/#install-docker-ce-1)

> 启动 Docker CE

```
$ sudo systemctl start docker # 启动docker

$ sudo systemctl enable docker # 设置docker开机自启
```

> 测试时候安装成功


```shell
$ sudo docker run hello-world
```

> 出现下面画面即安装成功

![](https://i.imgur.com/Mm4lilW.png)

> 建立 docker 用户组： 默认情况下，docker 命令会使用 Unix socket 与 Docker 引擎通讯。而只有 root 用户和 docker 组的用户才可以访问 Docker 引擎的 Unix socket。出于安全考虑，一般 Linux 系统上不会直接使用 root 用户。因此，更好地做法是将需要使用 docker 的用户加入 docker 用户组。

```shell
$ sudo groupadd docker  # 建立 docker 组

$ sudo usermod -aG docker $USER  # 将当前用户加入 docker 组
```

> 可能会遇到开启时提示(我就遇到了...)

```
Failed to start docker.service: Unit not found.
```

> 解决方法：`删除docker，切换成官方源下载`

## 卸载Docker

```shell
$ sudo yum remove docker-ce

$ sudo rm -rf /var/lib/docker
```

## 镜像仓库命令
### login/logout 登陆登出
> docker login : 登陆到一个Docker镜像仓库，如果未指定镜像仓库地址，默认为官方仓库 Docker Hub

> docker logout : 登出一个Docker镜像仓库，如果未指定镜像仓库地址，默认为官方仓库 Docker Hub

> 语法

```
docker login [OPTIONS] [SERVER]

docker login [OPTIONS] [SERVER]
```

> OPTIONS

- `-u` :登陆的用户名
- `-p` :登陆的密码

> DEMO

```
# 登陆到Docker Hub
docker login -u 用户名 -p 密码

# 登出Docker Hub
docker logout
```

### pull 拉取镜像
> docker pull : 从镜像仓库中拉取或者更新指定镜像

> 语法

```
docker pull [OPTIONS] NAME[:TAG|@DIGEST]
```

> OPTIONS

- `-a` :拉取所有 tagged 镜像
- `--disable-content-trust` :忽略镜像的校验,默认开启

### push 上传镜像
> docker push : 将本地的镜像上传到镜像仓库,要先登陆到镜像仓库

> 语法

```
docker push [OPTIONS] NAME[:TAG]
```

> OPTIONS

- `--disable-content-trust` :忽略镜像的校验,默认开启

> DEMO

```
# 上传本地镜像myapache:v1到镜像仓库中。
docker push myapache:v1
```

### search 查找镜像
> docker search : 从Docker Hub查找镜像
> 语法

```
docker search [OPTIONS] TERM
```

> OPTIONS

- `--automated` :只列出 automated build类型的镜像；
- `--no-trunc` :显示完整的镜像描述；
- `-s` :列出收藏数不小于指定值的镜像。

## 本地镜像管理命令
### images 列出本地镜像
> docker images : 列出本地镜像。

> 语法

```
docker images [OPTIONS] [REPOSITORY[:TAG]]
```

> OPTIONS

- `-a` :列出本地所有的镜像（含中间映像层，默认情况下，过滤掉中间映像层）；
- `--digests` :显示镜像的摘要信息；
- `-f` :显示满足条件的镜像；
- `--format` :指定返回值的模板文件；
- `--no-trunc` :显示完整的镜像信息；
- `-q` :只显示镜像ID。

### rmi 删除镜像
> docker rmi : 删除本地一个或多少镜像

> 语法

```
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

> OPTIONS

- `-f` :强制删除；
- `--no-prune` :不移除该镜像的过程镜像，默认移除；

### tag 标记本地镜像
> docker tag : 标记本地镜像，将其归入某一仓库。

> 语法

```
docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
```

> DEMO

```
# 将镜像ubuntu:15.10标记为 runoob/ubuntu:v3 镜像
root@VM_0_5_centos:~# docker tag ubuntu:15.10 runoob/ubuntu:v3
root@VM_0_5_centos:~# docker images   runoob/ubuntu:v3
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
runoob/ubuntu       v3                  4e3b13c8a266        3 months ago        136.3 MB
```

### build 创建镜像
> docker build 命令用于使用 Dockerfile 创建镜像。

> 语法

```
docker build [OPTIONS] PATH | URL | -
```

> OPTIONS

- `--build-arg=[]` :设置镜像创建时的变量；
- `--cpu-shares` :设置 cpu 使用权重；
- `--cpu-period` :限制 CPU CFS周期；
- `--cpu-quota` :限制 CPU CFS配额；
- `--cpuset-cpus` :指定使用的CPU id；
- `--cpuset-mems` :指定使用的内存 id；
- `--disable-content-trust` :忽略校验，默认开启；
- `-f` :指定要使用的Dockerfile路径；
- `--force-rm` :设置镜像过程中删除中间容器；
- `--isolation` :使用容器隔离技术；
- `--label=[]` :设置镜像使用的元数据；
- `-m` :设置内存最大值；
- `--memory-swap` :设置Swap的最大值为内存+swap，"-1"表示不限swap；
- `--no-cache` :创建镜像的过程不使用缓存；
- `--pull` :尝试去更新镜像的新版本；
- `--quiet`, -q :安静模式，成功后只输出镜像 ID；
- `--rm` :设置镜像成功后删除中间容器；
- `--shm-size` :设置/dev/shm的大小，默认值是64M；
- `--ulimit` :Ulimit配置。
- `--tag`, -t: 镜像的名字及标签，通常 name:tag 或者 name 格式；可以在一次构建中为一个镜像设置多个标签。
- `--network`: 默认 default。在构建期间设置RUN指令的网络模式

### history 镜像创建历史
> docker history : 查看指定镜像的创建历史。

> 语法

```
docker history [OPTIONS] IMAGE
```

> OPTIONS

- `-H` :以可读的格式打印镜像大小和日期，默认为true；
- `--no-trunc` :显示完整的提交记录；
- `-q` :仅列出提交记录ID。

> DEMO

```
# 查看本地镜像runoob/ubuntu:v3的创建历史。
root@VM_0_5_centos:~# docker history runoob/ubuntu:v3
IMAGE             CREATED           CREATED BY                                      SIZE      COMMENT
4e3b13c8a266      3 months ago      /bin/sh -c #(nop) CMD ["/bin/bash"]             0 B                 
<missing>         3 months ago      /bin/sh -c sed -i 's/^#\s*\(deb.*universe\)$/   1.863 kB            
<missing>         3 months ago      /bin/sh -c set -xe   && echo '#!/bin/sh' > /u   701 B               
<missing>         3 months ago      /bin/sh -c #(nop) ADD file:43cb048516c6b80f22   136.3 MB
```

### save 镜像保存
> docker save : 将指定镜像保存成 tar 归档文件。

> 语法

```
docker save [OPTIONS] IMAGE [IMAGE...]
```

> OPTIONS

- `-o` :输出到的文件。

### import 导入镜像
> docker import : 从归档文件中创建镜像。

> 语法

```
docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]
```

> OPTIONS

- `-c` :应用docker 指令创建镜像；
- `-m` :提交时的说明文字；

## 容器生命周期管理命令
### run
> docker run ：创建一个新的容器并运行一个命令

> `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`

#### OPTIONS 说明
 - `-a stdin`: 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项；
 - `-d`: 后台运行容器，并返回容器ID；
 - `-i`: 以交互模式运行容器，通常与 -t 同时使用；
 - `-p`: 端口映射，格式为：主机(宿主)端口:容器端口
 - `-t`: 为容器重新分配一个伪输入终端，通常与 -i 同时使用；
 - `--name="nginx-lb"`: 为容器指定一个名称；
 - `--dns 8.8.8.8`: 指定容器使用的DNS服务器，默认和宿主一致；
 - `--dns-search example.com`: 指定容器DNS搜索域名，默认和宿主一致；
 - `-h "mars"`: 指定容器的hostname；
 - `-e username="ritchie"`: 设置环境变量；
 - `--env-file=[]`: 从指定文件读入环境变量；
 - `--cpuset="0-2" or --cpuset="0,1,2"`: 绑定容器到指定CPU运行；
 - `-m `:设置容器使用内存最大值；
 - `--net="bridge"`: 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型；
 - `--link=[]`: 添加链接到另一个容器；
 - `--expose=[]`: 开放一个端口或一组端口；

### start/stop/restart
- docker start :启动一个或多少已经被停止的容器
- docker stop :停止一个运行中的容器
- docker restart :重启容器

> 语法

`docker start [OPTIONS] CONTAINER [CONTAINER...]`

`docker stop [OPTIONS] CONTAINER [CONTAINER...]`

`docker restart [OPTIONS] CONTAINER [CONTAINER...]`

### kill
> docker kill :杀掉一个运行中的容器。

> 语法

`docker kill [OPTIONS] CONTAINER [CONTAINER...]`

> OPTIONS

 - `-s` :向容器发送一个信号

> demo

```
root@VM_0_5_centos:~$ docker kill -s KILL mynginx
mynginx
```
### rm
> docker rm ：删除一个或多少容器


> 语法

`docker rm [OPTIONS] CONTAINER [CONTAINER...]`

> OPTIONS

- `-f` :通过SIGKILL信号强制删除一个运行中的容器
- `-l` :移除容器间的网络连接，而非容器本身
- `-v` :-v 删除与容器关联的卷

### pause/unpause
```
docker pause :暂停容器中所有的进程。
docker unpause :恢复容器中所有的进程。
```
> 语法

`docker pause [OPTIONS] CONTAINER [CONTAINER...]`

`docker unpause [OPTIONS] CONTAINER [CONTAINER...]`

### create
> docker create ：创建一个新的容器但不启动它

> 语法

`docker create [OPTIONS] IMAGE [COMMAND] [ARG...]`

> OPTIONS **同run**

### exec 
> docker exec ：在运行的容器中执行命令

> 语法

`docker exec [OPTIONS] CONTAINER COMMAND [ARG...]`

> OPTIONS

- `-d` :分离模式: 在后台运行
- `-i` :即使没有附加也保持STDIN 打开
- `-t` :分配一个伪终端

## 容器操作命令
### ps 列出容器
> docker ps : 列出容器

> 语法

`docker ps [OPTIONS]`

> OPTIONS

- `-a` :显示所有的容器，包括未运行的。
- `-f` :根据条件过滤显示的内容。
- `--format` :指定返回值的模板文件。
- `-l` :显示最近创建的容器。
- `-n` :列出最近创建的n个容器。
- `--no-trunc` :不截断输出。
- `-q` :静默模式，只显示容器编号。
- `-s` :显示总的文件大小。
### inspect 获取容器/镜像的元数据
> docker inspect : 获取容器/镜像的元数据。

> 语法

`docker inspect [OPTIONS] NAME|ID [NAME|ID...]`

> OPTIONS

- `-f` :指定返回值的模板文件。
- `-s` :显示总的文件大小。
- `--type` :为指定类型返回JSON。

> DEMO

```
# 获取镜像mysql:5.6的元信息。
root@VM_0_5_centos:~$ docker inspect mysql:5.6
[
    {
        "Id": "sha256:2c0964ec182ae9a045f866bbc2553087f6e42bfc16074a74fb820af235f070ec",
        "RepoTags": [
            "mysql:5.6"
        ],
        "RepoDigests": [],
        "Parent": "",
        "Comment": "",
        "Created": "2016-05-24T04:01:41.168371815Z",
        "Container": "e0924bc460ff97787f34610115e9363e6363b30b8efa406e28eb495ab199ca54",
        "ContainerConfig": {
            "Hostname": "b0cf605c7757",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "3306/tcp": {}
            },
...
```
```
# 获取正在运行的容器mymysql的 IP。
root@VM_0_5_centos:~$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mymysql
172.17.0.3
```
### top 查看容器中运行的进程信息
> docker top :查看容器中运行的进程信息，支持 ps 命令参数。

> 语法

`docker top [OPTIONS] CONTAINER [ps OPTIONS]`

> DEMO

```
# 查看容器mymysql的进程信息
root@VM_0_5_centos:~/mysql$ docker top mymysql
UID    PID    PPID    C      STIME   TTY  TIME       CMD
999    40347  40331   18     00:58   ?    00:00:02   mysqld
```

### attach 连接到正在运行中的容器
> docker attach :连接到正在运行中的容器。

> 语法

`docker attach [OPTIONS] CONTAINER`

> 要attach上去的容器必须正在运行，可以同时连接上同一个container来共享屏幕（与screen命令的attach类似）。
官方文档中说attach后可以通过CTRL-C来detach，但实际上经过我的测试，如果container当前在运行bash，CTRL-C自然是当前行的输入，没有退出；如果container当前正在前台运行进程，如输出nginx的access.log日志，CTRL-C不仅会导致退出容器，而且还stop了。这不是我们想要的，detach的意思按理应该是脱离容器终端，但容器依然运行。好在attach是可以带上`--sig-proxy=false`来确保CTRL-D或CTRL-C不会关闭容器。

> demo

```
# 容器mynginx将访问日志指到标准输出，连接到容器查看访问信息。
root@VM_0_5_centos:~$ docker attach --sig-proxy=false mynginx
192.168.239.1 - - [10/Jul/2016:16:54:26 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36" "-"
```

### events 从服务器获取实时事件
> docker events : 从服务器获取实时事件

> 语法

`docker events [OPTIONS]`

> OPTIONS

- -f ：根据条件过滤事件；
- --since ：从指定的时间戳后显示所有事件;
- --until ：流水时间显示到指定的时间为止；

> DEMO

```
# 显示docker 2016年7月1日后的所有事件。
root@VM_0_5_centos:~/mysql$ docker events  --since="1467302400"
2016-07-08T19:44:54.501277677+08:00 network connect 66f958fd13dc4314ad20034e576d5c5eba72e0849dcc38ad9e8436314a4149d4 (container=b8573233d675705df8c89796a2c2687cd8e36e03646457a15fb51022db440e64, name=bridge, type=bridge)
2016-07-08T19:44:54.723876221+08:00 container start b8573233d675705df8c89796a2c2687cd8e36e03646457a15fb51022db440e64 (image=nginx:latest, name=elegant_albattani)
2016-07-08T19:44:54.726110498+08:00 container resize b8573233d675705df8c89796a2c2687cd8e36e03646457a15fb51022db440e64 (height=39, image=nginx:latest, name=elegant_albattani, width=167)
2016-07-08T19:46:22.137250899+08:00 container die b8573233d675705df8c89796a2c2687cd8e36e03646457a15fb51022db440e64 (exitCode=0, image=nginx:latest, name=elegant_albattani)
...
```
```
# 显示docker 镜像为mysql:5.6 2016年7月1日后的相关事件。
root@VM_0_5_centos:~/mysql$ docker events -f "image"="mysql:5.6" --since="1467302400" 
2016-07-11T00:38:53.975174837+08:00 container start 96f7f14e99ab9d2f60943a50be23035eda1623782cc5f930411bbea407a2bb10 (image=mysql:5.6, name=mymysql)
2016-07-11T00:51:17.022572452+08:00 container kill 96f7f14e99ab9d2f60943a50be23035eda1623782cc5f930411bbea407a2bb10 (image=mysql:5.6, name=mymysql, signal=9)
2016-07-11T00:51:17.132532080+08:00 container die 96f7f14e99ab9d2f60943a50be23035eda1623782cc5f930411bbea407a2bb10 (exitCode=137, image=mysql:5.6, name=mymysql)
2016-07-11T00:51:17.514661357+08:00 container destroy 96f7f14e99ab9d2f60943a50be23035eda1623782cc5f930411bbea407a2bb10 (image=mysql:5.6, name=mymysql)
2016-07-11T00:57:18.551984549+08:00 container create c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (image=mysql:5.6, name=mymysql)
2016-07-11T00:57:18.557405864+08:00 container attach c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (image=mysql:5.6, name=mymysql)
2016-07-11T00:57:18.844134112+08:00 container start c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (image=mysql:5.6, name=mymysql)
2016-07-11T00:57:19.140141428+08:00 container die c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (exitCode=1, image=mysql:5.6, name=mymysql)
2016-07-11T00:58:05.941019136+08:00 container destroy c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (image=mysql:5.6, name=mymysql)
2016-07-11T00:58:07.965128417+08:00 container create a404c6c174a21c52f199cfce476e041074ab020453c7df2a13a7869b48f2f37e (image=mysql:5.6, name=mymysql)
2016-07-11T00:58:08.188734598+08:00 container start a404c6c174a21c52f199cfce476e041074ab020453c7df2a13a7869b48f2f37e (image=mysql:5.6, name=mymysql)
2016-07-11T00:58:20.010876777+08:00 container top a404c6c174a21c52f199cfce476e041074ab020453c7df2a13a7869b48f2f37e (image=mysql:5.6, name=mymysql)
2016-07-11T01:06:01.395365098+08:00 container top a404c6c174a21c52f199cfce476e041074ab020453c7df2a13a7869b48f2f37e (image=mysql:5.6, name=mymysql)
```

### logs 日志
> docker logs : 获取容器的日志

> 语法

`docker logs [OPTIONS] CONTAINER`

> OPTIONS

- `-f` : 跟踪日志输出
- `--since` :显示某个开始时间的所有日志
- `-t` : 显示时间戳
- `--tail` :仅列出最新N条容器日志

### wait 阻塞运行直到容器停止
> docker wait : 阻塞运行直到容器停止，然后打印出它的退出代码。

> 语法

`docker wait [OPTIONS] CONTAINER [CONTAINER...]`

> demo

`docker wait CONTAINER`

### export
> docker export :将文件系统作为一个tar归档文件导出到STDOUT。

> 语法

`docker export [OPTIONS] CONTAINER`

> OPTIONS

- `-o` :将输入内容写到文件。

> DEMO

```
# 将id为a404c6c174a2的容器按日期保存为tar文件。
root@VM_0_5_centos:~$ docker export -o mysql-`date +%Y%m%d`.tar a404c6c174a2
root@VM_0_5_centos:~$ ls mysql-`date +%Y%m%d`.tar
mysql-20160711.tar
```

### port 查看容器的端口映射、
> docker port :列出指定的容器的端口映射，或者查找将PRIVATE_PORT NAT到面向公众的端口。

> 语法

`docker port [OPTIONS] CONTAINER [PRIVATE_PORT[/PROTO]]`

> 实例

```
# 查看容器mynginx的端口映射情况。
root@VM_0_5_centos:~$ docker port mymysql
3306/tcp -> 0.0.0.0:3306
```

## 容器rootfs命令
### commit 
> docker commit :从容器创建一个新的镜像。

> 语法

```
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```

> OPTIONS

- `-a` :提交的镜像作者；
- `-c` :使用Dockerfile指令来创建镜像；
- `-m` :提交时的说明文字；
- `-p` :在commit时，将容器暂停。

### cp 拷贝数据
> docker cp :用于容器与主机之间的数据拷贝。

> 语法

```
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-

docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH
```

> OPTIONS

- `-L` :保持源目标中的链接

> DEMO

```
# 将主机/www/runoob目录拷贝到容器96f7f14e99ab的/www目录下。
docker cp /www/runoob 96f7f14e99ab:/www/

# 将主机/www/runoob目录拷贝到容器96f7f14e99ab中，目录重命名为www。
docker cp /www/runoob 96f7f14e99ab:/www

# 将容器96f7f14e99ab的/www目录拷贝到主机的/tmp目录中。
docker cp  96f7f14e99ab:/www /tmp/
```

### diff 检查容器里文件结构的更改
> docker diff : 检查容器里文件结构的更改。

> 语法

```
docker diff [OPTIONS] CONTAINER
```

> DEMO

```
# 查看容器mymysql的文件结构更改
root@VM_0_5_centos:~$ docker diff mymysql
A /logs
A /mysql_data
C /run
C /run/mysqld
A /run/mysqld/mysqld.pid
A /run/mysqld/mysqld.sock
C /tmp
```