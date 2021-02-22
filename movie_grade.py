# Python 샘플 코드 #
import requests
import json
import urllib.parse

url = 'http://open.kmrb.or.kr/openapi-data/service/MvResultService/mvResult'
queryParams = '?'

payload = urllib.parse.urlencode({
	'ServiceKey' : 'OL7rcMhk2w4AgCM7Zau7Nie36dskX1KKC9HVxqaNDsrQKwr6HLLaaEESU63tlhghUvlQeYj0YVGBgFiJarWXzw%3D%3D',
	'pageNo' : '1',
	'numOfRows' : '2',
	'title' : '1987',
	'rtNo' : '2017-MF02149',
	'aplcName' : '주식회사 우정필름'
})

res = requests.get(url + queryParams)
res_json = res.json()
print(res_json)