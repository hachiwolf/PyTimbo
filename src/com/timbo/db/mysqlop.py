# -*- coding: utf-8 -*-
'''
Created on 2013-1-14

@author: Administrator
'''
import sys
import MySQLdb

# 连接数据库
try:
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="timbo", db="address_bookdb")

except Exception, e:
    print e
    sys.exit()    
    
cursor = conn.cursor()
sql = "insert into t_addr(name, address) values(%s, %s)"
values = (("张三", "北京海淀区"), ("李四", "北京海淀区"), ("王五", "北京海淀区"))

try:
    cursor.executemany(sql, values)
except Exception, e:
    print e
    
sql = "select id, name, address from t_addr"
cursor.execute(sql)
data = cursor.fetchall()

if data:
    for x in data:
        print x[0], x[1], x[2]
        
conn.commit()
cursor.close()
conn.close()                