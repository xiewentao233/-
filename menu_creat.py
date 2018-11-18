import werobot

robot = werobot.WeRoBot(token='xiewentao2018')
robot.config["APP_ID"] = "wxd89365e4ddcc7c48"
robot.config["APP_SECRET"] = "6a41b3d0889bc09ff104f4ce5602adeb"
robot.client.delete_menu(
    {
        "button":
            [
                {
                    "type": "click",
                    "name": "空乘手机号",
                    "key": "handbook"
                },
                {
                    "name": "地服续命",
                    "sub_button":
                        [
                            {
                                "type": "view",
                                "name": "值机",
                                "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                            },
                            {
                                "type": "view",
                                "name": "候机",
                                "url": "http://www.baidu.com"
                            },
                            {
                                "type": "view",
                                "name": "贵宾室",
                                "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                            }
                        ]
                }
            ]
    }
)
