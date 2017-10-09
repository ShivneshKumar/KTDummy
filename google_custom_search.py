# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:24:45 2017

@author: Shivnesh.S
"""
import requests
google_api_key='AIzaSyDWbOC6S_1t4IAtuVSLhe9WwUB-G3yGQg8'

cx = '011447846146199412458:ojxhnwgdfdk'

query_engine = {'key':google_api_key,
                'cx':cx,
                'q':"Mu Sigma"}
response = requests.get('https://www.googleapis.com/customsearch/v1',params = query_engine)
