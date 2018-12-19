# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:05:27 2018

@author: Murk
"""
import mysql.connector
from mysql.connector import Error
from table import *

class bd_interaction:
    def __init__(self, host, user, passwd, database, connect=0, file=""):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.tables = dict() #name : table
        self.bd = None
        if connect:
            self.connect()
        if any(file):
            with open(file) as f:
                for line in f:
                    name, colomns = line.split(':')
                    self.add_table(name, colomns.split(','))
                f.close()

    def connect(self):
        try:
            self.bd = mysql.connector.connect(host = self.host, user = self.user,
                                              self.passwd = self.passwd,
                                              database = self.database)
        except Exception:
            raise Exception('connect')
        finally:
            print('connect: connection is ', self.bd.is_connected())
            
    def unconnect(self):
        if self.bd.is_connected():
            for table_name in self.tables:
                self.tables[table_name].cur.close()
            self.bd.close()
        print('unconnect: connection is ', self.bd.is_connected())

    def add_table(self, table_name, colomns):
        if self.tables.get(table_name) is None:
            self.tables[table_name] = table(name, bd, colomns)

    def __del__(self):
        self.unconnect()

        
