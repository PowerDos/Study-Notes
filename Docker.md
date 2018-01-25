# Docker
> 部分总结来自网络


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