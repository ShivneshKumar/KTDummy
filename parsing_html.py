# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:47:03 2017

@author: Shivnesh.S
"""
#impporting required packages
import requests
import json
from bs4 import BeautifulSoup
from google import search

#diffbot trial period token
diffbot_developer_token = '6673212352e7551e2e0334c69bace614'

#function to get the urls out of google search results
def get_url_list(query):
    google_results = search(query,tpe='nws',stop=1,extra_params={'num':3,'start':0})
    list_urls = []
    try:
        list_urls = list(google_results)
    except:
        return 'No Results'
    return list_urls

#function to get the main relevant content in a url
def url_main_content(keyword):
    article_list = []
    url_list = get_url_list(keyword)
    if type(url_list) == str:
        return url_list #url_list will contain 'No Results'
    else:
        for url in url_list:
            print(url)
            diffbot_response = requests.get('https://api.diffbot.com/v3/article',params ={'token':diffbot_developer_token,'url':url})
            article = {}
            try:
                response_obj = json.loads(diffbot_response.text)['objects'][0]
                article['pageURL'] =  response_obj['pageUrl']
                article['sitename'] = response_obj['siteName']
                article['title'] = response_obj['title']
                try:
                    article['author'] = response_obj['author']
                except:
                    article['author'] = 'Not Available'
                article['date'] = response_obj['date']
                try:
                    article['publisherCountry'] = response_obj['publisherCountry']
                except:
                    article['publisherCountry'] = 'Not Available'
                try:
                    article['publisherRegion'] = response_obj['publisherRegion']
                except:
                    article['publisherRegion'] = 'Not Available'
                article['text'] = response_obj['text']
            except:
                article['error'] = 'Unexpected Error'
            article_list = article_list + list([article])
    return article_list

#reading the keyword file to get list of keywords specified by user
keyword_file = open("C:\\Users\\Shivnesh.S\\NLP\\keyword.txt","r")
keyword_file_content=keyword_file.read()
keyword_file.close()
keyword_list = keyword_file_content.split('\n')

#creating a json for the final output of all keywords
keyword_json = {}
for keyword in keyword_list:
    content_list = url_main_content(keyword)
    keyword_json[keyword] = content_list

#Writing the final output to a local file
file_content = json.dumps(keyword_json)
new_file = open("C:\\Users\\Shivnesh.S\\NLP\\result.txt","w",encoding='utf-8')
new_file.write(file_content)
new_file.close()