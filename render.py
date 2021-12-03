#!/usr/bin/env python

import pandas as pd
import sys
from os.path import exists
from datetime import datetime
from transaction import Transaction
from utils import Utils
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np

if len(sys.argv) != 2:
    raise Exception("Usage render.py <input-file-name>")

input_file = sys.argv[1]

if not exists(input_file):
    raise Exception("File " + input_file + " not found.")

vest_transactions = []
d_transactions = pd.read_excel(input_file, "Transactions")
for _, row in d_transactions.iterrows():
    date = row[3]
    amount = row[4]
    price = row[5]
    transaction = Transaction(date, amount, price)
    vest_transactions.append(transaction)
    
transactions = []
d_schedules = pd.read_excel(input_file, "Vest Schedules")
for _, row in d_schedules.iterrows():
    date = row[7]
    amount = row[8]
    price = vest_transactions[-1].price
    vest_transaction = Utils.find_vest_transaction(vest_transactions, datetime.strptime(date, '%Y-%m-%d'))
    if (vest_transaction != None):
        price = vest_transaction.price
    transaction = Transaction(date, amount, price)
    #print(transaction)
    transactions.append(transaction)


transactions = sorted(transactions, key=lambda x: x.date)

annualities = Utils.get_annualities(transactions)

x_values = [x.date for x in annualities]
y_values = [x.value for x in annualities]

top = max(y_values)

yvals = np.linspace(start=0, stop=top, num=8)

dates = matplotlib.dates.date2num(x_values)

fig = plt.figure()

plt.subplots_adjust(left=0.2, bottom=0.2)
ax = fig.add_subplot()

ax.plot_date(dates, y_values, linestyle='dashed', linewidth=2, color='red')

plt.yticks(yvals)
plt.gca().yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())

start_drawing = False
count = 0
for value in y_values:
    if count == 3:
        break
    if value == top:
        start_drawing = True
    if start_drawing:
        plt.axhline(y=value, linestyle='dashed', color='gray')
        count = count + 1

plt.xlabel('Years', fontsize=12) 
plt.ylabel('Annual vested value', fontsize=12)


fig.savefig('chart.png')