2015-6-3:

	http://kbengine.org/docs/configuration/entities.html
	http://kbengine.org/docs/programming/entitydef.html

	疑问：定义Entity的时候




	 客户端调了loginGateway以后base服务器就会创建account实体，创建完以后生成一个mailbox，然后调用客户端的onCreatedProxies方法，通知客户端创建account的客户端部分
	 同时服务器上account.py的onEntitiesEnabled函数也会被调用，表示account的客户端部分也创建好了，服务器逻辑层可以撸起来了



	 cellapp与cell关系:
	 	cell是space（一个空间/场景）的一部分或者全部(由动态分割算法决定)。
	 	cellapp是一个进程，所有的space-cell都创建在cellapp进程中

	 	玩家的cell部分指的就是玩家在space-cell中对应的实体。

	 	实体在不同cell中迁移， 有2个原因
			第一个，由引擎动态负载均衡导致的迁移。
			第二， 玩家移动导致跨越到另一个cell中



	http://bbs.chinaunix.net/thread-2030722-1-1.html
服务端：考虑到服务端重启或多宿，为socket设置SO_REUSEADDR基本成为一个定律
客户端：客户端很少有必要bind端口，不bind时内核自动为你分配可用的端口
		每个客户端都对应服务端的一个proxy， 这个proxy在进游戏后由于demo逻辑的做法他是一个account实体， 能让玩家在客户端选角色。 当玩家选完角色之后在服务端demo逻辑中会切换与客户端绑定的proxy，所以在玩家进入场景中时他是avatar。
		有一些游戏也不需要按照这个逻辑写， 例如：登入游戏之后的这个account实体本身就是一个avatar， 不需要选择角色。
		这些概念你需要理解基本之后才能灵活运用。 看看文档以及demo中的proxy是什么，如何切换控制权给另一个proxy。

		self.client这个属性是一个maibox， 只能通过这个mailbox调用在def中定义的clientMethods方法。
		mailbox在底层包含了ip地址与实体的id， 当你调用某个正确的方法后， 底层会将方法参数等信息打包并带上实体的id，在客户端根据实体的id调用到某个方法。

	Volatile

账号登录的时候创建了一个proxy,然后选择角色进入游戏的时候又创建了一个proxy，不是说一个客户端就对应一个proxy？

avatar是proxy，服务器跟任何一个客户端之间同时只能存在一个proxy



当分布式的avatar需要存储时， baseapp先请求从cellapp获得数据放入base.cellData， 然后将所有持久化类型属性数据打包到dbmgr执行写入


引擎架构设计上baseApp, cellApp的区别
http://bbs.kbengine.org/forum.php?mod=viewthread&tid=69&highlight=baseApp


#0基础学KBEngine基础学习笔记之一

做了一段时间U3D客户端，总想着接触一些服务器知识。于是搜了一下开源服务器框架，准备折腾一下KBEngine。

本人习惯接触一样新技术的时候就做一些笔记，很多时候做完就留着当备份，有空拿出来看看。因为写的烂，再说这些东西你影撸几遍代码也肯定搞的定了。

但是这次我决定分享出来贡献自己的一份力量。因为我发现KBEngine这个服务器引擎一个很纠结的问题。

不同于很多开源项目，KBEngine（以下简称KB）并没有那些 quick start 之类的东西，官网上的很多文档更类似与参考手册，这也许让很多慕名而来的人学个一两天就望而却步了。

当然或许从某种程度上说也算是一种考验，毕竟开源的东西你还要求这要求那也过分了。

废话不扯。开始正题，本人水平有限，发现问题欢迎各位喷我。

本篇只是开头，说句实话我目前了解的也不多，顶多能挤多少算多少。不定时更新。

在读这篇文章之前，请各位自定搭建运行好u3d demo。


##了解服务器运行的一些抽象概念

首先了解一个概念，entity（实体），什么是实体，实体就是服务器所有东西的基类。

举个例子，你玩家登陆后，如果是个RPG游戏，你的新手村是个实体，你周围的NPC也是一个个实体，然后你自己当然也是个实体等等。

既然是实体，我们就需要交互，在交互之前，我们要了解一下谁负责我们实体数据的生命周期。

我目前浅薄的了解了一下，参考了下面这张图：

![1.png](E:/KBEngine-LearnNote/Day1/1.png)

在这上面有很多app进程，loginapp 负责登录请求的转发，bassapp 负责实体的 base 部分，cellapp 负责实体的 cell 部分（一般来说就是空间部分的数据）

很明显我们实体的数据被不同的进程拆分了，举个例子说，玩家的背包数据是baseapp的 base 部分，在baseapp这个进程上被维护。同理，玩家的空间坐标是cellapp的 cell部分，在cellapp上被维护。

很好, 目前我们大略的讲了一下实体的生命维护，那么我们的交互呢？

首先，我们可以看到，一个实体上的数据虽然被拆分了，但是这些数据依旧是一个实体的，只是由不同进程维护（好像是废话）。

KB给这些被拆分的实体每一个都配了 mailbox 用于和自己实体的其他部分 或者其他实体，或者周围实体等等进行交互。(也就是所谓数据的作用域)

从某种程度上说隐藏了那些消息拆包，事件分发的机制。但实际上底层还是一样的。

目前就这些，接下类就是枯燥的通信流程了。




