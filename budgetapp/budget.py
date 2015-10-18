#!/usr/bin/python

## Params: Gross Monthly Income - Expenses = show theoretical savings

import string

gross = input("What is your Net Monthly Income?:")

expenses=[]

while True:
    expense = raw_input("What are your expenses? type done when done. : ")
    if expense == "done" :
        print("Thanks for the input")
        break
    else:
        expenses.append(expense)

expenses = map(int, expenses)

total = gross - sum(expenses)

print "Here is a total of your expenses: " + str(sum(expenses))

print "Here is how much you have extra for the month: " + str(total)

if total > 0:
    print "You are living within your means"
else:
    print "You are spending too much"