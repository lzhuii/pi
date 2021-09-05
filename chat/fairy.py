import json

import requests

# 企业ID
corpid = ""
# 应用密钥
corpsecret = ""
# 应用ID
agent_id = 1
# 消息接收者
touser = ""
# 获取access_token的API地址
api_gettoken = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
# 发送消息API
api_send = "https://qyapi.weixin.qq.com/cgi-bin/message/send"


def get_token():
    res = requests.get(api_gettoken + "?corpid=" + corpid + "&corpsecret=" + corpsecret)
    print(res.json())
    return res.json()['access_token']


def send_msg():
    access_token = get_token()
    params = {
        "touser": touser,
        "msgtype": "text",
        "agentid": agent_id,
        "text": {
            "content": "想你"
        },
        "safe": 0
    }
    res = requests.post(api_send + "?access_token=" + access_token, data=json.dumps(params))
    print(res.text)