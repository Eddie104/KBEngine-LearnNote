#0基础学KBEngine基础学习笔记之二

紧接着上一篇，上一篇KBE老大指出我对实体的概念有所欠缺，目前我也没有什么新的感悟，也只有期待之后的研究的时候灵感昙花一现了。

其实很多东西就是临门一脚，如果你看明白了我上一篇的一些概念，接下来有能力的人老早在我写这篇文章之前跑通流程，在写自己的逻辑了。

顺便提个建议，论坛发帖是否可以支持 markdown ？


##接下来我们从零开始走通一下通信流程：

1.下载服务器模板 [minimum_project](http://kbengine.org/cn/docs/documentations/minimum_project.html),	解压 to your %KBE_ROOT% folder，然后重命名kbengine_my_assets。点击目录下的start_server.bat。

![2.png](D:/KBEngine-LearnNote/Notes/Pics/2.png)

![3.png](D:/KBEngine-LearnNote/Notes/Pics/3.png)

2.打开之前我们跑通的 kbengine_unity3d_demo, 再导入一个NGUI插件，如下建立一个场景。

![4.png](D:/KBEngine-LearnNote/Notes/Pics/4.png)

关于地址和端口的设置默认在 %KBE_ROOT%kbe/res/server/kbengine_defs.xml下

![5.png](D:/KBEngine-LearnNote/Notes/Pics/5.png)

如果你需要改变引擎设置, 请在({assets}/res/server/kbengine.xml)中覆盖kbe/res/server/[kbengine_defs.xml]的对应参数来修改, 这样的好处是不会破坏引擎的默认设置，在你更新引擎时也不会产生冲突，以及在多个逻辑项目时不会影响到其他的项目设置。

3.点击启动，你会发现一堆log，主要是一些初始化工作，我们先暂时跳过。Ngui 建立一个登陆界面如下：

4.


**参考**
[官网](http://kbengine.org/docs/)
[KBEngine简单RPG-Demo源码解析](http://bbs.kbengine.org/forum.php?mod=viewthread&tid=166&highlight=RPG)


