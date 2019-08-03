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


with open('objects.txt','r+') as f:
    jsn = json.load(f)['data']
    i=1
    for obj in jsn:
        print(obj)
        obj['id'] = str(i)
        i +=1
with open('objectsUpd.txt','w+') as f:
    json.dump(jsn,f)