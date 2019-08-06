from langdetect import detect_langs
import json
import unicodedata
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('Reviews') if isfile(join('Reviews', f))]
for fileName in onlyfiles:
    with open('Reviews/'+fileName) as file:
        data = json.load(file)

    for key in data.keys():
        print(len(data[key]))
        for i in range(0,len(data[key])):
                data[key][i]=unicodedata.normalize('NFKD', data[key][i]).encode('ascii','ignore')


    with open('Reviews/'+fileName, "w") as jsonFile:
        json.dump(data, jsonFile)

