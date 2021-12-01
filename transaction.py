#!/usr/bin/env python

from datetime import datetime

class Transaction:
   def __init__(self, date, amount, price):
      self.date = datetime.strptime(date, '%Y-%m-%d')
      self.amount = amount
      self.price = price
      self.value = float(self.amount) * float(self.price)

   def __str__(self):
       return "Transaction date: " + str(self.date) + ", transaction amount: " + str(self.amount) + ", unit price: " + str(self.price) + ", total value: " + str(self.value)

   def __repr__(self):
       return "Transaction date: " + str(self.date) + ", transaction amount: " + str(self.amount) + ", unit price: " + str(self.price) + ", total value: " + str(self.value)