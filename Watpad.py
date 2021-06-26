import requests
import re
url = "https://www.wattpad.com/689450174-ben-shapiro-x-reader-first-meeting"
headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

reponse = requests.get(url, headers=headers)
print(reponse)
print(reponse.content.decode(encoding="utf-8"))

string = reponse.content.decode("utf-8")


f = open("data.txt", "a")
f.write(string)
f.close()


string_search = """
    <div class="col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading" dir="ltr">
"""

index = string.find(string_search)

print(index)
