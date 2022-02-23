import pandas as pd

#the url: http://www.jaredlander.com/data/Tomato%20First.csv
df = pd.read_csv("http://www.jaredlander.com/data/Tomato%20First.csv")

#print(df)
#print(df.columns)
#print(type(data))

#print(type(1))

#print(df.head(3))

#where can I buy the sweetest tomato?

big = df['Sweet'][0]
num = 0
for x in range (len(df['Sweet'])):
    if (df['Sweet'][x] >= big):
        big = df['Sweet'][x]
        num = x
print(df['Source'][num])
