# -*- coding:utf-8 -*-


# 利用SAX编写程序解析Yahoo的XML格式的天气预报，获取当天和第二天的天气


from xml.parsers.expat import ParserCreate


class WeatherSaxHandler(object):
    def __init__(self):
        self.db = {'yweather:forecast': {}}
        self.count = 0

    def start_element(self, name, attrs):

        if name == 'yweather:location':
            self.db['yweather:location'] = attrs

        if name == 'yweather:forecast':
            self.count += 1
            self.db['yweather:forecast'][self.count] = attrs   # db['yweather:forecast']也是一个字典


def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml)
    result = {"today": {}, "tomorrow": {}, "city": handler.db['yweather:location']['city'], "country": handler.db['yweather:location']['country']}
    result["today"]["low"] = int(handler.db['yweather:forecast'][1]['low'])
    result["today"]["text"] = handler.db['yweather:forecast'][1]['text']
    result["today"]["high"] = int(handler.db['yweather:forecast'][1]['high'])
    result["tomorrow"]["low"] = int(handler.db['yweather:forecast'][2]['low'])
    result["tomorrow"]["text"] = handler.db['yweather:forecast'][2]['text']
    result["tomorrow"]["high"] = int(handler.db['yweather:forecast'][2]['high'])
    return result


# 测试:
data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
weather = parse_weather(data)
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == 20, weather['today']['low']
assert weather['today']['high'] == 33, weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
print('Weather:', str(weather))