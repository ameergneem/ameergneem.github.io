import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
import Features, SentimentOptions, KeywordsOptions
from os import listdir
from os.path import isfile, join

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='URWkPkuEa7jNHKKQ31-kxeGqVrKqgZcazoL4_QpR3Q3N',
    url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
)
filesnames = [f for f in listdir('Reviews') if isfile(join('Reviews', f))]
filesCounter = 1
for filename in filesnames:
        print('////////'+filename+' ( '+str(filesCounter)+'/'+str(len(filesnames))+ ' ) //////////')

        f = open('Reviews/'+filename,'r+') 
        data = json.load(f)
        f.close()
        res = {'1':{'positive':0, 'neutral':0,  'negative':0},'2':{'positive':0, 'neutral':0,  'negative':0},'3':{'positive':0, 'neutral':0,  'negative':0},'4':{'positive':0, 'neutral':0,  'negative':0},'5':{'positive':0, 'neutral':0,  'negative':0}}
        passed = 1
        for i in range(0,5):
            rating =  str(i+1)
            print(rating)
            reviewsArray = data[rating]
            for rev in reviewsArray:
                try:
                    response = natural_language_understanding.analyze(
                        text=rev,
                        features=Features(
                            sentiment= SentimentOptions(False,
                    [
                    ""
                    ]
                    ) )).get_result()

                    label = response['sentiment']['targets'][0]['label']
                    if label  not in res[rating].keys():
                        print(label)
                    res[rating][label] +=1
                except Exception as ex:
                    print(str(passed)+'  reviews passed')
                    #print(rev)
                    passed += 1
                    pass
            
        with open('Results/'+filename,'w+') as resFile:
            json.dump(res,resFile)
        
        filesCounter += 1


