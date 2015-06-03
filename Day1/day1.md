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