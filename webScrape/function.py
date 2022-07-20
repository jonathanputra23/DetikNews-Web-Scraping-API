import requests
from bs4 import BeautifulSoup
import json

value = {}

class scrape_function():
    def scrape_website(URL):
        num = 1
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        article_elements = soup.find_all('article')
        for article in article_elements:
            media_title = article.find(class_ ="title")
            link = article.find('a').get('href')
            media_date = article.find(class_ = "date")
            about = article.find('p')
            value[num]={
                "title": media_title.get_text(),
                "link": link,
                "date": media_date.get_text(),
                "summary": about.get_text()
                }
            num+=1
        value_json = json.dumps(value)
        json_data = json.loads(value_json)
        return json_data
        

    def getSiteId(category):
        if category=="detikcom":
            siteId=2
        elif category=="detiknews":
            siteId=3
        elif category=="detikfinance":
            siteId=29
        elif category=="detiksport":
            siteId=21
        elif category=="sepakbola":
            siteId=27
        elif category=="detikhealth":
            siteId=55
        elif category=="detikhot":
            siteId=32
        elif category=="wolipop":
            siteId=63
        elif category=="detikinet":
            siteId=5
        elif category=="detikfood":
            siteId=35
        elif category=="detikoto":
            siteId=44
        elif category=="detiktravel":
            siteId=66
        else:
            siteId=2
        return "&siteid={}".format(siteId)

    def search_website(keywords):
        #https://www.detik.com/search/searchall?query=racun&page=1&sortby=&sorttime=0&fromdatex=&todatex=&hitperpages=9&siteid=29
        URL = "https://www.detik.com/search/searchall?query="
        keyword_value = list(keywords.values())[0]
        siteId_value = scrape_function.getSiteId(list(keywords.values())[1])
        fromDate_value = scrape_function.getFromDate(list(keywords.values())[2])
        toDate_value = scrape_function.getToDate(list(keywords.values())[3])
        page_value = scrape_function.getPage(list(keywords.values())[4])
        
        if (len(keyword_value.split())>1):
            keyword_value = '+'.join(keyword_value.split())
        
        print(URL+keyword_value+siteId_value+fromDate_value+toDate_value+page_value)

        return URL+keyword_value+siteId_value+fromDate_value+toDate_value+page_value

    def getFromDate(fromDate):
        split_fromDate = fromDate.split('-') #YYYY-MM-DD to DD/MM/YYYY
        reverse_split_fromDate = list(reversed(split_fromDate))
        fromDate_value = '/'.join(reverse_split_fromDate)   
        return "&fromdatex={}".format(fromDate_value)

    def getToDate(toDate):
        split_toDate = toDate.split('-') #YYYY-MM-DD to DD/MM/YYYY
        reverse_split_toDate = list(reversed(split_toDate))
        toDate_value = '/'.join(reverse_split_toDate) 
        return "&todatex={}".format(toDate_value)

    def getPage(page):
        return "&page={}".format(page)