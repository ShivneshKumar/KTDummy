# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:07:51 2017

@author: Shivnesh.S
"""

import requests
import json
headers={'Content-Type': 'application/json'}

username = '54ab8084-b85f-45c7-8b0e-8baa106f7f69'
password = 'NnkIaIvBBDuJ'

endpoint = 'https://gateway.watsonplatform.net/natural-language-understanding/api'
query_nlu = {''}

op_stories = requests.get(endpoint,auth=(username,password),params = query_nlu)
