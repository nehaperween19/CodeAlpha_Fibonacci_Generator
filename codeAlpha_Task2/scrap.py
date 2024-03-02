import requests

def fetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/"

fetchAndSaveToFile(url,"data/news.html")
r = requests.get(url)
print(r.text)