#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jskubs'

from customer import Customer
import datetime
from pymongo import MongoClient

class Program:
    def __init__(self):
        self.client = MongoClient('127.0.0.1:27017')
        self.newcustomer = ''

    def create(self):
        lista = [dict(name='Jessica', age=25, register=33377789, phone='555-777-999'),
                 dict(name='Caio', age=23, register=78799901, phone='566-888-000'),
                 dict(name='Fernando', age=24, register=9876543, phone='555-798-000')]
        for l in lista:
            self.newcustomer = Customer(l['name'], l['age'], l['register'], l['phone'])
            now = datetime.datetime.now()
            created_at = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
            timestamp = created_at
            x = dict(timestamp=timestamp, created_at=created_at)
            dbMg = self.client.local
            try:
                dbMg.customers.insert({'type': 'customer', 'timestamp': x['timestamp'],
                                       'metadata': {'name': self.newcustomer.name, 'register': self.newcustomer.register,
                                                    'age': self.newcustomer.age, 'phone': self.newcustomer.phone},
                                       'created_at': x['created_at']})
                print dict(message='Ok')
            except Exception as e:
                print dict(message=e.message)

    def read(self):
        dbMg = self.client.local
        lista = dbMg.customers.find()
        for x in lista:
            print x

    def update(self):
        dbMg = self.client.local
        try:
            dbMg.customers.update({'metadata.register': 78799901},
                                  {"$set": {
                                      'metadata.phone': '888-444-333',
                                      'metadata.age': 25
                                  }})
            return dict(message='Ok')
        except Exception as e:
            return dict(message=e.message)

    def delete(self):
        dbMg = self.client.local
        try:
            dbMg.customers.remove({'metadata.register': 9876543})
            return dict(message='Ok')
        except Exception as e:
            return dict(message=e.message)

    def close(self):
        self.client.close()

if __name__ == '__main__':

    P = Program()
    P.create()
    P.read()
    result_upd = P.update()
    print result_upd

    P.read()

    result_del = P.delete()
    print result_del

    P.read()

    P.close()
