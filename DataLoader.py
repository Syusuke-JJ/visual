# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:29:59 2021

@author: 123
"""
import numpy as np
import pandas as pd
import datetime

relation_list = ['follows','fans','repose','comment','attitude']
node_csv = pd.read_csv('user_final.csv')
edge_csv = pd.read_csv('relation.csv')
edgu_csv = edge_csv[edge_csv['relation']!=0]
date0 = datetime.date(2021,1,1)

# Save the Data
data = open('data.txt','w')

data.write('{\n\t"nodes": [\n')
for i in range(len(node_csv)):
    data.write('\t\t{"id": '+str(node_csv['userId'][i])+
               ', "group": '+str(node_csv['label'][i])+
               ', "sex": "'+node_csv['sex'][i]+'"'+
               ', "fans_count": '+str(node_csv['fans_count'][i])+
               ', "follows_count": '+str(node_csv['follows_count'][i])+
               ', "weibos_count": '+str(node_csv['weibos_count'][i])+'},\n')
data.write('\t],\n')

data.write('\t"links": [\n')
for i in range(len(edge_csv)):
    data.write('\t\t{"source": '+str(edge_csv['src'][i])
               +', "target": '+str(edge_csv['dst'][i])
               +', "relation": "'+relation_list[edge_csv['relation'][i]-1]+'"'
               +', "date": "'+str(date0+datetime.timedelta(days=edge_csv['day'][i]))
               +'"},\n')
data.write('\t]\n}')
data.close()