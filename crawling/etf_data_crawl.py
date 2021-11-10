import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
input = 'QQQ'
url = 'https://www.etf.com/'
result_url = url+input
# url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'
headers = {
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

response = requests.get(result_url, headers=headers, verify=False)

print("requests header :",response.headers)
soup = BeautifulSoup(response.text, "html.parser")

print("requests find by div class name :",soup.find('div',attrs={'class':'field-content fundReportSegment'}))
tags1 = soup.find('div',attrs={'class':'field-content fundReportSegment'}).find("a").get_text()
print("requests find by div class name and 'a' tag :",tags1)
