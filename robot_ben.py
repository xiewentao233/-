# -*- coding: utf-8 -*-
import werobot
import requests
robot = werobot.WeRoBot(token='xiewentao2018')
robot.config["APP_ID"] = "wxd89365e4ddcc7c48"
robot.config["APP_SECRET"] = "6a41b3d0889bc09ff104f4ce5602adeb"


@robot.handler
# def hello(message):
#     return 'Hello World!'


@robot.key_click("handbook")
def music(message):
    return "这个是新员工入职文档，并不是空乘手机号，文档还未更新"
#
# @robot.location
# def location(message):
#     location_x = str(round(message.location[0], 3))
#     location_y = str(round(message.location[1], 3))
#     location = location_x + ',' + location_y
#     return weather_today(location)
#
# def weather_today(location):
#     try:
#         response = requests.get(WEATHER_API1, params={
#             'key': WEATHER_KEY,
#             'location': location
#         }, timeout=1)
#         json_data = response.json()
#         city = ''
#         arr = json_data['HeWeather6'][0]
#         if arr["status"] != "ok":
#             return_str = ''
#             if arr['status'] == 'unknown city':
#                 return_str = '未知或错误城市/地区'
#             if arr['status'] == 'no data for this location':
#                 return_str = '该城市/地区没有你所请求的数据'
#             if arr['status'] == 'no more requests':
#                 return_str = '超过访问次数，需要等到当月最后一天24点后进行访问次数的重置或升级你的访问量'
#             if return_str == '':
#                 return_str = '其他错误，请联系管理员'
#             return return_str
#         if 'parent_city' not in arr['basic'] or arr['basic']['parent_city'] == arr['basic']['location']:
#             loc = arr['basic']['location']
#             city = loc
#         else:
#             loc = arr['basic']['parent_city'] + arr['basic']['location']
#             city = arr['basic']['parent_city']
#         result = '%s今日天气\n' % loc
#         result += '———————————————\n'
#         forcast_arr = arr['daily_forecast'][0]
#         result += '温度：%s℃～%s℃(实况:%s℃)\n' % (forcast_arr['tmp_max'], forcast_arr['tmp_min'], arr['now']['tmp'])
#         if forcast_arr['cond_txt_d'] == forcast_arr['cond_txt_n']:
#             result += '天气：%s(实况:%s)\n' % (forcast_arr['cond_txt_d'], arr['now']['cond_txt'])
#         else:
#             result += '天气：%s转%s\n(实况:%s)\n' % (forcast_arr['cond_txt_d'], forcast_arr['cond_txt_n'], arr['now']['cond_txt'])
#         result += '风向：%s\n风力：%s\n' % (forcast_arr['wind_dir'], forcast_arr['wind_sc'])
#         result += '相对湿度：%s%%\n降水概率：%s%%\n' % (forcast_arr['hum'], forcast_arr['pop'])
#         result += '紫外线强度指数：%s\n' % forcast_arr['uv_index']
#
#         response = requests.get(WEATHER_API3, params={
#             'key': WEATHER_KEY,
#             'location': city
#         }, timeout=1)
#         json_data = response.json()
#         if json_data['HeWeather6'][0]['status'] == 'ok':
#             air = json_data['HeWeather6'][0]['air_now_city']['qlty']
#             result += '空气质量：%s\n' % air
#
#         if 'lifestyle' in arr:
#             result += '\n生活指数\n'
#             for i in range(7):
#                 type = DICT_TYPE[arr['lifestyle'][i]['type']]
#                 result += '%s：%s\n' % (type, arr['lifestyle'][i]['brf'])
#         result += '———————————————'
#         return result
#     except:
#         return '系统繁忙或出错，请重试'



# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
