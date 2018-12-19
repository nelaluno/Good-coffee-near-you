# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:05:27 2018

@author: Murk
"""

import mysql.connector
from mysql.connector import Error
    
class table():
    def __init__(self, name, bd, colomns):
        self.bd = bd
        self.name = name
        self.colomns = colomns
        self.cur = bd.cursor(buffered=True)
        #self.count = 0
    
    def insert(self, colomns=[], values=[]):
        try:
            insert_q = ('INSERT INTO' + self.name + '(' + ', '.join(colomns)+')'+
                                'VALUES (' + ','.join(values) + ')' + ';')
            self.cur.execute(insert_q)
            bd.commit()
        except Exception:
            raise Exception('insert')
        
    def update(self, new_col_val=[], where_col_val=[]):
        #may be i have to add several colomns
        try:
            update_q = []
            update_q.expend(['UPDATE', self.name, 'SET', new_col_val[0][0], '=', str(new_col_val[0][1])])
            for col, val in new_col_val[1:]:
                update_q.expend([',', col, '=', str(val)])
            update_q.expend(['WHERE', where_col_val[0][0], '=', str(where_col_val[0][1])])
            for col, val in where_col_val[1:]:
                update_q.expend(['and', col, '=', str(val)])
            self.cur.execute(' '.join(update_q)+';')
            bd.commit()
        except Exception:
            raise Exception('update')
        
    def query(self, query, commit=1):
        try:
            self.cur.execute(query)
            if commit:
                bd.commit()
            return self.cur
        except Exception:
            raise Exception('query')
        
    def close(self, close_bd_too = 0):
        try:
            self.cur.close()
        except Exception:
            raise Exception('close')
        finally:
            print('bd is connected - ', bd.is_connected()

    def __del__(self):
        try:
            self.cur.close()
        except Exception:
            raise Exception('close')
        finally:
            print('bd is connected - ', bd.is_connected()
        
        
