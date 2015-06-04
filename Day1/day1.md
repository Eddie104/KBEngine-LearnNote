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
