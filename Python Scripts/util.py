# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import json,urllib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
from os import listdir
from os.path import isfile, join
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
import Features, SentimentOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='URWkPkuEa7jNHKKQ31-kxeGqVrKqgZcazoL4_QpR3Q3N',
    url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
)

def analyze(txt):
    response = None
    while response is None:
        try:
            response = natural_language_understanding.analyze(
                            text=txt,
                            features=Features(
                                sentiment= SentimentOptions(False,
                        [
                        ""
                        ]
                        ) )).get_result()
        except Exception as ex:
            pass
    return response

onlyfiles = [f for f in listdir('NYTBooksReviews/NYTArticlesResults/') if isfile(join('NYTBooksReviews/NYTArticlesResults', f))]
allResults = []

def getBookRes(bookinfo):
    return {'bookName':bookinfo['bookName'],'sentement':analyze(bookinfo['NYTReview'])['sentiment']['targets'][0]['label']}

def getNYTBookInfoJson(bookName):
    fault = True
    response = None
    print('---'+bookName+'---')
    while fault == True:
        try:
            url = "https://api.nytimes.com/svc/books/v3/reviews.json?title="+bookName+"&api-key=pDjVYXtNBFGO9mbbCmxewEA7MJq2lQGo"
            response = urllib.urlopen(url)
        except Exception as ex:
            print('\n\n----------------------exception inside getNYTBookInfoJson----------------------')
            print('the response ',response)
            print('the exception ' ,ex)
            print('----------------------END----------------------\n\n')
            return ''
        data = json.loads(response.read())
        #print('the arrived data ',data)
        if 'fault' not in data.keys():            
                result = data['results']
                if result:
                    return result[0]['url']
                return ''
        else:
            print('Waiting...')
            time.sleep(7)


for filename in onlyfiles:
        allResults = []
 
        print('//////////'+filename+'//////////')
        try:
            with open('NYTBooksReviews/NYTArticlesResults/'+filename,'r+') as f:
               
                jsn = json.loads(f.read())
                for bookinfo in jsn:
                        res = getNYTBookInfoJson(bookinfo['bookName'])
                        bookinfo['url'] = res
                        allResults.append(bookinfo)
        except Exception as ex:
            print(ex)
            with open('NYTBooksReviews/NYTArticlesResults/withURLs/'+filename.split('.json')[0]+'WithURLs.json','w+') as f:
                json.dump(allResults,f)

            

        with open('NYTBooksReviews/NYTArticlesResults/withURLs/'+filename.split('.json')[0]+'WithURLs.json','w+') as f:
                json.dump(allResults,f)





