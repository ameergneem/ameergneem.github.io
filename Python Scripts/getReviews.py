# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

ratingsTexts = {
    'it was amazing':5,
    'really liked it':4,
    'liked it':3,
    'it was ok':2,
    'did not like it':1
}
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def getGenreBooksURLs(genre,driver):
                books = driver.find_elements_by_xpath('//div[@class="leftContainer"]/\
                    div/div[@class="bigBoxBody"]/div/div/\
                    div[@class="leftAlignedImage bookBox"]/\
                    div[@class="coverWrapper"]/a')
                
                books_urls = []

                for book in books:
                    books_urls.append(book.get_attribute('href'))
              
                
                return books_urls
                
def getReviewsFromPage(driver):
    return driver.find_elements_by_xpath('//div[@id="bookReviews"]/ \
                    div[@class="friendReviews elementListBrown"]')


def getBookData(bookURL,driver):
    driver.get(bookURL)
    allReviews = []
    pageReviews = getReviewsFromPage(driver)
    for review in pageReviews:
        allReviews.append(parseSingleReview(review))
    
    return allReviews


def parseSingleReview(review):
    try:
        span = review.find_elements_by_xpath('.//div/div/div/ \
                                    div[@class="reviewText stacked"]/span/ \
                                    span[2]')
        if len(span) ==0 :
            span = review.find_elements_by_xpath('.//div/div/div/ \
                                    div[@class="reviewText stacked"]/span/ \
                                    span[1]')[0]
        else:
            span = review.find_elements_by_xpath('.//div/div/div/ \
                                    div[@class="reviewText stacked"]/span/ \
                                    span[2]')[0]
        
        text = span.get_attribute('innerHTML').replace('<br>','').replace('<i>','').replace('</i>','')
        idx = review.find_element_by_xpath('.//div[1]/div[1]//div[1]/div[1]/span[2]').get_attribute('title')
        rating = ratingsTexts[idx]
        text = BeautifulSoup(text, "lxml").text
        return {'rating':rating,'text':text}
    except Exception as ex:
        
        return {'rating':0,'text':'NONE'}


def getGenresFromFile():
    with open('subjectsList.txt', 'r') as f: 
        return [w.replace('\n','')  for w in f.readlines()]



genres = getGenresFromFile()
print('num of genres ',len(genres))
driver = webdriver.Firefox()
numOfGenres = len(genres)
genresCounter = 1
passed = False
for genreIdx in range(0,len(genres)):
    if passed == True:
        genreIdx-=1
        genresCounter-=1
        passed = False
        driver = webdriver.Firefox()

    genre = genres[genreIdx]
    print('//////////////////////////'+genre+'//////////////////////////////')
    try:
        driver.get("https://www.goodreads.com/genres/"+genre)
        allBooksUrls = getGenreBooksURLs(genre,driver)
        numOfBooks = len(allBooksUrls)
        booksCounter = 1
        ratingsClasses = {'1':[],'2':[],'3':[],'4':[],'5':[]}
        for bookUrl in allBooksUrls:
            allReviews = getBookData(bookUrl,driver)
            numOfReviews = len(allReviews)
            reviewsCounter = 1
            for review in allReviews:
                print('genre: ('+str(genresCounter)+'/'+str(numOfGenres)+') , book: ('+str(booksCounter)+'/'+str(numOfBooks)+') , review:  ('+str(reviewsCounter)+'/'+str(numOfReviews)+')')
                if review['text'] is not 'NONE':
                    ratingsClasses[str(review['rating'])].append(review['text'])
                reviewsCounter +=1
            booksCounter += 1
        with open('Reviews/'+genre+'.json', 'w+') as json_file:  
            json.dump(ratingsClasses, json_file)
    except Exception as ex:
        print('passing '+ genre)
        print('due to '+str(ex))
        time.sleep(10)
        passed=True
        
    genresCounter += 1


        
#pDjVYXtNBFGO9mbbCmxewEA7MJq2lQGo
#getBookData('https://www.goodreads.com/book/show/37570546-maybe-you-should-talk-to-someone',driver)



