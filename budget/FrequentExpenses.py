from . import Expense
import collections
import matplotlib.pyplot as plt

#read in spending data
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

#create a list of spending spending categories
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

#count categories w/ a counter collection
spending_counter = collections.Counter(spending_categories)

#get the top 5 categories
top5 = spending_counter.most_common(5)

#convert the dictionary to 2 lists
categories, count = zip(*top5)

#plot the top 5 most common categories
fig, ax = plt.subplots()

#create the bar chart
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

#display the graph
plt.show()
