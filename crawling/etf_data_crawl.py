import requests
from bs4 import BeautifulSoup
import urllib3

# warnings error 메세지르 안보여주는 것
urllib3.disable_warnings()

#
input = 'VOO'

url = 'https://www.etf.com/'
result_url = url+input
# url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'
headers = {
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

# 503 error -> header의 User-Agent 추가 필요
# 500 error -> header와 parameter 추가 필요?

response = requests.get(result_url, headers=headers, verify=False)
soup = BeautifulSoup(response.text, "html.parser")
# class 명으로 검색해서 a 코드 사이에 있는 text 가져오기
tags1 = soup.find('div', attrs={'class':'field-content fundReportSegment'}).find("a").get_text()
# 동일한 class 명에서 id로 구분되어있는 것의 a 코드 사이에 있는 text 가져오
tags2 = soup.find('div', id='fundIndexData').find("a").get_text()
print("ETF.com segment:",tags1)
print("Index Tracked:",tags2)
# print(soup.find('div', id='fundIndexData').find("a").get_text())



#
# print("requests header :",response.headers)
# soup = BeautifulSoup(response.text, "html.parser")
# # print("requests find by div class name :",soup.find('div',attrs={'class':'field-content fundReportSegment'}))
# #class="generalData col-md-12 no-padding 0 pull-left col-xs-12 col-sm-12"
# # print("requests find by div class name :",soup.find('div',attrs={'class':"generalData col-md-12 no-padding 0 pull-left col-xs-12 col-sm-12"}))
# print(soup.find('div', id='fundIndexData').find("a").get_text)
# tags1 = soup.find('div',attrs={'class':'field-content fundReportSegment'}).find("a").get_text()
# tags1 = soup.find('div',attrs={'class':'field-content fundReportSegment'}).find('section',attrs={'class':'generalDataBox', 'id':'fundIndexData'})
# print("requests find by div class name and 'a' tag :",tags1)
# print(tags1)