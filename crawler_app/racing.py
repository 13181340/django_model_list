import requests
import codecs
from bs4 import BeautifulSoup

def get_html_from(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    html = requests.get(url,headers=header)
    html = html.text
    singer_parse= BeautifulSoup(html, 'html.parser')
    return html

def racingmodel_list(category):
    myurl = "https://namu.wiki/w/"+category+"/목록"
    html = get_html_from(myurl)
    singers_parse = BeautifulSoup(html,'html.parser')
    link = singers_parse.find_all("div",{"class":"wiki-content clearfix"})
    return link
