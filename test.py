import requests
from bs4 import BeautifulSoup

headers = {'content-type': 'text/html; charset=UTF-8','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
response = requests.get("https://www.ntu.edu.tw/", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
result = soup.find("href")
print(result)

