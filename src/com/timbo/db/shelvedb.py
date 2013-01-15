# -*- coding: utf-8 -*-
'''
Created on 2013-1-14

@author: Administrator
'''
import shelve

address = shelve.open('address')
address['1'] = ["Tom", "Beijing road", "2008-01-10"]
address['2'] = ["Jerry", "Shanghai road", "2008-03-09"]

if address.has_key('2'):
    del address['2']
    
print address
address.close()    