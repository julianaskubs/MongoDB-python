#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'jskubs'

from customer import Customer
import datetime
from pymongo import MongoClient

class Program:
    def __init__(self):
        self.client = MongoClient('127.0.0.1:27017')
        self.newcustomer = Customer('Alisson', 18, 334445566, '555-777-888')

    def create(self):
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
            return dict(message='Ok')
        except Exception as e:
            return dict(message=e.message)

    def read(self):
        dbMg = self.client.local
        lista = dbMg.customers.find()
        for x in lista:
            print x

    def update(self):
        pass

if __name__ == '__main__':
    # teste = Program().create()
    # print teste

    Program().read()



