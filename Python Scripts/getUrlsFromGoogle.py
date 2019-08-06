# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from os import listdir
from os.path import isfile, join
import json,urllib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import bs4 
import time
from googlesearch import search 



onlyfiles = [f for f in listdir('NYTBooksReviews/NYTArticlesResults/withURLs/') if isfile(join('NYTBooksReviews/NYTArticlesResults/withURLs/', f))]
for filename in onlyfiles:
    finalResult = []
    with open('NYTBooksReviews/NYTArticlesResults/withURLs/'+filename,'r+') as f:
        print(filename)
        data = json.loads(f.read())
        i = 1
        for bookinfo in data:
                print('---------'+str(i)+'/'+str(len(data))+' ---------')
                query = "ny times "+bookinfo['bookName']+" book review"
                try:
                    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
                        bookinfo['url'] = j
                        finalResult.append(bookinfo)
                except Exception as ex:
                    finalResult.append(bookinfo)
                    pass

                i += 1
    with open('NYTBooksReviews/NYTArticlesResults/withURLs/lastResults/'+filename.split('.json')[0]+'Updated.json','w+') as f2:
        json.dump(finalResult,f2)



