import httplib2
import urllib2
import json
from bs4 import BeautifulSoup
from sys import argv

resources = open('resources.txt', 'r+')
downloads = open('downloads.txt', 'r+')
data = open('sitecore_data.json', 'r')
resources.truncate()
downloads.truncate()

def getResourceTree(url):
    http = httplib2.Http()
    status, response = http.request(url)
    soup = BeautifulSoup(response, "html.parser")

    datas = data.read()
    dataNew = json.loads(datas)
    newWord = ""
    for words in dataNew.get("results"):
        for letters in words.get("url"):
            newWord += letters
        newWord += "\n"
        resources.write(newWord)
    

getResourceTree("http://www.sitecore.net/en/resources/index")

resources.close()
downloads.close()
data.close()