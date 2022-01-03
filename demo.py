import requests
from bs4 import BeautifulSoup
import re

headers = {'content-type': 'text/html; charset=UTF-8','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
response = requests.get("https://www.ntu.edu.tw/", headers=headers)

# BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

fp = open("alllink.txt","w",encoding="utf8")
count = 0


a_tags = soup.find_all('a')
for tag in a_tags:
  href = tag.get('href')
  if re.match("https://[a-z]+",href):
    count = count + 1
    fp.write(href+"\n")
  elif re.match("http://[a-z]+",href):
    count = count + 1
    fp.write(href+"\n")

print(count)
fp.close()
