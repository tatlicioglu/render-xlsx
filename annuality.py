#!/usr/bin/env python

import datetime

class Annuality:
   def __init__(self, year, value):
      self.year = year
      self.value = value
      self.date = datetime.datetime(year, 1, 1)

   def __str__(self):
       return "Year: " + str(self.year) + ", annuality value: " + str(self.value) + ", date: " + str(self.date)

   def __repr__(self):
       return "Year: " + str(self.year) + ", annuality value: " + str(self.value) + ", date: " + str(self.date)