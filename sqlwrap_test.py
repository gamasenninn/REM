#!/usr/local/bin/python3.8

import sqlite3
import json
import unittest
import sys

from sqlwrap import *

#
#  Test for sqlwrap.py
#


class TestSqlwrap(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("----setUpClass--------------")   
        self.conn = sqlite3.connect(':memory:')


    def test_create_table(self):
        sql = '''
            CREATE TABLE "納品" (
                    "ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
                    "納品日"	TEXT,
                    "納品先"	TEXT,
                    "担当者"	TEXT,
                    "摘要"	TEXT
            )
            '''
        self.conn.execute(sql)
        print("\n-----Created Table------")

        c = self.conn.cursor()
        c.execute("select name from sqlite_master where type='table'" )
        ret = c.fetchall()
        self.assertEqual('納品',ret[0][0])


    def test_insert_dict(self):
        print("\n-----insert into Table by DICT------")
        conn = self.conn
        data = {'納品日': "2020/11/01",'納品先': "ABC商店",'担当者': "小野",'摘要': "特別注文"}
        ret = dict_insert(conn, '納品', data)
        print (ret)

        self.assertRegex(ret,'OK')

        t1 = tuple([i for i in data.values()])  #値だけのタプルを取得

        c = conn.cursor()
        c.execute('SELECT * FROM 納品 WHERE ID=1' )
        ret = c.fetchall()
        t2 = ret[0][1:] #キーを除いた項目のタプル

        print(t1,t2)
        self.assertEqual(t1,t2)

    def test_insert_json(self):
        print("\n-----insert into Table by JSON------")
        conn = self.conn
        data = {'納品日': "2020/11/02",'納品先': "ABC商店",'担当者': "小野",'摘要': "特別注文"}
        j_data = json.dumps(data)
        ret = json_insert(conn, '納品', j_data)
        print (ret)

        self.assertRegex(ret,'OK')

        t1 = tuple([i for i in data.values()])  #値だけのタプルを取得

        c = conn.cursor()
        c.execute('SELECT * FROM 納品 WHERE ID=2' )
        ret = c.fetchall()
        t2 = ret[0][1:] #キーを除いた項目のタプル

        print(t1,t2)
        self.assertEqual(t1,t2)

    def test_update_dict(self):
        print("\n-----Update Table by DICT------")
        conn = self.conn
        data = {'ID': 2,'納品日': "2020/11/04",'納品先': "更新テスト",'担当者': "小野2",'摘要': "特別注文2"}
        ret = dict_update(conn,'納品',data,'ID')
        print (ret)

        self.assertRegex(ret,'OK')

        t1 = tuple([i for i in data.values()])  #値だけのタプルを取得

        c = conn.cursor()
        c.execute('SELECT * FROM 納品 WHERE ID=2' )
        ret = c.fetchall()
        t2 = ret[0][0:] 

        print(t1,t2)
        self.assertEqual(t1,t2)



if __name__ == "__main__":

    unittest.main()
    sys.exit()

#-----Update data------

data = {'納品日': "2020/11/02",'担当者': "小野",'摘要': "更新テスト"}
j_data = json.dumps(data)
ret = json_update(conn,'納品',j_data,'担当者')
print (ret)

#----Select data ------
print("\n-----select from Table------")
c.execute('SELECT * FROM 納品' )
nous = c.fetchall()
print (nous)

#----Select data JSON Format------
print("\n-----select data JSON ------")
nous = json_select_all(conn,'納品')
print(nous)

#-----Delete data------
print("\n-----Delete Table------")
data = {'ID': 2}
ret = dict_delete(conn,'納品',data,'ID')
print (ret)

data = {'ID': 1}
j_data = json.dumps(data)
ret = json_delete(conn,'納品',j_data,'ID')
print (ret)

#----Select data ------
print("\n-----select from Table------")
c.execute('SELECT * FROM 納品' )
nous = c.fetchall()
print (nous)

conn.commit()
conn.close()
