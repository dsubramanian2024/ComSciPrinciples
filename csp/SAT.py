'''
Author: Divya Subramanian
Data Set: SAT Scores in NY
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/Users/divyasubramanian/Downloads/2012_SAT_Results.csv") #saves the data set in the variable df
#link: https://catalog.data.gov/dataset/sat-results-e88d7

#DROP ALL THAT HAVE 's': df.drop([])
slist = s[]
for i in range(len(df['Num of SAT Test Takers'])):
    if (df['Num of SAT Test Takers'][i] == 's'):
        slist.append(i)
df = df.drop(df.index[slist])

# CHANGE TYPE TO NUMBERS
df["SAT Critical Reading Avg. Score"] = pd.to_numeric(df["SAT Critical Reading Avg. Score"])
df["SAT Math Avg. Score"] = pd.to_numeric(df["SAT Math Avg. Score"])
df["SAT Writing Avg. Score"] = pd.to_numeric(df["SAT Writing Avg. Score"])

#!!!Question: Which School had the highest average sum of the critical reading, writing, and math score?!!!

sum_column = df["SAT Critical Reading Avg. Score"] + df["SAT Math Avg. Score"] + df["SAT Writing Avg. Score"]
df["sum"] = sum_column # contains the sum of the three columns(scores)

maxsum = df["sum"].max() #finds the row with the greatest sum
maxindex = df[df["sum"] == maxsum].index.values # finds row num/index of maxsum
print ("School with highest average total SAT score: ")
print(df["SCHOOL NAME"][maxindex])

#MAKES A GRAPH WITH JUST MATH AND CRITICAL READING; can be made with two factors
fig, ax = plt.subplots()

width = .6
ax.bar(df["SCHOOL NAME"], df["SAT Critical Reading Avg. Score"], width, label = 'Critical Reading')
ax.bar(df["SCHOOL NAME"], df["SAT Math Avg. Score"], width, bottom = df["SAT Critical Reading Avg. Score"], label = 'Math')
#ax.bar(df["SCHOOL NAME"], df["SAT Writing Avg. Score"], width, bottom = df["SAT Math Avg. Score"], label = 'Writing')

ax.set_ylabel('Scores')
ax.set_title('Total Average SAT Score by section and school')
ax.legend()

plt.show()
