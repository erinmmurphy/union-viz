import pandas as pd

cfile = pd.read_stata('/Users/erinmurphy/Desktop/Adv Projects in Viz/Final project/Archived project data/state.dta')
cfile.head()

#This is the code I used to create the csv file
cfile.to_csv('/Users/erinmurphy/Desktop/Adv Projects in Viz/Final project/Archived project data/state.csv', index=False)

# only keep years 2008-2022, drop other years
cfile = cfile[cfile['year'].isin([2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])]
cfile.head()

# save to csv
cfile.to_csv('/Users/erinmurphy/Desktop/Adv Projects in Viz/Final project/Archived project data/state2018-22.csv', index=False)
