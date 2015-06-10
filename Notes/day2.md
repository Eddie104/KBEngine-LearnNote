#0基础学KBEngine基础学习笔记之二

紧接着上一篇，上一篇KBE老大指出我对实体的概念有所欠缺，目前我也没有什么新的感悟，也只有期待之后的研究的时候灵感昙花一现了。

其实很多东西就是临门一脚，如果你看明白了我上一篇的一些概念，接下来有能力的人老早在我写这篇文章之前跑通流程，在写自己的逻辑了。

顺便提个建议，论坛发帖是否可以支持 markdown ？


##接下来我们从零开始走通一下通信流程：

1.下载服务器模板 [minimum_project](http://kbengine.org/cn/docs/documentations/minimum_project.html),  解压 to your %KBE_ROOT% folder，然后重命名kbengine_my_assets。点击目录下的start_server.bat。

![2.png](E:/KBEngine-LearnNote/Notes/Pics/2.png)

![3.png](E:/KBEngine-LearnNote/Notes/Pics/3.png)

2.打开之前我们跑通的 kbengine_unity3d_demo, 再导入一个NGUI插件，如下建立一个场景。

![4.png](E:/KBEngine-LearnNote/Notes/Pics/4.png)

关于地址和端口的设置默认在 %KBE_ROOT%kbe/res/server/kbengine_defs.xml下

![5.png](E:/KBEngine-LearnNote/Notes/Pics/5.png)

如果你需要改变引擎设置, 请在({assets}/res/server/kbengine.xml)中覆盖kbe/res/server/[kbengine_defs.xml]的对应参数来修改, 这样的好处是不会破坏引擎的默认设置，在你更新引擎时也不会产生冲突，以及在多个逻辑项目时不会影响到其他的项目设置。

3.点击启动，你会发现一堆log，主要是一些初始化工作，我们先暂时跳过。Ngui 建立一个登陆界面如下：

![6.png](E:/KBEngine-LearnNote/Notes/Pics/6.png)

简单的控制脚本代码

	using KBEngine;
	using UnityEngine;
	using System;
	using System.IO;
	using System.Collections;
	using System.Collections.Generic;
	using System.Linq;

	public class LoginPanelHandler : MonoBehaviour {

	    public UIInput inPut_Name;
	    public UIInput inPut_PassWord;

	    public UIButton btn_Login;
	    public UIButton btn_Register;

	    public string stringAccount { get { return inPut_Name.value; } }
	    public string stringPasswd { get { return inPut_PassWord.value; } }


	    void Start()
	    {
	       EventDelegate.Add(btn_Login.onClick,btn_Login_OnClick);
	       EventDelegate.Add(btn_Register.onClick, btn_Register_OnClick);

	       KBEngine.Event.registerOut("onCreateAccountResult", this, "onCreateAccountResult");
	       KBEngine.Event.registerOut("onLoginSuccessfully", this, "onLoginSuccessfully");
	    }
	}


创建账号:

	public void btn_Register_OnClick()
	{
		Debug.Log("LoginPanelHandler => "+"Register ::"+"stringAccount:" + stringAccount + "stringPasswd:" + stringPasswd);

		KBEngine.Event.fireIn("createAccount", stringAccount, stringPasswd, System.Text.Encoding.UTF8.GetBytes("kbengine_unity3d_demo"));
	}
	public void onCreateAccountResult(UInt16 retcode, byte[] datas)
	{
		if (retcode != 0)
		{
		    Debug.LogError("createAccount is error(注册账号错误)! err=" + KBEngineApp.app.serverErr(retcode));
		    return;
		}

		if (KBEngineApp.validEmail(stringAccount))
		{
		    Debug.LogError("createAccount is successfully, Please activate your Email!(注册账号成功，请激活Email!)");
		}
		else
		{
		    Debug.LogError("createAccount is successfully!(注册账号成功!)");
		}
	}

登录账号:

    public void btn_Login_OnClick()
    {
        Debug.Log(" LoginPanelHandler =>" + "Login ::" + "stringAccount:" + stringAccount + "stringPasswd:" + stringPasswd);

        if (stringAccount.Length > 0 && stringPasswd.Length > 5)
        {
            KBEngine.Event.fireIn("login", inPut_Name.value, stringPasswd, System.Text.Encoding.UTF8.GetBytes("kbengine_unity3d_demo"));
        }
        else
        {
            Debug.LogError("account or password is error, length < 6!(账号或者密码错误，长度必须大于5!)");
        }
    }

    public void onLoginSuccessfully(UInt64 rndUUID, Int32 eid, Account accountEntity)
    {
        Debug.Log("login is successfully!(登陆成功!)");
    }


关于账号的创建登录流程我就简单说明一下,我们主要还是考虑实现一下登录之后的简单通信。
具体可以参考下方的 **KBEngine简单RPG-Demo源码解析** 参考链接

总之就是你创建账号后登录，

loginApp处理登录转发, 客户端接收 "KBEngine::Client_onLoginSuccessfully:", 

然后baseApp处理登录请求，baseApp 建立第一个 Account 实体，客户端接收 "KBEngine::Client_onCreatedProxies"。client 建立第一个 Account 实体, 调用 __init__()。（__init__ 这个函数在Python中表示构造函数，所以 c# 也要调用一下）

(ps: Account.cs 中注释掉 baseCall("reqAvatarList");)

	public override void __init__()
	{
		Event.fireOut("onLoginSuccessfully", new object[]{KBEngineApp.app.entity_uuid, id, this});
	    //baseCall("reqAvatarList");
	}


4.第一个实体通信

很好，按照上一篇幅的说法，baseApp 和 client 都有了 同一个 Account 实体, 只是在不同进程维护。

然后我们请求一下 Account 的 Avatar 列表, 其实我刚开始挺纠结 Avatar 是定义为实体 还是定义为Account的base数据。参考官方的Demo是定义为实体，然后替换 Acoount 成为新的 client 实体。

流程如下：

*　定义Avatar实体

*　实现Account base 请求角色列表方法

*　实现Account client 建立角色 和 回应角色方法

![7.png](E:/KBEngine-LearnNote/Notes/Pics/7.png)



**参考**
[官网](http://kbengine.org/docs/)
[KBEngine简单RPG-Demo源码解析](http://bbs.kbengine.org/forum.php?mod=viewthread&tid=166&highlight=RPG)






