#!/usr/bin/env python

import datetime

from transaction import Transaction
from annuality import Annuality

class Utils:

    @staticmethod
    def find_vest_transaction(transactions, approx_date):
        tolerance_days = 7
        for transaction in transactions:
            begin_date = transaction.date - datetime.timedelta(days=tolerance_days)
            end_date = transaction.date + datetime.timedelta(days=tolerance_days)
            if approx_date >= begin_date and approx_date <= end_date:
                return transaction
        
        return None


    @staticmethod
    def get_annualities(transactions):
        annual_transactions = []
        for transaction in transactions:
            if (len(annual_transactions) == 0 or annual_transactions[-1].year != transaction.date.year):
                annual_transactions.append(Annuality(transaction.date.year, 0))
            
            annual_transactions[-1].value = annual_transactions[-1].value + transaction.value
        
        return annual_transactions