from operator import concat, delitem, index
from sqlite3 import Row
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/paulsilvius/Desktop/FantasyFootball2021Analysis/BleacherReport2021top25ppr.csv')
df['Percentage Of Games Started'] = (df['Games Started']/17)*100
df['2021Rank'] = list(df.index.values + 1)
df.loc[df['Name'].str.split().str.len() == 2, 'LName'] = df['Name'].str.split().str[-1]
df.loc[df['Name'].str.split().str.len() == 3, 'LName'] = df['Name'].str.split().str[-2] + " " +df['Name'].str.split().str[-1]
df['RankPlusName'] = df['2021Rank'].map(str) + '.' + df['LName'].map(str)

ax = df.plot.bar(y='Percentage Of Games Started', x = 'RankPlusName', rot=0)
ax.set_xlabel("2021 Ranking", fontsize = 10)
ax.set_ylabel("Percentage of Games", fontsize = 10)
ax.tick_params(axis='x', labelrotation = 90)

plt.title('2021 Top 25 Ranked PPR Fantasy Football Players Games Started')
plt.tick_params(axis='x', which='major', labelsize=5)
plt.tick_params(axis='y', which='major', labelsize=10)
plt.axis('tight')
plt.grid(axis='y')
print (ax)
#print (df)

plt.show()