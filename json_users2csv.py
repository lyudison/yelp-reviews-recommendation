# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:20:22 2016
This script loads users json file and writes to csv
@author: ZMP
"""
import json
import csv
import sys,re

#Fixes ASCII error in Python csv writer module
reload(sys)
sys.setdefaultencoding('utf-8')

#Load json files by lines into data
data = []
attribute_name={}
f=open('yelp_academic_dataset_user.json')
i=0   
for line in f:
    data.append(json.loads(line))

#extract csv headers, 10000 samples should be sufficient
i=0
for rows in data:
    if i>=10000:
        break;
    i+=1;
    for keys in rows:
        if not attribute_name.has_key(keys):
            attribute_name[keys]=0
print attribute_name

#Process data into csv compatible and desired format
array=[]
for rows in data:
    row_data=[]
    for keys in attribute_name:
        if not rows.has_key(keys):
            row_data+=[0]
        else:
            if(keys==u'friends'):
                row_data+=[len(rows[keys])]
            if(keys==u'votes'):
                row_data+=[rows[keys][u'funny']]
            if(keys==u'compliments'):
                row_data+=[len(rows[keys])]
            if(keys==u'elite'):
                row_data+=[len(rows[keys])]
            if(keys=='yelping_since'):
                since=[int(x.group()) for x in re.finditer(r'\d+', rows[keys])]
                Yelp_time=1.0*(2016-since[0])+1.0*(5-since[1])/12                
                row_data+=[Yelp_time]
            if(keys==u'review_count'):
                row_data+=[rows[keys]]
            if(keys==u'user_id'):
                row_data+=[rows[keys]]
            if(keys==u'name'):
                row_data+=[rows[keys]]
            if(keys==u'type'):
                row_data+=[rows[keys]]
            if(keys==u'fans'):
                row_data+=[rows[keys]]
            if(keys==u'average_stars'):
                row_data+=[rows[keys]]                               
    array+=[row_data]

#writes into csv file
csvfile = open('user.csv','wb')
fileToWrite = csv.writer(csvfile, delimiter=',',quotechar='|')
print attribute_name.keys()
fileToWrite.writerow(attribute_name.keys())
fileToWrite.writerows(array)
