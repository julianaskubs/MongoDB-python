#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'jskubs'

import datetime
from pymongo import MongoClient
from Util import CustomerCrud as cc

class Customer:
    def __init__(self,data):
        self.list_data=data
        self.client = MongoClient('127.0.0.1')
        if 5 == len(self.list_data):
            cc().insert_customer(self.list_data, self.client)
        else:
            print 'Not Enough Values'
        self.client.close()


if __name__ == '__main__':
    op = raw_input('Press number:\n'
                   '1 to Insert Customer\n')
                   # TO-D0
                   # '2 to Delete Customer\n'
                   # '3 to Update Customer\n'
                   # '4 to List Customer:\n')
    i = 1
    while i == 1:
        if int(op) == 1:
            input_data = raw_input('Enter "name,bdate(yyyy-mm-dd),register,phone,gender" in this order and'
                                   ' separated by comma:\n')
            Customer(str(input_data).split(','))
        i = int(raw_input('Press 0 to out or 1 to continue:\n'))
