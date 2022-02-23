'''
Author: Laura, Divya, Andrew
Data Set: Electricity and Natural Gas Price Inflation
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#divya's path
df = pd.read_csv("/Users/divyasubramanian/Downloads/Energy_Prices__Dollars_per_Million_Btu__Beginning_1970.csv") #saves the data set in the variable df

#Laura's path
#df = pd.read_csv('C:/Users/liuyu/Downloads/Energy_Prices__Dollars_per_Million_Btu__Beginning_1970.csv')


def prices(column, sector):
    '''stores the prices and the time of the prices'''
    col = df[column]
    sec = df['Sector']
    year = df['Year']
    prices = []
    time = []
    for i in range(col.size):
        if sec[i] == sector:
            prices.append(col[i])
            time.append(year[i])
    return [time, prices]


def main():
    electric = prices('Electricity', 'Commercial')
    natural = prices('Natural Gas', 'Commercial')
    fig, ax = plt.subplots()

    # graphs the cost of electricity
    plt.subplot(2, 1, 1)
    plt.plot(electric[0], electric[1])
    plt.title('Electricity and Natural Gas Commercial Prices') #sets the title of the graph
    plt.ylabel('Electricity Cost') # y axis label for graph

    # graphs the cost of natural gas
    plt.subplot(2, 1, 2)
    plt.plot(natural[0], natural[1])
    plt.ylabel('Natural Gas Cost')# y axis label for graph
    plt.xlabel('Years') # label for x axis (both of the graphs)
    plt.show()

main()
