#Begining of NumEcon project

#Import various exstentions
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#Select data from Nato.int as offline excel document
#Import data
data1 = "data.ny.xlsx"
pd.read_excel(data1,"Ark1")
df1 = pd.read_excel(data1,"Ark1")
print(df1)
#Renaming columns
df1.rename(columns = {'Current prices and exchange rates':'Countries',}, inplace=True)


#Subsetting Countries
df1 = df1.set_index("Countries")

#Remaning the years, due to errors accouring with function variable names as numbers
myDict = {}
for i in range(2010,2018) #Range from the years 2010 to 2017
    myDict[stri(i)] = f"e{i}"
myDict

#Renaming years in dataframe
df1.rename(colmuns = {myDict}, inplace=true)

#Resetting index
df1 = df1.reset_index()

#Switching df from wide to long
df1 = pd.wide_to_long(df1, stubnames = "e", i = "Countries", j = "year")

#Renaming columns
df1 = df1.reset_index()
df1 = df1.rename(columns = {"e":"Million dollars"}, inplace=true)

#Showing defence expenditures of Nato Europe and the United states
#Making individuel columns starting with NATOs Europe countries combined.
NATO_EU = df1.head(1)

df_USA = df1.tail(2)
USA = df_USA.head(1)

year = [2010,2011,2012,2013,2014,2015,2016,2017]

#Showing plot of defence expenditures in plot over the period of time.
plt.plot(year, NATO_EU, "NATO_EU" )
plt.plot(year,USA, "USA")
plt.show()

#Plot above shows the actual spending on military in dollars and cents.
#Next focus will be on, the invidual NATO countries spending on military as a % part of their GNP.

#Import data
data2 = "data.ny.xlsx"
pd.read_excel(data2,"Ark2")
df2 = pd.read_excel(data2,"Ark2")
print(df2)

#Set Countries as a index number
df2 = df2.set_index("Countries")

#Changing names of variables
MyDict2 = {}
for i in range(2010, 2018): 
    MyDict2[str(i)] = f'e{i}'
MyDict2

#Renmaing years
df2.rename(columns = MyDict1, inplace = True)

#Resetting index
df2 = df2.reset_index()

# Changing dataframe from wide to long
df2 = pd.wide_to_long(gdp, stubnames='e', i='Country Code', j='Year')

#renaming columns
df2 = df2.reset_index()
df2.rename(columns = {'e':'Procent of GDP'}, inplace = True)

#Showing Scatterplot for % of GDP used on military
plt(x = "year", y = "Procent of GDP")
plt.xlabel("Year")
plt.ylabel("Procent of GDP")
plt.title("NATO countries use on military expendures as a part of their GDP (2010-2017)")

plt.show()

