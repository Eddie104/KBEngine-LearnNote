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

       //listen CreateAccount callBack
       //KBEngine.Event.registerOut("onCreateAccountResult", this, "onCreateAccountResult");
       KBEngine.Event.registerOut("onLoginSuccessfully", this, "onLoginSuccessfully");
    }

    public void btn_Register_OnClick()
    {
        Debug.Log("LoginPanelHandler => "+"Register ::"+"stringAccount:" + stringAccount + "stringPasswd:" + stringPasswd);

        KBEngine.Event.fireIn("createAccount", stringAccount, stringPasswd, System.Text.Encoding.UTF8.GetBytes("kbengine_unity3d_demo"));
    }
    //public void onCreateAccountResult(UInt16 retcode, byte[] datas)
    //{
    //    if (retcode != 0)
    //    {
    //        Debug.LogError("createAccount is error(注册账号错误)! err=" + KBEngineApp.app.serverErr(retcode));
    //        return;
    //    }

    //    if (KBEngineApp.validEmail(stringAccount))
    //    {
    //        Debug.LogError("createAccount is successfully, Please activate your Email!(注册账号成功，请激活Email!)");
    //    }
    //    else
    //    {
    //        Debug.LogError("createAccount is successfully!(注册账号成功!)");
    //    }
    //}


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

    void OnGUI()
    {
        if (GUI.Button(new Rect(10, 10, 150, 100), "reqCreateAvatar"))
        {
            Account account = (Account)KBEngineApp.app.player();
            account.reqCreateAvatar(1, "haha");
        }
    }
}
