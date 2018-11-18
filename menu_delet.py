import werobot

robot = werobot.WeRoBot(token='xiewentao2018')
robot.config["APP_ID"] = "wxd89365e4ddcc7c48"
robot.config["APP_SECRET"] = "6a41b3d0889bc09ff104f4ce5602adeb"
robot.client.delete_menu()