# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import json,urllib2
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from xml.dom import minidom
import time
from selenium.webdriver.firefox.options import Options
import xmltodict
import xml.etree.ElementTree as ET



def getBookRating(bookName,exCnt):
    try:
        url = "https://www.goodreads.com/search/index.xml?key=cDMawoujpx8pvTgGsm2w&q="+bookName
        #response = urllib.urlopen(url)
        #data = xmltodict.parse(response.read())
        dom = minidom.parse(urllib2.urlopen(url.replace(' ','%20')))
        child = dom.getElementsByTagName('average_rating')[0]
        ratingsCount=dom.getElementsByTagName('ratings_count')[0].firstChild.data
        id= dom.getElementsByTagName('best_book')[0].getElementsByTagName('id')[0].firstChild.data

        return child.firstChild.data , exCnt , id , ratingsCount
    except Exception as ex:
        print(str(exCnt)+")EXCEPTION!!!!! ")
        print(ex)
        exCnt += 1
        return '' , exCnt , -1 , -1
    return 'None' , exCnt , -1 , -1




with open('objectsUpd.txt','r+') as f:
    jsn = json.load(f)
    i=1
    exCnt = 1
    noneCnt = 1
    dataLen = len(jsn['data'])
    try:
        for obj in jsn['data']:
            id = -1
            ratingsCount = -1
            print('////////// '+str(i)+'/'+str(dataLen)+'//////////' )

            obj['GoodReadsRating'] , exCnt , id ,ratingsCount = getBookRating(obj['bookName'],exCnt)
            obj['GoodReadsRating'] = str(obj['GoodReadsRating'])
            obj['RatingsCount'] = str(ratingsCount)
            obj['GoodreadsURL'] = 'https://www.goodreads.com/book/show/'+str(id)+'-'+obj['bookName'].replace(' ','-')
            
            if obj['GoodReadsRating'] == 'None':
                print(str(noneCnt) + ')None')
                noneCnt += 1

            i += 1

    except Exception as ex:
        print(ex)
        with open('objectsUpd2.txt','w+') as f:
                json.dump(jsn,f)

with open('objectsUpd2.txt','w+') as f:
    json.dump(jsn,f)


    #https://www.goodreads.com/search/index.xml?key=cDMawoujpx8pvTgGsm2w&q=
    