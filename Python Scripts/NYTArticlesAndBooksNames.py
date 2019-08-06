# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='geckodriver')

def getText(x):
    return x.text
def getDataFromUrl(driver,url):
    driver.get(url)
    try:
        ele= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/article/section/div[1]/div/p[1]/strong')
        return ele.text
    except:
        return None


NYTBooksReviews = {'allReviews':[]}
try:
    with open('NYTArticlesURLs.txt','r') as file:
        i=1
        while i<3375:
          url = file.readline()
          i += 1
        
        while url:
            print('///////////// ('+str(i)+'/'+'10020) /////////////')
            bookName = getDataFromUrl(driver,url)
            if not bookName and bookName !=None:
                driver.close()
                options = Options()
                options.headless = True
                driver = webdriver.Firefox(options=options, executable_path='geckodriver')
            else:
                if bookName != None:
                    try:
                        paragraphsElements = driver.find_elements_by_class_name('css-exrw3m')
                    except:
                        paragraphsElements = []
                    wholeTextParagraphs =map(getText,paragraphsElements)
                    wholeText = '\n'.join(wholeTextParagraphs)
                    jsn = {'bookName': bookName,'NYTReview':wholeText}
                    NYTBooksReviews['allReviews'].append(jsn)
                    print(bookName)
                url = file.readline()
                i += 1
except Exception as ex:
        print("Exception!!!!!!!")
        print(ex)
        with open('NYTBooksReviews/allNYTReviewsFrom3375.json', 'w+') as json_file:  
            if len(NYTBooksReviews['allReviews']) > 0:
                json.dump(NYTBooksReviews, json_file)

with open('NYTBooksReviews/allNYTReviewsFrom3375.json', 'w+') as json_file:  
            if len(NYTBooksReviews['allReviews']) > 0:
                json.dump(NYTBooksReviews, json_file)

