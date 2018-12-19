# -*- coding: utf-8 -*-
import mysql
mybd = mysql.connector.connect(host = 'good-coffee-near-you.cgcnnlvq1rjd.us-east-1.rds.amazonaws.com',
                               user = 'barista', passwd = 'good0afternoon',
                               database = 'CoffeHouses')

mycursor = mydb.cursor()

with open('coffee_shop.txt', 'r') as f:
    for line in f:
        mycursor.execute(line)
f.close()

mycursor.close()
mydb.close()
