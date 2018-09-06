import json
import codecs

import requests


def read_jsonp(jsonp, callback=None):
    if callback is None:
        _jsonp_begin = jsonp[:jsonp.index('(') + 1]
    else:
        _jsonp_begin = callback + '('
    _jsonp_end = ')'
    jsonp = jsonp.strip()
    if not jsonp.startswith(_jsonp_begin) or not jsonp.endswith(_jsonp_end):
        raise ValueError("Invalid Jsonp")
    return json.loads(jsonp[len(_jsonp_begin):-len(_jsonp_end)])


with codecs.open('c://test.txt', 'w', 'utf-8') as f:
    json.dump(read_jsonp('callback({"a":"中文"})'), f, ensure_ascii=False)


def get_school_geo(school_name):
    payload = {'address': school_name, 'output': 'json', 'ak': 'Y7DhSblHhABx2YQE6v6ihd9O7q88GLz5', 'callback': 'showLocation'}
    url = "http://api.map.baidu.com/geocoder/v2/"
    r = requests.get(url, payload)
    school_geo_original = r.text
    print(school_geo_original)


get_school_geo("四川大学")
