# -*- coding: utf-8 -*-
import werobot

robot = werobot.WeRoBot(token='xiewentao2018')
robot.config["APP_ID"] = "wxd89365e4ddcc7c48"
robot.config["APP_SECRET"] = "6a41b3d0889bc09ff104f4ce5602adeb"


@robot.handler
def hello(message):
    return 'Hello World!'


# def echo(message1):
#    return 'Hello World2!'
# robot.add_handler(echo)

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()

# route() 可以将一个函数与一个URL进行绑定，在上面的示例中，route 将 “/hello/:name’ 这个URL地址绑定到了 “index(name = ‘World’)” 这个函数上https://blog.csdn.net/huithe/article/details/8087645
'''
def test_text():
    @werobot.text
    def text(message):
        return '普通的Text喵'

    message = parse_user_msg("""
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[this is a test]]></Content>
            <MsgId>1234567890123456</MsgId>
        </xml>
        """)

    reply = werobot.get_reply(message)

    assert isinstance(reply, TextReply)
    assert reply._args['content'] == u'普通的Text喵'

from werobot import WeRoBot
robot = WeRoBot(token = "xiewentao2018")
robot.config["APP_ID"]=""
robot.config["APP_APP_SECRE"]=""
'''