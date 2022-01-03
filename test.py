import requests
from bs4 import BeautifulSoup
import re

# 偽裝成HTML
headers = {'content-type': 'text/html; charset=UTF-8','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
response = requests.get("https://www.ntu.edu.tw/", headers=headers)

# BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")


fp = open("weblink.txt","w",encoding="utf8")

Timeout = 3
count_OK = 0
count_NOT_OK = 0
count_Private = 0

# 所有的<a> 標籤節點
a_tags = soup.find_all('a')
for tag in a_tags:
  # 輸出超連結網址
  href = tag.get('href')

  if re.match("https://[a-z]+",href):
    print(href)
    fp.write(href)
    try:
      if(href == "https://www.cloud.ntu.edu.tw/") :
        print("你的連線不是私人連線")
        fp.write("你的連線不是私人連線\n")
        count_Private = count_Private + 1
      else :
        r = requests.get(href,timeout=Timeout, headers=headers)
        fp.write("網頁正常\n")
        count_OK = count_OK + 1
    except requests.exceptions.Timeout as ex:
      print("HTTP 請求已超過時間.....\n"+str(ex))
      fp.write("網頁已失效\n")
      count_NOT_OK = count_NOT_OK + 1
  elif re.match("http://[a-z]+",href):
    print(href)
    fp.write(href)
    try:
      r = requests.get(href,timeout=Timeout, headers=headers)
      fp.write("網頁正常\n")
      count_OK = count_OK + 1
    except requests.exceptions.Timeout as ex:
      print("HTTP 請求已超過時間.....\n"+str(ex))
      fp.write("網頁已失效\n")
      count_NOT_OK = count_NOT_OK + 1
      
fp.write("===========================================================\n") 
fp.write("網頁全部個數 : " + str(count_OK + count_NOT_OK + count_NOT_OK) + "\n")
fp.write("Timeout : " + str(Timeout) + "s\n")
fp.write("網頁正常個數 : " + str(count_OK) + "\n")
fp.write("網頁失效個數 : " + str(count_NOT_OK) + "\n")
fp.write("網頁連線不是私人連線個數 : " + str(count_Private) + "\n")
fp.write("===========================================================\n") 

fp.close()
