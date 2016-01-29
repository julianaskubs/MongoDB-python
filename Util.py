__author__ = 'jskubs'

from pymongo import MongoClient
import datetime


class CustomerCrud:
    def __init__(self):
        pass

    def insert_customer(self, list_data, client):
        name,bdate,register,phone,gender = list_data
        now = datetime.datetime.now()
        created_at = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second)
        timestamp = created_at
        x = dict(name=name,bdate=bdate,register=register,phone=phone,gender=gender,timestamp=timestamp,
                 created_at=created_at)
        msg = self.insertMongo_customer(x, client)
        print msg

    def insertMongo_customer(self, x, client):
        dbMg = client.customers
        try:
            dbMg.customers.insert({'type':'customer', 'timestamp': x['timestamp'],
                                 'metadata':{'name':x['name'], 'birth_date':x['bdate'],
                                     'register':x['register'], 'phone':x['phone'], 'gender':x['gender']},
                                 'created_at': x['created_at']})
            return dict(message='Ok')
        except Exception as e:
            return dict(message=e.message)





