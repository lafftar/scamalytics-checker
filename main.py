import requests
from bs4 import BeautifulSoup
#
# for x in range(256):
#     ip = f"154.{x}.232.12"
#     resp = requests.get(f"https://scamalytics.com/ip/{ip}").content
#     html = BeautifulSoup(resp, 'lxml')
#     fraud_score = html.select("body > div.container > div.guage_body > "
#                               "div.score_bar > div.score")[0].text
#     print(f"{ip} ----------- {fraud_score}")
# resp = requests.get("https://scamalytics.com/ip/154.250.232.12").content
# html = BeautifulSoup(resp, 'lxml')
# fraud_score = html.select("body > div.container > div.guage_body > "
#                           "div.score_bar > div.score")[0].text

print(BeautifulSoup(requests.get("https://www.google.com/search?q=Miranda+Conwald&tbs=qdr:d").content, 'lxml').prettify())