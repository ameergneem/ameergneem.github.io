
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time


driver = webdriver.Firefox()
driver.get("https://www.nytimes.com/topic/subject/book-reviews")
driver.find_element_by_xpath("//*[contains(text(), 'Show More')]").click()
SCROLL_PAUSE_TIME = 3
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
#linkesObj=[]
i=0
try:
    while True:
        i+=1
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       # print( "Number of URLs: ",len(driver.find_elements_by_class_name('story-link')))
      
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        if i%100==0:
            SCROLL_PAUSE_TIME += 10

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print(i)
            break
        last_height = new_height

except Exception as ex :
    print("exception!!!!")
    print(ex)
    allUrls = []
    linkesObj = driver.find_elements_by_class_name('story-link')
    for linkObj in linkesObj:
        if linkObj.get_attribute('href') is not None:
            allUrls.append(linkObj.get_attribute('href'))

    with open('NYTArticlesURLs.txt','w') as file:
            for url in allUrls:
                file.write("%s\n" % url)



allUrls = []
linkesObj = driver.find_elements_by_class_name('story-link')
for linkObj in linkesObj:
    if linkObj.get_attribute('href') is not None:
        allUrls.append(linkObj.get_attribute('href'))

with open('NYTArticlesURLs.txt','w') as file:
        for url in allUrls:
            file.write("%s\n" % url)




'''

driver.find_element_by_xpath("//*[@id=\"latest-panel\"]/div[1]/ol[1]").find_elements_by_tag_name("li")[0].click()


elements = driver.find_elements_by_class_name('css-exrw3m')
print(elements[0].text)

for ele in elements:
    print(ele.text)
    
'''